"""
Business AI Team - Writing Agent
이메일, 문서, 요약, 번역 등 글쓰기 지원
"""
from typing import Dict, Any
from agents.base_agent import BaseAgent


class WritingAgent(BaseAgent):
    """
    Writing Agent - "작문 전문가"

    이메일, 문서, 요약, 번역 등 모든 비즈니스 글쓰기를 담당합니다.
    """

    def __init__(self):
        super().__init__(
            plugin_names=["marketing", "sales"],
            skill_names=["content-creation"],
            use_light_model=True,
        )

        base_prompt = """당신은 비즈니스 작문 전문가입니다.
명확하고 효과적인 비즈니스 커뮤니케이션을 작성합니다.

전문 분야:
- ✉️ 이메일 작성 (공식/비공식, 내부/외부)
- 📄 문서 작성 (보고서, 제안서, 기획서)
- 📝 요약 및 편집
- 🌐 번역 (한국어 ↔ 영어)
- 💬 메시지 및 커뮤니케이션 작성

원칙:
- 목적과 독자를 고려한 톤 선택
- 명확하고 간결한 표현
- 구조화되고 논리적인 전개
- 적절한 형식과 에티켓 준수
"""
        self.system_prompt = self._build_system_prompt(base_prompt, "Professional Writing Guidelines")

    async def write_email(self, purpose: str, recipient: str, key_points: str, tone: str = "professional") -> Dict[str, Any]:
        """이메일 작성"""
        prompt = f"""다음 이메일을 작성해주세요:

목적: {purpose}
수신자: {recipient}
전달할 내용: {key_points}
톤: {tone}

다음 형식으로 작성해주세요:
- 제목 (Subject)
- 본문 (Body)
- 서명 부분 제안

이메일은 {tone} 톤으로, 명확하고 전문적으로 작성해주세요."""

        return self._ok(email=self._call_llm(prompt, max_tokens=2000))

    async def write_document(self, doc_type: str, topic: str, details: str, length: str = "medium") -> Dict[str, Any]:
        """문서 작성 (보고서, 제안서, 기획서 등)"""
        prompt = f"""다음 {doc_type}을(를) 작성해주세요:

주제: {topic}
상세 내용: {details}
분량: {length}

다음을 포함해주세요:
1. 제목 및 개요
2. 구조화된 본문 (적절한 섹션 구분)
3. 핵심 포인트 강조
4. 결론 및 넥스트 스텝 (필요시)

전문적이고 설득력 있게 작성해주세요."""

        return self._ok(document=self._call_llm(prompt, max_tokens=3000))

    async def summarize_text(self, text: str, target_length: str = "short") -> Dict[str, Any]:
        """텍스트 요약"""
        prompt = f"""다음 텍스트를 {target_length} 길이로 요약해주세요:

{text[:5000]}

다음을 포함해주세요:
1. 핵심 요약 (3-5 bullet points)
2. 주요 내용 (필요시)
3. 액션 아이템 (있는 경우)"""

        return self._ok(summary=self._call_llm(prompt, max_tokens=1500))

    async def translate(self, text: str, source_lang: str, target_lang: str) -> Dict[str, Any]:
        """번역"""
        prompt = f"""다음 텍스트를 {source_lang}에서 {target_lang}(으)로 번역해주세요:

{text}

비즈니스 컨텍스트에 적합하게, 자연스럽고 정확하게 번역해주세요."""

        return self._ok(translation=self._call_llm(prompt, max_tokens=2000))

    async def edit_text(self, text: str, instructions: str) -> Dict[str, Any]:
        """텍스트 편집 및 개선"""
        prompt = f"""다음 텍스트를 편집해주세요:

원본 텍스트:
{text}

편집 지침:
{instructions}

개선된 버전과 함께 주요 변경사항을 설명해주세요."""

        return self._ok(edited=self._call_llm(prompt, max_tokens=2000))
