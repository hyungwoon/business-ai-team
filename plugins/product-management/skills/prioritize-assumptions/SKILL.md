---
name: prioritize-assumptions
description: "Impact × Risk 매트릭스를 활용해 가정을 우선순위화하고 각 가정에 대한 실험을 제안합니다. 가정 목록을 분류하거나, 무엇을 먼저 테스트할지 결정하거나, 가정 우선순위화 캔버스를 적용할 때 활용하세요."
---

## 가정 우선순위화

Impact × Risk 매트릭스를 활용해 가정을 분류하고 적합한 실험을 제안합니다.

### 컨텍스트

**$ARGUMENTS**의 가정 우선순위화를 지원합니다.

사용자가 가정이나 리서치 데이터가 담긴 파일을 제공하면 먼저 읽으세요.

### 도메인 컨텍스트

**ICE**는 가정 우선순위화에 적합합니다: Impact (Opportunity Score × # Customers) × Confidence (1–10) × Ease (1–10). Opportunity Score = Importance × (1 − Satisfaction), 0–1로 정규화 (Dan Olsen). **RICE**는 Impact를 Reach × Impact로 분리합니다: (R × I × C) / E. 전체 공식과 템플릿은 `prioritization-frameworks` 스킬을 참고하세요.

### 지시문

사용자가 우선순위화할 가정 목록을 제공합니다. 다음 프레임워크를 적용하세요:

1. **각 가정에 대해** 두 가지 차원을 평가합니다:
   - **Impact(영향도)**: 이 가정을 검증함으로써 창출되는 가치 × 영향받는 고객 수 (ICE에서: Impact = Opportunity Score × # Customers)
   - **Risk(리스크)**: (1 - Confidence) × Effort

2. **Impact × Risk 매트릭스에 따라 각 가정을 분류**합니다:
   - **Low Impact, Low Risk** → 우선순위가 높은 가정이 해결될 때까지 테스트 보류
   - **High Impact, Low Risk** → 구현 진행 (낮은 리스크, 높은 보상)
   - **Low Impact, High Risk** → 아이디어 기각 (투자 가치 없음)
   - **High Impact, High Risk** → 검증을 위한 실험 설계

3. **테스트가 필요한 각 가정에 대해** 다음 조건을 충족하는 실험을 제안합니다:
   - 최소한의 노력으로 검증된 학습을 극대화
   - 의견이 아닌 실제 행동을 측정
   - 명확한 성공 지표와 임계값 포함

4. **결과를 우선순위화된 매트릭스 또는 테이블 형태로 제시**합니다.

단계적으로 생각하세요. 산출물이 방대한 경우 마크다운으로 저장하세요.

---

### 추가 자료

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
