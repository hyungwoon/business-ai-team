---
name: pm-discovery
description: "제품 디스커버리. 아이디어 브레인스토밍, 가정 식별/우선순위화, 실험 설계, 기회-솔루션 트리, 고객 인터뷰. 기존/신규 제품 모두 지원. 디스커버리, 아이디에이션, 가정 검증, 실험 설계, 인터뷰 스크립트 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# 제품 디스커버리 (Product Discovery)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 기존 제품 아이디어 브레인스토밍 | [plugins/product-management/skills/brainstorm-ideas-existing/SKILL.md] |
| 신규 제품 아이디어 브레인스토밍 | [plugins/product-management/skills/brainstorm-ideas-new/SKILL.md] |
| 기존 제품 실험 설계 | [plugins/product-management/skills/brainstorm-experiments-existing/SKILL.md] |
| 신규 제품 실험 설계 | [plugins/product-management/skills/brainstorm-experiments-new/SKILL.md] |
| 기존 제품 가정 식별 | [plugins/product-management/skills/identify-assumptions-existing/SKILL.md] |
| 신규 제품 가정 식별 | [plugins/product-management/skills/identify-assumptions-new/SKILL.md] |
| 가정 우선순위화 | [plugins/product-management/skills/prioritize-assumptions/SKILL.md] |
| 기능 우선순위화 | [plugins/product-management/skills/prioritize-features/SKILL.md] |
| 기능 요청 분석 | [plugins/product-management/skills/analyze-feature-requests/SKILL.md] |
| 기회-솔루션 트리 | [plugins/product-management/skills/opportunity-solution-tree/SKILL.md] |
| 인터뷰 스크립트 작성 | [plugins/product-management/skills/interview-script/SKILL.md] |
| 인터뷰 요약 | [plugins/product-management/skills/summarize-interview/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 기존 vs 신규가 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
