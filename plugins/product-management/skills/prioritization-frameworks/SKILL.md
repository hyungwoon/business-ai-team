---
name: prioritization-frameworks
description: "공식, 사용 시기 가이드, 템플릿이 포함된 9가지 우선순위 프레임워크 참고 자료 — RICE, ICE, Kano, MoSCoW, Opportunity Score 등. 우선순위 결정 방법 선택 시, RICE vs ICE 등 프레임워크 비교 시, 또는 다양한 우선순위 결정 방식 학습 시 사용하세요."
---

## 우선순위 프레임워크 참고 자료

상황에 맞는 올바른 우선순위 프레임워크를 선택하고 적용하는 데 도움이 되는 참고 자료입니다.

### 핵심 원칙

고객이 솔루션을 설계하도록 허용하지 마세요. 기능이 아닌 **문제(기회)**를 우선순위화하세요.

### Opportunity Score (Dan Olsen, *The Lean Product Playbook*)

고객 문제 우선순위화를 위한 권장 프레임워크입니다.

각 니즈에 대해 **중요도(Importance)**와 **만족도(Satisfaction)**를 고객에게 조사하세요 (0~1 척도로 정규화).

세 가지 관련 공식:
- **현재 가치** = Importance × Satisfaction
- **Opportunity Score** = Importance × (1 − Satisfaction)
- **고객 가치 창출** = Importance × (S2 − S1), 여기서 S1 = 이전 만족도, S2 = 이후 만족도

높은 중요도 + 낮은 만족도 = 높은 Opportunity Score = 최선의 기회. 중요도 대 만족도 차트에 표시하세요—좌상단 사분면이 핵심 영역입니다. 솔루션이 아닌 고객 문제를 우선순위화합니다.

### ICE 프레임워크

이니셔티브와 아이디어 우선순위화에 유용합니다. 가치뿐만 아니라 리스크와 경제적 요소도 고려합니다.

- **I** (Impact) = Opportunity Score × 영향받는 고객 수
- **C** (Confidence) = 얼마나 확신하는가? (1-10). 리스크를 반영.
- **E** (Ease) = 구현이 얼마나 쉬운가? (1-10). 경제적 요소를 반영.

**점수** = I × C × E. 높을수록 먼저 우선순위화.

### RICE 프레임워크

ICE의 Impact를 두 가지 별도 요소로 분리합니다. 더 세분화된 분석이 필요한 대형 팀에 유용합니다.

- **R** (Reach) = 영향받는 고객 수
- **I** (Impact) = Opportunity Score (고객당 가치)
- **C** (Confidence) = 얼마나 확신하는가? (0-100%)
- **E** (Effort) = 구현에 필요한 노력? (person-months)

**점수** = (R × I × C) / E

### 9가지 프레임워크 개요

| 프레임워크 | 가장 적합한 상황 | 핵심 인사이트 |
|-----------|----------|-------------|
| Eisenhower Matrix | 개인 업무 | 긴급 vs 중요 — 개인 PM 업무 관리용 |
| Impact vs Effort | 업무/이니셔티브 | 단순 2×2 — 빠른 분류, 전략적 결정에는 부적합 |
| Risk vs Reward | 이니셔티브 | Impact vs Effort와 유사하지만 불확실성 반영 |
| **Opportunity Score** | 고객 문제 | **권장.** Importance × (1 − Satisfaction). 0~1로 정규화. |
| Kano Model | 기대치 이해 | Must-be, Performance, Attractive, Indifferent, Reverse. 이해용이지 우선순위화용 아님. |
| Weighted Decision Matrix | 다요소 결정 | 기준에 가중치 부여, 각 옵션 점수화. 이해관계자 동의 확보에 유용. |
| **ICE** | 아이디어/이니셔티브 | Impact × Confidence × Ease. 빠른 우선순위화에 권장. |
| **RICE** | 대규모 아이디어 | (Reach × Impact × Confidence) / Effort. ICE에 Reach 추가. |
| MoSCoW | 요구사항 | Must/Should/Could/Won't. 주의: 프로젝트 관리 기반 프레임워크. |

### 템플릿

- [Opportunity Score intro (PDF)](https://drive.google.com/file/d/1ENbYPmk1i1AKO7UnfyTuULL5GucTVufW/view)
- [Importance vs Satisfaction Template — Dan Olsen (Google Slides)](https://docs.google.com/presentation/d/1jg-LuF_3QHsf6f1nE1f98i4C0aulnRNMOO1jftgti8M/edit#slide=id.g796641d975_0_3)
- [ICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1LUfnsPolhZgm7X2oij-7EUe0CJT-Dwr-/edit?usp=share_link&ouid=111307342557889008106&rtpof=true&sd=true)
- [RICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1S-6QpyOz5MCrV7B67LUWdZkAzn38Eahv/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

### 참고 자료

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
