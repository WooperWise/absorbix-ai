from pathlib import Path
from markdown_it import MarkdownIt
from urllib.parse import unquote,urlsplit
from PIL import Image
from bs4 import BeautifulSoup
import re,json,hashlib,collections
B=Path(__file__).resolve().parents[1]
text=(B/'report_stage3.md').read_text()
checks=[]
def record(name,passed,details=None):checks.append({'check':name,'passed':bool(passed),'details':details})
chapters=re.findall(r'^# Глава [1-4]\. .+$',text,re.M)
record('four_main_chapters',len(chapters)==4,chapters)
passports=re.findall(r'^### 4\.2\.(\d+)\. M(\d+) ',text,re.M)
record('nineteen_module_passports',len(passports)==19 and [int(x[1]) for x in passports]==list(range(1,20)),passports)
record('no_unexpanded_placeholders',not re.search(r'\[\[(DIAGRAM|JSON):',text))
record('no_raw_chat_citation_markup','' not in text and 'turn951906' not in text)
anchors=set(re.findall(r'<a id="([^"]+)"',text))
md=MarkdownIt('commonmark',{'html':True}).enable('table')
tokens=md.parse(text)
links=[]
def walk(tokens):
 for token in tokens:
  if token.type=='link_open':links.append(token.attrGet('href'))
  if token.type=='image':links.append(token.attrGet('src'))
  if token.children:walk(token.children)
walk(tokens)
missing=[];badanchors=[];external=[]
for href in links:
 u=urlsplit(href)
 if u.scheme in ['http','https']:external.append(href);continue
 if u.scheme:continue
 if not u.path:
  if u.fragment and unquote(u.fragment) not in anchors:badanchors.append(href)
 else:
  target=B/unquote(u.path)
  if not target.exists():missing.append(href)
record('all_local_files_exist',not missing,sorted(set(missing)))
record('all_explicit_anchors_exist',not badanchors,sorted(set(badanchors)))
diagrams=json.loads((B/'diagrams/index.json').read_text())
record('ten_project_diagrams',len(diagrams)==10)
images=[]
for d in diagrams:
 files=[B/'diagrams'/(d['id']+'.'+e) for e in ['png','svg','dot','mmd']]
 okay=all(p.exists() and p.stat().st_size for p in files)
 with Image.open(files[0]) as im:
  im.verify()
 with Image.open(files[0]) as im:images.append({'name':d['id'],'width':im.width,'height':im.height})
 record('diagram_assets_'+d['id'],okay)
# Bibliography coverage: every external entry is referenced before the bibliography.
body=text.split('<a id="references"></a>')[0]
registered=json.loads((B/'sources.json').read_text())
uncited=[s['id'] for s in registered if ('#'+s['id']+')') not in body]
record('all_registered_sources_used',not uncited,uncited)
parsed_links=set(external)
record('all_primary_source_urls_present',all(s['url'] in parsed_links for s in registered))
contract_check=json.loads((B/'qa/contracts_check.json').read_text())
record('contract_checks_passed',contract_check['all_passed'],contract_check['test_count'])
# Render for local structural inspection; not a requested user output.
html='<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Stage 3 QA</title><style>body{max-width:1100px;margin:32px auto;font:16px/1.6 sans-serif}img{max-width:100%;height:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border:1px solid #bbb;padding:8px;vertical-align:top}pre{white-space:pre-wrap}details{margin:12px 0}</style></head><body>'+md.render(text)+'</body></html>'
soup=BeautifulSoup(html,'html.parser')
for tag in soup.find_all(['a','img']):
 key='href' if tag.name=='a' else 'src'
 val=tag.get(key)
 if val and not urlsplit(val).scheme and urlsplit(val).path: tag[key]='../'+val
(B/'qa/rendered_structure.html').write_text(str(soup),encoding='utf-8')
# Parent directory differs in QA HTML, so it is a structure check, not portable render.
report={'all_passed':all(c['passed'] for c in checks),'checks':checks,'main_report_bytes':len(text.encode()),'main_report_words_whitespace':len(text.split()),'main_body_words_whitespace':len(body.split()),'tables':sum(t.type=='table_open' for t in tokens),'mermaid_blocks':sum(t.type=='fence' and t.info.strip()=='mermaid' for t in tokens),'external_primary_sources':len(registered),'unique_external_urls_in_report':len(set(external)),'diagram_dimensions':images,'limitations':['Не выполнен запуск серверной платформы или научных моделей.','Проверка локальных ссылок не означает проверки научного содержания каждого источника.']}
(B/'qa/package_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ['all_passed','main_report_bytes','main_report_words_whitespace','main_body_words_whitespace','tables','mermaid_blocks','external_primary_sources']},ensure_ascii=False,indent=2))
for c in checks:
 if not c['passed']:print('FAILED',c)
if not report['all_passed']:raise SystemExit(1)
