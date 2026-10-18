# 양자 기술 동향 인덱스

_최종 업데이트: 2026-10-18 (KST) · 기간: 대략 2025-10 ~ 2026-10 (일부 '참고 항목'은 기준 문서로 그 이전 포함) · 총 102건_

> ⭐ = 중요도(1~5). 주요 항목은 GitHub 이슈(litkhai/notes-on-quantum)로도 기록됨. 날짜가 `YYYY-MM` 또는 `YYYY`인 항목은 출처에서 정확한 일자를 확인하지 못한 경우입니다. 원본 데이터: `index.jsonl`

## 목차
- [1. 양자컴퓨팅 하드웨어·연구 돌파구](#hardware) (27건)
- [2. 기업·투자·시장 동향 (정부 프로그램 포함)](#market) (31건)
- [3. 양자내성암호(PQC)·보안](#pqc) (24건)
- [4. 양자 소프트웨어·알고리즘·클라우드](#software) (20건)

<a id="hardware"></a>
## 1. 양자컴퓨팅 하드웨어·연구 돌파구

### 핵심 시사점
- **오류정정이 '단일 시연'에서 '논리 큐비트 수십 개 운용' 단계로 이동**: 퀀티누엄 Helios 48~94 논리 큐비트([arXiv](https://arxiv.org/abs/2602.22211)), IBM 70 논리(오류검출) 큐비트 우위 주장([IBM](https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits)), Infleqtion 30 논리 큐비트([Infleqtion](https://ir.infleqtion.com/news-events/press-releases/detail/212/infleqtion-achieves-30-entangled-logical-qubits-on-its-sqale-quantum-computer)). 다만 다수가 사후선택·오류검출 기반이라 완전한 내결함성과는 구분해야 함.
- **구글이 매직 스테이트 병목을 하드웨어로 돌파**(오류 약 40배 감소, 2026-10-15 Science) — 범용 FTQC 비용 추정을 끌어내리는 핵심 결과([Google](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/)).
- **중성원자의 급부상**: 하버드 3,000큐비트 연속 운전, 칼텍 6,100원자, Pasqal 1,024원자, 그리고 구글의 중성원자 진출(2026-03)([Google](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/)). 확장성 측면에서 가장 빠르게 따라붙는 방식.
- **이온트랩 고충실도·제조화 경쟁**: IonQ 99.99% 2큐비트 충실도→256큐비트 Superion(2027 인도)([IonQ](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)), qLDPC 손익분기 시연.
- **위상(마요라나) 큐비트는 여전히 논쟁 중**: Microsoft Majorana 2(패리티 수명 ~20초, 2029 목표) 발표에도 학계 회의론 지속([Reuters](https://www.reuters.com/business/microsoft-reveals-new-quantum-chip-made-with-ai-says-it-will-have-systems-by-2026-06-02/)).

### 항목 (최신순)
- **2026-10-15** [Bringing the magic: Google breaks open a bottleneck in quantum computing](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) — Google (blog.google) ⭐⭐⭐⭐⭐ · [이슈 #14](https://github.com/litkhai/notes-on-quantum/issues/14)  
  구글 퀀텀 AI가 Willow 프로세서에서 '매직 스테이트 컬티베이션'을 실제 하드웨어로 구현해, 컬티베이션 없을 때 대비 오류를 약 40배 줄였다고 Science에 발표했다.
- **2026-10** [IonQ Achieves Record 1 kHz Quantum Interconnect Speed](https://www.ionq.com/news/ionq-demonstrates-world-first-quantum-memory-enhanced-interconnect-for-distributed-quantum-applications) — IonQ ⭐⭐⭐  
  IonQ가 Lightsynq 인수로 확보한 다이아몬드 SiV 양자메모리와 바륨 이온을 광자로 연결해 약 1.03kHz 속도로 벨 쌍(충실도 약 87.9%)을 생성했다.
- **2026-09-24** [Infleqtion Achieves 30 Entangled Logical Qubits on Its Sqale Quantum Computer](https://ir.infleqtion.com/news-events/press-releases/detail/212/infleqtion-achieves-30-entangled-logical-qubits-on-its-sqale-quantum-computer) — Infleqtion IR ⭐⭐⭐⭐  
  Infleqtion이 중성원자 Sqale 시스템에서 물리 원자 80개(8개씩 10블록)로 논리 큐비트 30개를 얽힘 상태로 구현했다고 발표했다.
- **2026-09-14** [Breakeven demonstration of quantum low-density parity-check codes (arXiv:2606.06455)](https://arxiv.org/abs/2606.06455) — arXiv / IonQ ⭐⭐⭐⭐  
  IonQ 연구진이 40개 바륨 이온 체인 한 대에서 qLDPC·토릭·연접 코드 등 8종 오류정정 코드를 하드웨어 재구성 없이 시연했다.
- **2026-09-08** [IonQ Launches Superion Product Line (Superion 256)](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing) — IonQ ⭐⭐⭐⭐  
  IonQ가 레이저 대신 칩 집적 전자제어(EQC)를 쓰는 6세대 256큐비트 플랫폼 Superion 256을 공개했다.
- **2026-09-02** [Experimental validation of a compact fault-tolerant architecture for trapped ions (C4-Helix, arXiv:2609.03194)](https://arxiv.org/pdf/2609.03194v1) — arXiv / Quantinuum ⭐⭐⭐⭐  
  퀀티누엄이 98큐비트 Helios에서 [[20,2,6]] C4-Helix 코드 기반 내결함성 아키텍처를 검증했다.
- **2026-09-02** [IBM Quantum Nighthawk r2—more circuits, faster](https://www.ibm.com/quantum/blog/nighthawk-r2) — IBM Quantum Blog ⭐⭐⭐⭐  
  IBM이 120큐비트 Nighthawk r2(ibm_phoenix)를 IBM Quantum Platform에 공개했다.
- **2026-08-31** [Xanadu Charts Path to Over 1,000 Logical Qubits by 2031](https://investors.xanadu.ai/news-releases/news-release-details/xanadu-charts-path-over-1000-logical-qubits-2031) — Xanadu IR ⭐⭐⭐  
  광자 기반 Xanadu가 2028~2029년 내결함성 달성, 2029년 최대 200 논리큐비트, 2030년 500, 2031년 1,000개 이상을 목표로 하는 로드맵을 발표했다.
- **2026-07-30** [IBM and The University of Chicago Demonstrate Quantum Advantage on Logical Circuits](https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits) — IBM Newsroom ⭐⭐⭐⭐⭐ · [이슈 #15](https://github.com/litkhai/notes-on-quantum/issues/15)  
  IBM과 시카고대가 오류검출 인코딩된 70개 '논리' 큐비트로 2,415개 2큐비트 연산·468개 T게이트 회로를 약 15분 만에 실행하고, 충실도 하한을 인증하는 '도핑된 클리포드 샘플링'으로 양자우위를 주장했다.
- **2026-07-14** [PsiQuantum has a plan to make a massive quantum computer out of light](https://www.technologyreview.com/2026/07/14/1140356/psiquantum-plan-massive-quantum-computer-out-of-light/) — MIT Technology Review ⭐⭐⭐  
  MIT 테크놀로지 리뷰가 PsiQuantum의 광자 기반 대규모 양자컴퓨터 전략을 분석했다.
- **2026-06-11** [Pasqal Inaugurates Italy's First Neutral-Atom Quantum Computer (SOL)](https://www.pasqal.com/newsroom/pasqal-inaugurates-italys-first-neutral-atom-quantum-computer-third-pasqal-system-in-europe/) — Pasqal ⭐⭐⭐  
  Pasqal이 이탈리아 CINECA에 140큐비트 Orion QPU 'SOL'을 설치해 Leonardo 슈퍼컴퓨터와 통합했다.
- **2026-06-11** [Alice & Bob Unveils First Quantum System Available for Research Partners (Helium)](https://thequantuminsider.com/2026/06/11/alice-bob-unveils-first-quantum-system-available-for-research-partners/) — The Quantum Insider ⭐⭐⭐  
  Alice & Bob이 18 캣큐비트 칩 기반 온프레미스 연구용 'Helium' 시스템을 공개했다.
- **2026-06-10** [Improved quantum processor logical error rates via correction and detection](https://www.nature.com/articles/s41586-026-10628-y) — Nature ⭐⭐⭐⭐  
  마이크로소프트와 퀀티누엄이 이온트랩 QCCD 장치에서 12큐비트 코드와 16큐비트 테서랙트 컬러코드를 이용해 물리 기준 대비 논리 오류율을 11~800배 개선했다고 Nature에 발표했다.
- **2026-06-02** [Microsoft reveals new quantum chip made with AI (Majorana 2)](https://www.reuters.com/business/microsoft-reveals-new-quantum-chip-made-with-ai-says-it-will-have-systems-by-2026-06-02/) — Reuters ⭐⭐⭐⭐  
  마이크로소프트가 Build에서 납(Pb) 기반 InAs–Pb 테트론 소자를 쓴 Majorana 2를 공개하며 패리티 수명 약 20초(이전 ms 수준)를 주장하고 2029년 확장 가능한 양자컴퓨터를 목표로 제시했다.
- **2026-04-14** [Defect-Free 1024-Atom Registers: Scaling to 1000 Qubits](https://www.pasqal.com/blog/defect-free-1024-atom-registers-scaling-to-1000-qubits/) — Pasqal ⭐⭐⭐  
  Pasqal이 극저온 플랫폼에서 결함 없는 1,024원자 레지스터를 구현했다(95% 시행에서 결함 0.5% 미만).
- **2026-04-07** [Rigetti Announces General Availability of 108-Qubit System (Cepheus-1-108Q)](https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system) — Rigetti IR ⭐⭐⭐  
  Rigetti가 9큐비트 칩렛 12개를 연결한 108큐비트 Cepheus-1-108Q를 정식 출시했다.
- **2026-03-24** [Building superconducting and neutral atom quantum computers](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) — Google (blog.google) ⭐⭐⭐⭐  
  구글 퀀텀 AI가 초전도에 더해 중성원자 양자컴퓨팅으로 연구 범위를 확장한다고 발표했다.
- **2026-03** [IBM Quantum Roadmap 2026 (updated March 2026)](https://www.ibm.com/roadmaps/quantum/2026/) — IBM ⭐⭐⭐  
  IBM이 2026년을 '첫 양자우위 사례' 해로 규정하고 Nighthawk 7,500게이트, 실시간 오류정정 디코더 시제품, Kookaburra 모듈 시연을 목표로 제시했다.
- **2026-02-25** [Computing with many encoded logical qubits beyond break-even (arXiv:2602.22211)](https://arxiv.org/abs/2602.22211) — arXiv / Quantinuum ⭐⭐⭐⭐  
  퀀티누엄이 98큐비트 Helios에서 아이스버그 코드 등 고효율 코드로 48~94개 논리 큐비트 연산을 물리 대비 우수한(손익분기 초과) 성능으로 시연했다.
- **2026** [Neutral Atom Quantum Computing: 2026's Big Leap](https://spectrum.ieee.org/neutral-atom-quantum-computing) — IEEE Spectrum ⭐⭐⭐  
  IEEE 스펙트럼은 2026년을 오류정정 '레벨2' 기계가 고객에게 전달되는 해로 전망했다.
- **2025-11-12** [IBM Delivers New Quantum Processors (Nighthawk, Loon), Software, and Algorithm Breakthroughs](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance) — IBM Newsroom ⭐⭐⭐⭐  
  IBM이 218개 튜너블 커플러를 갖춘 120큐비트 Nighthawk와 장거리 온칩 연결(c-coupler)로 내결함성 핵심 요소를 시연하는 실험용 Loon 프로세서를 공개했다.
- **2025-11-05** [Quantinuum Announces Commercial Launch of Helios](https://www.quantinuum.com/press-releases/quantinuum-announces-commercial-launch-of-new-helios-quantum-computer-that-offers-unprecedented-accuracy-to-enable-generative-quantum-ai-genqai) — Quantinuum ⭐⭐⭐⭐  
  퀀티누엄이 98큐비트 이온트랩 Helios를 상용 출시했다.
- **2025-10-22** [A verifiable quantum advantage (Quantum Echoes)](https://research.google/blog/a-verifiable-quantum-advantage/) — Google Research ⭐⭐⭐⭐⭐ · [이슈 #16](https://github.com/litkhai/notes-on-quantum/issues/16)  
  구글이 Willow에서 2차 OTOC(시간역순 상관함수)를 측정하는 'Quantum Echoes' 실험으로 검증 가능한 양자우위를 주장했다(Nature).
- **2025-10-21** [IonQ Achieves Landmark Result, Setting New World Record in Quantum Computing Performance (99.99% 2Q fidelity)](https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing) — IonQ ⭐⭐⭐⭐  
  IonQ가 전자 큐비트 제어(EQC) 시제품으로 2큐비트 게이트 충실도 99.99%를 달성했다고 발표했다.
- **2025-10-07** [Nobel Prize in Physics 2025 (macroscopic quantum tunnelling in circuits)](https://www.nobelprize.org/prizes/physics/2025/press-release/) — NobelPrize.org ⭐⭐⭐⭐  
  2025년 노벨물리학상은 전기회로에서 거시적 양자터널링과 에너지 양자화를 발견한 존 클라크, 미셸 드보레, 존 마티니스에게 돌아갔다.
- **2025-09** [Continuous operation of a coherent 3,000-qubit system](https://www.nature.com/articles/s41586-025-09596-6) — Nature (Harvard/MIT) ⭐⭐⭐⭐  
  하버드·MIT 연구진이 광격자 '컨베이어 벨트'로 원자를 초당 최대 30만 개 재장전해 3,000개 이상 큐비트를 2시간 넘게 연속 운용했다.
- **2025-09** [Caltech Team Sets Record with 6,100-Qubit Array](https://www.caltech.edu/about/news/caltech-team-sets-record-with-6100-qubit-array) — Caltech ⭐⭐⭐  
  칼텍이 광집게로 세슘 원자 큐비트 6,100개 이상 배열을 만들어 Nature에 발표했다.

<a id="market"></a>
## 2. 기업·투자·시장 동향 (정부 프로그램 포함)

### 핵심 시사점
- **2026년은 양자 '상장의 해'**: Infleqtion(NYSE, 2월)·Xanadu(3월)·Horizon(3월)·Quantinuum(나스닥 QNT, 6월, 기업가치 약 176억 달러)([Reuters](https://www.reuters.com/business/honeywells-quantinuum-valued-1763-billion-shares-rise-nasdaq-debut-2026-06-04/))·Pasqal(8월).
- **미 정부가 '지분 투자자'로 등장**: 상무부 CHIPS 20.13억 달러·9개사 지분 참여([NIST](https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion)), DARPA QBI Stage C 6개 팀([DARPA](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage)), DOE 2.15억 달러 Quantum Genesis Q.
- **IonQ의 공격적 M&A·자본조달**: SkyWater(약 18억 달러) 인수 완료, Elisity(최대 13억 달러) 인수 발표, 20억 달러 증자 → 매출 급증(2Q +287%)과 희석 우려가 공존([IonQ](https://ionq.com/news/ionq-to-acquire-elisity-to-accelerate-zero-trust-for-the-quantum-era)).
- **빅테크 장기 베팅 확대**: IBM 100억 달러+ 투자 약속과 2028~29년 실적 기여 전망([IBM](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)); 유럽에서도 OQC £2.6억·Quobly €1.15억 등 대형 라운드.
- **한국: 정책 본격화**: 2035 양자 종합계획·IonQ 공동연구센터 MOU([연합뉴스](https://en.yna.co.kr/view/AEN20260129007100320)), 서울·전남광주·부울경 양자클러스터 지정(2026-09-01)([연합뉴스](https://www.yna.co.kr/view/AKR20260901080100017)), KISTI 슈퍼컴 6호기+IonQ 하이브리드(2027 상반기).

### 항목 (최신순)
- **2026-10-16** [IonQ Announces Pricing of $2.0 Billion Equity Offering](https://investors.ionq.com/news/news-details/2026/IonQ-Announces-Pricing-of-2-0-Billion-Equity-Offering/default.aspx) — IonQ IR ⭐⭐⭐⭐  
  IonQ가 보통주·사전납입 워런트와 시리즈C 워런트를 묶어 주당 40달러에 20억 달러 규모 증자를 단행했고 10월 16일 마감했다(순조달 약 19.9억 달러).
- **2026-10-15** [Quantum Computing Stocks Rebound After Dilution Scare](https://247wallst.com/investing/2026/10/15/quantum-computing-stocks-rebound-after-dilution-scare-ionq-and-rigetti-climb-3-d-wave-advances-2/) — 24/7 Wall St. ⭐⭐  
  IonQ의 대규모 증자로 인한 희석 우려 매도 이후 10월 15일 IonQ·Rigetti가 약 3%, D-Wave가 약 2% 반등했다.
- **2026-10-12** [IonQ to Acquire Elisity for $1.3B to Advance Quantum Security](https://ionq.com/news/ionq-to-acquire-elisity-to-accelerate-zero-trust-for-the-quantum-era) — IonQ ⭐⭐⭐⭐  
  IonQ가 제로트러스트 보안기업 Elisity를 최대 13억 달러(성과 연동 1.5억 달러 포함) 전액 주식으로 인수한다고 발표했다.
- **2026-10-08** [Four more teams enter Quantum Benchmarking Initiative's final stage](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage) — DARPA ⭐⭐⭐⭐⭐  
  DARPA QBI 최종 단계(Stage C)에 Atom Computing, Diraq, IBM, IonQ가 새로 진입해 기존 Microsoft·PsiQuantum과 함께 6개 팀이 됐다.
- **2026-10-08** [Universal Quantum raises over $100m Series A](https://universalquantum.com/knowledge-hub/universal-quantum-raises-over-100m-series-a-to-scale-quantum-computing-globally) — Universal Quantum ⭐⭐⭐  
  영국 서식스대 스핀아웃 이온트랩 기업 Universal Quantum이 1억 달러 이상 시리즈A를 유치했다.
- **2026-09-23** [IonQ Superion 256 to Power NVIDIA Quantum Research Center](https://www.ionq.com/news/ionq-to-advance-quantum-supercomputing-by-bringing-first-qpu-to-nvidia-accelerated-quantum-research-center) — IonQ ⭐⭐⭐  
  IonQ Superion 256이 NVIDIA 가속 양자연구센터(NVAQC)의 첫 온프레미스 QPU로 2027년 설치된다.
- **2026-09-04** [D-Wave 8-K: CHIPS award finalized, shares issued to Commerce](https://www.sec.gov/Archives/edgar/data/1907982/000190798226000144/qbts-20260904.htm) — SEC (D-Wave) ⭐⭐⭐  
  D-Wave가 상무부와 1억 달러 CHIPS 인센티브 계약을 확정하고 상무부에 주당 14.093달러로 약 709.6만 주를 발행했다.
- **2026-09-04** [슈퍼컴 6호기+아이온큐 양자컴퓨터, 내년 상반기 서비스](https://zdnet.co.kr/view/?no=20260904121201) — ZDNet Korea ⭐⭐⭐  
  KISTI의 국가 슈퍼컴퓨터 6호기(HANGANG)와 IonQ 양자컴퓨터를 결합한 하이브리드 서비스가 2027년 상반기 제공될 예정이다.
- **2026-09-01** [서울·전남광주·부울경에 양자클러스터…산업 생태계 조성](https://www.yna.co.kr/view/AKR20260901080100017) — 연합뉴스 ⭐⭐⭐⭐⭐ · [이슈 #19](https://github.com/litkhai/notes-on-quantum/issues/19)  
  과기정통부가 양자전략위원회 의결로 서울(양자컴퓨팅), 전남·광주(양자통신), 부산·울산·경남(양자센싱) 3곳을 첫 양자클러스터로 지정했다.
- **2026-09** [DOE Launches Competition to Accelerate Development of World's First Fault-Tolerant Quantum Computer (Quantum Genesis Q)](https://www.energy.gov/science/articles/doe-launches-competition-accelerate-development-worlds-first-fault-tolerant) — U.S. Department of Energy ⭐⭐⭐⭐  
  미 에너지부가 논리 큐비트 100개 이상 내결함성 과학용 양자컴퓨터 개발 경쟁 'Quantum Genesis Q'(최대 2.15억 달러)를 시작했다.
- **2026-08-27** [Pasqal and Bleichroeder Acquisition Corp. II Complete Business Combination](https://www.pasqal.com/newsroom/pasqal-and-bleichroeder-acquisition-corp-ii-complete-business-combination/) — Pasqal ⭐⭐⭐⭐  
  프랑스 중성원자 기업 Pasqal이 SPAC 합병을 8월 27일 완료하고 8월 28일 나스닥(PSQL)에 상장했다.
- **2026-08-05** [IonQ Announces Record Second Quarter 2026 Revenues, Growing 287% YoY](https://investors.ionq.com/news/news-details/2026/IonQ-Announces-Record-Second-Quarter-2026-Revenues-Growing-287-YoY/default.aspx) — IonQ IR ⭐⭐⭐⭐  
  IonQ의 2026년 2분기 매출이 8,010만 달러로 전년 대비 287% 증가했고, 독자 기준 연간 가이던스를 2.8~2.9억 달러로 상향했다.
- **2026-07-31** [IonQ Completes Acquisition of SkyWater Technology](https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology) — IonQ ⭐⭐⭐⭐  
  IonQ가 미국 파운드리 SkyWater 인수를 약 18억 달러(현금 7.4억 달러+주식)에 완료했다.
- **2026-07-30** [IBM CEO says quantum computing will have a 'measurable impact' on earnings by 2028 or 2029](https://www.cnbc.com/2026/07/30/ibm-ceo-quantum-computing-measurable-impact-earnings-2028-2029.html) — CNBC ⭐⭐⭐  
  IBM CEO는 양자컴퓨팅이 2028~2029년 실적에 '측정 가능한 영향'을 줄 것이라고 밝혔다.
- **2026-06-17** [PsiQuantum's billion-dollar Brisbane project starts construction at new Moreton Bay site](https://www.afr.com/technology/first-look-at-psiquantum-s-revamped-supercomputer-project-20260617-p607i5) — Australian Financial Review ⭐⭐⭐  
  PsiQuantum의 호주 브리즈번 프로젝트가 공항 부지에서 모어턴베이로 옮겨 착공했다.
- **2026-06-16** [Atom Computing Raises More Than $300 Million](https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html) — PR Newswire ⭐⭐⭐  
  Atom Computing이 Third Point Ventures 주도 1억 달러 시리즈C와 상무부 1억 달러 의향서를 포함해 총 3억 달러 이상을 조달했다고 발표했다.
- **2026-06-04** [Honeywell's Quantinuum valued at $17.63 billion as shares rise in Nasdaq debut](https://www.reuters.com/business/honeywells-quantinuum-valued-1763-billion-shares-rise-nasdaq-debut-2026-06-04/) — Reuters ⭐⭐⭐⭐⭐ · [이슈 #18](https://github.com/litkhai/notes-on-quantum/issues/18)  
  허니웰 자회사 퀀티누엄이 나스닥(QNT)에 상장해 첫날 기업가치 176.3억 달러를 기록했다.
- **2026-06-03** [OQC raises £260m in Europe's largest ever private quantum computing funding round](https://oqc.tech/company/newsroom/series-c) — OQC ⭐⭐⭐  
  영국 Oxford Quantum Circuits가 Bullhound Capital 주도로 유럽 최대 민간 양자컴퓨팅 투자인 2.6억 파운드 시리즈C를 유치했다.
- **2026-06-03** [Quobly secures €115 million Series A](https://www.quobly.io/press-releases/quobly-secures-e115-million-series-a-to-bring-silicon-based-quantum-computers-to-market) — Quobly ⭐⭐  
  프랑스 실리콘 스핀 큐비트 기업 Quobly가 1.15억 유로 시리즈A를 유치했다.
- **2026-06-02** [IBM Commits More Than $10 Billion to Quantum Computing](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers) — IBM Newsroom ⭐⭐⭐⭐  
  IBM이 2029년 내결함성 컴퓨터까지 로드맵을 뒷받침하기 위해 양자컴퓨팅에 100억 달러 이상을 투자하겠다고 발표했다.
- **2026-05-21** [Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion](https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion) — NIST ⭐⭐⭐⭐⭐ · [이슈 #17](https://github.com/litkhai/notes-on-quantum/issues/17)  
  미 상무부가 CHIPS법에 따라 9개 기업에 총 20.13억 달러 인센티브 의향서를 체결하고 각 사의 소수 지분을 받기로 했다.
- **2026-05-11** [Algorithmiq Establishes Milan Headquarters and raises €18m](https://www.algorithmiq.tech/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software/) — Algorithmiq ⭐⭐  
  양자 알고리즘·오류완화 소프트웨어 기업 Algorithmiq가 본사를 밀라노로 옮기고 1,800만 유로를 조달했다(누적 3,600만 유로).
- **2026-03-30** [Quantum firms race to market as the industry sees 'inflection point'](https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html) — CNBC ⭐⭐⭐  
  CNBC는 2026년 양자기업들이 SPAC·IPO로 잇달아 상장에 나서는 흐름을 '변곡점'으로 분석했다.
- **2026-03-26** [Xanadu Announces Closing of Business Combination with Crane Harbor](https://investors.xanadu.ai/news-releases/news-release-details/xanadu-quantum-technologies-limited-announces-closing-business) — Xanadu IR ⭐⭐⭐⭐  
  캐나다 광자 양자기업 Xanadu가 Crane Harbor SPAC 합병을 마치고 3월 27일 나스닥·TSX에 XNDU로 상장했다.
- **2026-03-19** [Horizon Quantum Goes Public via SPAC, Raises $120 Million](https://thequantuminsider.com/2026/03/19/horizon-quantum-goes-public-via-spac-raises-120-million/) — The Quantum Insider ⭐⭐  
  싱가포르 양자 소프트웨어 기업 Horizon Quantum이 dMY Squared SPAC 합병으로 나스닥(HQ)에 상장하며 약 1.2억 달러를 조달했다.
- **2026-03** [Pasqal new financing of at least €340 million in anticipation of its public listing](https://www.pasqal.com/newsroom/pasqal-is-entering-a-new-phase-of-development-with-new-financing-expected-of-at-least-e340-million-in-anticipation-of-its-public-listing/) — Pasqal ⭐⭐⭐  
  Pasqal이 상장을 앞두고 민간투자 1.7억 유로와 SPAC 연계 전환금융 약 1.7억 유로 등 최소 3.4억 유로 자금 조달을 발표했다.
- **2026-03** [KISTI Partners with NVIDIA and IonQ to Build a Leading 'Quantum–HPC Hybrid' Infrastructure](https://www.kisti.re.kr/eng/news/post/eng_news/6919) — KISTI ⭐⭐⭐⭐  
  KISTI가 NVIDIA·IonQ와 협약을 맺고 IonQ 100큐비트 Tempo를 국가 슈퍼컴 6호기 HANGANG과 CUDA-Q·NVQLink로 통합하기로 했다.
- **2026-02-17** [Infleqtion Becomes First Neutral-Atom Quantum Company to Go Public](https://ir.infleqtion.com/news-events/press-releases/detail/167/infleqtion-becomes-first-neutral-atom-quantum-company-to-go-public) — Infleqtion IR ⭐⭐⭐  
  Infleqtion이 Churchill Capital Corp X와의 합병을 2월 13일 완료하고 2월 17일 NYSE(INFQ)에 상장했다.
- **2026-01-29** [Science ministry unveils road map for quantum industry](https://en.yna.co.kr/view/AEN20260129007100320) — Yonhap News Agency ⭐⭐⭐⭐⭐ · [이슈 #19](https://github.com/litkhai/notes-on-quantum/issues/19)  
  과기정통부가 2035년 세계 최고 양자칩 생산국, 전문인력 1만 명, 양자기업 2,000개 육성을 목표로 하는 제1차 양자 종합계획을 발표했다.
- **2026-01-20** [D-Wave Completes Acquisition of Quantum Circuits Inc.](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-completes-acquisition-of-quantum-circuits/) — D-Wave ⭐⭐⭐  
  어닐링 강자 D-Wave가 듀얼레일 초전도 큐비트 기업 Quantum Circuits 인수(5.5억 달러)를 완료하며 게이트 방식에 본격 진출했다.
- **2025-09-10** [PsiQuantum valued at $7 billion in latest funding round, teams up with Nvidia](https://www.reuters.com/business/psiquantum-valued-7-billion-latest-funding-round-teams-up-with-nvidia-2025-09-10/) — Reuters ⭐⭐⭐  
  PsiQuantum이 BlackRock·Temasek·Baillie Gifford 주도, NVentures 참여로 10억 달러 시리즈E를 유치하며 기업가치 70억 달러를 인정받았다(인덱스 기간 직전 참고 항목).

<a id="pqc"></a>
## 3. 양자내성암호(PQC)·보안

### 핵심 시사점
- **Q-Day 전망이 앞당겨짐**: 구글 ECC 해독 회로(논리 1,200개 미만, ZK증명)·Oratomic 1만 원자 쇼어·Pinnacle 10만 큐비트 RSA 추정이 연달아 발표([Cloudflare 정리](https://blog.cloudflare.com/post-quantum-roadmap/)).
- **업계 전환 시한 2029로 수렴, '인증(서명) 우선'**: 구글 2029 타임라인·Android 17 ML-DSA([Google](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)), Cloudflare 2029, 이더리움 2029, 크롬 MTC(2027).
- **표준·프로토콜 정비**: IETF RFC 10024(하이브리드 ML-KEM TLS)([RFC](https://www.rfc-editor.org/rfc/rfc10024.html)), NIST HQC(FIPS 207 초안 임박)·FN-DSA(FIPS 206 미확정), CNSA 2.0 2027-01-01 조달 기준.
- **한국 PQC 일정 구체화**: 국정원 59개 과제 종합계획 — 2027년 공공평가 반영, 2029년 1월 KEM 일부 의무화([ZDNet Korea](https://zdnet.co.kr/view/?no=20260920204430)); 과기정통부 5대 분야 시범전환([연합뉴스](https://www.yna.co.kr/view/AKR20260506053400017)); KpqC 4종 KS 표준화 진행.
- **암호자산이 새 전선**: 유로폴 경고([Europol](https://www.europol.europa.eu/media-press/newsroom/news/europol-urges-early-action-to-protect-cryptocurrencies-and-sensitive-data-quantum-threats)), 비트코인 BIP-360 초안, 이더리움 2029 목표.

### 항목 (최신순)
- **2026-10-07** [Europol urges early action to protect cryptocurrencies and sensitive data from quantum threats](https://www.europol.europa.eu/media-press/newsroom/news/europol-urges-early-action-to-protect-cryptocurrencies-and-sensitive-data-quantum-threats) — Europol ⭐⭐⭐  
  유로폴이 두 건의 보고서를 내고 양자컴퓨터가 공개키로부터 암호화폐 지갑 개인키를 노출시킬 수 있다고 경고했다.
- **2026-10-07** [NSA's 2027 PQC gate for national-security systems (CNSA 2.0)](https://quantakrypto.com/news/2026-10-07/nsa-pqc-resource-hub-2027-nss-deadline) — QuantaKrypto ⭐⭐⭐⭐  
  NSA CNSA 2.0에 따라 2027년 1월 1일부터 신규 국가안보시스템(NSS) 조달품은 양자내성 알고리즘을 지원해야 한다.
- **2026-10** [Post-Quantum Encryption Worldwide (Cloudflare Radar)](https://radar.cloudflare.com/post-quantum) — Cloudflare Radar ⭐⭐⭐  
  Cloudflare Radar는 PQ 암호화 트래픽 비율과 오리진 서버의 X25519MLKEM768 지원률(검색 시점 약 16% 수준)을 실시간으로 보여준다.
- **2026-09-17** [양자내성암호 전환, 내년부터 공공 사이버보안 실태 평가에 반영 (국정원 PQC 전환 종합 추진계획)](https://zdnet.co.kr/view/?no=20260920204430) — ZDNet Korea ⭐⭐⭐⭐⭐ · [이슈 #22](https://github.com/litkhai/notes-on-quantum/issues/22)  
  국정원이 2대 전략·6대 과제·59개 세부과제의 'PQC 전환 종합 추진계획'을 공개했다.
- **2026-09-07** [EF Protocol: Current and Emerging Priorities](https://blog.ethereum.org/2026/09/07/protocol-priorities) — Ethereum Foundation Blog ⭐⭐⭐  
  이더리움 재단이 양자내성을 최우선 과제로 올리고 2029년 12월까지 실행·합의·데이터 계층 전반의 완전한 양자내성을 목표로 제시했다.
- **2026-08** [RFC 10024: Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3](https://www.rfc-editor.org/rfc/rfc10024.html) — RFC Editor (IETF) ⭐⭐⭐⭐  
  IETF가 TLS 1.3용 하이브리드 키합의 표준 RFC 10024를 발행했다.
- **2026-07** [New Windows Features to Secure Today's Data in a Post-Quantum World](https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-windows-features-to-secure-today%E2%80%99s-data-in-a-post-quantum-world/4523370) — Microsoft Tech Community ⭐⭐⭐  
  윈도우가 ML-KEM 하이브리드 TLS 키교환과 복합(composite) 알고리즘을 지원하고, AD CS의 ML-DSA 인증서 발급이 2026년 5월 정식 제공됐다.
- **2026-05-06** [정부, 국가 주요 인프라 '양자내성암호 전환' 확대](https://www.yna.co.kr/view/AKR20260506053400017) — 연합뉴스 ⭐⭐⭐⭐  
  과기정통부가 의료·에너지·행정에 이어 통신·금융·교통·국방·우주 5대 분야로 PQC 시범전환을 확대하고 드림시큐리티·케이스마텍 등 사업자를 선정했다.
- **2026-04-07** [Cloudflare targets 2029 for full post-quantum security](https://blog.cloudflare.com/post-quantum-roadmap/) — Cloudflare Blog ⭐⭐⭐⭐⭐ · [이슈 #21](https://github.com/litkhai/notes-on-quantum/issues/21)  
  Cloudflare가 인증(서명)까지 포함한 완전한 PQ 보안 목표를 2029년으로 앞당겼다.
- **2026-03-25** [Quantum frontiers may be closer than they appear (Google's timeline for PQC migration)](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) — Google (blog.google) ⭐⭐⭐⭐⭐ · [이슈 #21](https://github.com/litkhai/notes-on-quantum/issues/21)  
  구글이 PQC 전환 시한을 2029년으로 설정하고 위협모델을 조정해 인증·서명 전환을 우선하기로 했다.
- **2026-03** [Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) — Google Research ⭐⭐⭐⭐⭐ · [이슈 #20](https://github.com/litkhai/notes-on-quantum/issues/20)  
  구글이 secp256k1 타원곡선 이산로그를 깨는 최적화된 쇼어 회로(논리 큐비트 1,200개 미만·토폴리 9천만 개 등)를 추정하고, 공격 회로 자체는 공개하지 않은 채 영지식증명으로 검증했다.
- **2026-03** [Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits (arXiv:2603.28627)](https://arxiv.org/abs/2603.28627v1) — arXiv / Oratomic ⭐⭐⭐⭐⭐ · [이슈 #20](https://github.com/litkhai/notes-on-quantum/issues/20)  
  Oratomic이 재배치 가능한 중성원자 시스템에서 약 1만 개 물리 큐비트로 P-256 등 암호 관련 쇼어 알고리즘 실행이 가능하다는 자원 추정을 발표했다.
- **2026-02-23** [Bitcoin Took Its First Step Against Quantum Computers (BIP-360)](https://www.forbes.com/sites/digital-assets/2026/02/23/bitcoin-took-its-first-step-against-quantum-computers/) — Forbes ⭐⭐⭐  
  공개키 장기 노출을 막는 P2MR(Pay-to-Merkle-Root) 출력 형식 BIP-360이 2026년 2월 BIP 저장소에 병합됐다.
- **2026-02-13** [New Architecture Could Cut Quantum Hardware Needed to Break RSA-2048 by Tenfold (Pinnacle)](https://thequantuminsider.com/2026/02/13/new-architecture-could-cut-quantum-hardware-needed-to-break-rsa-2048-by-tenfold-study-finds/) — The Quantum Insider ⭐⭐⭐⭐  
  Iceberg Quantum이 qLDPC 코드 기반 'Pinnacle' 아키텍처로 RSA-2048 해독에 필요한 물리 큐비트를 10만 개 미만으로 줄일 수 있다고 추정했다(오류율 10⁻³ 가정, 최소 구성 약 한 달 소요).
- **2026-01** [KpqC SMAUG-T & HAETAE official site (KpqC final algorithms)](https://kpqc.cryptolab.co.kr/) — CryptoLab / KpqC ⭐⭐⭐⭐  
  한국형 양자내성암호(KpqC)는 NTRU+·SMAUG-T(KEM)와 AIMer·HAETAE(서명) 4종이 최종 선정됐고, 2026년 1월 공식 사양과 참조구현이 공개됐다.
- **2026** [FIPS 206 (FN-DSA) Status Update](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/1HXzjlMUU6Y) — NIST PQC Forum ⭐⭐⭐  
  FALCON 기반 FN-DSA(FIPS 206)는 2026년 10월 현재 아직 최종화되지 않았고 초안이 행정 승인 단계에 있다.
- **2026** [Chrome Quantum-resistant Root Program - FAQ (Merkle Tree Certificates)](https://googlechrome.github.io/chromerootprogram/cqrp/faq/) — Google Chrome ⭐⭐⭐⭐  
  크롬은 공개 웹 PQ 인증에 대형 X.509 체인 대신 머클트리 인증서(MTC)를 쓰는 방안을 추진하며, MTC 프로덕션은 2027년 1분기, 양자내성 루트스토어는 2027년 3분기를 목표로 한다.
- **2025-11** [Post-Quantum Cryptography APIs Now Generally Available on Microsoft Platforms](https://techcommunity.microsoft.com/blog/microsoft-security-blog/post-quantum-cryptography-apis-now-generally-available-on-microsoft-platforms/4469093) — Microsoft Tech Community ⭐⭐⭐  
  ML-KEM과 ML-DSA가 2025년 11월 업데이트로 Windows 11·Windows Server 2025의 CNG 및 인증서 API에서 정식 제공됐다.
- **2025-10-02** [Signal Protocol and Post-Quantum Ratchets (SPQR)](https://signal.org/blog/spqr/) — Signal ⭐⭐⭐  
  시그널이 기존 더블 래칫과 병행하는 ML-KEM 기반 희소 포스트퀀텀 래칫(SPQR)을 도입해 '트리플 래칫'을 구성했다.
- **2025-06** [A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography (EU)](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) — European Commission ⭐⭐⭐⭐  
  EU 로드맵은 2026년 말까지 회원국별 PQC 계획 수립·전환 착수, 2030년 말까지 핵심 인프라 등 고위험 사용처 전환, 2035년까지 가능한 범위 전체 전환을 제시한다(참고 기준 문서, 구속력 없음).
- **2025-06** [Get ahead with quantum-secure cryptography (WWDC25)](https://developer.apple.com/videos/play/wwdc2025/314/) — Apple Developer ⭐⭐⭐  
  애플이 iOS 26부터 URLSession·Network.framework에서 X25519MLKEM768 하이브리드 TLS를 기본 활성화하고 CryptoKit에 ML-KEM·ML-DSA·X-Wing HPKE API를 추가한다고 발표했다(참고 항목).
- **2025-05** [How to factor 2048 bit RSA integers with less than a million noisy qubits (arXiv:2505.15917)](https://arxiv.org/abs/2505.15917) — arXiv / Google ⭐⭐⭐⭐  
  구글 크레이그 기드니가 0.1% 게이트 오류 등을 가정할 때 약 90만 개 물리 큐비트로 RSA-2048을 1주 이내에 인수분해할 수 있다고 추정했다(기존 2천만 개 추정 대비 대폭 감소).
- **2025-03** [NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) — NIST ⭐⭐⭐  
  NIST가 ML-KEM의 백업 KEM으로 코드 기반 HQC를 선정했다.
- **2024-11** [NIST IR 8547 (Initial Public Draft): Transition to Post-Quantum Cryptography Standards](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf) — NIST ⭐⭐⭐⭐  
  NIST IR 8547 초안은 RSA·ECC 등 양자취약 공개키 알고리즘을 2030년 이후 폐기 권고(deprecated), 2035년 이후 사용 금지(disallowed)하는 일정을 제안한다.

<a id="software"></a>
## 4. 양자 소프트웨어·알고리즘·클라우드

### 핵심 시사점
- **양자우위 주장은 '검증 인프라' 경쟁으로**: Quantum Advantage Tracker 출범(2025-11) 이후 IBM 3편 논문은 증거 수준이 상이하다는 평가([PostQuantum](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/)); 구글 Quantum Echoes는 BP 텐서네트워크로도 재현 불가 분석.
- **SDK가 내결함성(FT) 컴파일 시대로**: Qiskit 2.5의 PBC·Clifford+T 파이프라인([IBM](https://www.ibm.com/quantum/blog/qiskit-2-5-release-summary)), Quantinuum Guppy FT, Microsoft QDK 멀티프레임워크 지원.
- **GPU-QPU 결합이 표준 아키텍처화**: NVIDIA NVQLink(2025-10)→cudaq-realtime 공개(2026-03)([NVIDIA](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/03/16/launching-cudaq-realtime/)); 실시간 디코딩이 핵심 워크로드.
- **클라우드 접근 확대**: Braket에 Rigetti 108큐비트, QuEra 내결함성 Libra 2028 Braket 제공 예정([AWS](https://aws.amazon.com/blogs/quantum-computing/aws-deepens-strategic-collaboration-with-quera-to-bring-fault-tolerant-quantum-computing-to-amazon-braket/)), 구글 Willow 조기 접근.
- **AI가 양자 알고리즘 설계에 진입**: Anthropic Claude가 ECC 점덧셈 회로 게이트 약 17배 절감([Anthropic](https://www.anthropic.com/research/designing-efficient-quantum-circuits)); DQI 계열의 증명 가능한 우위 이론 결과 잇따름.

### 항목 (최신순)
- **2026-10-16** [Designing more efficient quantum circuits with Claude](https://www.anthropic.com/research/designing-efficient-quantum-circuits) — Anthropic ⭐⭐⭐⭐  
  Anthropic이 Claude로 화학·최적화·정수론 등 8개 과제의 양자회로를 설계해 기존보다 효율적인 회로를 얻었다고 발표했다.
- **2026-10** [Exponential quantum advantages for decoded quantum interferometry in the streaming setting (arXiv:2610.01902)](https://arxiv.org/html/2610.01902) — arXiv ⭐⭐⭐  
  디코디드 양자간섭(DQI) 알고리즘을 스트리밍 환경으로 확장해, 폴리로그 공간만 쓰는 1회 통과 양자 알고리즘이 다항 공간이 필요한 고전 알고리즘을 능가함을 증명했다(제약 만족 93% 대 76%).
- **2026-10** [A provable quantum advantage for approximate optimization via decoded quantum interferometry (arXiv:2610.02145)](https://arxiv.org/abs/2610.02145) — arXiv ⭐⭐⭐  
  오라클 설정에서 folded OPI 문제에 대해 DQI와 모든 다항시간 고전 알고리즘 사이의 엄밀한 근사 격차를 증명했다.
- **2026-09-22** [IonQ Demonstrates Industry's First End-to-End Real-Time Quantum Error Decoder](https://www.ionq.com/news/ionq-demonstrates-industrys-first-end-to-end-real-time-quantum-error-decoder) — IonQ ⭐⭐⭐  
  IonQ가 단일 CPU(맥북 M4 Max)로 동작하는 종단간 실시간 QEC 디코더를 발표했다.
- **2026-08-03** [Guppy v1 stable release / Nexus Developer Platform 26.1](https://docs.quantinuum.com/guppy/release_notes.html) — Quantinuum Docs ⭐⭐⭐  
  퀀티누엄의 양자 프로그래밍 언어 Guppy가 8월 3일 v1 안정판이 됐고, Nexus 26.1 프리릴리스에는 QEC 코드 아키텍처를 정의·컴파일하는 Guppy FT와 재사용 알고리즘 라이브러리가 추가됐다.
- **2026-08-01** [IBM's Three Quantum Advantage Claims, Fact-Checked](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/) — PostQuantum.com ⭐⭐⭐⭐ · [이슈 #15](https://github.com/litkhai/notes-on-quantum/issues/15)  
  IBM이 7월 30일 시카고대·Qedma·Algorithmiq와 낸 3편의 양자우위 논문은 증거 수준이 서로 다르다는 분석이다.
- **2026-07-02** [Release News: Qiskit v2.5 is here!](https://www.ibm.com/quantum/blog/qiskit-2-5-release-summary) — IBM Quantum Blog ⭐⭐⭐⭐  
  Qiskit 2.5가 출시되어 C API의 동적회로 제어흐름 검사, 다중 IR 컴파일러(MultiStagePassManager), PBC·Clifford+T용 내결함성 컴파일 파이프라인, 트랜스파일 속도 향상을 제공한다.
- **2026-06-30** [Cirq v1.7.0 release](https://github.com/quantumlib/Cirq/releases/tag/v1.7.0) — GitHub (quantumlib) ⭐⭐  
  구글 Cirq 1.7.0이 Python 3.14 지원, CY/CCY 게이트, QASM 3 도구, 구글 하드웨어 시뮬레이터 개선을 담아 출시됐다.
- **2026-06-15** [AWS Deepens Strategic Collaboration with QuEra to Bring Fault-Tolerant Quantum Computing to Amazon Braket](https://aws.amazon.com/blogs/quantum-computing/aws-deepens-strategic-collaboration-with-quera-to-bring-fault-tolerant-quantum-computing-to-amazon-braket/) — AWS Quantum Technologies Blog ⭐⭐⭐⭐  
  AWS와 QuEra가 다년 협력을 확대해 QuEra의 첫 내결함성 컴퓨터 Libra를 2028년 Amazon Braket에서 제공하기로 했다.
- **2026-06** [Majorana 2, made more reliable with Microsoft Discovery agentic AI](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/) — Microsoft ⭐⭐⭐  
  마이크로소프트는 Azure 기반 에이전틱 AI 연구 플랫폼 Microsoft Discovery를 활용해 Majorana 2 큐비트 신뢰성을 높였다고 밝혔다.
- **2026-05-22** [Stim v1.16.0 - Flowing Circuits](https://github.com/quantumlib/Stim/releases/tag/v1.16.0) — GitHub (quantumlib) ⭐⭐  
  QEC 시뮬레이터 Stim 1.16.0이 stimflow, CliffordString, Python 3.13/3.14 휠, Sinter 디코더 지원을 추가해 출시됐다.
- **2026-04-07** [Amazon Braket launches Rigetti Cepheus-1-108Q superconducting device](https://aws.amazon.com/blogs/quantum-computing/amazon-braket-launches-rigetti-cepheus-1-108q-superconducting-device/) — AWS Quantum Technologies Blog ⭐⭐⭐  
  Amazon Braket에 Rigetti 108큐비트 Cepheus-1-108Q가 추가돼 Braket 최초의 100큐비트 초과 게이트 방식 장치가 됐다(미 서부 리전).
- **2026-04** [Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment (arXiv:2604.15427)](https://arxiv.org/abs/2604.15427) — arXiv ⭐⭐⭐ · [이슈 #16](https://github.com/litkhai/notes-on-quantum/issues/16)  
  텐서네트워크+신뢰전파(BP) 고전 시뮬레이션 기법으로도 구글 Quantum Echoes 실험을 현실적으로 재현할 수 없다는 분석이다.
- **2026-03-28** [Google Opens Early Access to 'Willow' Quantum Processor, Invites Experimental Proposals](https://thequantuminsider.com/2026/03/28/google-opens-early-access-to-willow-quantum-processor-invites-experimental-proposals/) — The Quantum Insider ⭐⭐⭐  
  구글이 비공개 Willow 프로세서를 선정된 연구자에게 개방하는 조기 접근 프로그램을 시작했다(제안 마감 5월 15일, 7월 1일 선정 발표).
- **2026-03-16** [Introducing cudaq-realtime for programming the Logical QPU](https://nvidia.github.io/cuda-quantum/blogs/blog/2026/03/16/launching-cudaq-realtime/) — NVIDIA CUDA-Q Blog ⭐⭐⭐⭐  
  NVIDIA가 GTC 2026에서 CUDA-Q 0.14의 cudaq-realtime API로 NVQLink를 공개 제공했다.
- **2026-01-22** [Powerful new developer tools increase the versatility of the Microsoft Quantum platform](https://azure.microsoft.com/en-us/blog/quantum/2026/01/22/powerful-new-developer-tools-increase-the-versatility-of-the-microsoft-quantum-platform/) — Microsoft Azure Quantum Blog ⭐⭐⭐  
  마이크로소프트가 오픈소스 Quantum Development Kit(QDK)를 확장해 Q#과 함께 Qiskit·Cirq·OpenQASM을 지원하고 VS Code·GitHub Copilot 연동과 오류정정 도구를 추가했다.
- **2025-12** [Tianyan: Cloud services with quantum advantage (arXiv:2512.10504)](https://arxiv.org/abs/2512.10504) — arXiv ⭐⭐⭐  
  중국 Zuchongzhi 3.0과 같은 구조의 105큐비트 칩을 상용 클라우드 'Tianyan-287'로 배포했다는 논문이다.
- **2025-11-12** [Quantum Advantage Tracker: the race to advantage](https://www.ibm.com/quantum/blog/quantum-advantage-tracker) — IBM Quantum Blog ⭐⭐⭐⭐  
  IBM·Algorithmiq·Flatiron 연구진·BlueQubit이 양자우위 주장을 최고 고전 기법과 비교·검증하는 공개 커뮤니티 트래커를 출범했다.
- **2025-10-28** [NVIDIA Introduces NVQLink — Connecting Quantum and GPU Computing](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing) — NVIDIA Newsroom ⭐⭐⭐⭐  
  NVIDIA가 GTC 워싱턴에서 QPU·제어시스템을 GPU 슈퍼컴퓨팅과 저지연으로 묶는 개방형 인터커넥트 NVQLink를 발표했다.
- **2025-09-24** [HSBC says quantum computing trial helps bond trading](https://www.reuters.com/business/finance/hsbc-says-quantum-computing-trial-helps-bond-trading-2025-09-24/) — Reuters ⭐⭐⭐  
  HSBC가 IBM Heron을 활용한 채권거래 체결 예측 실험에서 최대 34% 개선을 보고했다.
