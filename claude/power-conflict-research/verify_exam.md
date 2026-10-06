# Verification of exam_materials.md

Checked 6 Oct 2026 by an independent checker.

**Method**
- **AQA filestore:** all 18 filestore PDFs cited in the file were re-downloaded directly from filestore.aqa.org.uk (all returned HTTP 200, application/pdf). This includes the 8702/2 Nov21 and Jun22 question papers used for the Covid check.
- **PMT:** the 10 PMT PDFs (June 2017, 2018, 2019, 2024 and 2025, QP and MS) were re-opened with WebFetch. WebFetch saved each binary PDF, and the text was extracted locally with pdftotext.
- **Quotes:** a script pulled every quoted string (≥8 characters) out of exam_materials.md. It checked each one (a) against all sources and (b) against the specific PDF the file attributes it to. Curly and straight quotes and whitespace were normalised; nothing else was.
- **Results:** 318 quoted fragments were found verbatim. Every miss was then inspected by hand (see below).
- **Printed poems:** each poem was also checked line by line, in order, against its PDF.

---

## SAFE (checked, correct)

**Source index and Covid claim (§0)**
- All filestore URLs resolve to the PDFs named.
- These files are absent (302 redirect to aqa.org.uk): AQA-87022-WRE-JUN17, -JUN19, -JUN24 and -JUN25; QP-JUN24; QP-JUN23 (non-CR).
- These files exist: AQA-87022-WRE-NOV21 and -JUN22.

**Power and Conflict on 8702/1P in Nov 2021 and June 2022: CONFIRMED**
- **The two 8702/2 papers have no anthology question.** AQA-87022-QP-NOV21 and AQA-87022-QP-JUN22 are both titled "Paper 2 Shakespeare and unseen poetry". Each is 1 hour 45 minutes and 70 marks, with the rubric "Answer one question from Section A and both questions in Section B." Section B is "Unseen poetry" (07.1/07.2).
- **8702/1P front pages:** AQA-87021P-QP-NOV21 (header IB/M/Jun21) and AQA-87021P-QP-JUN22-CR (IB/M/Jun22) both read "Paper 1P Poetry anthology", "Time allowed: 50 minutes", "Answer one question.", "The maximum mark for this paper is 30."
- **Question 1 is Love and relationships on both papers:** Farmer's Bride in Nov 2021 and Sonnet 29 in June 2022.
- **Question 2 is Power and conflict on both papers:** London in Nov 2021 and Bayonet Charge in June 2022.
- **The reports confirm the series.** They are headed "8702/1P – NOVEMBER 2021" and "8702/1P – JUNE 2022". The quotes "least popular choice" and "lowest entry of the options offered" are both verbatim.

**Q26 / Q02 question wording (§1)**
- All 10 question wordings are verbatim from the correct PDFs: Specimen, 2017, 2018, 2019, Nov 2020, Nov 2021 1P, June 2022 1P, 2023, 2024 and 2025.
- Headers and dates are correct:
  - Jun17: Friday 26 May 2017
  - Jun18: Friday 25 May 2018
  - Jun19: Thursday 23 May 2019
  - Jun20: Thursday 21 May 2020
  - Jun25: Tuesday 20 May 2025
- The 2024 PMT file reads "Paper Reference is 8702/2R" with footer "IB/G/Jun23/8702/2R". The MS header reads "8702/2R – JUNE 2024".
- The opening phrases of the in-copyright poems (Hughes, Duffy, Armitage, Garland) are verbatim.
- The June 2022 -CR note "Poem not reproduced here due to third-party copyright restrictions" is verbatim.

**Printed poems**
- These match their PDFs line for line and in order (the PDF line numbers are omitted, which is fine):
  - Ozymandias (SQP)
  - London (Nov21 1P)
  - My Last Duchess (Jun23 -CR, including the "Ferrara" subtitle)
  - Exposure (Jun25)
- The SQP vs 2018 Ozymandias differences were confirmed by a side-by-side diff: shatter'd/shattered, "lip and"/"lip, and", stamp'd/stamped, mock'd/mocked, mighty/Mighty. All other lines are identical.

**Other §1 facts**
- The SQP list names "The Prelude: stealing the boat" and "The émigree". This is verbatim.
- The 2025 question numbers are confirmed: Q25, Q26, Q27 ("Worlds and lives"), then 28.1 and 28.2.

**Level descriptors (§2a)**
- All Specimen Level 6–1 headings, AO bullets, and top-of-level and bottom-of-level text are verbatim from AQA-87022-SMS.
- The June 2025 Level 6 and Level 5 text, the preamble and the rubric-infringement sentence are verbatim from the PMT MS25.
  - The script first flagged three lines here. That was only a pdftotext line-break artefact in "themes/ideas/ perspectives". The wording is correct.
- 2017 matches the specimen. In 2019 the AO2 bullet reads "Exploration of effects of writer's methods to create meanings". Both are correct.
- The note that 2025 has "argument" (no "well-structured comparison") and adds "themes/" is correct. 2023 and 2024 have "ideas/perspectives/…" without "themes".
- The indicative-content preamble is present in every mark scheme checked: SMS, 2017–2019, Nov20, 1P Nov21, 1P Jun22, 2023, 2024 and 2025.

**Indicative content (§2b)**
- Every AO1/AO2/AO3 bullet for all 10 series is verbatim and comes from the attributed mark scheme. This includes AQA's own slips, such as "war effects a change of attitude" and the spelling "The Émigré" (2017).

**Examiners' reports (§3)**
- Every quote is verbatim from the attributed report: Nov20 8702/2, Nov21 1P, Jun22 1P and Jun23 8702/2. This includes "Kamizaze" [sic], which really is the misspelling in the PDF.
- I scanned the Nov21 and Jun23 reports for Power and Conflict poem names. No relevant passage was missed.

**Exemplar commentary (§4)**
- These are all verbatim in AQA-8702-EX-COMMENTARY.PDF:
  - the opening of the exemplar
  - margin comments 34–42
  - the Commentary paragraph
  - the 23.75% and 18.75% figures
- The PDF gives no mark or level and does not say the response is a real candidate's script. Both points are confirmed.

**Specification (§5)**
- These are verbatim from AQA-8702-SP-2015.PDF (Version 1.3 28 September 2022):
  - the Paper 2 summary
  - the Section B sentence
  - 3.2.2
  - the cluster list, including "Worlds and Lives (First teaching 2023, first exam 2025)"
  - "study all 15 poems"
  - the AO1, AO2 and AO3 definitions
- The 2025 QP front-page lines "maximum mark for this paper is 96" and "30 marks for Section B and 32 marks for Section C" are verbatim.
- The 15-poem list on the live papers is correct.

---

## USE WITH CARE

1. **§2a line 279, "In June 2023 'language and form and structure' became 'analysis of methods'."** This is misleading about timing. The wording "insightful analysis of methods" is already in the June 2020 MS (used Nov 2020), and also in the 1P Nov21/Jun22, 2023, 2024 and 2025 schemes. The MS for 2017, 2018 and 2019 still read "language and form and structure". Suggested wording: "From the June 2020 paper (sat Nov 2020) onward …".
2. **§3 Nov20, "Section B: This section of the paper…"** In the PDF, "Section B" is a heading on its own line with no colon. The words after it are verbatim. Don't put "Section B:" inside the quotation marks.
3. **§3 Jun23 thesis-statement quote.** The PDF has a capital Y: "You can then use this to come up with a short answer…". The file has "you".
4. **§4 line 397.** "There will be a full list of poems…" and "The named poem will be printed on the question paper." are two separate sentences on the page, with margin comments between them. Each is verbatim, but they should not be quoted as one continuous passage.
5. **§4 line 392, question wording.** In the exemplar PDF the question carries superscript comment markers ("Compare34 … present35 … power36"). The words are correct with the markers stripped.
6. **§5 lines 405 and 407.** The spec has "(page 11)", "(page 12)" and "(page 13)" after each "What's assessed" bullet. "3.2.2 Poetry" is a heading with no colon. These page references were silently dropped.
7. **§5 line 411.** The file says only 2025 prints "Extract from, The Prelude" (with the comma). The 2017 and 2024 papers (PMT) print it the same way. 2018, 2019, 2023 and the 1P papers have "Extract from The Prelude". The SQP list also puts Kamikaze before Checking Out Me History. These are trivial differences.
8. **§3 Jun23 comparison quote, "written under the L&R paragraph but about Section B generally."** The passage really does come straight after the Love and relationships paragraph. Its wording is general ("students", "comparison is not a discrete AO"), so reading it as general advice is reasonable. It is still an interpretation, not stated by AQA.
9. **§4 caveat for the student (not an error in the file).** AQA's own exemplar contains slips:
   - It says the Duchess's "kindness and gentle spirit (white pony)". The poem says "the white mule".
   - It quotes Ozymandias's "lands". The poem has only "antique land".

   If this exemplar is shown to the student, warn him not to copy these.
10. **PMT-only items.** The 2017, 2018, 2019, 2024 and 2025 QP and MS text was verified against PMT copies only, because AQA filestore redirects. The copies are clearly AQA PDFs (AQA headers and codes) but they are a secondary host.

---

## DROP / FIX

- **None required.** No wrong quotation, wrong attribution or wrong question/poem pairing was found.
- The only substantive correction is item 1 above: date the "analysis of methods" wording change to the June 2020 paper (Nov 2020), not June 2023.

---

## Gaps and conflicts
- GAP (confirmed): the 8702/2 examiners' reports for June 2017, 2019, 2024 and 2025 are not on the public filestore (302 redirect). June 2018 was not re-probed.
- CONFLICT (confirmed, real): the Ozymandias text differs between SQP and 2018, and poem-title spellings vary across papers.
- NOTE: the June 2024 PMT paper has no exam date on its cover. The year is attributed only from the MS header "8702/2R – JUNE 2024".
