"""
Business AI Team - Finance Agent
재무 분석, 예산 계획, 재무 예측
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class FinanceAgent(BaseAgent):
    """
    Finance Agent - "재무 전문가"

    재무 분석, 예산 계획, 재무 예측을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["finance", "data"])

        base_prompt = """당신은 재무 전문가입니다.
조직의 재무 건강과 성장을 지원합니다.

전문 분야:
- 💰 재무 분석 및 성과 평가
- 📊 예산 계획 및 관리
- 💹 재무 예측 및 모델링
- 💼 투자 분석 및 ROI 평가
- 📈 성장 전략과 재무 영향

원칙:
- 데이터 기반 분석
- 명확한 재무 지표
- 실행 가능한 권장사항
- 리스크와 기회의 균형
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Financial Best Practices")

    async def analyze_finances(self, financial_data: str, period: str = None) -> Dict[str, Any]:
        """재무 분석"""
        period_str = f"\n기간: {period}" if period else ""

        prompt = f"""다음 재무 데이터를 분석해주세요:

{financial_data[:5000]}
{period_str}

다음을 제공해주세요:
1. 주요 재무 지표 (수익성, 유동성, 안정성)
2. 추세 분석 및 YoY 비교
3. 강점과 약점
4. 개선 기회
5. 주의 영역"""

        return self._ok(analysis=self._call_llm(prompt, max_tokens=3000))

    async def create_budget(self, departments: List[str], total_budget: str, constraints: str = None) -> Dict[str, Any]:
        """예산 계획 및 할당"""
        depts_str = "\n".join([f"- {d}" for d in departments])
        constraints_str = f"\n제약사항: {constraints}" if constraints else ""

        prompt = f"""다음 부서에 대한 예산을 계획해주세요:

부서:
{depts_str}

총 예산: {total_budget}
{constraints_str}

다음을 제공해주세요:
1. 부서별 예산 할당
2. 할당 근거 및 우선순위
3. 예산 관리 지침
4. 모니터링 포인트
5. 리스크 및 완화 방안"""

        return self._ok(budget=self._call_llm(prompt, max_tokens=3000))

    async def forecast_financials(self, historical_data: str, growth_assumptions: str) -> Dict[str, Any]:
        """재무 예측"""
        prompt = f"""다음 데이터를 기반으로 재무를 예측해주세요:

과거 데이터:
{historical_data[:3000]}

성장 가정:
{growth_assumptions}

다음을 제공해주세요:
1. 향후 3년 재무 예측
2. 주요 가정 및 근거
3. 시나리오 분석 (낙관/보수적)
4. KPI 예상
5. 리스크 요소 및 대응책"""

        return self._ok(forecast=self._call_llm(prompt, max_tokens=3000))
