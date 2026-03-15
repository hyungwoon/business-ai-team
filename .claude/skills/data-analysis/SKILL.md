---
name: data-analysis
description: "범용 데이터 분석. SQL 쿼리, 데이터 탐색/검증/시각화, 통계 분석, 인터랙티브 대시보드. 데이터 조회, SQL, 차트, 대시보드, 통계 요청 시 사용."
allowed-tools: Read, Write, Glob, Bash
---

# 데이터 분석 (Data Analysis)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/data.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 데이터 컨텍스트 추출 | [plugins/data/skills/data-context-extractor/SKILL.md] |
| 데이터 탐색 및 EDA | [plugins/data/skills/data-exploration/SKILL.md] |
| 데이터 검증 및 품질 확인 | [plugins/data/skills/data-validation/SKILL.md] |
| 데이터 시각화 및 차트 | [plugins/data/skills/data-visualization/SKILL.md] |
| 인터랙티브 대시보드 제작 | [plugins/data/skills/interactive-dashboard-builder/SKILL.md] |
| SQL 쿼리 작성 | [plugins/data/skills/sql-queries/SKILL.md] |
| 통계 분석 | [plugins/data/skills/statistical-analysis/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 데이터 소스나 분석 목적이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
