---
name: marketing
version: 1.0.0
description: "마케팅. 브랜드 보이스, 캠페인 기획, 경쟁 분석, 콘텐츠 제작, 퍼포먼스 분석. 마케팅 전략, 캠페인, 콘텐츠, 광고 성과 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# 마케팅 (Marketing)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/marketing.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 브랜드 보이스 정의 및 적용 | [plugins/marketing/skills/brand-voice/SKILL.md] |
| 캠페인 기획 | [plugins/marketing/skills/campaign-planning/SKILL.md] |
| 경쟁사 분석 | [plugins/marketing/skills/competitive-analysis/SKILL.md] |
| 콘텐츠 제작 | [plugins/marketing/skills/content-creation/SKILL.md] |
| 퍼포먼스 분석 | [plugins/marketing/skills/performance-analytics/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 타겟 채널이나 캠페인 목표가 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/marketing.md`입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
