# PLUGINS DIRECTORY

17 domain plugins containing 56 skills. 10 from Anthropic knowledge-work-plugins, 7 custom-built.

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
| product-management | Anthropic | roadmap-management, feature-spec, user-research-synthesis, competitive-analysis, metrics-tracking, stakeholder-comms | 6 commands |
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

Size range: 150-900 lines. Custom plugins tend shorter (~150-200), Anthropic plugins longer (300-900).

## CONVENTIONS

- Skill names: kebab-case, action-oriented
- SKILL.md is the ONLY file agents read — README.md and commands/ are supplementary
- Skills degrade gracefully without MCP connectors
- Cross-domain sharing: skills are referenced by multiple agents (competitive-analysis used by Marketing, Research, Product)

## ANTI-PATTERNS

- **NEVER** add agent-specific logic to SKILL.md — skills are domain-generic
- **NEVER** modify SKILL.md without checking if `knowledge/` has corrections to preserve
- Custom plugins (7) have fewer skills — extend them rather than creating new plugins
