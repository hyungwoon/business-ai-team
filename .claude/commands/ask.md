---
description: 비즈니스 + 엔지니어링 질문에 전문가 관점으로 답변합니다. 에이전트, 플러그인 스킬, 네이티브 스킬을 자동으로 로드합니다.
---

# 전문가 질문

사용자 질문: $ARGUMENTS

## 실행 절차

### 0단계: 경로 탐색 (로컬 우선, 글로벌 폴백)

다음 순서로 에이전트 경로를 결정한다:

1. **로컬 확인**: 현재 프로젝트에 `agents/` 폴더가 존재하는지 확인
   - 존재하면 → `AGENTS_DIR` = `agents/`, `PLUGINS_DIR` = `plugins/`, `KNOWLEDGE_DIR` = `knowledge/`
2. **글로벌 폴백**: 로컬에 없으면 `~/.claude/business-team/agents/` 존재 여부 확인
   - 존재하면 → `AGENTS_DIR` = `~/.claude/business-team/agents/`, `PLUGINS_DIR` = `~/.claude/business-team/plugins/`, `KNOWLEDGE_DIR` = `~/.claude/business-team/knowledge/`
3. **둘 다 없으면**: 에이전트 없이 직접 답변한다.

이후 모든 단계에서 `agents/`는 `AGENTS_DIR`, `plugins/`는 `PLUGINS_DIR`, `knowledge/`는 `KNOWLEDGE_DIR`로 대체하여 참조한다.

### 0.5단계: 기존 맥락 확인

현재 대화에서 이미 프로젝트 맥락이 로드되어 있다면 (`_context.md` 참조 이력), 해당 맥락을 활용한다.

### 1단계: 과업 감지 및 전환 안내

질문이 사실 확인이 아니라 **과업 요청**(결과물 생성 필요)인 경우:

```
이 요청은 결과물이 필요한 과업이네요. `/route`로 전환하면 더 체계적인 결과를 드릴 수 있습니다.

바로 여기서 답변할까요, 아니면 `/route`로 전환할까요?
```

사용자가 여기서 답변을 원하면 그대로 진행.

### 2단계: 도메인 분류 — 비즈니스 + 엔지니어링 동시 판별

요청을 분석하여 **두 경로 중 해당하는 것을 모두** 활성화한다:

**A. 비즈니스 도메인 (agents/ → plugins/)**
- CLAUDE.md 매핑 테이블에서 에이전트 식별
- 해당 `AGENTS_DIR/[에이전트].md` 파일을 Read

**B. 엔지니어링 워크플로우 (.claude/skills/ 직접)**
- 아래 키워드 매칭 시 해당 네이티브 스킬을 직접 Read:

| 키워드 | 네이티브 스킬 |
|---|---|
| 코드 리뷰, PR 리뷰, 코드 검토 | `.claude/skills/review/SKILL.md` |
| 브라우저 테스트, 스크린샷, 페이지 확인 | `.claude/skills/browse/SKILL.md` |
| QA, 품질 테스트, 버그 찾기 | `.claude/skills/qa/SKILL.md` |
| 릴리스, 배포, PR 생성, 푸시 | `.claude/skills/ship/SKILL.md` |
| 플랜 리뷰, 제품 리뷰 (CEO 모드) | `.claude/skills/plan-ceo-review/SKILL.md` |
| 설계 리뷰, 아키텍처 리뷰 | `.claude/skills/plan-eng-review/SKILL.md` |
| 회고, 주간 리뷰, 개발 현황 | `.claude/skills/eng-retro/SKILL.md` |
| 쿠키, 로그인 세션 | `.claude/skills/setup-browser-cookies/SKILL.md` |

**복합 요청**: A와 B 모두 해당하면 둘 다 로드. 예: "PRD 작성하고 코드 리뷰해줘" → Product 에이전트 + review 네이티브 스킬

### 2.5단계: 학습 지식 읽기

`KNOWLEDGE_DIR`이 존재하면:

1. `KNOWLEDGE_DIR/[도메인].md` 읽기 (해당 도메인의 학습 지식)
2. `KNOWLEDGE_DIR/preferences.md` 읽기 (공통 선호도)
3. 항목이 존재하면 → 응답 시 학습된 보정 사항을 **우선 반영**
4. 항목이 없거나 디렉토리가 없으면 → 스킵

### 3단계: 스킬 읽기

에이전트 파일의 "플러그인 & 스킬 라우팅" 섹션에서 관련 `PLUGINS_DIR/[플러그인]/skills/[스킬]/SKILL.md`를 Read 도구로 읽는다.

### 4단계: 전문가 관점 응답

에이전트의 전문 관점과 스킬의 베스트 프랙티스를 반영하고,
학습 지식의 보정 사항을 우선 반영하여 답변한다.

### 5단계: 담당 표시

응답 맨 앞에 담당 표시:
- 비즈니스: `> **담당**: [에이전트] | 참조 스킬: [스킬]`
- 엔지니어링: `> **담당**: Engineering | 참조 스킬: [네이티브 스킬]`
- 복합: `> **담당**: [에이전트] + Engineering | 참조 스킬: [스킬], [네이티브 스킬]`

**에이전트/스킬 파일을 읽지 않고 응답하는 것은 금지된다.**
