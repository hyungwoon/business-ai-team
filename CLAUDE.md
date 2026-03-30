# CLAUDE.md

## 프로젝트 개요
비즈니스를 돕는 범용 AI 전문가 팀 시스템. 마케팅, 리서치, 전략 수립, 문서 작성 등 다양한 비즈니스 업무를 지원한다.

## 빠른 명령

| 명령 | 설명 |
|------|------|
| `/ask [질문]` | 비즈니스 질문에 전문가 관점으로 답변 (`/route`의 간편 버전) |
| `/route [요청]` | 비즈니스 요청을 전문가 에이전트에 라우팅하여 전문 관점으로 응답 |
| `/team` | 현재 사용 가능한 전문가 에이전트 팀과 보유 스킬 목록 표시 |
| `/improve` | 학습 지식 리뷰 — 누적된 피드백 현황 확인 및 SKILL.md 반영 |
| `/health` | 프로젝트 건강도 진단 — 스킬 크기, 중복, 학습 현황, 구조 점수(A-F) |

## 에이전트 매핑 테이블 (라우팅 힌트)

> 라우팅 절차는 `.claude/rules/expert-routing.md`에 정의됨. 아래 테이블은 도메인 분류 가속을 위한 참조용.
> 모호한 요청은 `requirements-brainstorming.md` 규칙의 2축 분류 매트릭스를 거친 후 라우팅된다.

| 요청 키워드 | 에이전트 | 파일 | 플러그인 스킬 |
|---|---|---|---|
| 작업관리, 일정, 메모, 생산성 | Productivity | `agents/productivity.md` | `productivity/` → task-management, memory-management · `customer-support/` → knowledge-management |
| 리서치, 조사, 경쟁사분석, 트렌드 | Research | `agents/research.md` | `marketing/` → competitive-analysis · `sales/` → account-research, competitive-intelligence · `data/` → data-exploration · `enterprise-search/` → search-strategy, knowledge-synthesis, source-management |
| 이메일, 문서작성, 번역, 요약 | Writing | `agents/writing.md` | `marketing/` → brand-voice, content-creation · `sales/` → draft-outreach, create-an-asset · `customer-support/` → response-drafting |
| 마케팅, 캠페인, 콘텐츠, 브랜드 | Marketing | `agents/marketing.md` | `marketing/` → brand-voice, content-creation, campaign-planning, competitive-analysis, performance-analytics |
| 영업, 파이프라인, 제안서, CRM | Sales | `agents/sales.md` | `sales/` → draft-outreach, create-an-asset, daily-briefing, account-research, competitive-intelligence, call-prep · `customer-support/` → ticket-triage, customer-research, escalation |
| 데이터분석, 시각화, 인사이트, 통계 | Data | `agents/data.md` | `data/` → data-exploration, data-visualization, statistical-analysis, sql-queries, data-validation, data-context-extractor, interactive-dashboard-builder |
| 계약검토, 법률자문, 규정, 한국법령, 판례, 법제처 | Legal | `agents/legal.md` | `legal/` → contract-review, legal-risk-assessment, compliance, nda-triage, canned-responses, meeting-briefing · `enterprise-search/` → search-strategy, knowledge-synthesis, source-management · `korean-law MCP` → search_law, search_precedents, get_law_text, chain_full_research 등 64개 도구 |
| 컴플라이언스, 리스크, 감사 | Compliance | `agents/compliance.md` | `compliance/` → risk-management · `data/` → data-exploration, data-validation |
| 재무분석, 예산, 투자, ROI | Finance | `agents/finance.md` | `finance/` → financial-analysis, financial-statements, variance-analysis, journal-entry-prep, reconciliation, audit-support, close-management · `data/` → data-exploration, statistical-analysis |
| 사업개발, 파트너십, 성장전략, M&A | BizDev | `agents/business-dev.md` | `business-dev/` → growth-strategy · `marketing/` → competitive-analysis, campaign-planning · `sales/` → account-research |
| 제품전략, 로드맵, 기능스펙, PM, PRD, 디스커버리, 가정검증, OKR, 스프린트, GTM, 가격전략, 비즈니스모델, 사용자리서치, 경쟁분석, 시장분석, 코호트, A/B테스트, 포지셔닝, 배틀카드, 페르소나, 여정맵, 지표, 성장루프, 시장규모 | Product | `agents/product.md` | `product-management/` → [Discovery] brainstorm-ideas-*, identify-assumptions-*, prioritize-*, opportunity-solution-tree, interview-*, [Strategy] product-strategy, lean-canvas, business-model, pricing-strategy, swot-analysis, pestle-analysis, porters-five-forces, [Execution] create-prd, brainstorm-okrs, outcome-roadmap, sprint-plan, retro, release-notes, pre-mortem, user-stories, [Core] roadmap-management, metrics-tracking, stakeholder-comms, [Research] user-personas, market-sizing, competitor-analysis, customer-journey-map, [GTM] gtm-strategy, beachhead-segment, growth-loops, competitive-battlecard, [Growth] positioning-ideas, value-prop-statements, [Analytics] cohort-analysis, ab-test-analysis |
| 기술아키텍처, 개발프로세스, CTO, 플러그인관리 | Development | `agents/development.md` | `development/` → tech-leadership · `cowork-plugin-management/` → cowork-plugin-customizer, create-cowork-plugin |
| UX/UI, 브랜드가이드, 디자인시스템 | Design | `agents/design.md` | `design/` → ux-design · `marketing/` → brand-voice |
| 채용, 조직문화, 성과관리, HR | HR | `agents/hr.md` | `hr/` → talent-management · `productivity/` → task-management |
| 보도자료, 위기관리, 미디어전략 | PR | `agents/pr.md` | `pr/` → communications · `marketing/` → content-creation, brand-voice |
| 보안평가, 보안정책, 사이버보안 | Security | `agents/security.md` | `security/` → cybersecurity · `data/` → data-exploration |

### 복합 요청 라우팅 예시

- "신규 SaaS 런칭 전략" → Research + Product + Marketing + Sales
- "시리즈A 투자 준비" → Finance + Legal + BizDev + Product
- "해외 진출 검토" → Research + Legal + Compliance + BizDev
- "마케팅 캠페인 성과 분석" → Marketing + Data
- "신규 채용 및 팀 빌딩" → HR + Finance + Product

---

## 실행 품질 보장 시스템

> 장시간 자율 에이전트 워크플로우의 8가지 실패 모드를 체계적으로 방지하는 규칙 세트.
> 모든 규칙은 `.claude/rules/`에 위치하며, 에이전트 모드(autopilot, ralph, ultrawork)와 자동 연동된다.

| 단계 | 실패 모드 | 대응 규칙 | 핵심 메커니즘 |
|------|-----------|-----------|-------------|
| 계획 | 단기적 사고 | `plan-compete.md` | 3개 플랜 병렬 생성 → 적대적 평가 → 최적안 선택 |
| 실행 | 컨텍스트 불안 | `context-compaction.md` | 75% 도달 시 핸드오프 프롬프트 자동 생성 |
| 실행 | 계획 이탈 | `contract-enforcement.md` | 매 N 태스크마다 fresh-context 검증 → ALIGNED/DRIFTED 판정 |
| 실행 | 복잡성 공포 | `complexity-decomposer.md` | 복잡 태스크 자동 분해 + 스텁/TODO 하드 블록 |
| 사후 | 검증 게으름 | `fresh-context-verification.md` | 독립 에이전트가 fresh context에서 검증 → PASS/FAIL |
| 사후 | 엔트로피 증가 | `entropy-cleanup.md` | 세션 종료 시 blast radius 분석 + 자동 정리 |
| 메타 | 측정 불가 | `telemetry-rubrics.md` | 5개 지표 0-5점 루브릭 + 주간 트렌드 분석 |

### 실행 순서 (자동)

```
요구사항 정제 (requirements-brainstorming.md)
  → 복잡도 분류 (complexity-decomposer.md)
  → 플랜 경쟁 (plan-compete.md) — Complex만
  → 실행 + 주기적 계약 검증 (contract-enforcement.md)
  → 태스크 완료 시 독립 검증 (fresh-context-verification.md)
  → 세션 종료 시 엔트로피 정리 (entropy-cleanup.md)
  → 텔레메트리 기록 (telemetry-rubrics.md)
  → 핸드오프 생성 (context-compaction.md) — 미완료 시
```

---

## 압축(Compaction) 시 보존 지시
컨텍스트 압축 시 반드시 보존할 정보: 현재 로드된 에이전트명, 참조 중인 SKILL.md 경로, 활성 프로젝트의 _context.md 내용, 진행 중인 브레인스토밍/인터뷰 상태, knowledge/ 학습 항목.

## 문서 작성 스타일
- 기본 언어: 한국어
- 마크다운 포맷 사용
- 실용적이고 실행 가능한 내용 중심
- 불필요한 장식(이모지 등) 최소화

## 운영 환경
- **실행**: Claude Code CLI (별도 API 키 불필요)
- **지식 원천**: `agents/` (시스템 프롬프트) + `plugins/` (SKILL.md) + `knowledge/` (학습 보정)
- **학습 지식**: `knowledge/` (RLVR — 사용자 피드백 자동 학습, `/improve`로 리뷰)
- **결과물 저장**: `projects/` (로컬 전용, Git 제외)

