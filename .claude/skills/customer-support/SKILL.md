---
name: customer-support
description: "고객 지원. 티켓 분류, 응답 작성, 고객 조사, 에스컬레이션, 지식 관리. 고객 문의 대응, 지원 프로세스, 지식베이스 관리 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 고객 지원 (Customer Support)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/customer-support.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 티켓 분류 및 우선순위 설정 | [plugins/customer-support/skills/ticket-triage/SKILL.md] |
| 고객 응답 초안 작성 | [plugins/customer-support/skills/response-drafting/SKILL.md] |
| 고객 조사 및 분석 | [plugins/customer-support/skills/customer-research/SKILL.md] |
| 에스컬레이션 처리 | [plugins/customer-support/skills/escalation/SKILL.md] |
| 지식베이스 관리 | [plugins/customer-support/skills/knowledge-management/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 고객 문의 유형이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/sales.md` (고객지원 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
