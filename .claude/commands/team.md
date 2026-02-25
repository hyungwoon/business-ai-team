---
description: 현재 사용 가능한 전문가 에이전트 팀과 보유 스킬 목록을 표시합니다.
---

# 전문가 팀 목록 표시

## 실행 절차

### 0단계: 경로 탐색 (로컬 우선, 글로벌 폴백)

다음 순서로 에이전트 경로를 결정한다:

1. **로컬 확인**: 현재 프로젝트에 `agents/` 폴더가 존재하는지 확인
   - 존재하면 → `AGENTS_DIR` = `agents/`, `PLUGINS_DIR` = `plugins/`, 소스 표시 = "(로컬)"
2. **글로벌 폴백**: 로컬에 없으면 `~/.claude/business-team/agents/` 존재 여부 확인
   - 존재하면 → `AGENTS_DIR` = `~/.claude/business-team/agents/`, `PLUGINS_DIR` = `~/.claude/business-team/plugins/`, 소스 표시 = "(글로벌)"
3. **둘 다 없으면**: "에이전트 팀이 설정되어 있지 않습니다. business-ai-team 프로젝트에서 ./install.sh를 실행하세요." 안내.

### 1단계: 에이전트 스캔

`AGENTS_DIR`의 모든 .md 파일 목록을 Glob으로 확인한다.

### 2단계: 스킬 스캔

`PLUGINS_DIR`의 모든 SKILL.md 파일 목록을 Glob으로 확인한다.

### 3단계: 팀 구성 출력

각 에이전트 파일의 첫 줄 설명(> 인용문)을 읽어 전문 분야를 채우고,
각 에이전트의 플러그인 & 스킬 라우팅 섹션에서 스킬 목록을 추출한다.

## 출력 형식

```
## 전문가 팀 구성 [소스 표시]

| 에이전트 | 전문 분야 | 보유 스킬 |
|----------|-----------|-----------|
| Marketing | 마케팅 | brand-voice, content-creation, ... |
| Sales | 영업 | draft-outreach, call-prep, ... |
| ... | ... | ... |

## 사용법

- `/route [비즈니스 요청]` — 전문가 라우팅으로 응답
- `/ask [질문]` — 간편 전문가 질문
- 일반 대화에서도 비즈니스 요청 시 자동 라우팅됩니다
```
