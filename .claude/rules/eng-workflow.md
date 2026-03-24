# 엔지니어링 워크플로우 스킬

> [garrytan/gstack](https://github.com/garrytan/gstack) 기반. `.claude/skills/`에 플랫 구조로 통합.

## 사용 가능한 스킬

| 커맨드 | 모드 | 용도 |
|---|---|---|
| `/plan-ceo-review` | Founder/CEO | 문제 재정의, 10-star product 발견, 스코프 확장/유지/축소 모드 |
| `/plan-eng-review` | Eng Manager | 아키텍처, 데이터 흐름, 보안, 배포 전략 심층 리뷰 |
| `/review` | Staff Engineer | CI 통과하지만 프로덕션에서 터지는 버그 탐지 |
| `/ship` | Release Engineer | main 동기화 → 테스트 → 푸시 → PR 생성 자동화 |
| `/browse` | QA Engineer | 헤드리스 브라우저로 페이지 조작, 스크린샷, 콘솔 에러 확인 |
| `/qa` | QA Lead | git diff 분석 → 영향받는 페이지 자동 테스트 → QA 리포트 |
| `/setup-browser-cookies` | Session Manager | 실제 브라우저(Chrome, Arc 등)에서 쿠키 가져오기 |
| `/eng-retro` | Eng Manager | git 커밋 분석 기반 주간 엔지니어링 회고 |

## 브라우저 스킬 (`/browse`, `/qa`, `/setup-browser-cookies`)

- **최초 실행 시 빌드 필요**: `cd .claude/skills/browse && ./setup` (Bun 필요)
- **이후 ~100ms/커맨드** — 지속형 Chromium 데몬, 30분 미사용 시 자동 종료
- 쿠키/탭/localStorage 세션 간 유지

## 팀원 설정 (최초 1회)
```bash
cd .claude/skills/browse && ./setup
# Bun 미설치 시: curl -fsSL https://bun.sh/install | bash
```
