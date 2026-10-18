import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from openai import OpenAI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
LOG_LINES: list[str] = []
RESULTS: list[tuple[str, bool]] = []

THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


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

EXTRACTION_PROMPT = (
    "Извлеки из текста структурированные данные и верни строго JSON с ключами "
    '"compound" (МНН препарата), "limiting_factor" (что ограничивает всасывание), '
    '"proposed_strategy" (предлагаемая стратегия). Без пояснений, только JSON.\n\n' + EXTRACTION_TEXT
)


def strip_think(text: str) -> str:
    return THINK_RE.sub("", text).strip()


def main() -> int:
    load_env_file(ROOT / ".env")
    log(f"=== Проверка локальной модели (OpenAI-совместимый API) · {datetime.now().isoformat(timespec='seconds')} ===")
    log(f"openai {__import__('openai').__version__} · python {sys.version.split()[0]}")
    log("")

    base_url = os.environ.get("OPENAI_BASE_URL", "http://localhost:8000/v1")
    model = os.environ.get("LOCAL_MODEL", "")
    log(f"Эндпойнт: {base_url}")
    model_note = model or "не задан, возьмём первый из /v1/models"
    record("переменные окружения", bool(base_url), f"OPENAI_BASE_URL задан, LOCAL_MODEL={model_note}")

    try:
        client = OpenAI(base_url=base_url, api_key=os.environ.get("OPENAI_API_KEY", "dummy"), timeout=120)
        record("создание клиента OpenAI", True, f"base_url={base_url}")
    except Exception as exc:
        record("создание клиента OpenAI", False, f"{type(exc).__name__}: {exc}")
        return finish()

    try:
        ids = [m.id for m in client.models.list().data]
        record("GET /v1/models", len(ids) > 0, f"доступно моделей: {len(ids)}: {', '.join(ids)}")
        if not model:
            model = ids[0] if ids else ""
    except Exception as exc:
        record("GET /v1/models", False, f"{type(exc).__name__}: {exc}")

    if not model:
        log("Модель не определена, продолжать некуда")
        return finish()
    log(f"Модель для smoke-теста: {model}")
    log("")

    extra_body = {"chat_template_kwargs": {"enable_thinking": False}}
    prompt = "Ответь по-русски одним коротким предложением: подтвердите, что генеративный вызов работает."
    try:
        t0 = time.perf_counter()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            extra_body=extra_body,
        )
        latency = (time.perf_counter() - t0) * 1000
        content = strip_think(resp.choices[0].message.content or "")
        usage = resp.usage
        tokens = f", токены: prompt={usage.prompt_tokens}, completion={usage.completion_tokens}" if usage else ""
        record("chat.completions.create", bool(content), f"{latency:.0f} мс{tokens}, ответ: {content[:120]}")
    except Exception as exc:
        record("chat.completions.create", False, f"{type(exc).__name__}: {exc}")

    try:
        t0 = time.perf_counter()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": EXTRACTION_PROMPT}],
            response_format={
                "type": "json_schema",
                "json_schema": {"name": "Extraction", "schema": Extraction.model_json_schema(), "strict": True},
            },
            extra_body=extra_body,
        )
        latency = (time.perf_counter() - t0) * 1000
        content = strip_think(resp.choices[0].message.content or "")
        parsed = Extraction.model_validate_json(content)
        record("structured output (json_schema)", True, f"{latency:.0f} мс, схема соблюдена")
        log("Извлечено: " + parsed.model_dump_json(ensure_ascii=False))
    except Exception as exc:
        record("structured output (json_schema)", False, f"{type(exc).__name__}: {exc}")

    return finish()


def finish() -> int:
    log("")
    passed = sum(1 for _, ok in RESULTS if ok)
    log(f"Итог: {passed}/{len(RESULTS)} проверок пройдено")
    log_dir = Path(os.environ.get("LOG_DIR", ROOT / "material" / "part4" / "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    out = log_dir / f"check_local_model_{datetime.now().date().isoformat()}.log"
    out.write_text("\n".join(LOG_LINES) + "\n", encoding="utf-8")
    print(f"Лог сохранён: {out}")
    return 0 if passed == len(RESULTS) and RESULTS else 1


if __name__ == "__main__":
    raise SystemExit(main())
