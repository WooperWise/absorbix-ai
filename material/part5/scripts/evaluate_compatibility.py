"""Score author-label agreement for the public challenge; abstentions are reported separately."""
from pathlib import Path
import argparse,json
R=Path(__file__).resolve().parents[1]
def jl(p):return [json.loads(s) for s in Path(p).read_text().splitlines() if s]
def main():
 p=argparse.ArgumentParser();p.add_argument('--predictions',required=True);p.add_argument('--subset',choices=['published75','excipient_role_screened74','visually_checked_excipient65'],default='published75');p.add_argument('--output',required=True);a=p.parse_args()
 ids=set(json.loads((R/'splits/compatibility_subsets.json').read_text())[a.subset]);gold={x['record_id']:x['label_original'] for x in jl(R/'reference/compatibility_labels.jsonl')};pred={}
 for x in jl(a.predictions):
  cid=x['record_id'];v=x['predicted_label']
  if cid in pred or cid not in gold:raise ValueError('Duplicate or unknown ID: '+cid)
  if v not in [0,1,None]:raise ValueError('Label must be 0,1 or null')
  pred[cid]=v
 if not ids<=set(pred):raise ValueError('Missing predictions must be explicit abstentions: '+str(sorted(ids-set(pred))))
 covered=[c for c in ids if pred[c] is not None];tp=sum(gold[c]==1 and pred[c]==1 for c in covered);tn=sum(gold[c]==0 and pred[c]==0 for c in covered);fp=sum(gold[c]==0 and pred[c]==1 for c in covered);fn=sum(gold[c]==1 and pred[c]==0 for c in covered)
 div=lambda x,y:x/y if y else None
 out={'subset':a.subset,'n':len(ids),'covered':len(covered),'coverage':div(len(covered),len(ids)),'tp':tp,'tn':tn,'fp':fp,'fn':fn,'accuracy_on_answered':div(tp+tn,len(covered)),'correct_fraction_of_all':div(tp+tn,len(ids)),'precision_on_answered':div(tp,tp+fp),'recall_on_answered':div(tp,tp+fn),'positive_detection_all':div(tp,sum(gold[c]==1 for c in ids)),'F1_on_answered':div(2*tp,2*tp+fp+fn),'warning':'Agreement with published labels, not universal compatibility; report abstention and scope together.'}
 Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':main()
