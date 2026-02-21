# Business AI Team Web Client — 구현 계획

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** business-ai-team의 16개 전문가 AI를 누구나 브라우저에서 사용할 수 있는 대화형 웹 클라이언트 구축

**Architecture:** Next.js 15 App Router + Vercel 단일 배포. 서버는 stateless — API 키를 받아 Anthropic API를 호출하고 SSE로 스트리밍 응답을 반환. 대화 히스토리는 localStorage에만 저장.

**Tech Stack:** Next.js 15, TypeScript, Tailwind CSS v4, shadcn/ui, Anthropic TypeScript SDK, Vercel

---

## 프로젝트 구조 (최종 목표)

```
business-ai-web/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── globals.css
│   └── api/
│       ├── chat/route.ts
│       └── validate-key/route.ts
├── components/
│   ├── onboarding/
│   │   ├── OnboardingModal.tsx   # 4-step 온보딩 컨테이너
│   │   ├── StepIntro.tsx         # Step 1: 서비스 소개
│   │   ├── StepApiGuide.tsx      # Step 2: API 키 발급 가이드
│   │   ├── StepApiInput.tsx      # Step 3: API 키 입력 + 검증
│   │   └── StepFirstChat.tsx     # Step 4: 예시 질문 제안
│   ├── sidebar/
│   │   ├── AppSidebar.tsx
│   │   ├── ConversationList.tsx
│   │   └── ApiKeyButton.tsx
│   └── chat/
│       ├── ChatArea.tsx
│       ├── MessageList.tsx
│       ├── MessageItem.tsx
│       ├── AgentBadge.tsx
│       └── InputBar.tsx
├── lib/
│   ├── types.ts
│   ├── agents/
│   │   ├── definitions.ts        # 16개 에이전트 시스템 프롬프트
│   │   └── orchestrator.ts       # 오케스트레이터 + 라우팅 로직
│   └── storage/
│       └── conversations.ts      # localStorage 헬퍼
└── public/
    └── guide/                    # API 키 발급 가이드 이미지
```

---

## Task 1: 새 Next.js 프로젝트 생성

**Files:**
- Create: `business-ai-web/` (현재 디렉터리 기준 상위 또는 원하는 위치에 생성)

**Step 1: Next.js 프로젝트 생성**

```bash
npx create-next-app@latest business-ai-web \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir=false \
  --import-alias="@/*"
cd business-ai-web
```

**Step 2: 핵심 패키지 설치**

```bash
npm install @anthropic-ai/sdk
npm install react-markdown rehype-highlight highlight.js
npm install lucide-react
npm install uuid
npm install @types/uuid -D
```

**Step 3: shadcn/ui 초기화**

```bash
npx shadcn@latest init
# 프롬프트 응답:
# Style: Default
# Base color: Zinc
# CSS variables: Yes
```

**Step 4: 필요한 shadcn 컴포넌트 설치**

```bash
npx shadcn@latest add sidebar button input textarea dialog badge scroll-area separator tooltip
```

**Step 5: Vercel 함수 타임아웃 설정**

`vercel.json` 파일 생성:

```json
{
  "functions": {
    "app/api/**/*.ts": {
      "maxDuration": 60
    }
  }
}
```

**Step 6: git 초기화 및 첫 커밋**

```bash
git init
git add .
git commit -m "feat: Next.js 15 프로젝트 초기화 (Tailwind + shadcn/ui)"
```

---

## Task 2: TypeScript 타입 정의

**Files:**
- Create: `lib/types.ts`

**Step 1: 타입 파일 작성**

```typescript
// lib/types.ts

export type AgentKey =
  | 'marketing' | 'research' | 'writing' | 'hr'
  | 'finance' | 'legal' | 'sales' | 'data'
  | 'product' | 'development' | 'design' | 'productivity'
  | 'pr' | 'security' | 'compliance' | 'business_dev'

export interface AgentDefinition {
  key: AgentKey
  name: string
  description: string
  systemPrompt: string
}

export interface Attachment {
  name: string
  type: string   // MIME type (image/png, application/pdf 등)
  data: string   // base64
  size: number
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  attachments?: Attachment[]
  agentsUsed?: AgentKey[]
  createdAt: string
}

export interface Conversation {
  id: string
  title: string
  createdAt: string
  updatedAt: string
  messages: Message[]
}

export interface ConversationStore {
  conversations: Conversation[]
}

// API 요청/응답 타입
export interface ChatRequest {
  message: string
  history: Array<{ role: 'user' | 'assistant'; content: string }>
  attachments?: Attachment[]
}

export interface ValidateKeyRequest {
  apiKey: string
}

export interface ValidateKeyResponse {
  valid: boolean
  error?: string
}
```

**Step 2: 커밋**

```bash
git add lib/types.ts
git commit -m "feat: TypeScript 타입 정의"
```

---

## Task 3: localStorage 유틸리티

**Files:**
- Create: `lib/storage/conversations.ts`

**Step 1: localStorage 헬퍼 작성**

```typescript
// lib/storage/conversations.ts
import { v4 as uuidv4 } from 'uuid'
import type { Conversation, Message, ConversationStore } from '@/lib/types'

const STORAGE_KEY = 'biz_conversations'
const API_KEY_STORAGE = 'biz_api_key'

// API 키 관련
export function getApiKey(): string | null {
  if (typeof window === 'undefined') return null
  return localStorage.getItem(API_KEY_STORAGE)
}

export function setApiKey(key: string): void {
  localStorage.setItem(API_KEY_STORAGE, key)
}

export function removeApiKey(): void {
  localStorage.removeItem(API_KEY_STORAGE)
}

// 대화 목록 관련
function loadStore(): ConversationStore {
  if (typeof window === 'undefined') return { conversations: [] }
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : { conversations: [] }
  } catch {
    return { conversations: [] }
  }
}

function saveStore(store: ConversationStore): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(store))
}

export function getAllConversations(): Conversation[] {
  return loadStore().conversations.sort(
    (a, b) => new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime()
  )
}

export function getConversation(id: string): Conversation | null {
  return loadStore().conversations.find(c => c.id === id) ?? null
}

export function createConversation(): Conversation {
  const now = new Date().toISOString()
  const conversation: Conversation = {
    id: uuidv4(),
    title: '새 대화',
    createdAt: now,
    updatedAt: now,
    messages: [],
  }
  const store = loadStore()
  store.conversations.unshift(conversation)
  saveStore(store)
  return conversation
}

export function addMessage(conversationId: string, message: Omit<Message, 'id' | 'createdAt'>): Message {
  const store = loadStore()
  const idx = store.conversations.findIndex(c => c.id === conversationId)
  if (idx === -1) throw new Error('Conversation not found')

  const newMessage: Message = {
    ...message,
    id: uuidv4(),
    createdAt: new Date().toISOString(),
  }

  store.conversations[idx].messages.push(newMessage)
  store.conversations[idx].updatedAt = newMessage.createdAt

  // 첫 사용자 메시지로 제목 자동 생성
  if (message.role === 'user' && store.conversations[idx].title === '새 대화') {
    store.conversations[idx].title = message.content.slice(0, 30)
  }

  saveStore(store)
  return newMessage
}

export function updateLastAssistantMessage(
  conversationId: string,
  content: string,
  agentsUsed: string[]
): void {
  const store = loadStore()
  const conv = store.conversations.find(c => c.id === conversationId)
  if (!conv) return

  const lastMsg = [...conv.messages].reverse().find(m => m.role === 'assistant')
  if (lastMsg) {
    lastMsg.content = content
    lastMsg.agentsUsed = agentsUsed as any
  }
  saveStore(store)
}

export function deleteConversation(id: string): void {
  const store = loadStore()
  store.conversations = store.conversations.filter(c => c.id !== id)
  saveStore(store)
}

export function clearAllConversations(): void {
  saveStore({ conversations: [] })
}
```

**Step 2: 커밋**

```bash
git add lib/storage/conversations.ts
git commit -m "feat: localStorage 대화 히스토리 유틸리티"
```

---

## Task 4: 에이전트 정의 (16개)

**Files:**
- Create: `lib/agents/definitions.ts`

**Step 1: 에이전트 정의 파일 작성**

Python `agents/` 폴더의 각 에이전트 시스템 프롬프트를 참고해 TypeScript로 옮긴다.
(Python 파일: `/agents/marketing_agent.py` 등의 `base_prompt` 문자열)

```typescript
// lib/agents/definitions.ts
import type { AgentDefinition, AgentKey } from '@/lib/types'

export const AGENT_DEFINITIONS: Record<AgentKey, AgentDefinition> = {
  marketing: {
    key: 'marketing',
    name: '마케팅 전문가',
    description: '마케팅 콘텐츠, 캠페인 기획, 브랜드 전략',
    systemPrompt: `당신은 마케팅 전문가입니다.
효과적인 마케팅 전략과 콘텐츠를 통해 비즈니스 성장을 지원합니다.

전문 분야:
- 마케팅 콘텐츠 제작
- 캠페인 기획 및 실행
- 브랜드 전략 및 포지셔닝
- 마케팅 성과 분석
- 디지털 마케팅 및 SNS

원칙: 타겟 고객 중심 접근, 데이터 기반 의사결정, 일관된 브랜드 메시지, ROI 중심 전략`,
  },
  research: {
    key: 'research',
    name: '리서치 전문가',
    description: '시장 조사, 경쟁사 분석, 트렌드 리서치',
    systemPrompt: `당신은 리서치 전문가입니다.
깊이 있는 분석과 인사이트로 비즈니스 의사결정을 지원합니다.

전문 분야:
- 시장 조사 및 분석
- 경쟁사 분석
- 트렌드 리서치
- 고객 인사이트 도출
- 데이터 수집 및 해석

원칙: 객관적 사실 기반, 다양한 소스 활용, 실행 가능한 인사이트 제공`,
  },
  writing: {
    key: 'writing',
    name: '작문 전문가',
    description: '이메일, 문서, 번역, 요약',
    systemPrompt: `당신은 작문 전문가입니다.
명확하고 효과적인 문서 작성으로 커뮤니케이션을 지원합니다.

전문 분야:
- 비즈니스 이메일 작성
- 제안서 및 보고서
- 번역 (한국어 ↔ 영어)
- 문서 요약 및 편집
- 프레젠테이션 내러티브

원칙: 독자 중심, 명확성, 간결성, 목적에 맞는 톤`,
  },
  hr: {
    key: 'hr',
    name: 'HR 전문가',
    description: '채용, 조직 관리, 성과 관리',
    systemPrompt: `당신은 HR 전문가입니다.
조직의 인재를 관리하고 성과를 극대화하는 전략을 지원합니다.

전문 분야:
- 채용 프로세스 설계
- 성과 관리 시스템
- 조직 문화 개선
- 직원 교육 및 개발
- 보상 및 복리후생 설계

원칙: 사람 중심, 공정성, 데이터 기반 HR, 법규 준수`,
  },
  finance: {
    key: 'finance',
    name: '재무 전문가',
    description: '재무 분석, 예산 수립, 투자 검토',
    systemPrompt: `당신은 재무 전문가입니다.
비즈니스의 재무 건전성을 유지하고 성장을 위한 재무 전략을 지원합니다.

전문 분야:
- 재무제표 분석
- 예산 수립 및 관리
- 투자 타당성 검토
- 현금 흐름 관리
- 재무 리스크 관리

원칙: 보수적 접근, 데이터 정확성, 리스크 인식, 장기적 관점`,
  },
  legal: {
    key: 'legal',
    name: '법무 전문가',
    description: '계약 검토, 법률 자문, 리스크 식별',
    systemPrompt: `당신은 법무 전문가입니다.
비즈니스 운영에서 발생하는 법적 리스크를 식별하고 관리합니다.

전문 분야:
- 계약서 검토 및 작성
- 법적 리스크 식별
- 지적재산권 관리
- 개인정보보호 컴플라이언스
- 분쟁 예방 전략

원칙: 리스크 최소화, 명확한 설명, 실무적 조언 (단, 공식 법률 자문은 변호사에게)`,
  },
  sales: {
    key: 'sales',
    name: '영업 전문가',
    description: '영업 전략, 파이프라인 관리, 제안서',
    systemPrompt: `당신은 영업 전문가입니다.
효과적인 영업 전략과 실행으로 매출 성장을 지원합니다.

전문 분야:
- 영업 전략 수립
- 파이프라인 관리
- 제안서 및 영업 자료 작성
- 고객 관계 관리
- 협상 전략

원칙: 고객 가치 중심, 데이터 기반 영업, 관계 구축, 지속적 개선`,
  },
  data: {
    key: 'data',
    name: '데이터 분석가',
    description: '데이터 분석, 시각화, 인사이트 도출',
    systemPrompt: `당신은 데이터 분석가입니다.
데이터에서 의미 있는 인사이트를 발견하고 의사결정을 지원합니다.

전문 분야:
- 데이터 분석 및 해석
- 통계 분석
- 데이터 시각화 방향 제시
- KPI 설계 및 모니터링
- A/B 테스트 설계

원칙: 데이터 품질 우선, 객관성, 실행 가능한 인사이트, 불확실성 명시`,
  },
  product: {
    key: 'product',
    name: '프로덕트 매니저',
    description: '제품 전략, 로드맵, 사용자 리서치',
    systemPrompt: `당신은 프로덕트 매니저입니다.
사용자 중심의 제품 전략으로 비즈니스 성과를 극대화합니다.

전문 분야:
- 제품 비전 및 전략
- 로드맵 수립
- 사용자 리서치 설계
- 기능 우선순위 결정
- 제품 지표 정의

원칙: 사용자 중심, 데이터 기반, 빠른 실험, 비즈니스 임팩트 연결`,
  },
  development: {
    key: 'development',
    name: '개발 전문가',
    description: '기술 아키텍처, 코드 리뷰, 개발 전략',
    systemPrompt: `당신은 개발 전문가입니다.
기술적 의사결정과 개발 전략으로 제품 개발을 지원합니다.

전문 분야:
- 기술 아키텍처 설계
- 기술 스택 선택
- 코드 품질 및 리뷰
- 개발 프로세스 개선
- 기술 부채 관리

원칙: 단순성, 확장성, 유지보수성, 보안, 성능`,
  },
  design: {
    key: 'design',
    name: '디자인 전문가',
    description: 'UX/UI 설계, 브랜드 디자인, 사용성',
    systemPrompt: `당신은 디자인 전문가입니다.
사용자 경험과 브랜드 정체성을 통해 비즈니스 가치를 높입니다.

전문 분야:
- UX/UI 설계
- 브랜드 아이덴티티
- 사용성 테스트 설계
- 디자인 시스템
- 시각적 커뮤니케이션

원칙: 사용자 우선, 일관성, 접근성, 비즈니스 목표 연계`,
  },
  productivity: {
    key: 'productivity',
    name: '생산성 전문가',
    description: '업무 관리, 일정 조율, 프로세스 최적화',
    systemPrompt: `당신은 생산성 전문가입니다.
효율적인 업무 방식으로 개인과 팀의 생산성을 극대화합니다.

전문 분야:
- 작업 관리 및 우선순위
- 일정 계획 및 조율
- 회의 효율화
- 업무 프로세스 최적화
- 메모 및 문서 정리

원칙: 선택과 집중, 시간 효율, 체계적 접근, 지속 가능한 방식`,
  },
  pr: {
    key: 'pr',
    name: 'PR 전문가',
    description: '홍보 전략, 미디어 관계, 위기 커뮤니케이션',
    systemPrompt: `당신은 PR 전문가입니다.
브랜드 이미지와 대외 커뮤니케이션을 전략적으로 관리합니다.

전문 분야:
- 홍보 전략 수립
- 보도자료 작성
- 미디어 관계 관리
- 위기 커뮤니케이션
- 소셜 미디어 전략

원칙: 진정성, 투명성, 선제적 커뮤니케이션, 브랜드 일관성`,
  },
  security: {
    key: 'security',
    name: '보안 전문가',
    description: '정보 보안, 리스크 관리, 보안 정책',
    systemPrompt: `당신은 보안 전문가입니다.
비즈니스 자산과 데이터를 보호하는 보안 전략을 지원합니다.

전문 분야:
- 보안 리스크 평가
- 보안 정책 수립
- 데이터 보호 전략
- 보안 인식 교육
- 인시던트 대응 계획

원칙: 심층 방어, 최소 권한, 지속적 모니터링, 사전 예방`,
  },
  compliance: {
    key: 'compliance',
    name: '컴플라이언스 전문가',
    description: '규정 준수, 내부 감사, 리스크 관리',
    systemPrompt: `당신은 컴플라이언스 전문가입니다.
법적·규제적 요구사항 준수를 통해 비즈니스 리스크를 관리합니다.

전문 분야:
- 규정 준수 체계 구축
- 내부 감사 프로세스
- 리스크 식별 및 평가
- 컴플라이언스 교육
- 정책 문서화

원칙: 예방 중심, 문서화, 지속적 모니터링, 이해관계자 소통`,
  },
  business_dev: {
    key: 'business_dev',
    name: '사업개발 전문가',
    description: '파트너십, 신규 사업, 사업 전략',
    systemPrompt: `당신은 사업개발 전문가입니다.
새로운 비즈니스 기회를 발굴하고 성장 전략을 실행합니다.

전문 분야:
- 사업 기회 발굴
- 파트너십 전략
- M&A 검토
- 신규 시장 진출
- 사업 모델 설계

원칙: 기회 탐색, 빠른 검증, 장기적 관계 구축, 전략적 정렬`,
  },
}

export const AGENT_KEYS = Object.keys(AGENT_DEFINITIONS) as AgentKey[]
```

**Step 2: 커밋**

```bash
git add lib/agents/definitions.ts
git commit -m "feat: 16개 전문가 에이전트 TypeScript 정의"
```

---

## Task 5: 오케스트레이터 로직

**Files:**
- Create: `lib/agents/orchestrator.ts`

**Step 1: 오케스트레이터 작성**

```typescript
// lib/agents/orchestrator.ts
import Anthropic from '@anthropic-ai/sdk'
import { AGENT_DEFINITIONS, AGENT_KEYS } from './definitions'
import type { AgentKey, Attachment } from '@/lib/types'

const ORCHESTRATOR_SYSTEM_PROMPT = `당신은 사업가의 개인 비서이자 전문가 팀의 리더입니다.
사용자의 비즈니스 요청을 분석하고 적절한 전문가 팀원에게 작업을 할당합니다.

팀 구성:
- marketing: 마케팅 콘텐츠, 캠페인, 브랜드 전략
- research: 시장 조사, 경쟁사 분석, 트렌드
- writing: 이메일, 문서, 번역, 요약
- hr: 채용, 조직 관리, 성과 관리
- finance: 재무 분석, 예산, 투자
- legal: 계약 검토, 법률 자문
- sales: 영업 전략, 파이프라인, 제안서
- data: 데이터 분석, 통계, KPI
- product: 제품 전략, 로드맵, 사용자 리서치
- development: 기술 아키텍처, 코드, 개발 전략
- design: UX/UI, 브랜드, 사용성
- productivity: 업무 관리, 일정, 프로세스
- pr: 홍보, 미디어, 위기 커뮤니케이션
- security: 정보 보안, 리스크
- compliance: 규정 준수, 내부 감사
- business_dev: 파트너십, 신규 사업

요청에 가장 적합한 에이전트를 선택하세요.`

// 오케스트레이터: 어느 에이전트를 쓸지 결정 (non-streaming)
export async function selectAgent(
  apiKey: string,
  message: string,
  history: Array<{ role: 'user' | 'assistant'; content: string }>
): Promise<AgentKey> {
  const client = new Anthropic({ apiKey })

  const tools: Anthropic.Tool[] = AGENT_KEYS.map(key => ({
    name: key,
    description: AGENT_DEFINITIONS[key].description,
    input_schema: {
      type: 'object' as const,
      properties: {
        task: { type: 'string', description: '처리할 작업 내용' },
      },
      required: ['task'],
    },
  }))

  const response = await client.messages.create({
    model: 'claude-haiku-4-5-20251001',  // 라우팅은 Haiku로 (빠르고 저렴)
    max_tokens: 100,
    system: ORCHESTRATOR_SYSTEM_PROMPT,
    tools,
    tool_choice: { type: 'any' },
    messages: [
      ...history.slice(-6),  // 최근 3턴만 컨텍스트로
      { role: 'user', content: message },
    ],
  })

  const toolUse = response.content.find(b => b.type === 'tool_use')
  if (toolUse && toolUse.type === 'tool_use') {
    const selected = toolUse.name as AgentKey
    if (AGENT_KEYS.includes(selected)) return selected
  }

  return 'writing'  // 폴백: 범용 작문 에이전트
}

// 선택된 에이전트로 스트리밍 응답 생성
export async function* streamAgentResponse(
  apiKey: string,
  agentKey: AgentKey,
  message: string,
  history: Array<{ role: 'user' | 'assistant'; content: string }>,
  attachments?: Attachment[]
): AsyncGenerator<string> {
  const client = new Anthropic({ apiKey })
  const agent = AGENT_DEFINITIONS[agentKey]

  // 파일 첨부 처리
  const userContent: Anthropic.MessageParam['content'] = []

  if (attachments && attachments.length > 0) {
    for (const att of attachments) {
      if (att.type.startsWith('image/')) {
        userContent.push({
          type: 'image',
          source: {
            type: 'base64',
            media_type: att.type as 'image/jpeg' | 'image/png' | 'image/gif' | 'image/webp',
            data: att.data,
          },
        })
      }
    }
  }

  userContent.push({ type: 'text', text: message })

  const stream = await client.messages.stream({
    model: 'claude-sonnet-4-6',
    max_tokens: 4096,
    system: agent.systemPrompt,
    messages: [
      ...history.slice(-20),
      { role: 'user', content: userContent },
    ],
  })

  for await (const chunk of stream) {
    if (
      chunk.type === 'content_block_delta' &&
      chunk.delta.type === 'text_delta'
    ) {
      yield chunk.delta.text
    }
  }
}
```

**Step 2: 커밋**

```bash
git add lib/agents/orchestrator.ts
git commit -m "feat: 에이전트 오케스트레이터 (라우팅 + 스트리밍)"
```

---

## Task 6: API Route — validate-key

**Files:**
- Create: `app/api/validate-key/route.ts`

**Step 1: validate-key 엔드포인트 작성**

```typescript
// app/api/validate-key/route.ts
import { NextRequest, NextResponse } from 'next/server'
import Anthropic from '@anthropic-ai/sdk'

export async function POST(req: NextRequest) {
  const { apiKey } = await req.json()

  if (!apiKey || typeof apiKey !== 'string') {
    return NextResponse.json({ valid: false, error: 'API 키를 입력해주세요.' }, { status: 400 })
  }

  if (!apiKey.startsWith('sk-ant-')) {
    return NextResponse.json(
      { valid: false, error: 'API 키 형식이 올바르지 않습니다. sk-ant-로 시작해야 합니다.' },
      { status: 400 }
    )
  }

  try {
    const client = new Anthropic({ apiKey })
    await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 10,
      messages: [{ role: 'user', content: 'hi' }],
    })
    return NextResponse.json({ valid: true })
  } catch (err: any) {
    if (err?.status === 401) {
      return NextResponse.json({ valid: false, error: '유효하지 않은 API 키입니다.' })
    }
    if (err?.status === 429) {
      return NextResponse.json({ valid: false, error: '요청 한도를 초과했습니다. 잠시 후 다시 시도해주세요.' })
    }
    return NextResponse.json({ valid: false, error: 'API 키 확인 중 오류가 발생했습니다.' })
  }
}
```

**Step 2: 커밋**

```bash
git add app/api/validate-key/route.ts
git commit -m "feat: API 키 유효성 검증 엔드포인트"
```

---

## Task 7: API Route — chat (SSE 스트리밍)

**Files:**
- Create: `app/api/chat/route.ts`

**Step 1: chat 엔드포인트 작성**

```typescript
// app/api/chat/route.ts
import { NextRequest } from 'next/server'
import { selectAgent, streamAgentResponse } from '@/lib/agents/orchestrator'

export const maxDuration = 60

export async function POST(req: NextRequest) {
  const apiKey = req.headers.get('x-api-key')
  if (!apiKey) {
    return new Response('API 키가 필요합니다.', { status: 401 })
  }

  const { message, history, attachments } = await req.json()

  const encoder = new TextEncoder()
  const stream = new ReadableStream({
    async start(controller) {
      const send = (event: string, data: string) => {
        controller.enqueue(encoder.encode(`event: ${event}\ndata: ${data}\n\n`))
      }

      try {
        // 1단계: 에이전트 선택
        const agentKey = await selectAgent(apiKey, message, history)
        send('agent', agentKey)

        // 2단계: 선택된 에이전트로 스트리밍 응답
        for await (const chunk of streamAgentResponse(apiKey, agentKey, message, history, attachments)) {
          send('delta', chunk)
        }

        send('done', '[DONE]')
      } catch (err: any) {
        const errMsg = err?.status === 401
          ? 'API 키가 유효하지 않습니다.'
          : err?.status === 429
          ? '요청 한도를 초과했습니다.'
          : '오류가 발생했습니다. 다시 시도해주세요.'
        send('error', errMsg)
      } finally {
        controller.close()
      }
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Step 2: 커밋**

```bash
git add app/api/chat/route.ts
git commit -m "feat: SSE 스트리밍 채팅 API 엔드포인트"
```

---

## Task 8: 온보딩 모달 (4단계 — 핵심)

초심자가 API 키 없이 막히지 않도록 친절한 단계별 가이드를 제공한다.

**Files:**
- Create: `components/onboarding/OnboardingModal.tsx`
- Create: `components/onboarding/StepIntro.tsx`
- Create: `components/onboarding/StepApiGuide.tsx`
- Create: `components/onboarding/StepApiInput.tsx`
- Create: `components/onboarding/StepFirstChat.tsx`

**Step 1: OnboardingModal 컨테이너**

```typescript
// components/onboarding/OnboardingModal.tsx
'use client'
import { useState } from 'react'
import { Dialog, DialogContent } from '@/components/ui/dialog'
import { StepIntro } from './StepIntro'
import { StepApiGuide } from './StepApiGuide'
import { StepApiInput } from './StepApiInput'
import { StepFirstChat } from './StepFirstChat'
import { setApiKey } from '@/lib/storage/conversations'

interface OnboardingModalProps {
  open: boolean
  onComplete: (apiKey: string, firstMessage?: string) => void
}

export function OnboardingModal({ open, onComplete }: OnboardingModalProps) {
  const [step, setStep] = useState(0)
  const [savedKey, setSavedKey] = useState('')

  const handleKeyConfirmed = (key: string) => {
    setApiKey(key)
    setSavedKey(key)
    setStep(3)
  }

  const handleFirstChat = (message?: string) => {
    onComplete(savedKey, message)
  }

  return (
    <Dialog open={open} onOpenChange={() => {}}>
      {/* 닫기 버튼 없음 — API 키 입력 전까지 필수 */}
      <DialogContent
        className="max-w-lg bg-zinc-900 border-zinc-800 text-white [&>button]:hidden"
      >
        {/* 진행 표시 점 */}
        <div className="flex justify-center gap-2 mb-2">
          {[0, 1, 2, 3].map(i => (
            <div
              key={i}
              className={`h-1.5 rounded-full transition-all duration-300 ${
                i === step ? 'w-6 bg-indigo-500' : i < step ? 'w-3 bg-indigo-400' : 'w-3 bg-zinc-700'
              }`}
            />
          ))}
        </div>

        {step === 0 && <StepIntro onNext={() => setStep(1)} />}
        {step === 1 && <StepApiGuide onNext={() => setStep(2)} onBack={() => setStep(0)} />}
        {step === 2 && <StepApiInput onConfirmed={handleKeyConfirmed} onBack={() => setStep(1)} />}
        {step === 3 && <StepFirstChat onStart={handleFirstChat} />}
      </DialogContent>
    </Dialog>
  )
}
```

**Step 2: StepIntro — 서비스 소개**

```typescript
// components/onboarding/StepIntro.tsx
import { Button } from '@/components/ui/button'

const TEAM_PREVIEW = [
  { icon: '📢', name: '마케팅', desc: '콘텐츠·캠페인' },
  { icon: '🔍', name: '리서치', desc: '시장·경쟁사 분석' },
  { icon: '✍️', name: '작문', desc: '이메일·문서·번역' },
  { icon: '💰', name: '재무', desc: '예산·투자 분석' },
  { icon: '⚖️', name: '법무', desc: '계약·리스크' },
  { icon: '📊', name: '데이터', desc: '분석·인사이트' },
]

export function StepIntro({ onNext }: { onNext: () => void }) {
  return (
    <div className="space-y-6">
      <div className="text-center space-y-2">
        <h2 className="text-2xl font-bold text-white" style={{ fontFamily: 'Poppins, sans-serif' }}>
          Business AI Team에 오신 것을 환영합니다
        </h2>
        <p className="text-zinc-400 text-sm">
          16명의 전문가 AI 팀이 당신의 비즈니스를 도와드립니다
        </p>
      </div>

      <div className="grid grid-cols-3 gap-3">
        {TEAM_PREVIEW.map(member => (
          <div
            key={member.name}
            className="bg-zinc-800 rounded-xl p-3 text-center border border-zinc-700"
          >
            <div className="text-2xl mb-1">{member.icon}</div>
            <div className="text-white text-xs font-semibold">{member.name}</div>
            <div className="text-zinc-500 text-xs">{member.desc}</div>
          </div>
        ))}
      </div>

      <p className="text-zinc-500 text-xs text-center">
        마케팅, 재무, 법무, 개발 등 16개 분야 전문가가 대기 중입니다.
        질문 하나로 적합한 전문가가 자동으로 배정됩니다.
      </p>

      <Button
        onClick={onNext}
        className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold h-11"
      >
        시작하기
      </Button>
    </div>
  )
}
```

**Step 3: StepApiGuide — API 키 발급 가이드 (초심자 핵심)**

```typescript
// components/onboarding/StepApiGuide.tsx
import { Button } from '@/components/ui/button'
import { ExternalLink, ChevronLeft } from 'lucide-react'

const STEPS = [
  {
    step: '1',
    title: 'Anthropic Console 접속',
    desc: 'console.anthropic.com 에 접속해 회원가입 또는 로그인하세요.',
  },
  {
    step: '2',
    title: '"API Keys" 메뉴 클릭',
    desc: '로그인 후 좌측 사이드바에서 "API Keys"를 클릭하세요.',
  },
  {
    step: '3',
    title: '"Create Key" 버튼 클릭',
    desc: '우측 상단의 "+ Create Key" 버튼을 눌러 새 키를 생성하세요.',
  },
  {
    step: '4',
    title: '키 복사',
    desc: 'sk-ant-로 시작하는 키가 생성됩니다. 반드시 복사해두세요. (다시 확인 불가)',
  },
]

export function StepApiGuide({ onNext, onBack }: { onNext: () => void; onBack: () => void }) {
  return (
    <div className="space-y-5">
      <div className="space-y-1">
        <h2 className="text-xl font-bold text-white" style={{ fontFamily: 'Poppins, sans-serif' }}>
          API 키 발급 방법
        </h2>
        <p className="text-zinc-400 text-sm">
          이 서비스를 사용하려면 Anthropic API 키가 필요합니다.
          아래 단계를 따라 무료로 발급받으세요.
        </p>
      </div>

      {/* 비용 안내 배너 */}
      <div className="bg-emerald-950 border border-emerald-800 rounded-lg px-4 py-3 text-sm">
        <span className="text-emerald-400 font-semibold">무료 크레딧 안내: </span>
        <span className="text-zinc-300">
          새 계정에는 $5 무료 크레딧이 제공됩니다.
          일반적인 사용 기준으로 수백 회 이상 대화할 수 있는 양입니다.
        </span>
      </div>

      {/* 단계별 가이드 */}
      <div className="space-y-3">
        {STEPS.map(({ step, title, desc }) => (
          <div key={step} className="flex gap-3 items-start">
            <div className="flex-shrink-0 w-7 h-7 rounded-full bg-indigo-600 flex items-center justify-center text-white text-xs font-bold">
              {step}
            </div>
            <div>
              <p className="text-white text-sm font-medium">{title}</p>
              <p className="text-zinc-400 text-xs mt-0.5">{desc}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Console 바로가기 */}
      <a
        href="https://console.anthropic.com"
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center justify-center gap-2 w-full border border-indigo-600 text-indigo-400 hover:bg-indigo-950 rounded-lg py-2.5 text-sm font-medium transition-colors cursor-pointer"
      >
        <ExternalLink size={15} />
        console.anthropic.com 열기
      </a>

      <div className="flex gap-2">
        <Button variant="ghost" onClick={onBack} className="text-zinc-400 hover:text-white">
          <ChevronLeft size={16} />
          이전
        </Button>
        <Button onClick={onNext} className="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white h-10">
          키를 발급받았어요
        </Button>
      </div>
    </div>
  )
}
```

**Step 4: StepApiInput — API 키 입력 + 검증**

```typescript
// components/onboarding/StepApiInput.tsx
'use client'
import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { CheckCircle, AlertCircle, ChevronLeft, Eye, EyeOff, ClipboardPaste } from 'lucide-react'

interface StepApiInputProps {
  onConfirmed: (key: string) => void
  onBack: () => void
}

export function StepApiInput({ onConfirmed, onBack }: StepApiInputProps) {
  const [key, setKey] = useState('')
  const [showKey, setShowKey] = useState(false)
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle')
  const [errorMsg, setErrorMsg] = useState('')

  const isValidFormat = key.startsWith('sk-ant-') && key.length > 20

  const handlePaste = async () => {
    try {
      const text = await navigator.clipboard.readText()
      setKey(text.trim())
      setStatus('idle')
    } catch {
      // 클립보드 접근 불가 시 사용자가 수동 입력
    }
  }

  const handleVerify = async () => {
    if (!isValidFormat) return
    setStatus('loading')
    setErrorMsg('')

    try {
      const res = await fetch('/api/validate-key', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ apiKey: key }),
      })
      const data = await res.json()

      if (data.valid) {
        setStatus('success')
        setTimeout(() => onConfirmed(key), 800)
      } else {
        setStatus('error')
        setErrorMsg(data.error ?? '알 수 없는 오류가 발생했습니다.')
      }
    } catch {
      setStatus('error')
      setErrorMsg('네트워크 오류가 발생했습니다. 인터넷 연결을 확인해주세요.')
    }
  }

  return (
    <div className="space-y-5">
      <div className="space-y-1">
        <h2 className="text-xl font-bold text-white" style={{ fontFamily: 'Poppins, sans-serif' }}>
          API 키 입력
        </h2>
        <p className="text-zinc-400 text-sm">
          발급받은 API 키를 아래에 붙여넣어 주세요.
        </p>
      </div>

      {/* 입력창 */}
      <div className="space-y-2">
        <div className="flex gap-2">
          <div className="relative flex-1">
            <Input
              type={showKey ? 'text' : 'password'}
              placeholder="sk-ant-api03-..."
              value={key}
              onChange={e => { setKey(e.target.value); setStatus('idle') }}
              className="bg-zinc-800 border-zinc-700 text-white placeholder:text-zinc-600 pr-10 font-mono text-sm"
            />
            <button
              onClick={() => setShowKey(v => !v)}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500 hover:text-zinc-300"
            >
              {showKey ? <EyeOff size={16} /> : <Eye size={16} />}
            </button>
          </div>
          <Button
            variant="outline"
            onClick={handlePaste}
            className="border-zinc-700 text-zinc-300 hover:text-white hover:bg-zinc-800 shrink-0"
          >
            <ClipboardPaste size={15} />
            붙여넣기
          </Button>
        </div>

        {/* 형식 검사 힌트 */}
        {key && !isValidFormat && (
          <p className="text-amber-400 text-xs flex items-center gap-1">
            <AlertCircle size={12} />
            API 키는 sk-ant-로 시작해야 합니다.
          </p>
        )}

        {/* 성공/실패 메시지 */}
        {status === 'success' && (
          <p className="text-emerald-400 text-sm flex items-center gap-1.5">
            <CheckCircle size={14} />
            연결됐습니다! AI 팀을 사용할 준비가 됐어요.
          </p>
        )}
        {status === 'error' && (
          <div className="bg-red-950 border border-red-800 rounded-lg p-3 space-y-1">
            <p className="text-red-400 text-sm flex items-center gap-1.5">
              <AlertCircle size={14} />
              {errorMsg}
            </p>
            <p className="text-zinc-400 text-xs">
              API 키를 다시 확인하거나 새로 발급받으세요.
            </p>
          </div>
        )}
      </div>

      {/* 보안 안내 */}
      <div className="bg-zinc-800 rounded-lg p-3 text-xs text-zinc-400 space-y-1">
        <p className="font-medium text-zinc-300">보안 안내</p>
        <p>입력한 API 키는 이 브라우저에만 저장되며, 서버에는 저장되지 않습니다.</p>
        <p>브라우저 데이터를 삭제하면 다시 입력해야 합니다.</p>
      </div>

      <div className="flex gap-2">
        <Button variant="ghost" onClick={onBack} className="text-zinc-400 hover:text-white">
          <ChevronLeft size={16} />
          이전
        </Button>
        <Button
          onClick={handleVerify}
          disabled={!isValidFormat || status === 'loading' || status === 'success'}
          className="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white h-10 disabled:opacity-50"
        >
          {status === 'loading' ? '확인 중...' : status === 'success' ? '연결 완료' : '연결 확인'}
        </Button>
      </div>
    </div>
  )
}
```

**Step 5: StepFirstChat — 예시 질문 제안**

```typescript
// components/onboarding/StepFirstChat.tsx
import { Button } from '@/components/ui/button'
import { ArrowRight } from 'lucide-react'

const EXAMPLE_MESSAGES = [
  { label: '마케팅 전략 세우기', message: '우리 서비스의 마케팅 전략을 세워줘. 타겟 고객과 채널 전략도 포함해줘.' },
  { label: '경쟁사 분석', message: '주요 경쟁사 3곳을 분석해줘. 강점, 약점, 차별화 포인트를 정리해줘.' },
  { label: '파트너사 이메일 작성', message: '파트너사에 협업을 제안하는 비즈니스 이메일을 작성해줘.' },
]

export function StepFirstChat({ onStart }: { onStart: (message?: string) => void }) {
  return (
    <div className="space-y-6">
      <div className="text-center space-y-2">
        <div className="text-4xl mb-3">🎉</div>
        <h2 className="text-xl font-bold text-white" style={{ fontFamily: 'Poppins, sans-serif' }}>
          준비 완료!
        </h2>
        <p className="text-zinc-400 text-sm">
          이제 AI 팀에게 무엇이든 물어보세요.
          <br />아래 예시를 눌러 바로 시작할 수도 있습니다.
        </p>
      </div>

      <div className="space-y-2">
        {EXAMPLE_MESSAGES.map(({ label, message }) => (
          <button
            key={label}
            onClick={() => onStart(message)}
            className="w-full text-left bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 hover:border-indigo-600 rounded-xl px-4 py-3 transition-all duration-200 group cursor-pointer"
          >
            <div className="flex items-center justify-between">
              <span className="text-white text-sm font-medium">{label}</span>
              <ArrowRight size={14} className="text-zinc-600 group-hover:text-indigo-400 transition-colors" />
            </div>
            <p className="text-zinc-500 text-xs mt-1 line-clamp-1">{message}</p>
          </button>
        ))}
      </div>

      <Button
        onClick={() => onStart()}
        variant="ghost"
        className="w-full text-zinc-400 hover:text-white"
      >
        직접 입력할게요
      </Button>
    </div>
  )
}
```

**Step 6: 커밋**

```bash
git add components/onboarding/
git commit -m "feat: 4단계 온보딩 모달 (API 키 발급 가이드 포함)"
```

---

## Task 9: 사이드바

**Files:**
- Create: `components/sidebar/AppSidebar.tsx`
- Create: `components/sidebar/ConversationList.tsx`
- Create: `components/sidebar/ApiKeyButton.tsx`

**Step 1: ApiKeyButton — 사이드바 하단 키 설정**

```typescript
// components/sidebar/ApiKeyButton.tsx
'use client'
import { useState } from 'react'
import { Settings, Trash2, RefreshCw } from 'lucide-react'
import { getApiKey, removeApiKey, setApiKey } from '@/lib/storage/conversations'
import { Button } from '@/components/ui/button'
import {
  Dialog, DialogContent, DialogHeader, DialogTitle
} from '@/components/ui/dialog'
import { Input } from '@/components/ui/input'

export function ApiKeyButton({ onKeyChanged }: { onKeyChanged: () => void }) {
  const [open, setOpen] = useState(false)
  const [newKey, setNewKey] = useState('')
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle')
  const [error, setError] = useState('')

  const currentKey = getApiKey()
  const maskedKey = currentKey
    ? `sk-ant-...${currentKey.slice(-6)}`
    : '키 없음'

  const handleSave = async () => {
    if (!newKey.startsWith('sk-ant-')) return
    setStatus('loading')
    try {
      const res = await fetch('/api/validate-key', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ apiKey: newKey }),
      })
      const data = await res.json()
      if (data.valid) {
        setApiKey(newKey)
        setStatus('success')
        setTimeout(() => { setOpen(false); onKeyChanged(); setNewKey(''); setStatus('idle') }, 800)
      } else {
        setStatus('error')
        setError(data.error ?? '유효하지 않은 키입니다.')
      }
    } catch {
      setStatus('error')
      setError('네트워크 오류')
    }
  }

  const handleDelete = () => {
    removeApiKey()
    setOpen(false)
    onKeyChanged()
  }

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="flex items-center gap-2 w-full px-3 py-2 rounded-lg text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors text-sm cursor-pointer"
      >
        <Settings size={15} />
        <span className="font-mono text-xs">{maskedKey}</span>
      </button>

      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="bg-zinc-900 border-zinc-800 text-white max-w-sm">
          <DialogHeader>
            <DialogTitle>API 키 설정</DialogTitle>
          </DialogHeader>
          <div className="space-y-4">
            <div className="bg-zinc-800 rounded-lg p-3 text-sm text-zinc-400 font-mono">
              현재: {maskedKey}
            </div>
            <Input
              placeholder="새 API 키 (sk-ant-...)"
              value={newKey}
              onChange={e => { setNewKey(e.target.value); setStatus('idle') }}
              className="bg-zinc-800 border-zinc-700 text-white font-mono text-sm"
            />
            {status === 'error' && <p className="text-red-400 text-xs">{error}</p>}
            {status === 'success' && <p className="text-emerald-400 text-xs">저장됐습니다!</p>}
            <div className="flex gap-2">
              <Button
                variant="outline"
                onClick={handleDelete}
                className="border-red-800 text-red-400 hover:bg-red-950 hover:text-red-300"
              >
                <Trash2 size={14} />
                삭제
              </Button>
              <Button
                onClick={handleSave}
                disabled={!newKey.startsWith('sk-ant-') || status === 'loading'}
                className="flex-1 bg-indigo-600 hover:bg-indigo-500"
              >
                {status === 'loading' ? <RefreshCw size={14} className="animate-spin" /> : '저장'}
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </>
  )
}
```

**Step 2: ConversationList**

```typescript
// components/sidebar/ConversationList.tsx
'use client'
import { Trash2 } from 'lucide-react'
import type { Conversation } from '@/lib/types'
import { deleteConversation } from '@/lib/storage/conversations'

function groupByDate(conversations: Conversation[]) {
  const today = new Date().toDateString()
  const yesterday = new Date(Date.now() - 86400000).toDateString()
  const groups: Record<string, Conversation[]> = { '오늘': [], '어제': [], '이전': [] }

  for (const conv of conversations) {
    const d = new Date(conv.updatedAt).toDateString()
    if (d === today) groups['오늘'].push(conv)
    else if (d === yesterday) groups['어제'].push(conv)
    else groups['이전'].push(conv)
  }
  return groups
}

interface Props {
  conversations: Conversation[]
  activeId: string | null
  onSelect: (id: string) => void
  onDelete: () => void
}

export function ConversationList({ conversations, activeId, onSelect, onDelete }: Props) {
  const groups = groupByDate(conversations)

  const handleDelete = (e: React.MouseEvent, id: string) => {
    e.stopPropagation()
    deleteConversation(id)
    onDelete()
  }

  return (
    <div className="space-y-4 overflow-y-auto flex-1 px-2">
      {Object.entries(groups).map(([label, convs]) =>
        convs.length === 0 ? null : (
          <div key={label}>
            <p className="text-zinc-600 text-xs px-2 mb-1 font-medium">{label}</p>
            {convs.map(conv => (
              <div
                key={conv.id}
                onClick={() => onSelect(conv.id)}
                className={`group flex items-center gap-2 px-3 py-2 rounded-lg cursor-pointer transition-colors ${
                  activeId === conv.id
                    ? 'bg-zinc-800 text-white'
                    : 'text-zinc-400 hover:bg-zinc-800/60 hover:text-white'
                }`}
              >
                <span className="flex-1 text-sm truncate">{conv.title}</span>
                <button
                  onClick={e => handleDelete(e, conv.id)}
                  className="opacity-0 group-hover:opacity-100 text-zinc-600 hover:text-red-400 transition-all cursor-pointer"
                >
                  <Trash2 size={13} />
                </button>
              </div>
            ))}
          </div>
        )
      )}
      {conversations.length === 0 && (
        <p className="text-zinc-600 text-sm text-center py-8">대화 기록이 없습니다</p>
      )}
    </div>
  )
}
```

**Step 3: AppSidebar**

```typescript
// components/sidebar/AppSidebar.tsx
'use client'
import { SquarePen } from 'lucide-react'
import { ConversationList } from './ConversationList'
import { ApiKeyButton } from './ApiKeyButton'
import type { Conversation } from '@/lib/types'

interface AppSidebarProps {
  conversations: Conversation[]
  activeId: string | null
  onNewChat: () => void
  onSelect: (id: string) => void
  onRefresh: () => void
}

export function AppSidebar({ conversations, activeId, onNewChat, onSelect, onRefresh }: AppSidebarProps) {
  return (
    <div className="w-64 flex-shrink-0 bg-zinc-950 border-r border-zinc-800 flex flex-col h-screen">
      {/* 헤더 */}
      <div className="p-3 border-b border-zinc-800">
        <button
          onClick={onNewChat}
          className="flex items-center gap-2 w-full px-3 py-2.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium transition-colors cursor-pointer"
        >
          <SquarePen size={15} />
          새 대화
        </button>
      </div>

      {/* 대화 목록 */}
      <div className="flex-1 overflow-hidden py-3">
        <ConversationList
          conversations={conversations}
          activeId={activeId}
          onSelect={onSelect}
          onDelete={onRefresh}
        />
      </div>

      {/* API 키 설정 (하단 고정) */}
      <div className="p-3 border-t border-zinc-800">
        <ApiKeyButton onKeyChanged={onRefresh} />
      </div>
    </div>
  )
}
```

**Step 4: 커밋**

```bash
git add components/sidebar/
git commit -m "feat: 사이드바 (대화 목록 + API 키 설정)"
```

---

## Task 10: 채팅 컴포넌트

**Files:**
- Create: `components/chat/AgentBadge.tsx`
- Create: `components/chat/MessageItem.tsx`
- Create: `components/chat/MessageList.tsx`
- Create: `components/chat/InputBar.tsx`
- Create: `components/chat/ChatArea.tsx`

**Step 1: AgentBadge**

```typescript
// components/chat/AgentBadge.tsx
import type { AgentKey } from '@/lib/types'
import { AGENT_DEFINITIONS } from '@/lib/agents/definitions'

const AGENT_COLORS: Partial<Record<AgentKey, string>> = {
  marketing: 'bg-pink-950 text-pink-400 border-pink-800',
  research: 'bg-blue-950 text-blue-400 border-blue-800',
  writing: 'bg-purple-950 text-purple-400 border-purple-800',
  hr: 'bg-orange-950 text-orange-400 border-orange-800',
  finance: 'bg-yellow-950 text-yellow-400 border-yellow-800',
  legal: 'bg-red-950 text-red-400 border-red-800',
  sales: 'bg-green-950 text-green-400 border-green-800',
  data: 'bg-cyan-950 text-cyan-400 border-cyan-800',
  product: 'bg-indigo-950 text-indigo-400 border-indigo-800',
  development: 'bg-teal-950 text-teal-400 border-teal-800',
  design: 'bg-violet-950 text-violet-400 border-violet-800',
  productivity: 'bg-amber-950 text-amber-400 border-amber-800',
  pr: 'bg-rose-950 text-rose-400 border-rose-800',
  security: 'bg-slate-800 text-slate-400 border-slate-600',
  compliance: 'bg-stone-800 text-stone-400 border-stone-600',
  business_dev: 'bg-emerald-950 text-emerald-400 border-emerald-800',
}

export function AgentBadge({ agentKey }: { agentKey: AgentKey }) {
  const def = AGENT_DEFINITIONS[agentKey]
  const color = AGENT_COLORS[agentKey] ?? 'bg-zinc-800 text-zinc-400 border-zinc-700'
  return (
    <span className={`inline-flex items-center text-xs px-2 py-0.5 rounded-full border ${color}`}>
      {def?.name ?? agentKey}
    </span>
  )
}
```

**Step 2: MessageItem**

```typescript
// components/chat/MessageItem.tsx
import ReactMarkdown from 'react-markdown'
import rehypeHighlight from 'rehype-highlight'
import { AgentBadge } from './AgentBadge'
import type { Message, AgentKey } from '@/lib/types'
import 'highlight.js/styles/github-dark.css'

export function MessageItem({ message }: { message: Message }) {
  const isUser = message.role === 'user'
  return (
    <div className={`flex gap-3 ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-indigo-600 flex items-center justify-center text-white text-xs font-bold shrink-0 mt-1">
          AI
        </div>
      )}
      <div className={`max-w-[80%] space-y-2 ${isUser ? 'items-end' : 'items-start'} flex flex-col`}>
        {/* 첨부 이미지 */}
        {message.attachments?.filter(a => a.type.startsWith('image/')).map((att, i) => (
          <img
            key={i}
            src={`data:${att.type};base64,${att.data}`}
            alt={att.name}
            className="rounded-lg max-w-xs max-h-48 object-cover border border-zinc-700"
          />
        ))}

        {/* 메시지 버블 */}
        <div className={`rounded-2xl px-4 py-3 text-sm ${
          isUser
            ? 'bg-indigo-600 text-white rounded-br-sm'
            : 'bg-zinc-800 text-zinc-100 rounded-bl-sm'
        }`}>
          {isUser ? (
            <p className="whitespace-pre-wrap">{message.content}</p>
          ) : (
            <div className="prose prose-invert prose-sm max-w-none">
              <ReactMarkdown rehypePlugins={[rehypeHighlight]}>
                {message.content}
              </ReactMarkdown>
            </div>
          )}
        </div>

        {/* 사용된 에이전트 뱃지 */}
        {!isUser && message.agentsUsed && message.agentsUsed.length > 0 && (
          <div className="flex flex-wrap gap-1 px-1">
            {message.agentsUsed.map(key => (
              <AgentBadge key={key} agentKey={key as AgentKey} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
```

**Step 3: InputBar**

```typescript
// components/chat/InputBar.tsx
'use client'
import { useRef, useState, KeyboardEvent } from 'react'
import { Send, Paperclip, X } from 'lucide-react'
import type { Attachment } from '@/lib/types'

interface InputBarProps {
  onSend: (message: string, attachments: Attachment[]) => void
  disabled?: boolean
}

export function InputBar({ onSend, disabled }: InputBarProps) {
  const [text, setText] = useState('')
  const [attachments, setAttachments] = useState<Attachment[]>([])
  const fileRef = useRef<HTMLInputElement>(null)
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  const handleFile = async (files: FileList | null) => {
    if (!files) return
    const newAtts: Attachment[] = []
    for (const file of Array.from(files)) {
      if (file.size > 5 * 1024 * 1024) continue  // 5MB 제한
      const data = await new Promise<string>(resolve => {
        const reader = new FileReader()
        reader.onload = e => resolve((e.target?.result as string).split(',')[1])
        reader.readAsDataURL(file)
      })
      newAtts.push({ name: file.name, type: file.type, data, size: file.size })
    }
    setAttachments(prev => [...prev, ...newAtts])
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    handleFile(e.dataTransfer.files)
  }

  const handleSend = () => {
    if (!text.trim() && attachments.length === 0) return
    onSend(text.trim(), attachments)
    setText('')
    setAttachments([])
    if (textareaRef.current) textareaRef.current.style.height = 'auto'
  }

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div
      className="border-t border-zinc-800 bg-zinc-950 p-4"
      onDrop={handleDrop}
      onDragOver={e => e.preventDefault()}
    >
      {/* 첨부 파일 미리보기 */}
      {attachments.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-3">
          {attachments.map((att, i) => (
            <div key={i} className="flex items-center gap-1.5 bg-zinc-800 rounded-lg px-3 py-1.5 text-xs text-zinc-300">
              {att.type.startsWith('image/') && (
                <img
                  src={`data:${att.type};base64,${att.data}`}
                  alt={att.name}
                  className="w-6 h-6 object-cover rounded"
                />
              )}
              <span className="max-w-[120px] truncate">{att.name}</span>
              <button onClick={() => setAttachments(prev => prev.filter((_, j) => j !== i))}>
                <X size={12} className="text-zinc-500 hover:text-white" />
              </button>
            </div>
          ))}
        </div>
      )}

      <div className="flex gap-2 items-end">
        <button
          onClick={() => fileRef.current?.click()}
          className="text-zinc-500 hover:text-zinc-300 p-2 rounded-lg hover:bg-zinc-800 transition-colors cursor-pointer shrink-0"
        >
          <Paperclip size={18} />
        </button>
        <input
          ref={fileRef}
          type="file"
          multiple
          accept="image/*,.pdf,.txt,.md,.csv"
          className="hidden"
          onChange={e => handleFile(e.target.files)}
        />

        <textarea
          ref={textareaRef}
          value={text}
          onChange={e => {
            setText(e.target.value)
            e.target.style.height = 'auto'
            e.target.style.height = `${Math.min(e.target.scrollHeight, 160)}px`
          }}
          onKeyDown={handleKeyDown}
          placeholder="메시지를 입력하세요... (Shift+Enter: 줄바꿈)"
          disabled={disabled}
          rows={1}
          className="flex-1 bg-zinc-800 text-white rounded-xl px-4 py-3 text-sm resize-none outline-none border border-zinc-700 focus:border-indigo-600 placeholder:text-zinc-600 transition-colors disabled:opacity-50"
          style={{ minHeight: '48px', maxHeight: '160px' }}
        />

        <button
          onClick={handleSend}
          disabled={disabled || (!text.trim() && attachments.length === 0)}
          className="bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-white rounded-xl p-3 transition-colors cursor-pointer shrink-0"
        >
          <Send size={16} />
        </button>
      </div>
      <p className="text-zinc-700 text-xs mt-2 text-center">
        AI 답변은 참고용입니다. 중요한 결정은 전문가와 상의하세요.
      </p>
    </div>
  )
}
```

**Step 4: ChatArea (메인 채팅 영역)**

```typescript
// components/chat/ChatArea.tsx
'use client'
import { useEffect, useRef, useState } from 'react'
import { MessageList } from './MessageList'
import { InputBar } from './InputBar'
import { AgentBadge } from './AgentBadge'
import { addMessage, updateLastAssistantMessage } from '@/lib/storage/conversations'
import type { Conversation, Message, Attachment, AgentKey } from '@/lib/types'
import { v4 as uuidv4 } from 'uuid'

interface ChatAreaProps {
  conversation: Conversation | null
  apiKey: string
  onMessagesUpdate: () => void
}

export function ChatArea({ conversation, apiKey, onMessagesUpdate }: ChatAreaProps) {
  const [streaming, setStreaming] = useState(false)
  const [streamingText, setStreamingText] = useState('')
  const [activeAgent, setActiveAgent] = useState<AgentKey | null>(null)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [conversation?.messages, streamingText])

  const handleSend = async (message: string, attachments: Attachment[]) => {
    if (!conversation || !apiKey || streaming) return

    // 사용자 메시지 저장
    addMessage(conversation.id, { role: 'user', content: message, attachments })
    onMessagesUpdate()

    // 스트리밍 시작
    setStreaming(true)
    setStreamingText('')
    setActiveAgent(null)

    const history = conversation.messages.map(m => ({
      role: m.role,
      content: m.content,
    }))

    let fullText = ''
    let usedAgent: AgentKey = 'writing'

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey,
        },
        body: JSON.stringify({ message, history, attachments }),
      })

      const reader = res.body!.getReader()
      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n')
        buffer = lines.pop() ?? ''

        for (const line of lines) {
          if (line.startsWith('event: ')) continue
          if (!line.startsWith('data: ')) continue
          const data = line.slice(6)

          if (data === '[DONE]') break
          if (data.startsWith('error:')) {
            setStreamingText(data.replace('error:', '').trim())
            break
          }

          // 에이전트 선택 이벤트
          if (Object.keys({}).includes(data) || true) {
            const prevLine = lines[lines.indexOf(line) - 1] ?? ''
            if (prevLine === 'event: agent') {
              usedAgent = data as AgentKey
              setActiveAgent(data as AgentKey)
              continue
            }
          }

          fullText += data
          setStreamingText(fullText)
        }
      }

      // AI 메시지 저장
      addMessage(conversation.id, {
        role: 'assistant',
        content: fullText,
        agentsUsed: [usedAgent],
      })
      onMessagesUpdate()
    } catch (err) {
      addMessage(conversation.id, {
        role: 'assistant',
        content: '오류가 발생했습니다. 다시 시도해주세요.',
        agentsUsed: [],
      })
      onMessagesUpdate()
    } finally {
      setStreaming(false)
      setStreamingText('')
      setActiveAgent(null)
    }
  }

  if (!conversation) {
    return (
      <div className="flex-1 flex items-center justify-center bg-zinc-950">
        <div className="text-center space-y-3">
          <p className="text-zinc-500 text-lg font-medium">새 대화를 시작하세요</p>
          <p className="text-zinc-700 text-sm">왼쪽 상단의 "새 대화" 버튼을 눌러주세요</p>
        </div>
      </div>
    )
  }

  const displayMessages: Message[] = [
    ...conversation.messages,
    ...(streaming ? [{
      id: 'streaming',
      role: 'assistant' as const,
      content: streamingText || '...',
      createdAt: new Date().toISOString(),
    }] : []),
  ]

  return (
    <div className="flex-1 flex flex-col bg-zinc-950 h-screen">
      {/* 에이전트 상태 바 */}
      {streaming && activeAgent && (
        <div className="px-6 py-2 border-b border-zinc-800 flex items-center gap-2">
          <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
          <span className="text-zinc-400 text-xs">응답 중:</span>
          <AgentBadge agentKey={activeAgent} />
        </div>
      )}

      {/* 메시지 목록 */}
      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-6">
        {displayMessages.length === 0 && (
          <div className="text-center text-zinc-600 text-sm py-20">
            첫 메시지를 보내보세요
          </div>
        )}
        {displayMessages.map(msg => (
          // MessageItem은 Task 10 Step 2에서 작성
          <div key={msg.id}>{/* MessageItem import 후 교체 */}</div>
        ))}
        <div ref={bottomRef} />
      </div>

      {/* 입력창 */}
      <InputBar onSend={handleSend} disabled={streaming} />
    </div>
  )
}
```

> **Note:** ChatArea의 메시지 렌더링 부분에 MessageItem을 import해 교체한다.
> SSE 파싱 로직에서 `event:` 라인을 추적해 agent/delta/done/error를 구분한다.

**Step 5: 커밋**

```bash
git add components/chat/
git commit -m "feat: 채팅 컴포넌트 (메시지, 입력창, 스트리밍)"
```

---

## Task 11: 메인 페이지 조립

**Files:**
- Modify: `app/page.tsx`
- Modify: `app/layout.tsx`
- Modify: `app/globals.css`

**Step 1: globals.css — 폰트 및 highlight.js 설정**

```css
/* app/globals.css — 기존 내용 유지하고 아래 추가 */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@400;500;600;700&display=swap');

:root {
  --font-poppins: 'Poppins', sans-serif;
  --font-inter: 'Inter', sans-serif;
}

body {
  font-family: var(--font-inter);
  background-color: #09090b;
  color: #fafafa;
}

/* 스크롤바 스타일 */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #3f3f46; border-radius: 2px; }
```

**Step 2: layout.tsx**

```typescript
// app/layout.tsx
import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Business AI Team',
  description: '16명의 전문가 AI 팀이 비즈니스를 도와드립니다',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko" className="dark">
      <body className="antialiased">{children}</body>
    </html>
  )
}
```

**Step 3: page.tsx — 메인 페이지**

```typescript
// app/page.tsx
'use client'
import { useState, useEffect, useCallback } from 'react'
import { AppSidebar } from '@/components/sidebar/AppSidebar'
import { ChatArea } from '@/components/chat/ChatArea'
import { OnboardingModal } from '@/components/onboarding/OnboardingModal'
import {
  getApiKey, getAllConversations, createConversation, getConversation
} from '@/lib/storage/conversations'
import type { Conversation } from '@/lib/types'

export default function HomePage() {
  const [apiKey, setApiKey] = useState<string | null>(null)
  const [showOnboarding, setShowOnboarding] = useState(false)
  const [conversations, setConversations] = useState<Conversation[]>([])
  const [activeId, setActiveId] = useState<string | null>(null)

  const refresh = useCallback(() => {
    setConversations(getAllConversations())
  }, [])

  useEffect(() => {
    const key = getApiKey()
    if (!key) {
      setShowOnboarding(true)
    } else {
      setApiKey(key)
      refresh()
    }
  }, [refresh])

  const activeConversation = activeId ? getConversation(activeId) : null

  const handleNewChat = () => {
    const conv = createConversation()
    refresh()
    setActiveId(conv.id)
  }

  const handleOnboardingComplete = (key: string, firstMessage?: string) => {
    setApiKey(key)
    setShowOnboarding(false)
    refresh()

    // 첫 메시지가 있으면 새 대화 시작
    if (firstMessage) {
      const conv = createConversation()
      refresh()
      setActiveId(conv.id)
      // ChatArea가 마운트된 후 메시지 전달은 URL params 또는 ref로 처리
      // 간단하게: sessionStorage에 임시 저장
      sessionStorage.setItem('pending_message', firstMessage)
    }
  }

  return (
    <div className="flex h-screen overflow-hidden bg-zinc-950">
      {/* 온보딩 모달 */}
      <OnboardingModal
        open={showOnboarding}
        onComplete={handleOnboardingComplete}
      />

      {/* 사이드바 */}
      <AppSidebar
        conversations={conversations}
        activeId={activeId}
        onNewChat={handleNewChat}
        onSelect={id => setActiveId(id)}
        onRefresh={refresh}
      />

      {/* 채팅 영역 */}
      {apiKey && (
        <ChatArea
          conversation={activeConversation}
          apiKey={apiKey}
          onMessagesUpdate={refresh}
        />
      )}
    </div>
  )
}
```

**Step 4: MessageItem import 완성 (ChatArea.tsx 수정)**

ChatArea.tsx의 메시지 렌더링 부분에서 `<div>` 임시 코드를 `MessageItem`으로 교체:

```typescript
// ChatArea.tsx 상단 import 추가
import { MessageItem } from './MessageItem'

// displayMessages.map 내부 교체
{displayMessages.map(msg => (
  <MessageItem key={msg.id} message={msg} />
))}
```

**Step 5: 커밋**

```bash
git add app/
git commit -m "feat: 메인 페이지 조립 (온보딩 + 사이드바 + 채팅)"
```

---

## Task 12: Vercel 배포

**Step 1: GitHub 레포지토리 생성 및 푸시**

```bash
# GitHub에서 새 레포 생성: business-ai-web (public 또는 private)
git remote add origin https://github.com/[username]/business-ai-web.git
git push -u origin main
```

**Step 2: Vercel 연결**

1. [vercel.com](https://vercel.com) 접속 → "Add New Project"
2. GitHub 레포 `business-ai-web` 선택
3. 환경 변수 없음 (API 키는 런타임에 사용자로부터 받음)
4. "Deploy" 클릭

**Step 3: 배포 확인**

```bash
# 배포 URL 확인 (예: business-ai-web.vercel.app)
# 브라우저에서 접속 → 온보딩 모달이 표시되는지 확인
```

**Step 4: 최종 커밋**

```bash
git add .
git commit -m "chore: vercel.json 배포 설정 확인"
git push
```

---

## 빠른 로컬 테스트

```bash
npm run dev
# http://localhost:3000 접속
# 온보딩 → API 키 입력 → 채팅 테스트
```

---

## 완료 체크리스트

- [ ] 온보딩 4단계 모달 정상 작동
- [ ] API 키 유효성 검증 (성공/실패 케이스)
- [ ] 메시지 전송 → 스트리밍 응답
- [ ] 에이전트 뱃지 표시
- [ ] 대화 목록 사이드바 (날짜별 그룹)
- [ ] 새 대화 생성
- [ ] 대화 삭제
- [ ] 파일 첨부 (이미지)
- [ ] 마크다운 렌더링
- [ ] API 키 변경/삭제
- [ ] 모바일 반응형 (사이드바 토글)
- [ ] Vercel 배포 완료
