# Business AI Team

당신의 비즈니스를 돕는 범용 AI 전문가 팀.

마케팅, 리서치, 전략 수립, 문서 작성 등 비즈니스 전 분야를 16명의 AI 전문가가 지원합니다.

---

## 전문가 팀 구성

```
MainAgent (팀 리더)
│
├── 핵심 운영팀 (Core Operations)
│   ├── ProductivityAgent   → 작업 관리, 일정 조율, 메모 정리       [Haiku]
│   ├── ResearchAgent       → 시장 조사, 경쟁사 분석, 트렌드 리서치  [Sonnet]
│   └── WritingAgent        → 이메일, 문서, 번역                   [Haiku]
│
├── 확장 운영팀 (Extended Operations)
│   ├── DataAgent           → 데이터 분석, 시각화, 인사이트          [Sonnet]
│   ├── MarketingAgent      → 마케팅 콘텐츠, 캠페인 기획             [Sonnet]
│   └── SalesAgent          → 영업 전략, 파이프라인, 제안서           [Sonnet]
│
└── 전략 자문팀 (Strategic Advisory)
    ├── LegalAgent          → 계약 검토, 법률 자문                   [Sonnet]
    ├── ComplianceAgent     → 규정 준수, 리스크 관리                  [Sonnet]
    ├── FinanceAgent        → 재무 분석, 예산 계획                   [Sonnet]
    ├── BusinessDevAgent    → 사업 기회, 파트너십 전략                [Sonnet]
    ├── ProductAgent        → 제품 전략, 로드맵, 기능 스펙            [Sonnet]
    ├── DevelopmentAgent    → 기술 아키텍처, 개발 프로세스            [Sonnet]
    ├── DesignAgent         → UX/UI, 브랜드 가이드라인               [Sonnet]
    ├── HRAgent             → 채용 전략, 조직 문화, 성과 관리         [Sonnet]
    ├── PRAgent             → 보도자료, 위기 관리, 미디어 전략        [Sonnet]
    └── SecurityAgent       → 보안 평가, 정책 수립, 보안 감사         [Sonnet]
```

---

## 시작하기

### 1. 환경 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. API 키 설정

```bash
cp .env.example .env
# .env 파일에 ANTHROPIC_API_KEY 입력
```

### 3. 실행

```bash
# 대화형 인터페이스
python3 assistant.py

# 단일 요청 실행
python3 run_request.py "경쟁사 3곳 분석 후 차별화 전략 보고서 작성해줘"

# 시스템 검증
python3 test_complete_system.py
```

---

## 사용 예시

```
# 작업 관리
"이번 주 해야 할 작업 정리하고 우선순위 잡아줘. 신제품 출시 준비, 투자자 미팅, 마케팅 자료 작성."

# 리서치
"AI 에이전트 시장 조사해줘. 주요 트렌드와 경쟁사 분석."

# 문서 작성
"파트너사에 보낼 협업 제안 이메일 작성해줘."

# 복합 작업
"경쟁사 3곳 분석하고 결과를 바탕으로 차별화 전략 보고서 써줘."

# 재무
"이 재무 데이터 분석해줘. 주요 지표와 개선 기회 포함."

# 법률
"이 계약서 검토하고 위험 요소 알려줘."
```

---

## 아키텍처

### 처리 흐름

```
사용자 요청
    ↓
MainAgent (팀 리더)
    │  - 요청 분석
    │  - Prompt Caching 적용 (시스템 프롬프트 캐시)
    │  - 히스토리 슬라이딩 윈도우 (최근 20개 메시지)
    ↓
Tool Use Pattern (8개 통합 Tool)
    │  - Tool 정의 캐시 (루프당 재구성 없음)
    ↓
전문가 에이전트 실행
    │  - Prompt Caching 적용 (각 에이전트 시스템 프롬프트)
    │  - Plugin 베스트 프랙티스 통합
    │  - 모델 계층화 (단순 작업 Haiku, 복잡 분석 Sonnet)
    ↓
결과 통합 → 사용자
```

### 8개 통합 Tool (토큰 최적화 핵심)

16개 에이전트를 8개 Tool로 묶어 Tool 정의 토큰 50% 절감.

| Tool | 담당 에이전트 |
|------|-------------|
| `manage_productivity` | ProductivityAgent |
| `perform_research` | ResearchAgent |
| `perform_writing` | WritingAgent |
| `consult_extended_ops` | Data, Marketing, Sales |
| `consult_legal_team` | Legal, Compliance |
| `consult_business_strategy` | Finance, BizDev, Product |
| `consult_tech_creative` | Development, Design |
| `consult_org_pr_security` | HR, PR, Security |

### 토큰 최적화 현황

| 최적화 항목 | 절감 효과 |
|-----------|---------|
| 8개 통합 Tool (16→8) | Tool 정의 토큰 50% |
| Prompt Caching (ephemeral) | 입력 토큰 60~90% (캐시 히트 시) |
| 히스토리 슬라이딩 윈도우 | 장기 세션 30% |
| Tool 정의 캐시 (루프 외부) | 반복당 5~10% |
| 모델 계층화 (Haiku/Sonnet) | 단순 작업 60~70% |

---

## 프로젝트 구조

```
business-ai-team/
├── assistant.py              # 대화형 CLI 인터페이스
├── run_request.py            # 단일 요청 실행
├── test_complete_system.py   # 시스템 검증 테스트
├── requirements.txt
├── .env.example
├── .gitignore
├── CLAUDE.md                 # 개발 가이드 (AI 에이전트용)
│
├── agents/
│   ├── base_agent.py         # 공통 BaseAgent (Prompt Caching 포함)
│   ├── main_agent.py         # 메인 에이전트 (팀 리더)
│   ├── team_orchestrator.py  # 팀 조율 및 Tool 등록
│   ├── productivity_agent.py
│   ├── research_agent.py
│   ├── writing_agent.py
│   ├── data_agent.py
│   ├── marketing_agent.py
│   ├── sales_agent.py
│   ├── legal_agent.py
│   ├── compliance_agent.py
│   ├── finance_agent.py
│   ├── business_dev_agent.py
│   ├── product_agent.py
│   ├── development_agent.py
│   ├── design_agent.py
│   ├── hr_agent.py
│   ├── pr_agent.py
│   └── security_agent.py
│
├── core/
│   ├── config.py             # 설정 (모델 계층화 포함)
│   └── plugin_loader.py      # Anthropic 플러그인 로더
│
├── plugins/                  # Anthropic 플러그인
│   ├── marketing/
│   ├── productivity/
│   ├── sales/
│   ├── data/
│   └── enterprise-search/
│
└── archive/                  # 결과물 보관 (Git 제외)
```

---

## 새 에이전트 추가 방법

1. `agents/new_agent.py` 생성 (BaseAgent 상속)

```python
from agents.base_agent import BaseAgent

class NewAgent(BaseAgent):
    def __init__(self):
        super().__init__(plugin_names=["marketing"])  # 필요한 플러그인
        base_prompt = "당신은 ... 전문가입니다."
        self.system_prompt = self._build_system_prompt(base_prompt)

    async def do_something(self, param: str) -> dict:
        prompt = f"..."
        return self._ok(result=self._call_llm(prompt))
```

2. `agents/team_orchestrator.py`에서 에이전트 등록

---

## 설정

`.env` 파일:

```
ANTHROPIC_API_KEY=your-api-key
MODEL_NAME=claude-sonnet-4-5          # 복잡한 작업용 (기본값)
MODEL_NAME_LIGHT=claude-haiku-4-5-20251001  # 단순 작업용
```

---

## 문제 해결

**ANTHROPIC_API_KEY not found**
`.env` 파일과 API 키를 확인하세요.

**Module not found**
```bash
source venv/bin/activate && pip install -r requirements.txt
```

**Plugin 스킬 경고**
일부 스킬이 없어도 에이전트는 정상 작동합니다. 경고는 무시해도 됩니다.
