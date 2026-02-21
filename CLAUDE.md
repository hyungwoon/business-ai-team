# CLAUDE.md

## 프로젝트 개요
비즈니스를 돕는 범용 AI 전문가 팀 시스템. 마케팅, 리서치, 전략 수립, 문서 작성 등 다양한 비즈니스 업무를 지원한다.

## 폴더 구조
```
business-ai-team/
├── agents/           # AI 에이전트 모듈
│   ├── base_agent.py           # 공통 BaseAgent (Prompt Caching 포함)
│   ├── main_agent.py           # 팀 리더 에이전트
│   ├── team_orchestrator.py    # 팀 조율 및 8개 통합 Tool 등록
│   └── [16개 전문가 에이전트]
├── core/             # 설정, 플러그인 로더
├── plugins/          # Anthropic 플러그인 (marketing, sales, data, productivity, enterprise-search)
├── archive/          # 사용자 요청 결과물 보관 (컨텍스트 제외 대상)
└── venv/             # Python 가상환경
```

## 작업 규칙

### 결과물 저장
- 사용자 요청으로 생성한 리서치, 전략, 기획 문서 → `archive/` 폴더에 저장
- archive 폴더는 에이전트 검색/참조 대상에서 제외
- 코드, 시스템 문서는 루트 또는 해당 폴더에 저장

### 파일명 규칙
- 한글 파일명 사용 가능
- 내용을 명확히 알 수 있는 이름 사용
- 예: `빈센트_스튜디오_브랜드_마케팅_전략.md`

### 에이전트 추가 규칙
- **반드시 BaseAgent 상속** (`agents/base_agent.py`)
- `super().__init__(plugin_names=[...], use_light_model=False/True)`
- `self.system_prompt = self._build_system_prompt(base_prompt, "Section Name")`
- LLM 호출은 `self._call_llm(prompt, max_tokens)` 사용 (Prompt Caching 자동 적용)
- 응답은 `self._ok(**data)` 또는 `self._err(msg)` 사용

### 모델 계층화 원칙
- 단순 처리 (메모 정리, 이메일 작성 등) → `use_light_model=True` (Haiku)
- 복잡한 분석/전략 작업 → `use_light_model=False` (Sonnet, 기본값)

## 문서 작성 스타일
- 기본 언어: 한국어
- 마크다운 포맷 사용
- 실용적이고 실행 가능한 내용 중심
- 불필요한 장식(이모지 등) 최소화

## 자주 사용하는 명령어
```bash
# 가상환경 활성화
source venv/bin/activate

# 시스템 실행
./venv/bin/python3 assistant.py

# 단일 요청
./venv/bin/python3 run_request.py "요청 내용"

# 시스템 검증 테스트
./venv/bin/python3 test_complete_system.py
```

## 환경 설정
- Python 3.13
- Anthropic API 키 필요 (.env 파일)
- 모델: Sonnet (복잡 작업), Haiku (단순 작업)

## 토큰 최적화 (상세: TOKEN_OPTIMIZATION.md)
1. 16개 에이전트 → 8개 통합 Tool (Tool 정의 토큰 50% 절감)
2. Prompt Caching 적용 (입력 토큰 60~90% 절감)
3. 히스토리 슬라이딩 윈도우 (장기 세션 30% 절감)
4. Tool 정의 캐시 (루프당 재구성 방지)
5. 모델 계층화 (단순 작업 Haiku 사용)
