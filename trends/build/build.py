import json, sys, os, datetime
sys.path.insert(0, os.path.dirname(__file__))
from items_hw import HW; from items_mk import MK; from items_pq import PQ; from items_sw import SW
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cats=[("hardware","hw",HW),("market","mk",MK),("pqc","pq",PQ),("software","sw",SW)]
GI=json.load(open(os.path.join(os.path.dirname(__file__),"github_issues.json")))
recs=[]; seen=set()
for cat,pfx,items in cats:
    items=sorted(items,key=lambda x:x[0],reverse=True)
    for i,(d,t,pub,url,ko,en,tags,ents,imp) in enumerate(items,1):
        assert url not in seen, url; seen.add(url)
        prec={4:"year",7:"month",10:"day"}[len(d)]
        recs.append(dict(id=f"{pfx}-{i:03d}",category=cat,title=t,source=pub,date=d,date_precision=prec,url=url,
            summary_ko=ko,summary_en=en,tags=tags,entities=ents,importance=imp,added="2026-10-18"))
        if url in GI: recs[-1]["github_issue"]=GI[url]
with open(os.path.join(ROOT,"index.jsonl"),"w",encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r,ensure_ascii=False)+"\n")
with open(os.path.join(ROOT,"index.json"),"w",encoding="utf-8") as f: json.dump(recs,f,ensure_ascii=False,indent=1)
TK=json.load(open(os.path.join(os.path.dirname(__file__),"takeaways.json")))
names={"hardware":"1. 양자컴퓨팅 하드웨어·연구 돌파구","market":"2. 기업·투자·시장 동향 (정부 프로그램 포함)","pqc":"3. 양자내성암호(PQC)·보안","software":"4. 양자 소프트웨어·알고리즘·클라우드"}
L=["# 양자 기술 동향 인덱스","",f"_최종 업데이트: 2026-10-18 (KST) · 기간: 대략 2025-10 ~ 2026-10 (일부 '참고 항목'은 기준 문서로 그 이전 포함) · 총 {len(recs)}건_","",
   "> ⭐ = 중요도(1~5). 주요 항목은 GitHub 이슈(litkhai/notes-on-quantum)로도 기록됨. 날짜가 `YYYY-MM` 또는 `YYYY`인 항목은 출처에서 정확한 일자를 확인하지 못한 경우입니다. 원본 데이터: `index.jsonl`","",
   "## 목차"]+[f"- [{names[c]}](#{c}) ({sum(1 for r in recs if r['category']==c)}건)" for c,_,_ in cats]+[""]
for c,_,_ in cats:
    L+=[f'<a id="{c}"></a>',f"## {names[c]}","","### 핵심 시사점"]+[f"- {x}" for x in TK[c]]+["","### 항목 (최신순)"]
    for r in [r for r in recs if r["category"]==c]:
        first=r["summary_ko"].split(". ")[0].rstrip(".")+"."
        L.append(f"- **{r['date']}** [{r['title']}]({r['url']}) — {r['source']} {'⭐'*r['importance']}"+(f" · [이슈 #{r['github_issue'].rsplit('/',1)[1]}]({r['github_issue']})" if r.get('github_issue') else "")+f"  \n  {first}")
    L.append("")
md="\n".join(L)
open(os.path.join(ROOT,"INDEX.md"),"w",encoding="utf-8").write(md)
for c,_,_ in cats: print(c,sum(1 for r in recs if r['category']==c))
print("total",len(recs))
