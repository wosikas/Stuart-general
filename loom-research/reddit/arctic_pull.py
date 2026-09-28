#!/usr/bin/env python3
"""Source B: pull posts and comment threads from the Arctic Shift Reddit archive.

Runs anywhere (it does not touch reddit.com). Writes one JSON per subreddit into
<pack>/b-arctic/ plus status.json. A down or failing archive is recorded as a
status, not treated as "no discussion".

Usage: arctic_pull.py <pack_dir> --subreddits subreddits.txt [--days 30]
       [--max-posts 500] [--threads 25]
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://arctic-shift.photon-reddit.com/api"
UA = "loom-research/0.1 (personal, read-only)"
PAUSE = 1.0  # seconds between requests


class ArchiveDown(Exception):
    pass


def get(path, params, retries=4):
    url = f"{API}/{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(PAUSE)
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read()[:200].decode("utf-8", "replace")
            if e.code == 503 and "maintenance" in body.lower():
                raise ArchiveDown(body)
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(2 ** (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < retries - 1:
                time.sleep(2 ** (attempt + 1))
                continue
            raise


def comments_flat(node, out):
    """Collect every object with a comment body from Arctic Shift's tree shape."""
    if isinstance(node, dict):
        if "body" in node and ("link_id" in node or "parent_id" in node):
            out.append({k: node.get(k) for k in ("id", "parent_id", "body", "score", "created_utc")})
        for v in node.values():
            comments_flat(v, out)
    elif isinstance(node, list):
        for v in node:
            comments_flat(v, out)
    return out


def pull_sub(sub, start, end, max_posts, n_threads):
    posts, before = [], int(end.timestamp())
    while len(posts) < max_posts:
        data = get("posts/search", {
            "subreddit": sub, "after": int(start.timestamp()), "before": before,
            "sort": "desc", "limit": 100,
            # "permalink" is not an accepted field name here; the URL is rebuilt from id.
            "fields": "id,title,selftext,score,num_comments,created_utc",
        }).get("data") or []
        if not data:
            break
        posts += data
        before = min(p["created_utc"] for p in data)
        if len(data) < 100:
            break
    posts = posts[:max_posts]
    for p in posts:
        p["url"] = f"https://www.reddit.com/r/{sub}/comments/{p['id']}/"
    for p in sorted(posts, key=lambda p: p.get("num_comments") or 0, reverse=True)[:n_threads]:
        if (p.get("num_comments") or 0) == 0:
            continue
        tree = get("comments/tree", {"link_id": f"t3_{p['id']}", "limit": 500})
        p["comments"] = comments_flat(tree.get("data"), [])
    return posts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--subreddits", required=True)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--max-posts", type=int, default=500)
    ap.add_argument("--threads", type=int, default=25)
    a = ap.parse_args()

    subs = [s.strip() for s in Path(a.subreddits).read_text().splitlines()
            if s.strip() and not s.startswith("#")]
    out = Path(a.pack) / "b-arctic"
    out.mkdir(parents=True, exist_ok=True)
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=a.days)
    status = {"source": "arctic-shift", "window": [start.date().isoformat(), end.date().isoformat()],
              "subreddits": {}}

    for sub in subs:
        try:
            posts = pull_sub(sub, start, end, a.max_posts, a.threads)
            (out / f"{sub}.json").write_text(json.dumps(posts, indent=1))
            status["subreddits"][sub] = {"state": "ok" if posts else "no-results", "posts": len(posts)}
        except ArchiveDown as e:
            status["subreddits"][sub] = {"state": "unavailable", "detail": str(e)}
            for rest in subs[subs.index(sub) + 1:]:
                status["subreddits"][rest] = {"state": "unavailable", "detail": "archive down"}
            break
        except Exception as e:  # recorded, never read as "no discussion"
            status["subreddits"][sub] = {"state": "error", "detail": f"{type(e).__name__}: {e}"[:200]}
        print(sub, status["subreddits"][sub])

    (out / "status.json").write_text(json.dumps(status, indent=1))
    return 0 if all(v["state"] in ("ok", "no-results") for v in status["subreddits"].values()) else 2


if __name__ == "__main__":
    sys.exit(main())
