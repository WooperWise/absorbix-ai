from pathlib import Path
import json, hashlib, copy
from jsonschema import Draft202012Validator, FormatChecker
import yaml
B=Path(__file__).resolve().parents[1]
def dump(p,obj): p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def obj(props,required=None,**more):
 return dict(type='object',properties=props,required=list(props) if required is None else required,additionalProperties=False,**more)
def text(**kw):return dict(type='string',minLength=1,**kw)
def nullable_text():return {'type':['string','null'],'minLength':1}
def array(items,minItems=0):return dict(type='array',items=items,minItems=minItems)
def enum(*values):return dict(type='string',enum=list(values))
def schema(name,body):return {'$schema':'https://json-schema.org/draft/2020-12/schema','$id':f'urn:pharma-diploma:{name}:1.0.0','title':name,**body}
version={'const':'1.0.0'}
refs=array(text())
dose=obj({'status':enum('known','unknown','not_applicable'),'amount':{'type':['number','null'],'exclusiveMinimum':0},'unit':nullable_text(),'basis':nullable_text()})
dose['allOf']=[{'if':{'properties':{'status':{'const':'known'}}},'then':{'properties':{'amount':{'type':'number'},'unit':text(),'basis':text()}},'else':{'properties':{'amount':{'type':'null'},'unit':{'type':'null'},'basis':{'type':'null'}}}}]
case=schema('case-revision',obj({
 'schema_version':version,'case_id':text(),'case_revision_id':text(),'workspace_id':text(),
 'data_kind':enum('research','synthetic_fixture'),
 'analysis_intent':enum('increase_exposure','target_release_profile','bioequivalence_screen','stability','manufacturability','exploratory'),
 'route':enum('oral','intravenous','intramuscular','subcutaneous','other','unknown'),
 'population':obj({'status':enum('defined','unknown'),'description':nullable_text()}),
 'identity':obj({'status':enum('resolved','molecule_only','ambiguous','unresolved'),'molecular_entity_ref':nullable_text(),'substance_form_ref':nullable_text(),'product_revision_ref':nullable_text()}),
 'composition_completeness':enum('complete_quantitative','qualitative_only','partial','unknown'),
 'dose':dose,
 'requirements':array(obj({'id':text(),'level':enum('hard','preference'),'statement':text(),'origin_ref':text()})),
 'external_processing_allowed':{'type':'boolean'},'source_refs':refs,'created_at':{'type':'string','format':'date-time'}
}))
value={'oneOf':[
 obj({'kind':{'const':'numeric'},'number':{'type':'number'},'unit':text()}),
 obj({'kind':{'const':'interval'},'lower':{'type':'number'},'upper':{'type':'number'},'unit':text()}),
 obj({'kind':{'const':'censored'},'operator':enum('<','<=','>','>='),'bound':{'type':'number'},'unit':text()}),
 obj({'kind':{'const':'categorical'},'category':text()}),
 obj({'kind':{'const':'not_reported'},'reason':text()})
]}
obs=schema('observation',obj({
 'schema_version':version,'observation_id':text(),'workspace_id':text(),'subject_ref':text(),
 'endpoint':text(),'origin_kind':enum('reported_measurement','partner_measurement','deterministic_calculation','ml_prediction','mechanistic_simulation','expert_judgment','synthetic_fixture'),
 'value':value,'quantity_basis':text(),
 'conditions':obj({'pH':{'type':'number'},'temperature':obj({'value':{'type':'number'},'unit':{'const':'Cel'}}),'medium':text(),'duration_description':text()},required=[]),
 'method_description':text(),'source_snapshot_ref':text(),
 'evidence_locator':obj({'kind':{'const':'line_range'},'start_line':{'type':'integer','minimum':1},'end_line':{'type':'integer','minimum':1}}),
 'original_value_text':text(),'review_status':enum('draft','checked','rejected'),
 'limitations':refs,'created_at':{'type':'string','format':'date-time'}
}))
result=schema('module-result',obj({
 'schema_version':version,'module_id':{'type':'string','pattern':'^M(0[1-9]|1[0-9])$'},
 'workspace_id':text(),'case_revision_id':text(),'run_id':text(),
 'execution_status':enum('succeeded','partial','blocked','failed'),
 'scientific_status':enum('supported','uncertain','predicted','undetermined','out_of_domain','not_applicable'),
 'input_refs':refs,'output_refs':refs,'evidence_refs':refs,
 'warnings':array(obj({'code':text(),'message':text(),'severity':enum('info','warning','critical')})),
 'missing_inputs':refs,
 'tool_versions':{'type':'object','additionalProperties':text()},'policy_version':text(),
 'created_at':{'type':'string','format':'date-time'},'content_hash':{'type':'string','pattern':'^[a-f0-9]{64}$'}
}))
result['allOf']=[{'if':{'properties':{'execution_status':{'enum':['succeeded','partial']}}},'then':{'properties':{'output_refs':{'minItems':1}}}},
 {'if':{'properties':{'scientific_status':{'const':'supported'}}},'then':{'properties':{'evidence_refs':{'minItems':1}}}}]
model=schema('model-use-assessment',obj({
 'schema_version':version,'assessment_id':text(),'workspace_id':text(),'case_revision_id':text(),
 'model_ref':text(),'model_version':text(),'question_of_interest':text(),'context_of_use':text(),
 'role':enum('screening','ranking','quantitative_prediction','scenario_exploration'),
 'model_influence':text(),'consequence_of_wrong_decision':text(),'risk_rationale':text(),
 'input_domain_description':text(),'evaluation_criteria':array(text(),minItems=1),
 'validation_evidence_refs':refs,'limitations':refs,
 'decision':enum('not_assessed','insufficient','outside_scope','fit_for_context'),
 'reviewer_ref':nullable_text(),'created_at':{'type':'string','format':'date-time'}
}))
model['allOf']=[{'if':{'properties':{'decision':{'const':'fit_for_context'}}},'then':{'properties':{'validation_evidence_refs':{'minItems':1},'reviewer_ref':text()}}}]
candidate=schema('candidate-assessment',obj({
 'schema_version':version,'assessment_id':text(),'workspace_id':text(),'case_revision_id':text(),
 'candidate_revision_id':text(),'strategy_definition_ref':text(),
 'checks':array(obj({'check_id':text(),'rule_kind':enum('user_requirement','regulatory_context','precedent_screen','model_flag','formulation_evidence'),'rule_ref':text(),'constraint_level':enum('hard','advisory'),'verdict':enum('met','violated','unknown','not_applicable'),'rationale':text(),'evidence_refs':refs})),
 'eligibility':enum('eligible_for_review','conditional','ineligible','insufficient_data'),
 'expected_effect':obj({'endpoint':text(),'status':enum('not_quantified','quantified_prediction','observed_comparison'),'description':text(),'basis_refs':refs}),
 'next_checks':refs,'created_at':{'type':'string','format':'date-time'}
}))
schemas={'case_revision':case,'observation':obs,'module_result':result,'model_use_assessment':model,'candidate_assessment':candidate}
for name,s in schemas.items():
 Draft202012Validator.check_schema(s)
 dump(B/'contracts'/f'{name}.schema.json',s)
t='2026-10-18T00:00:00Z'
case_example={
 'schema_version':'1.0.0','case_id':'CASE-DEMO-001','case_revision_id':'CASE-DEMO-001-R1','workspace_id':'WS-DEMO',
 'data_kind':'synthetic_fixture','analysis_intent':'exploratory','route':'oral',
 'population':{'status':'unknown','description':None},
 'identity':{'status':'molecule_only','molecular_entity_ref':'MOLECULE-FIXTURE-001','substance_form_ref':None,'product_revision_ref':None},
 'composition_completeness':'unknown','dose':{'status':'unknown','amount':None,'unit':None,'basis':None},
 'requirements':[{'id':'REQ-DEMO-001','level':'hard','statement':'Не передавать тестовый кейс внешним сервисам.','origin_ref':'fixture-user-input'}],
 'external_processing_allowed':False,'source_refs':['SNAPSHOT-FIXTURE-001'],'created_at':t}
fixture='''СИНТЕТИЧЕСКАЯ ТЕСТОВАЯ ФИКСТУРА. Это не научный источник и не результат эксперимента.\nДля условного образца MOLECULE-FIXTURE-001 задано тестовое значение: 1.25 mg/mL при pH 2.0 и 25 Cel.\nСреда: условная тестовая среда. Метод: искусственно созданная запись для проверки структуры данных.\nВсе значения придуманы исключительно для проверки контракта; фармакологическая интерпретация запрещена.\n'''
(B/'examples/fixture_source.txt').write_text(fixture,encoding='utf-8')
obs_example={'schema_version':'1.0.0','observation_id':'OBS-FIXTURE-001','workspace_id':'WS-DEMO','subject_ref':'MOLECULE-FIXTURE-001','endpoint':'fixture.solubility','origin_kind':'synthetic_fixture','value':{'kind':'numeric','number':1.25,'unit':'mg/mL'},'quantity_basis':'Условное вещество фикстуры; не лекарственный продукт.','conditions':{'pH':2.0,'temperature':{'value':25.0,'unit':'Cel'},'medium':'Условная тестовая среда'},'method_description':'Синтетический контрактный пример; физическое измерение не проводилось.','source_snapshot_ref':'SNAPSHOT-FIXTURE-001','evidence_locator':{'kind':'line_range','start_line':1,'end_line':4},'original_value_text':'1.25 mg/mL при pH 2.0 и 25 Cel','review_status':'draft','limitations':['Используется только в тестах; не включать в исследовательский корпус.'],'created_at':t}
res_example={'schema_version':'1.0.0','module_id':'M09','workspace_id':'WS-DEMO','case_revision_id':'CASE-DEMO-001-R1','run_id':'RUN-FIXTURE-001','execution_status':'partial','scientific_status':'undetermined','input_refs':['CASE-DEMO-001-R1'],'output_refs':['ASSESSMENT-FIXTURE-001'],'evidence_refs':[], 'warnings':[{'code':'composition_unknown','message':'Количественный состав и конкретный продукт не определены.','severity':'warning'}],'missing_inputs':['product_revision_ref','quantitative_composition','dose'],'tool_versions':{'fixture_generator':'1.0.0'},'policy_version':'fixture-policy-1','created_at':t}
res_example['content_hash']=hashlib.sha256(json.dumps(res_example,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
model_example={'schema_version':'1.0.0','assessment_id':'MODEL-ASSESSMENT-FIXTURE-001','workspace_id':'WS-DEMO','case_revision_id':'CASE-DEMO-001-R1','model_ref':'MODEL-FIXTURE-NOT-EXECUTED','model_version':'not-selected','question_of_interest':'Достаточно ли данных для количественного сравнения экспозиций?','context_of_use':'Контрактная демонстрация отказа при отсутствии продуктового контекста.','role':'quantitative_prediction','model_influence':'Количественный результат мог бы изменить выбор кандидата.','consequence_of_wrong_decision':'Выбор неподходящего направления разработки.','risk_rationale':'Нет данных о продукте, дозе и конкретной оценённой модели.','input_domain_description':'Не установлена: модель не выбрана.','evaluation_criteria':['До расчёта должны быть заданы модель, контекст, входы и план проверки.'],'validation_evidence_refs':[],'limitations':['Это синтетический пример; расчёт не запускался.'],'decision':'insufficient','reviewer_ref':None,'created_at':t}
cand_example={'schema_version':'1.0.0','assessment_id':'ASSESSMENT-FIXTURE-001','workspace_id':'WS-DEMO','case_revision_id':'CASE-DEMO-001-R1','candidate_revision_id':'CANDIDATE-FIXTURE-R1','strategy_definition_ref':'STRATEGY-FIXTURE-R1','checks':[{'check_id':'CHECK-COMPOSITION','rule_kind':'formulation_evidence','rule_ref':'fixture-rule-composition-required','constraint_level':'advisory','verdict':'unknown','rationale':'Отсутствуют конкретный продукт и количества компонентов.','evidence_refs':[]}],'eligibility':'insufficient_data','expected_effect':{'endpoint':'exposure_change','status':'not_quantified','description':'Оценка величины изменения не выполнялась.','basis_refs':[]},'next_checks':['Определить продукт, дозу и количественный состав.'],'created_at':t}
examples={'case_revision':case_example,'observation':obs_example,'module_result':res_example,'model_use_assessment':model_example,'candidate_assessment':cand_example}
checker=FormatChecker()
checks=[]
for name,e in examples.items():
 Draft202012Validator(schemas[name],format_checker=checker).validate(e)
 dump(B/'examples'/f'{name}.example.json',e)
 checks.append({'test':'positive_'+name,'expected':'valid','passed':True})
def negative(name,label,fn):
 x=copy.deepcopy(examples[name]);fn(x)
 errors=list(Draft202012Validator(schemas[name],format_checker=checker).iter_errors(x))
 if not errors:raise AssertionError('Negative not caught: '+label)
 checks.append({'test':label,'expected':'rejected','passed':True,'detected_at':[list(e.path) for e in errors[:3]]})
negative('case_revision','missing_workspace',lambda x:x.pop('workspace_id'))
negative('case_revision','unknown_dose_is_not_zero',lambda x:x['dose'].update(amount=0))
negative('case_revision','known_dose_requires_basis',lambda x:x['dose'].update(status='known',amount=1,unit='mg',basis=None))
negative('case_revision','external_processing_boolean_required',lambda x:x.update(external_processing_allowed='true'))
negative('observation','observation_requires_provenance',lambda x:x.pop('source_snapshot_ref'))
negative('observation','measurement_value_must_be_typed',lambda x:x['value'].update(number='1.25'))
negative('observation','zero_line_locator_rejected',lambda x:x['evidence_locator'].update(start_line=0))
negative('module_result','invented_scientific_status_rejected',lambda x:x.update(scientific_status='clinically_proven'))
negative('module_result','successful_output_not_empty',lambda x:x.update(execution_status='succeeded',output_refs=[]))
negative('module_result','supported_requires_evidence',lambda x:x.update(scientific_status='supported',evidence_refs=[]))
negative('module_result','invalid_date_rejected',lambda x:x.update(created_at='not-a-date'))
negative('model_use_assessment','fit_requires_evidence_and_reviewer',lambda x:x.update(decision='fit_for_context'))
negative('candidate_assessment','universal_safety_status_rejected',lambda x:x.update(eligibility='FDA_approved_safe'))
# Small cross-field rules demonstrate boundaries beyond JSON Schema.
def semantics(name,x):
 if name=='observation':
  if x['evidence_locator']['start_line']>x['evidence_locator']['end_line']:raise ValueError('Reversed line interval')
  if x['source_snapshot_ref'].startswith('SNAPSHOT-FIXTURE') and x['origin_kind']!='synthetic_fixture':raise ValueError('Synthetic source mislabeled as research')
  if x['value']['kind']=='interval' and x['value']['lower']>x['value']['upper']:raise ValueError('Reversed numeric interval')
 if name=='candidate_assessment':
  if any(c['verdict']=='violated' and c['rule_kind']=='user_requirement' and c['constraint_level']=='hard' for c in x['checks']) and x['eligibility']=='eligible_for_review':raise ValueError('Hard requirement violation cannot be silently eligible')
for label,fn in [
 ('reversed_evidence_lines',lambda x:x['evidence_locator'].update(start_line=4,end_line=1)),
 ('fixture_is_not_a_real_measurement',lambda x:x.update(origin_kind='reported_measurement')),
 ('reversed_numeric_interval',lambda x:x.update(value={'kind':'interval','lower':2,'upper':1,'unit':'mg/mL'}))]:
 x=copy.deepcopy(obs_example);fn(x)
 Draft202012Validator(obs,format_checker=checker).validate(x)
 try: semantics('observation',x)
 except ValueError:checks.append({'test':label,'expected':'semantic_rejection','passed':True})
 else:raise AssertionError(label)
# Fragment: only the async run boundary, not a complete production API.
openapi={
 'openapi':'3.1.2',
 'info':{'title':'Diploma formulation platform — design contract fragment','version':'0.1.0','description':'Проектный фрагмент: запуск и чтение анализа. Не развёрнутая служба и не полный API.'},
 'paths':{
  '/v1/case-revisions/{revision_id}/runs':{'post':{
   'operationId':'startAnalysisRun','description':'Workspace устанавливается по проверенной сессии. Повтор ключа с другим телом отклоняется.',
   'parameters':[{'name':'revision_id','in':'path','required':True,'schema':{'type':'string'}},{'name':'Idempotency-Key','in':'header','required':True,'schema':{'type':'string','minLength':1}}],
   'requestBody':{'required':True,'content':{'application/json':{'schema':{'$ref':'#/components/schemas/RunRequest'}}}},
   'responses':{'202':{'description':'Задание принято; результат ещё не получен.','content':{'application/json':{'schema':{'$ref':'#/components/schemas/RunStatus'}}}},'403':{'$ref':'#/components/responses/Problem'},'409':{'$ref':'#/components/responses/Problem'},'422':{'$ref':'#/components/responses/Problem'}}}},
  '/v1/runs/{run_id}':{'get':{'operationId':'getAnalysisRun','parameters':[{'name':'run_id','in':'path','required':True,'schema':{'type':'string'}}],'responses':{'200':{'description':'Техническое состояние и ссылки на доступные результаты.','content':{'application/json':{'schema':{'$ref':'#/components/schemas/RunStatus'}}}},'403':{'$ref':'#/components/responses/Problem'},'404':{'$ref':'#/components/responses/Problem'}}}}
 },
 'components':{
  'schemas':{
   'RunRequest':obj({'workflow_profile':text(),'budget_profile':text()}),
   'RunStatus':obj({'run_id':text(),'case_revision_id':text(),'status':enum('created','queued','running','waiting_input','retry_scheduled','needs_reconciliation','succeeded','partial','failed','cancelled'),'result_refs':refs}),
   'Problem':obj({'type':{'type':'string','format':'uri-reference'},'title':text(),'status':{'type':'integer','minimum':100,'maximum':599},'detail':text(),'instance':{'type':'string','format':'uri-reference'}},required=['type','title','status'])
  },
  'responses':{'Problem':{'description':'Ошибка в формате RFC 9457; частные данные и секреты не включаются.','content':{'application/problem+json':{'schema':{'$ref':'#/components/schemas/Problem'}}}}}
 },
 'x-deployment-security-note':'Механизм аутентификации выбирается при интеграции с платформой компании; отсутствие securitySchemes в данном фрагменте не означает публичный неаутентифицированный API.'
}
(B/'contracts/openapi.fragment.yaml').write_text(yaml.safe_dump(openapi,allow_unicode=True,sort_keys=False),encoding='utf-8')
# Check YAML round-trip and local JSON pointers. This is not a full OpenAPI conformance test.
loaded=yaml.safe_load((B/'contracts/openapi.fragment.yaml').read_text())
def walk(x):
 if isinstance(x,dict):
  if '$ref' in x:
   ref=x['$ref']; assert ref.startswith('#/')
   cur=loaded
   for k in ref[2:].split('/'):cur=cur[k.replace('~1','/').replace('~0','~')]
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(loaded)
checks.append({'test':'openapi_yaml_and_local_references','expected':'parse_and_resolve','passed':True,'limitation':'Не выполнена полная проверка сторонним OpenAPI-валидатором; runtime API отсутствует.'})
report={'schema_count':len(schemas),'positive_examples':len(examples),'checks':checks,'test_count':len(checks),'all_passed':all(c['passed'] for c in checks),'limitations':['Проверены структура контрактов, фикстуры и несколько предметных инвариантов, не весь будущий продукт.','UCUM-конверсия, HTTP runtime, многопользовательский доступ, модели, файлы внешних источников и научная пригодность не тестировались.','Синтетические значения не имеют фармакологического смысла.']}
dump(B/'qa/contracts_check.json',report)
(B/'examples/README.md').write_text('''# Синтетические примеры контрактов\n\nВсе пять JSON-примеров — искусственные тестовые данные. Препарат, продукт, исследование и вычислительная модель за ними не стоят. Число 1.25 в observation.example.json создано только для проверки типов и связи с локальной фикстурой. Его нельзя использовать как физико-химическое свойство.\n\n`module_result.example.json` демонстрирует частичную проверку состава при неизвестных продукте и дозе. `model_use_assessment.example.json` показывает отказ от количественной оценки, а не проведённую симуляцию.\n\n`content_hash` в примере ModuleResult — SHA-256 канонической JSON-сериализации оболочки без самого поля content_hash (ключи сортируются, разделители `,` и `:`, UTF-8). В реальном продукте алгоритм канонизации должен быть закреплён контрактом; данный способ не объявляется внешним стандартом канонического JSON.\n''',encoding='utf-8')
print(json.dumps({'schemas':len(schemas),'examples':len(examples),'tests':len(checks),'all_passed':report['all_passed']},ensure_ascii=False))
