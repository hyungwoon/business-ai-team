---
name: pm-analytics
description: "제품 코호트/A/B 테스트 분석. 코호트별 리텐션/이탈 패턴, A/B 테스트 통계적 유의성/신뢰구간/출시 권고. 코호트, A/B 테스트, 리텐션 분석 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 제품 데이터 분석 (PM Analytics)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 코호트 리텐션/이탈 분석 | [plugins/product-management/skills/cohort-analysis/SKILL.md] |
| A/B 테스트 결과 해석 | [plugins/product-management/skills/ab-test-analysis/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 결과물은 마크다운 문서로 저장
