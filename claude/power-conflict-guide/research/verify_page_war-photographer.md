# Verify page: war-photographer (independent check, 2026-10-06)

Quotations: every <q>, <mark>, quotes[].q (War Photographer + Remains, Poppies, Bayonet Charge partners) re-checked against anth.txt: all match. Line numbers in synopsis/quotes/blocks match anth.txt (24 lines, 4 x 6). Longest consecutive run from the poem in the page JSON now 10 words (was 12).

Sources re-opened (WebFetch): WJEC fact sheet PDF (read with pdftotext), Oak National Academy lesson, Tate Britain McCullin page, Tate Liverpool exhibition guide, Tate Etc. issue 45 interview, Britannica (Troubles, Lebanese Civil War, Khmer Rouge), poets.org.

## FIXED
- quotes[6]: 12-word run "The reader's eyeballs prick / with tears between the bath and pre-lunch beers." -> "eyeballs prick / with tears between the bath and pre-lunch beers." (10 words). No other source file carries the 12-word run (parts/model_remains.html already uses the 10-word form). out/*.html are stale until re-rendered.
- Labels: Tate items split correctly: Tate Britain ("foremost war photographer", "own darkroom", Northern Ireland), Tate Liverpool exhibition guide ("eighteen years", Beirut, Cambodia), Tate Etc. = Tate's magazine, issue 45 (2019), interview by Simon Grant ("gut-wrenching…", "make life uncomfortable on a Sunday morning"). Oak items labelled "Oak National Academy lesson"; both Oak quotes confirmed verbatim.
- Darkroom quote: page reads "all printed by McCullin himself in his own darkroom" (lower case, mid-sentence) -> quoted as such and attributed to Tate Britain.
- "gut-wrenching" quote: context added (dying children, Biafra, 1969) per the interview.
- Timeline "1960s–80s": end date unsourced -> "From 1960s" (Tate: "From the 1960s"; Tate Liverpool: eighteen years at the magazine).
- Form explain item 3 (general claim that poets use strict form to contain feeling): unsourced -> reworded, labelled "our reading".
- "sought approval": poem does not say from whom; synopsis step and block note no longer say he asked "her permission" / man "bled to death" -> "sought approval (perhaps from her)"; blood "soaked into the dust".
- poets.org "social critique" item: care extended (link to this poem is our reading).

## CARE (kept, labelled)
- Jones Griffiths as inspiration: WJEC only. McCullin: WJEC + Oak ("may be based on").
- Tate Etc. quotes: one interview (McCullin's own words).
- Phnom Penh death toll: Britannica 1.5–3 million vs WJEC "almost 3 million"; page uses Britannica, flagged.

## OK
- WJEC quotes verbatim in the PDF: "distancing effect", "semantic field of religion", "witness death, pain and suffering", "regularity and the routine nature of his job", "Each stanza focuses on a different aspect…", "strict, controlled structure contrasts…", "third person to reflect the detachment…", "risk their lives…".
- Britannica: Troubles "about 1968 to 1998", "Some 3,600 people were killed"; Lebanon 1975–90, >100,000 killed, 1982 siege; Khmer Rouge April 1975, 1.5–3 million. poets.org quotes verbatim.
- Themes match theme_tags.md (War, Effects of conflict, Difficult experiences, Conflict aqa:true with correct sources; Memory, Guilt, Place and home aqa:false).
- AQA quotes match exam_materials.md (QP J19, MS19 AO1/AO3, MS-J22 "more reflective stance", MS24, ER-N20 "bolted-on context"). Exam question verbatim June 2019.
- Form: 4 x 6 lines, couplets Mass/grass, feet/heat, must/dust, where/care; half-rhymes then/again, six/prick; third person: all correct. No banned sources, names or paths.
