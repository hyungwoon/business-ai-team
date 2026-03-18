---
name: pm-core
version: 1.0.0
description: "핵심 PM 운영. 로드맵 관리(Now/Next/Later, RICE, MoSCoW), 제품 지표 정의/추적/분석, 이해관계자 커뮤니케이션. 로드맵, 지표, 대시보드, 이해관계자 업데이트 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 핵심 PM 운영 (Core PM)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/product.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 로드맵 관리/우선순위화 | [plugins/product-management/skills/roadmap-management/SKILL.md] |
| 제품 지표 정의/추적/분석 | [plugins/product-management/skills/metrics-tracking/SKILL.md] |
| 이해관계자 업데이트/커뮤니케이션 | [plugins/product-management/skills/stakeholder-comms/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/product.md` (핵심 PM 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
