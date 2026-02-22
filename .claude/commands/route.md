---
description: 비즈니스 요청을 전문가 에이전트에 라우팅합니다. 에이전트 시스템 프롬프트와 SKILL.md를 반드시 읽은 후 전문가 관점으로 응답합니다.
---

# 전문가 라우팅 커맨드

사용자의 비즈니스 요청: $ARGUMENTS

## 실행 절차 (순서 엄수, 생략 불가)

### 1단계: 도메인 분류

아래 매핑 테이블에서 요청에 해당하는 에이전트를 식별한다. 복합 요청이면 여러 에이전트를 식별한다.

| 키워드 | 에이전트 | 파일 |
|---|---|---|
| 작업관리, 일정, 메모, 생산성 | Productivity | `agents/productivity.md` |
| 리서치, 조사, 경쟁사분석, 트렌드, 생명과학 | Research | `agents/research.md` |
| 이메일, 문서작성, 번역, 요약 | Writing | `agents/writing.md` |
| 마케팅, 캠페인, 콘텐츠, 브랜드 | Marketing | `agents/marketing.md` |
| 영업, 파이프라인, 제안서, CRM | Sales | `agents/sales.md` |
| 데이터분석, 시각화, 인사이트, 통계 | Data | `agents/data.md` |
| 계약검토, 법률자문, 규정 | Legal | `agents/legal.md` |
| 컴플라이언스, 리스크, 감사 | Compliance | `agents/compliance.md` |
| 재무분석, 예산, 투자, ROI | Finance | `agents/finance.md` |
| 사업개발, 파트너십, 성장전략, M&A | BizDev | `agents/business-dev.md` |
| 제품전략, 로드맵, 기능스펙, PM | Product | `agents/product.md` |
| 기술아키텍처, 개발프로세스, CTO | Development | `agents/development.md` |
| UX/UI, 브랜드가이드, 디자인시스템 | Design | `agents/design.md` |
| 채용, 조직문화, 성과관리, HR | HR | `agents/hr.md` |
| 보도자료, 위기관리, 미디어전략 | PR | `agents/pr.md` |
| 보안평가, 보안정책, 사이버보안 | Security | `agents/security.md` |

### 2단계: 에이전트 시스템 프롬프트 읽기 (필수)

식별된 에이전트의 `.md` 파일을 Read 도구로 **반드시** 읽는다.

- 단일 에이전트: 해당 파일 1개 읽기
- 복합 에이전트: 주 에이전트 + 보조 에이전트 모두 읽기 (병렬 Read 사용)

**이 단계를 건너뛰면 안 된다. 기억이나 추정으로 대체 금지.**

### 3단계: 플러그인 스킬 읽기 (필수)

에이전트 .md 파일의 "플러그인 & 스킬 라우팅" 섹션에서 요청과 관련된 스킬을 확인하고, 해당 `SKILL.md`를 Read 도구로 **반드시** 읽는다.

경로 패턴: `plugins/[플러그인명]/skills/[스킬명]/SKILL.md`

- 요청과 직접 관련된 스킬만 선택적으로 읽기 (모든 스킬을 읽을 필요 없음)
- 복수 스킬이 필요하면 병렬 Read 사용

### 4단계: 전문가 관점 응답

읽은 에이전트 시스템 프롬프트의 원칙, 커뮤니케이션 스타일, 출력 기준을 적용하고,
읽은 SKILL.md의 베스트 프랙티스, 프레임워크, 템플릿을 활용하여 응답한다.

### 5단계: 담당 표시 (필수)

응답 **맨 앞에** 반드시 다음 형식으로 표시:

```
> **담당**: [에이전트명] | 참조 스킬: [사용한 스킬명]
```

예시:
- `> **담당**: Marketing | 참조 스킬: content-creation, campaign-planning`
- `> **담당**: Research + Product | 참조 스킬: competitive-analysis, feature-spec`

---

## 검증 체크리스트

응답 전 확인:
- [ ] 에이전트 .md 파일을 실제로 Read 했는가?
- [ ] 관련 SKILL.md를 실제로 Read 했는가?
- [ ] 응답에 `> **담당**:` 표시가 있는가?
- [ ] 에이전트의 커뮤니케이션 스타일과 출력 기준을 반영했는가?
