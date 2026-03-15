---
name: productivity
description: "생산성. 작업 관리, 메모리/컨텍스트 관리. 할 일 관리, 기억 저장, 컨텍스트 유지 요청 시 사용."
allowed-tools: Read, Write, Glob
---

# 생산성 (Productivity)

사용자 요청에 따라 아래 프레임워크 중 적절한 것을 선택하여 적용합니다.
`knowledge/productivity.md`가 존재하면 먼저 읽어 보정 사항을 반영합니다.

## 스킬 라우팅

| 요청 유형 | 참조 파일 |
|---|---|
| 메모리 및 컨텍스트 관리 | [plugins/productivity/skills/memory-management/SKILL.md] |
| 작업 관리 및 우선순위 | [plugins/productivity/skills/task-management/SKILL.md] |

## 사용법

1. 사용자의 요청을 위 라우팅 테이블에서 매칭
2. 해당 `references/` 파일을 Read
3. 파일의 프레임워크와 지시사항에 따라 실행
4. 작업 범위나 저장 대상이 불명확하면 사용자에게 확인
5. 결과물은 마크다운 문서로 저장
