---
name: prioritize-features
description: "영향도, 노력, 리스크, 전략적 정합성을 기준으로 기능 아이디어 백로그를 우선순위화하고 상위 5개를 추천합니다. 기능 백로그 우선순위 결정, 범위 조정, 제품 아이디어 순위 산정 시 활용하세요."
---

## 기능 백로그 우선순위화

기능 아이디어 백로그를 평가하고 순위를 매겨 추진할 상위 5개를 선정합니다.

### 컨텍스트

**$ARGUMENTS**의 기능 우선순위화를 지원합니다.

사용자가 파일(스프레드시트, 백로그, 기회 평가서 등)을 제공하면 직접 읽고 분석하세요.

### 도메인 컨텍스트

프레임워크 선택 가이드는 `prioritization-frameworks` 스킬을 참고하세요. 핵심 권장 사항:

**Opportunity Score** (Dan Olsen, *The Lean Product Playbook*)는 고객 문제 평가에 권장됩니다: Opportunity Score = Importance × (1 − Satisfaction), 0–1로 정규화. Importance 높고 Satisfaction 낮을수록 최고의 기회. **문제(기회)**를 우선순위화하세요, 솔루션이 아니라.

**ICE**는 이니셔티브의 빠른 점수 산정에 권장됩니다: Impact (Opportunity Score × # Customers) × Confidence × Ease. **RICE**는 대형 팀을 위해 Reach를 별도 요소로 추가합니다.

### 지시문

사용자가 제품 목표, 원하는 결과, 기능 아이디어를 설명합니다. 다음 단계를 순서대로 수행하세요:

1. **우선순위 파악**: 제품 목표와 성공 지표를 확인합니다.

2. **각 기능을 다음 기준으로 평가**합니다:
   - **Impact(영향도)**: 원하는 결과에 얼마나 기여하는가? 고객 데이터가 있다면 Opportunity Score를 고려하세요.
   - **Effort(노력)**: 개발, 디자인, 조율에 얼마나 리소스가 필요한가?
   - **Risk(리스크)**: 불확실성이 얼마나 존재하는가? 검증이 필요한 가정은 무엇인가?
   - **전략적 정합성**: 제품 비전 및 현재 목표와 얼마나 잘 맞는가?

3. **상위 5개 기능을 추천**합니다:
   - 명확한 순위(1–5위)
   - 각 선정에 대한 간략한 근거
   - 고려된 주요 트레이드오프
   - 우선순위에서 제외된 항목과 그 이유

4. **우선순위 테이블 형태로 제시**합니다(유용한 경우).

단계적으로 생각하세요. 산출물이 방대한 경우 마크다운으로 저장하세요.

---

### 추가 자료

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
