"""Optional real-data acquisition. Not required to run the supplied 160/75/24 tests.
Network acquisition was NOT successfully executed in the author's environment.
"""
from pathlib import Path
import argparse,urllib.request,csv,io,json,hashlib,datetime
URL='https://raw.githubusercontent.com/mcsorkun/AqSolDB/master/results/data_curated.csv'
def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--expected-rows',type=int,default=9982);a=p.parse_args();out=Path(a.out)
 if out.exists():p.error('Refusing to overwrite existing data. Choose a new snapshot directory.')
 req=urllib.request.Request(URL,headers={'User-Agent':'pharma-diploma-dataset-acquisition/1.0'})
 try:
  with urllib.request.urlopen(req,timeout=30) as r:
   raw=r.read(50_000_001);headers=dict(r.headers)
  if len(raw)>50_000_000:raise ValueError('Unexpectedly large response')
  rows=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
  if len(rows)!=a.expected_rows:raise ValueError(f'Expected {a.expected_rows} rows, got {len(rows)}; inspect upstream version before accepting')
  if not rows or not {'SMILES','Solubility','SD','Occurrences'}<=set(rows[0]):raise ValueError('Unexpected schema')
  out.mkdir(parents=True);(out/'data_curated.csv').write_bytes(raw)
  manifest={'url':URL,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(rows),'upstream_ref':'master (not pinned to immutable commit)','response_headers':headers,'data_license_url':'https://github.com/mcsorkun/AqSolDB/blob/master/data/LICENSE','data_license':'CC0-1.0','limitations':['Not formulation-level data.','Freeze this snapshot before use.','SD=0 is not universally zero measurement uncertainty.','This script does not assign BCS or interpret safety.']}
  (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');print(json.dumps(manifest,ensure_ascii=False,indent=2))
 except Exception as e:p.exit(2,'Acquisition failed; no valid snapshot claimed: '+str(e)+'\n')
if __name__=='__main__':main()
