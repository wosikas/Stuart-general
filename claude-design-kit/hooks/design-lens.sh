#!/usr/bin/env bash
# UserPromptSubmit hook. Prints a short design reminder when the prompt looks like UI work.
# Whatever this prints on exit 0 is added to Claude's context for that turn.
# It also stamps the start of the turn, so the Stop hook can tell which files
# changed during this turn.
input=$(cat)
prompt=$(printf '%s' "$input" | jq -r '.prompt // empty')
session=$(printf '%s' "$input" | jq -r '.session_id // "default"')
touch "${TMPDIR:-/tmp}/claude-design-turn-$session" 2>/dev/null
if printf '%s' "$prompt" | grep -qiE '(^|[^a-z])(ui|ux|screen|page|component|layout|design|redesign|button|form|modal|dashboard|landing|onboarding|flow|css|tailwind|figma|mockup)([^a-z]|$)'; then
cat <<'EOF'
[Design lens] You, Claude Code, do the design work yourself. There is no separate
design agent: tools like a Design artifact type or Figma are tools you operate.
First classify: new design / major change, or minor change.
New or major: no production UI code yet. Add a feature section to the single design
board (design/board/index.html, one Artifact link): Brief, up to 3 genuinely different
high-fidelity Options (desktop + mobile), States, Recommendation, Decision. Screenshot
and check it, republish, then stop and ask the user to pick. Record the pick in the
board and in design/decisions/<slug>.md before building. On a pick, badge the
approved option(s) and grey out the rest with a "Not chosen" label, then republish.
Minor: build directly, update Foundations if tokens change, render and check it.
EOF
fi
exit 0
