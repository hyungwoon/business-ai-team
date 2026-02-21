"""
Business AI Team - Main Agent
범용 비즈니스 어시스턴트 메인 에이전트
"""
from anthropic import Anthropic
from typing import List, Dict, Any, Optional, Callable
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from core.config import get_settings

MAX_HISTORY_MESSAGES = 20  # 최근 N개 메시지만 유지 (히스토리 트리밍)


class MainAgent:
    """
    Main Agent - "팀 리더"

    사용자의 비즈니스 요청을 분석하고 적절한 전문가 팀원에게 작업을 할당합니다.
    """

    def __init__(self):
        self.settings = get_settings()
        self.client = Anthropic(api_key=self.settings.anthropic_api_key)

        # Tool registry
        self.tools: Dict[str, Dict[str, Any]] = {}

        # Tool 정의 캐시 (루프 진입 전 1회만 생성)
        self._tools_cache: Optional[List[Dict]] = None

        self.system_prompt = """당신은 사업가의 개인 비서이자 전문가 팀의 리더입니다.
당신은 다양한 전문가 팀원들을 관리하며, 사용자의 비즈니스 니즈를 충족시킵니다.

**핵심 운영 팀 (Core Operations):**
- 📋 **Productivity**: 작업 관리, 일정 조율, 메모 정리
- 🔍 **Research**: 시장 조사, 경쟁사 분석, 트렌드 리서치
- ✍️ **Writing**: 이메일, 문서 작성, 요약, 번역

**확장 운영 팀 (Extended Operations):**
- 📊 **Data**: 데이터 분석, 시각화, 인사이트 도출
- 📢 **Marketing**: 마케팅 콘텐츠, 캠페인 기획, 성과 분석
- 💼 **Sales**: 영업 전략, 파이프라인 관리, 제안서 작성

**전략 자문 팀 (Strategic Advisory):**
- ⚖️ **Legal & Compliance**: 계약 검토, 법률 자문, 컴플라이언스
- 💰 **Finance, BizDev, Product**: 재무/사업개발/제품 전략
- 🏗️ **Tech & Design**: 기술 아키텍처, UX/UI, 브랜드
- 👥 **HR, PR, Security**: 조직 관리, 홍보, 보안 정책

**작업 방식:**
1. 사용자 요청 분석 → 적절한 팀 선택
2. 단순 작업은 1개 팀, 복잡한 작업은 여러 팀 조합
3. 결과를 통합하여 완성된 답변 제공

**원칙:**
- 비즈니스 목표 우선, 실용적 솔루션
- 명확하고 구체적인 결과물
- 한국어로 자연스럽게 소통

당신은 유능하고 신뢰할 수 있는 비즈니스 파트너입니다.
"""

    def register_tool(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        handler: Callable
    ):
        """팀원(SubAgent)를 Tool로 등록. 새 Tool 등록 시 캐시 초기화."""
        self.tools[name] = {
            "name": name,
            "description": description,
            "input_schema": {
                "type": "object",
                "properties": parameters,
                "required": list(parameters.keys())
            },
            "handler": handler
        }
        # 새 Tool이 등록되면 캐시 무효화
        self._tools_cache = None

    def _get_tools_for_claude(self) -> List[Dict]:
        """Tool 정의를 캐시하여 반복 재구성 방지."""
        if self._tools_cache is None:
            self._tools_cache = [
                {
                    "name": t["name"],
                    "description": t["description"],
                    "input_schema": t["input_schema"]
                }
                for t in self.tools.values()
            ]
        return self._tools_cache

    def _trim_history(self, messages: List[Dict]) -> List[Dict]:
        """
        슬라이딩 윈도우로 대화 히스토리 관리.
        첫 user 메시지(원래 요청)는 보존하고 최근 N개만 유지.
        """
        if len(messages) <= MAX_HISTORY_MESSAGES:
            return messages
        return [messages[0]] + messages[-(MAX_HISTORY_MESSAGES - 1):]

    async def process_request(
        self,
        user_message: str,
        context: Optional[Dict[str, Any]] = None,
        max_iterations: int = 5
    ) -> Dict[str, Any]:
        """사용자 요청 처리"""
        messages = [{"role": "user", "content": user_message}]

        if context:
            context_text = f"\n\n**추가 컨텍스트:**\n{json.dumps(context, ensure_ascii=False, indent=2)}"
            messages[0]["content"] += context_text

        iterations = 0
        tool_results = []

        # Tool 정의는 루프 바깥에서 1회만 구성 (Step 4)
        tools_for_claude = self._get_tools_for_claude()

        while iterations < max_iterations:
            iterations += 1

            # 히스토리 트리밍 (Step 3)
            messages = self._trim_history(messages)

            # Prompt Caching 적용: system을 캐시 블록으로 전송 (Step 1)
            response = self.client.messages.create(
                model=self.settings.model_name,
                max_tokens=4096,
                system=[
                    {
                        "type": "text",
                        "text": self.system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                tools=tools_for_claude,
                messages=messages
            )

            if response.stop_reason == "end_turn":
                final_text = ""
                for block in response.content:
                    if hasattr(block, "text"):
                        final_text += block.text

                return {
                    "success": True,
                    "answer": final_text,
                    "tool_calls": tool_results,
                    "iterations": iterations
                }

            elif response.stop_reason == "tool_use":
                tool_uses = [block for block in response.content if block.type == "tool_use"]

                messages.append({
                    "role": "assistant",
                    "content": response.content
                })

                tool_results_content = []
                for tool_use in tool_uses:
                    tool_name = tool_use.name
                    tool_input = tool_use.input
                    tool_id = tool_use.id

                    if tool_name in self.tools:
                        handler = self.tools[tool_name]["handler"]

                        try:
                            result = await handler(**tool_input)
                            tool_results.append({
                                "tool": tool_name,
                                "input": tool_input,
                                "result": result,
                                "success": True
                            })
                            tool_results_content.append({
                                "type": "tool_result",
                                "tool_use_id": tool_id,
                                "content": json.dumps(result, ensure_ascii=False)
                            })
                        except Exception as e:
                            error_msg = f"Error: {str(e)}"
                            tool_results.append({
                                "tool": tool_name,
                                "input": tool_input,
                                "error": error_msg,
                                "success": False
                            })
                            tool_results_content.append({
                                "type": "tool_result",
                                "tool_use_id": tool_id,
                                "content": error_msg,
                                "is_error": True
                            })
                    else:
                        tool_results_content.append({
                            "type": "tool_result",
                            "tool_use_id": tool_id,
                            "content": f"Tool '{tool_name}' not found",
                            "is_error": True
                        })

                messages.append({
                    "role": "user",
                    "content": tool_results_content
                })

            else:
                return {
                    "success": False,
                    "error": f"Unexpected stop reason: {response.stop_reason}",
                    "tool_calls": tool_results
                }

        return {
            "success": False,
            "error": "Max iterations reached",
            "tool_calls": tool_results
        }

    def get_available_tools(self) -> List[Dict[str, Any]]:
        """등록된 모든 Tool 목록 반환"""
        return [
            {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": list(tool["input_schema"]["properties"].keys())
            }
            for tool in self.tools.values()
        ]
