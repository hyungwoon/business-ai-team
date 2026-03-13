---
name: user-stories
description: "3 C's(Card, Conversation, Confirmation)와 INVEST 기준을 따르는 유저 스토리를 설명, 디자인 링크, 인수 기준과 함께 작성합니다. 유저 스토리 작성, 기능을 백로그 항목으로 분해, 또는 인수 기준 정의 시 사용하세요."
---
# User Stories

3 C's(Card, Conversation, Confirmation)와 INVEST 기준을 따르는 유저 스토리를 작성합니다. 설명, 디자인 링크, 인수 기준이 포함된 스토리를 생성합니다.

**사용 시기:** 유저 스토리 작성, 기능을 스토리로 분해, 백로그 항목 생성, 또는 인수 기준 정의 시.

**Arguments:**
- `$PRODUCT`: 제품 또는 시스템 이름
- `$FEATURE`: 스토리로 분해할 신규 기능
- `$DESIGN`: 디자인 파일 링크 (Figma, Miro 등)
- `$ASSUMPTIONS`: 핵심 가정 또는 맥락

## 단계별 프로세스

1. **제공된 디자인과 맥락을 바탕으로 기능 분석**
2. **사용자 역할 및 고유한 사용자 여정 파악**
3. **3 C's 프레임워크 적용:**
   - Card: 간단한 제목과 한 줄 요약
   - Conversation: 의도에 대한 상세 논의
   - Confirmation: 명확한 인수 기준
4. **INVEST 기준 준수:** Independent(독립적), Negotiable(협상 가능), Valuable(가치 있음), Estimable(추정 가능), Small(작음), Testable(테스트 가능)
5. **초등학생도 이해할 수 있는 평이한 언어 사용**
6. **시각적 참고를 위한 디자인 파일 링크 연결**
7. **구조화된 형식으로 유저 스토리 출력**

## 스토리 템플릿

**제목:** [기능명]

**설명:** As a [사용자 역할], I want to [액션], so that [혜택].

**디자인:** [디자인 파일 링크]

**인수 기준:**
1. [명확하고 테스트 가능한 기준]
2. [관찰 가능한 동작]
3. [시스템이 올바르게 검증함]
4. [엣지 케이스 처리]
5. [성능 또는 접근성 고려 사항]
6. [연동 지점]

## 유저 스토리 예시

**제목:** 최근 본 상품 섹션

**설명:** As an Online Shopper, I want to see a 'Recently viewed' section on the product page to easily revisit items I considered.

**디자인:** [Figma 링크]

**인수 기준:**
1. 이전에 최소 1개 이상의 상품을 조회한 모든 사용자에 대해 상품 페이지 하단에 '최근 본 상품' 섹션이 표시된다.
2. 세션에서 처음 방문하는 상품 페이지에서는 표시되지 않는다.
3. 현재 보고 있는 상품은 목록에서 제외된다.
4. 섹션에는 이미지, 제목, 가격이 포함된 상품 카드 또는 썸네일이 표시된다.
5. 각 상품 카드에는 조회 시점이 표시된다 (예: '5분 전에 봤습니다').
6. 상품 카드를 클릭하면 해당 상품 페이지로 이동한다.

## 산출물

- 기능에 대한 완전한 유저 스토리 세트
- 각 스토리에는 제목, 설명, 디자인 링크, 4~6개의 인수 기준 포함
- 스토리는 독립적으로 개발 가능
- 스토리는 한 스프린트 내에 완료할 수 있는 크기로 조정됨
- 관련 디자인 문서 참조 포함

---

### 참고 자료

- [How to Write User Stories: The Ultimate Guide](https://www.productcompass.pm/p/how-to-write-user-stories)
