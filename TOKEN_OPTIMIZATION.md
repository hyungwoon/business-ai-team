# Token Optimization - Business AI Team

이 시스템의 토큰 최적화 전략과 구현 내용을 설명합니다.

---

## 최적화 현황

### 총 절감 효과 (누적)

| 항목 | 기법 | 절감 효과 |
|------|------|---------|
| Tool 정의 토큰 | 16개 → 8개 통합 Tool | 50% |
| 시스템 프롬프트 캐시 | Prompt Caching | 60~90% (캐시 히트 시) |
| 장기 세션 히스토리 | 슬라이딩 윈도우 (최근 20개) | 30% |
| Tool 재구성 방지 | 루프 외부 1회 구성 | 5~10% (반복당) |
| 모델 계층화 | Haiku (단순) / Sonnet (복잡) | 60~70% (단순 작업) |

---

## 구현 상세

### 1. 통합 Tool 패턴 (16 → 8 Tool)

**파일:** `agents/_orchestrator.md`

Claude API는 각 Tool 정의를 매 호출마다 전송합니다.
16개 에이전트를 개별 Tool로 등록하면 16개 분량의 Tool 정의 토큰이 소비됩니다.
8개 통합 Tool로 묶으면 이를 절반으로 줄입니다.

```
예: 3개 에이전트를 1개 Tool로

Tool: consult_extended_ops
  설명: 데이터 분석, 마케팅, 영업 전문가 팀 (Data, Marketing, Sales)
  파라미터:
    - action: 수행할 액션 (string)
    - params: 액션 파라미터 (object)
```

### 2. Prompt Caching (ephemeral)

**파일:** `agents/_architecture.md`, `agents/_main.md`

Anthropic의 `cache_control: {"type": "ephemeral"}` 기능을 활용합니다.
시스템 프롬프트(정적 콘텐츠)를 캐시 블록으로 전송하면
동일 세션 내 반복 호출 시 캐시 히트로 입력 토큰 60~90% 절감됩니다.

```
시스템 프롬프트 전송 구조:
  system: [
    {
      type: "text",
      text: <시스템 프롬프트 + 플러그인 스킬>,
      cache_control: { type: "ephemeral" }   ← 캐시 적용
    }
  ]

캐시 효과 확인 (API 응답의 usage 필드):
  cache_read_input_tokens      ← 캐시에서 읽은 토큰
  cache_creation_input_tokens  ← 캐시 생성 시 쓴 토큰
```

### 3. 히스토리 슬라이딩 윈도우

**파일:** `agents/_main.md`

Tool Use 사이클이 반복되면 대화 히스토리가 누적됩니다.
장기 세션에서 히스토리 무한 누적은 불필요한 컨텍스트를 낭비합니다.

```
최대 히스토리: 20개 메시지

트리밍 규칙:
  - 첫 user 메시지(원래 요청)는 항상 보존
  - 나머지는 최근 19개만 유지
  - 20개 이하면 트리밍하지 않음
```

### 4. Tool 정의 캐시

**파일:** `agents/_main.md`

Tool 정의는 세션 동안 변하지 않으므로 1회만 구성하고 재사용합니다.
루프 진입 전에 Tool 정의를 캐시하여 매 반복마다 재구성하는 비용을 방지합니다.

```
패턴:
  1. 루프 진입 전: Tool 정의 리스트 1회 생성 → 캐시에 저장
  2. 새 Tool 등록 시: 캐시 무효화 → 다음 호출에서 재생성
  3. 루프 내: 캐시된 Tool 정의 재사용
```

### 5. 모델 계층화

**파일:** `agents/_architecture.md`

모든 에이전트에 동일한 Sonnet을 쓰는 대신,
단순 작업에는 Haiku를 사용하여 비용을 절감합니다.

```
기본 모델: claude-sonnet-4-6         (복잡한 분석/전략)
경량 모델: claude-haiku-4-5-20251001 (단순 처리)

경량 모델 적용 에이전트:
  - Productivity (메모 정리, 일정 조율)
  - Writing (이메일, 문서 작성)
```

---

## 공통 아키텍처

모든 최적화 개념은 `agents/_architecture.md`에 문서화되어 있습니다.
16개 에이전트는 동일한 구조를 따르며 각각 `.md` 파일로 정의됩니다.

```
에이전트 구조:
  시스템 프롬프트     → agents/[name].md에 정의
  플러그인 스킬       → plugins/[name]/skills/에서 로드
  모델 선택          → 메타데이터의 모델 필드 참조
  Prompt Caching    → 시스템 프롬프트를 ephemeral 캐시 블록으로 전송
  표준 응답 포맷      → { success, agent, ...data }
```
