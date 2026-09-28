#!/usr/bin/env bash
# Stop hook. If Claude changed UI source files during this turn, it is sent back once to
# screenshot the result, add it to the board's Built vs mockup part, and critique it.
# Changes to the design board itself do not count. Exit 0 with no output lets Claude stop.
input=$(cat)
# Only send Claude back once per turn, so this can never loop.
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false')" = "true" ] && exit 0

session=$(printf '%s' "$input" | jq -r '.session_id // "default"')
marker="${TMPDIR:-/tmp}/claude-design-turn-$session"
[ -f "$marker" ] || exit 0

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
changed=""
while IFS= read -r f; do
  [ -f "$f" ] && [ "$f" -nt "$marker" ] && changed="$changed $f"
done < <(git status --porcelain -uall 2>/dev/null | awk '{print $NF}' \
          | grep -E '\.(tsx|jsx|vue|svelte|astro|html|css|scss)$' | grep -v '^design/')
[ -z "$changed" ] && exit 0

jq -n --arg files "$changed" '{
  decision: "block",
  reason: ("UI files changed this turn:" + $files + ". Before finishing: screenshot the result at desktop and mobile widths, add it to the Built vs mockup part of this project'"'"'s design board, compare it with the approved option, and give a three-line critique. For a minor change with no board section, just screenshot and critique.")
}'
exit 0
