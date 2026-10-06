# Final reader check (first-time 15-year-old reader)

Scope: all content/*.json except poppies.json (being edited by another checker), plus parts/front.html, models.html, model_ozymandias.html, model_remains.html, model_storm.html, back.html. No new facts were added, and no quotations, sources or labels were changed. The only exception is one quotation that was shortened to a verbatim sub-phrase (noted below).

## Fixes made

### Errors an examiner would mark down, or that would mislead a student
- **back.html glossary, Enjambment:** the example was "I gave commands; / Then all smiles stopped together." That line is end-stopped by a semicolon, so it is not enjambment. Replaced it with "a one-way / journey into history" (Kamikaze), which the guide already uses as enjambment.
- **model_ozymandias.html:** the quotation "The curtain I have drawn for you, but I)" carried a stray bracket from the poem's parenthesis. Shortened it to the verbatim "The curtain I have drawn for you".
- **model_ozymandias.html:** "rulers should despair, but because their works will crumble too" was garbled. Changed to "...but only because...".
- **model_storm.html:** the answer claimed Heaney's islanders "survive". The poem never says this. Changed it three times (plan, introduction, conclusion) to "are left alive" / "nobody dies". This is consistent with the Storm page ("no one dies in Storm").
- **model_remains.html:** "a short final couplet" could be read as a rhyming couplet. Changed to "a short two-line final stanza", which matches the Remains page.

### Contradictions between pages
- **Ozymandias page vs My Last Duchess page and the 2023 report:** the Ozymandias page called MLD "the most popular partner in 2023". The 2023 report says "‘Ozymandias’ and ‘London’ were the most popular choices". Changed to "one of the two most popular partners in 2023, with London".
- **Checking Out Me History page vs The Emigrée page:** the CoMH page said "Rumens ends threatened". The Emigrée page reads the ending as defiant ("evidence of sunlight"). Reworded the CoMH point: the speaker is still under threat at the end, though she holds on to her "sunlight".
- **Storm page exam thesis:** it said the islanders fear an enemy "that might strike". That contradicted the Storm, Ozymandias and Prelude pages, which say the storm attacks now. Changed to "are terrified by an invisible enemy, while Owen's soldiers are actually being killed by it".

### Consistency with front.html
- **"Which poem do I use?" table (id=partners):**
  - Every row's partner matches the facts.partner on its poem page. Poppies matches by its facts field, which I read for this check only and did not edit.
  - Fixed the "Backed by AQA?" column where it contradicted the poem pages and exam_materials.md:
    - The Emigrée → Remains: changed "Our suggestion" to "Yes: Nov 2020 mark scheme (Remains question)".
    - Checking Out Me History → Ozymandias: changed "Our suggestion" to "Partly: specimen mark scheme (one method bullet)".
    - Poppies → Remains: changed "Our suggestion" to "Partly: both named in the 2017 mark scheme". That mark scheme names them as options for the Bayonet Charge question, not as a pair.
    - Tissue → Ozymandias: changed "Yes" to "Partly: specimen mark scheme (one method bullet)", in line with the Tissue page, which calls it a weak link.
- **Theme map (id=themes):**
  - Added London to the "Effects of conflict / difficult experiences" row. The London page has a solid Difficult experiences tag (Nov 2020 mark scheme).
  - The Patriotism row listed Charge and Exposure as AQA-linked. On both pages that tag is dashed (our reading). Reworded it to "Bayonet Charge (our reading also fits The Charge of the Light Brigade, Exposure and Kamikaze)".
  - Every other solid tag checked against the map: no contradictions.

### Readability: jargon now explained
- Everyman (Bayonet Charge)
- Emancipation and guerrilla warfare (CoMH)
- Assonance (Exposure)
- Translucent (Kamikaze)
- Radical (London, Ozymandias)
- Sardonic (London)
- Auditors and discourse (MLD)
- Anecdote (Remains)
- Caesurae changed to "mid-line stops (caesuras)" and sectarian explained (Storm)
- "Mile after mile" changed to "on and on" (Charge: half a league is not miles)
- Nostalgic (Emigrée)
- Exaltation of emotion over reason (Prelude)
- Fundamentalism and received ideas (Tissue)

## Checked, no change needed
- Shared facts agree across pages:
  - Troubles 1968–98, about 3,600 killed (Storm, War Photographer)
  - Tennyson wrote "a few minutes after" reading The Times (Charge, Exposure)
  - Armitage succeeded Duffy in 2019 (Remains, War Photographer)
  - Owen in the snow in January 1917 (Exposure, model 3)
  - The 2022 "worked well" for Remains with Bayonet Charge (front; confirmed in exam_materials.md)
  - The 2022 "more reflective stance" (Remains, War Photographer)
  - The exam table of questions and themes
- "(see model answer 3)" correctly points to the Exposure/Storm model (render order: ozymandias, remains, storm).
- Rumens 1944–2026 is sourced in context_the-emigree.md (Bloodaxe and Telegraph obituary).
- Long sentences are mostly the "A sentence you could use" lines and verbatim AQA warnings. I left them, because they are model sentences or quotations.

## Unresolved (report only)
- The Prelude quotes the same line two ways: "Foster'd alike by beauty and by fear" (cards.why) and "Fostered alike…" (context, ao3). It is probably 1805 vs 1850 text. Not verified, so not changed.
- War Photographer: the WJEC quote spells "Phillip Jones Griffiths" and the guide's own text spells "Philip". The quote is verbatim, so it was left.
- model_remains.html shows some quotations inside &lt;q&gt; without curly quote marks inside. This is a style issue against SCHEMA.md; the wording is unchanged.
- poppies.json was not read for readability or contradictions, as instructed. The Kamikaze and War Photographer pages' readings of Poppies ("Weir ends in hope and longing", "full of love and fear") need checking against the Poppies page by its checker.

## Validation
- All 15 JSON files parse.
- `python3 render.py && python3 final_check.py`, first 3 lines:
  - wrote guide.html 15 poems
  - quotations checked: 1095; failures: 0
  - banned strings in guide.html: none
