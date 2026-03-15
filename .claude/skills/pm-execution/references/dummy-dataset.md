---
name: dummy-dataset
description: "사용자 정의 컬럼, 제약 조건, 출력 형식(CSV, JSON, SQL, Python script)으로 테스트용 현실적인 더미 데이터셋을 생성합니다. 테스트 데이터 생성, 목(mock) 데이터셋 구성, 개발 및 데모용 샘플 데이터 생성 시 사용하세요."
---
# 더미 데이터셋 생성

사용자 정의 컬럼, 제약 조건, 출력 형식(CSV, JSON, SQL, Python script)으로 테스트용 현실적인 더미 데이터셋을 생성합니다. 즉시 사용 가능한 실행 가능 스크립트 또는 직접적인 데이터 파일을 생성합니다.

**사용 시기:** 테스트 데이터 생성, 샘플 데이터셋 생성, 개발용 현실적인 목 데이터 구성, 또는 테스트 환경 채우기 시.

**Arguments:**
- `$PRODUCT`: 제품 또는 시스템 이름
- `$DATASET_TYPE`: 데이터 유형 (예: 고객 피드백, 거래 내역, 사용자 프로필)
- `$ROWS`: 생성할 행 수 (기본값: 100)
- `$COLUMNS`: 포함할 특정 컬럼 또는 필드
- `$FORMAT`: 출력 형식 (CSV, JSON, SQL, Python script)
- `$CONSTRAINTS`: 추가 제약 조건 또는 비즈니스 규칙

## 단계별 프로세스

1. **데이터셋 유형 파악** - 데이터 도메인 이해
2. **컬럼 명세 정의** - 이름, 데이터 타입, 값 범위
3. **행 수 결정** - 필요한 샘플 레코드 수
4. **출력 형식 선택** - CSV, JSON, SQL INSERT, 또는 Python script
5. **현실적인 패턴 적용** - 데이터가 실제처럼 유효하게 보이도록
6. **비즈니스 제약 조건 적용** - 비즈니스 로직 및 관계 준수
7. **데이터 생성 또는 스크립팅** - 실행 가능한 출력 생성
8. **출력 검증** - 데이터 품질 및 완전성 확인

## 템플릿: Python Script 출력

```python
import csv
import json
from datetime import datetime, timedelta
import random

# Configuration
ROWS = $ROWS
FILENAME = "$DATASET_TYPE.csv"

# Column definitions with realistic value generators
columns = {
    "id": "auto-increment",
    "name": "first_last_name",
    "email": "email",
    "created_at": "timestamp",
    # Add more columns...
}

def generate_dataset():
    """Generate realistic dummy dataset"""
    data = []
    for i in range(1, ROWS + 1):
        record = {
            "id": f"U{i:06d}",
            # Generate values based on column definitions
        }
        data.append(record)
    return data

def save_as_csv(data, filename):
    """Save dataset as CSV"""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    dataset = generate_dataset()
    save_as_csv(dataset, FILENAME)
    print(f"Generated {len(dataset)} records in {FILENAME}")
```

## 데이터셋 명세 예시

**데이터셋 유형:** 고객 피드백

**컬럼:**
- feedback_id (자동 증가, U001, U002...)
- customer_name (현실적인 이름)
- email (유효한 이메일 형식)
- feedback_date (최근 90일 내 날짜)
- rating (별 1~5개)
- category (Bug, Feature Request, Complaint, Praise)
- text (현실적인 피드백 내용)
- product (전자기기, 의류, 홈)

**제약 조건:**
- 평점 분포: 5점 40%, 4점 30%, 3점 20%, 1~2점 10%
- Bug 카테고리는 평점 1~3만 허용
- Feature Request는 평점 3~5만 허용
- 이메일 도메인은 현실적으로 (gmail, yahoo, company.com)

## 산출물

- 즉시 실행 가능한 Python script 또는 직접 데이터 파일
- 적절한 헤더와 형식의 CSV 파일
- 유효한 구조와 타입의 JSON 파일
- 데이터베이스 입력용 SQL INSERT 문
- 데이터 검증 및 제약 조건 준수
- 현실적이고 비즈니스에 적합한 값
- 데이터 생성 로직 문서화
- 데이터셋 사용을 위한 빠른 시작 가이드

## 출력 형식

**CSV:** 평면 테이블 형식, 스프레드시트와 데이터베이스로 쉽게 가져오기 가능

**JSON:** 중첩 구조, API 및 NoSQL 데이터베이스에 적합

**SQL:** INSERT 문, 관계형 데이터베이스에서 직접 실행 가능

**Python Script:** 사용자 정의 또는 대용량 데이터셋을 위한 실행 가능 생성기
