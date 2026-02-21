# CLAUDE.md

## 프로젝트 개요
비즈니스를 돕는 범용 AI 전문가 팀 시스템. 마케팅, 리서치, 전략 수립, 문서 작성 등 다양한 비즈니스 업무를 지원한다.

## 폴더 구조
```
business-ai-team/
├── agents/           # AI 에이전트 모듈 (시스템 프롬프트 + 전문 지식 원천)
│   └── [16개 전문가 에이전트.md] # 각 도메인별 시스템 프롬프트 + 스킬 라우팅
├── plugins/          # 16개 도메인별 플러그인 (SKILL.md = 베스트 프랙티스)
│   ├── marketing/    # brand-voice, content-creation, campaign-planning 등
│   ├── sales/        # draft-outreach, account-research, call-prep 등
│   ├── data/         # data-exploration, visualization, sql-queries 등
│   ├── finance/      # financial-statements, variance-analysis, audit-support 등
│   ├── legal/        # contract-review, legal-risk-assessment, nda-triage 등
│   ├── product-management/  # roadmap-management, feature-spec, metrics-tracking 등
│   └── [10개 추가 플러그인]
├── archive/          # 사용자 요청 결과물 보관 (컨텍스트 제외 대상)
│   ├── [프로젝트명]/              # 독립 프로젝트 폴더
│   ├── [상위프로젝트]/            # 상위 프로젝트 폴더 (하위 스쿼드/팀 포함)
│   │   ├── _context.md          # 상위 프로젝트 개요 + 스쿼드 목록
│   │   └── [스쿼드명]/          # 스쿼드별 하위 폴더
│   │       └── _context.md      # 스쿼드 작업 기록
│   └── 기타/                     # 단발성 또는 미분류 결과물
└── docs/             # 설계 문서
```

## 세션 종료 의무 절차 (MANDATORY — 절대 생략 불가)

> **이 규칙은 모든 작업 규칙보다 우선한다. 세션이 끝날 때마다 반드시 실행해야 하며, 어떠한 이유로도 건너뛸 수 없다.**

### 세션 종료 체크리스트 (순서 준수)

1. **_context.md 업데이트**
   - 이번 세션에서 작업한 모든 프로젝트의 `_context.md` 최신화
   - 작업 히스토리 테이블에 새 행 추가 (날짜 | 파일명 | 내용)
   - 현재 상태 및 다음 단계 갱신

2. **변경 파일 스테이징**
   ```bash
   git add [변경된 파일들]  # 구체적 파일명으로 — git add . 사용 금지
   ```
   - **archive/ 폴더는 절대 스테이징 금지** — 클라이언트 결과물은 로컬 전용, GitHub에 올리지 않음
   - `.gitignore`에 `archive/`가 등록되어 있으나, 실수로 추가되지 않도록 주의
   - 푸시 대상: 에이전트 코드, 설정 파일, CLAUDE.md 등 시스템 파일만

3. **커밋 (컨벤셔널 커밋 형식)**
   ```bash
   git commit -m "feat/docs/chore: 작업 내용 요약"
   ```
   - 이번 세션의 주요 작업을 명확히 기술
   - 여러 작업은 분리 커밋 또는 bullet 형식으로 기술

4. **GitHub 푸시 (필수)**
   ```bash
   git push origin main
   ```

5. **완료 확인**
   - `git status` 실행 → "커밋할 변경 사항이 없음" 확인
   - `git log --oneline -3` 으로 최신 커밋 확인

### 세션 종료 트리거 조건
- 사용자가 "끝", "마무리", "종료", "그만", "나중에", "다음에" 등 종료 의사를 표현할 때
- 대화가 자연스럽게 마무리될 때
- 사용자가 다음 주제로 넘어가려 할 때

### 금지 사항
- **절대 금지**: 시스템 파일 변경 후 푸시 없이 대화 종료
- **절대 금지**: `git add .` 또는 `git add -A` 사용 (archive/ 포함 위험)
- **절대 금지**: `archive/` 폴더를 git에 추가하거나 푸시
- **절대 금지**: _context.md 미업데이트 상태로 종료

---

## 작업 규칙

### 프로젝트 폴더링 규칙
- 사용자가 특정 클라이언트/프로젝트를 언급하면 → `archive/[프로젝트명]/` 폴더 자동 생성 후 저장
- 프로젝트명은 클라이언트명 또는 브랜드명 기준 (예: `빈센트-스튜디오`, `antiegg`)
- 동일 프로젝트 후속 작업은 기존 폴더에 누적 저장 (이전 결과물 맥락 유지)
- 단발성 요청이거나 프로젝트 맥락이 없으면 → `archive/기타/`에 저장
- 새 프로젝트 시작 시 사용자에게 확인 불필요 — 폴더명을 스스로 판단해 생성

#### 중첩 프로젝트 구조 (상위 프로젝트가 있는 경우)
- 스쿼드/팀이 상위 프로젝트(매거진, 조직 등)에 소속된 경우 → `archive/[상위프로젝트]/[스쿼드명]/` 중첩 구조 사용
- 예: `archive/[매거진명]/[스쿼드명]/`, `archive/[조직명]/[팀명]/`
- 상위 프로젝트 폴더에 `_context.md` 생성 — 전체 개요 + 하위 스쿼드 목록 역할
- 새 스쿼드 추가 시 `archive/[상위프로젝트]/[신규스쿼드]/` 폴더 생성 및 `_context.md` 작성
- 상위 `_context.md`의 스쿼드 목록 테이블도 함께 업데이트

### 결과물 저장
- 사용자 요청으로 생성한 리서치, 전략, 기획 문서 → `archive/[프로젝트명]/` 폴더에 저장
- archive 폴더는 에이전트 검색/참조 대상에서 제외
- 코드, 시스템 문서는 루트 또는 해당 폴더에 저장

### 파일명 규칙
- **날짜 접두어 필수**: `YYYY-MM-DD_` 형식으로 작성일을 앞에 붙임
- 한글 파일명 사용 가능
- 내용을 명확히 알 수 있는 이름 사용 (프로젝트명 접두어 불필요 — 폴더가 맥락 역할)
- 예: `archive/빈센트-스튜디오/2026-02-20_3월_콘텐츠_플랜.md`

### _context.md 자동 관리 규칙
- 각 프로젝트 폴더에는 반드시 `_context.md` 유지 (`_` 접두어로 목록 최상단 노출)
- **새 프로젝트 시작 시**: `_context.md` 생성 (클라이언트 개요, 방향성, 작업 히스토리 테이블 포함)
- **결과물 저장 시마다**: `_context.md`의 작업 히스토리 테이블에 새 행 추가 + 현재 상태 업데이트
- **_context.md 필수 구성 요소**:
  - 클라이언트 개요 (업종, 담당자, 채널 등)
  - 브랜드/프로젝트 방향성 및 주요 결정사항
  - 작업 히스토리 (날짜 | 파일명 | 내용 테이블)
  - 현재 상태 (최신 날짜 기준)
  - 다음 단계
- **프로젝트 재개 시**: `_context.md` 먼저 읽어 맥락 파악 후 작업 시작
- **중첩 구조 재개 시**: 상위 `_context.md` → 해당 스쿼드 `_context.md` 순으로 읽어 전체 맥락 파악

### 에이전트 지식 관리 원칙
- `agents/*.md`의 시스템 프롬프트는 각 도메인의 전문 지식 원천
- `plugins/*/skills/*/SKILL.md`는 도메인별 베스트 프랙티스
- 에이전트 문서 수정 시 해당 도메인의 전문성이 CLI 세션에도 자동 반영됨
- 새 도메인 추가 시: 에이전트 .md 생성 + 플러그인 스킬 추가 + 라우팅 테이블 갱신

## 문서 작성 스타일
- 기본 언어: 한국어
- 마크다운 포맷 사용
- 실용적이고 실행 가능한 내용 중심
- 불필요한 장식(이모지 등) 최소화

## 운영 환경
- **실행**: Claude Code CLI (별도 API 키 불필요)
- **지식 원천**: `agents/` (시스템 프롬프트) + `plugins/` (SKILL.md)
- **결과물 저장**: `archive/` (로컬 전용, Git 제외)

---

## 전문가 라우팅 시스템 (CLI 세션용)

> **CLI에서 비즈니스 요청을 받으면, 해당 전문가 에이전트의 시스템 프롬프트와 플러그인 스킬을 읽어서 그 관점으로 응답한다.**

### 라우팅 절차

1. **요청 분류**: 사용자 요청의 도메인을 파악
2. **에이전트 참조**: 해당 에이전트의 `.md` 파일에서 시스템 프롬프트 읽기
3. **플러그인 스킬 로드**: 해당 에이전트가 사용하는 `plugins/[name]/skills/[skill]/SKILL.md` 읽기
4. **전문가 관점 적용**: 에이전트의 전문 분야, 원칙, 플러그인 지식을 반영하여 응답
5. **복합 요청**: 여러 도메인에 걸친 요청은 관련 에이전트 여러 개를 참조

### 에이전트-플러그인 매핑 테이블

| 요청 키워드 | 에이전트 | 파일 | 플러그인 스킬 |
|---|---|---|---|
| 작업관리, 일정, 메모, 생산성 | Productivity | `agents/productivity.md` | `productivity/` → task-management, memory-management |
| 리서치, 조사, 경쟁사분석, 트렌드 | Research | `agents/research.md` | `marketing/` → competitive-analysis · `sales/` → account-research, competitive-intelligence · `data/` → data-exploration |
| 이메일, 문서작성, 번역, 요약 | Writing | `agents/writing.md` | `marketing/` → brand-voice, content-creation · `sales/` → draft-outreach, create-an-asset · `customer-support/` → response-drafting |
| 마케팅, 캠페인, 콘텐츠, 브랜드 | Marketing | `agents/marketing.md` | `marketing/` → brand-voice, content-creation, campaign-planning, competitive-analysis, performance-analytics |
| 영업, 파이프라인, 제안서, CRM | Sales | `agents/sales.md` | `sales/` → draft-outreach, create-an-asset, daily-briefing, account-research, competitive-intelligence, call-prep |
| 데이터분석, 시각화, 인사이트, 통계 | Data | `agents/data.md` | `data/` → data-exploration, data-visualization, statistical-analysis, sql-queries, data-validation, data-context-extractor, interactive-dashboard-builder |
| 계약검토, 법률자문, 규정 | Legal | `agents/legal.md` | `legal/` → contract-review, legal-risk-assessment, compliance, nda-triage, canned-responses, meeting-briefing |
| 컴플라이언스, 리스크, 감사 | Compliance | `agents/compliance.md` | `compliance/` → risk-management |
| 재무분석, 예산, 투자, ROI | Finance | `agents/finance.md` | `finance/` → financial-statements, variance-analysis, journal-entry-prep, reconciliation, audit-support, close-management |
| 사업개발, 파트너십, 성장전략, M&A | BizDev | `agents/business-dev.md` | `business-dev/` → growth-strategy |
| 제품전략, 로드맵, 기능스펙, PM | Product | `agents/product.md` | `product-management/` → roadmap-management, feature-spec, user-research-synthesis, competitive-analysis, metrics-tracking, stakeholder-comms |
| 기술아키텍처, 개발프로세스, CTO | Development | `agents/development.md` | `development/` → tech-leadership |
| UX/UI, 브랜드가이드, 디자인시스템 | Design | `agents/design.md` | `design/` → ux-design |
| 채용, 조직문화, 성과관리, HR | HR | `agents/hr.md` | `hr/` → talent-management |
| 보도자료, 위기관리, 미디어전략 | PR | `agents/pr.md` | `pr/` → communications |
| 보안평가, 보안정책, 사이버보안 | Security | `agents/security.md` | `security/` → cybersecurity |

### 복합 요청 라우팅 예시

- "신규 SaaS 런칭 전략" → Research + Product + Marketing + Sales
- "시리즈A 투자 준비" → Finance + Legal + BizDev + Product
- "해외 진출 검토" → Research + Legal + Compliance + BizDev
- "마케팅 캠페인 성과 분석" → Marketing + Data
- "신규 채용 및 팀 빌딩" → HR + Finance + Product

### 응답 시 에이전트 표시 (필수)

비즈니스 요청에 응답할 때, **본문 맨 앞에** 어떤 에이전트가 참여했는지 표시한다:

```
> **담당**: Marketing + Data | 참조 스킬: campaign-planning, performance-analytics
```

- 단일 에이전트: `> **담당**: Marketing | 참조 스킬: content-creation`
- 복합 에이전트: `> **담당**: Research + Product + Marketing | 참조 스킬: competitive-analysis, feature-spec, campaign-planning`
- 일반 대화(비즈니스 도메인 아님): 표시 생략

### 라우팅 원칙

- **단일 도메인 요청**: 해당 에이전트 1개의 시스템 프롬프트 + 플러그인 스킬 참조
- **복합 도메인 요청**: 주 에이전트의 관점을 중심으로, 보조 에이전트의 전문성 보충
- **플러그인 스킬은 필요 시에만**: 모든 스킬을 매번 읽지 않고, 요청과 직접 관련된 스킬만 선택적으로 로드
- **에이전트 문서가 진실의 원천**: CLAUDE.md의 매핑은 라우팅 가이드일 뿐, 실제 시스템 프롬프트와 스킬 내용은 항상 파일에서 직접 읽기
