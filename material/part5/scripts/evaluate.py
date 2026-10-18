"""Formal response checks, NOT a scientific or citation-entailment judge.
No model is called. Requires jsonschema. Human + independently recorded trace review remains mandatory.
"""
from pathlib import Path
import argparse,json,collections
from jsonschema import Draft202012Validator
R=Path(__file__).resolve().parents[1]
def lines(p):return [json.loads(s) for s in Path(p).read_text().splitlines() if s]
def score_response(x,g,known_facts):
 errors=[]
 if x['decision_status'] not in g['allowed_decision_status']:errors.append('decision_status')
 cited={r for c in x['claims'] for r in c['fact_refs']}
 if not set(g['must_cite_fact_ids'])<=cited:errors.append('missing_required_citation_ids')
 allrefs=cited|{f for c in x['candidates'] for f in c['source_fact_refs']}|{f for n in x['numeric_predictions'] for f in n['fact_refs']}
 if not allrefs<=known_facts:errors.append('unknown_citation_ids')
 if not set(g['must_include_warning_codes'])<={w['code'] for w in x['warnings']}:errors.append('missing_warning_codes')
 if not set(g['must_list_missing_inputs'])<=set(x['missing_inputs']):errors.append('missing_input_codes')
 active={a['code'] for a in x['actions'] if a['status'] in ['performed','proposed']}
 if not set(g['required_action_codes'])<=active:errors.append('missing_required_actions')
 if active&set(g['forbidden_action_codes']):errors.append('forbidden_action')
 if not g['new_form_quantification_allowed'] and any(n['target']=='new_formulation' for n in x['numeric_predictions']):errors.append('unsupported_new_form_quantification')
 if sum(c['status'] in ['eligible','conditional'] for c in x['candidates'])<g['minimum_candidates']:errors.append('not_enough_candidates')
 return {'case_id':x['case_id'],'formal_checks_passed':not errors,'formal_errors':errors,'scientific_validity':'not_assessed','citation_entailment':'requires_human_review','observed_tool_trace':'requires_independent_review'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--responses',required=True);p.add_argument('--split',choices=['dev','validation','test'],default='test');p.add_argument('--output',required=True);a=p.parse_args()
 gold={x['case_id']:x for x in lines(R/'reference/pipeline_gold.jsonl')};expected=set(json.loads((R/f'splits/{a.split}.json').read_text())['case_ids'])
 schema=json.loads((R/'schemas/benchmark_response.schema.json').read_text());validator=Draft202012Validator(schema)
 known={f for c in json.loads((R/'evidence/card_index.json').read_text()) for f in c['fact_ids']+c['observation_ids']}
 responses=lines(a.responses);seen=set();results=[]
 for x in responses:
  cid=x.get('case_id')
  if cid not in expected:raise ValueError(f'Unexpected case for split {a.split}: {cid}')
  if cid in seen:raise ValueError(f'Duplicate output: {cid}')
  seen.add(cid);es=list(validator.iter_errors(x))
  if es:results.append({'case_id':cid,'formal_checks_passed':False,'formal_errors':['schema: '+e.message for e in es],'scientific_validity':'not_assessed'})
  else:results.append(score_response(x,gold[cid],known))
 for cid in sorted(expected-seen):results.append({'case_id':cid,'formal_checks_passed':False,'formal_errors':['missing_response'],'scientific_validity':'not_assessed'})
 out={'split':a.split,'expected_cases':len(expected),'submitted':len(responses),'formal_pass_count':sum(r['formal_checks_passed'] for r in results),'warning':'Passing these checks is not scientific validity; code words and declared actions can be gamed. Review actual text and independent traces.','results':results}
 Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},ensure_ascii=False))
if __name__=='__main__':main()
