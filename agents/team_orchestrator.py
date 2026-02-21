"""
Business AI Team - Team Orchestrator
MainAgent에 모든 전문가 에이전트를 Tool로 등록하고 관리합니다.
"""
from typing import Dict, Any, Optional, List
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from agents.main_agent import MainAgent
from agents.productivity_agent import ProductivityAgent
from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent

# Advisory Team Agents
from agents.legal_agent import LegalAgent
from agents.compliance_agent import ComplianceAgent
from agents.finance_agent import FinanceAgent
from agents.business_dev_agent import BusinessDevAgent
from agents.product_agent import ProductAgent
from agents.development_agent import DevelopmentAgent
from agents.design_agent import DesignAgent
from agents.hr_agent import HRAgent
from agents.pr_agent import PRAgent
from agents.security_agent import SecurityAgent

# Extended Operations Team
from agents.data_agent import DataAgent
from agents.marketing_agent import MarketingAgent
from agents.sales_agent import SalesAgent


class TeamOrchestrator:
    """
    팀 오케스트레이터

    MainAgent와 전문가 에이전트들을 연결하고 Tool로 등록합니다.
    """

    def __init__(self):
        # Initialize main agent
        self.main_agent = MainAgent()

        # Initialize specialist agents (Operations Team)
        self.productivity_agent = ProductivityAgent()
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()

        # Initialize advisory team agents
        self.legal_agent = LegalAgent()
        self.compliance_agent = ComplianceAgent()
        self.finance_agent = FinanceAgent()
        self.business_dev_agent = BusinessDevAgent()
        self.product_agent = ProductAgent()
        self.development_agent = DevelopmentAgent()
        self.design_agent = DesignAgent()
        self.hr_agent = HRAgent()
        self.pr_agent = PRAgent()
        self.security_agent = SecurityAgent()

        # Initialize extended operations team
        self.data_agent = DataAgent()
        self.marketing_agent = MarketingAgent()
        self.sales_agent = SalesAgent()

        # Register all tools
        self._register_tools()

    def _register_tools(self):
        """모든 전문가 에이전트를 통합 Tool로 등록"""

        # 1. Productivity Tools (통합)
        self.main_agent.register_tool(
            name="manage_productivity",
            description="""생산성 관련 작업을 수행합니다. 작업 관리, 일정 조율, 메모 요약 등을 포함합니다.
            
            Actions:
            - manage_tasks: 작업 목록 생성, 우선순위 설정
            - organize_schedule: 일정 조율 및 최적화
            - summarize_notes: 메모 요약 및 구조화
            """,
            parameters={
                "action": {
                    "type": "string",
                    "enum": ["manage_tasks", "organize_schedule", "summarize_notes"],
                    "description": "수행할 작업 유형"
                },
                "params": {
                    "type": "object",
                    "description": "작업 수행에 필요한 파라미터 (각 action별 요구사항 참조)",
                    "properties": {
                        "request": {"type": "string"},
                        "tasks": {"type": "array", "items": {"type": "object"}},
                        "events": {"type": "array", "items": {"type": "string"}},
                        "constraints": {"type": "string"},
                        "notes": {"type": "string"}
                    }
                }
            },
            handler=self._handle_productivity_request
        )

        # 2. Research Tools (통합)
        self.main_agent.register_tool(
            name="perform_research",
            description="""리서치 및 분석 작업을 수행합니다. 주제 조사, 경쟁사 분석, 자료 요약 등을 포함합니다.
            
            Actions:
            - research_topic: 특정 주제 포괄적 조사
            - analyze_competitors: 경쟁사 분석 및 비교
            - summarize_research: 조사 자료 요약 및 인사이트
            """,
            parameters={
                "action": {
                    "type": "string",
                    "enum": ["research_topic", "analyze_competitors", "summarize_research"],
                    "description": "수행할 리서치 작업 유형"
                },
                "params": {
                    "type": "object",
                    "description": "리서치 파라미터",
                    "properties": {
                        "topic": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                        "competitors": {"type": "array", "items": {"type": "string"}},
                        "focus": {"type": "string"},
                        "documents": {"type": "string"}
                    }
                }
            },
            handler=self._handle_research_request
        )

        # 3. Writing Tools (통합)
        self.main_agent.register_tool(
            name="perform_writing",
            description="""글쓰기 및 번역 작업을 수행합니다. 이메일, 문서 작성, 텍스트 요약, 번역 등을 포함합니다.
            
            Actions:
            - write_email: 이메일 작성
            - write_document: 보고서/제안서 등 문서 작성
            - translate_text: 텍스트 번역
            - summarize_text: 텍스트 요약
            """,
            parameters={
                "action": {
                    "type": "string",
                    "enum": ["write_email", "write_document", "translate_text", "summarize_text"],
                    "description": "수행할 글쓰기 작업 유형"
                },
                "params": {
                    "type": "object",
                    "description": "글쓰기 파라미터",
                    "properties": {
                        "purpose": {"type": "string"},
                        "recipient": {"type": "string"},
                        "key_points": {"type": "string"},
                        "tone": {"type": "string"},
                        "doc_type": {"type": "string"},
                        "topic": {"type": "string"},
                        "details": {"type": "string"},
                        "length": {"type": "string"},
                        "text": {"type": "string"},
                        "source_lang": {"type": "string"},
                        "target_lang": {"type": "string"},
                        "target_length": {"type": "string"}
                    }
                }
            },
            handler=self._handle_writing_request
        )

        # 4. Advisory Tools (통합 - 그룹별)
        
        # Legal & Compliance
        self.main_agent.register_tool(
            name="consult_legal_team",
            description="""법률 및 컴플라이언스 자문을 구합니다.
            
            Actions:
            - review_contract: 계약서 검토
            - provide_legal_advice: 법률 자문
            - assess_compliance: 규정 준수 평가
            - monitor_compliance: 컴플라이언스 모니터링
            - create_compliance_report: 리포트 작성
            - identify_risks: 리스크 식별
            """,
            parameters={
                "action": {
                    "type": "string",
                    "enum": [
                        "review_contract", "provide_legal_advice", "assess_compliance",
                        "monitor_compliance", "create_compliance_report", "identify_risks"
                    ],
                    "description": "수행할 법률/컴플라이언스 작업"
                },
                "params": {
                    "type": "object",
                    "description": "작업 파라미터 (contract_text, situation, questions, business_practice, etc.)"
                }
            },
            handler=self._handle_legal_compliance_request
        )

        # Business Strategy (Finance, BizDev, Product)
        self.main_agent.register_tool(
            name="consult_business_strategy",
            description="""비즈니스 전략(재무, 사업개발, 제품) 관련 자문을 구합니다.
            
            Actions:
            - analyze_finances, create_budget, forecast_financials (Finance)
            - identify_opportunities, develop_partnership, create_growth_plan (BizDev)
            - analyze_product_opp, create_roadmap, define_specs (Product)
            """,
            parameters={
                "action": {
                    "type": "string",
                    "description": "수행할 비즈니스 전략 작업"
                },
                "params": {
                    "type": "object",
                    "description": "작업 파라미터"
                }
            },
            handler=self._handle_business_strategy_request
        )

        # Technical & Creative (Dev, Design)
        self.main_agent.register_tool(
            name="consult_tech_creative",
            description="""기술 및 디자인 관련 자문을 구합니다.
            
            Actions:
            - design_architecture, review_tech_design, plan_dev_process (Dev)
            - review_ux_ui, create_brand_guidelines, design_system_audit (Design)
            """,
            parameters={
                "action": {
                    "type": "string",
                    "description": "수행할 기술/디자인 작업"
                },
                "params": {
                    "type": "object",
                    "description": "작업 파라미터"
                }
            },
            handler=self._handle_tech_creative_request
        )

        # Org & PR (HR, PR, Security)
        self.main_agent.register_tool(
            name="consult_org_pr_security",
            description="""조직, 홍보, 보안 관련 자문을 구합니다.

            Actions:
            - develop_hiring, design_culture (HR)
            - draft_press_release, create_crisis_plan (PR)
            - assess_security, create_security_policy (Security)
            """,
            parameters={
                "action": {
                    "type": "string",
                    "description": "수행할 작업"
                },
                "params": {
                    "type": "object",
                    "description": "작업 파라미터"
                }
            },
            handler=self._handle_org_pr_security_request
        )

        # Extended Operations (Data, Marketing, Sales)
        self.main_agent.register_tool(
            name="consult_extended_ops",
            description="""데이터, 마케팅, 영업 관련 작업을 수행합니다.

            Actions:
            - analyze_data, create_visualization_plan, generate_insights (Data)
            - create_marketing_content, plan_campaign, analyze_marketing_performance (Marketing)
            - develop_sales_strategy, manage_pipeline, create_sales_proposal (Sales)
            """,
            parameters={
                "action": {
                    "type": "string",
                    "description": "수행할 작업"
                },
                "params": {
                    "type": "object",
                    "description": "작업 파라미터"
                }
            },
            handler=self._handle_extended_ops_request
        )

    # Unified Tool Handlers

    async def _handle_productivity_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """ProductivityAgent 통합 핸들러"""
        if action == "manage_tasks":
            return await self.productivity_agent.manage_tasks(
                params.get("request", ""), 
                params.get("tasks")
            )
        elif action == "organize_schedule":
            return await self.productivity_agent.organize_schedule(
                params.get("events", []), 
                params.get("constraints")
            )
        elif action == "summarize_notes":
            return await self.productivity_agent.summarize_notes(
                params.get("notes", "")
            )
        else:
            return {"success": False, "error": f"Unknown productivity action: {action}"}

    async def _handle_research_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """ResearchAgent 통합 핸들러"""
        if action == "research_topic":
            return await self.research_agent.research_topic(
                params.get("topic", ""),
                params.get("focus_areas")
            )
        elif action == "analyze_competitors":
            return await self.research_agent.analyze_competitors(
                params.get("competitors", []),
                params.get("focus")
            )
        elif action == "summarize_research":
            return await self.research_agent.summarize_findings(
                params.get("documents", "")
            )
        else:
            return {"success": False, "error": f"Unknown research action: {action}"}

    async def _handle_writing_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """WritingAgent 통합 핸들러"""
        if action == "write_email":
            return await self.writing_agent.write_email(
                params.get("purpose", ""),
                params.get("recipient", ""),
                params.get("key_points", ""),
                params.get("tone", "professional")
            )
        elif action == "write_document":
            return await self.writing_agent.write_document(
                params.get("doc_type", ""),
                params.get("topic", ""),
                params.get("details", ""),
                params.get("length", "medium")
            )
        elif action == "translate_text":
            return await self.writing_agent.translate(
                params.get("text", ""),
                params.get("source_lang", ""),
                params.get("target_lang", "")
            )
        elif action == "summarize_text":
            return await self.writing_agent.summarize_text(
                params.get("text", ""),
                params.get("target_length", "short")
            )
        else:
            return {"success": False, "error": f"Unknown writing action: {action}"}

    async def _handle_legal_compliance_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Legal & Compliance 통합 핸들러"""
        # Legal
        if action == "review_contract":
            return await self.legal_agent.review_contract(params.get("contract_text"), params.get("focus"))
        elif action == "provide_legal_advice":
            return await self.legal_agent.provide_advice(params.get("situation"), params.get("questions"))
        elif action == "assess_compliance":
            return await self.legal_agent.assess_compliance(params.get("business_practice"), params.get("regulations"))
        
        # Compliance
        elif action == "monitor_compliance":
            return await self.compliance_agent.monitor_compliance(params.get("areas", []))
        elif action == "create_compliance_report":
            return await self.compliance_agent.create_report(params.get("period"), params.get("focus_areas"))
        elif action == "identify_risks":
            return await self.compliance_agent.identify_risks(params.get("business_process"))
            
        else:
            return {"success": False, "error": f"Unknown legal/compliance action: {action}"}

    async def _handle_business_strategy_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Business Strategy (Finance, BizDev, Product) 통합 핸들러"""
        # Finance
        if action == "analyze_finances":
            return await self.finance_agent.analyze_finances(params.get("financial_data"), params.get("period"))
        elif action == "create_budget":
            return await self.finance_agent.create_budget(params.get("departments"), params.get("total_budget"), params.get("constraints"))
        elif action == "forecast_financials":
            return await self.finance_agent.forecast_financials(params.get("historical_data"), params.get("growth_assumptions"))
            
        # BizDev
        elif action == "identify_opportunities":
            return await self.business_dev_agent.identify_opportunities(params.get("market"), params.get("focus_areas"))
        elif action == "develop_partnership_strategy":
            return await self.business_dev_agent.develop_partnership_strategy(params.get("partner_type"), params.get("objectives"))
        elif action == "create_growth_plan":
            return await self.business_dev_agent.create_growth_plan(params.get("current_state"), params.get("target_goals"), params.get("timeframe"))

        # Product
        elif action == "analyze_product_opportunity":
            return await self.product_agent.analyze_opportunity(params.get("market"), params.get("customer_problem"))
        elif action == "create_product_roadmap":
            return await self.product_agent.create_roadmap(params.get("product_vision"), params.get("phases"))
        elif action == "define_feature_specs":
            return await self.product_agent.define_specs(params.get("feature_description"), params.get("requirements"))
            
        else:
            return {"success": False, "error": f"Unknown business strategy action: {action}"}

    async def _handle_tech_creative_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Technical & Creative (Dev, Design) 통합 핸들러"""
        # Development
        if action == "design_architecture":
            return await self.development_agent.design_architecture(params.get("product_requirements"), params.get("constraints"))
        elif action == "review_technical_design":
            return await self.development_agent.review_design(params.get("design_document"), params.get("focus"))
        elif action == "plan_development_process":
            return await self.development_agent.plan_process(params.get("team_size"), params.get("project_scope"), params.get("timeline"))
            
        # Design
        elif action == "review_ux_ui":
            return await self.design_agent.review_ux_ui(params.get("product_description"), params.get("issues"))
        elif action == "create_brand_guidelines":
            return await self.design_agent.create_brand_guidelines(params.get("brand_info"), params.get("target_audience"))
        elif action == "design_system_audit":
            return await self.design_agent.audit_design_system(params.get("current_system"), params.get("goals"))
            
        else:
            return {"success": False, "error": f"Unknown technical/creative action: {action}"}

    async def _handle_org_pr_security_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Org & PR & Security 통합 핸들러"""
        # HR
        if action == "develop_hiring_strategy":
            return await self.hr_agent.develop_hiring_strategy(params.get("positions"), params.get("company_context"))
        elif action == "design_org_culture":
            return await self.hr_agent.design_culture(params.get("current_culture"), params.get("desired_values"))
        elif action == "create_performance_framework":
            return await self.hr_agent.create_performance_framework(params.get("team_structure"), params.get("goals"))
            
        # PR
        elif action == "draft_press_release":
            return await self.pr_agent.draft_press_release(params.get("news_topic"), params.get("key_messages"), params.get("company_info"))
        elif action == "create_crisis_plan":
            return await self.pr_agent.create_crisis_plan(params.get("crisis_scenario"), params.get("stakeholders"))
        elif action == "develop_media_strategy":
            return await self.pr_agent.develop_media_strategy(params.get("objectives"), params.get("target_media"), params.get("budget"))

        # Security
        elif action == "assess_security_posture":
            return await self.security_agent.assess_posture(params.get("system_description"), params.get("current_measures"))
        elif action == "create_security_policy":
            return await self.security_agent.create_policy(params.get("scope"), params.get("requirements"))
        elif action == "conduct_security_audit":
            return await self.security_agent.conduct_audit(params.get("audit_scope"), params.get("standards"))
            
        else:
            return {"success": False, "error": f"Unknown org/pr/security action: {action}"}

    async def _handle_extended_ops_request(self, action: str, params: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Extended Operations (Data, Marketing, Sales) 통합 핸들러"""
        # Data
        if action == "analyze_data":
            return await self.data_agent.analyze_data(params.get("data_description"), params.get("analysis_goal"))
        elif action == "create_visualization_plan":
            return await self.data_agent.create_visualization_plan(params.get("data_type"), params.get("audience"), params.get("purpose"))
        elif action == "generate_insights":
            return await self.data_agent.generate_insights(params.get("business_context"), params.get("data_findings"))

        # Marketing
        elif action == "create_marketing_content":
            return await self.marketing_agent.create_marketing_content(params.get("content_type"), params.get("topic"), params.get("target_audience"))
        elif action == "plan_campaign":
            return await self.marketing_agent.plan_campaign(params.get("campaign_goal"), params.get("budget"), params.get("duration"))
        elif action == "analyze_marketing_performance":
            return await self.marketing_agent.analyze_marketing_performance(params.get("metrics_data"), params.get("period"))

        # Sales
        elif action == "develop_sales_strategy":
            return await self.sales_agent.develop_sales_strategy(params.get("target_market"), params.get("goals"), params.get("resources"))
        elif action == "manage_pipeline":
            return await self.sales_agent.manage_pipeline(params.get("pipeline_data"), params.get("focus"))
        elif action == "create_sales_proposal":
            return await self.sales_agent.create_sales_proposal(params.get("client_info"), params.get("solution"), params.get("pricing"))

        else:
            return {"success": False, "error": f"Unknown extended ops action: {action}"}


    # Public API

    async def process_request(
        self,
        user_message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        사용자 요청 처리

        Args:
            user_message: 사용자 메시지
            context: 추가 컨텍스트

        Returns:
            처리 결과
        """
        return await self.main_agent.process_request(
            user_message=user_message,
            context=context
        )


# Global instance
_team_orchestrator: Optional[TeamOrchestrator] = None


def get_team_orchestrator() -> TeamOrchestrator:
    """전역 팀 오케스트레이터 인스턴스 반환"""
    global _team_orchestrator
    if _team_orchestrator is None:
        _team_orchestrator = TeamOrchestrator()
    return _team_orchestrator
