---
name: legal
description: "법무. 계약 검토, 법적 리스크 평가, 컴플라이언스, NDA 분류, 법률 답변 템플릿, 미팅 브리핑. 계약서, 법적 리스크, NDA, 법률 자문 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 법무 (Legal)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/legal.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 법률 답변 템플릿 | [references/canned-responses.md] |
| 컴플라이언스 검토 | [references/compliance.md] |
| 계약서 검토 | [references/contract-review.md] |
| 법적 리스크 평가 | [references/legal-risk-assessment.md] |
| 미팅 브리핑 준비 | [references/meeting-briefing.md] |
| NDA 분류 및 검토 | [references/nda-triage.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 계약 유형이나 관할 법률이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
