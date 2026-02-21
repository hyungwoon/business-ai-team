#!/usr/bin/env python3
"""
Business AI Team - CLI Interface
간단한 명령줄 인터페이스로 AI 팀과 대화합니다.
"""
import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from agents.team_orchestrator import get_team_orchestrator
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


console = Console()


def print_welcome():
    """환영 메시지 출력"""
    welcome = """
# 🤖 Business AI Team

당신의 비즈니스를 돕는 AI 전문가 팀입니다.

**팀원 소개:**
- 📋 **생산성 전문가** - 작업 관리, 일정 조율, 메모 정리
- 🔍 **리서치 전문가** - 시장 조사, 경쟁사 분석, 트렌드 파악
- ✍️ **작문 전문가** - 이메일, 문서, 요약, 번역

**사용 예시:**
- "이번 주 해야 할 작업들을 정리하고 우선순위를 정해줘"
- "AI 스타트업 시장에 대해 조사해줘"
- "파트너사에 보낼 제안 이메일을 작성해줘"
- "이 문서를 영어로 번역해줘"

무엇을 도와드릴까요?
"""
    console.print(Panel(Markdown(welcome), border_style="blue"))


def print_tool_calls(tool_calls):
    """사용된 도구 출력"""
    if tool_calls:
        console.print("\n[dim]사용된 전문가:[/dim]")
        for call in tool_calls:
            tool_name = call.get("tool", "unknown")
            success = call.get("success", False)
            status = "✓" if success else "✗"
            console.print(f"  {status} {tool_name}")


async def chat_loop():
    """대화 루프"""
    print_welcome()

    # Initialize team
    console.print("[yellow]팀 초기화 중...[/yellow]")
    try:
        team = get_team_orchestrator()
        console.print("[green]✓ 팀 준비 완료![/green]\n")
    except Exception as e:
        console.print(f"[red]오류: 팀 초기화 실패 - {str(e)}[/red]")
        console.print("[yellow]팁: .env 파일에 ANTHROPIC_API_KEY가 설정되어 있는지 확인하세요.[/yellow]")
        return

    # Chat loop
    while True:
        try:
            # Get user input
            console.print("[bold cyan]You:[/bold cyan] ", end="")
            user_input = input().strip()

            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "bye", "종료"]:
                console.print("[yellow]안녕히 가세요! 👋[/yellow]")
                break

            # Process request
            console.print("\n[yellow]처리 중...[/yellow]")

            result = await team.process_request(user_input)

            if result.get("success"):
                # Print answer
                console.print("\n[bold green]AI Team:[/bold green]")
                answer = result.get("answer", "")
                console.print(Markdown(answer))

                # Print tool calls
                tool_calls = result.get("tool_calls", [])
                print_tool_calls(tool_calls)

            else:
                error = result.get("error", "알 수 없는 오류")
                console.print(f"\n[red]오류: {error}[/red]")

            console.print()  # Add spacing

        except KeyboardInterrupt:
            console.print("\n[yellow]종료합니다... 👋[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[red]오류 발생: {str(e)}[/red]")


def main():
    """Main entry point"""
    try:
        asyncio.run(chat_loop())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
