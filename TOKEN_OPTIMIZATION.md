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

**파일:** `agents/team_orchestrator.py`

Claude API는 각 Tool 정의를 매 호출마다 전송합니다.
16개 에이전트를 개별 Tool로 등록하면 16개 분량의 Tool 정의 토큰이 소비됩니다.
8개 통합 Tool로 묶으면 이를 절반으로 줄입니다.

```python
# 예: 3개 에이전트를 1개 Tool로
main_agent.register_tool(
    name="consult_extended_ops",
    description="데이터 분석, 마케팅, 영업 전문가 팀 (DataAgent, MarketingAgent, SalesAgent)",
    parameters={
        "action": {"type": "string", "description": "수행할 액션"},
        "params": {"type": "object", "description": "액션 파라미터"}
    },
    handler=handle_extended_ops
)
```

### 2. Prompt Caching (ephemeral)

**파일:** `agents/base_agent.py`, `agents/main_agent.py`

Anthropic의 `cache_control: {"type": "ephemeral"}` 기능을 활용합니다.
시스템 프롬프트(정적 콘텐츠)를 캐시 블록으로 전송하면
동일 세션 내 반복 호출 시 캐시 히트로 입력 토큰 60~90% 절감됩니다.

```python
# base_agent.py의 _call_llm 메서드
response = self.client.messages.create(
    model=self._get_model(),
    max_tokens=max_tokens,
    system=[
        {
            "type": "text",
            "text": self.system_prompt,
            "cache_control": {"type": "ephemeral"},  # 캐시 적용
        }
    ],
    messages=[{"role": "user", "content": prompt}],
)
```

캐시 효과 확인:
```python
# API 응답의 usage 필드에서 확인
response.usage.cache_read_input_tokens       # 캐시에서 읽은 토큰
response.usage.cache_creation_input_tokens   # 캐시 생성 시 쓴 토큰
```

### 3. 히스토리 슬라이딩 윈도우

**파일:** `agents/main_agent.py`

Tool Use 사이클이 반복되면 대화 히스토리가 누적됩니다.
장기 세션에서 히스토리 무한 누적은 불필요한 컨텍스트를 낭비합니다.

```python
MAX_HISTORY_MESSAGES = 20

def _trim_history(self, messages: list) -> list:
    """첫 user 메시지(원래 요청)는 보존, 최근 N개만 유지"""
    if len(messages) <= MAX_HISTORY_MESSAGES:
        return messages
    return [messages[0]] + messages[-(MAX_HISTORY_MESSAGES - 1):]
```

### 4. Tool 정의 캐시

**파일:** `agents/main_agent.py`

기존 코드는 `process_request` 루프마다 `tools_for_claude` 리스트를 재구성했습니다.
동일 세션에서 Tool 정의는 변하지 않으므로 1회만 구성하고 재사용합니다.

```python
def _get_tools_for_claude(self) -> list:
    """Tool 정의를 캐시하여 반복 재구성 방지"""
    if self._tools_cache is None:
        self._tools_cache = [...]
    return self._tools_cache

# 루프 진입 전 1회 호출
tools_for_claude = self._get_tools_for_claude()
while iterations < max_iterations:
    response = client.messages.create(tools=tools_for_claude, ...)
```

### 5. 모델 계층화

**파일:** `core/config.py`, `agents/base_agent.py`

모든 에이전트에 동일한 Sonnet을 쓰는 대신,
단순 작업에는 Haiku를 사용하여 비용을 절감합니다.

```python
# config.py
model_name: str = "claude-sonnet-4-5"               # 복잡한 분석/전략
model_name_light: str = "claude-haiku-4-5-20251001"  # 단순 처리

# 적용 에이전트
ProductivityAgent(use_light_model=True)  # 메모 정리, 일정 조율
WritingAgent(use_light_model=True)       # 이메일, 문서 작성
```

---

## BaseAgent 클래스

모든 최적화 로직은 `agents/base_agent.py`의 `BaseAgent`에 집중되어 있습니다.
16개 에이전트는 모두 `BaseAgent`를 상속하며 중복 코드 없이 동일한 최적화를 적용받습니다.

```python
class MyAgent(BaseAgent):
    def __init__(self):
        super().__init__(plugin_names=["marketing"], use_light_model=False)
        self.system_prompt = self._build_system_prompt("당신은 ... 전문가입니다.")

    async def do_task(self, input: str) -> dict:
        return self._ok(result=self._call_llm(f"...", max_tokens=2000))
```

BaseAgent가 제공하는 것:
- `_call_llm()` - Prompt Caching이 적용된 LLM 호출
- `_get_model()` - 모델 계층화 (light/standard)
- `_build_system_prompt()` - 플러그인 스킬 통합
- `_ok() / _err()` - 표준 응답 포맷
