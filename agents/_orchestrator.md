# Team Orchestrator

> MainAgent에 모든 전문가 에이전트를 Tool로 등록하고 관리하는 오케스트레이터

## 8개 통합 Tool 정의

16개 에이전트를 8개 Tool로 묶어 Tool 정의 토큰 50% 절감.

### 1. manage_productivity
- **에이전트**: Productivity
- **액션**: manage_tasks, organize_schedule, summarize_notes
- **설명**: 생산성 관련 작업 (작업 관리, 일정 조율, 메모 요약)

### 2. perform_research
- **에이전트**: Research
- **액션**: research_topic, analyze_competitors, summarize_research
- **설명**: 리서치 및 분석 작업 (주제 조사, 경쟁사 분석, 자료 요약)

### 3. perform_writing
- **에이전트**: Writing
- **액션**: write_email, write_document, translate_text, summarize_text
- **설명**: 글쓰기 및 번역 작업

### 4. consult_legal_team
- **에이전트**: Legal + Compliance
- **액션**: review_contract, provide_legal_advice, assess_compliance, monitor_compliance, create_compliance_report, identify_risks
- **설명**: 법률 및 컴플라이언스 자문

### 5. consult_business_strategy
- **에이전트**: Finance + BizDev + Product
- **액션**: analyze_finances, create_budget, forecast_financials, identify_opportunities, develop_partnership_strategy, create_growth_plan, analyze_product_opportunity, create_product_roadmap, define_feature_specs
- **설명**: 비즈니스 전략 (재무, 사업개발, 제품)

### 6. consult_tech_creative
- **에이전트**: Development + Design
- **액션**: design_architecture, review_technical_design, plan_development_process, review_ux_ui, create_brand_guidelines, design_system_audit
- **설명**: 기술 및 디자인 자문

### 7. consult_org_pr_security
- **에이전트**: HR + PR + Security
- **액션**: develop_hiring_strategy, design_org_culture, create_performance_framework, draft_press_release, create_crisis_plan, develop_media_strategy, assess_security_posture, create_security_policy, conduct_security_audit
- **설명**: 조직, 홍보, 보안 자문

### 8. consult_extended_ops
- **에이전트**: Data + Marketing + Sales
- **액션**: analyze_data, create_visualization_plan, generate_insights, create_marketing_content, plan_campaign, analyze_marketing_performance, develop_sales_strategy, manage_pipeline, create_sales_proposal
- **설명**: 데이터, 마케팅, 영업 작업

## Tool 파라미터 구조

모든 통합 Tool은 동일한 파라미터 패턴을 사용:

- **action** (string): 수행할 액션 이름
- **params** (object): 액션별 필요한 파라미터
