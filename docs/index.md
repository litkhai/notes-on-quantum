---
title: Quantum Notes
hide:
  - navigation
  - toc
---

<div class="quantum-hero" markdown>

# 양자컴퓨팅 이론과 산업을 연결하는 한글 강의·학습 노트

큐비트와 간섭의 원리에서 시작해 오류 정정, 주요 플레이어의 전략, 산업 가치사슬과 시장 전망까지 연결합니다. 180분 비기너 코스에서 출발해 장문 입문 본문과 주제별 심화 읽기로 이어집니다.

<div class="quantum-hero__actions" markdown>

[3시간 입문 강의](01-beginner-lecture/README.md){ .md-button .md-button--primary }
[입문 강의 본문](01-beginner-lecture/lecture-notes.md){ .md-button }
[상세 심화 읽기](02-deep-dive/README.md){ .md-button }
[주요 플레이어](02-deep-dive/08-major-players.md){ .md-button }
[Qiskit Aer 실험](04-simulations/README.md){ .md-button }
[GitHub 저장소](https://github.com/litkhai/notes-on-quantum){ .md-button }

</div>

</div>

> 양자컴퓨터는 특정 문제의 구조를 확률진폭·위상·간섭·얽힘으로 처리하는 특수 가속기입니다.

## 나에게 맞는 경로

<div class="grid cards" markdown>

-   **3시간 입문 강의**

    ---

    비전공자를 위한 장문 강의 본문에서 이론, 하드웨어, 산업·시장과 보안을 하나의 순서로 읽고, 발표 덱의 배경 이론으로 이중슬릿·벨 실험·VQE·QKD·클라우드 비용까지 보강합니다.

    [입문 강의 본문 →](01-beginner-lecture/lecture-notes.md) · [배경 이론 →](01-beginner-lecture/background-theory.md)

-   **상세 심화 과정**

    ---

    양자이론의 출발, 큐비트, Grover, 얽힘, 물리 구현, 오류 정정과 보안을 수식·조건·예외까지 확장합니다.

    [심화 과정 안내 →](02-deep-dive/README.md)

-   **산업과 주요 플레이어**

    ---

    IBM·Google·Microsoft·AWS·NVIDIA와 주요 QPU 기업이 서로 다른 병목과 가치사슬 계층을 어떻게 공략하는지 비교합니다.

    [플레이어 전략 지도 →](02-deep-dive/08-major-players.md)

-   **용어와 근거 확인**

    ---

    FAQ, 핵심 용어, 논문·표준·공식 기업 자료를 통해 강의에서 생략한 조건과 출처를 확인합니다.

    [추천 읽기 경로 →](03-reference/reading-guide.md)

</div>

## 코드로 재현하기

Qiskit Aer 시뮬레이션은 `H-H`, `H-Z-H`, Bell 상태, 2큐비트 Grover와 교육용 잡음 모델을 자동 실행합니다. 결과 문서와 JSON은 동일한 shots·seed로 생성되며 GitHub Actions가 회로 테스트와 결과 일치를 검사합니다.

[시뮬레이션 안내](04-simulations/README.md){ .md-button .md-button--primary }
[자동 실행 결과](04-simulations/results.md){ .md-button }

## 180분 강의 구성

| 구간 | 핵심 내용 | 자료 |
|---|---|---|
| 0:00–0:10 | 오프닝: 양자컴퓨팅에 대한 네 가지 오해 | [180분 상세 진행표](01-beginner-lecture/runsheet.md) |
| 0:10–0:40 | 1장 양자역학의 역사: 뽑기, 고양이, 벨 실험, 이중슬릿 | [배경 이론 1장](01-beginner-lecture/background-theory.md) |
| 0:40–1:33 | 2장 양자컴퓨팅이란: Grover, 데모, 큐비트·간섭·얽힘, 샷과 오류 정정 | [입문 강의 본문](01-beginner-lecture/lecture-notes.md) |
| 1:33–1:43 | 휴식 | — |
| 1:43–2:14 | 3장 유즈케이스: 화학·소재, 최적화, 금융, 보안 | [배경 이론 3장](01-beginner-lecture/background-theory.md) |
| 2:14–2:56 | 4장 어떻게 바라볼 것인가: 장비, 추상화, 클라우드 비용, GPU, 시장 숫자 | [산업·시장 브리프](01-beginner-lecture/industry-market-brief.md) |
| 2:56–3:00 | 5장 마치며: 조직의 준비와 결론 | [강사용 가이드](01-beginner-lecture/instructor-guide.md) |

## 이 자료가 유지하는 구분

1. **과학적 가능성:** 물리 법칙과 알고리즘이 성립하는가?
2. **공학적 실현:** 충분히 신뢰할 수 있는 장비로 확장 가능한가?
3. **경제적 가치:** 전체 비용을 포함해 실제 고객 문제에 이익이 있는가?

기업 로드맵, 시장 전망과 기술 논문은 서로 다른 증거 수준으로 표시합니다. 기업 사례는 산업 구조를 이해하기 위한 교육 자료이며, 투자 판단에는 별도의 조사와 검증이 필요합니다.

## 빠른 링크

- [입문 강의 본문](01-beginner-lecture/lecture-notes.md)
- [FAQ](03-reference/faq.md)
- [용어 사전](03-reference/glossary.md)
- [추천 읽기 경로](03-reference/reading-guide.md)
- [논문과 공식 자료](03-reference/references.md)
- [원문 보관소](archive/README.md)
- [Git 저장소 안내](project-guide.md)
- [GitHub 저장소](https://github.com/litkhai/notes-on-quantum)
