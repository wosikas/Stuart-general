#!/usr/bin/env python3
"""Coverage gate: decide whether a Reddit pack is complete enough to report on.

Reads a pack directory:
  a-last30days/*.json  (source A, last30days --emit json --json-profile raw)
  b-arctic/*.json      (source B, arctic_pull.py) + b-arctic/status.json
Writes coverage.md and coverage.json into the pack and exits:
  0 PASS, 1 FAIL, 2 PARTIAL (some subreddits short).

Source D (web search snippets) is never counted as coverage; the report may use
it only as a supplement and must label it as snippets.

Usage: coverage_gate.py <pack_dir> --subreddits subreddits.txt [--days 30]
       [--min-posts 20] [--min-threads 5]
"""
import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

POST_ID = re.compile(r"/comments/([a-z0-9]+)")


def norm_sub(s):
    return (s or "").lower().removeprefix("/").removeprefix("r/").strip()


def to_date(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return datetime.fromtimestamp(v, timezone.utc).date()
    try:
        return date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def load_a(pack):
    """Posts and per-run reddit status from last30days raw JSON."""
    posts, runs = [], []
    for f in sorted((pack / "a-last30days").glob("*.json")):
        try:
            rep = json.loads(f.read_text())
        except (ValueError, OSError) as e:
            runs.append({"run": f.stem, "state": "unreadable", "detail": str(e)[:120]})
            continue
        st = (rep.get("source_status") or {}).get("reddit") or {}
        items = (rep.get("items_by_source") or {}).get("reddit") or []
        state, detail = st.get("state", "missing"), st.get("detail") or ""
        # last30days reports "ok" even when sub-requests were rate-limited; surface it.
        if state == "ok" and re.search(r"rate-limited|HTTP 429|HTTP 503", detail):
            state = "partial"
        runs.append({"run": f.stem, "state": state, "items": len(items), "detail": detail,
                     "planner": (rep.get("provider_runtime") or {}).get("planner_model")})
        for it in items:
            m = POST_ID.search(it.get("url") or "")
            posts.append({
                "id": m.group(1) if m else it.get("item_id"),
                "sub": norm_sub(it.get("container")),
                "date": to_date(it.get("published_at")),
                "comments": len((it.get("metadata") or {}).get("top_comments") or []),
                "src": "A",
            })
    return posts, runs


def load_b(pack):
    d = pack / "b-arctic"
    status = {}
    if (d / "status.json").exists():
        raw = json.loads((d / "status.json").read_text()).get("subreddits", {})
        status = {norm_sub(k): v for k, v in raw.items()}
    posts = []
    for f in sorted(d.glob("*.json")):
        if f.name == "status.json":
            continue
        for p in json.loads(f.read_text()):
            posts.append({"id": p.get("id"), "sub": norm_sub(f.stem),
                          "date": to_date(p.get("created_utc")),
                          "comments": len(p.get("comments") or []), "src": "B"})
    return posts, status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--subreddits", required=True)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--min-posts", type=int, default=20)
    ap.add_argument("--min-threads", type=int, default=5)
    a = ap.parse_args()
    pack = Path(a.pack)

    subs = [norm_sub(s) for s in Path(a.subreddits).read_text().splitlines()
            if s.strip() and not s.startswith("#")]
    a_posts, a_runs = load_a(pack)
    b_posts, b_status = load_b(pack)
    end = date.today()
    start = end - timedelta(days=a.days)

    rows, verdicts = [], []
    for sub in subs:
        merged = {}
        for p in a_posts + b_posts:
            if p["sub"] != sub:
                continue
            cur = merged.setdefault(p["id"], {"date": p["date"], "comments": 0, "src": set()})
            cur["comments"] = max(cur["comments"], p["comments"])
            cur["src"].add(p["src"])
            cur["date"] = cur["date"] or p["date"]
        dates = [v["date"] for v in merged.values() if v["date"]]
        in_window = [d for d in dates if start <= d <= end]
        threads = sum(1 for v in merged.values() if v["comments"] > 0)
        row = {
            "subreddit": sub,
            "posts": len(merged),
            "posts_in_window": len(in_window),
            "from_A": sum(1 for v in merged.values() if "A" in v["src"]),
            "from_B": sum(1 for v in merged.values() if "B" in v["src"]),
            "threads_with_comments": threads,
            "earliest": min(dates).isoformat() if dates else None,
            "latest": max(dates).isoformat() if dates else None,
            "B_state": (b_status.get(sub) or {}).get("state", "not-run"),
        }
        problems = []
        if row["posts_in_window"] < a.min_posts:
            problems.append(f"only {row['posts_in_window']} posts in window (need {a.min_posts})")
        if threads < a.min_threads:
            problems.append(f"only {threads} threads with comments (need {a.min_threads})")
        if dates and max(dates) < end - timedelta(days=3):
            problems.append(f"nothing newer than {max(dates)}")
        if dates and min(dates) > start + timedelta(days=7):
            problems.append(f"nothing older than {min(dates)} (first week of window missing)")
        row["verdict"] = "ok" if not problems else "short"
        row["problems"] = problems
        rows.append(row)
        verdicts.append(row["verdict"])

    a_ok = any(r["state"] in ("ok", "partial") for r in a_runs)
    b_ok = any(v.get("state") == "ok" for v in b_status.values())
    if not (a_ok or b_ok) or all(v == "short" for v in verdicts):
        overall, code = "FAIL", 1
    elif any(v == "short" for v in verdicts):
        overall, code = "PARTIAL", 2
    else:
        overall, code = "PASS", 0

    result = {"overall": overall, "window": [start.isoformat(), end.isoformat()],
              "thresholds": {"min_posts": a.min_posts, "min_threads": a.min_threads},
              "source_A_runs": a_runs, "source_B_status": b_status, "subreddits": rows}
    (pack / "coverage.json").write_text(json.dumps(result, indent=1))

    md = [f"# Reddit coverage: {overall}",
          f"Window {start} to {end}. Thresholds per subreddit: {a.min_posts} posts in window, "
          f"{a.min_threads} threads with comments. Source D (search snippets) is not counted.",
          "", "| Subreddit | Posts in window | From A | From B | Threads w/ comments | Earliest | Latest | B state | Verdict |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| r/{r['subreddit']} | {r['posts_in_window']} | {r['from_A']} | {r['from_B']} | "
                  f"{r['threads_with_comments']} | {r['earliest'] or '-'} | {r['latest'] or '-'} | "
                  f"{r['B_state']} | {r['verdict']}{': ' + '; '.join(r['problems']) if r['problems'] else ''} |")
    md += ["", "## Source A runs (last30days)", "| Run | Reddit state | Items | Planner | Detail |", "|---|---|---|---|---|"]
    md += [f"| {r['run']} | {r['state']} | {r.get('items', '-')} | {r.get('planner') or '-'} | {(r.get('detail') or '')[:90]} |"
           for r in a_runs] or ["| none | not-run | - | - | - |"]
    md += ["", "Failure states (rate-limited, unreachable, error, unavailable) mean coverage is unknown, "
           "not that nobody discussed the topic."]
    (pack / "coverage.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return code


if __name__ == "__main__":
    sys.exit(main())
