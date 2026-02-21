"""
Business AI Team - Compliance Agent
규정 준수, 모니터링, 리스크 관리
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class ComplianceAgent(BaseAgent):
    """
    Compliance Agent - "컴플라이언스 전문가"

    규정 준수 모니터링, 리포트 작성, 리스크 식별을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["compliance", "data"])

        base_prompt = """당신은 컴플라이언스 전문가입니다.
조직의 규정 준수 및 리스크 관리를 지원합니다.

전문 분야:
- 🏛️ 규정 준수 모니터링
- 📊 컴플라이언스 리포트 작성
- ⚠️ 리스크 식별 및 평가
- 🔐 데이터 보호 및 프라이버시
- 📋 감시 프로세스 설계

원칙:
- 선제적 리스크 관리
- 명확한 문서화
- 지속적인 모니터링
- 실행 가능한 개선 조치
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Compliance Best Practices")

    async def monitor_compliance(self, areas: List[str]) -> Dict[str, Any]:
        """컴플라이언스 모니터링"""
        areas_str = "\n".join([f"- {a}" for a in areas])

        prompt = f"""다음 영역의 컴플라이언스를 모니터링해주세요:

{areas_str}

다음을 제공해주세요:
1. 각 영역의 현재 준수 상태 체크리스트
2. 발견된 갭 및 위험
3. 개선 권장사항
4. 우선순위 액션 플랜
5. 모니터링 체크리스트"""

        return self._ok(monitoring=self._call_llm(prompt, max_tokens=3000))

    async def create_compliance_report(self, period: str, focus_areas: List[str]) -> Dict[str, Any]:
        """컴플라이언스 리포트 작성"""
        areas_str = "\n".join([f"- {a}" for a in focus_areas])

        prompt = f"""다음 기간의 컴플라이언스 리포트를 작성해주세요:

기간: {period}
초점 영역:
{areas_str}

다음을 포함해주세요:
1. Executive Summary
2. 각 영역별 준수 상태
3. 주요 발견 및 이슈
4. 리스크 평가 매트릭스
5. 개선 조치 및 타임라인
6. 다음 기간 계획"""

        return self._ok(report=self._call_llm(prompt, max_tokens=3000))

    async def identify_risks(self, business_process: str) -> Dict[str, Any]:
        """리스크 식별 및 평가"""
        prompt = f"""다음 비즈니스 프로세스의 리스크를 식별하고 평가해주세요:

프로세스: {business_process}

다음을 제공해주세요:
1. 식별된 리스크 목록 (높음/중간/낮음)
2. 각 리스크의 영향 및 발생 확률
3. 현재 완화 조치
4. 추가 완화 전략
5. 모니터링 계획"""

        return self._ok(risk_assessment=self._call_llm(prompt, max_tokens=3000))
