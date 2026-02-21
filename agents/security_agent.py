"""
Business AI Team - Security Agent
보안 평가, 정책 수립, 보안 감사
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class SecurityAgent(BaseAgent):
    """
    Security Agent - "보안 전문가"

    보안 태세 평가, 정책 수립, 보안 감사를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["security", "data"])

        base_prompt = """당신은 정보보안 전문가입니다.
조직의 사이버 보안과 데이터 보호를 담당합니다.

전문 분야:
- 🔒 사이버 보안 전략
- 🛡️ 위협 평가 및 취약점 분석
- 📋 보안 정책 및 절차 수립
- 🔍 보안 감사 및 컴플라이언스
- 🚨 사고 대응 및 복구

원칙:
- 심층 방어 (Defense in Depth)
- 최소 권한 원칙
- 보안과 사용성의 균형
- 지속적인 모니터링 및 개선
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Security Best Practices")

    async def assess_security_posture(self, system_description: str, current_measures: List[str] = None) -> Dict[str, Any]:
        """보안 태세 평가"""
        measures_str = ""
        if current_measures:
            measures_str = "\n현재 보안 조치:\n" + "\n".join([f"- {m}" for m in current_measures])

        prompt = f"""다음 시스템의 보안 태세를 평가해주세요:

시스템 설명: {system_description}
{measures_str}

다음을 제공해주세요:
1. 현재 보안 상태 평가
2. 주요 위협 및 취약점
3. 위험도 분석 (높음/중간/낮음)
4. 개선 권장사항 (우선순위별)
5. 단기/장기 액션 플랜
6. 필요한 리소스 및 투자"""

        return self._ok(assessment=self._call_llm(prompt, max_tokens=3000))

    async def create_security_policy(self, scope: str, requirements: List[str]) -> Dict[str, Any]:
        """보안 정책 수립"""
        req_str = "\n".join([f"- {r}" for r in requirements])

        prompt = f"""다음 범위의 보안 정책을 수립해주세요:

범위: {scope}

요구사항:
{req_str}

다음을 제공해주세요:
1. 정책 목적 및 범위
2. 역할 및 책임
3. 정책 세부 내용
4. 준수 요건
5. 위반 시 조치
6. 검토 및 업데이트 주기"""

        return self._ok(policy=self._call_llm(prompt, max_tokens=3000))

    async def conduct_security_audit(self, audit_scope: str, standards: List[str] = None) -> Dict[str, Any]:
        """보안 감사"""
        standards_str = ""
        if standards:
            standards_str = "\n적용 표준: " + ", ".join(standards)

        prompt = f"""다음 범위의 보안 감사를 수행해주세요:

감사 범위: {audit_scope}
{standards_str}

다음을 제공해주세요:
1. 감사 체크리스트
2. 발견 사항 (심각도별)
3. 컴플라이언스 갭 분석
4. 권장 조치 사항
5. 개선 우선순위
6. 후속 감사 계획"""

        return self._ok(audit_report=self._call_llm(prompt, max_tokens=3000))
