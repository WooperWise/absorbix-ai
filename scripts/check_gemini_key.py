import os
import sys
import time
from datetime import datetime
from importlib.metadata import version
from pathlib import Path

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
LOG_LINES: list[str] = []
RESULTS: list[tuple[str, bool]] = []


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def log(message: str = "") -> None:
    print(message, flush=True)
    LOG_LINES.append(message)


def record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok))
    log(f"[{'OK' if ok else 'FAIL'}] {name}: {detail}")


class Extraction(BaseModel):
    compound: str = Field(description="МНН препарата")
    limiting_factor: str = Field(description="Что ограничивает всасывание")
    proposed_strategy: str = Field(description="Предлагаемая стратегия оптимизации")


EXTRACTION_TEXT = (
    "Итраконазол — слабое основание с крайне низкой растворимостью при физиологическом pH. "
    "Ограничивающий фактор всасывания — растворимость. Для повышения биодоступности предлагается "
    "твёрдая аморфная дисперсия на полимере HPMC."
)

NON_TEXT_MARKERS = ("embedding", "imagen", "veo", "tts", "aqa", "image", "audio", "live", "learnlm")


def pick_model(names: list[str]) -> str | None:
    for marker in ("flash-lite", "flash"):
        for name in names:
            if marker in name:
                return name
    return names[0] if names else None


def main() -> int:
    load_env_file(ROOT / ".env")
    log(f"=== Проверка ключа Google AI Studio · {datetime.now().isoformat(timespec='seconds')} ===")
    pyd = __import__("pydantic").VERSION
    log(f"google-genai {version('google-genai')} · pydantic {pyd} · python {sys.version.split()[0]}")
    log("")

    api_key = os.environ.get("GEMINI_API_KEY", "")
    prefix = "AIza" if api_key.startswith("AIza") else api_key[:4] + " (не AIza)"
    record("ключ в .env", len(api_key) >= 30, f"длина {len(api_key)}, префикс {prefix}")
    if not api_key:
        log("Ключ не найден: заполните GEMINI_API_KEY в .env (см. .env.example)")
        return finish()

    try:
        client = genai.Client(api_key=api_key)
        record("создание клиента genai.Client", True, "без исключений")
    except Exception as exc:
        record("создание клиента genai.Client", False, f"{type(exc).__name__}: {exc}")
        return finish()

    names: list[str] = []
    try:
        for m in client.models.list():
            model_name = m.name or ""
            short = model_name.removeprefix("models/")
            if "gemini" not in short:
                continue
            if any(marker in short for marker in NON_TEXT_MARKERS):
                continue
            methods = getattr(m, "supported_generation_methods", None) or []
            if methods and "generateContent" not in methods:
                continue
            names.append(short)
        record("listModels", len(names) > 0, f"доступно текстовых gemini-моделей: {len(names)}")
        log("Модели: " + (", ".join(sorted(names)) if names else "—"))
    except Exception as exc:
        record("listModels", False, f"{type(exc).__name__}: {exc}")

    model_id = pick_model(names)
    if not model_id:
        log("Нет подходящей модели для вызова generateContent")
        return finish()
    log(f"Модель для smoke-теста: {model_id}")
    log("")

    prompt = "Ответь по-русски одним коротким предложением: подтвердите, что генеративный вызов работает."
    try:
        t0 = time.perf_counter()
        resp = client.models.generate_content(model=model_id, contents=prompt)
        latency = (time.perf_counter() - t0) * 1000
        text = (resp.text or "").strip().replace("\n", " ")
        usage = getattr(resp, "usage_metadata", None)
        tokens = ""
        if usage:
            tokens = f", токены: prompt={usage.prompt_token_count}, output={usage.candidates_token_count}"
        record("generateContent", bool(text), f"{latency:.0f} мс{tokens}, ответ: {text[:120]}")
    except Exception as exc:
        record("generateContent", False, f"{type(exc).__name__}: {exc}")

    try:
        t0 = time.perf_counter()
        resp = client.models.generate_content(
            model=model_id,
            contents=EXTRACTION_TEXT,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=Extraction,
            ),
        )
        latency = (time.perf_counter() - t0) * 1000
        parsed = getattr(resp, "parsed", None)
        if isinstance(parsed, Extraction):
            record("structured output (response_schema)", True, f"{latency:.0f} мс, схема соблюдена")
            log("Извлечено: " + parsed.model_dump_json(ensure_ascii=False))
        else:
            raw = (resp.text or "").strip().replace("\n", " ")
            detail = f"parsed не является Extraction; сырой ответ: {raw[:200]}"
            record("structured output (response_schema)", False, detail)
    except Exception as exc:
        record("structured output (response_schema)", False, f"{type(exc).__name__}: {exc}")

    return finish()


def finish() -> int:
    log("")
    passed = sum(1 for _, ok in RESULTS if ok)
    log(f"Итог: {passed}/{len(RESULTS)} проверок пройдено")
    log_dir = Path(os.environ.get("LOG_DIR", ROOT / "material" / "part4" / "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    out = log_dir / f"check_gemini_key_{datetime.now().date().isoformat()}.log"
    out.write_text("\n".join(LOG_LINES) + "\n", encoding="utf-8")
    print(f"Лог сохранён: {out}")
    return 0 if passed == len(RESULTS) and RESULTS else 1


if __name__ == "__main__":
    raise SystemExit(main())
