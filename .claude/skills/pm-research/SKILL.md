---
name: pm-research
version: 1.0.0
description: "사용자/시장 리서치. 페르소나, 세그먼트, 고객 여정 지도, TAM/SAM/SOM 시장 규모, 경쟁사 프로파일링, 감성 분석. 사용자 조사, 시장 규모, 경쟁사, 페르소나 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# 시장 리서치 (PM Research)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 사용자 페르소나 작성 | [plugins/product-management/skills/user-personas/SKILL.md] |
| 시장 세그먼트 분석 | [plugins/product-management/skills/market-segments/SKILL.md] |
| 고객 세분화 | [plugins/product-management/skills/user-segmentation/SKILL.md] |
| 고객 여정 지도 | [plugins/product-management/skills/customer-journey-map/SKILL.md] |
| 시장 규모 산정(TAM/SAM/SOM) | [plugins/product-management/skills/market-sizing/SKILL.md] |
| 경쟁사 분석 | [plugins/product-management/skills/competitor-analysis/SKILL.md] |
| 감성/리뷰 분석 | [plugins/product-management/skills/sentiment-analysis/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/product.md` (시장 리서치 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
