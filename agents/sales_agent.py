"""
Business AI Team - Sales Agent
영업 전략, 파이프라인, 고객 관리
"""
from typing import Dict, Any
from agents.base_agent import BaseAgent


class SalesAgent(BaseAgent):
    """
    Sales Agent - "영업 전문가"

    영업 전략, 파이프라인 관리, 고객 관계를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["sales"])

        base_prompt = """당신은 영업 전문가입니다.
효과적인 영업 전략과 고객 관계 관리로 매출 성장을 지원합니다.

전문 분야:
- 💼 영업 전략 및 계획
- 📈 파이프라인 관리
- 🤝 고객 관계 관리 (CRM)
- 📊 영업 예측 및 분석
- 📝 제안서 및 견적 작성

원칙:
- 고객 가치 중심 접근
- 데이터 기반 영업
- 장기적 관계 구축
- 목표 달성 지향
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Sales Best Practices")

    async def develop_sales_strategy(self, target_market: str, goals: str, resources: str) -> Dict[str, Any]:
        """영업 전략 수립"""
        prompt = f"""다음 영업 전략을 수립해주세요:

타겟 시장: {target_market}
목표: {goals}
가용 리소스: {resources}

다음을 포함해주세요:
1. 시장 분석 및 기회
2. 타겟 고객 세그먼트
3. 가치 제안 (Value Proposition)
4. 영업 채널 전략
5. 가격 전략
6. 실행 계획 및 타임라인
7. KPI 및 성과 측정"""

        return self._ok(strategy=self._call_llm(prompt, max_tokens=3000))

    async def manage_pipeline(self, pipeline_data: str, focus: str = None) -> Dict[str, Any]:
        """파이프라인 관리 및 분석"""
        focus_str = f"\n초점: {focus}" if focus else ""

        prompt = f"""다음 영업 파이프라인을 분석하고 관리 방안을 제시해주세요:

파이프라인 데이터:
{pipeline_data[:3000]}
{focus_str}

다음을 제공해주세요:
1. 파이프라인 현황 요약
2. 단계별 분석 및 병목
3. 우선순위 기회
4. 리스크 요인
5. 액션 아이템
6. 예상 매출 및 달성률"""

        return self._ok(pipeline_analysis=self._call_llm(prompt, max_tokens=3000))

    async def create_sales_proposal(self, client_info: str, solution: str, pricing: str) -> Dict[str, Any]:
        """영업 제안서 작성"""
        prompt = f"""다음 영업 제안서를 작성해주세요:

고객 정보: {client_info}
제안 솔루션: {solution}
가격 정보: {pricing}

다음을 포함해주세요:
1. Executive Summary
2. 고객 니즈 및 과제
3. 제안 솔루션 상세
4. 기대 효과 및 ROI
5. 가격 및 조건
6. 구현 계획
7. 다음 단계"""

        return self._ok(proposal=self._call_llm(prompt, max_tokens=3000))
