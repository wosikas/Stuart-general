# Brief: research and write one poem page

Base folder: /tmp/claude-0/-home-user-Stuart-general/9238462c-e100-5e4e-81b8-d3616f26c44e/scratchpad
You will research ONE Power and Conflict poem in depth and write its page content as JSON.

## Read first
1. pc/RULES.md (binding accuracy rules).
2. build/SCHEMA.md (the JSON format and rules) and mock/ozy.html (the approved gold-standard page: match its depth, tone and plain English).
3. What we already have (verified): pc/strand1_power.md, pc/strand2_nature.md, pc/strand3_war.md, pc/strand4_identity.md and the matching pc/verify*.md files (corrections!), pc/exam_materials.md (AQA questions, mark schemes, examiners' reports — verbatim), pc/anth.txt (AQA anthology text = master copy for wording and line numbers), pc/theme_tags.md (AQA-backed theme tags; if it does not exist yet, wait a minute and check again; if still missing, derive tags yourself from exam_materials.md using the rule in SCHEMA.md).
4. PMT notes for your poem in pc/pmt_dl/ (LEADS ONLY — they contain errors; use them as a checklist of what to cover, verify everything).

## Research (new, this session)
Deep AO3 context like pc/context_shelley.md (read it as the model): the poet's life and beliefs, the times and events around the poem, the story behind the poem (where/when published, what prompted it, author interviews or statements if a reliable page has them), the literary background. Two reliable sources where possible (Britannica, poets' official sites/estates, publishers, Poetry Archive, British Library, IWM, National Army Museum, National Archives, universities, exam boards' own resources such as AQA/WJEC/Pearson). Blocked sites: note and move on; never work around blocks. Save your research notes (fact | URL | exact sentence | SAFE/USE WITH CARE) to pc/context_<slug>.md.

Also verify the form (e.g. dramatic monologue, blank verse, free verse, ballad, stanza shape) from a reliable source if you make claims about it; anything you count yourself from anth.txt is fine.

## Write
build/content/<slug>.json, following SCHEMA.md exactly. Requirements:
- Synopsis covers the whole poem in order, with the AQA line numbers (count lines in anth.txt; ignore page numbers).
- Comparisons: up to 3 best partners, AQA-backed pairings first (see exam_materials.md). Every quotation from either poem must match anth.txt exactly.
- Context cards: 3–4 cards, 3–5 items each, every item with "src"; "use" says which question theme it helps; "care" for one-source or our-reading items.
- exam_box: a likely question using a real AQA focus phrase, a model thesis, ONE model comparison paragraph, 3 "why it scores" bullets.
- For copyright:true poems: never more than ~12 consecutive words of the poem anywhere.
- Plain English for a 15–16-year-old.

## Self-check before finishing
Run a python check that every <q>…</q> and every quotes[].q string and every <mark> text appears verbatim in pc/anth.txt (normalise curly vs straight apostrophes, dashes and whitespace/line breaks; strip the curly quote marks you added). Fix any that fail. Validate JSON with json.load.

Return: 6 lines — what you added beyond what we had, the strongest context facts, anything single-source, anything blocked, and any gaps.
