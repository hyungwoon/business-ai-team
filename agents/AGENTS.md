# AGENTS DIRECTORY

16 lightweight domain routers. Each ~50 lines: system prompt + skill routing table.

## STRUCTURE

All files are flat `[domain].md` — no subdirectories. Each agent file contains:

1. **Title + description** (1 line Korean)
2. **System prompt** (3-5 lines: expertise + principles)
3. **Actions** (capabilities list)
4. **Communication style** (tone + language patterns)
5. **Plugin & skill routing table** (maps request types → plugin → skill)
6. **Output criteria** (quality standards)

## WHERE TO LOOK

| Agent | Domain | Cross-Domain Skills |
|-------|--------|---------------------|
| marketing | Brand, content, campaigns | — |
| sales | Outreach, pipeline, assets | customer-support (ticket-triage, escalation) |
| research | Market research, trends | marketing, sales, data, enterprise-search skills |
| writing | Documents, emails, translation | marketing (brand-voice, content-creation) |
| data | Analysis, visualization, SQL | — |
| finance | Financial analysis, budgets | — |
| legal | Contracts, risk, compliance | enterprise-search (search-strategy) |
| product | Roadmap, specs, metrics | — |
| productivity | Task management, scheduling | — |
| hr | Talent, culture, performance | — |
| design | UX/UI, brand guidelines | — |
| development | Architecture, tech processes | — |
| pr | Press, crisis communications | — |
| security | Cybersecurity, audits | — |
| compliance | Regulations, risk management | — |
| business-dev | Growth, partnerships | — |

## CONVENTIONS

- Routing table format: `| 요청 유형 | 플러그인 | 스킬 |`
- Agent = router, not expert. Expertise lives in `plugins/*/SKILL.md`
- Cross-domain references are explicit (Research → Sales's account-research)
- Communication style includes Korean-specific patterns (conditional language for Legal, etc.)

## ANTI-PATTERNS

- **NEVER** add full expertise content to agent files — keep them as routing metadata
- **NEVER** reference a skill without verifying it exists in `plugins/`
- Agent file is source of truth for routing — CLAUDE.md mapping table is just a guide
