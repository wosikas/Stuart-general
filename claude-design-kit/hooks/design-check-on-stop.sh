#!/usr/bin/env bash
# Stop hook. If UI files changed in the working tree, remind Claude to render, look,
# and compare against the chosen mockup. Reminder only: it never blocks.
input=$(cat)
# Avoid loops if a previous stop hook already made Claude continue.
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false')" = "true" ] && exit 0

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
changed=$(git status --porcelain 2>/dev/null | grep -E '\.(tsx|jsx|vue|svelte|astro|html|css|scss)$')
[ -z "$changed" ] && exit 0

cat <<'EOF'
{"systemMessage": "UI files changed. Before calling this done: screenshot the result at desktop and mobile widths, add it to the Built vs mockup part of the design board, compare it with the chosen option, and give a three-line critique."}
EOF
exit 0
