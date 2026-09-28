#!/usr/bin/env bash
# PreToolUse hook for Write. Blocks creating a NEW UI source file unless a design
# decision was recorded recently. Edits to existing files are always allowed, so minor
# changes are never blocked. Exit code 2 blocks the call and shows stderr to Claude.
#
# Adjust UI_PATTERN and WINDOW_MIN to fit the project.
UI_PATTERN='(^|/)(src/)?(app|pages|components|views|screens|ui|routes)/.*\.(tsx|jsx|vue|svelte|astro|html|css|scss)$'
WINDOW_MIN=720   # a decision file touched in the last 12 hours unlocks new UI files

input=$(cat)
file=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty')
[ -z "$file" ] && exit 0

# The design board and decision files are always allowed.
case "$file" in */design/*|design/*) exit 0 ;; esac

# Only gate UI files that do not exist yet.
printf '%s' "$file" | grep -qE "$UI_PATTERN" || exit 0
[ -e "$file" ] && exit 0

root="${CLAUDE_PROJECT_DIR:-.}"
if find "$root/design/decisions" -name "*.md" -mmin "-$WINDOW_MIN" 2>/dev/null | grep -q .; then
  exit 0
fi

cat >&2 <<EOF
Design gate: you are creating a new UI file ($file) but no design decision has been
recorded. For a new design or major change, first add a feature section to the design
board at design/board/index.html with up to 3 high-fidelity options, republish it, and
let the user pick. Record the pick on the board and in design/decisions/<feature-slug>.md,
then build. If this really is a minor change, tell the user and record that decision.
EOF
exit 2
