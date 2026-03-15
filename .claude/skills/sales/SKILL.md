---
name: sales
description: "영업. 아웃리치 작성, 영업 자료 제작, 데일리 브리핑, 어카운트 리서치, 경쟁 인텔리전스, 콜 준비. 영업 전략, 제안서, 고객 분석 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# 영업 (Sales)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/sales.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 어카운트 리서치 | [plugins/sales/skills/account-research/SKILL.md] |
| 콜 준비 | [plugins/sales/skills/call-prep/SKILL.md] |
| 경쟁 인텔리전스 | [plugins/sales/skills/competitive-intelligence/SKILL.md] |
| 영업 자료 제작 | [plugins/sales/skills/create-an-asset/SKILL.md] |
| 데일리 브리핑 | [plugins/sales/skills/daily-briefing/SKILL.md] |
| 아웃리치 초안 작성 | [plugins/sales/skills/draft-outreach/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 타겟 고객이나 영업 단계가 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/sales.md`입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
