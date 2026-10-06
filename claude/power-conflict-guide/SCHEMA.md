# Poem page content schema (one JSON file per poem: build/content/<slug>.json)

The gold-standard example is the Ozymandias mock-up: ../mock/ozy.html (open and read it). Every poem page must reach the same depth and style.

Audience: a 15–16-year-old, new to the poems, aiming high. Plain English. Sentences under ~25 words. Explain any technical term the first time.

## Binding accuracy rules
- Read ../pc/RULES.md. No facts from memory. Every context fact must come from a page opened in this session (or from the verified files in ../pc/), and its source named in the "src" field.
- Poem wording: ../pc/anth.txt is AQA's anthology text = MASTER COPY. Every quotation must match it exactly (apostrophes ’ and dashes as printed are fine either way; words and punctuation must match).
- Quotation marks “…” only around verbatim text (poem, AQA, named source). Your own wording never in quotes.
- Readings/interpretations are fine (that's the point of analysis) but must be sensible readings of the text. Where an idea is ours and not a sourced fact (e.g. a link to a historical event), add "care":"our reading".
- Single-source facts: "care":"one source".
- PMT notes (../pc/pmt_dl/<poem>.txt) are LEADS ONLY: they contain errors. Verify anything taken from them.
- Copyright: poets in copyright (Heaney, Hughes, Armitage, Weir, Duffy, Dharker, Rumens, Agard, Garland) → set "copyright": true; quote only short phrases (max ~12 words per quote), NEVER whole lines-in-sequence or stanzas. Out of copyright (Shelley, Blake, Wordsworth, Browning, Tennyson, Owen) → "copyright": false and the poem_blocks carry the full text.
- Don't put the student's or family names anywhere. No file paths.

## Allowed inline HTML in text fields
<b>, <i>, <q>…</q> for a quotation from the poem (renders highlighted italic; put the curly quotes inside: <q>“king of kings”</q>), <mark> (only inside poem_blocks text), <span class="src">Britannica</span>, <span class="care">our reading</span>, <br>.

## Fields
```json
{
 "num": 1,
 "slug": "ozymandias",
 "title": "Ozymandias",
 "poet": "Percy Bysshe Shelley",
 "poet_dates": "1792–1822",
 "published": "published 1818",
 "group": "Power and pride",               // one of: Power and pride | Nature | War and its aftermath | Identity, home and loss
 "anchor": true,
 "copyright": false,
 "facts": {"type": "Sonnet (14 lines)", "exam": "Yes: specimen and June 2018", "partner": "Storm on the Island"},
 "themes": [ {"name": "Power", "aqa": true, "src": "AQA question 2018"},
             {"name": "Tyranny", "aqa": false, "src": "our reading"} ],
     // Use the theme vocabulary: Power, Pride, Tyranny, Nature, Time, Conflict, War, Effects of conflict, Difficult experiences,
     // Identity, Memory, Loss, Guilt, Fear, Patriotism and duty, Place and home, Isolation, Art outlasts power, Childhood.
     // aqa:true ONLY if ../pc/theme_tags.md shows an AQA question / mark scheme / report linking THIS poem to THIS theme; src names it.
 "cards": {"story": "…", "message": "…", "why": "…"},          // "why" may include <span class="src">…</span>
 "title_note": {"heading": "The title", "text": "…", "src": "University of Toronto; Britannica"},
 "synopsis": {
    "setup": "…",
    "steps": [ {"lines": "Lines 1–3", "text": "…"} ],          // 4–7 steps covering the WHOLE poem in order, with AQA line numbers
    "turn": "…", "ending": "…", "tone": "…"
 },
 "poem_intro": "Highlighted words are the ones worth quoting in the exam.",   // for copyright poems: explain that the full poem is in the anthology (link added by renderer)
 "poem_blocks": [
    {"lines": "1–3", "text": "I met a traveller from an <mark>antique land</mark><br>Who said: …", "note": "plain-English meaning …"}
 ],
    // copyright:false → "text" = the full verbatim lines for that block (all blocks together = whole poem, in order), line breaks as <br>, quotable bits in <mark>.
    // copyright:true  → "text" = ONLY 1–2 short key phrases from those lines, each in <mark>, separated by " … " (no full lines); "note" = full plain-English explanation of what happens in those lines.
 "quotes": [ {"line": "LINE 5", "q": "sneer of cold command", "means": "…", "why": "…", "tech": "alliteration"} ],   // 8 for anchors, 6–7 otherwise; q WITHOUT surrounding quote marks
 "form": {  // optional but expected where form matters (sonnet, dramatic monologue, blank verse, free verse…)
    "heading": "The form: what a sonnet is, and what Shelley does with it",
    "explain": ["…", "…"],          // what the form is, why poets use it (sourced)
    "this_poem": ["…", "…"],        // what this poet does with it and why it matters
    "say": "A sentence you could use: …"
 },
 "methods": [ {"title": "Irony", "text": "…", "term": "Irony", "def": "when the result is the opposite of what someone meant or expected."} ],   // 4
 "warn": "Examiners warn: …",     // optional, only verbatim-sourced AQA warnings
 "context": {
    "timeline": [ {"date": "1792", "text": "Shelley born, Sussex"}, {"date": "Jan 1818", "text": "Ozymandias published", "hi": true}, {"date": "1792", "text": "…", "care": "one source"} ],   // 6–8 events, all sourced
    "cards": [ {"title": "Who Shelley was", "items": [ {"text": "…", "src": "Britannica", "use": "power · tyranny", "care": ""} ]} ],   // 3–4 cards, 3–5 items each
    "ao3": "Putting it into an answer (AO3): …"
 },
 "comparisons": [   // up to 3, best first
    {"partner": "Storm on the Island", "use_for": ["Nature", "Power"], "aqa": "AQA: specimen and 2018 mark schemes",
     "similar": ["… with <q>“…”</q> from BOTH poems …"], "different": ["<b>Speed:</b> …"]}
 ],
    // aqa: cite where an AQA mark scheme/report suggests the pairing (see ../pc/exam_materials.md); if none, "Our suggestion".
    // Partner-poem quotations must also match anth.txt exactly.
 "exam_box": {
    "question": "A likely question: Compare how poets present … in ‘X’ and in one other poem from ‘Power and conflict’.",   // use real AQA question wording/themes where possible
    "thesis": "…",                 // a model opening sentence
    "para": "…",                   // ONE model comparison paragraph (90–140 words) with <q> quotes from both poems
    "why": ["thesis answers the question in one sentence", "…"]   // 3 short bullets: why this paragraph scores
 }
}
```
Write valid JSON (UTF-8). Escape double quotes inside strings as \" or use curly quotes “ ” (preferred).
