"""
Business AI Team - Business Development Agent
사업 기회, 파트너십 전략, 성장 계획
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class BusinessDevAgent(BaseAgent):
    """
    Business Development Agent - "사업개발 전문가"

    사업 기회 발굴, 파트너십 전략, 성장 계획을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["marketing", "sales"])

        base_prompt = """당신은 사업개발 전문가입니다.
조직의 성장 전략과 전략적 파트너십을 지원합니다.

전문 분야:
- 🎯 사업 기회 발굴 및 평가
- 🤝 전략적 파트너십 기획
- 📋 사업 계획 개발
- 🔍 시장 진입 전략
- 💼 M&A 및 비즈니스 협력

원칙:
- 전략적 시각
- 데이터 기반 기회 평가
- 실행 가능한 계획
- 장기 성장 지향
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Business Development Best Practices")

    async def identify_opportunities(self, market: str, focus_areas: List[str] = None) -> Dict[str, Any]:
        """사업 기회 발굴"""
        focus_str = f"\n초점 영역: {', '.join(focus_areas)}" if focus_areas else ""

        prompt = f"""다음 시장에서 사업 기회를 발굴해주세요:

시장: {market}
{focus_str}

다음을 제공해주세요:
1. 식별된 기회 목록 (5-10개)
2. 각 기회의 매력도 및 실행 가능성
3. 필요한 역량 및 리소스
4. 진입 시기 및 전략
5. 예상 ROI 및 리스크"""

        return self._ok(opportunities=self._call_llm(prompt, max_tokens=3000))

    async def develop_partnership_strategy(self, partner_type: str, objectives: List[str]) -> Dict[str, Any]:
        """파트너십 전략 개발"""
        obj_str = "\n".join([f"- {o}" for o in objectives])

        prompt = f"""다음 유형의 파트너와의 전략적 파트너십을 개발해주세요:

파트너 유형: {partner_type}
목표:
{obj_str}

다음을 제공해주세요:
1. 파트너십 목표 및 가치 제안
2. 잠재 파트너 프로필
3. 협력 구조 및 모델
4. 상호 이익 분석
5. 협상 전략 및 계약 핵심
6. 성공 지표 및 모니터링"""

        return self._ok(partnership_strategy=self._call_llm(prompt, max_tokens=3000))

    async def create_growth_plan(self, current_state: str, target_goals: str, timeframe: str) -> Dict[str, Any]:
        """성장 계획 수립"""
        prompt = f"""다음을 기반으로 성장 계획을 수립해주세요:

현재 상태: {current_state}
목표: {target_goals}
기간: {timeframe}

다음을 포함해주세요:
1. 성장 전략 (제품/시장 확대)
2. 주요 마일스톤 및 타임라인
3. 필요한 리소스 및 투자
4. 성공 지표 (KPI)
5. 위험 및 대응 계획
6. 조직 역량 개발 계획"""

        return self._ok(growth_plan=self._call_llm(prompt, max_tokens=3000))
