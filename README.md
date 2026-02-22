# Business AI Team

당신의 비즈니스를 돕는 범용 AI 전문가 팀.

마케팅, 리서치, 전략 수립, 문서 작성 등 비즈니스 전 분야를 16명의 AI 전문가가 지원합니다.

---

## 실행 방법

**Claude Code CLI**에서 이 프로젝트 디렉토리를 열면 자동으로 전문가 팀이 활성화됩니다.

```bash
cd business-ai-team
claude
```

별도의 API 키 설정이나 환경 구성은 필요하지 않습니다.

---

## 전문가 팀 구성

```
운영 지원 (Run the Business)
├── Productivity   → 작업 관리, 일정 조율, 메모 정리
├── Writing        → 이메일, 문서, 번역
└── Data           → 데이터 분석, 시각화, 인사이트

수익 창출 (Grow the Business)
├── Marketing      → 마케팅 콘텐츠, 캠페인 기획
├── Sales          → 영업 전략, 파이프라인, 제안서
├── BizDev         → 사업 기회, 파트너십 전략
└── Product        → 제품 전략, 로드맵, 기능 스펙

전문 자문 (Protect the Business)
├── Legal          → 계약 검토, 법률 자문
├── Compliance     → 규정 준수, 리스크 관리
├── Finance        → 재무 분석, 예산 계획
└── Security       → 보안 평가, 정책 수립, 보안 감사

조직 기반 (Build the Business)
├── HR             → 채용 전략, 조직 문화, 성과 관리
├── Design         → UX/UI, 브랜드 가이드라인
├── Development    → 기술 아키텍처, 개발 프로세스
├── PR             → 보도자료, 위기 관리, 미디어 전략
└── Research       → 시장 조사, 경쟁사 분석, 트렌드 리서치
```

---

## 빠른 명령

| 명령 | 설명 |
|------|------|
| `/ask [질문]` | 비즈니스 질문에 전문가 관점으로 답변 (`/route`의 간편 버전) |
| `/route [요청]` | 비즈니스 요청을 전문가 에이전트에 라우팅하여 전문 관점으로 응답 |
| `/team` | 현재 사용 가능한 전문가 에이전트 팀과 보유 스킬 목록 표시 |

일반 대화에서도 비즈니스 요청 시 자동으로 해당 전문가에게 라우팅됩니다.

---

## 사용 예시

```
# 빠른 명령 사용
/ask AI 에이전트 시장의 주요 트렌드는?
/route 시리즈A 투자 준비를 위한 재무 전략 수립해줘
/team

# 작업 관리
"이번 주 해야 할 작업 정리하고 우선순위 잡아줘. 신제품 출시 준비, 투자자 미팅, 마케팅 자료 작성."

# 리서치
"AI 에이전트 시장 조사해줘. 주요 트렌드와 경쟁사 분석."

# 문서 작성
"파트너사에 보낼 협업 제안 이메일 작성해줘."

# 복합 작업
"경쟁사 3곳 분석하고 결과를 바탕으로 차별화 전략 보고서 써줘."

# 재무
"이 재무 데이터 분석해줘. 주요 지표와 개선 기회 포함."

# 법률
"이 계약서 검토하고 위험 요소 알려줘."
```

---

## 작동 원리

비즈니스 요청이 들어오면, CLI가 **CLAUDE.md의 라우팅 테이블**을 따라 해당 전문가 에이전트의 시스템 프롬프트와 플러그인 스킬을 참조하여 응답합니다.

```
사용자 요청 (예: "마케팅 캠페인 기획")
    ↓
CLAUDE.md 라우팅 테이블 → 마케팅 도메인 식별
    ↓
agents/marketing.md → 시스템 프롬프트 참조
    ↓
plugins/marketing/skills/ → 베스트 프랙티스 참조
    ↓
전문가 관점이 반영된 응답
```

복합 요청은 여러 에이전트의 전문성을 조합합니다:
- "신규 SaaS 런칭 전략" → Research + Product + Marketing + Sales
- "시리즈A 투자 준비" → Finance + Legal + BizDev + Product

---

## 프로젝트 구조

```
business-ai-team/
├── CLAUDE.md                # 시스템 설정 + 전문가 라우팅 테이블
├── agents/                  # 16개 전문가 에이전트 (시스템 프롬프트 + 스킬 라우팅)
│   ├── marketing.md
│   ├── research.md
│   ├── sales.md
│   └── ... (13개 추가 에이전트)
├── .claude/commands/         # 슬래시 커맨드 (/ask, /route, /team)
├── plugins/                 # 18개 도메인별 플러그인 스킬
│   ├── marketing/skills/    # brand-voice, content-creation 등
│   ├── sales/skills/        # draft-outreach, account-research 등
│   ├── data/skills/         # data-exploration, visualization 등
│   └── ... (15개 추가 플러그인)
├── archive/                 # 결과물 보관 (Git 제외)
└── docs/                    # 설계 문서
```

---

## 플러그인 스킬 목록

11개 플러그인은 [Anthropic knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)에서 가져왔으며, 7개는 이 프로젝트에서 자체 생성했습니다.

| 플러그인 | 출처 | 스킬 |
|---------|------|------|
| marketing | Anthropic | brand-voice, content-creation, campaign-planning, competitive-analysis, performance-analytics |
| sales | Anthropic | draft-outreach, create-an-asset, daily-briefing, account-research, competitive-intelligence, call-prep |
| data | Anthropic | data-exploration, data-visualization, statistical-analysis, sql-queries, data-validation, data-context-extractor, interactive-dashboard-builder |
| finance | Anthropic + 자체 | financial-analysis, financial-statements, variance-analysis, journal-entry-prep, reconciliation, audit-support, close-management |
| legal | Anthropic | contract-review, legal-risk-assessment, compliance, nda-triage, canned-responses, meeting-briefing |
| product-management | Anthropic | roadmap-management, feature-spec, user-research-synthesis, competitive-analysis, metrics-tracking, stakeholder-comms |
| productivity | Anthropic | task-management, memory-management |
| customer-support | Anthropic | ticket-triage, response-drafting, customer-research, escalation, knowledge-management |
| enterprise-search | Anthropic | search-strategy, knowledge-synthesis, source-management |
| bio-research | Anthropic | instrument-data-to-allotrope, nextflow-development, scientific-problem-selection, scvi-tools, single-cell-rna-qc |
| cowork-plugin-management | Anthropic | cowork-plugin-customizer, create-cowork-plugin |
| business-dev | 자체 | growth-strategy |
| compliance | 자체 | risk-management |
| development | 자체 | tech-leadership |
| design | 자체 | ux-design |
| hr | 자체 | talent-management |
| pr | 자체 | communications |
| security | 자체 | cybersecurity |
