# Reddit evidence pack for Loom research

Reddit blocks cloud servers (HTTP 403) and has closed self-serve API keys, so Reddit
comes from three sources, in this order of trust:

| Source | Where it runs | What it gives | Counted as coverage? |
|---|---|---|---|
| **A. last30days on the Mac** | Your Mac (home connection) | Posts, scores, comment counts, top comments, per-run status | Yes |
| **B. Arctic Shift archive** | Anywhere, incl. the cloud | Posts + full comment trees for the busiest threads | Yes |
| **D. Web search snippets** | The research run | Short quotes found by search | **No**, supplement only, labelled as snippets |

## 1. On the Mac (source A)

```bash
cd <this folder>
LOOM_REPO=/path/to/your/loom/clone ./mac_collect.sh --push
```

- Runs each topic in `topics.txt` against the subreddits in `subreddits.txt`: Reddit only, `--deep`, last 30 days, one minute between topics and half the default Reddit request pace.
- Writes `research/reddit/<date>/a-last30days/*.json` in the loom repo, then runs the coverage check, then commits and pushes. Leave off `--push` to look first.
- If last30days is not at `~/.claude/skills/last30days/scripts/last30days.py`, set `L30_ENGINE=/path/to/last30days.py`.

## 2. In the cloud (source B)

```bash
python3 arctic_pull.py <pack> --subreddits subreddits.txt --days 30
```

Adds `b-arctic/` to the same pack. If the archive is down it records `unavailable` and moves on.

## 3. The coverage check (runs before any report)

```bash
python3 coverage_gate.py <pack> --subreddits subreddits.txt --days 30
```

Writes `coverage.md` and `coverage.json`. Per subreddit it counts unique posts in the window (A and B merged), threads with comments, and the earliest and latest dates, and checks:

- at least **20 posts** in the window (`--min-posts`)
- at least **5 threads with comments** (`--min-threads`)
- the newest post is within 3 days of today, and the first week of the window is present

Result: **PASS** (exit 0), **PARTIAL** (exit 2: some subreddits short) or **FAIL** (exit 1: no source worked, or every subreddit short).

## Rules for the report run

1. Run `coverage_gate.py` first. Put `coverage.md` in the report's Evidence section.
2. **FAIL**: no Reddit conclusions. Say Reddit coverage failed and why.
3. **PARTIAL**: Reddit conclusions only for subreddits marked `ok`; name the short ones as gaps.
4. A failure state (`rate-limited`, `unreachable`, `error`, `unavailable`) means coverage is unknown. Never read it as "nobody discussed this".
5. Search snippets (D) may add quotes but never change a PASS/PARTIAL/FAIL verdict. Mark them "(snippet)".

Edit `subreddits.txt` and `topics.txt` to change scope. Keep the subreddit list in line with the Reddit data access request.
