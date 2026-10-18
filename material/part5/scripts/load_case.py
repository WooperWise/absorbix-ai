"""Build only model-visible context. Never reads reference/ or examples/.
Usage: python scripts/load_case.py --case P5-A01-V01 --output /tmp/input.json
This is an adapter-neutral fixture, not an implementation of the user pipeline.
"""
from pathlib import Path
import argparse,json
R=Path(__file__).resolve().parents[1]
def read_json(path):return json.loads((R/path).read_text(encoding='utf-8'))
def load(case_id:str)->dict:
 cases=[json.loads(s) for s in (R/'data/pipeline/inputs.jsonl').read_text().splitlines() if s]
 matches=[x for x in cases if x['case_id']==case_id]
 if len(matches)!=1:raise ValueError(f'Unknown or duplicate case: {case_id}')
 x=matches[0];cards={c['card_id']:c for c in read_json('evidence/card_index.json')}
 payload={'input':x,'evidence_cards':[],'observations':[],'entities':[],'contexts':[]}
 allowed_root=(R/'evidence/cards').resolve()
 for cid in x['dossier']['card_refs']:
  c=cards[cid];path=(R/c['path']).resolve()
  if not path.is_relative_to(allowed_root):raise ValueError('Card path escapes public evidence directory')
  payload['evidence_cards'].append({'card_id':cid,'source_id':c['source_id'],'content':path.read_text(),'local_sha256':c['local_card_sha256'],'capture_kind':c['capture_kind']})
 obs=[json.loads(s) for s in (R/'evidence/observations/observations.jsonl').read_text().splitlines() if s]
 payload['observations']=[o for o in obs if o['observation_id'] in x['dossier']['observation_refs']]
 entities=read_json('evidence/entities.json');identity=x['case_revision']['identity']
 payload['entities']=[e for e in entities['entities'] if e['entity_id']==identity['molecular_entity_ref']]
 payload['contexts']=[e for e in entities['contexts'] if e['context_id']==identity['product_revision_ref']]
 sids=set(x['case_revision']['source_refs']);payload['source_metadata']=[s for s in read_json('evidence/sources.json') if s['source_id'] in sids]
 payload['test_profile']='Source-supplied decision workflow; not raw document extraction or live web retrieval.'
 return payload
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--output');a=p.parse_args()
 try:
  text=json.dumps(load(a.case),ensure_ascii=False,indent=2)
  if a.output:Path(a.output).write_text(text+'\n',encoding='utf-8')
  else:print(text)
 except (ValueError,KeyError,OSError) as e:p.exit(2,str(e)+'\n')
