from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests, json, sys, datetime
B=Path(__file__).resolve().parents[1]
sources=json.loads((B/'sources.json').read_text())
a=int(sys.argv[1]) if len(sys.argv)>1 else 0
b=int(sys.argv[2]) if len(sys.argv)>2 else len(sources)
def check(s):
 out={'id':s['id'],'requested_url':s['url'],'method':'GET (streamed; not a full-content verification)','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=requests.get(s['url'],timeout=(6,12),allow_redirects=True,stream=True)
  out.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('content-type'))
  if 200 <= r.status_code < 300:out['interpretation']='transport_accessible; does not prove full text, correctness, currency or API readiness'
  elif r.status_code in [401,403,429]:out['interpretation']='restricted_or_rate_limited; not proof that the reference is invalid'
  else:out['interpretation']='http_non_success; compare with official browser/document access record'
  r.close()
 except Exception as e:out.update(error=type(e).__name__+': '+str(e)[:240],interpretation='network_check_failed; does not establish absence of source')
 return out
results=[]
with ThreadPoolExecutor(max_workers=8) as ex:
 for fut in as_completed([ex.submit(check,s) for s in sources[a:b]]):results.append(fut.result())
p=B/'qa/link_audit.json'
prev=json.loads(p.read_text()).get('checks',[]) if p.exists() else []
byid={r['id']:r for r in prev+results}
payload={'purpose':'Дополнительная транспортная проверка основных URL реестра. Содержательная проверка первоисточников описана отдельно в sources.md. HTTP 200 не равен успешной научной проверке; блокировка GET не доказывает несуществование страницы.','checks':sorted(byid.values(),key=lambda x:x['id'])}
p.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
for r in sorted(results,key=lambda x:x['id']):print(r['id'],r.get('http_status',r.get('error','unknown')))
