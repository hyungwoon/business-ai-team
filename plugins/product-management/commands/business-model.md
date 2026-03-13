---
description: Lean Canvas, Business Model Canvas, Startup Canvas, Value Proposition 프레임워크를 사용하여 비즈니스 모델을 탐색합니다
argument-hint: "[lean|full|startup|value-prop] <제품 또는 비즈니스>"
---

# /business-model -- 비즈니스 모델 탐색

네 가지 상호 보완적인 프레임워크를 사용하여 비즈니스 모델을 구축하고 분석합니다. 하나를 선택하거나 전체를 실행하여 완전한 그림을 얻으세요.

## 호출 방법

```
/business-model lean Marketplace connecting freelance PMs with startups
/business-model full Enterprise analytics platform
/business-model startup AI writing tool for non-native English speakers
/business-model value-prop SaaS onboarding tool
/business-model all SaaS onboarding tool        # 네 가지 모두 실행
/business-model                                   # 필요한 것을 물어봄
```

## 모드

---

### Lean Canvas 모드

적합한 경우: 초기 단계 아이디어, 스타트업, 신규 제품 라인.

**lean-canvas** 스킬을 적용하여 완전한 Lean Canvas를 생성합니다:

```
## Lean Canvas: [제품]

| Problem (Top 3) | Solution | Unique Value Proposition |
|-----------------|----------|------------------------|
| 1. [problem]    | [solution to each] | [single clear message] |
| 2. [problem]    |          |                        |
| 3. [problem]    |          |                        |

| Key Metrics | Unfair Advantage |
|------------|-----------------|
| [what you measure] | [what can't be copied] |

| Channels | Customer Segments |
|---------|------------------|
| [how you reach them] | [who, early adopters first] |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable] | [how you make money] |

### 가장 위험한 가정
[이것이 작동하기 위해 반드시 사실이어야 하는 것 — 위험도 순으로 우선순위 정렬]

### 실행할 실험
[가장 위험한 가정을 저비용으로 검증하는 방법]
```

---

### Full Business Model Canvas 모드

적합한 경우: 완성된 제품, 전략적 계획, 투자자 자료.

**business-model** 스킬을 적용하여 9개의 구성 요소를 모두 생성합니다:

```
## Business Model Canvas: [제품]

| Key Partners | Key Activities | Value Propositions | Customer Relationships | Customer Segments |
|-------------|---------------|-------------------|----------------------|------------------|
| [who helps you] | [core actions] | [why customers choose you] | [how you interact] | [who you serve] |

| Key Resources | | Channels | |
|-------------|---|---------|---|
| [what you need] | | [how you deliver] | |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [your costs] | [your revenue] |

### 분석
[이 모델의 강점과 약점]
[각 요소가 서로를 강화하는 방식]
[취약점과 의존 관계]
```

---

### Startup Canvas 모드

적합한 경우: 전략과 비즈니스 모델을 하나의 아티팩트로 필요로 하는 신규 제품 및 스타트업. 신규 제품에 Lean Canvas와 BMC보다 권장됨.

**startup-canvas** 스킬을 적용하여 9개 전략 섹션 + 비즈니스 모델을 포함한 Startup Canvas를 생성합니다:

```
## Startup Canvas: [제품]

### Part 1: 제품 전략

| Vision | Market Segments | Relative Costs |
|--------|----------------|---------------|
| [inspiring why] | [JTBD, first segment] | [low cost vs unique value] |

| Value Proposition | Trade-offs | Key Metrics |
|------------------|-----------|------------|
| [What before → How → What after → Alternatives] | [what you won't do] | [North Star + OMTM] |

| Growth | Capabilities | Can't/Won't |
|--------|-------------|------------|
| [PLG vs Sales-Led, channels] | [build vs partner] | [why competitors can't copy] |

### Part 2: 비즈니스 모델

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable, how they scale] | [pricing model, revenue per channel] |

### 전략 일관성 점검
[모든 요소가 서로 강화하고 있는가?]

### 가장 위험한 가정
[반드시 사실이어야 하는 것 — 그리고 테스트 방법]
```

---

### Value Proposition 모드

적합한 경우: 메시징 정제, 사용자 가치 이해, 제품-시장 적합성 분석.

**value-proposition** 스킬을 적용하여 JTBD 기반 가치 제안을 생성합니다:

```
## Value Proposition: [제품]

### For [Segment]:
1. **Who**: [타깃 사용자 프로필]
2. **Why**: [수행하려는 작업]
3. **What Before**: [현재의 고통스러운 현실]
4. **How**: [솔루션 접근 방식]
5. **What After**: [개선된 현실]
6. **Alternatives**: [당신 없이 사용할 것과 당신이 더 나은 이유]

### 가치 제안 문장
[한 문장: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]
```

---

### All 모드

네 가지 프레임워크를 모두 실행하고 프레임워크 간 인사이트를 비교하는 종합 섹션을 추가합니다.

## 워크플로우 (모든 모드)

### 1단계: 맥락 파악

질문:
- 제품 또는 비즈니스 아이디어는 무엇인가요?
- 어느 단계인가요? (아이디어, 검증됨, 확장 중)
- 개선할 기존 비즈니스 모델이 있나요?
- 타깃 고객은 누구인가요?

### 2단계: 선택한 프레임워크 생성

위에 설명된 대로 관련 스킬을 적용합니다.

### 3단계: 저장 및 반복

마크다운으로 저장합니다. 다음을 제안합니다:
- "이 모델을 SWOT 또는 PESTLE 분석으로 **스트레스 테스트**할까요?"
- "수익 흐름에 대한 **가격 전략을 설계**할까요?"
- "이 모델을 중심으로 **전략 캔버스를 구축**할까요?"
- "**비치헤드 세그먼트를 식별**할까요?"

## 참고

- **Startup Canvas**는 신규 제품의 권장 시작점 — 전략과 비즈니스 모델을 분리하며 BMC와 Lean Canvas가 놓치는 것(비전, 트레이드오프, 지표, Can't/Won't)을 다룹니다
- **Lean Canvas**는 속도와 가설 테스트에 최적 — 과도하게 고민하지 말되, 전략과 비즈니스 모델을 하나의 아티팩트로 혼합한다는 점을 인식하세요
- **BMC**는 모든 것이 어떻게 연결되는지 명확히 해야 하는 성숙한 비즈니스에 더 적합하지만, 전략적 섹션(비전, 트레이드오프, 지표)이 없습니다
- **Value Proposition**은 제품-시장 적합성 대화에 가장 날카로운 도구입니다
- "all" 모드에서는 프레임워크들이 동의하는 부분(강한 신호)과 분기하는 부분(조사 필요)을 강조하세요
