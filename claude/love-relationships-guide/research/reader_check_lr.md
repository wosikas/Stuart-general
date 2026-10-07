# Reader check: Love and Relationships guide (final pass)

Read the whole of build_lr/out/guide.html as the student would: front, all 15 poem pages, 3 model answers, glossary and sources. All fixes were made in the source files (content/*.json, parts/*.html). No new facts were added. Backups of the files before this pass: content_bak_readercheck/, parts_bak_readercheck/.

## Fixes made

| # | Where | Problem | Fix |
|---|---|---|---|
| 1 | 9 copyright poems (Singh Song!, Winter Swans, Letters From Yorkshire, Mother any distance, Follower, Walking Away, Eden Rock, Before You Were Mine, Climbing My Grandfather), `poem_intro` | The copyright notice appeared twice in section 2, because the template adds its own copy | Cut `poem_intro` back to "Highlighted words are the ones worth quoting in the exam." Now there is one notice per poem (9 in total) |
| 2 | neutral-tones title note | Showed "our reading (our reading)" | Removed the duplicate label |
| 3 | climbing-my-grandfather title note | Showed "our reading (AQA anthology; our reading)" | Removed the duplicate label. Source now reads "our reading, from the AQA anthology text" |
| 4 | Title notes for follower, walking-away, letters-from-yorkshire, mother-any-distance | Brackets inside brackets, e.g. "(AQA anthology (our check of the text))" | Simplified the source lists |
| 5 | mother-any-distance (6 places) | "Oak National Academy video Armitage's own words, one source (Oak National Academy video)": the source was named twice | Changed the label to "Armitage's own words; one source" (the source is still named next to it) |
| 6 | before-you-were-mine (about 12 places) | The long label "Duffy's words as quoted in a University of Glasgow guide (one source)" was repeated next to an identical source | Shortened to "Duffy's words, quoted by the University of Glasgow; one source" |
| 7 | mother-any-distance timeline | "May 2017" did not match "June 2017" everywhere else | Changed to "2017 · Printed on the AQA GCSE exam (June 2017 series)" |
| 8 | sonnet-29 "In the exam?" | "Paper 1P" was jargon that is never explained | Changed to "on the separate Covid-era poetry paper", which matches the front section |
| 9 | walking-away setup | "(Day Lewis wrote it for his own eldest son.)" was stated as fact, but the same page labels it "one source" | Changed to "(One source says Day Lewis wrote it for his eldest son.)" |
| 10 | winter-swans, comparison with Love's Philosophy | "Both end with an image of two becoming one" contradicted the next line, which says Love's Philosophy ends on an unanswered question | Changed to "Both use an image of two becoming one" |
| 11 | follower context | "Writing about Ireland in 1926, a farmer notes…" while the source is dated 2026, which is confusing | Changed to "A farming article describing Ireland in 1926 notes…" |
| 12 | follower context (3 places) | "(published journalist's interview, on his own website)": it was unclear whose website | Changed to "(published on the journalist's own website)" |
| 13 | parts/model_follower.html, paragraph 1 | "Heaney describes his father's “His shoulders…”" was ungrammatical | Changed to "Heaney describes his father: “His shoulders…”" |
| 14 | parts/model_follower.html, paragraph 4 panel | The "[ABAB] is best avoided" quote is from the 2022 report on the Power and conflict question, but it read as Love and Relationships advice (the front section quotes the 2022 report on Sonnet 29's ABBA) | Labelled "Examiners (2022, writing about the Power and conflict question)" |
| 15 | parts/back.html Sources | "(sample text)" was unclear. The Background line was repetitive ("named beside each fact … named beside its fact") and said "the exam boards" | Changed to "(free PDF from AQA)". Reworded the Background line once, without "exam boards" |

## Checked, no change needed
- Front theme-map table compared with each poem's "In the exam?" box and its partner lists (years, printed poems, AQA wording): consistent. Spot-checked against lr/exam_materials_lr.md, e.g. Farmer's Bride and Winter Swans in the 2017 mark scheme are correct.
- Farmer's Bride: "1912 or 1913" is used on the page, in the timeline and in the model answer. It is never given as a single year.
- Letters From Yorkshire: the relationship is kept open throughout ("AQA's reading", "never named"). The book is marked "not confirmed" in the header and timeline.
- Walking Away: only the publication year (1962) is given. The page says the date of writing and the date of the game are unknown.
- Stand-alone use: there are no file or folder names, no "brief", agent, "verify" or process notes, and no family names. Physics & Maths Tutor appears only in the back Sources list.
- Rendering: no "undefined", "None" or "null", no empty brackets, empty spans or list items, no escaped tags, and no duplicate headings.

## Left as is (noted)
- On Eden Rock's last block the section label reads "Lines 20". The "Lines" prefix comes from the renderer template, so it is not a content issue and was not changed.
- Model answers quote the Level 6 wording from the 2025 mark scheme ("argument"). The Farmer's Bride model quotes the older wording ("comparison"). Both are accurate for their sources.

## Final run
`python3 render.py && python3 final_check.py`: 15 poems; 1294 quotations checked, 0 failures; no banned strings; the longest copied run from a copyright poem is 9 words (limit 10).
