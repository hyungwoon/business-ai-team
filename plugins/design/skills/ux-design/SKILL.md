---
name: ux-design
description: Apply UX research, information architecture, interaction design, and usability principles to product and service design. Use when planning user research, reviewing design decisions, writing UX specifications, evaluating usability, or defining design systems.
version: 2.0.0
last-updated: 2026-03-15
---

# UX Design Skill

Frameworks for user experience research, design strategy, interaction design, and design system governance.

## UX Research Methods

### Method Selection by Research Question

| Question Type | Recommended Method | Output |
|---|---|---|
| What do users need? | In-depth interview (IDI) | Jobs-to-be-done, pain points |
| How do users behave? | Contextual inquiry, session recording | Usage patterns, friction points |
| Which design works better? | A/B test, preference test | Quantified conversion lift |
| Can users complete tasks? | Usability test (moderated) | Task completion rate, error rate |
| What is sentiment at scale? | Survey (NPS, CSAT, SUS) | Benchmark scores, trends |
| Why do users leave? | Exit survey, funnel analysis | Drop-off reasons |

### Interview Guide Template

**Screener criteria:** [Define target user profile]

**Warm-up (5 min):**
- Tell me about your role and how you spend most of your day.
- How long have you been using [product category]?

**Core questions (30-40 min):**
- Walk me through the last time you [target task]. Start from the very beginning.
- What were you trying to accomplish at that point?
- What made that hard / easy?
- What workarounds, if any, did you use?
- If you had a magic wand to change one thing, what would it be?

**Closing (5 min):**
- Is there anything I haven't asked that you think would be useful for us to know?

**Analysis:** Affinity clustering → themes → insights → design opportunities

---

## Information Architecture

### Card Sorting

Use **open card sort** when exploring how users naturally categorize content.
Use **closed card sort** when validating a proposed navigation structure.

**Optimal Workshop / Maze** are standard tools. Aim for 20–30 participants for quantitative reliability.

**Analysis output:** Similarity matrix → dendrogram → proposed IA with confidence scores

### Navigation Patterns

| Pattern | Best For | Consideration |
|---|---|---|
| Top navigation bar | Desktop, 5-8 top-level sections | Collapses poorly on mobile |
| Left sidebar | Complex apps, many sections | Takes horizontal space |
| Bottom tab bar | Mobile, 3-5 primary sections | iOS/Android standard |
| Hamburger menu | Mobile supplemental navigation | Low discoverability |
| Hub & spoke | Task-focused apps, deep flows | No cross-section shortcut |
| Search-first | Large catalogs, expert users | Requires good search quality |

---

## Interaction Design Principles

### Heuristics (Nielsen's 10 + Korean UX context)

1. **Visibility of system status** — Always show what is happening (loading states, progress, success/error)
2. **Match between system and real world** — Use language and metaphors familiar to Korean users; avoid jargon
3. **User control and freedom** — Easy undo, cancel, and back navigation
4. **Consistency and standards** — Follow platform conventions (iOS HIG, Material Design, Korean web norms)
5. **Error prevention** — Validate inputs before submission; warn before destructive actions
6. **Recognition over recall** — Surface options; don't require memorization
7. **Flexibility and efficiency** — Power-user shortcuts (keyboard shortcuts, bulk actions)
8. **Aesthetic and minimalist design** — Remove non-essential elements; prioritize content hierarchy
9. **Help users recognize and recover from errors** — Plain-language error messages with recovery steps
10. **Help and documentation** — Contextual help; Korean-language support materials

**Korean UX specifics:**
- Mobile-first: Korea has highest mobile usage density globally; design for thumb reach zones
- App fatigue: Users compare against KakaoTalk, Naver, Coupang — high baseline expectations
- Trust signals: Company registration number, customer service number, and physical address increase conversion

### Micro-interaction Patterns

| Trigger | Animation | Duration | Purpose |
|---|---|---|---|
| Button tap | Scale 0.97 → 1.0 | 100ms | Physical feedback |
| Form error | Shake + red border | 300ms | Draw attention |
| Success action | Checkmark + fade | 400ms | Confirm completion |
| Loading | Skeleton screen | Until data loads | Prevent layout shift |
| Destructive confirm | Slide-up modal | 250ms | Prevent accidents |

---

## Usability Testing

### Test Plan Template

**Objective:** [What design decisions will this test inform?]
**Participants:** [Number, screener criteria, recruitment method]
**Tasks:**
1. Task 1: [Specific, realistic scenario — no leading language]
2. Task 2: ...

**Metrics:**
- Task completion rate (binary: completed / not completed)
- Time on task
- Error rate (# of errors per task attempt)
- SUS score (post-test survey)
- Qualitative: verbal reactions, confusion moments

**Severity classification for issues found:**
| Severity | Definition | Fix Priority |
|---|---|---|
| Critical | Prevents task completion | Before launch |
| Major | Causes significant delay or frustration | Next sprint |
| Minor | Cosmetic or slight confusion | Backlog |

---

## Design System

### Component Documentation Standard

Each component should document:

```
Component: [Name]
Status: Stable / Beta / Deprecated

Usage: When to use vs. when NOT to use

Props / Variants:
  - variant: primary | secondary | ghost | danger
  - size: sm | md | lg
  - state: default | hover | active | disabled | loading

Accessibility:
  - Role: button / link / etc.
  - Keyboard: Tab to focus, Enter/Space to activate
  - ARIA: aria-label required for icon-only buttons
  - Color contrast: 4.5:1 minimum (WCAG AA)

Do / Don't:
  ✅ Use primary for one main CTA per page
  ❌ Use multiple primary buttons in the same view
```

### Design Token Structure

```
color/
  brand/primary     → #6366F1
  brand/secondary   → #818CF8
  semantic/success  → #10B981
  semantic/error    → #EF4444
  semantic/warning  → #F59E0B
  neutral/900       → #18181B
  neutral/500       → #71717A

spacing/
  xs  → 4px
  sm  → 8px
  md  → 16px
  lg  → 24px
  xl  → 32px
  2xl → 48px

typography/
  heading/xl  → Poppins 32px/1.25 SemiBold
  heading/lg  → Poppins 24px/1.3 SemiBold
  body/md     → Inter 16px/1.6 Regular
  body/sm     → Inter 14px/1.5 Regular
  label/md    → Inter 14px/1.4 Medium
```

---

## Design Sprint Methodology (5-Day Process)

A Design Sprint compresses months of work into one week. Use when facing a critical design decision, entering a new market, or validating a risky assumption before building.

### Day-by-Day Activities

**Day 1 — Understand (Map)**

Goal: Align the team on the problem and pick a target.

| Activity | Duration | Output |
|---|---|---|
| Long-term goal setting | 30 min | "In 2 years, we want to..." |
| Sprint questions (what could go wrong?) | 30 min | Risk list |
| Expert interviews (내부 전문가 인터뷰) | 2 hours | Knowledge map |
| How Might We (HMW) notes | 30 min | HMW sticky notes |
| Affinity clustering of HMWs | 30 min | Clustered opportunity areas |
| Journey map creation | 1 hour | End-to-end user journey |
| Target selection vote | 30 min | Chosen moment on the map |

**Day 2 — Sketch (Diverge)**

Goal: Generate a wide range of competing solutions.

| Activity | Duration | Output |
|---|---|---|
| Lightning demos (competitor / analogous inspiration) | 1 hour | Inspiration notes |
| 4-part sketching: Notes → Ideas → Crazy 8s → Solution sketch | 3 hours | Individual solution sketches |
| Silent critique (dot voting on sketches) | 30 min | Voted sketches |
| Speed critique | 30 min | Annotated sketches |
| Straw poll + decider vote | 15 min | Winning concept(s) |

**Day 3 — Decide (Converge)**

Goal: Turn competing ideas into a single testable prototype plan.

| Activity | Duration | Output |
|---|---|---|
| Rumble or all-in-one decision | 30 min | Chosen direction |
| Storyboard (15-20 frames) | 3 hours | Panel-by-panel prototype plan |
| User test script draft | 1 hour | Interview guide for Day 5 |

**Day 4 — Prototype**

Goal: Build a realistic-looking prototype — not a real product.

| Activity | Duration | Output |
|---|---|---|
| Assign roles: Makers, Stitcher, Writer, Asset collector, Interviewer | 15 min | Role assignments |
| Build in Figma / Keynote / Marvel | 5-6 hours | Clickable prototype |
| Trial run with team | 30 min | Refined prototype |
| Finalize interview script | 30 min | Ready-to-use script |

**Day 5 — Test**

Goal: Learn from 5 real users. Five interviews reveal 85% of usability issues.

| Activity | Duration | Output |
|---|---|---|
| User interviews (5 sessions × 60 min) | 5 hours | Recorded sessions |
| Live note-taking by observers | During interviews | Observation notes |
| Debrief and pattern finding | 1 hour | Themes: hits, misses, questions |
| Decision: go, iterate, or pivot | 30 min | Next step recommendation |

---

## Design-to-Dev Handoff Checklist

A complete handoff prevents back-and-forth and reduces implementation bugs.

### Figma File Preparation
- [ ] All layers named descriptively (no "Rectangle 47" or "Group 12")
- [ ] Components used consistently — no one-off overrides without annotation
- [ ] Auto-layout applied to all responsive elements
- [ ] Variants defined for all interactive states (default, hover, active, disabled, loading, error)
- [ ] Design tokens linked (colors, spacing, typography from shared library)
- [ ] Prototype flows connected for key user journeys

### Specification Completeness
- [ ] Spacing values annotated (or readable from auto-layout)
- [ ] Typography specs: font, size, weight, line-height, letter-spacing
- [ ] Color values in hex / design token names
- [ ] Icon sizes and source library specified
- [ ] Animation specs: duration, easing, trigger (see Motion section)
- [ ] Responsive behavior documented for each breakpoint
- [ ] Empty states, error states, loading states all designed

### Accessibility Annotations
- [ ] Focus order annotated for keyboard navigation
- [ ] ARIA labels specified for icon-only buttons and form inputs
- [ ] Color contrast ratios verified (4.5:1 for normal text, 3:1 for large text)
- [ ] Touch target sizes: minimum 44×44px (iOS) / 48×48dp (Android)

### Developer Handoff Meeting Agenda
```
1. Walk through user flow (10 min) — designer leads
2. Component inventory (10 min) — what's in the library vs. net new
3. Edge cases and states (15 min) — what happens when data is empty, long, or errored
4. Open questions (10 min) — resolve ambiguities before build starts
5. Acceptance criteria (5 min) — how will we know it's done correctly?
```

---

## Accessibility Audit Checklist (KWCAG 2.2)

한국 웹 접근성 지침 (KWCAG 2.2)은 장애인차별금지법에 따라 공공기관 및 민간 웹사이트에 적용됩니다.

### 인식의 용이성 (Perceivable)

- [ ] **1.1 대체 텍스트** — 모든 이미지에 의미 있는 alt 텍스트 제공 (장식용 이미지는 alt="")
- [ ] **1.2 멀티미디어 대체 수단** — 영상에 자막 또는 원고 제공
- [ ] **1.3 색에 무관한 콘텐츠** — 색상만으로 정보를 전달하지 않음 (아이콘 + 텍스트 병행)
- [ ] **1.4 명도 대비** — 일반 텍스트 4.5:1 이상, 큰 텍스트 3:1 이상
- [ ] **1.5 자동 재생 금지** — 3초 이상 자동 재생 콘텐츠는 정지/음소거 기능 제공

### 운용의 용이성 (Operable)

- [ ] **2.1 키보드 접근성** — 모든 기능을 키보드만으로 사용 가능
- [ ] **2.2 초점 이동** — 키보드 초점이 논리적 순서로 이동, 초점 표시 명확
- [ ] **2.3 충분한 시간** — 시간 제한 콘텐츠에 연장/해제 옵션 제공
- [ ] **2.4 광과민성 발작 예방** — 초당 3회 이상 깜빡이는 콘텐츠 금지
- [ ] **2.5 건너뛰기 링크** — 반복 내비게이션을 건너뛸 수 있는 링크 제공

### 이해의 용이성 (Understandable)

- [ ] **3.1 기본 언어 표시** — HTML lang 속성으로 페이지 언어 명시 (lang="ko")
- [ ] **3.2 사용자 요구에 따른 실행** — 포커스 이동만으로 컨텍스트 변경 금지
- [ ] **3.3 레이블 제공** — 모든 입력 필드에 레이블 연결 (label for 또는 aria-label)
- [ ] **3.4 오류 정정** — 입력 오류 시 오류 내용과 수정 방법 안내

### 견고성 (Robust)

- [ ] **4.1 마크업 오류 방지** — 유효한 HTML, 중복 id 없음
- [ ] **4.2 웹 애플리케이션 접근성** — 동적 콘텐츠에 ARIA 역할/속성/상태 적용

### 자동화 검사 도구

| 도구 | 용도 | 비고 |
|---|---|---|
| axe DevTools | 브라우저 확장 — 자동 접근성 검사 | 무료 버전 사용 가능 |
| Lighthouse | Chrome DevTools 내장 접근성 점수 | CI/CD 파이프라인 통합 가능 |
| WAVE | 시각적 접근성 오류 표시 | 웹 기반 도구 |
| Colour Contrast Analyser | 색상 대비 측정 | 데스크톱 앱 (무료) |

---

## Design Critique Framework

Structured critique produces actionable feedback. Unstructured critique produces hurt feelings and vague revisions.

### Critique Session Structure (60 min)

```
1. Context setting by presenter (5 min)
   - What problem are we solving?
   - Who is the user?
   - What stage is this? (Concept / Wireframe / High-fidelity / Final)
   - What specific feedback do you need?

2. Silent observation (5 min)
   - Reviewers look at the design without speaking
   - Write observations on sticky notes (physical or digital)

3. Presenter walkthrough (10 min)
   - Walk through the design and key decisions
   - No defending yet — just explaining

4. Structured feedback round (30 min)
   - Each reviewer shares: one thing that works well + one question or concern
   - Feedback format: "I notice [observation]. I wonder [question]."
   - Avoid: "I like / I don't like" — focus on user impact

5. Discussion and prioritization (10 min)
   - Presenter identifies top 3 feedback items to act on
   - Agree on next steps and timeline
```

### Feedback Quality Standards

| Good Feedback | Poor Feedback |
|---|---|
| "The error message doesn't tell the user what to do next" | "This looks bad" |
| "Users might not notice the CTA — it competes with the banner" | "Make the button bigger" |
| "The onboarding flow has 7 steps — research shows drop-off after 3" | "Too many steps" |
| "This pattern differs from our design system's modal component" | "I don't like modals" |

---

## Design KPI Framework (Google HEART)

HEART provides a structured way to measure UX quality at scale.

| Dimension | Definition | Example Metrics |
|---|---|---|
| **Happiness** | Subjective satisfaction | NPS, CSAT, SUS score, app store rating |
| **Engagement** | Depth of interaction | Sessions per user per week, features used per session |
| **Adoption** | New users or features | % users who tried new feature within 30 days, activation rate |
| **Retention** | Return usage | D7/D30 retention, churn rate, subscription renewal rate |
| **Task success** | Efficiency and effectiveness | Task completion rate, time on task, error rate |

### HEART Metric Definition Template

```
Metric: [NAME]
Dimension: [Happiness / Engagement / Adoption / Retention / Task success]
Signal: [User behavior or attitude that indicates this]
Metric: [How we measure it — specific formula]
Baseline: [Current value]
Target: [Goal value + timeframe]
Data source: [Analytics tool / survey / usability test]
Owner: [Team or person responsible]
```

### HEART Dashboard (Quarterly Review)

```
Product: [PRODUCT NAME]
Period: [QUARTER]

HAPPINESS
  NPS:          [SCORE] (target: [TARGET])
  CSAT:         [SCORE] (target: [TARGET])
  App rating:   [SCORE] / 5.0

ENGAGEMENT
  DAU/MAU ratio:        [%] (stickiness)
  Avg. sessions/user/week: [COUNT]
  Core feature usage:   [%] of active users

ADOPTION
  New feature adoption (30-day): [%]
  Activation rate:      [%]

RETENTION
  D7 retention:         [%]
  D30 retention:        [%]
  Monthly churn:        [%]

TASK SUCCESS
  Core task completion: [%]
  Avg. time on task:    [SECONDS]
  Error rate:           [%]
```

---

## Design System Governance Model

### Contribution Process

Anyone on the product team can contribute to the design system. The process ensures quality without creating a bottleneck.

```
1. Propose (Designer)
   - Open a contribution request in the design system Figma file
   - Include: use case, proposed component, rationale for why existing components don't cover it

2. Review (Design System Team)
   - Assess: Is this truly reusable (3+ use cases) or a one-off?
   - Check: Does it conflict with existing components?
   - Decision: Accept / Reject / Merge with existing component

3. Design (Contributor + Design System Team)
   - Design all variants and states
   - Write usage guidelines and do/don't examples
   - Accessibility review

4. Build (Engineering)
   - Implement in component library
   - Write unit tests and Storybook stories
   - Accessibility testing (axe, keyboard, screen reader)

5. Release
   - Version bump (see versioning below)
   - Announce in #design-system channel with migration guide if breaking
   - Update documentation site
```

### Versioning Policy

Follow semantic versioning (MAJOR.MINOR.PATCH):

| Change Type | Version Bump | Example |
|---|---|---|
| Breaking change (removed or renamed component) | MAJOR (v2.0.0) | Button renamed to PrimaryButton |
| New component or non-breaking new variant | MINOR (v1.3.0) | Added DatePicker component |
| Bug fix, visual tweak, documentation update | PATCH (v1.2.1) | Fixed hover state color |

### Deprecation Process

```
1. Mark component as Deprecated in Figma (status badge)
2. Add deprecation notice to documentation with:
   - Reason for deprecation
   - Replacement component (if any)
   - Migration guide
3. Keep deprecated component for minimum 2 major versions
4. Announce in #design-system with 90-day removal timeline
5. Remove after timeline expires
```

---

## Motion Design Principles & Timing Guidelines

Motion communicates state changes, guides attention, and provides feedback. Use it purposefully.

### Core Principles

1. **Purposeful** — Every animation must serve a function (feedback, orientation, or focus). Remove decorative motion.
2. **Responsive** — Motion should feel instant. Delays > 400ms feel sluggish.
3. **Natural** — Use easing curves that mimic physical objects (ease-out for entering, ease-in for exiting).
4. **Respectful** — Honor `prefers-reduced-motion` media query for users with vestibular disorders.

### Timing Reference

| Use Case | Duration | Easing |
|---|---|---|
| Micro-interactions (button press, toggle) | 100-150ms | ease-out |
| Small element transitions (tooltip, dropdown) | 150-200ms | ease-out |
| Page-level transitions | 250-350ms | ease-in-out |
| Large modal / sheet entry | 300-400ms | cubic-bezier(0.16, 1, 0.3, 1) — spring-like |
| Loading / skeleton reveal | 400-600ms | ease-in-out |
| Celebration / success animation | 600-800ms | spring |

### Easing Cheat Sheet

```css
/* Entering elements — decelerate into position */
ease-out: cubic-bezier(0, 0, 0.2, 1)

/* Exiting elements — accelerate out */
ease-in: cubic-bezier(0.4, 0, 1, 1)

/* Elements moving within the screen */
ease-in-out: cubic-bezier(0.4, 0, 0.2, 1)

/* Spring-like — for modals, drawers, overlays */
spring: cubic-bezier(0.16, 1, 0.3, 1)
```

### Reduced Motion Implementation

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Responsive Breakpoint Strategy

### Breakpoint System

| Breakpoint | Name | Min Width | Typical Device |
|---|---|---|---|
| xs | Mobile S | 320px | Small phones (iPhone SE) |
| sm | Mobile | 375px | Standard phones |
| md | Tablet | 768px | iPad portrait, large phones landscape |
| lg | Desktop S | 1024px | iPad landscape, small laptops |
| xl | Desktop | 1280px | Standard laptops |
| 2xl | Desktop L | 1440px | Large monitors |

### Layout Grid by Breakpoint

| Breakpoint | Columns | Gutter | Margin |
|---|---|---|---|
| xs / sm | 4 | 16px | 16px |
| md | 8 | 24px | 24px |
| lg | 12 | 24px | 32px |
| xl / 2xl | 12 | 32px | 48px |

### Korean Mobile-First Considerations

Korea's mobile usage patterns differ from global norms:

- **Bottom navigation preferred** — KakaoTalk, Naver, Coupang all use bottom tab bars. Users expect primary navigation at thumb reach.
- **Thumb zone design** — Primary actions should sit in the bottom 60% of the screen. Avoid placing critical CTAs in the top corners.
- **Dense information layouts** — Korean users tolerate higher information density than Western users. Naver's homepage is a reference point.
- **Safe area insets** — Account for iPhone notch and Android gesture navigation bar using `env(safe-area-inset-*)`.

### Responsive Component Checklist

For each component, verify behavior at every breakpoint:

- [ ] Text does not overflow or truncate unexpectedly
- [ ] Images scale correctly (aspect ratio preserved)
- [ ] Touch targets meet minimum size (44×44px)
- [ ] Navigation collapses gracefully (hamburger or bottom bar)
- [ ] Tables reflow to card layout on mobile
- [ ] Forms stack vertically on small screens
- [ ] Modals use full-screen on mobile (not floating)
- [ ] Horizontal scroll is intentional, not accidental
