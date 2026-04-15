# 학습 지식 인덱스

> 이 디렉토리는 대화 중 사용자 피드백으로부터 자동 학습된 지식을 저장합니다.
> `feedback-learning.md` 규칙에 의해 자동 관리됩니다.

## 도메인별 학습 현황

| 도메인 | 파일 | 정보 보정 | 실무 노하우 | 주의사항 | 거부 기록 | 합계 | last_cleaned |
|--------|------|-----------|-------------|----------|----------|------|-------------|
| Business Dev | `business-dev.md` | 0 | 0 | 0 | 0 | 0 | — |
| Compliance | `compliance.md` | 0 | 0 | 0 | 0 | 0 | — |
| Data | `data.md` | 0 | 0 | 0 | 0 | 0 | — |
| Design | `design.md` | 0 | 0 | 0 | 0 | 0 | — |
| Development | `development.md` | 0 | 0 | 0 | 0 | 0 | — |
| Finance | `finance.md` | 0 | 0 | 0 | 0 | 0 | — |
| HR | `hr.md` | 0 | 0 | 0 | 0 | 0 | — |
| Legal | `legal.md` | 0 | 0 | 0 | 0 | 0 | — |
| Marketing | `marketing.md` | 0 | 0 | 0 | 0 | 0 | — |
| PR | `pr.md` | 0 | 0 | 0 | 0 | 0 | — |
| Product | `product.md` | 0 | 0 | 0 | 0 | 0 | — |
| Productivity | `productivity.md` | 0 | 0 | 0 | 0 | 0 | — |
| Research | `research.md` | 0 | 0 | 0 | 0 | 0 | — |
| Sales | `sales.md` | 1 | 0 | 0 | 0 | 1 | 2026-04-15 |
| Security | `security.md` | 0 | 0 | 0 | 0 | 0 | — |
| Writing | `writing.md` | 1 | 5 | 3 | 0 | 9 | 2026-04-15 ✓반영 |
| **합계** | | **1** | **5** | **3** | **0** | **9** | |

## 도메인 공통

| 파일 | 항목 수 |
|------|---------|
| `preferences.md` | 8 |

## 관리 방법

- **자동 추가**: 대화 중 사용자 보정 감지 시 `feedback-learning.md` 규칙에 의해 자동 반영
- **자동 정리 (autoDream)**: 세션 종료 시 `entropy-cleanup.md` 3.5단계에서 자동 실행 — 중복 병합, 모순 해소, 90일+ staleness 정리, 시간 표현 정규화. 실행 후 해당 도메인의 `last_cleaned`를 당일로 갱신
- **수동 리뷰**: `/improve` 커맨드로 누적된 학습 지식 리뷰 및 SKILL.md 반영
- **카운트 갱신**: 항목 추가/삭제 시 이 파일의 카운트 테이블도 함께 업데이트
- **Skeptical Retrieval**: knowledge 항목은 힌트이지 진실이 아님. 90일+ 경과 항목은 현재 상태와 대조 검증 후 사용 (`expert-routing.md` 6단계 참조)
- **✓반영 마커**: `last_cleaned` 컬럼의 "✓반영"은 해당 도메인의 knowledge가 이미 agent/SKILL 레이어에 직접 배선되어 별도 SKILL.md 복사가 불필요함을 뜻함 (예: `writing.md`는 `agents/writing.md`가 직접 참조)

## 파일 자동 생성

도메인 파일(business-dev.md, compliance.md 등)은 첫 학습이 감지될 때 자동으로 생성됩니다. 초기에는 이 인덱스에 0으로 표시되며, 사용자 피드백이 누적되면 해당 파일이 자동 생성되고 카운트가 업데이트됩니다.
