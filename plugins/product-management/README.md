# Product Management Plugin

> 제품 관리 종합 플러그인 — 60개 스킬, 31개 커맨드

## 개요

PM 전체 라이프사이클을 지원하는 종합 플러그인입니다. Anthropic의 기본 3개 스킬(roadmap-management, metrics-tracking, stakeholder-comms)에 PM Skills (Paweł Huryn)의 57개 스킬을 통합하여, 디스커버리부터 성장까지 모든 단계를 커버합니다.

- **60개 스킬** — 7개 카테고리로 체계화
- **31개 커맨드** — pm-skills-ko 체인 워크플로우
- **12개 MCP 커넥터** — Slack, Linear, Notion, Figma, Amplitude 등 연동

## 스킬 목록 (60개)

### 디스커버리 (12)

| 스킬 | 설명 |
|------|------|
| `brainstorm-ideas-existing` | 기존 제품의 아이디어 도출. PM/디자이너/엔지니어 시각 활용 다각적 아이디에이션 |
| `brainstorm-ideas-new` | 신규 제품의 기능 아이디어 도출. 초기 디스커버리 단계 아이디에이션 |
| `brainstorm-experiments-existing` | 기존 제품 가정 검증 실험 설계. 프로토타입, A/B 테스트, 스파이크 |
| `brainstorm-experiments-new` | 신규 제품 린 실험 설계. XYZ 가설, 랜딩 페이지, 사전 주문 검증 |
| `identify-assumptions-existing` | 기존 제품 기능의 위험 가정 식별. 가치/사용성/실행가능성/기술 타당성 |
| `identify-assumptions-new` | 신규 제품의 8가지 위험 카테고리 가정 식별. GTM, 전략, 팀 포함 |
| `prioritize-assumptions` | Impact × Risk 매트릭스로 가정 우선순위화 및 실험 제안 |
| `prioritize-features` | 영향도/노력/리스크/전략 정합성 기준 기능 우선순위화 |
| `analyze-feature-requests` | 기능 요청 분석. 테마/전략 정렬/영향/노력/위험도 기준 우선순위 결정 |
| `opportunity-solution-tree` | Teresa Torres OST 구축. 결과→기회→솔루션→실험 연결 |
| `interview-script` | JTBD 기반 고객 인터뷰 스크립트 작성. 엄마 테스트 원칙 적용 |
| `summarize-interview` | 인터뷰 트랜스크립트를 JTBD/만족도 신호/액션 아이템으로 요약 |

### 전략 (15)

| 스킬 | 설명 |
|------|------|
| `product-strategy` | 9개 섹션 Product Strategy Canvas로 종합 제품 전략 수립 |
| `startup-canvas` | 신제품용 전략+비즈니스 모델 결합 Startup Canvas 생성 |
| `product-vision` | 팀 동기부여 및 이해관계자 정렬을 위한 제품 비전 구상 |
| `value-proposition` | JTBD 프레임워크 기반 6단계 가치 제안 설계 |
| `lean-canvas` | 9개 구성요소 Lean Canvas 생성. 문제/솔루션/핵심지표/UVP |
| `business-model` | 9개 구성요소 Business Model Canvas 생성 |
| `monetization-strategy` | 3~5가지 수익화 전략 브레인스토밍. 적합성/리스크/검증 실험 |
| `pricing-strategy` | 가격 모델/경쟁사 가격/지불 의사/탄력성 분석 및 설계 |
| `swot-analysis` | 강점/약점/기회/위협 분석 및 실행 가능한 권고사항 도출 |
| `pestle-analysis` | 정치/경제/사회/기술/법적/환경적 거시 환경 분석 |
| `porters-five-forces` | Porter 5 Forces 산업 역학 분석. 경쟁/공급자/구매자/대체재/진입 |
| `ansoff-matrix` | 시장 침투/시장 개발/제품 개발/다각화 성장 전략 매핑 |
| `positioning-ideas` | 경쟁사 차별화 제품 포지셔닝 아이디어 브레인스토밍 |
| `value-prop-statements` | 마케팅/영업/온보딩용 가치 제안 문장 생성 |
| `product-name` | 브랜드 가치에 부합하는 독창적 제품명 5가지 브레인스토밍 |

### 실행 (15)

| 스킬 | 설명 |
|------|------|
| `create-prd` | 8개 섹션 템플릿 PRD 작성. 문제/목표/세그먼트/가치제안/솔루션/출시계획 |
| `brainstorm-okrs` | 회사 목표 연계 팀 OKR 브레인스토밍. 측정 가능한 핵심 결과 포함 |
| `outcome-roadmap` | 산출물→결과 중심 로드맵 전환. 전략적 의도 반영 |
| `sprint-plan` | 역량 추정/스토리 선택/의존성/리스크 기반 스프린트 계획 |
| `retro` | 구조화된 스프린트 회고. 잘 된 점/개선점/우선순위 액션 아이템 |
| `release-notes` | 티켓/PRD에서 사용자 대상 릴리스 노트 생성. 카테고리별 정리 |
| `pre-mortem` | 사전 부검 리스크 분석. Tigers/Paper Tigers/Elephants 분류 |
| `stakeholder-map` | 권한/관심도 그리드 이해관계자 맵 구성 및 커뮤니케이션 전략 |
| `summarize-meeting` | 회의 전사본을 구조화된 회의록으로 요약. 결정/액션 아이템 포함 |
| `user-stories` | 3 C's + INVEST 기준 유저 스토리 작성. 인수 기준 포함 |
| `job-stories` | When-I want to-So I can 형식 잡 스토리 작성. 상세 인수 기준 |
| `wwas` | Why-What-Acceptance 형식 백로그 항목 작성 |
| `test-scenarios` | 유저 스토리 기반 종합 테스트 시나리오 작성 |
| `dummy-dataset` | 테스트용 현실적 더미 데이터셋 생성. CSV/JSON/SQL/Python |
| `prioritization-frameworks` | 9가지 우선순위 프레임워크 참고. RICE/ICE/Kano/MoSCoW/Opportunity Score |

### 핵심 PM (3)

| 스킬 | 설명 |
|------|------|
| `roadmap-management` | Now/Next/Later, RICE, MoSCoW, ICE 프레임워크 기반 로드맵 관리 |
| `metrics-tracking` | 제품 지표 정의/추적/분석. OKR, 대시보드 설계, 주간 리뷰 |
| `stakeholder-comms` | 대상별 이해관계자 업데이트 작성. 경영진/엔지니어링/고객/파트너 |

### 시장 리서치 (7)

| 스킬 | 설명 |
|------|------|
| `user-personas` | 리서치 데이터 기반 사용자 페르소나 작성. JTBD/페인 포인트/이점 |
| `market-segments` | 인구통계/JTBD/적합도 기반 3~5개 잠재 고객 세그먼트 식별 |
| `user-segmentation` | 행동/JTBD/니즈 기반 피드백 데이터 사용자 세분화 |
| `customer-journey-map` | 단계/접점/감정/페인 포인트/기회 포함 고객 여정 지도 |
| `market-sizing` | TAM/SAM/SOM 하향식+상향식 시장 규모 추정 |
| `competitor-analysis` | 경쟁사 강점/약점/차별화 기회 분석. 경쟁 환경 매핑 |
| `sentiment-analysis` | 사용자 피드백 감성 분석. 감성 점수/JTBD/만족도 인사이트 |

### 데이터 분석 (2)

| 스킬 | 설명 |
|------|------|
| `cohort-analysis` | 코호트별 리텐션/기능 도입/이탈 패턴 분석 |
| `ab-test-analysis` | A/B 테스트 결과 분석. 통계적 유의성/신뢰 구간/출시 권고 |

### 출시 전략 (6)

| 스킬 | 설명 |
|------|------|
| `gtm-strategy` | 마케팅 채널/메시징/성공 지표/타임라인 포함 GTM 전략 수립 |
| `beachhead-segment` | 첫 교두보 시장 세그먼트 파악. 페인 포인트/지불 의향/점유율 평가 |
| `ideal-customer-profile` | 인구통계/행동/JTBD/니즈 기반 이상적 고객 프로필(ICP) 정의 |
| `growth-loops` | 바이럴/사용/협업/UGC/추천 등 5가지 성장 루프 설계 |
| `gtm-motions` | 인바운드/아웃바운드/PLG 등 7가지 GTM 모션 및 도구 파악 |
| `competitive-battlecard` | 영업용 경쟁 배틀카드 작성. 포지셔닝/기능 비교/반론 대응 |

## 커맨드 (31)

| 커맨드 | 설명 |
|--------|------|
| `/discover` | 엔드투엔드 디스커버리 워크플로우 (아이디어→가정→실험) |
| `/brainstorm` | 아이디어 브레인스토밍 (기존/신규 제품) |
| `/interview` | 인터뷰 스크립트 작성 및 인터뷰 종합 |
| `/research-users` | 사용자 리서치 종합 |
| `/write-prd` | PRD (Product Requirements Document) 작성 |
| `/write-stories` | 유저 스토리/잡 스토리/WWA 작성 |
| `/write-query` | 데이터 분석용 쿼리 작성 |
| `/plan-okrs` | OKR 설정 및 정렬 |
| `/sprint` | 스프린트 계획/회고/릴리스 노트 (3가지 모드) |
| `/transform-roadmap` | 산출물→결과 중심 로드맵 전환 |
| `/strategy` | 제품 전략 캔버스 수립 |
| `/business-model` | 비즈니스 모델 캔버스 작성 |
| `/value-proposition` | 가치 제안 설계 |
| `/pricing` | 가격 전략 분석 및 설계 |
| `/market-scan` | 거시 환경 분석 (SWOT/PESTLE/Porter/Ansoff) |
| `/competitive-analysis` | 경쟁사 분석 |
| `/battlecard` | 경쟁 배틀카드 작성 |
| `/market-product` | 마케팅/포지셔닝 전략 |
| `/growth-strategy` | 성장 루프 및 GTM 전략 |
| `/plan-launch` | 출시 계획 수립 |
| `/stakeholder-map` | 이해관계자 맵 구성 |
| `/pre-mortem` | 사전 부검 리스크 분석 |
| `/meeting-notes` | 회의 전사본 요약 |
| `/setup-metrics` | 제품 지표 설정 |
| `/north-star` | 노스스타 메트릭 정의 |
| `/triage-requests` | 기능 요청 분석 및 분류 |
| `/test-scenarios` | 테스트 시나리오 작성 |
| `/generate-data` | 더미 데이터셋 생성 |
| `/analyze-cohorts` | 코호트 분석 |
| `/analyze-test` | A/B 테스트 결과 분석 |
| `/analyze-feedback` | 사용자 피드백 감성 분석 |

## MCP 커넥터

다음 도구와 연동하여 더욱 강력한 기능을 제공합니다:

- **Slack** — 팀 맥락 및 이해관계자 스레드
- **Linear** — 로드맵 통합, 티켓 맥락, 상태 추적
- **Asana** — 프로젝트 관리, 작업 추적
- **monday.com** — 워크플로우 자동화, 상태 관리
- **ClickUp** — 작업 관리, 타임라인
- **Atlassian** — Jira 통합, 이슈 추적
- **Notion** — 기존 스펙, 리서치, 회의록
- **Figma** — 디자인 맥락, 핸드오프
- **Amplitude** — 사용자 데이터, 지표, 행동 분석
- **Pendo** — 제품 분석, 사용자 피드백
- **Intercom** — 지원 티켓, 기능 요청, 사용자 대화
- **Fireflies** — 회의 기록, 토론 맥락

## 크레딧

- **Anthropic** — 핵심 PM 3개 스킬 (roadmap-management, metrics-tracking, stakeholder-comms)
- **Paweł Huryn (PM Skills)** — 57개 추가 스킬 및 프레임워크
- **lucas-flatwhite** — 한국어 번역 및 로컬라이제이션

## 사용 예시

### PRD 작성

```
당신: /write-prd
Claude: 어떤 기능이나 문제를 PRD로 작성하고 싶으신가요?
당신: 엔터프라이즈 고객을 위해 SSO 지원을 추가해야 합니다
Claude: [대상 사용자, 제약사항, 성공 지표에 대해 질문]
Claude: [8개 섹션 PRD 생성 — 문제 정의, 목표, 세그먼트, 가치 제안, 솔루션, 출시 계획]
```

### 디스커버리 워크플로우

```
당신: /discover 스마트 알림 시스템
Claude: 기존 제품인가요, 신규 제품인가요?
당신: 기존 제품의 새 기능입니다
Claude: [아이디어 브레인스토밍 → 가정 식별 → 가정 우선순위화 → 실험 설계]
Claude: [디스커버리 결과 문서 생성]
```

### 스프린트 관리

```
당신: /sprint plan
Claude: 팀 규모와 스프린트 기간을 알려주세요
당신: 5명, 2주 스프린트
Claude: [역량 추정, 스토리 선택, 의존성 매핑, 리스크 식별]
Claude: [스프린트 계획 문서 생성]
```

### 경쟁 배틀카드

```
당신: /battlecard
Claude: 어떤 경쟁사에 대한 배틀카드를 만들까요?
당신: Notion 대비 우리 제품 배틀카드
Claude: [경쟁사 조사, 포지셔닝 분석]
Claude: [포지셔닝/기능 비교/반론 대응/승/패 패턴이 포함된 배틀카드]
```

## 추가 정보

더 자세한 정보는 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.
