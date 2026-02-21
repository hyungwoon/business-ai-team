"""
Business AI Team - Base Agent
모든 전문가 에이전트의 공통 기반 클래스
"""
import sys
from pathlib import Path
from typing import Optional

sys.path.append(str(Path(__file__).parent.parent))

from anthropic import Anthropic
from core.config import get_settings
from core.plugin_loader import get_plugin_loader


class BaseAgent:
    """
    모든 전문가 에이전트의 기반 클래스.

    - Prompt Caching 자동 적용 (시스템 프롬프트)
    - 플러그인 스킬 로드 공통화
    - LLM 호출 패턴 통일
    - 응답 포맷 표준화
    """

    _shared_client: Optional[Anthropic] = None  # 모든 에이전트가 공유하는 클라이언트

    def __init__(
        self,
        plugin_names: Optional[list] = None,
        skill_names: Optional[list] = None,
        use_light_model: bool = False,
    ):
        self.settings = get_settings()
        if BaseAgent._shared_client is None:
            BaseAgent._shared_client = Anthropic(api_key=self.settings.anthropic_api_key)
        self.client = BaseAgent._shared_client
        self.use_light_model = use_light_model
        self._skills = self._load_skills(plugin_names, skill_names)

    # ------------------------------------------------------------------
    # 내부 헬퍼 메서드
    # ------------------------------------------------------------------

    def _load_skills(self, plugin_names: Optional[list], skill_names: Optional[list]) -> str:
        if not plugin_names:
            return ""
        try:
            loader = get_plugin_loader()
            return loader.load_all_skills_for_agent(plugin_names, skill_names)
        except Exception:
            return ""

    def _build_system_prompt(self, base_prompt: str, section_name: str = "Best Practices") -> str:
        """베이스 프롬프트에 플러그인 스킬을 추가."""
        if self._skills:
            return base_prompt + f"\n\n# {section_name}\n\n" + self._skills
        return base_prompt

    def _get_model(self) -> str:
        if self.use_light_model:
            return self.settings.model_name_light
        return self.settings.model_name

    def _call_llm(self, prompt: str, max_tokens: int = 2000) -> str:
        """
        LLM 호출 (Prompt Caching 적용).

        시스템 프롬프트를 ephemeral 캐시 블록으로 전송하여
        반복 호출 시 입력 토큰 60~90% 절감.
        """
        response = self.client.messages.create(
            model=self._get_model(),
            max_tokens=max_tokens,
            system=[
                {
                    "type": "text",
                    "text": self.system_prompt,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    def _ok(self, **data) -> dict:
        """성공 응답 표준 포맷."""
        return {"success": True, "agent": self.__class__.__name__, **data}

    def _err(self, msg: str) -> dict:
        """오류 응답 표준 포맷."""
        return {"success": False, "error": msg, "agent": self.__class__.__name__}
