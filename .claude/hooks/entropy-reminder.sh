#!/bin/bash
# entropy-reminder.sh — Stop hook
# Reminds to run entropy cleanup before session end
# Called by settings.json: "command": ".claude/hooks/entropy-reminder.sh"

INPUT=$(cat)

STOP_REASON=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('stop_reason', ''))
except:
    print('')
" 2>/dev/null)

# Only intercept assistant-initiated stops
if [ "$STOP_REASON" = "user" ]; then
  exit 0
fi

cat <<'HOOKJSON'
{
  "decision": "block",
  "reason": "[business-ai-team] Session closing checklist required before stop.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "session-closing.md mandatory checklist:\n0. Learning knowledge reflection\n0.5. Entropy cleanup (stale comments, unused imports, doc sync)\n0.7. Telemetry recording\n0.8. Handoff prompt (if incomplete tasks)\n1. _context.md update\n2-5. Stage, commit, push, verify"
  }
}
HOOKJSON
