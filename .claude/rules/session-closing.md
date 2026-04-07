# 세션 종료 의무 절차

> 세션이 끝날 때마다 실행한다. 단순하게 3단계.

## 세션 종료 체크리스트

### 1. _context.md 업데이트 (프로젝트 작업 시)
- 이번 세션에서 작업한 프로젝트의 `_context.md` 최신화
- 작업 히스토리 테이블에 새 행 추가 (날짜 | 파일명 | 내용)
- 현재 상태 및 다음 단계 갱신
- 미완료 태스크 있으면 다음 액션 명시

### 2. 커밋 & 푸시
- `git add [구체적 파일명]` — `git add .` 사용 금지 (projects/ 유출 위험)
- `git commit -m "feat/docs/chore: 작업 내용 요약"` (컨벤셔널 커밋)
- `git push origin main`
- **projects/ 폴더는 절대 스테이징 금지**

### 3. 완료 확인
- `git status` → 커밋할 변경 사항 없음 확인
- `git log --oneline -3` 으로 최신 커밋 확인

## 선택적 추가 단계 (필요 시만)
- **학습 지식 반영**: `knowledge/`에 3건+ 누적 시 SKILL.md에 반영 (`feedback-learning.md` 참조)
- **Worklog 전파**: `worklog-enforcement.md` 참조 (Daily + Project + Task)
- **핸드오프 생성**: 미완료 태스크 시 `.omc/state/handoff-{sessionId}.md` 생성 (`context-compaction.md` 참조)

## 세션 종료 트리거 조건
- 사용자가 "끝", "마무리", "종료", "그만", "나중에", "다음에" 등 종료 의사를 표현할 때
- 대화가 자연스럽게 마무리될 때

## 금지 사항
- 시스템 파일 변경 후 푸시 없이 대화 종료 금지
- `git add .` 또는 `git add -A` 사용 금지 (projects/ 포함 위험)
- `projects/` 폴더를 git에 추가하거나 푸시 금지