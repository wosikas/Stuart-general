# Verify log: lr/exam_materials_lr.md and lr/theme_tags_lr.md

Independent check, 6 Oct 2026. Method:
- All 15 AQA filestore PDFs were re-downloaded directly from filestore.aqa.org.uk into `vlr/dl/`. Their md5 hashes match the `dl/` copies byte for byte.
- All 10 PMT PDFs (QP/MS 2017, 2018, 2019, 2024, 2025) were re-opened through WebFetch. WebFetch could not read the text, but it saved the binaries, and their md5 hashes match the `pmt/` copies byte for byte.
- Text was re-extracted fresh (pdftotext, raw and layout) into `vlr/txt/`. Every quoted string was then checked by script against the specific PDF it is attributed to (`vlr_tools/attr.py`, `vlr_tools/qchk.py`).
- The printed poems were diffed line by line against the layout text, and the count of indicative-content bullets was checked per mark scheme (`vlr_tools/bul.py`). The partner tally was recomputed (`vlr_tools/tally.py`).

## FIXED
1. **exam_materials §0 and Conflicts.** The file said question papers always write "Mother, any distance". In fact the **June 2019 QP poem list prints "Mother, Any Distance"**. Both places have been corrected. The Conflicts line now also notes that ER-N20 and ER-J22 use the lower-case form.
2. **exam_materials, June 2018 Singh Song! GAP resolved.** Page 18 of the PMT QP18 was rendered as an image. **No title is printed above the poem**: it appears only in the question, and "Daljit Nagra" is printed after the last line on p. 19. The note and the Gaps entry have been rewritten.
3. **exam_materials Conflicts.** "Cecil Day Lewis (anthology TG)" has no opened source in this pass, so it is now marked as not re-checked.
4. **theme_tags, strict rule.** Four tags rested on AQA words that do not name the idea, so they were removed and moved into notes as "not AQA-backed / our reading":
   - Love's Philosophy → Rejection and heartbreak ("negative types of powerful feelings")
   - Porphyria's Lover → Identity (an AO2 first-person method bullet; the file's own rule excludes method bullets)
   - The Farmer's Bride → Desire ("mounting tension and frustration")
   - Walking Away → Loss ("sadness of the parent")

   The theme map, the Gaps entry and the mapping-review list were updated to match. **Loss now has no AQA-backed poem.**
5. **theme_tags: unflagged mappings now marked (mapping)/\*.**
   - Sonnet 29 Nature from ER-J22 "vines"
   - The Farmer's Bride Identity ("individuality")
   - Singh Song! Identity ("difference between people")
   - Follower Identity ("self")
6. **theme_tags Takeaway.** It said partners stay in the same strand "in every MS and ER". That was false: MS17 suggests Winter Swans and The Farmer's Bride for a growing-up question, and MS-N21's AO2 bullet suggests Walking Away and Mother, Any Distance for a romantic question. Reworded to "almost always", with the two exceptions named.
7. **theme_tags title-spelling note.** Added the June 2019 QP exception.

## CARE
- Some mappings were kept but are judgement calls (all marked \*):
  - Sonnet 29 Separation ("in his absence" is a reading the report records, not one it endorses)
  - Sonnet 29 Longing ("fantasising about him")
  - Mother, any distance → Power and control ("constriction")
  - Neutral Tones → Rejection and heartbreak ("ending of a relationship")
  - Commitment rows ("lasting nature", "more established relationships")
- Climbing My Grandfather is tagged "Family (parent and child)", but it is a grandparent poem. AQA's word is "adult family figure".
- Letters From Yorkshire: AQA's only source (the specimen mark scheme, SMS) reads it as presenting a "parent". Check this against the poem.
- The June 2024 PMT QP footer reads "IB/G/Jun23/8702/2R", and the MS reads "8702/2R – JUNE 2024". Both were confirmed in the files, but the reason is unexplained.
- Printed-poem indentation is not reproduced. The text agrees exactly with the PDFs, apart from the margin line numbers and one page footer inside the Farmer's Bride page break.
- PMT files could only be checked as binaries through WebFetch, which returned no readable text. The verification relies on the hash match plus local extraction.

## OK (confirmed verbatim against the attributed PDF)
- All 10 L&R question wordings (SQP, 2017, 2018, 2019, Nov 2020, Nov 2021 1P Q01, June 2022 1P Q01, 2023, 2024, 2025). Also the cover dates, IB codes, the 50-minute / 30-mark 1P details and the 1P contents tables.
- The printed-poem table: printed poems, titles above the in-copyright poems, and the opening phrases. Follower is identical in the SQP and 2025. The -CR files print Walking Away, Before You Were Mine and Sonnet 29 in full; only Bayonet Charge (J22) and the Section C extract (N20) are withheld.
- Full texts of The Farmer's Bride (Nov 2021), Sonnet 29 (June 2022) and Neutral Tones (June 2024): every line, in order.
- The poem list (June 2025 QP) and the SQP variants ("C Day Lewis", "Letters From Yorkshire", Mew before Dooley).
- Mark-scheme grid headings for all 10 mark schemes, and the indicative-content preamble.
- Every indicative-content bullet in all 10 mark schemes. Bullet counts are complete (SMS 13, MS17 12, MS18 12, MS19 13, N20 12, N21 12, J22 12, MS23 14, MS24 14, MS25 13), with no omissions. The [sic] missing quote mark in MS19 is real.
- The suggested-partner lists and the §2c tallies (recomputed, all correct). The cross-over statement is also correct.
- Every examiners'-report passage (ER-N20, ER-N21, ER-J22, ER23) is verbatim and in the section claimed. This includes "famer’s" [sic] and the ellipsis passage in ER-N21.
- The exemplar commentary quotations in §4.
- Every verbatim phrase in theme_tags_lr.md is found in the PDF it is attributed to.
- The negative claims hold: no AQA document ties When We Two Parted to heartbreak or separation, Porphyria's Lover to possession or control, or Eden Rock to death or loss, and no examiners' report mentions Letters From Yorkshire.
- The focus count (Romantic ×5, Family ×3, Growing up ×2) and the past-question → partners table.

Backups of the pre-fix files: `vlr/exam_materials_lr.bak`, `vlr/theme_tags_lr.bak`.
