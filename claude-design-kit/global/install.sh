#!/usr/bin/env bash
# Installs the design kit globally into ~/.claude. Safe to re-run.
# Backs up CLAUDE.md and settings.json before changing them.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="$HOME/.claude"
stamp=$(date +%Y%m%d-%H%M%S)
command -v jq >/dev/null || { echo "jq is required: brew install jq" >&2; exit 1; }
mkdir -p "$dest/hooks"

# 1. Hook scripts: added (overwritten if already present from an earlier install).
for f in design-lens.sh design-gate.sh design-check-on-stop.sh; do
  cp "$here/hooks/$f" "$dest/hooks/$f"; chmod +x "$dest/hooks/$f"
  echo "added    $dest/hooks/$f"
done

# 2. CLAUDE.md: the design block is appended, or replaced if a previous install left one.
md="$dest/CLAUDE.md"
if [ -f "$md" ]; then
  cp "$md" "$md.bak-$stamp"
  sed -i.tmp '/<!-- BEGIN claude-design-kit -->/,/<!-- END claude-design-kit -->/d' "$md" && rm -f "$md.tmp"
  printf '\n' >> "$md"; echo "updated  $md (backup: $md.bak-$stamp)"
else
  echo "added    $md"
fi
cat "$here/CLAUDE.design.md" >> "$md"

# 3. settings.json: the three hooks are merged in. Your existing settings and hooks are kept.
st="$dest/settings.json"
if [ -f "$st" ]; then cp "$st" "$st.bak-$stamp"; echo "updated  $st (backup: $st.bak-$stamp)"
else echo '{}' > "$st"; echo "added    $st"; fi
jq -s '
  .[0] as $cur | .[1].hooks as $new |
  $cur | .hooks = (
    reduce ($new | keys[]) as $ev ((.hooks // {});
      .[$ev] = (
        ((.[$ev] // []) | map(select((.hooks // []) | all(.command | test("claude/hooks/design-") | not))))
        + $new[$ev]))
  )' "$st" "$here/settings.hooks.json" > "$st.new" && mv "$st.new" "$st"

echo; echo "Done. Open Claude Code and run /hooks to confirm the three design hooks are listed."
