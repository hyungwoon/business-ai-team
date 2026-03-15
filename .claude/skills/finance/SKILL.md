---
name: finance
description: "재무 관리. 재무 분석, 재무제표, 차이 분석, 분개 준비, 계정 조정, 감사 지원, 결산 관리. 재무 분석, 결산, 감사, 예산 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 재무 관리 (Finance)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/finance.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 감사 지원 | [references/audit-support.md] |
| 결산 관리 | [references/close-management.md] |
| 재무 분석 | [references/financial-analysis.md] |
| 재무제표 작성 | [references/financial-statements.md] |
| 분개 준비 | [references/journal-entry-prep.md] |
| 계정 조정 | [references/reconciliation.md] |
| 차이 분석 | [references/variance-analysis.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 재무 기간이나 분석 범위가 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
