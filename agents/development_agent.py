"""
Business AI Team - Development Agent
기술 아키텍처, 설계 검토, 개발 프로세스
"""
from typing import Dict, Any
from agents.base_agent import BaseAgent


class DevelopmentAgent(BaseAgent):
    """
    Development Agent - "개발 전문가"

    기술 아키텍처 설계, 설계 검토, 개발 프로세스 계획을 담당합니다.
    """

    def __init__(self):
        super().__init__(plugin_names=["development", "data"])

        base_prompt = """당신은 개발 리더(CTO/Tech Lead)입니다.
기술 전략, 아키텍처, 개발 프로세스를 담당합니다.

전문 분야:
- 🏗️ 기술 아키텍처 설계
- 📋 개발 프로세스 및 방법론
- 🔧 기술 스택 선택
- 🚀 DevOps 및 배포 전략
- 👥 개발 팀 관리 및 성장

원칙:
- 확장성과 유지보수성 우선
- 기술 부채 관리
- 지속적 개선 및 학습
- 협업과 커뮤니케이션
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Development Best Practices")

    async def design_architecture(self, product_requirements: str, constraints: str = None) -> Dict[str, Any]:
        """기술 아키텍처 설계"""
        constraints_str = f"\n제약사항: {constraints}" if constraints else ""

        prompt = f"""다음 요구사항을 기반으로 기술 아키텍처를 설계해주세요:

요구사항: {product_requirements}
{constraints_str}

다음을 제공해주세요:
1. 시스템 아키텍처 개요
2. 기술 스택 추천 및 근거
3. 주요 컴포넌트 및 역할
4. 확장성 및 성능 전략
5. 보안 및 안정성 고려사항
6. 개발 타임라인 및 리소스
7. 리스크 및 대응 방안"""

        return self._ok(architecture=self._call_llm(prompt, max_tokens=3000))

    async def review_technical_design(self, design_document: str, focus: str = None) -> Dict[str, Any]:
        """기술 설계 검토"""
        focus_str = f"\n초점: {focus}" if focus else ""

        prompt = f"""다음 기술 설계를 검토해주세요:

{design_document[:5000]}
{focus_str}

다음을 제공해주세요:
1. 설계의 강점
2. 개선이 필요한 영역
3. 확장성 및 성능 평가
4. 보안 및 안정성 검토
5. 기술 부채 분석
6. 구현 권장사항"""

        return self._ok(review=self._call_llm(prompt, max_tokens=3000))

    async def plan_development_process(self, team_size: int, project_scope: str, timeline: str) -> Dict[str, Any]:
        """개발 프로세스 계획"""
        prompt = f"""다음을 기반으로 개발 프로세스를 계획해주세요:

팀 규모: {team_size}명
프로젝트 범위: {project_scope}
일정: {timeline}

다음을 포함해주세요:
1. 개발 방법론 추천 (Agile/Scrum 등)
2. 스프린트 및 릴리스 계획
3. 코드 리뷰 및 QA 프로세스
4. CI/CD 파이프라인
5. 팀 구조 및 역할
6. 커뮤니케이션 및 협업 도구
7. 리스크 및 완화 전략"""

        return self._ok(process_plan=self._call_llm(prompt, max_tokens=3000))
