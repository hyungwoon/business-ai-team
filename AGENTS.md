# PROJECT KNOWLEDGE BASE

**Generated:** 2026-03-15
**Commit:** fb48154
**Branch:** main

## OVERVIEW

16 AI agents + 31 Claude Code 네이티브 스킬(.claude/skills/). 110+ plugin skills + gstack 엔지니어링 워크플로우. RLVR 능동적 학습 + 세션 리마인드.

## STRUCTURE

```
business-ai-team/
├── CLAUDE.md              # Master config: agent mapping table, session rules
├── agents/                # 16 domain agents (lightweight routers)
├── plugins/               # 17 domain plugins, 110+ skills (best practices)
├── knowledge/             # RLVR feedback storage (auto-learning)
├── .claude/skills/        # 31 native skills (23 business + 8 engineering)
├── .claude/rules/         # 4 rules (expert-routing, brainstorming, feedback-learning, session-reminder)
├── .claude/commands/      # 5 commands (/ask, /route, /team, /improve, /health)
└── projects/              # Client deliverables (LOCAL ONLY)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Understand request flow | `CLAUDE.md` lines 82-107 | 6-stage pipeline diagram |
| Add/modify an agent | `agents/[domain].md` | ~50 lines: system prompt + skill routing table |
| Add/modify a skill | `plugins/[domain]/skills/[skill]/SKILL.md` | 69-900 lines: frameworks + templates |
| Check learned corrections | `knowledge/[domain].md` | 4 tables: corrections, tips, warnings, rejections |
| Modify routing rules | `.claude/rules/expert-routing.md` | Mandatory procedures + forbidden actions + domain boundary routing |
| Modify brainstorming gate | `.claude/rules/requirements-brainstorming.md` | 심층 인터뷰 게이트 (2축 분류 + 7개 인터뷰 기법, 질문 수 무제한) |
| Modify feedback detection | `.claude/rules/feedback-learning.md` | 5종 감지 패턴 (정보 보정, 실무 노하우, 주의사항, 거부 기록, 선호도) |
| Review learning status | `knowledge/_index.md` | Domain counts; `/improve` command |
| Resume a project | `projects/[name]/_context.md` | Always read first before working |
| Use native skills | `.claude/skills/[name]/SKILL.md` | 31 mega-skills — 비즈니스 라우터는 plugins/ 직접 참조, gstack은 자체 완결 |
| Check project health | `/health` command | Size, duplicates, learning status, structure |
| Configure session reminders | `.claude/rules/session-reminder.md` | Auto-load preferences, context, learning at session start |

## REQUEST FLOW

```
User Request
  → [0.5] Check projects/_context.md (skip gate if continuation)
  → [1] Brainstorming Gate (A=full, B=light, C=1 question, D=direct)
  → [2] Domain Classification (CLAUDE.md mapping table)
  → [3] Read agents/[domain].md (MANDATORY — never from memory)
  → [4] Read plugins/.../SKILL.md (MANDATORY)
  → [4.5] Read knowledge/[domain].md + preferences.md
  → [5] Generate response (knowledge overrides SKILL.md)
  → [6] Prepend "> **담당**: [Agent] | 참조 스킬: [Skill]"
  → [RLVR] Auto-detect feedback → store in knowledge/
```

## CONVENTIONS

- **Language**: Korean primary, English/Korean mixed in plugin SKILL.md files (product-management is Korean)
- **Agent files**: Lightweight routing metadata (~50-120 lines), NOT full system prompts
- **Skill files**: YAML frontmatter (name, description) + markdown content
- **File naming**: `YYYY-MM-DD_[description].md` for all project deliverables
- **Context files**: `_context.md` mandatory in every project folder (underscore prefix for sort-first)
- **Cross-domain skills**: Agents can reference skills from other plugins (e.g., Research uses Sales's account-research)
- **Plugin origin**: 10 from Anthropic knowledge-work-plugins, 7 custom-built
- **PM Skills**: product-management plugin expanded to 62 skills via PM Skills (Paweł Huryn) Korean edition integration
- **Native skills**: `.claude/skills/` — 23 business mega-skills (router → plugins/ 직접 참조) + 8 engineering skills (gstack-based, 자체 완결)
- **PM mega-skills**: 62 skills grouped into 7 mega-skills (pm-discovery, pm-strategy, pm-execution, pm-core, pm-research, pm-gtm, pm-analytics)

## ANTI-PATTERNS (THIS PROJECT)

- **NEVER** generate business response without reading `agents/[agent].md` file
- **NEVER** provide domain expertise without reading the corresponding `SKILL.md`
- **NEVER** deliver response without `> **담당**:` attribution header
- **NEVER** substitute memory/estimation for reading agent files
- **NEVER** use `git add .` — always stage specific files (projects/ leak risk)
- **NEVER** push `projects/` folder to git
- **NEVER** end session without updating `_context.md` for worked projects
- **NEVER** skip session-end git push after system file changes
- **NEVER** delete from `knowledge/` after SKILL.md reflection (preserve history)

## UNIQUE STYLES

- **Agents as routers**: Agents contain routing tables to skills, not full expertise
- **Mandatory file reads**: System enforces `Read` tool calls — no memory/estimation
- **RLVR learning**: Auto-detects user corrections ("아닌데", "실무에서는", "주의해야") + rejections ("이건 안 써", "필요없어", "다시 해줘") → stores in knowledge/
- **3-item threshold**: When domain accumulates 3+ feedback items → auto-reflect to SKILL.md
- **Priority hierarchy**: knowledge/ corrections > SKILL.md best practices > agent system prompt
- **Dual-path resolution**: Local agents/ first, falls back to `~/.claude/business-team/agents/`
- **Brainstorming gate escape**: "바로 해줘", "알아서 해줘", "급해" → skip gate

## COMMANDS

```bash
# Slash commands (in Claude Code CLI)
/ask [question]     # Quick expert routing (simplified /route)
/route [request]    # Full routing with brainstorming gate
/team               # List all agents and skills
/improve            # Review learning feedback, reflect to SKILL.md
/health             # Project health dashboard (size, duplicates, structure)
```

## NOTES

- `projects/` is in `.gitignore` but verify no accidental staging before push
- Knowledge: Writing domain has 9 learned items (형운 voice profile), preferences has 8 items. Other domains at 0 — system learns incrementally through use
- Multi-agent composition: complex requests route to 2-5 agents (e.g., "시리즈A 투자 준비" → Finance + Legal + BizDev + Product)
- Session-end checklist overrides ALL other rules — mandatory push after system changes
- Same project, different request direction → re-run brainstorming gate
- Dual-skill sync: 13 router skills have "참조 원본" section linking to agents/ as single source of truth
- Cross-plugin discoverability: 10 core plugin skills have "관련 스킬" cross-reference tables
- Architecture visualization: `architecture.html` — request flow, 4-layer diagram, agent routing map
- Custom plugin v2.0: 7 custom plugins expanded from avg 176줄 → avg 575줄 (3.3x depth increase)
