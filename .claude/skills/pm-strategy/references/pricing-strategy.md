---
name: pricing-strategy
description: "가격 모델, 경쟁사 가격 분석, 지불 의사 추정, 가격 탄력성 등 가격 전략을 분석하고 설계합니다. 가격 책정, 가격 모델 평가, 가격 변경 준비, 또는 freemium과 유료 방식 비교 시 사용하세요."
---

## Pricing Strategy

가치 전달, 경쟁적 포지셔닝, 지불 의사를 기반으로 가격 전략을 설계합니다.

### 컨텍스트

**$ARGUMENTS**에 대한 가격 전략을 수립합니다.

사용자가 파일(경쟁사 가격, 설문 데이터, 재무 모델, 사용 데이터)을 제공하면 먼저 읽으세요. 필요한 경우 웹 검색으로 경쟁사 가격을 조사하세요.

### 지시문

1. **전달하는 가치 이해**:
   - 핵심 가치 제안은 무엇인가?
   - 고객의 대안(및 그 비용)은 무엇인가?
   - 제품이 제공하는 정량적 결과는? (절약된 시간, 창출된 매출, 절감된 비용)
   - 해당 가치를 기반으로 고객의 지불 의사는 얼마인가?

2. **가격 모델 평가** — 가장 적합한 모델 추천:

   | 모델 | 적합한 경우 | 예시 |
   |---|---|---|
   | **Flat-rate** | 단순한 제품, 예측 가능한 비용 | Basecamp ($99/mo flat) |
   | **Per-seat** | 협업 툴, 팀 제품 | Slack, Figma |
   | **Usage-based** | 인프라, API 제품 | AWS, Twilio |
   | **Tiered** | 뚜렷한 사용자 세그먼트가 있는 제품 | 대부분의 SaaS (Free/Pro/Enterprise) |
   | **Freemium** | 바이럴/네트워크 효과가 있는 제품 | Spotify, Notion |
   | **Freemium + usage** | 플랫폼 제품 | Vercel, OpenAI API |
   | **Value-based** | 임팩트가 큰 엔터프라이즈 툴 | Salesforce, Palantir |

3. **경쟁사 가격 분석**:
   - 경쟁사의 가격 티어와 포함 항목 정리
   - 자사 제품의 위치 파악 (프리미엄, 중간시장, 저가)
   - 가격 격차 또는 기회 발굴
   - 업계 가격 관행 파악

4. **가격 구조 설계**:
   - **티어**: 명확한 차별화를 갖춘 2~4개 티어 정의
   - **기능 구분**: 어떤 기능을 어느 티어에? (임의적 제한이 아닌 가치 지표 기반)
   - **가치 지표**: 어떤 단위로 청구할 것인가? (사용자 수, 이벤트 수, 저장 용량, API 호출 수)
   - **앵커 가격**: 가장 인기 있는 티어를 명확한 선택지처럼 느껴지도록 설정
   - **연간 할인**: 일반적으로 월간 가격 대비 15~20% 할인

5. **가격 민감도 추정**:
   - Van Westendorp Price Sensitivity Meter (설문 데이터가 있는 경우):
     - 너무 저렴 → 품질 의심
     - 저렴 → 좋은 가치
     - 비쌈 → 망설임 시작
     - 너무 비쌈 → 구매 거부
   - 또는 경쟁사 가격 및 전달되는 가치를 기반으로 추정

6. **가격 실험 계획**:
   - 가격 페이지 A/B 테스트 (다른 가격대, 티어명, 기능 묶음)
   - 지불 의사 확인을 위한 창업자 주도 영업 대화
   - 다양한 가격 앵커로 랜딩 페이지 테스트
   - 가격대별 전환율 코호트 분석

7. **가격 추천안 출력**:
   ```
   Recommended Model: [모델 유형]
   Value Metric: [청구 기준]

   | Tier | Price | Target Segment | Key Features | Positioning |
   |---|---|---|---|---|

   Key Assumptions:
   - [가정] → [검증 방법]

   Risks:
   - [리스크] → [완화 방법]
   ```

단계적으로 생각하세요. 마크다운으로 저장하세요. 런칭 전 검증이 필요한 가정은 별도로 표시하세요.

---

### Further Reading

- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
- [The AI Product Pricing Masterclass: OpenAI Product Lead on Why SaaS Pricing Fails in AI (and How to Fix It)](https://www.productcompass.pm/p/ai-product-pricing) (video course)
