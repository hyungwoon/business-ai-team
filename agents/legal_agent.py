"""
Business AI Team - Legal Agent
법률 자문, 계약 검토, 규정 준수 평가
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class LegalAgent(BaseAgent):
    """
    Legal Agent - "법률 전문가"

    계약 검토, 법률 자문, 규정 준수 평가를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["legal", "enterprise-search"])

        base_prompt = """당신은 법률 전문가입니다.
기업의 법적 위험을 최소화하고 규정 준수를 지원합니다.

전문 분야:
- ⚖️ 계약서 검토 및 분석
- 📋 법률 자문 및 위험 평가
- 📜 규정 및 컴플라이언스 지원
- 🔍 법적 쟁점 분석
- 📑 법률 문서 작성 및 검토

원칙:
- 법적 정확성 우선
- 리스크 중심 분석
- 실행 가능한 권장사항
- 명확한 법적 근거 제시

주의사항:
- 이 조언은 일반적인 가이드라인이며, 구체적인 법률 문제는 변호사와 상담하세요.
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Legal Best Practices")

    async def review_contract(self, contract_text: str, focus: str = None) -> Dict[str, Any]:
        """계약서 검토 및 분석"""
        focus_str = f"\n분석 초점: {focus}" if focus else ""

        prompt = f"""다음 계약서를 검토하고 분석해주세요:

{contract_text[:5000]}
{focus_str}

다음을 제공해주세요:
1. 주요 조항 요약
2. 법적 위험 요소 (높음/중간/낮음)
3. 보호 조항 분석
4. 개선 권장사항
5. 주의할 점"""

        return self._ok(review=self._call_llm(prompt, max_tokens=3000))

    async def provide_legal_advice(self, situation: str, questions: List[str] = None) -> Dict[str, Any]:
        """법률 자문 제공"""
        questions_str = ""
        if questions:
            questions_str = "\n질문 목록:\n" + "\n".join([f"- {q}" for q in questions])

        prompt = f"""다음 상황에 대해 법률 자문을 제공해주세요:

상황: {situation}
{questions_str}

다음을 포함해주세요:
1. 법적 현황 분석
2. 가능한 옵션 및 각각의 법적 함의
3. 권장 조치
4. 예상되는 법적 결과
5. 추가 검토가 필요한 사항"""

        return self._ok(advice=self._call_llm(prompt, max_tokens=3000))

    async def assess_compliance(self, business_practice: str, regulations: List[str] = None) -> Dict[str, Any]:
        """규정 준수 평가"""
        regulations_str = ""
        if regulations:
            regulations_str = "\n관련 규정: " + ", ".join(regulations)

        prompt = f"""다음 비즈니스 실행에 대한 규정 준수를 평가해주세요:

실행: {business_practice}
{regulations_str}

다음을 제공해주세요:
1. 규정 준수 현황
2. 위험 요소 및 갭 분석
3. 준수 개선 방안
4. 예상 리스크
5. 타임라인 및 우선순위"""

        return self._ok(assessment=self._call_llm(prompt, max_tokens=3000))
