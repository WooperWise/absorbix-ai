"""Offline structural/integrity checks. Does not validate drug science or user repository."""
from pathlib import Path
import json,hashlib,collections,sys,copy
from jsonschema import Draft202012Validator,FormatChecker
from load_case import load
from evaluate import score_response
R=Path(__file__).resolve().parents[1]
def j(p):return json.loads((R/p).read_text())
def jl(p):return [json.loads(s) for s in (R/p).read_text().splitlines() if s]
errors=[];checks=[]
def check(name,condition):
 checks.append({'check':name,'passed':bool(condition)})
 if not condition:errors.append(name)
I=jl('data/pipeline/inputs.jsonl');G=jl('reference/pipeline_gold.jsonl');idx=jl('reference/case_index.jsonl');O=jl('evidence/observations/observations.jsonl');C=j('evidence/card_index.json');S=j('evidence/sources.json');real=jl('data/tools/formulationde_public75.jsonl')
check('160 main cases',len(I)==160);check('20 unique groups',len({x['leakage_group'] for x in idx})==20);check('160 unique IDs',len({x['case_id'] for x in I})==160);check('gold exact IDs',{x['case_id'] for x in I}=={x['case_id'] for x in G});check('JSON and JSONL equal',j('data/pipeline/inputs.json')==I)
for name,values in [('pipeline_input.schema.json',I),('stage3/observation.schema.json',O)]:
 schema=j('schemas/'+name);Draft202012Validator.check_schema(schema);val=Draft202012Validator(schema,format_checker=FormatChecker());errs=[(v.get('case_id',v.get('observation_id')),e.message) for v in values for e in val.iter_errors(v)];check(name+' validation',not errs)
 errors.extend(map(str,errs))
facts={f for c in C for f in c['fact_ids']+c['observation_ids']};sources={s['source_id'] for s in S};cards={c['card_id']:c for c in C};obsids={o['observation_id'] for o in O}
check('all source_refs resolve',all(set(x['case_revision']['source_refs'])<=sources for x in I))
check('all card_refs resolve',all(set(x['dossier']['card_refs'])<=set(cards) for x in I))
check('all observation_refs resolve',all(set(x['dossier']['observation_refs'])<=obsids for x in I))
check('all gold fact refs resolve',all(set(x['must_cite_fact_ids']+x['anchor_fact_refs'])<=facts for x in G))
for c in C:
 p=R/c['path'];check('card hash '+c['card_id'],p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==c['local_card_sha256'])
for o in O:
 p=R/cards[o['source_snapshot_ref']]['path'];text=p.read_text().splitlines();loc=o['evidence_locator'];a,b=loc['start_line'],loc['end_line'];check('observation locator '+o['observation_id'],1<=a<=b<=len(text) and o['observation_id'] in '\n'.join(text[a-1:b]))
splits=[j('splits/'+s+'.json') for s in ['dev','validation','test']]
check('splits cover all cases',set.union(*(set(s['case_ids']) for s in splits))=={x['case_id'] for x in I})
check('no group overlap',all(not set(a['leakage_groups'])&set(b['leakage_groups']) for i,a in enumerate(splits) for b in splits[i+1:]))
check('all cases explicitly synthetic',all(x['case_revision']['data_kind']=='synthetic_fixture' for x in I))
check('all oracles draft',all(x['oracle_status']=='draft_for_expert_review' for x in G))
check('75 public rows and 59/16 labels',len(real)==75 and collections.Counter(x['label_original'] for x in real)=={0:59,1:16})
check('preserve row72 role flag',real[71]['api_name_raw']=='Tenofovir disoproxil fumarate' and real[71]['second_component_name_raw']=='Lamivudine' and not real[71]['use_for_excipient_only_subset'])
check('24 contract tests',len(j('data/tools/contract_tests.json'))==24)
check('loader excludes gold/example keys',all('draft_oracle' not in json.dumps(load(x['case_id'])) and 'oracle_status' not in json.dumps(load(x['case_id'])) for x in I))
# These are evaluator tests created directly from gold. They are NOT outputs from an AI.
g=G[0];synthetic={'case_id':g['case_id'],'decision_status':g['allowed_decision_status'][0],'claims':[{'text':'Synthetic scorer unit test, not science.','fact_refs':g['must_cite_fact_ids'],'origin_kind':'source_fact'}],'warnings':[{'code':c,'message':'unit test'} for c in g['must_include_warning_codes']],'missing_inputs':g['must_list_missing_inputs'],'actions':[{'code':c,'status':'performed'} for c in g['required_action_codes']],'candidates':[{'title':'unit test','status':'conditional','rationale':'unit test','source_fact_refs':[],'next_check':'unit test'} for _ in range(g['minimum_candidates'])],'numeric_predictions':[]}
check('scorer accepts matching formal fixture only',score_response(synthetic,g,facts)['formal_checks_passed'])
bad=copy.deepcopy(synthetic);bad['numeric_predictions']=[{'endpoint':'AUC','value':2,'unit':'1','target':'new_formulation','fact_refs':[]}];check('scorer rejects fabricated new-form number','unsupported_new_form_quantification' in score_response(bad,g,facts)['formal_errors'])
bad=copy.deepcopy(synthetic);bad['warnings']=[];check('scorer detects missing warnings','missing_warning_codes' in score_response(bad,g,facts)['formal_errors'])
out={'validation_kind':'offline_artifact_integrity_and_scorer_unit_tests','checks_run':len(checks),'checks_passed':sum(c['passed'] for c in checks),'errors':errors,'checks':checks,'not_tested':['actual_user_repository','actual_LLM_answers','scientific_expert_agreement','external_API_success','clinical_or_laboratory_effect']}
(R/'qa/validation_report.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='checks'},ensure_ascii=False));sys.exit(bool(errors))
