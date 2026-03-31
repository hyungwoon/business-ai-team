#!/bin/bash
# complexity-check.sh — PostToolUse Edit hook
# Detects TODO/stub/placeholder patterns in edited code
# Called by settings.json: "command": ".claude/hooks/complexity-check.sh"

INPUT=$(cat)

# Extract tool_input.new_string or tool_input.content
NEW_CONTENT=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    ti = data.get('tool_input', {})
    print(ti.get('new_string', '') or ti.get('content', '') or '')
except:
    print('')
" 2>/dev/null)

if [ -z "$NEW_CONTENT" ]; then
  exit 0
fi

# Check for anti-patterns
FOUND=""
echo "$NEW_CONTENT" | grep -iE '//\s*TODO:\s*implement' >/dev/null 2>&1 && FOUND="$FOUND\n- // TODO: implement"
echo "$NEW_CONTENT" | grep -iE 'throw new Error\(.*(Not implemented|not yet)' >/dev/null 2>&1 && FOUND="$FOUND\n- throw new Error('Not implemented')"
echo "$NEW_CONTENT" | grep -iE '//\s*\.\.\.\s*(rest|existing)\s*(of\s*)?(the\s*)?code' >/dev/null 2>&1 && FOUND="$FOUND\n- // ... rest of code"
echo "$NEW_CONTENT" | grep -iE '//\s*(add your code here|implement this|placeholder)' >/dev/null 2>&1 && FOUND="$FOUND\n- placeholder comment"

if [ -n "$FOUND" ]; then
  cat <<HOOKJSON
{
  "decision": "block",
  "reason": "[business-ai-team] Stub/TODO pattern detected. Replace with actual implementation.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "complexity-decomposer.md: Stub code detected. If the task is complex, decompose into subtasks — but each subtask must contain real implementation. TODO/placeholder patterns are blocked."
  }
}
HOOKJSON
fi
