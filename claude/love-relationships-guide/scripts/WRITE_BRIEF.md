# Brief: research and write one poem page

Base folder: /tmp/claude-0/-home-user-Stuart-general/9238462c-e100-5e4e-81b8-d3616f26c44e/scratchpad
You will research ONE Power and Conflict poem in depth and write its page content as JSON.

## Read first
1. pc/RULES.md (binding accuracy rules).
2. build_lr/SCHEMA.md (the JSON format and rules) and mock/ozy.html (the approved gold-standard page: match its depth, tone and plain English).
3. What we already have (verified): lr/exam_materials_lr.md (AQA Love and relationships questions, mark schemes, examiners' reports — verbatim), pc/exam_materials.md (level descriptors and general examiners' advice), pc/anth.txt (AQA anthology text = master copy for wording and line numbers; the Love and relationships poems are in its first part), lr/theme_tags_lr.md (AQA-backed theme tags). For poets also in the Power and Conflict cluster (Shelley, Browning, Heaney, Armitage, Duffy) you may reuse verified facts from pc/context_shelley.md, pc/context_my-last-duchess.md, pc/context_storm-on-the-island.md, pc/context_remains.md, pc/context_war-photographer.md and build/content/*.json (already independently verified).
4. PMT notes for your poem in lr/pmt_dl/ (LEADS ONLY — they contain errors; use them as a checklist of what to cover, verify everything).

## Research (new, this session)
Deep AO3 context like pc/context_shelley.md (read it as the model): the poet's life and beliefs, the times and events around the poem, the story behind the poem (where/when published, what prompted it, author interviews or statements if a reliable page has them), the literary background. Two reliable sources where possible (Britannica, poets' official sites/estates, publishers, Poetry Archive, British Library, IWM, National Army Museum, National Archives, universities, exam boards' own resources such as AQA/WJEC/Pearson). Blocked sites: note and move on; never work around blocks. Save your research notes (fact | URL | exact sentence | SAFE/USE WITH CARE) to lr/context_<slug>.md.

Also verify the form (e.g. dramatic monologue, blank verse, free verse, ballad, stanza shape) from a reliable source if you make claims about it; anything you count yourself from anth.txt is fine.

## Write
build_lr/content/<slug>.json, following build_lr/SCHEMA.md exactly. Requirements:
- Synopsis covers the whole poem in order, with the AQA line numbers (count lines in anth.txt; ignore page numbers).
- Comparisons: up to 3 best partners, AQA-backed pairings first (see lr/exam_materials_lr.md); always include the guide's anchor partner named in your task. Every quotation from either poem must match anth.txt exactly.
- Context cards: 3–4 cards, 3–5 items each, every item with "src"; "use" says which question theme it helps; "care" for one-source or our-reading items.
- exam_box: a likely question using a real AQA focus phrase, a model thesis, ONE model comparison paragraph, 3 "why it scores" bullets.
- For copyright:true poems: never more than ~10 consecutive words of the poem anywhere.
- Plain English for a 15–16-year-old.

## Self-check before finishing
Run a python check that every <q>…</q> and every quotes[].q string and every <mark> text appears verbatim in pc/anth.txt (normalise curly vs straight apostrophes, dashes and whitespace/line breaks; strip the curly quote marks you added). Fix any that fail. Validate JSON with json.load.

Return: 6 lines — what you added beyond what we had, the strongest context facts, anything single-source, anything blocked, and any gaps.

## Love and relationships guide: the anchor system (binding)
AQA's Love and relationships questions alternate between ROMANTIC love and FAMILY relationships, and AQA's mark schemes suggest partners from the same strand. The guide has FOUR anchor poems the student learns in depth:
- Romantic: Porphyria's Lover (main) and Winter Swans (backup, used when Porphyria's Lover is printed).
- Family: Mother, any distance (main) and Follower (backup, used when Mother, any distance is printed).
facts.partner must name the anchor partner first, e.g. "Porphyria's Lover (your anchor); Love's Philosophy also works well". The anchor partner must be one of the comparisons (comparison A ideally). Poem numbering and groups:
1 Love's Philosophy, 2 Sonnet 29 – ‘I think of thee!’, 3 Porphyria's Lover ★, 4 The Farmer's Bride, 5 Singh Song!, 6 Winter Swans ★ (group "Romantic love");
7 When We Two Parted, 8 Neutral Tones, 9 Letters From Yorkshire (group "Heartbreak and distance");
10 Mother, any distance ★, 11 Follower ★, 12 Walking Away, 13 Eden Rock, 14 Before You Were Mine, 15 Climbing My Grandfather (group "Family").
Anchors (★) get "anchor": true and 8 quotations.
