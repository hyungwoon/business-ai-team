# KNOWLEDGE DIRECTORY

RLVR (Reinforcement Learning from Verbal Reasoning) feedback storage. Auto-learns from user corrections during conversations.

## STRUCTURE

```
knowledge/
├── _index.md         # Learning counts per domain (corrections | tips | warnings | rejections | total)
├── preferences.md    # Cross-domain user preferences (format, style, language)
├── writing.md        # Writing domain (pre-existing with learned content)
└── [domain].md       # Other domain files (auto-created on first learning detection)
```

## HOW IT WORKS

1. **Detection**: System auto-detects feedback patterns during conversation
2. **Storage**: Appends row to appropriate domain table + increments `_index.md`
3. **Application**: Read at step 4.5 of request flow — overrides SKILL.md
4. **Reflection**: At 3+ items per domain → auto-reflect to SKILL.md's `## 실무 보정 사항`

## DETECTION PATTERNS

| Category | Table | Triggers |
|----------|-------|----------|
| 정보 보정 (corrections) | `기존 정보 \| 보정 내용 \| 출처` | "아닌데", "틀렸", "바뀌었", "사실은" |
| 실무 노하우 (tips) | `노하우 \| 적용 맥락` | "실무에서는", "경험상", "우리 회사에서는" |
| 주의사항 (warnings) | `주의사항 \| 위험/영향` | "주의해야", "함정이", "절대 하면 안 되는" |
| 거부/불만족 (rejections) | `거부 대상 \| 이유 \| 대안` | "이건 안 써", "필요없어", "다시 해줘", "별로야", "이전 게 나았어" |
| 선호도 (preferences) | → `preferences.md` | "항상 이렇게", "난 이걸 선호", "앞으로는" |

## PRIORITY HIERARCHY

```
knowledge/[domain].md  >  SKILL.md best practices  >  agents/[agent].md system prompt
(most recent feedback)    (established patterns)      (base identity)
```

## ANTI-PATTERNS

- **NEVER** delete items from knowledge/ after reflecting to SKILL.md (preserve audit trail)
- **NEVER** skip reading knowledge/ files during response generation
- Duplicate check: same content → skip; conflicting info → update existing row
- **NEVER** pre-create domain files — let them auto-generate on first learning detection
- Current state: writing.md has 9 learned items; other domains created on demand (system learns incrementally)
