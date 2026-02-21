"""
Business AI Team - Data Agent
데이터 분석, 시각화, 인사이트 도출
"""
from typing import Dict, Any
from agents.base_agent import BaseAgent


class DataAgent(BaseAgent):
    """
    Data Agent - "데이터 전문가"

    데이터 분석, 시각화, 인사이트 도출을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["data"])

        base_prompt = """당신은 데이터 분석 전문가입니다.
데이터를 통해 비즈니스 인사이트를 도출하고 의사결정을 지원합니다.

전문 분야:
- 📊 데이터 분석 및 통계
- 📈 데이터 시각화
- 🔍 트렌드 분석 및 예측
- 💡 비즈니스 인사이트 도출
- 🗄️ 데이터 품질 관리

원칙:
- 데이터 기반 의사결정
- 명확한 시각화
- 실행 가능한 인사이트
- 통계적 엄밀성
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Data Analysis Best Practices")

    async def analyze_data(self, data_description: str, analysis_goal: str) -> Dict[str, Any]:
        """데이터 분석"""
        prompt = f"""다음 데이터를 분석해주세요:

데이터 설명:
{data_description[:3000]}

분석 목표: {analysis_goal}

다음을 제공해주세요:
1. 데이터 개요 및 품질 평가
2. 주요 발견 사항
3. 통계적 분석 결과
4. 트렌드 및 패턴
5. 비즈니스 인사이트
6. 추가 분석 권장사항"""

        return self._ok(analysis=self._call_llm(prompt, max_tokens=3000))

    async def create_visualization_plan(self, data_type: str, audience: str, purpose: str) -> Dict[str, Any]:
        """시각화 계획 수립"""
        prompt = f"""다음 데이터의 시각화 계획을 수립해주세요:

데이터 유형: {data_type}
대상 청중: {audience}
목적: {purpose}

다음을 제공해주세요:
1. 권장 차트/그래프 유형
2. 시각화 레이아웃
3. 핵심 지표 및 KPI
4. 색상 및 디자인 가이드
5. 인터랙티브 요소 권장
6. 스토리텔링 구조"""

        return self._ok(visualization_plan=self._call_llm(prompt, max_tokens=3000))

    async def generate_insights(self, business_context: str, data_findings: str) -> Dict[str, Any]:
        """비즈니스 인사이트 도출"""
        prompt = f"""다음 데이터 발견에서 비즈니스 인사이트를 도출해주세요:

비즈니스 컨텍스트: {business_context}

데이터 발견:
{data_findings[:3000]}

다음을 제공해주세요:
1. 핵심 인사이트 (3-5개)
2. 각 인사이트의 비즈니스 영향
3. 권장 액션
4. 추가 조사가 필요한 영역
5. 의사결정 지원 요약"""

        return self._ok(insights=self._call_llm(prompt, max_tokens=3000))
