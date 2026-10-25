# GitHub issue drafts for litkhai/notes-on-quantum (NOT created; awaiting user approval)
Labels to create first (missing): hardware, market, pqc, software
Existing issues #1–#12 checked (all repo/infra/lecture topics) → no overlap.

## 1 [hardware] 구글, Willow에서 매직 스테이트 컬티베이션 실증 — 오류 약 40배 감소 (2026-10-15)
Index: hw (magic state) · https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/
요약: 구글 퀀텀 AI가 Willow에서 매직 스테이트 컬티베이션을 하드웨어로 구현, 미적용 대비 오류 약 40배 감소, 논리 T-스테이트 충실도 99.99% (Science, 2026-10-15).
왜 중요한가: 매직 스테이트는 범용 내결함성 양자컴퓨팅의 최대 자원 병목. 실증으로 FTQC 필요 규모 추정이 하향되고 암호 위협 타임라인 논의에도 직결.

## 2 [hardware] IBM·시카고대, 70개 오류검출 논리 큐비트로 '검증 가능한 양자우위' 주장 (2026-07-30)
Index: hw · https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits · 평가: https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/
요약: 도핑된 클리포드 샘플링으로 2,415개 2큐비트 연산·468 T게이트 회로를 약 15분 실행, 충실도 하한 인증. Quantum Advantage Tracker 공개 검증 중.
왜 중요한가: '정확성을 신뢰할 수 있는' 양자우위의 첫 본격 사례 주장. 단 오류검출·사후선택 기반이며 동료평가 전 — 고전 반박 여부 추적 필요.

## 3 [hardware] 구글 'Quantum Echoes'(OTOC) — 검증 가능한 양자우위 주장 (2025-10-22)
Index: hw · https://research.google/blog/a-verifiable-quantum-advantage/ · 후속: https://arxiv.org/abs/2604.15427
요약: Willow 65큐비트로 2차 OTOC 측정, 약 2.1시간 vs Frontier 추정 약 3.2년(~1.3만 배). 2026-04 분석에서 BP 텐서네트워크로도 재현 불가.
왜 중요한가: 무작위회로 샘플링을 넘어 물리적 관측량 기반 우위 — 재현·검증 가능하다는 점에서 우위 논쟁의 기준점.

## 4 [market] 미 상무부, 양자기업 9곳에 CHIPS 20.13억 달러 + 지분 참여 (2026-05-21)
Index: mk · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
요약: IBM(파운드리 10억)·GlobalFoundries(3.75억)·Atom·D-Wave·Infleqtion·PsiQuantum·Quantinuum·Rigetti(각 ~1억)·Diraq(최대 3,800만), 각 사 소수 지분 취득.
왜 중요한가: 미 정부가 보조금 제공자를 넘어 지분 투자자로 등장. 국내 양자 공급망·정책 설계 참고 사례.

## 5 [market] 퀀티누엄 나스닥 상장(QNT), 첫날 기업가치 176억 달러 (2026-06-04)
Index: mk · https://www.reuters.com/business/honeywells-quantinuum-valued-1763-billion-shares-rise-nasdaq-debut-2026-06-04/
요약: 주당 60달러·2,800만 주 증액 IPO. 2026년 Infleqtion·Xanadu·Horizon·Pasqal과 함께 양자 상장 러시의 정점.
왜 중요한가: 순수 양자기업 최대 상장으로 업계 밸류에이션 기준점 형성, 자본조달 경쟁 가속.

## 6 [market] 과기정통부, 서울·전남광주·부울경 양자클러스터 지정 (2026-09-01)
Index: mk · https://www.yna.co.kr/view/AKR20260901080100017 · 관련: https://en.yna.co.kr/view/AEN20260129007100320
요약: 서울(컴퓨팅)·전남광주(통신)·부울경(센싱) 지정, 2027년 본격 추진. 1월 2035 양자 종합계획(인력 1만·기업 2천, IonQ 공동연구센터 MOU)의 후속.
왜 중요한가: 한국 양자 산업정책의 실행 단계 진입 — 지역 거점·예산·참여 기회 직결.

## 7 [pqc] Q-Day 전망 단축: 구글 ECC 해독 회로 추정 + Oratomic '1만 원자 쇼어' (2026-03)
Index: pq (2건) · https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/ · https://arxiv.org/abs/2603.28627v1
요약: 구글은 secp256k1 해독에 논리 큐비트 1,200개 미만 회로를 ZK증명으로 검증(회로 비공개). Oratomic은 재배치형 중성원자 약 1만 개로 P-256 등 쇼어 실행 가능 추정.
왜 중요한가: 소프트웨어·오류정정·하드웨어 진전이 겹쳐 2035+ 전망이 앞당겨졌다는 업계 판단의 근거.

## 8 [pqc] 업계 PQC 전환 시한 2029로 수렴 — 구글·Cloudflare '인증 우선' (2026-03-25 / 04-07)
Index: pq (2건) · https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/ · https://blog.cloudflare.com/post-quantum-roadmap/
요약: 구글 2029 전환 시한·Android 17 ML-DSA. Cloudflare도 인증 포함 완전 PQ를 2029년 목표(인간 트래픽 65%+ 이미 PQ 암호화).
왜 중요한가: 'HNDL 대비 암호화'에서 '서명·인증 전환'으로 우선순위 이동 — 장기 키·코드서명·인증서 인벤토리 필요.

## 9 [pqc] 국정원 'PQC 전환 종합 추진계획' — 2029년 1월 KEM 일부 의무화 (2026-09-17)
Index: pq · https://zdnet.co.kr/view/?no=20260920204430
요약: 2대 전략·6대 과제·59개 세부과제. 2027년 공공기관 평가 반영, KEM 2028년 검증 후 2029년 1월 일부 의무화. 검증 대상: ML-KEM·NTRU+·SMAUG-T, ML-DSA·SLH-DSA·AIMer·HAETAE.
왜 중요한가: 국내 공공·핵심산업 PQC 전환의 구속력 있는 일정과 KpqC 채택 경로 확정.

(software: importance-5 item 없음 → 이슈 없음)
