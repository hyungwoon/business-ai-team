"""
Business AI Team - Design Agent
UX/UI 리뷰, 브랜드 가이드라인, 디자인 시스템
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class DesignAgent(BaseAgent):
    """
    Design Agent - "디자인 전문가"

    UX/UI 리뷰, 브랜드 가이드라인, 디자인 시스템 감사를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["design", "marketing"])

        base_prompt = """당신은 디자인 전문가입니다.
사용자 경험과 브랜드 일관성을 담당합니다.

전문 분야:
- 🎨 UX/UI 디자인 리뷰
- 🖼️ 브랜드 아이덴티티 및 가이드라인
- 📐 디자인 시스템 구축
- 👁️ 사용성 평가 및 개선
- 🎯 사용자 중심 디자인

원칙:
- 사용자 중심 접근
- 일관된 브랜드 경험
- 접근성과 포용성
- 데이터 기반 디자인 결정
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Design Best Practices")

    async def review_ux_ui(self, product_description: str, issues: List[str] = None) -> Dict[str, Any]:
        """UX/UI 리뷰 및 개선 제안"""
        issues_str = ""
        if issues:
            issues_str = "\n보고된 이슈:\n" + "\n".join([f"- {i}" for i in issues])

        prompt = f"""다음 제품의 UX/UI를 리뷰해주세요:

제품 설명: {product_description}
{issues_str}

다음을 제공해주세요:
1. 현재 UX/UI 평가
2. 사용성 문제점 분석
3. 개선 권장사항 (우선순위별)
4. 사용자 흐름 최적화 방안
5. 접근성 고려사항
6. 구현 가이드라인"""

        return self._ok(review=self._call_llm(prompt, max_tokens=3000))

    async def create_brand_guidelines(self, brand_info: str, target_audience: str) -> Dict[str, Any]:
        """브랜드 가이드라인 작성"""
        prompt = f"""다음 브랜드의 가이드라인을 작성해주세요:

브랜드 정보: {brand_info}
타겟 고객: {target_audience}

다음을 포함해주세요:
1. 브랜드 미션 및 비전
2. 브랜드 가치 및 성격
3. 시각적 아이덴티티 (로고, 색상, 타이포그래피)
4. 톤 앤 보이스 가이드
5. 적용 예시 및 사용 규칙
6. Do's and Don'ts"""

        return self._ok(guidelines=self._call_llm(prompt, max_tokens=3000))

    async def design_system_audit(self, current_system: str, goals: List[str] = None) -> Dict[str, Any]:
        """디자인 시스템 감사"""
        goals_str = ""
        if goals:
            goals_str = "\n목표:\n" + "\n".join([f"- {g}" for g in goals])

        prompt = f"""다음 디자인 시스템을 감사해주세요:

현재 시스템: {current_system}
{goals_str}

다음을 제공해주세요:
1. 현재 시스템 분석
2. 일관성 평가
3. 컴포넌트 체계 검토
4. 갭 분석 및 누락 요소
5. 개선 권장사항
6. 구현 로드맵"""

        return self._ok(audit=self._call_llm(prompt, max_tokens=3000))
