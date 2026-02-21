"""
Business AI Team - Product Agent
제품 전략, 로드맵, 기능 스펙 정의
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class ProductAgent(BaseAgent):
    """
    Product Agent - "프로덕트 전문가"

    제품 기회 분석, 로드맵 작성, 기능 스펙 정의를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["product", "marketing"])

        base_prompt = """당신은 제품 전문가입니다.
제품의 개발, 관리, 성장을 지원합니다.

전문 분야:
- 📱 제품 전략 및 정의
- 🗺️ 로드맵 계획 및 관리
- 👥 고객 요구사항 분석
- 🔧 기능 스펙 정의
- 📊 제품 성과 분석

원칙:
- 고객 중심 사고
- 데이터 기반 의사결정
- 반복적 개발 및 학습
- 명확한 우선순위
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Product Best Practices")

    async def analyze_product_opportunity(self, market: str, customer_problem: str) -> Dict[str, Any]:
        """제품 기회 분석"""
        prompt = f"""다음 제품 기회를 분석해주세요:

시장: {market}
고객 문제: {customer_problem}

다음을 제공해주세요:
1. 시장 기회 규모 및 성장성
2. 경쟁 구도 분석
3. 고객 세그먼트 및 니즈
4. 제품 가치 제안
5. 진입 전략 및 차별화
6. 예상 성과 지표"""

        return self._ok(analysis=self._call_llm(prompt, max_tokens=3000))

    async def create_product_roadmap(self, product_vision: str, phases: List[str]) -> Dict[str, Any]:
        """제품 로드맵 작성"""
        phases_str = "\n".join([f"- {p}" for p in phases])

        prompt = f"""다음을 기반으로 제품 로드맵을 작성해주세요:

비전: {product_vision}

단계:
{phases_str}

다음을 포함해주세요:
1. 각 단계별 목표 및 핵심 기능
2. 우선순위 및 의존성
3. 타임라인 및 마일스톤
4. 리소스 계획
5. 성공 지표 및 검증 방법
6. 위험 및 대응 전략"""

        return self._ok(roadmap=self._call_llm(prompt, max_tokens=3000))

    async def define_feature_specs(self, feature_description: str, requirements: str) -> Dict[str, Any]:
        """기능 스펙 정의"""
        prompt = f"""다음 기능에 대한 상세 스펙을 정의해주세요:

기능: {feature_description}
요구사항: {requirements}

다음을 포함해주세요:
1. 기능 개요 및 가치
2. 사용자 스토리 및 유즈케이스
3. 상세 요구사항 (기능/비기능)
4. UI/UX 고려사항
5. 기술적 고려사항
6. 테스트 전략
7. 성공 기준"""

        return self._ok(specs=self._call_llm(prompt, max_tokens=3000))
