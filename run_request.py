#!/usr/bin/env python3
"""
Run a single request through Business AI Team
"""
import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from agents.team_orchestrator import get_team_orchestrator


async def run_request(request: str):
    """Run a request through the team"""
    print("🤖 Business AI Team 초기화 중...\n")

    team = get_team_orchestrator()
    print("✓ 팀 준비 완료!\n")
    print(f"📋 요청: {request[:100]}...\n")
    print("=" * 60)
    print("처리 중...\n")

    # Call main_agent directly with higher max_iterations
    result = await team.main_agent.process_request(
        user_message=request,
        max_iterations=20
    )

    if result.get("success"):
        print("\n📝 AI Team 응답:\n")
        print(result.get("answer", ""))

        tool_calls = result.get("tool_calls", [])
        if tool_calls:
            print("\n" + "=" * 60)
            print("🔧 사용된 전문가:")
            for call in tool_calls:
                status = "✓" if call.get("success") else "✗"
                print(f"  {status} {call.get('tool')}")
    else:
        print(f"\n❌ 오류: {result.get('error')}")

    return result


if __name__ == "__main__":
    request = """'에터널링크(EternalLink)' - AI 기반 사후 데이터 관리 플랫폼에 대한 상세 사업 기획서를 작성해줘.

## 요청 사항

### 1. 상세 사업 기획서
- 비전 및 미션
- 문제 정의 및 솔루션
- 타겟 고객 세그먼트 (페르소나 포함)
- 핵심 가치 제안 (Value Proposition)
- 수익 모델 상세 (가격 전략, 단위 경제)
- 마케팅 및 고객 획득 전략
- 운영 계획
- 재무 계획 (3년 추정)
- 리스크 분석 및 대응 전략

### 2. 프로덕트 개발 로드맵
- 기술 스택 및 아키텍처
- MVP 기능 정의
- 단계별 기능 로드맵 (Phase 1, 2, 3)
- 개발 일정 및 마일스톤
- 필요 인력 및 조직 구성

### 3. AI 에이전트 시스템 설계
- 에이전트 종류 및 역할
- 데이터 수집/처리 방식
- 보안 및 프라이버시 설계
- 윤리적 가이드라인

한국 시장 특성을 반영하고, 실제 실행 가능한 수준의 구체적인 계획을 세워줘."""

    asyncio.run(run_request(request))
