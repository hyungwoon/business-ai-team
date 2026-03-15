---
name: data-analysis
description: "데이터 분석. 데이터 탐색, 시각화, 통계 분석, SQL 쿼리, 데이터 검증, 인터랙티브 대시보드. 데이터 조회, 차트, SQL, 대시보드 요청 시 사용."
allowed-tools: Read, Write, Glob, Bash
---

# 데이터 분석 (Data Analysis)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/data.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 데이터 컨텍스트 추출 | [references/data-context-extractor.md] |
| 데이터 탐색 및 EDA | [references/data-exploration.md] |
| 데이터 검증 및 품질 확인 | [references/data-validation.md] |
| 데이터 시각화 및 차트 | [references/data-visualization.md] |
| 인터랙티브 대시보드 제작 | [references/interactive-dashboard-builder.md] |
| SQL 쿼리 작성 | [references/sql-queries.md] |
| 통계 분석 | [references/statistical-analysis.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 데이터 소스나 분석 목적이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
