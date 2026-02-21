"""
Business AI Team - Productivity Agent
작업 관리, 일정, 메모, 할일 등 생산성 지원
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class ProductivityAgent(BaseAgent):
    """
    Productivity Agent - "생산성 전문가"

    작업 관리, 일정 조율, 메모 정리, 할일 추적을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["productivity"], use_light_model=True)

        base_prompt = """당신은 생산성 전문가입니다.
사용자의 작업, 일정, 메모를 효율적으로 관리하고 조직화합니다.

전문 분야:
- 📋 작업 관리 및 우선순위 설정
- 📅 일정 조율 및 시간 관리
- 📝 메모 정리 및 구조화
- ✅ 할일 목록 관리 및 추적
- 🎯 목표 설정 및 진행 상황 모니터링

원칙:
- 명확하고 실행 가능한 작업으로 분해
- 우선순위를 고려한 스케줄링
- 체계적인 정보 조직화
- 효율적인 워크플로우 제안
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Productivity Best Practices")

    async def manage_tasks(self, request: str, tasks: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """작업 관리 (생성, 우선순위 설정, 정리)"""
        tasks_str = ""
        if tasks:
            tasks_str = "\n현재 작업 목록:\n" + "\n".join([f"- {t.get('title', str(t))}" for t in tasks])

        prompt = f"""사용자 요청: {request}

{tasks_str}

위 요청을 분석하고 다음을 제공해주세요:
1. 추천 작업 목록 (구체적이고 실행 가능한)
2. 각 작업의 우선순위 (높음/중간/낮음)
3. 예상 소요 시간
4. 작업 순서 제안

JSON 형식으로 반환해주세요."""

        return self._ok(recommendations=self._call_llm(prompt, max_tokens=2000))

    async def organize_schedule(self, events: List[str], constraints: str = None) -> Dict[str, Any]:
        """일정 조율 및 최적화"""
        events_str = "\n".join([f"- {e}" for e in events])
        constraints_str = f"\n제약사항: {constraints}" if constraints else ""

        prompt = f"""다음 일정들을 최적화해주세요:

{events_str}
{constraints_str}

다음을 제공해주세요:
1. 최적화된 일정 배치
2. 시간 블록 제안
3. 여유 시간 확보 방안
4. 주의사항 및 추천사항"""

        return self._ok(schedule=self._call_llm(prompt, max_tokens=2000))

    async def summarize_notes(self, notes: str) -> Dict[str, Any]:
        """메모 요약 및 구조화"""
        prompt = f"""다음 메모를 분석하고 구조화해주세요:

{notes}

다음을 제공해주세요:
1. 핵심 요약 (3-5개 bullet points)
2. 주제별 분류
3. 액션 아이템 추출
4. 중요한 날짜/데드라인 추출"""

        return self._ok(summary=self._call_llm(prompt, max_tokens=2000))
