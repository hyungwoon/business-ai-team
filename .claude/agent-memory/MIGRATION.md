# Knowledge → Agent Memory 마이그레이션

## 마이그레이션 날짜: 2026-03-31

## 변경 내역
- `knowledge/` → `.claude/agent-memory/` 구조 전환
- Claude Code 네이티브 에이전트 메모리와 호환 (`memory: project` frontmatter)
- 에이전트 프롬프트에 자동 주입 (loadAgentMemoryPrompt)

## 구조
- `_shared/`: 모든 에이전트 공통 (preferences 등)
- `<agentType>/`: 에이전트별 학습 지식
- 각 에이전트 디렉토리 내 `learned-knowledge.md`: 학습된 보정/노하우/주의사항

## 이전 knowledge/ 디렉토리
원본은 `knowledge/`에 보존 (호환성). 향후 `.claude/agent-memory/`로 완전 전환 예정.

## 새 학습 저장 위치
앞으로 새 학습은 `.claude/agent-memory/<도메인>/learned-knowledge.md`에 저장.
