#!/usr/bin/env bash
# UserPromptSubmit hook. Prints a short design reminder when the prompt looks like UI work.
# Whatever this prints on exit 0 is added to Claude's context for that turn.
prompt=$(jq -r '.prompt // empty')
if printf '%s' "$prompt" | grep -qiE '(^|[^a-z])(ui|ux|screen|page|component|layout|design|redesign|button|form|modal|dashboard|landing|onboarding|flow|css|tailwind|figma|mockup)([^a-z]|$)'; then
cat <<'EOF'
[Design lens] First classify: new design / major change, or minor change.
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
