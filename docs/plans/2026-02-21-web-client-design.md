# Business AI Team — 웹 클라이언트 설계 문서

**날짜:** 2026-02-21
**상태:** 승인됨
**작성자:** 브레인스토밍 세션

---

## 1. 프로젝트 개요

business-ai-team CLI를 일반 사용자도 사용할 수 있도록 대화형 웹 클라이언트를 구축한다.
별도 서버 비용 없이 완전 무료로 운영 가능한 구조를 목표로 한다.

### 핵심 목표
- 누구나 자신의 Anthropic API 키로 16개 전문가 AI 팀을 사용할 수 있게
- 초심자도 쉽게 API 키를 발급받고 연결할 수 있도록 상세한 온보딩 제공
- ChatGPT/Claude 수준의 자연스러운 대화 인터페이스

---

## 2. 아키텍처

### 선택: A안 — Vercel 올인원

```
┌─────────────────────────────────────────────────────┐
│                    Vercel (단일 배포)                  │
│                                                      │
│  ┌──────────────┐     ┌──────────────────────────┐  │
│  │   Next.js    │     │    Next.js API Routes     │  │
│  │   Frontend   │────▶│                          │  │
│  │              │     │  POST /api/chat           │  │
│  │  - 채팅 UI   │     │  POST /api/validate-key   │  │
│  │  - 히스토리  │     │                          │  │
│  │  - API키 입력│     └──────────┬───────────────┘  │
│  │              │                │                  │
│  │  localStorage│                ▼                  │
│  │  - API 키    │     ┌──────────────────────┐      │
│  │  - 대화 목록 │     │    Anthropic API      │      │
│  │  - 메시지    │     │   (사용자 API 키로)   │      │
│  └──────────────┘     └──────────────────────┘      │
└─────────────────────────────────────────────────────┘
```

### 핵심 원칙
- **서버 Stateless**: API 키는 DB에 저장하지 않음. 요청마다 헤더로 전달
- **외부 의존성 0**: Supabase 등 추가 서비스 없음
- **완전 무료**: Vercel 무료 플랜으로 운영

---

## 3. 인증 방식

**API 키 = 신원**

- 별도 회원가입/로그인 없음
- 사용자가 Anthropic API 키 입력 → localStorage 저장
- 키 해시(SHA-256)를 유저 식별자로 사용 (서버 로그용, 저장 안 함)
- 첫 방문 시 온보딩 모달 자동 표시

---

## 4. 데이터 모델 (localStorage)

```typescript
// "biz_api_key" — Anthropic API 키
type StoredApiKey = string

// "biz_conversations" — 대화 목록
type ConversationStore = {
  conversations: Conversation[]
}

type Conversation = {
  id: string        // uuid
  title: string     // 첫 메시지 앞 30자 자동 생성
  createdAt: string
  updatedAt: string
  messages: Message[]
}

type Message = {
  id: string
  role: "user" | "assistant"
  content: string
  attachments?: Attachment[]
  agentsUsed?: string[]   // 사용된 에이전트 목록
  createdAt: string
}

type Attachment = {
  name: string
  type: string    // MIME type
  data: string    // base64
  size: number
}
```

---

## 5. API Routes

```
POST /api/chat
  Header: X-API-Key: sk-ant-...
  Body:   { message, history, attachments? }
  Response: SSE stream
    event: "agent"  → data: "marketing_agent"
    event: "delta"  → data: "텍스트 조각..."
    event: "done"   → data: "[DONE]"

POST /api/validate-key
  Body:   { apiKey }
  Response: { valid: boolean, error?: string }
```

---

## 6. 에이전트 라우팅 (2-step)

```
1단계: 오케스트레이터 (tool_use)
  → 메시지 분석 → 적절한 에이전트 선택

2단계: 선택된 에이전트 (streaming)
  → 해당 시스템 프롬프트 + 사용자 메시지 → 스트리밍 응답
```

### 16개 에이전트
| 키 | 이름 |
|----|------|
| marketing | 마케팅 전문가 |
| research | 리서치 전문가 |
| writing | 작문 전문가 |
| hr | HR 전문가 |
| finance | 재무 전문가 |
| legal | 법무 전문가 |
| sales | 영업 전문가 |
| data | 데이터 분석가 |
| product | 프로덕트 매니저 |
| development | 개발 전문가 |
| design | 디자인 전문가 |
| productivity | 생산성 전문가 |
| pr | PR 전문가 |
| security | 보안 전문가 |
| compliance | 컴플라이언스 |
| business_dev | 사업개발 전문가 |

---

## 7. UI 레이아웃

```
┌──────────────┬─────────────────────────────────────┐
│   사이드바   │           메인 채팅 영역              │
│  (260px)     │                                      │
│              │  ┌──────────────────────────────┐   │
│  [+ 새 대화] │  │         메시지 목록           │   │
│  ─────────── │  │                              │   │
│  오늘        │  │  [user] 마케팅 전략 짜줘      │   │
│  > 마케팅... │  │  [ai]   마케팅 전문가 분석... │   │
│  > 경쟁사... │  │         ↳ 사용된 에이전트:   │   │
│  ─────────── │  │           marketing          │   │
│  어제        │  │                              │   │
│  > HR 정책.. │  └──────────────────────────────┘   │
│              │                                      │
│  ─────────── │  ┌──────────────────────────────┐   │
│  [⚙ API 키] │  │  📎  메시지 입력창      [전송]│   │
└──────────────┴──┴──────────────────────────────┴───┘
```

---

## 8. 온보딩 — API 키 입력 화면 (초심자 대상)

초심자 사용자가 막힘 없이 API 키를 발급받고 연결할 수 있도록 단계별 가이드를 제공한다.

### 온보딩 흐름

```
[첫 방문]
    │
    ▼
환영 모달: "시작하기"
    │
    ▼
Step 1: 서비스 소개 (스킵 가능)
  - "이 서비스는 무엇인가요?" 한 줄 설명
  - AI 팀원 카드 미리보기 (마케터, 리서처 등)
    │
    ▼
Step 2: API 키 발급 안내 (핵심)
  - "Anthropic API 키가 필요합니다" 설명
  - 비용 안내: "첫 사용 시 $5 무료 크레딧 제공"
  - [console.anthropic.com 바로가기] 버튼
  - 스크린샷 포함 4단계 발급 가이드:
      1. console.anthropic.com 접속 → 회원가입
      2. 좌측 메뉴 "API Keys" 클릭
      3. "+ Create Key" 버튼 클릭
      4. 생성된 키 복사 (sk-ant-... 형태)
    │
    ▼
Step 3: API 키 입력
  - 입력창 + "붙여넣기" 버튼
  - 실시간 형식 검사 (sk-ant-로 시작하는지)
  - [연결 확인] 버튼 → 실제 API 호출로 유효성 검증
  - 성공: "연결됐습니다! 이제 AI 팀을 사용할 수 있습니다."
  - 실패: 구체적 오류 메시지 + 해결 방법 안내
    │
    ▼
Step 4: 첫 대화 시작
  - 예시 질문 3개 제안 버튼:
      - "우리 서비스 마케팅 전략을 세워줘"
      - "경쟁사 분석을 해줘"
      - "팀원에게 보낼 이메일을 작성해줘"
```

### API 키 보안 안내 문구
> "입력한 API 키는 이 브라우저에만 저장되며, 서버에는 전달되지 않습니다.
> 브라우저를 초기화하면 다시 입력해야 합니다."

### 설정 페이지 (재진입 시)
- 사이드바 하단 "API 키 설정" 클릭
- 현재 키 마스킹 표시 (sk-ant-...xxxx)
- [키 변경] / [삭제] 버튼

---

## 9. 디자인 시스템

| 항목 | 결정 |
|------|------|
| **스타일** | Dark Mode (OLED) |
| **Primary** | `#6366F1` Indigo |
| **Accent** | `#10B981` Emerald |
| **Background** | `#09090B` zinc-950 |
| **Surface** | `#18181B` zinc-900 |
| **폰트** | Poppins (헤딩) + Inter (본문) |
| **컴포넌트** | shadcn/ui |
| **아이콘** | Lucide React |
| **마크다운** | react-markdown + rehype-highlight |
| **스트리밍** | Server-Sent Events (SSE) |

---

## 10. 기술 스택

| 영역 | 선택 |
|------|------|
| 프레임워크 | Next.js 15 (App Router) |
| 언어 | TypeScript |
| 스타일 | Tailwind CSS v4 |
| UI 컴포넌트 | shadcn/ui |
| AI SDK | Anthropic SDK (TypeScript) |
| 호스팅 | Vercel (무료) |
| 저장소 | localStorage |

---

## 11. 제약 및 트레이드오프

| 항목 | 내용 |
|------|------|
| 디바이스 동기화 | 없음 (의도적) |
| 데이터 영속성 | 브라우저 삭제 시 소실 |
| 파일 저장 | base64 인코딩, 메시지에 포함 |
| Vercel 함수 제한 | 실행 시간 최대 60초 (Pro 없이) |
| 비용 | 완전 무료 |
