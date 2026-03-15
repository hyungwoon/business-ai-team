---
name: pm-execution
description: "제품 실행. PRD 작성, OKR 설정, 로드맵 전환, 스프린트 계획/회고, 릴리스 노트, 사전 부검, 이해관계자 맵, 회의록, 유저 스토리/잡 스토리, 테스트 시나리오, 더미 데이터, 우선순위 프레임워크. 실행, 문서 작성, 스프린트, PRD 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 제품 실행 (Product Execution)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| PRD 작성 | [plugins/product-management/skills/create-prd/SKILL.md] |
| OKR 설정 | [plugins/product-management/skills/brainstorm-okrs/SKILL.md] |
| 아웃컴 로드맵 전환 | [plugins/product-management/skills/outcome-roadmap/SKILL.md] |
| 스프린트 계획 | [plugins/product-management/skills/sprint-plan/SKILL.md] |
| 스프린트 회고 | [plugins/product-management/skills/retro/SKILL.md] |
| 릴리스 노트 작성 | [plugins/product-management/skills/release-notes/SKILL.md] |
| 사전 부검 (Pre-mortem) | [plugins/product-management/skills/pre-mortem/SKILL.md] |
| 이해관계자 맵 | [plugins/product-management/skills/stakeholder-map/SKILL.md] |
| 회의록 요약 | [plugins/product-management/skills/summarize-meeting/SKILL.md] |
| 유저 스토리 작성 | [plugins/product-management/skills/user-stories/SKILL.md] |
| 잡 스토리 작성 | [plugins/product-management/skills/job-stories/SKILL.md] |
| WWAS 분석 | [plugins/product-management/skills/wwas/SKILL.md] |
| 테스트 시나리오 설계 | [plugins/product-management/skills/test-scenarios/SKILL.md] |
| 더미 데이터 생성 | [plugins/product-management/skills/dummy-dataset/SKILL.md] |
| 우선순위 프레임워크 | [plugins/product-management/skills/prioritization-frameworks/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 문서 산출물은 마크다운으로 저장
5. 복수 문서가 필요하면 순서대로 생성

## 참조 원본

이 라우팅 테이블의 원본은 `agents/product.md` (실행 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
