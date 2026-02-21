# 아키텍처 개요

> 모든 전문가 에이전트의 공통 구조, 설정, 플러그인 로드 방식을 정의

## 공통 에이전트 구조 (BaseAgent 패턴)

모든 전문가 에이전트는 동일한 구조를 따른다:

1. **시스템 프롬프트**: 각 에이전트의 `.md` 파일에 정의된 전문가 역할과 원칙
2. **플러그인 스킬**: `plugins/[name]/skills/[skill]/SKILL.md`에서 베스트 프랙티스 로드
3. **모델 선택**: 작업 복잡도에 따라 Sonnet 또는 Haiku 사용
4. **Prompt Caching**: 시스템 프롬프트를 ephemeral 캐시 블록으로 전송하여 반복 호출 시 입력 토큰 60~90% 절감

## 설정

- **API 키**: 환경 변수 `ANTHROPIC_API_KEY`
- **기본 모델**: `claude-sonnet-4-6` (복잡한 분석/전략 작업)
- **경량 모델**: `claude-haiku-4-5-20251001` (단순 처리 작업 — 비용 60~70% 절감)
- **환경 파일**: `.env`

## 플러그인 로드

플러그인 스킬은 다음 경로 규칙을 따른다:
- 매니페스트: `plugins/[name]/.claude-plugin/plugin.json`
- 스킬: `plugins/[name]/skills/[skill]/SKILL.md`
- 커맨드: `plugins/[name]/commands/[command].md`

로드 방식:
1. 에이전트 메타데이터의 플러그인 목록 확인
2. 각 플러그인의 모든 스킬 또는 지정된 스킬만 로드
3. 시스템 프롬프트 뒤에 `--- [plugin]/[skill] Skill ---` 형식으로 합산

## Prompt Caching 패턴

시스템 프롬프트(정적 콘텐츠)를 캐시 블록으로 전송:

```
system: [
  {
    type: "text",
    text: <시스템 프롬프트 + 플러그인 스킬>,
    cache_control: { type: "ephemeral" }
  }
]
```

동일 세션 내 반복 호출 시 캐시 히트로 입력 토큰 대폭 절감.

## 표준 응답 포맷

- 성공: `{ success: true, agent: "<에이전트명>", ...data }`
- 실패: `{ success: false, error: "<메시지>", agent: "<에이전트명>" }`
