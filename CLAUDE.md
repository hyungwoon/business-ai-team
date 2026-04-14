# CLAUDE.md

> **CRITICAL**: 비즈니스 도메인 응답 전 반드시 agents/[domain].md를 Read 도구로 실제 읽기. 기억/추정 대체 절대 금지.
> **CRITICAL**: 응답 맨 앞에 `> **담당**: [Agent] | 참조 스킬: [Skill]` 헤더 필수 포함.
> **CRITICAL**: `git add .` 사용 금지 — projects/ 유출 위험. 구체적 파일명으로 스테이징.

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
| `/skill-test [스킬명]` | 스킬 품질 테스트 — Evaluation/A/B 테스트, 포트폴리오 점검, 디스크립션 최적화 |

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

---

> **REMINDER**: 비즈니스 응답 전 agents/*.md + SKILL.md + knowledge/preferences.md 각각 별도 Read 호출 필수.
> **REMINDER**: `> **담당**:` 헤더 없는 비즈니스 응답 전달 금지.
> **REMINDER**: projects/ 폴더는 절대 git에 추가하지 않는다.

---

# PROJECT KNOWLEDGE BASE (English reference)

**Generated:** 2026-03-31
**Branch:** main

## OVERVIEW

16 AI agents + 31 Claude Code 네이티브 스킬(.claude/skills/). 110+ plugin skills + gstack 엔지니어링 워크플로우. RLVR 능동적 학습 + 세션 리마인드.

## STRUCTURE

```
business-ai-team/
├── CLAUDE.md              # Master config: agent mapping table, session rules
├── agents/                # 16 domain agents (lightweight routers)
├── plugins/               # 17 domain plugins, 110+ skills (best practices)
├── knowledge/             # RLVR feedback storage (auto-learning)
├── .claude/skills/        # 31 native skills (23 business + 8 engineering)
├── .claude/rules/         # 14 rules (expert-routing, requirements-brainstorming, feedback-learning, session-reminder, session-closing, project-workspace, eng-workflow, plan-compete, contract-enforcement, complexity-decomposer, context-compaction, entropy-cleanup, fresh-context-verification, skill-budget)
├── .claude/commands/      # 6 commands (/ask, /route, /team, /improve, /health, /skill-test)
└── projects/              # Client deliverables (LOCAL ONLY)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Understand request flow | `CLAUDE.md` "실행 품질 보장 시스템" section | 8-stage pipeline diagram |
| Add/modify an agent | `agents/[domain].md` | ~50 lines: system prompt + skill routing table |
| Add/modify a skill | `plugins/[domain]/skills/[skill]/SKILL.md` | 69-900 lines: frameworks + templates |
| Check learned corrections | `knowledge/[domain].md` | 4 tables: corrections, tips, warnings, rejections |
| Modify routing rules | `.claude/rules/expert-routing.md` | Mandatory procedures + forbidden actions + domain boundary routing |
| Modify brainstorming gate | `.claude/rules/requirements-brainstorming.md` | 심층 인터뷰 게이트 (2축 분류 + 7개 인터뷰 기법, 질문 수 무제한) |
| Modify feedback detection | `.claude/rules/feedback-learning.md` | 5종 감지 패턴 (정보 보정, 실무 노하우, 주의사항, 거부 기록, 선호도) |
| Quality assurance rules | `.claude/rules/plan-compete.md` + 6 more | 8가지 실패 모드 대응 (plan-compete, contract-enforcement, complexity-decomposer, context-compaction, entropy-cleanup, fresh-context-verification, telemetry-rubrics) |
| Session lifecycle | `.claude/rules/session-closing.md`, `project-workspace.md` | 세션 종료 체크리스트, 프로젝트 폴더링 규칙 |
| Engineering workflow | `.claude/rules/eng-workflow.md` | gstack 기반 엔지니어링 스킬 가이드 |
| Review learning status | `knowledge/_index.md` | Domain counts; `/improve` command |
| Resume a project | `projects/[name]/_context.md` | Always read first before working |
| Use native skills | `.claude/skills/[name]/SKILL.md` | 31 mega-skills — 비즈니스 라우터는 plugins/ 직접 참조, gstack은 자체 완결 |
| Check project health | `/health` command | Size, duplicates, learning status, structure |
| Configure session reminders | `.claude/rules/session-reminder.md` | Auto-load preferences, context, learning at session start |

## REQUEST FLOW

```
User Request
  → [0.5] Check projects/_context.md (skip gate if continuation)
  → [1] Brainstorming Gate (A=full, B=light, C=1 question, D=direct)
  → [2] Domain Classification (CLAUDE.md mapping table)
  → [3] Read agents/[domain].md (MANDATORY — never from memory)
  → [4] Read plugins/.../SKILL.md (MANDATORY)
  → [4.5] Read knowledge/[domain].md + preferences.md
  → [5] Generate response (knowledge overrides SKILL.md)
  → [6] Prepend "> **담당**: [Agent] | 참조 스킬: [Skill]"
  → [RLVR] Auto-detect feedback → store in knowledge/
```

## CONVENTIONS

- **Language**: Korean primary, English/Korean mixed in plugin SKILL.md files (product-management is Korean)
- **Agent files**: Lightweight routing metadata (~50-120 lines), NOT full system prompts
- **Skill files**: YAML frontmatter (name, description) + markdown content
- **File naming**: `YYYY-MM-DD_[description].md` for all project deliverables
- **Context files**: `_context.md` mandatory in every project folder (underscore prefix for sort-first)
- **Cross-domain skills**: Agents can reference skills from other plugins (e.g., Research uses Sales's account-research)
- **Plugin origin**: 10 from Anthropic knowledge-work-plugins, 7 custom-built
- **PM Skills**: product-management plugin expanded to 60 skills via PM Skills (Paweł Huryn) Korean edition integration
- **Native skills**: `.claude/skills/` — 23 business mega-skills (router → plugins/ 직접 참조) + 8 engineering skills (gstack-based, 자체 완결)
- **PM mega-skills**: 60 skills grouped into 7 mega-skills (pm-discovery, pm-strategy, pm-execution, pm-core, pm-research, pm-gtm, pm-analytics)

## ANTI-PATTERNS (THIS PROJECT)

- **NEVER** generate business response without reading `agents/[agent].md` file
- **NEVER** provide domain expertise without reading the corresponding `SKILL.md`
- **NEVER** deliver response without `> **담당**:` attribution header
- **NEVER** substitute memory/estimation for reading agent files
- **NEVER** use `git add .` — always stage specific files (projects/ leak risk)
- **NEVER** push `projects/` folder to git
- **NEVER** end session without updating `_context.md` for worked projects
- **NEVER** skip session-end git push after system file changes
- **NEVER** delete from `knowledge/` after SKILL.md reflection (preserve history)

## UNIQUE STYLES

- **Agents as routers**: Agents contain routing tables to skills, not full expertise
- **Mandatory file reads**: System enforces `Read` tool calls — no memory/estimation
- **RLVR learning**: Auto-detects user corrections ("아닌데", "실무에서는", "주의해야") + rejections ("이건 안 써", "필요없어", "다시 해줘") → stores in knowledge/
- **3-item threshold**: When domain accumulates 3+ feedback items → auto-reflect to SKILL.md
- **Priority hierarchy**: knowledge/ corrections > SKILL.md best practices > agent system prompt
- **Dual-path resolution**: Local agents/ first, falls back to `~/.claude/business-team/agents/`
- **Brainstorming gate escape**: "바로 해줘", "알아서 해줘", "급해" → skip gate

## NOTES

- `projects/` is in `.gitignore` but verify no accidental staging before push
- Knowledge: Writing domain has 9 learned items (형운 voice profile), Sales has 1 item, preferences has 8 items. Other domains at 0 — system learns incrementally through use
- Multi-agent composition: complex requests route to 2-5 agents (e.g., "시리즈A 투자 준비" → Finance + Legal + BizDev + Product)
- Session-end checklist overrides ALL other rules — mandatory push after system changes
- Same project, different request direction → re-run brainstorming gate
- Dual-skill sync: 13 router skills have "참조 원본" section linking to agents/ as single source of truth
- Cross-plugin discoverability: 10 core plugin skills have "관련 스킬" cross-reference tables
- Architecture visualization: `architecture.html` — request flow, 4-layer diagram, agent routing map
- Custom plugin v2.0: 7 custom plugins expanded from avg 176줄 → avg 575줄 (3.3x depth increase)

---

## .CLAUDE DIRECTORY REFERENCE

System control layer: 4 routing rules + 5 slash commands + 31 native skills. These files govern all request processing behavior.

### .claude/ structure

```
.claude/
├── settings.local.json
├── skills/                # 31 native skills (Claude Code auto-discovery)
│   ├── pm-discovery/      # Router (35 lines) → routes to plugins/
│   ├── browse/            # Self-contained (243 lines) + build infra
│   └── ... (31 total)
├── rules/                 # Auto-loaded rules (always active)
│   ├── expert-routing.md
│   ├── requirements-brainstorming.md
│   ├── feedback-learning.md    # Extended with active learning
│   └── session-reminder.md     # NEW: auto-load prefs/context/learning
└── commands/
    ├── ask.md
    ├── route.md
    ├── team.md
    ├── improve.md
    └── health.md               # NEW: project health dashboard
```

### .claude/ where to look

| Task | File | Key Content |
|------|------|-------------|
| Change routing enforcement | `rules/expert-routing.md` | Mandatory read procedures, forbidden actions (절대 금지) |
| Change brainstorming behavior | `rules/requirements-brainstorming.md` | 2-axis matrix, gate types A-D, escape conditions |
| Change feedback detection | `rules/feedback-learning.md` | Pattern triggers, storage procedure, 3-item threshold |
| Modify quick question flow | `commands/ask.md` | Path resolution, simplified routing |
| Modify full routing flow | `commands/route.md` | Brainstorming gate + domain classification + skill loading |
| Change learning review | `commands/improve.md` | Dashboard display, reflection proposal workflow |
| Configure session auto-load | `rules/session-reminder.md` | Preferences, context, learning loaded at session start |
| Check project health | `commands/health.md` | Size, duplicates, learning status, structure dashboard |
| Use or modify native skills | `skills/[name]/SKILL.md` | 31 mega-skills auto-discovered by Claude Code |

### .claude/ conventions

- Rules in `rules/` are auto-loaded every session — always active
- Commands in `commands/` are user-invoked via `/[name]`
- Skills in `skills/` are auto-discovered by Claude Code — available without explicit invocation
- Both rules and commands support dual-path resolution: local first → `~/.claude/business-team/` fallback
- Rules use "절대 금지" (absolute prohibition) for hard enforcement

### .claude/ anti-patterns

- **NEVER** weaken mandatory file-read requirements in expert-routing.md
- **NEVER** remove brainstorming gate without replacing with equivalent quality control
- Gate escape conditions ("바로 해줘", "급해") are intentional — don't remove them

---

## AGENTS DIRECTORY REFERENCE

16 lightweight domain routers. Each ~50 lines: system prompt + skill routing table.

### agents/ structure

All files are flat `[domain].md` — no subdirectories. Each agent file contains:

1. **Title + description** (1 line Korean)
2. **System prompt** (3-5 lines: expertise + principles)
3. **Actions** (capabilities list)
4. **Communication style** (tone + language patterns)
5. **Plugin & skill routing table** (maps request types → plugin → skill)
6. **Output criteria** (quality standards)

### agents/ where to look

| Agent | Domain | Cross-Domain Skills |
|-------|--------|---------------------|
| marketing | Brand, content, campaigns | — |
| sales | Outreach, pipeline, assets | customer-support (ticket-triage, escalation) |
| research | Market research, trends | marketing, sales, data, enterprise-search skills |
| writing | Documents, emails, translation | marketing (brand-voice, content-creation) |
| data | Analysis, visualization, SQL | — |
| finance | Financial analysis, budgets | — |
| legal | Contracts, risk, compliance | enterprise-search (search-strategy) |
| product | Discovery, strategy, execution, roadmap, GTM, metrics (60 skills) | — |
| productivity | Task management, scheduling | — |
| hr | Talent, culture, performance | — |
| design | UX/UI, brand guidelines | — |
| development | Architecture, tech processes | — |
| pr | Press, crisis communications | — |
| security | Cybersecurity, audits | — |
| compliance | Regulations, risk management | — |
| business-dev | Growth, partnerships | — |

### agents/ conventions

- Routing table format: `| 요청 유형 | 플러그인 | 스킬 |`
- Agent = router, not expert. Expertise lives in `plugins/*/SKILL.md`
- Cross-domain references are explicit (Research → Sales's account-research)
- Communication style includes Korean-specific patterns (conditional language for Legal, etc.)

### agents/ anti-patterns

- **NEVER** add full expertise content to agent files — keep them as routing metadata
- **NEVER** reference a skill without verifying it exists in `plugins/`
- Agent file is source of truth for routing — CLAUDE.md mapping table is just a guide

---

## KNOWLEDGE DIRECTORY REFERENCE

RLVR (Reinforcement Learning from Verbal Reasoning) feedback storage. Auto-learns from user corrections during conversations.

### knowledge/ structure

```
knowledge/
├── _index.md         # Learning counts per domain (corrections | tips | warnings | rejections | total)
├── preferences.md    # Cross-domain user preferences (format, style, language)
├── writing.md        # Writing domain (pre-existing with learned content)
└── [domain].md       # Other domain files (auto-created on first learning detection)
```

### knowledge/ how it works

1. **Detection**: System auto-detects feedback patterns during conversation
2. **Storage**: Appends row to appropriate domain table + increments `_index.md`
3. **Application**: Read at step 4.5 of request flow — overrides SKILL.md
4. **Reflection**: At 3+ items per domain → auto-reflect to SKILL.md's `## 실무 보정 사항`

### knowledge/ detection patterns

| Category | Table | Triggers |
|----------|-------|----------|
| 정보 보정 (corrections) | `기존 정보 \| 보정 내용 \| 출처` | "아닌데", "틀렸", "바뀌었", "사실은" |
| 실무 노하우 (tips) | `노하우 \| 적용 맥락` | "실무에서는", "경험상", "우리 회사에서는" |
| 주의사항 (warnings) | `주의사항 \| 위험/영향` | "주의해야", "함정이", "절대 하면 안 되는" |
| 거부/불만족 (rejections) | `거부 대상 \| 이유 \| 대안` | "이건 안 써", "필요없어", "다시 해줘", "별로야", "이전 게 나았어" |
| 선호도 (preferences) | → `preferences.md` | "항상 이렇게", "난 이걸 선호", "앞으로는" |

### knowledge/ priority hierarchy

```
knowledge/[domain].md  >  SKILL.md best practices  >  agents/[agent].md system prompt
(most recent feedback)    (established patterns)      (base identity)
```

### knowledge/ anti-patterns

- **NEVER** delete items from knowledge/ after reflecting to SKILL.md (preserve audit trail)
- **NEVER** skip reading knowledge/ files during response generation
- Duplicate check: same content → skip; conflicting info → update existing row
- **NEVER** pre-create domain files — let them auto-generate on first learning detection
- Current state: writing.md has 9 learned items; other domains created on demand (system learns incrementally)

---

## PLUGINS DIRECTORY REFERENCE

17 domain plugins containing 110 skills. 10 from Anthropic knowledge-work-plugins, 7 custom-built. product-management expanded to 60 skills via PM Skills (Paweł Huryn) Korean edition. Plugin skills are also available as native mega-skills via `.claude/skills/` for Claude Code auto-discovery.

### plugins/ structure

```
[domain]/
├── .claude-plugin/plugin.json   # Metadata (name, version, author)
├── .mcp.json                    # MCP server connections (Slack, HubSpot, etc.)
├── README.md                    # Plugin overview + commands + skills list
├── CONNECTORS.md                # MCP integration reference (optional)
├── commands/                    # Slash commands (e.g., /draft-content)
│   └── [command].md
└── skills/                      # Domain expertise
    └── [skill-name]/
        ├── SKILL.md             # Core: YAML frontmatter + frameworks + templates
        ├── references/          # Supporting materials (optional)
        └── examples/            # Usage examples (optional)
```

### plugins/ where to look

| Plugin | Origin | Skills | Notes |
|--------|--------|--------|-------|
| marketing | Anthropic | brand-voice, content-creation, campaign-planning, competitive-analysis, performance-analytics | 7 commands |
| sales | Anthropic | draft-outreach, create-an-asset, daily-briefing, account-research, competitive-intelligence, call-prep | Standalone skills |
| data | Anthropic | data-exploration, data-visualization, statistical-analysis, sql-queries, data-validation, data-context-extractor, interactive-dashboard-builder | Has scripts/ + references/ |
| finance | Anthropic+custom | financial-analysis, financial-statements, variance-analysis, journal-entry-prep, reconciliation, audit-support, close-management | 7 skills |
| legal | Anthropic | contract-review, legal-risk-assessment, compliance, nda-triage, canned-responses, meeting-briefing | Playbook-based review |
| product-management | Anthropic + PM Skills (Paweł Huryn) | 60 skills grouped into pm-discovery, pm-strategy, pm-execution, pm-core, pm-research, pm-gtm, pm-analytics | 31 commands, 12 MCP connectors; 7 mega-skills in .claude/skills/ |
| customer-support | Anthropic | ticket-triage, response-drafting, customer-research, escalation, knowledge-management | Cross-referenced by Sales |
| productivity | Anthropic | task-management, memory-management | Persistent memory system |
| enterprise-search | Anthropic | search-strategy, knowledge-synthesis, source-management | Source-agnostic |
| cowork-plugin-management | Anthropic | cowork-plugin-customizer, create-cowork-plugin | Has examples/ + references/ |
| business-dev | Custom | growth-strategy | — |
| compliance | Custom | risk-management | — |
| development | Custom | tech-leadership | — |
| design | Custom | ux-design | — |
| hr | Custom | talent-management | — |
| pr | Custom | communications | Crisis response anti-patterns |
| security | Custom | cybersecurity | Incident response protocols |

### plugins/ SKILL.md format

```yaml
---
name: skill-name        # kebab-case, matches folder
description: When to use # Trigger patterns
---
# Skill Name
[Core frameworks/methodology]
[Detailed guidance with tables]
[Templates with [CUSTOMIZE] markers]
[Configuration sections]
```

Size range: 69-867 lines. Custom plugins v2.0 expanded to 504-642 lines (was ~150-200), Anthropic plugins 156-867 lines. PM Skills (product-management) skills are Korean, 69-303 lines each.

### plugins/ conventions

- Skill names: kebab-case, action-oriented
- SKILL.md is the ONLY file agents read — README.md and commands/ are supplementary
- Skills degrade gracefully without MCP connectors
- Cross-domain sharing: skills are referenced by multiple agents (competitive-analysis used by Marketing, Research; Product uses own competitor-analysis)

### plugins/ anti-patterns

- **NEVER** add agent-specific logic to SKILL.md — skills are domain-generic
- **NEVER** modify SKILL.md without checking if `knowledge/` has corrections to preserve
- Custom plugins (7) have fewer skills — extend them rather than creating new plugins