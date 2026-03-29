# 세션 종료 의무 절차 (MANDATORY — 절대 생략 불가)

> **이 규칙은 모든 작업 규칙보다 우선한다. 세션이 끝날 때마다 반드시 실행해야 하며, 어떠한 이유로도 건너뛸 수 없다.**

## 세션 종료 체크리스트 (순서 준수)

0. **학습 지식 반영 확인**
   - 이번 세션에서 `knowledge/`에 학습된 항목이 있는지 확인
   - 동일 도메인 3건 이상 누적 시 → 해당 SKILL.md에 `## 실무 보정 사항` 자동 추가
   - `feedback-learning.md` 규칙에 따라 처리

0.5. **엔트로피 정리** ← `entropy-cleanup.md` 규칙 참조
   - fresh-context 에이전트를 스폰하여 이번 세션의 변경사항 정합성 검사
   - 스테일 주석, 미사용 임포트, 문서 불일치 자동 수정
   - 호출자 불일치, 중복 코드 등 위험 항목은 플래그하여 사용자에게 보고
   - 자동 수정분은 별도 커밋 (`chore: 세션 후 엔트로피 정리`)

0.7. **텔레메트리 기록** ← `telemetry-rubrics.md` 규칙 참조
   - `.omc/telemetry/{YYYY-MM-DD}.jsonl`에 세션 레코드 추가
   - 루브릭 기준으로 점수 산정: plan_adherence, verification_quality, context_efficiency, entropy_delta, code_quality
   - 사용자 피드백 신호 감지 시 user_feedback 필드 기록

0.8. **핸드오프 프롬프트 생성** (미완료 태스크 존재 시) ← `context-compaction.md` 규칙 참조
   - 미완료 태스크가 있으면 `.omc/state/handoff-{sessionId}.md` 생성
   - 의도, 진행상황, 핵심 결정, 주의사항, 다음 액션 포함
   - 다음 세션 시작 시 자동 주입됨

1. **_context.md 업데이트**
   - 이번 세션에서 작업한 모든 프로젝트의 `_context.md` 최신화
   - 작업 히스토리 테이블에 새 행 추가 (날짜 | 파일명 | 내용)
   - 현재 상태 및 다음 단계 갱신

2. **변경 파일 스테이징**
   ```bash
   git add [변경된 파일들]  # 구체적 파일명으로 — git add . 사용 금지
   ```
   - **projects/ 폴더는 절대 스테이징 금지** — 프로젝트 결과물은 로컬 전용, GitHub에 올리지 않음
   - `.gitignore`에 `projects/`가 등록되어 있으나, 실수로 추가되지 않도록 주의
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

## 세션 종료 트리거 조건
- 사용자가 "끝", "마무리", "종료", "그만", "나중에", "다음에" 등 종료 의사를 표현할 때
- 대화가 자연스럽게 마무리될 때
- 사용자가 다음 주제로 넘어가려 할 때

## 금지 사항
- **절대 금지**: 시스템 파일 변경 후 푸시 없이 대화 종료
- **절대 금지**: `git add .` 또는 `git add -A` 사용 (projects/ 포함 위험)
- **절대 금지**: `projects/` 폴더를 git에 추가하거나 푸시
- **절대 금지**: _context.md 미업데이트 상태로 종료
