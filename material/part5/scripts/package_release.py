"""Check top-level Markdown links and package a reproducible release without bytecode."""
from pathlib import Path
import json,hashlib,sys,platform,zipfile,importlib.metadata,re
from urllib.parse import urlsplit,unquote
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1]
issues=[];link_count=0;parser=MarkdownIt()
for name in ['report_stage5.md','sources.md','README.md','DATASET_CARD.md','PROVENANCE_AND_RIGHTS.md']:
 p=R/name;text=p.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',text))
 for block in parser.parse(text):
  for token in block.children or []:
   if token.type not in ['link_open','image']:continue
   target=token.attrGet('href') if token.type=='link_open' else token.attrGet('src')
   if not target:continue
   link_count+=1;u=urlsplit(target)
   if u.scheme in ['http','https','mailto']:continue
   if not u.path:
    if u.fragment and u.fragment not in anchors:issues.append({'file':name,'target':target,'error':'missing anchor'})
   elif not (p.parent/unquote(u.path)).exists():issues.append({'file':name,'target':target,'error':'missing local file'})
qa={'links_checked':link_count,'errors':issues,'scope':'Top-level current Markdown; not availability of external web URLs or dependencies of historical project_basis reports.'}
(R/'qa/link_check.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n')
if issues:raise ValueError(str(issues))
(R/'qa/runtime_environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'jsonschema':importlib.metadata.version('jsonschema'),'validation_date':'2026-10-18','network_download_status':'AqSolDB not acquired; DNS/download restriction'},ensure_ascii=False,indent=2)+'\n')
files=sorted(p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='MANIFEST.json')
manifest={'dataset_version':'1.0.0','release_date':'2026-10-18','hash_algorithm':'sha256','note':'Hashes cover included local artifacts, not original web pages that were only read. Manifest excludes itself.','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(R/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
zip_path=R.parent/'diploma_stage5_dataset.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files+[R/'MANIFEST.json']):z.write(p,arcname='diploma_stage5/'+str(p.relative_to(R)))
with zipfile.ZipFile(zip_path) as z:
 if z.testzip():raise ValueError('ZIP CRC validation failed')
 for f in manifest['files']:
  raw=z.read('diploma_stage5/'+f['path'])
  if hashlib.sha256(raw).hexdigest()!=f['sha256']:raise ValueError('ZIP manifest mismatch')
print(json.dumps({'archive':str(zip_path),'bytes':zip_path.stat().st_size,'files':len(files)+1,'md_links_checked':link_count,'link_errors':len(issues),'zip_crc_and_sha256':'passed'},ensure_ascii=False))
