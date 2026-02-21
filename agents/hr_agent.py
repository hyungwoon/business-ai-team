"""
Business AI Team - HR Agent
채용 전략, 조직 문화, 성과 관리
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class HRAgent(BaseAgent):
    """
    HR Agent - "인사 전문가"

    채용 전략, 조직 문화 설계, 성과 관리 체계를 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["productivity"])

        base_prompt = """당신은 인사(HR) 전문가입니다.
조직의 인재 관리와 문화 발전을 지원합니다.

전문 분야:
- 👥 채용 전략 및 인재 확보
- 🏢 조직 문화 설계 및 발전
- 📊 성과 관리 및 평가 체계
- 🎓 인재 개발 및 교육
- 💼 보상 및 복리후생 전략

원칙:
- 사람 중심 접근
- 공정하고 투명한 프로세스
- 지속적인 성장 지원
- 다양성과 포용성
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "HR Best Practices")

    async def develop_hiring_strategy(self, positions: List[str], company_context: str) -> Dict[str, Any]:
        """채용 전략 수립"""
        positions_str = "\n".join([f"- {p}" for p in positions])

        prompt = f"""다음 포지션에 대한 채용 전략을 수립해주세요:

채용 포지션:
{positions_str}

회사 상황: {company_context}

다음을 제공해주세요:
1. 각 포지션별 이상적인 후보자 프로필
2. 채용 채널 및 소싱 전략
3. 선발 프로세스 설계
4. 면접 질문 및 평가 기준
5. 채용 브랜딩 전략
6. 온보딩 계획"""

        return self._ok(strategy=self._call_llm(prompt, max_tokens=3000))

    async def design_org_culture(self, current_culture: str, desired_values: List[str]) -> Dict[str, Any]:
        """조직 문화 설계"""
        values_str = "\n".join([f"- {v}" for v in desired_values])

        prompt = f"""조직 문화를 설계해주세요:

현재 문화: {current_culture}

원하는 가치:
{values_str}

다음을 제공해주세요:
1. 문화 비전 및 미션
2. 핵심 가치 정의 및 행동 지침
3. 문화 변화 로드맵
4. 리더십 역할
5. 문화 강화 프로그램
6. 측정 및 피드백 방법"""

        return self._ok(culture_plan=self._call_llm(prompt, max_tokens=3000))

    async def create_performance_framework(self, team_structure: str, goals: str) -> Dict[str, Any]:
        """성과 관리 체계 구축"""
        prompt = f"""성과 관리 체계를 구축해주세요:

팀 구조: {team_structure}
조직 목표: {goals}

다음을 제공해주세요:
1. 성과 관리 철학 및 원칙
2. 목표 설정 프레임워크 (OKR/KPI)
3. 평가 주기 및 프로세스
4. 피드백 시스템
5. 보상 연계 방안
6. 성장 및 개발 계획"""

        return self._ok(framework=self._call_llm(prompt, max_tokens=3000))
