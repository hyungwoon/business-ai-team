#!/bin/bash
# contract-check.sh — Periodic plan adherence check
# Tracks tool use count and triggers verification reminder every N calls
# Called by settings.json: "command": ".claude/hooks/contract-check.sh"

COUNTER_DIR="/Users/hyungwoon/Documents/AI/_core/business-ai-team/.omc/state"
COUNTER_FILE="$COUNTER_DIR/tool-use-counter.txt"
CHECK_INTERVAL=10

# Ensure counter directory exists
mkdir -p "$COUNTER_DIR" 2>/dev/null

# Read current count
if [ -f "$COUNTER_FILE" ]; then
  COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo "0")
else
  COUNT=0
fi

# Increment
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

# Check if it's time for verification
if [ $((COUNT % CHECK_INTERVAL)) -eq 0 ]; then
  cat <<HOOKJSON
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "contract-enforcement.md: ${COUNT} tool calls reached. Periodic plan adherence check:\n1. Are you still aligned with the original plan/requirements?\n2. Have you drifted into scope creep or approximation?\n3. Are downstream consumers of your changes updated?\nIf drifted, stop and report before continuing."
  }
}
HOOKJSON
fi
