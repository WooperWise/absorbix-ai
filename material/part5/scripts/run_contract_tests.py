"""Reference fixture logic only. Does not exercise the user's adapters or a medical model."""
from pathlib import Path
import json,math
R=Path(__file__).resolve().parents[1]
def execute(op,x):
 if op=='convert_units':
  scale={('%','1'):0.01,('1','%'):100,('mg/mL','g/L'):1,('mg/mL','ug/mL'):1000}
  key=(x['unit'],x['target_unit'])
  if key not in scale:raise ValueError('Unsupported conversion; no guessing')
  return {'value':x['value']*scale[key],'unit':x['target_unit']}
 if op=='concentration':
  if x['mass_unit']!='mg' or x['volume_unit']!='mL' or x['volume']<=0:raise ValueError('Unsupported units/volume')
  return {'value':x['mass']/x['volume'],'unit':'mg/mL'}
 if op=='normalize_unknown':return {'amount':x['excipient_amount'],'status':'unknown' if x['excipient_amount'] is None else 'known'}
 if op=='compare_context':
  pairs=[('endpoint_a','endpoint_b'),('form_a','form_b'),('dose_a_mg','dose_b_mg')]
  return {'merge_allowed':all(x[a]==x[b] for a,b in pairs if a in x and b in x)}
 if op=='normalize_uncertainty':return {'type':x['reported_type'],'ci95':None}
 if op=='route_guard':return {'status':'out_of_domain' if x['route']!='oral' else 'requires_full_domain_check'}
 if op=='scope_guard':return {'status':'out_of_domain' if x['molecule_class']!='small_molecule' else 'requires_full_domain_check'}
 if op=='source_failure':return {'status':'technical_failure','no_evidence_found':None}
 if op=='evidence_origin':return {'is_measurement':x['origin'] in ['reported_measurement','partner_measurement']}
 if op=='IID_guard':return {'verdict':'insufficient_context','approved_recipe':False}
 if op=='FAERS_guard':return {'incidence':None,'causality_established':False}
 if op=='access_guard':return {'call_allowed':bool(x['external_processing_allowed'])}
 raise ValueError('Unknown operation '+op)
def equal(a,b):
 if isinstance(a,dict):return set(a)==set(b) and all(equal(a[k],b[k]) for k in a)
 if isinstance(a,float) and isinstance(b,(int,float)):return math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12)
 return a==b
rows=json.loads((R/'data/tools/contract_tests.json').read_text());out=[]
for row in rows:
 actual=execute(row['operation'],row['input']);out.append({'test_id':row['test_id'],'actual':actual,'passed':equal(actual,row['expected'])})
report={'kind':'reference_fixture_logic_not_user_pipeline','total':len(out),'passed':sum(x['passed'] for x in out),'results':out}
(R/'qa/reference_contract_test_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['passed'], '/', report['total']);assert all(x['passed'] for x in out)
