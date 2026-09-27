#!/usr/bin/env bash
# Source A: collect Reddit on the Mac (home connection) with last30days, then
# check coverage and optionally push the pack to the loom repo.
#
# Usage:
#   LOOM_REPO=/path/to/loom/clone ./mac_collect.sh [--push]
# Optional env:
#   L30_ENGINE   path to last30days.py (default: ~/.claude/skills/last30days/scripts/last30days.py)
#   DAYS         lookback window (default 30)
#   PAUSE        seconds between topics (default 60)
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ENGINE="${L30_ENGINE:-$HOME/.claude/skills/last30days/scripts/last30days.py}"
DAYS="${DAYS:-30}"
PAUSE="${PAUSE:-60}"
PUSH=0
[[ "${1:-}" == "--push" ]] && PUSH=1

: "${LOOM_REPO:?Set LOOM_REPO to your local clone of the loom repo}"
[[ -f "$ENGINE" ]] || { echo "last30days engine not found at $ENGINE (set L30_ENGINE)"; exit 1; }

DATE="$(date +%Y-%m-%d)"
PACK="$LOOM_REPO/research/reddit/$DATE"
OUT="$PACK/a-last30days"
mkdir -p "$OUT"

SUBS="$(grep -v '^#' "$HERE/subreddits.txt" | grep -v '^\s*$' | paste -sd, -)"
cp "$HERE/subreddits.txt" "$HERE/topics.txt" "$PACK/"

# Half the default keyless pace: slower, fewer 429s.
export LAST30DAYS_REDDIT_KEYLESS_RATE="${LAST30DAYS_REDDIT_KEYLESS_RATE:-0.5}"

first=1
while IFS= read -r topic; do
  [[ -z "${topic// }" || "$topic" == \#* ]] && continue
  [[ $first -eq 0 ]] && sleep "$PAUSE"
  first=0
  slug="$(echo "$topic" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//')"
  echo "== $topic"
  python3 "$ENGINE" "$topic" \
    --search reddit --subreddits "$SUBS" --deep --days "$DAYS" \
    --emit json --json-profile raw --output "$OUT/$slug.json" \
    || echo "   run failed for '$topic' (coverage check will show it)"
done < "$HERE/topics.txt"

python3 "$HERE/coverage_gate.py" "$PACK" --subreddits "$HERE/subreddits.txt" --days "$DAYS" || true

if [[ $PUSH -eq 1 ]]; then
  git -C "$LOOM_REPO" add "research/reddit/$DATE"
  git -C "$LOOM_REPO" commit -m "research: Reddit pack $DATE (last30days)"
  git -C "$LOOM_REPO" push
fi
echo "Pack: $PACK"
