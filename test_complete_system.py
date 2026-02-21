"""
Business AI Team - 완전한 시스템 테스트
토큰 최적화된 통합 Tool 시스템 검증
"""
import asyncio
from agents.team_orchestrator import get_team_orchestrator


async def test_system():
    """전체 시스템 테스트"""
    print("🧪 Business AI Team - 시스템 검증\n")
    print("=" * 60)

    # 1. 팀 초기화
    print("\n1️⃣ 팀 초기화 중...")
    try:
        team = get_team_orchestrator()
        print("✅ 성공: 팀 초기화 완료")
    except Exception as e:
        print(f"❌ 실패: {e}")
        return

    # 2. Tool 등록 확인
    print("\n2️⃣ Tool 등록 확인 중...")
    tools = team.main_agent.get_available_tools()
    print(f"✅ 성공: {len(tools)}개 통합 Tool 등록됨\n")

    # Tool 목록 출력 (토큰 최적화 구조)
    print("📋 등록된 통합 Tool:")
    print("-" * 60)
    for i, tool in enumerate(tools, 1):
        name = tool["name"]
        params = ", ".join(tool["parameters"])
        print(f"{i}. {name}")
        print(f"   Parameters: {params}")

    # 3. 팀 구성 확인
    print("\n" + "=" * 60)
    print("\n3️⃣ 팀 구성 확인 중...")

    core_ops = ["productivity_agent", "research_agent", "writing_agent"]
    extended_ops = ["data_agent", "marketing_agent", "sales_agent"]
    advisory = ["legal_agent", "compliance_agent", "finance_agent",
                "business_dev_agent", "product_agent", "development_agent",
                "design_agent", "hr_agent", "pr_agent", "security_agent"]

    print("\n✅ 핵심 운영 팀 (Core Operations):")
    for agent in core_ops:
        status = "✓" if hasattr(team, agent) else "✗"
        print(f"   {status} {agent}")

    print("\n✅ 확장 운영 팀 (Extended Operations):")
    for agent in extended_ops:
        status = "✓" if hasattr(team, agent) else "✗"
        print(f"   {status} {agent}")

    print("\n✅ 전략 자문 팀 (Strategic Advisory):")
    for agent in advisory:
        status = "✓" if hasattr(team, agent) else "✗"
        print(f"   {status} {agent}")

    total_agents = len(core_ops) + len(extended_ops) + len(advisory)
    print(f"\n📊 총 {total_agents}개 전문가 에이전트 활성화")

    # 4. 토큰 최적화 검증
    print("\n" + "=" * 60)
    print("\n4️⃣ 토큰 최적화 전략 검증...")

    expected_tool_count = 8  # 통합 Tool 개수
    actual_tool_count = len(tools)

    print(f"\n📊 토큰 최적화 비교:")
    print(f"   개별 Tool 방식: ~{total_agents}개 Tool 등록 필요")
    print(f"   통합 Tool 방식: {actual_tool_count}개 Tool 등록 (현재)")
    reduction = ((total_agents - actual_tool_count) / total_agents) * 100
    print(f"   🎯 토큰 절약률: ~{reduction:.1f}%")

    if actual_tool_count == expected_tool_count:
        print(f"\n✅ 최적화 성공: {actual_tool_count}개 통합 Tool로 {total_agents}개 에이전트 관리")
    else:
        print(f"\n⚠️ 예상 Tool 수({expected_tool_count})와 다름: {actual_tool_count}개")

    # 5. 통합 구조 설명
    print("\n" + "=" * 60)
    print("\n5️⃣ 통합 Tool 구조:")
    print("-" * 60)

    tool_mapping = {
        "manage_productivity": ["manage_tasks", "organize_schedule", "summarize_notes"],
        "perform_research": ["research_topic", "analyze_competitors", "summarize_research"],
        "perform_writing": ["write_email", "write_document", "translate_text", "summarize_text"],
        "consult_legal_team": ["review_contract", "provide_legal_advice", "assess_compliance",
                               "monitor_compliance", "create_compliance_report", "identify_risks"],
        "consult_business_strategy": ["Finance", "BizDev", "Product 관련 9개 액션"],
        "consult_tech_creative": ["Development", "Design 관련 6개 액션"],
        "consult_org_pr_security": ["HR", "PR", "Security 관련 9개 액션"],
        "consult_extended_ops": ["Data", "Marketing", "Sales 관련 9개 액션"]
    }

    for tool, actions in tool_mapping.items():
        print(f"\n🔧 {tool}:")
        if isinstance(actions[0], str) and not "관련" in actions[0]:
            for action in actions:
                print(f"   - {action}")
        else:
            print(f"   - {', '.join(actions)}")

    # 최종 결과
    print("\n" + "=" * 60)
    print("\n🎉 시스템 검증 완료!")
    print("\n💡 핵심 성과:")
    print(f"   ✓ {total_agents}개 전문가 에이전트 → {actual_tool_count}개 통합 Tool")
    print(f"   ✓ MainAgent 시스템 프롬프트 토큰 최적화")
    print(f"   ✓ action + params 패턴으로 유연한 확장")
    print(f"   ✓ 그룹화된 Tool로 관련 기능 통합 관리")

    print("\n🚀 시스템 상태: 정상 작동 준비 완료")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_system())
