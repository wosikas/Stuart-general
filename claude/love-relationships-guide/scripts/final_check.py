#!/usr/bin/env python3
"""Whole-guide checks: quotations vs AQA anthology, copyright run length, banned strings."""
import json, glob, os, re, html

B = os.path.dirname(os.path.abspath(__file__))
anth = open(os.path.join(B, "..", "pc", "anth.txt"), encoding="utf-8").read()

def norm(s):
    s = html.unescape(s)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("\x0c", " ")
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("…", "..."), ("é", "e"), ("É", "E")):
        s = s.replace(a, b)
    s = s.replace(" 's ", "'s ")  # anthology extraction artefact: "there 's"
    s = re.sub(r"\s*/\s*", " ", s)
    s = s.replace("...", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip(" \"'.,;:!?-").lower()

lines = [l for l in anth.split("\n") if not re.fullmatch(r"\s*\d+\s*", l)]
A = norm(" ".join(lines))
A_words = A.split()

fails, n = [], 0
COPY = {"letters-from-yorkshire", "walking-away", "eden-rock", "follower", "mother-any-distance", "before-you-were-mine", "winter-swans", "singh-song", "climbing-my-grandfather"}

def check(q, where):
    global n
    for part in re.split(r"\s*(?:…|\.\.\.|”\s*/\s*“)\s*", q):
        p = norm(part)
        if len(p) < 3: continue
        n += 1
        if p not in A:
            fails.append((where, part[:90]))

def texts(o):
    if isinstance(o, dict):
        for v in o.values(): yield from texts(v)
    elif isinstance(o, list):
        for v in o: yield from texts(v)
    elif isinstance(o, str):
        yield o

for fn in sorted(glob.glob(os.path.join(B, "content", "*.json"))):
    p = json.load(open(fn, encoding="utf-8"))
    slug = p["slug"]
    for t in texts(p):
        for q in re.findall(r"<q>(.*?)</q>", t, re.S): check(q, slug + " <q>")
        for q in re.findall(r"<mark>(.*?)</mark>", t, re.S): check(q, slug + " <mark>")
    for k in p["quotes"]: check(k["q"], slug + " quotes")
    if not p.get("copyright"):
        whole = norm(" ".join(b["text"] for b in p["poem_blocks"]))
        if whole not in A and whole not in re.sub(r"(?<= )\d+\. ", "", A): fails.append((slug, "poem_blocks do not reproduce the poem exactly"))

for fn in glob.glob(os.path.join(B, "parts", "*.html")):
    s = open(fn, encoding="utf-8").read()
    for q in re.findall(r"<q>(.*?)</q>", s, re.S): check(q, os.path.basename(fn))

out = open(os.path.join(B, "out", "guide.html"), encoding="utf-8").read() if os.path.exists(os.path.join(B, "out", "guide.html")) else ""
banned = ["/home", "/tmp", "scratchpad", "Stuart", "Finlay", "York Notes", "LitCharts", "SparkNotes", "Bitesize", "Save My Exams", "TODO", "XXX"]
bad = [b for b in banned if b in out]

# longest run of consecutive words from each in-copyright poem appearing in the built page
def longest_run(page_words, poem_words):
    best = 0
    idx = {}
    for i, w in enumerate(poem_words): idx.setdefault(w, []).append(i)
    for i in range(len(page_words)):
        for j in idx.get(page_words[i], []):
            k = 0
            while i + k < len(page_words) and j + k < len(poem_words) and page_words[i + k] == poem_words[j + k]: k += 1
            best = max(best, k)
    return best

print(f"quotations checked: {n}; failures: {len(fails)}")
for f in fails: print("  FAIL", f)
print("banned strings in guide.html:", bad or "none")
if out:
    body = norm(re.sub(r"<style.*?</style>", " ", out, flags=re.S))
    pw = body.split()
    titles = {"letters-from-yorkshire": ("Letters From Yorkshire", "MAURA DOOLEY"), "walking-away": ("Walking Away", "LEWIS"),
              "eden-rock": ("Eden Rock", "CAUSLEY"), "follower": ("Follower", "HEANEY"), "mother-any-distance": ("Mother, any distance", "ARMITAGE"),
              "before-you-were-mine": ("Before You Were Mine", "DUFFY"), "winter-swans": ("Winter Swans", "SHEERS"),
              "singh-song": ("Singh Song!", "NAGRA"), "climbing-my-grandfather": ("Climbing My Grandfather", "WATERHOUSE")}
    for slug, (t, poet) in titles.items():
        m = re.search(r"^\x0c?" + re.escape(t) + r"\s*$", anth[anth.find("Love and relationships"):], re.M | re.I)
        if m: i = anth.find("Love and relationships") + m.start()
        else: i = anth.find(t + " greater", anth.find("Love and relationships")) - 1  # Mother, any distance: no separate title line
        j = anth.find(poet, i)
        poem = norm(anth[i:j]).split()[len(norm(t).split()):]
        print(f"  longest copied run, {slug}: {longest_run(pw, poem)} words")
