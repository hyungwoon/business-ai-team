---
description: 비즈니스 질문에 전문가 관점으로 답변합니다. 에이전트와 스킬을 자동으로 로드합니다.
---

# 비즈니스 전문가 질문

사용자 질문: $ARGUMENTS

## 실행 절차

### 0단계: 경로 탐색 (로컬 우선, 글로벌 폴백)

다음 순서로 에이전트 경로를 결정한다:

1. **로컬 확인**: 현재 프로젝트에 `agents/` 폴더가 존재하는지 확인
   - 존재하면 → `AGENTS_DIR` = `agents/`, `PLUGINS_DIR` = `plugins/`
2. **글로벌 폴백**: 로컬에 없으면 `~/.claude/business-team/agents/` 존재 여부 확인
   - 존재하면 → `AGENTS_DIR` = `~/.claude/business-team/agents/`, `PLUGINS_DIR` = `~/.claude/business-team/plugins/`
3. **둘 다 없으면**: 에이전트 없이 직접 답변한다.

이후 모든 단계에서 `agents/`는 `AGENTS_DIR`, `plugins/`는 `PLUGINS_DIR`로 대체하여 참조한다.

### 1단계: 도메인 분류 및 에이전트 읽기

질문의 도메인을 파악하여 해당 `AGENTS_DIR/[에이전트].md` 파일을 Read 도구로 읽는다.
- CLAUDE.md에 매핑 테이블이 있으면 참조, 없으면 Glob으로 `AGENTS_DIR/*.md`를 스캔하여 가장 관련된 에이전트 식별

### 2단계: 스킬 읽기

에이전트 파일의 "플러그인 & 스킬 라우팅" 섹션에서 관련 `PLUGINS_DIR/[플러그인]/skills/[스킬]/SKILL.md`를 Read 도구로 읽는다.

### 3단계: 전문가 관점 응답

에이전트의 전문 관점과 스킬의 베스트 프랙티스를 반영하여 답변한다.

### 4단계: 담당 표시

응답 맨 앞에 `> **담당**: [에이전트] | 참조 스킬: [스킬]` 표시

**에이전트/스킬 파일을 읽지 않고 응답하는 것은 금지된다.**
