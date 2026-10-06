#!/usr/bin/env python3
"""Build the Power and Conflict guide: content/*.json + parts/*.html -> out/guide.html"""
import json, glob, os, html, re, sys

B = os.path.dirname(os.path.abspath(__file__))
ANTH_URL = "https://filestore.aqa.org.uk/resources/english/AQA-8702-TG-POEMS.PDF"

THEME_COL = {
 "Power": ("#fde7d9", "#9a3d0c"), "Pride": ("#efe3fb", "#6a2fa0"), "Tyranny": ("#fbe0e6", "#9c2346"),
 "Nature": ("#ddf3e4", "#1e6b3a"), "Time": ("#e0ecfb", "#1f4f8f"), "Conflict": ("#fde2d2", "#a2400f"),
 "War": ("#f6dcdc", "#8f2424"), "Effects of conflict": ("#fbe6cf", "#8a4b0c"),
 "Difficult experiences": ("#ece6dc", "#5e4a2c"), "Identity": ("#e3e6fb", "#3a3f9a"),
 "Memory": ("#e6f0f7", "#245a7a"), "Loss": ("#eceef2", "#454c5c"), "Guilt": ("#f3e3d6", "#7a3d14"),
 "Fear": ("#e9e1f1", "#5a2f80"), "Patriotism and duty": ("#dfeaf6", "#1d4a7a"),
 "Place and home": ("#e2f2ef", "#1f6359"), "Isolation": ("#e9edf0", "#3e4f5c"),
 "Art outlasts power": ("#f6eedb", "#7a5a0c"), "Childhood": ("#fdf0d5", "#86600a"),
}

def tag(t):
    bg, fg = THEME_COL.get(t["name"], ("#eceef2", "#454c5c"))
    src = html.escape(t.get("src", ""))
    if t.get("aqa"):
        return f'<span class="tag" style="background:{bg};color:{fg}">{html.escape(t["name"])} <small>· {src}</small></span>'
    return f'<span class="tag dash">{html.escape(t["name"])} <small>· {src or "our reading"}</small></span>'

def simple_tag(name):
    bg, fg = THEME_COL.get(name, ("#eceef2", "#454c5c"))
    return f'<span class="tag" style="background:{bg};color:{fg}">{html.escape(name)}</span>'

def q(s):  # a quotation from a poem, add curly quotes
    return f'<span class="qt">“{s}”</span>'

def poem_page(p):
    o = []
    n = p["num"]
    o.append(f'<section class="poem" id="{p["slug"]}">')
    o.append(f'''<div class="banner"><div>
<div class="kick">POEM {n} OF 15 &nbsp;·&nbsp; THEME GROUP: {html.escape(p["group"]).upper()}</div>
<h1>{html.escape(p["title"])}</h1>
<div class="by">{html.escape(p["poet"])} ({p["poet_dates"]}) · {p["published"]}</div>
{'<div class="anchor">★ ANCHOR POEM: learn this one first</div>' if p.get("anchor") else ''}
</div><div class="big">{n:02d}</div></div>''')
    o.append('<div class="wrap">')
    f = p["facts"]
    o.append('<div class="facts"><div class="fact span3"><div class="k">Themes <span class="kk">(solid = linked by AQA · dashed = our reading)</span></div><div class="v">'
             + "".join(tag(t) for t in p["themes"]) + '</div></div>'
             + f'<div class="fact"><div class="k">Type of poem</div><div class="v">{f["type"]}</div></div>'
             + f'<div class="fact"><div class="k">In the exam?</div><div class="v">{f["exam"]}</div></div>'
             + f'<div class="fact"><div class="k">Best partner</div><div class="v">{f["partner"]}</div></div></div>')
    c = p["cards"]
    o.append('<div class="three">' + "".join(
        f'<div class="card"><h4>{h}</h4><p>{c[k]}</p></div>' for h, k in
        (("The story in short", "story"), ("The message", "message"), ("Why it was written", "why"))) + '</div>')
    if p.get("title_note"):
        t = p["title_note"]
        o.append(f'<div class="card mt"><h4>{t.get("heading","The title")}</h4><p>{t["text"]} <span class="src">({t.get("src","")})</span></p></div>')
    s = p["synopsis"]
    o.append('<h2><span class="n">1</span>What happens, step by step</h2><div class="sub">Follow along in the poem. The line numbers match the AQA anthology.</div><div class="card"><ul class="steps">')
    o.append(f'<li><span class="lines">The setup</span><span>{s["setup"]}</span></li>')
    for st in s["steps"]:
        o.append(f'<li><span class="lines">{st["lines"]}</span><span>{st["text"]}</span></li>')
    lab = lambda txt, l: txt if re.match(r"^(<b>)?" + l, txt) else f"<b>{l}:</b> " + txt
    o.append(f'</ul><div class="turn">{lab(s["turn"], "The turning point")} {lab(s["ending"], "How it ends")} {lab(s["tone"], "The tone")}</div></div>')
    # poem
    if p.get("copyright"):
        intro = (p.get("poem_intro") or "") + f' The poem is still in copyright, so read the full text in your anthology, or in <a href="{ANTH_URL}">AQA\'s free anthology PDF</a>. Below, each section is explained in plain English, with the key words to quote.'
        h2 = "The poem, section by section"
        lh = "Key words to quote"
    else:
        intro = p.get("poem_intro") or "Highlighted words are the ones worth quoting in the exam."
        h2 = "The poem, with what it means"
        lh = "The poem"
    o.append(f'<h2><span class="n">2</span>{h2}</h2><div class="sub">{intro}</div><div class="card"><div class="grid"><div class="colh">{lh}</div><div class="colh rr">What it means, in plain English</div>')
    for b in p["poem_blocks"]:
        cls = "l poemtext" + (" cr" if p.get("copyright") else "")
        lab = f'<span class="blab">Lines {b["lines"]}</span>' if p.get("copyright") else ""
        o.append(f'<div class="{cls}">{lab}{b["text"]}</div><div class="r">{b["note"]}</div>')
    o.append('</div></div>')
    # quotes
    o.append(f'<h2><span class="n">3</span>Key quotations to learn</h2><div class="sub">Learn these word for word. Short quotations score better than long ones.</div><div class="qs">')
    for k in p["quotes"]:
        extra = ""
        if k.get("why"): extra += f' <b>Why it matters:</b> {k["why"]}'
        if k.get("tech"): extra += f' <b>Technique:</b> {k["tech"]}'
        o.append(f'<div class="qc"><div class="ln2">{k["line"]}</div><div class="qq">“{k["q"]}”</div><div class="m"><b>Means:</b> {k["means"]}{extra}</div></div>')
    o.append('</div>')
    # methods + form
    o.append(f'<h2><span class="n">4</span>How the poet writes it (methods)</h2><div class="sub">This is AO2: how the poet\'s choices create meaning.</div>')
    if p.get("form"):
        fm = p["form"]
        o.append(f'<div class="card mb"><b class="fh">{fm["heading"]}</b><div class="fgrid"><div><h5>About the form</h5><ul>'
                 + "".join(f"<li>{x}</li>" for x in fm["explain"]) + '</ul></div><div class="oz"><h5>What this poem does with it</h5><ul>'
                 + "".join(f"<li>{x}</li>" for x in fm["this_poem"]) + f'</ul></div></div><div class="say">{fm["say"]}</div></div>')
    o.append('<div class="meth">' + "".join(
        f'<div class="card"><b>{m["title"]}</b><p class="mt6">{m["text"]}</p><div class="def"><b>{m["term"]}:</b> {m["def"]}</div></div>'
        for m in p["methods"]) + '</div>')
    if p.get("warn"):
        o.append(f'<div class="warn">{p["warn"]}</div>')
    # context
    cx = p["context"]
    o.append('<h2><span class="n">5</span>Context (AO3): the background you can use</h2><div class="sub">Green labels show which kind of question each fact helps with. Context only earns marks when you link it to the poem\'s ideas.</div>')
    o.append('<div class="card"><h4 class="tlh">Timeline</h4><div class="tl">' + "".join(
        f'<div class="ev{" hi" if e.get("hi") else ""}"><b>{e["date"]}</b>{e["text"]}{(" <span class=care>" + e["care"] + "</span>") if e.get("care") else ""}</div>' for e in cx["timeline"]) + '</div></div>')
    o.append('<div class="ctxg">')
    for cd in cx["cards"]:
        items = ""
        for it in cd["items"]:
            items += f'<li>{it["text"]}'
            if it.get("src"): items += f' <span class="src">{it["src"]}</span>'
            if it.get("use"): items += f' <span class="use">{it["use"]}</span>'
            if it.get("care"): items += f' <span class="care">{it["care"]}</span>'
            items += '</li>'
        o.append(f'<div class="card"><h4>{cd["title"]}</h4><ul>{items}</ul></div>')
    o.append('</div>')
    ao3 = re.sub(r"^(<b>)?Putting it into an answer \(AO3\):(</b>)?\s*", "", cx["ao3"])
    o.append(f'<div class="dark mt"><b>Putting it into an answer (AO3):</b> {ao3}</div>')
    # comparisons
    o.append(f'<h2><span class="n">6</span>Comparing it: the best partner poems</h2><div class="sub">Pick the partner that fits the question\'s theme.</div>')
    for i, cp in enumerate(p["comparisons"]):
        o.append(f'''<div class="cmpc"><div class="cmph"><span class="pn">{"ABC"[i]}</span><div><b>{html.escape(p["title"])} + {html.escape(cp["partner"])}</b><br><span>Use for: {"".join(simple_tag(x) for x in cp["use_for"])} · {cp["aqa"]}</span></div></div>
<div class="sd"><div><h5>Similar</h5><ul>{"".join(f"<li>{x}</li>" for x in cp["similar"])}</ul></div><div><h5>Different</h5><ul>{"".join(f"<li>{x}</li>" for x in cp["different"])}</ul></div></div></div>''')
    # exam box
    e = p["exam_box"]
    o.append(f'''<h2><span class="n">7</span>In the exam</h2><div class="examb"><div class="eq">{e["question"]}</div>
<div class="et"><b>A strong opening (thesis):</b> {e["thesis"]}</div>
<div class="ep"><b>A model comparison paragraph:</b><br>{e["para"]}</div>
<div class="ew"><b>Why it scores:</b><ul>{"".join(f"<li>{x}</li>" for x in e["why"])}</ul></div></div>''')
    o.append('<div class="backtop"><a href="#contents">↑ Back to contents</a></div></div></section>')
    return "\n".join(o)

def build():
    poems = []
    for fn in glob.glob(os.path.join(B, "content", "*.json")):
        with open(fn, encoding="utf-8") as fh:
            poems.append(json.load(fh))
    poems.sort(key=lambda p: p["num"])
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    if only:
        poems = [p for p in poems if p["slug"] in only]
    css = open(os.path.join(B, "style.css"), encoding="utf-8").read()
    parts = {}
    mods = ""
    for slug in ("ozymandias", "remains", "storm"):
        fn = os.path.join(B, "parts", f"model_{slug}.html")
        if os.path.exists(fn): mods += open(fn, encoding="utf-8").read()
    for name in ("front", "models", "back"):
        fn = os.path.join(B, "parts", name + ".html")
        parts[name] = open(fn, encoding="utf-8").read() if os.path.exists(fn) else ""
    groups = {}
    for p in poems:
        groups.setdefault(p["group"], []).append(p)
    nav = '<nav class="toc" id="contents"><h2>Contents</h2><div class="tocg">'
    nav += '<div><h5>Start here</h5><ul><li><a href="#q26">What Q26 asks</a></li><li><a href="#marks">Where the marks come from</a></li><li><a href="#themes">The theme map</a></li><li><a href="#partners">Which poem do I use?</a></li><li><a href="#examiners">What examiners say</a></li></ul></div>'
    for g, ps in groups.items():
        nav += f'<div><h5>{g}</h5><ul>' + "".join(
            f'<li><a href="#{p["slug"]}">{p["num"]}. {html.escape(p["title"])}{" ★" if p.get("anchor") else ""}</a></li>' for p in ps) + '</ul></div>'
    nav += '<div><h5>Practice</h5><ul><li><a href="#models">Model answers</a></li><li><a href="#glossary">Glossary</a></li><li><a href="#sources">Sources</a></li></ul></div></div></nav>'
    parts["models"] = parts["models"].replace("<!--MODELS-->", mods)
    body = parts["front"].replace("<!--NAV-->", nav) + "".join(poem_page(p) for p in poems) + parts["models"] + parts["back"]
    out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Power and Conflict Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>{css}</style></head><body><main>{body}</main></body></html>'''
    body = re.sub(r'<table class="t( [^"]*)?"(.*?)</table>', r'<div class="tw"><table class="t\1"\2</table></div>', body, flags=re.S)
    art = f'''<title>Power and Conflict Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>{css}</style><main>{body}</main>'''
    out = out.split("<main>")[0] + "<main>" + body + "</main></body></html>"
    if not only:
        with open(os.path.join(B, "out", "artifact.html"), "w", encoding="utf-8") as fh:
            fh.write(art)
    name = "guide.html" if not only else "preview-" + "-".join(only) + ".html"
    with open(os.path.join(B, "out", name), "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote", name, len(poems), "poems")

if __name__ == "__main__":
    build()
