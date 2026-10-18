"""Render the static stage-5 report with counts/examples from generated files."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[1]
def j(p):return json.loads((R/p).read_text())
def jl(p):return [json.loads(x) for x in (R/p).read_text().splitlines() if x]
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(str(c).replace('|','\\|').replace('\n',' ') for c in row)+' |' for row in rows])
S=j('evidence/sources.json');A=j('reference/anchor_design.json');I=jl('reference/case_index.jsonl');stats=j('qa/dataset_statistics.json');Q=j('qa/validation_report.json')
for s in S:
 if s['source_id']=='L08':s['type']='manufacturer_medical_information';s['access_level']='manufacturer_page_read';s['limitations']+=' Это медицинская информационная страница производителя, а не полный текст инструкции.'
(R/'evidence/sources.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n')
sourceparts=[]
for s in S:
 date=s['publication_or_revision'] or 'Не установлена / динамический ресурс'
 sourceparts.append(f'''<a id="{s['source_id']}"></a>
## {s['source_id']}. {s['title']}

**Прямая ссылка:** [{s['url']}]({s['url']})  
**Дата публикации / редакции:** {date}. **Обращение:** {s['accessed_on']}.  
**Тип:** `{s['type']}`. **Просмотрено:** `{s['access_level']}`.  
**Локатор:** {s.get('locator') or 'См. соответствующее описание ресурса и выбранные карточки.'}  
**Права:** {s.get('license') or 'Универсальная лицензия не установлена; источник не перепечатан целиком.'}

**Ограничение:** {s['limitations']}
''')
sources='\n'.join(sourceparts)
(R/'sources.md').write_text('# Источники этапа 5\n\nДата проверки: 18.10.2026. Позиции не равны независимым исследованиям.\n\n'+sources)
body=(R/'scripts/report_body.md').read_text()
body=body.replace('{{ANCHOR_TABLE}}',table(['ID / вещество','Предметный контекст','Профиль','Источник'],[[a['anchor_id']+' — '+a['molecule'],a['topic'],'ядро' if a['scope']=='core' else 'граница расширения',f"[{a['source_id']}](#{a['source_id']})"] for a in A]))
body=body.replace('{{SPLIT_TABLE}}',table(['Выборка','Контексты','Кейсы'],[[s,', '.join(j('splits/'+s+'.json')['leakage_groups']),len(j('splits/'+s+'.json')['case_ids'])] for s in ['dev','validation','test']]))
body=body.replace('{{COUNTS_TABLE}}',table(['Составляющая','Количество','Статус'],[
 ['Сценарии основного процесса',160,'Синтетические запросы на реальных ограниченных основаниях'],['Контексты/семейства',20,'Отобраны целевым образом, не случайная выборка рынка'],['Пероральное ядро',136,'17 контекстов × 8 сценариев'],['Границы расширений',24,'3 контекста × 8 сценариев'],['Реальные опубликованные пары',75,'Перенос Table S1 с флагами качества'],['Контрактные фикстуры',24,'Синтетические проверки логики, не эксперименты'],['Численные наблюдения',12,'Выборочные сведения и производные единиц'],['Предметные карточки',20,'Кураторские парафразы'],['Общие карточки правил',4,'IID, openFDA, M9, архитектура'],['Примеры согласования',12,'Вход и критерии; не слепой режим'],['Позиций источников',len(S),'Разные типы; D05/D06 — один источник']]))
inputs=jl('data/pipeline/inputs.jsonl');gold=jl('reference/pipeline_gold.jsonl');obs=jl('evidence/observations/observations.jsonl')
block=lambda x:'```json\n'+json.dumps(x,ensure_ascii=False,indent=2)+'\n```'
body=body.replace('{{EXAMPLE_INPUT}}',block(inputs[0])).replace('{{EXAMPLE_OBSERVATION}}',block(obs[0])).replace('{{EXAMPLE_GOLD}}',block(next(x for x in gold if x['case_id']=='P5-A02-V03')))
body=body.replace('{{QA_TABLE}}',table(['Проверка','Результат','Интерпретация'],[['Проверки структуры, ссылок и оценщика',f"{Q['checks_passed']}/{Q['checks_run']}",'Проверка артефактов'],['Эталонная логика контрактных фикстур','24/24','Тесты приложенного кода, не вашего инструмента'],['Независимое экспертное согласование','Не выполнено','Все рубрики draft'],['Прогон пользовательского пайплайна','Не выполнен','Репозиторий не предоставлялся'],['Загрузка полного AqSolDB','Не состоялась','Основные данные независимы от неё']]))
body=body.replace('{{SOURCES}}',sources)
assert '{{' not in body
(R/'report_stage5.md').write_text(body,encoding='utf-8')
(R/'qa/report_statistics.json').write_text(json.dumps({'utf8_bytes':len(body.encode()),'words_whitespace':len(body.split()),'lines':len(body.splitlines()),'chapter_count':len(re.findall(r'^# Глава ',body,re.M))},ensure_ascii=False,indent=2)+'\n')
print(len(body.split()),'words;',len(body.encode()),'bytes')
