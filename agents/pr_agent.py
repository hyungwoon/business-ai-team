"""
Business AI Team - PR Agent
보도자료, 위기 관리, 미디어 전략
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class PRAgent(BaseAgent):
    """
    PR Agent - "홍보 전문가"

    보도자료 작성, 위기 관리, 미디어 전략을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["pr", "marketing"])

        base_prompt = """당신은 홍보(PR) 전문가입니다.
조직의 대외 커뮤니케이션과 평판 관리를 담당합니다.

전문 분야:
- 📰 보도자료 작성 및 배포
- 🚨 위기 관리 및 커뮤니케이션
- 📺 미디어 관계 및 전략
- 🎤 스포크스퍼슨 트레이닝
- 📱 소셜 미디어 PR

원칙:
- 진실성과 투명성
- 신속하고 일관된 메시지
- 이해관계자 중심 접근
- 선제적 커뮤니케이션
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "PR Best Practices")

    async def draft_press_release(self, news_topic: str, key_messages: List[str], company_info: str) -> Dict[str, Any]:
        """보도자료 작성"""
        messages_str = "\n".join([f"- {m}" for m in key_messages])

        prompt = f"""다음 주제로 보도자료를 작성해주세요:

주제: {news_topic}

핵심 메시지:
{messages_str}

회사 정보: {company_info}

다음을 제공해주세요:
1. 헤드라인 (3가지 옵션)
2. 서브헤드라인
3. 본문 (역피라미드 구조)
4. 인용문
5. 회사 소개 (boilerplate)
6. 미디어 연락처"""

        return self._ok(press_release=self._call_llm(prompt, max_tokens=3000))

    async def create_crisis_plan(self, crisis_scenario: str, stakeholders: List[str]) -> Dict[str, Any]:
        """위기 관리 계획"""
        stakeholders_str = "\n".join([f"- {s}" for s in stakeholders])

        prompt = f"""다음 위기 상황에 대한 대응 계획을 작성해주세요:

위기 시나리오: {crisis_scenario}

이해관계자:
{stakeholders_str}

다음을 제공해주세요:
1. 위기 단계별 대응 전략
2. 핵심 메시지 (이해관계자별)
3. 커뮤니케이션 채널 및 타이밍
4. Q&A 준비
5. 모니터링 및 대응 팀 구성
6. 사후 복구 계획"""

        return self._ok(crisis_plan=self._call_llm(prompt, max_tokens=3000))

    async def develop_media_strategy(self, objectives: List[str], target_media: List[str], budget: str = None) -> Dict[str, Any]:
        """미디어 전략 개발"""
        obj_str = "\n".join([f"- {o}" for o in objectives])
        media_str = "\n".join([f"- {m}" for m in target_media])
        budget_str = f"\n예산: {budget}" if budget else ""

        prompt = f"""미디어 전략을 개발해주세요:

목표:
{obj_str}

타겟 미디어:
{media_str}
{budget_str}

다음을 제공해주세요:
1. 미디어 전략 개요
2. 타겟 미디어 분석 및 접근 방법
3. 콘텐츠 캘린더
4. 기자/인플루언서 관계 구축 계획
5. 성과 측정 지표
6. 실행 타임라인"""

        return self._ok(media_strategy=self._call_llm(prompt, max_tokens=3000))
