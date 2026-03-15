---
name: plugin-management
description: "플러그인 관리. 기존 플러그인 커스터마이징, 신규 플러그인 생성. 플러그인 수정, 새 플러그인 만들기 요청 시 사용."
allowed-tools: Read, Write, Glob, Bash
---

# 플러그인 관리 (Plugin Management)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/plugin-management.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 기존 플러그인 커스터마이징 | [plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md] |
| 신규 플러그인 생성 | [plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 수정 대상 플러그인이나 생성 목적이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장

## 참조 원본

이 라우팅 테이블의 원본은 `agents/development.md` (플러그인 관리 섹션)입니다.
스킬 추가/삭제 시 에이전트 파일을 먼저 업데이트하고, 이 파일도 동기화하세요.
`/health` 커맨드로 동기화 상태를 확인할 수 있습니다.
