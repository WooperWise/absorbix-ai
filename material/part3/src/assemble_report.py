from pathlib import Path
import json,re,zipfile,shutil
B=Path(__file__).resolve().parents[1]
diagrams={d['id']:d for d in json.loads((B/'diagrams/index.json').read_text())}
t='\n\n'.join((B/'src'/f'chapter{i}.md').read_text() for i in range(1,5))
def dsub(m):
 id=m.group(1);d=diagrams[id]; number=int(id.split('_')[0])
 return f'''<a id="diagram-{number:02d}"></a>

**Схема {number:02d}. {d['title']}**

![Схема {number:02d}. {d['title']}](diagrams/{id}.png)

*{d['caption']}* [SVG](diagrams/{id}.svg) · [Mermaid](diagrams/{id}.mmd) · [DOT](diagrams/{id}.dot).

<details>
<summary>Редактируемая схема Mermaid — также сохранена внутри этого Markdown-файла</summary>

```mermaid
{d['mermaid'].strip()}
```

</details>
'''
t=re.sub(r'\[\[DIAGRAM:([^\]]+)\]\]',dsub,t)
def jsub(m):
 return '```json\n'+(B/m.group(1)).read_text().strip()+'\n```'
t=re.sub(r'\[\[JSON:([^\]]+)\]\]',jsub,t)
sources=(B/'sources.md').read_text()
sources=sources.replace('# Источники этапа 3 — проектирование платформы','# Приложение. Аннотированный реестр источников',1)
t+='\n\n<a id="references"></a>\n'+sources
(B/'report_stage3.md').write_text(t,encoding='utf-8')
# Keep the accepted previous report readable, including the images it references.
previous_zip=B.parent/'diploma_stage2_markdown.zip'
if previous_zip.exists():
 with zipfile.ZipFile(previous_zip) as z:
  for info in z.infolist():
   p=Path(info.filename)
   if p.is_absolute() or '..' in p.parts:continue
   if p.parts and p.parts[0] in ['charts','diagrams'] and p.suffix in ['.png','.svg','.dot','.json']:
    target=B/'basis'/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(info))
readme='''# Этап 3: проектирование платформы лекарственных форм

Основной документ: **[report_stage3.md](report_stage3.md)**. Это полный отчёт, а не краткое содержание. Внешний реестр источников также включён в конец основного файла.

## Просмотр

Распакуйте архив целиком, сохраняя папки рядом с report_stage3.md. Обычный Markdown-просмотрщик покажет PNG-схемы. Редактор с Mermaid сможет дополнительно открыть исходный код каждой схемы внутри раскрываемого блока. SVG подходят для увеличения, DOT и MMD — для редактирования. Для просмотра материалов не нужен запущенный сервер.

При скачивании только report_stage3.md текст, таблицы, библиография и встроенный Mermaid-код сохраняются; отдельные PNG/SVG и примеры контрактов находятся в архиве.

## Структура

- `report_stage3.md` — четыре главы и библиография.
- `sources.md`, `sources.json` — аннотированный реестр 47 внешних источников и ссылки на материалы проекта.
- `diagrams/` — 10 схем в PNG/SVG, исходники DOT/MMD и индекс.
- `contracts/` — 5 JSON Schema и ограниченный фрагмент OpenAPI 3.1.2.
- `examples/` — 5 синтетических примеров и искусственная текстовая фикстура; это не данные лекарств.
- `qa/` — фактические результаты проверок комплектности и контрактов, техническая проверка URL при наличии.
- `basis/` — предоставленное ТЗ, реестры этапов 1–2 и принятый отчёт этапа 2 с его изображениями. Источники ранних этапов не представляются как новые независимые исследования.
- `src/` — тексты глав и скрипты сборки. Скрипты определяют корень комплекта относительно собственного размещения.

## Граница проверки

Программная платформа, модели и лабораторные эксперименты не запускались. Проверены синтетические контрактные материалы и комплектность отчёта. `qa/contracts_check.json` перечисляет реально выполненные проверки и их ограничения. Наличие контрольной суммы подтверждает состав файла, а не научную истинность.

## Воспроизведение контрактной проверки

Требуются Python, jsonschema и PyYAML. Запуск: `python src/build_contracts.py`. Для перерисовки схем нужен Graphviz (`dot` и `neato`): `python src/build_diagrams.py`. Для сборки текста: `python src/assemble_report.py`; если рядом с корнем есть исходный архив этапа 2, его изображения копируются дополнительно; готовый комплект уже содержит их в basis/.

Файлы шрифтов, ключи доступа, чужие закрытые документы и полные тексты внешних статей в архив не включены.
'''
(B/'README.md').write_text(readme,encoding='utf-8')
print('Main report:',len(t),'characters;',len(t.split()),'whitespace words;',len(t.encode()),'bytes')
