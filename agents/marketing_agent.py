"""
Business AI Team - Marketing Agent
마케팅 콘텐츠, 캠페인, 브랜드 전략
"""
from typing import Dict, Any
from agents.base_agent import BaseAgent


class MarketingAgent(BaseAgent):
    """
    Marketing Agent - "마케팅 전문가"

    마케팅 콘텐츠 제작, 캠페인 기획, 브랜드 전략을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["marketing"])

        base_prompt = """당신은 마케팅 전문가입니다.
효과적인 마케팅 전략과 콘텐츠를 통해 비즈니스 성장을 지원합니다.

전문 분야:
- 📢 마케팅 콘텐츠 제작
- 🎯 캠페인 기획 및 실행
- 🏷️ 브랜드 전략 및 포지셔닝
- 📊 마케팅 성과 분석
- 📱 디지털 마케팅 및 SNS

원칙:
- 타겟 고객 중심 접근
- 데이터 기반 의사결정
- 일관된 브랜드 메시지
- ROI 중심 전략
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Marketing Best Practices")

    async def create_marketing_content(self, content_type: str, topic: str, target_audience: str) -> Dict[str, Any]:
        """마케팅 콘텐츠 제작"""
        prompt = f"""다음 마케팅 콘텐츠를 제작해주세요:

콘텐츠 유형: {content_type}
주제: {topic}
타겟 고객: {target_audience}

다음을 제공해주세요:
1. 콘텐츠 제목/헤드라인 (3가지 옵션)
2. 본문 콘텐츠
3. CTA (Call to Action)
4. 해시태그/키워드
5. 배포 채널 추천"""

        return self._ok(content=self._call_llm(prompt, max_tokens=3000))

    async def plan_campaign(self, campaign_goal: str, budget: str, duration: str) -> Dict[str, Any]:
        """캠페인 기획"""
        prompt = f"""다음 마케팅 캠페인을 기획해주세요:

캠페인 목표: {campaign_goal}
예산: {budget}
기간: {duration}

다음을 포함해주세요:
1. 캠페인 컨셉 및 핵심 메시지
2. 타겟 고객 정의
3. 채널 전략 (온라인/오프라인)
4. 콘텐츠 계획
5. 예산 배분
6. KPI 및 성과 측정 방법
7. 타임라인"""

        return self._ok(campaign_plan=self._call_llm(prompt, max_tokens=3000))

    async def analyze_marketing_performance(self, metrics_data: str, period: str) -> Dict[str, Any]:
        """마케팅 성과 분석"""
        prompt = f"""다음 마케팅 성과를 분석해주세요:

성과 데이터:
{metrics_data[:3000]}

기간: {period}

다음을 제공해주세요:
1. 주요 지표 요약
2. 채널별 성과 분석
3. 트렌드 및 인사이트
4. 개선 기회
5. 다음 기간 권장사항"""

        return self._ok(analysis=self._call_llm(prompt, max_tokens=3000))
