---
name: pm-gtm
version: 1.0.0
description: "Go-to-Market 출시 전략. GTM 수립, 교두보 시장(beachhead), ICP 정의, 성장 루프(바이럴/PLG), GTM 모션(인바운드/아웃바운드), 배틀카드. 출시, 시장 진입, ICP, 배틀카드 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# Go-to-Market 전략 (PM GTM)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| GTM 전략 수립 | [plugins/product-management/skills/gtm-strategy/SKILL.md] |
| 교두보 시장 선정 | [plugins/product-management/skills/beachhead-segment/SKILL.md] |
| ICP(이상적 고객 프로필) 정의 | [plugins/product-management/skills/ideal-customer-profile/SKILL.md] |
| 성장 루프 설계 | [plugins/product-management/skills/growth-loops/SKILL.md] |
| GTM 모션 선택 | [plugins/product-management/skills/gtm-motions/SKILL.md] |
| 경쟁 배틀카드 작성 | [plugins/product-management/skills/competitive-battlecard/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/product.md` (출시 전략 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
