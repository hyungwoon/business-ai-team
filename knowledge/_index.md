# 학습 지식 인덱스

> 이 디렉토리는 대화 중 사용자 피드백으로부터 자동 학습된 지식을 저장합니다.
> `feedback-learning.md` 규칙에 의해 자동 관리됩니다.

## 도메인별 학습 현황

| 도메인 | 파일 | 정보 보정 | 실무 노하우 | 주의사항 | 거부 기록 | 합계 |
|--------|------|-----------|-------------|----------|----------|------|
| Business Dev | `business-dev.md` | 0 | 0 | 0 | 0 | 0 |
| Compliance | `compliance.md` | 0 | 0 | 0 | 0 | 0 |
| Data | `data.md` | 0 | 0 | 0 | 0 | 0 |
| Design | `design.md` | 0 | 0 | 0 | 0 | 0 |
| Development | `development.md` | 0 | 0 | 0 | 0 | 0 |
| Finance | `finance.md` | 0 | 0 | 0 | 0 | 0 |
| HR | `hr.md` | 0 | 0 | 0 | 0 | 0 |
| Legal | `legal.md` | 0 | 0 | 0 | 0 | 0 |
| Marketing | `marketing.md` | 0 | 0 | 0 | 0 | 0 |
| PR | `pr.md` | 0 | 0 | 0 | 0 | 0 |
| Product | `product.md` | 0 | 0 | 0 | 0 | 0 |
| Productivity | `productivity.md` | 0 | 0 | 0 | 0 | 0 |
| Research | `research.md` | 0 | 0 | 0 | 0 | 0 |
| Sales | `sales.md` | 1 | 0 | 0 | 0 | 1 |
| Security | `security.md` | 0 | 0 | 0 | 0 | 0 |
| Writing | `writing.md` | 1 | 5 | 3 | 0 | 9 |
| **합계** | | **1** | **5** | **3** | **0** | **9** |

## 도메인 공통

| 파일 | 항목 수 |
|------|---------|
| `preferences.md` | 8 |

## 관리 방법

- **자동 추가**: 대화 중 사용자 보정 감지 시 `feedback-learning.md` 규칙에 의해 자동 반영
- **수동 리뷰**: `/improve` 커맨드로 누적된 학습 지식 리뷰 및 SKILL.md 반영
- **카운트 갱신**: 항목 추가/삭제 시 이 파일의 카운트 테이블도 함께 업데이트

## 파일 자동 생성

도메인 파일(business-dev.md, compliance.md 등)은 첫 학습이 감지될 때 자동으로 생성됩니다. 초기에는 이 인덱스에 0으로 표시되며, 사용자 피드백이 누적되면 해당 파일이 자동 생성되고 카운트가 업데이트됩니다.
