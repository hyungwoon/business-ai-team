# PLUGINS DIRECTORY

17 domain plugins containing 112 skills. 10 from Anthropic knowledge-work-plugins, 7 custom-built. product-management expanded to 62 skills (competitive-analysis + competitor-analysis merged) via PM Skills (Paweł Huryn) Korean edition. Plugin skills are also available as native mega-skills via `.claude/skills/` for Claude Code auto-discovery.

## STRUCTURE

```
[domain]/
├── .claude-plugin/plugin.json   # Metadata (name, version, author)
├── .mcp.json                    # MCP server connections (Slack, HubSpot, etc.)
├── README.md                    # Plugin overview + commands + skills list
├── CONNECTORS.md                # MCP integration reference (optional)
├── commands/                    # Slash commands (e.g., /draft-content)
│   └── [command].md
└── skills/                      # Domain expertise
    └── [skill-name]/
        ├── SKILL.md             # Core: YAML frontmatter + frameworks + templates
        ├── references/          # Supporting materials (optional)
        └── examples/            # Usage examples (optional)
```

## WHERE TO LOOK

| Plugin | Origin | Skills | Notes |
|--------|--------|--------|-------|
| marketing | Anthropic | brand-voice, content-creation, campaign-planning, competitive-analysis, performance-analytics | 7 commands |
| sales | Anthropic | draft-outreach, create-an-asset, daily-briefing, account-research, competitive-intelligence, call-prep | Standalone skills |
| data | Anthropic | data-exploration, data-visualization, statistical-analysis, sql-queries, data-validation, data-context-extractor, interactive-dashboard-builder | Has scripts/ + references/ |
| finance | Anthropic+custom | financial-analysis, financial-statements, variance-analysis, journal-entry-prep, reconciliation, audit-support, close-management | 7 skills |
| legal | Anthropic | contract-review, legal-risk-assessment, compliance, nda-triage, canned-responses, meeting-briefing | Playbook-based review |
| product-management | Anthropic + PM Skills (Paweł Huryn) | 62 skills: [pm-discovery] brainstorm-ideas-*, identify-assumptions-*, prioritize-*, opportunity-solution-tree, interview-*, summarize-interview [pm-strategy] product-strategy, lean-canvas, business-model, pricing-strategy, swot-analysis, pestle-analysis, porters-five-forces, ansoff-matrix, product-vision, value-proposition, startup-canvas, monetization-strategy [pm-execution] create-prd, brainstorm-okrs, outcome-roadmap, sprint-plan, retro, release-notes, pre-mortem, stakeholder-map, summarize-meeting, user-stories, job-stories, wwas, test-scenarios, dummy-dataset, prioritization-frameworks [pm-core] roadmap-management, metrics-tracking, stakeholder-comms [pm-research] user-personas, market-segments, user-segmentation, customer-journey-map, market-sizing, competitor-analysis, sentiment-analysis [pm-gtm] gtm-strategy, beachhead-segment, ideal-customer-profile, growth-loops, gtm-motions, competitive-battlecard, positioning-ideas, value-prop-statements, product-name [pm-analytics] cohort-analysis, ab-test-analysis | 31 commands, 12 MCP connectors; 7 mega-skills in .claude/skills/ |
| customer-support | Anthropic | ticket-triage, response-drafting, customer-research, escalation, knowledge-management | Cross-referenced by Sales |
| productivity | Anthropic | task-management, memory-management | Persistent memory system |
| enterprise-search | Anthropic | search-strategy, knowledge-synthesis, source-management | Source-agnostic |
| cowork-plugin-management | Anthropic | cowork-plugin-customizer, create-cowork-plugin | Has examples/ + references/ |
| business-dev | Custom | growth-strategy | — |
| compliance | Custom | risk-management | — |
| development | Custom | tech-leadership | — |
| design | Custom | ux-design | — |
| hr | Custom | talent-management | — |
| pr | Custom | communications | Crisis response anti-patterns |
| security | Custom | cybersecurity | Incident response protocols |

## SKILL.MD FORMAT

```yaml
---
name: skill-name        # kebab-case, matches folder
description: When to use # Trigger patterns
---
# Skill Name
[Core frameworks/methodology]
[Detailed guidance with tables]
[Templates with [CUSTOMIZE] markers]
[Configuration sections]
```

Size range: 69-900 lines. Custom plugins tend shorter (~150-200), Anthropic plugins longer (300-900). PM Skills (product-management) skills are Korean, 69-275 lines each.

## CONVENTIONS

- Skill names: kebab-case, action-oriented
- SKILL.md is the ONLY file agents read — README.md and commands/ are supplementary
- Skills degrade gracefully without MCP connectors
- Cross-domain sharing: skills are referenced by multiple agents (competitive-analysis used by Marketing, Research; Product uses own competitor-analysis)

## ANTI-PATTERNS

- **NEVER** add agent-specific logic to SKILL.md — skills are domain-generic
- **NEVER** modify SKILL.md without checking if `knowledge/` has corrections to preserve
- Custom plugins (7) have fewer skills — extend them rather than creating new plugins
