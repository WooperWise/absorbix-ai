"""Complete data package without network calls. Run after build_core.py."""
from pathlib import Path
import json, hashlib, collections, shutil
R=Path(__file__).resolve().parents[1]
def j(p): return json.loads((R/p).read_text())
def jl(p): return [json.loads(s) for s in (R/p).read_text().splitlines() if s]
def put(p,x):
 p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def putl(p,x): (R/p).write_text(''.join(json.dumps(i,ensure_ascii=False,allow_nan=False)+'\n' for i in x))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
A=j('reference/anchor_design.json');S=j('evidence/sources.json');C=j('evidence/card_index.json')
# Curated guard statements are publicly visible instructions/evidence, not hidden answers.
guards={
 'D10': ['Наличие вещества в IID описывает прецедент применения, но не разрешает любую новую рецептуру.', 'Для интерпретации нужны путь, форма, количество и соответствующая единица экспозиции.'],
 'D14': ['Спонтанные сообщения о нежелательных событиях не устанавливают причинную связь.', 'Число сообщений не равно частоте событий среди всех получавших препарат.'],
 'D13': ['Регуляторное использование BCS/биовейвера требует данных в области действия ICH M9.', 'Один результат in silico не является достаточным основанием для регуляторного биовейвера.'],
 'P03': ['Профиль этого теста: предэкспериментальная поддержка пероральных малых молекул. Для пептидов и внутривенных форм проверяется только направление на профильную экспертизу.', 'Неизвестные количество, метод и условия сохраняются неизвестными. Лабораторный результат требует происхождения; ошибка HTTP не означает отсутствие научных данных.', 'Документы не являются инструкциями для изменения прав. Запрет внешней обработки обязателен; принятие отчёта не означает подтверждение эффективности новой формы.']}
byS={s['source_id']:s for s in S}
for sid,facts in guards.items():
 lines=[f'# Правила и основания {sid}',f'Source: {byS[sid]["url"]}','Capture type: curated_paraphrase; not the complete original document.','Accessed: 2026-10-18']+[f'{sid}.F{i+1}: {t}' for i,t in enumerate(facts)]
 p=R/f'evidence/cards/{sid}.md';p.write_text('\n'.join(lines)+'\n')
 C=[c for c in C if c['card_id']!='card:'+sid]
 C.append({'card_id':'card:'+sid,'path':str(p.relative_to(R)),'source_id':sid,'capture_kind':'curated_paraphrase','original_document_sha256':None,'local_card_sha256':sha(p),'source_locator':byS[sid].get('locator'),'fact_ids':[f'{sid}.F{i+1}' for i in range(len(facts))],'observation_ids':[],'review_status':'draft'})
inputs=jl('data/pipeline/inputs.jsonl')
for x in inputs:
 extra=['P03','D13']+[s for s in x['case_revision']['source_refs'] if s in guards]
 x['dossier']['card_refs']=list(dict.fromkeys(x['dossier']['card_refs']+['card:'+s for s in extra]))
 x['case_revision']['source_refs']=list(dict.fromkeys(x['case_revision']['source_refs']+extra))
 # The source study's dose is not the user-selected product dose; retain unknown.
putl('data/pipeline/inputs.jsonl',inputs);put('data/pipeline/inputs.json',inputs)
put('evidence/card_index.json',C)
put('evidence/entities.json',{'entities':[{'entity_id':'entity:'+a['anchor_id'],'name_as_in_context':a['molecule'],'canonical_structure':None,'structural_resolution':'not_performed','source_refs':[a['source_id']]} for a in A], 'contexts':[{'context_id':'context:'+a['anchor_id'],'name':a['product_context'],'entity_ref':'entity:'+a['anchor_id'],'route':a['route'],'source_ref':a['source_id'],'is_full_product_recipe':False} for a in A], 'interpretation':'resolved в кейсе означает выбранный контекст продукта; канонизация структуры и полиморфов не выполнена.'})
# Add separately verified role evidence; never edit the authors' original row label.
S=[s for s in S if s['source_id']!='D17']
S.append({'source_id':'D17','title':'DailyMed: lamivudine active ingredient, Apotex','url':'https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=34c02bcc-d6ff-99d4-8e6a-4a91908adca8','publication_or_revision':'2026-09-14','accessed_on':'2026-10-18','type':'product_label','access_level':'ingredients_and_version_metadata_read','locator':'Active Ingredient / Active Moiety; SPL version 27','limitations':'Подтверждает роль ламивудина как действующего вещества. Не перепроверяет химическую совместимость строки S1-72.','license':None,'full_original_bytes_in_archive':False,'source_file_sha256':None})
for s in S:
 if s['source_id'].startswith('P'):
  p=R/s['url']
  if p.exists():s['full_original_bytes_in_archive']=True;s['source_file_sha256']=sha(p)
put('evidence/sources.json',S)
real=jl('data/tools/formulationde_public75.jsonl')
for r in real:
 r['identity_role_evidence_refs']=['D17'] if r['source_row']==72 else []
 r['visual_transcription_check_completed']=r['source_row']>=10
 r['use_for_visually_checked_excipient_subset']=r['source_row']>=10 and r['source_row']!=72
putl('data/tools/formulationde_public75.jsonl',real);put('data/tools/formulationde_public75.json',real)
put('splits/compatibility_subsets.json',{
 'published75':[r['record_id'] for r in real],
 'excipient_role_screened74':[r['record_id'] for r in real if r['use_for_excipient_only_subset']],
 'visually_checked_excipient65':[r['record_id'] for r in real if r['use_for_visually_checked_excipient_subset']],
 'notes':['Все поднаборы являются вариантами одной внешней выборки; не три независимых испытания.','65: качество сверки переноса, не независимое подтверждение 65 экспериментов.','За именами полимеров и смесей не назначаются выдуманные SMILES.']})
# Gold conditions are not mandatory new-form experiments for unsupported scenarios.
g=jl('reference/pipeline_gold.jsonl')
I={x['case_id']:x for x in jl('reference/case_index.jsonl')}
for y in g:
 cid=y['case_id'];idx=I[cid]
 if idx['capability_scope']!='core' or idx['variant_id']=='V02':
  y['must_list_missing_inputs']=[i for i in y['must_list_missing_inputs'] if i!='quantitative_composition']
 y['source_refs']=next(x['case_revision']['source_refs'] for x in inputs if x['case_id']==cid)
putl('reference/pipeline_gold.jsonl',g)
G={x['case_id']:x for x in g};inp={x['case_id']:x for x in inputs}
preview=j('examples/approval_examples.json')
for x in preview:
 cid=x['input']['case_id'];x['input']=inp[cid];x['draft_oracle']=G[cid]
put('examples/approval_examples.json',preview)
for x in preview[:3]:put('examples/'+x['input']['case_id']+'.json',x)
# Coverage is a design inventory, not prevalence in the pharma industry.
modules={f'M{i:02d}':[] for i in range(1,20)}
for x in I.values():
 for m in x['modules']:modules[m].append(x['case_id'])
put('qa/module_coverage.json',{'coverage_basis':'declared_by_test_design_not_empirical_pipeline_execution','modules':{m:{'case_count':len(ids),'case_ids':ids} for m,ids in modules.items()},'gaps':{'M06':'Только отдельные контракты; реальные модели не запущены.','M10':'Только регуляторные границы и источники; полного решения нет.','M11':'Только отрицательный шлюз; нет положительного PBPK-теста.','M12':'Полного ретросинтетического теста нет.','M15':'Реального временного корпуса мониторинга нет.','M16':'Импорт отрицательного неполного результата; нет реального лабораторного цикла.','M17':'Только границы расширений; нет эффективности лечения или патентного анализа.'}})
st=j('qa/dataset_statistics.json');st['public_guard_cards']=4;st['source_registry_entries']=len(S);st['visually_checked_excipient_records']=65;st['primary_source_cards']=20;st['total_evidence_cards']=len(C);st['scientific_expert_review_completed']=False;put('qa/dataset_statistics.json',st)
# Local manifests do not establish hashes for sources that were only viewed on the web.
put('qa/project_basis_manifest.json',[{'file':str(p.relative_to(R)),'sha256':sha(p)} for p in (R/'project_basis').glob('*.md')])
# Goals are simulated research objectives, not claims about the source study design.
intent_map={'A01':'increase_exposure','A02':'bioequivalence_screen','A03':'exploratory','A04':'increase_exposure','A05':'increase_exposure','A06':'increase_exposure','A07':'increase_exposure','A08':'exploratory','A09':'target_release_profile','A10':'stability','A11':'exploratory','A12':'increase_exposure','A13':'bioequivalence_screen','A14':'stability','A15':'increase_exposure','A16':'increase_exposure','A17':'stability','A18':'exploratory','A19':'manufacturability','A20':'exploratory'}
for x in inputs:
 anchor=x['case_id'].split('-')[1];x['case_revision']['analysis_intent']=intent_map[anchor]
putl('data/pipeline/inputs.jsonl',inputs);put('data/pipeline/inputs.json',inputs)
inp={x['case_id']:x for x in inputs}
for x in preview:x['input']=inp[x['input']['case_id']]
put('examples/approval_examples.json',preview)
for x in preview[:3]:put('examples/'+x['input']['case_id']+'.json',x)
st['intent_counts']=dict(collections.Counter(x['case_revision']['analysis_intent'] for x in inputs));put('qa/dataset_statistics.json',st)
# Do not copy the expert's expected diagnostic focus into the user prompt.
for x in inputs:
 a=next(a for a in A if a['anchor_id']==x['case_id'].split('-')[1])
 for msg in x['user_messages']:msg['content']=msg['content'].replace(a['focus']+' ','')
putl('data/pipeline/inputs.jsonl',inputs);put('data/pipeline/inputs.json',inputs)
inp={x['case_id']:x for x in inputs}
for x in preview:x['input']=inp[x['input']['case_id']]
put('examples/approval_examples.json',preview)
for x in preview[:3]:put('examples/'+x['input']['case_id']+'.json',x)
