---
name: enterprise-search
version: 1.0.0
description: "엔터프라이즈 검색. 검색 전략, 지식 종합, 소스 관리. 정보 검색, 지식 정리, 소스 관리 요청 시 사용."
allowed-tools: Read, Write, Glob, WebSearch
---

# 엔터프라이즈 검색 (Enterprise Search)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/enterprise-search.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 지식 종합 및 정리 | [plugins/enterprise-search/skills/knowledge-synthesis/SKILL.md] |
| 검색 전략 수립 | [plugins/enterprise-search/skills/search-strategy/SKILL.md] |
| 소스 관리 | [plugins/enterprise-search/skills/source-management/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 검색 범위나 지식 도메인이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/research.md` (검색 전략 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
