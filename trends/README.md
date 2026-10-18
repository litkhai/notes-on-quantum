# quantum-index — 양자 기술 동향 인덱스

이 저장소의 `trends/`에 둔 양자 기술 4개 분야 동향 인덱스. 최초 구축: 2026-10-18 (KST).
문서 사이트(`docs/`)와는 별도이며, MkDocs 내비게이션에는 넣지 않는다.

## 변경 이력
- 2026-10-18 오전: 최초 구축(102건), 주요 항목 GitHub 이슈 #14–#22 기록.
- 2026-10-18 업데이트 패스: 최근 2주(10/4–10/18) 신규 25건 추가(하드웨어 2·시장 7·PQC 6·소프트웨어 10) → 총 127건. 신규 이슈 #24(PQC 정부 시한)·#25(Oratomic)·#26(구글 모듈형 쌍곡 코드), `software` 라벨 생성.

## 파일 구조
| 파일 | 설명 |
|---|---|
| `index.jsonl` | **원본 데이터(정본)**. 한 줄 = 한 항목(JSON). |
| `index.json` | 같은 데이터의 JSON 배열 버전(가독성용, `index.jsonl`에서 재생성). |
| `INDEX.md` | 한국어 인덱스. 분야별 핵심 시사점 + 최신순 링크 목록. |
| `README.md` | 이 문서. |
| `build/` | 생성 스크립트(`build.py`)와 항목 소스(`items_*.py`, `takeaways.json`). |

## 레코드 스키마
```json
{"id":"hw-001","category":"hardware|market|pqc|software","title":"...","source":"출처/발행처",
 "date":"YYYY-MM-DD | YYYY-MM | YYYY","date_precision":"day|month|year","url":"https://...",
 "summary_ko":"2~3문장 한국어 요약","summary_en":"1문장 영어 요약","tags":["..."],
 "entities":["회사/기관"],"importance":1-5,"added":"YYYY-MM-DD(인덱스 추가일)"}
```
- 카테고리: `hardware`(하드웨어·연구), `market`(기업·투자·정부 프로그램), `pqc`(양자내성암호·보안), `software`(SDK·알고리즘·클라우드)
- id 접두어: hw / mk / pq / sw. id는 빌드 시 카테고리 내 최신순으로 매겨지므로 **영구 키는 `url`**입니다.
- 중요도: 5=분야 판도 변화, 4=주요, 3=주목할 만함, 2=참고, 1=배경.
- 날짜는 출처에서 확인된 정밀도까지만 기록(추정 금지). '참고 항목'(기준 문서)은 12개월 이전일 수 있음.

## 업데이트 방법 (향후 정기 실행용)
1. 새 자료 조사: WebSearch/WebFetch, X `search_news`(max_age_hours ≤ 720) 등. **실제로 확인한 출처의 URL·날짜·수치만** 기록.
2. **중복 제거 기준 = `url`** (정규화: 끝 슬래시·추적 파라미터 제거 후 비교). 이미 있는 URL이면 추가하지 않고, 내용이 바뀌었으면 해당 레코드만 갱신.
   같은 사건의 다른 매체 기사는 가능하면 1차 출처(보도자료·논문) 하나만 유지.
3. (GitHub 이슈) 주요 항목을 이슈로 기록하면 `build/github_issues.json`에 url→이슈 URL을 추가하면 빌드 시 `github_issue` 필드와 INDEX.md 링크가 생성됨.
   방법 A(권장): `build/items_<cat>.py`에 튜플 추가 → 이 디렉터리에서 `python3 build/build.py` 실행(저장소 루트에서는 `python3 trends/build/build.py`) → `index.jsonl`, `index.json`, `INDEX.md` 재생성(빌드가 URL 중복 시 assert로 중단).
   방법 B: `index.jsonl`에 직접 한 줄 추가 후 INDEX.md를 수작업 갱신.
4. `build/takeaways.json`의 분야별 핵심 시사점을 최신 흐름에 맞게 수정.
5. 빌드는 `build/`의 부모(`trends/`)에만 쓴다. 출력 경로는 스크립트 위치에서 계산한다.

## 추적 중인 주요 후속 이벤트 (다음 업데이트 체크리스트)
- NIST FIPS 207(HQC) 초안·FIPS 206(FN-DSA) 확정, NIST IR 8547 최종본
- CNSA 2.0 조달 기준 시행(2027-01-01), 국정원 PQC 검증제도(2028) 세부
- DOE Quantum Genesis Q 선정(신청 마감 2026-10-19), DARPA QBI Stage C 진행
- IonQ–Elisity 인수 마감(2026 Q4), 양자 상장사 실적(QNT, PSQL, XNDU, INFQ, IONQ, RGTI, QBTS)
- 한국 양자클러스터 실행계획(연내), KISTI HANGANG+IonQ 서비스(2027 상반기)
- 구글 매직 스테이트 후속, IBM Kookaburra, Microsoft·Atom Computing Magne 가동
