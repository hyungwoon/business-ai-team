"""
Business AI Team - Research Agent
정보 조사, 분석, 인사이트 도출
"""
from typing import Dict, Any, List
from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """
    Research Agent - "리서치 전문가"

    정보 조사, 시장 분석, 경쟁사 리서치를 담당합니다.
    """

    def __init__(self):
        super().__init__(
            plugin_names=["marketing", "sales", "data"],
            skill_names=["competitive-analysis", "performance-analytics"],
        )

        base_prompt = """당신은 비즈니스 리서치 전문가입니다.
시장, 경쟁사, 트렌드를 분석하고 실행 가능한 인사이트를 제공합니다.

전문 분야:
- 🔍 시장 조사 및 트렌드 분석
- 🎯 경쟁사 분석 및 벤치마킹
- 📊 산업 리포트 요약 및 해석
- 💡 비즈니스 기회 발굴
- 📈 데이터 기반 인사이트 도출

원칙:
- 객관적이고 데이터 기반의 분석
- 실행 가능한 인사이트 제공
- 명확한 근거와 함께 결론 제시
- 다양한 관점 고려
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Research Best Practices")

    async def research_topic(self, topic: str, focus_areas: List[str] = None) -> Dict[str, Any]:
        """주제에 대한 포괄적 리서치"""
        focus_str = f"\n집중 영역: {', '.join(focus_areas)}" if focus_areas else ""

        prompt = f"""다음 주제에 대해 포괄적으로 조사해주세요:

주제: {topic}
{focus_str}

다음을 포함해주세요:
1. 핵심 개요 및 현황
2. 주요 트렌드 및 인사이트
3. 시장 기회 및 위험 요소
4. 실행 가능한 제안사항
5. 참고할만한 사례나 데이터"""

        return self._ok(research=self._call_llm(prompt, max_tokens=3000))

    async def analyze_competitors(self, competitors: List[str], focus: str = None) -> Dict[str, Any]:
        """경쟁사 분석"""
        competitors_str = "\n".join([f"- {c}" for c in competitors])
        focus_str = f"\n분석 초점: {focus}" if focus else ""

        prompt = f"""다음 경쟁사들을 분석해주세요:

{competitors_str}
{focus_str}

다음을 제공해주세요:
1. 각 경쟁사의 강점과 약점
2. 비교 분석 (제품, 가격, 마케팅 전략 등)
3. 시장 포지셔닝
4. 우리의 차별화 기회
5. 벤치마킹 포인트"""

        return self._ok(analysis=self._call_llm(prompt, max_tokens=3000))

    async def summarize_findings(self, documents: str) -> Dict[str, Any]:
        """조사 자료 요약 및 인사이트 도출"""
        prompt = f"""다음 조사 자료를 분석하고 핵심 인사이트를 도출해주세요:

{documents[:3000]}

다음을 제공해주세요:
1. 핵심 요약 (5-7개 bullet points)
2. 주요 인사이트 및 시사점
3. 실행 가능한 제안사항
4. 추가 조사가 필요한 영역"""

        return self._ok(summary=self._call_llm(prompt, max_tokens=2000))
