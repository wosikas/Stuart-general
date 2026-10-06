# Brief: independently verify one poem page

Base: /tmp/claude-0/-home-user-Stuart-general/9238462c-e100-5e4e-81b8-d3616f26c44e/scratchpad
You are an independent checker. Assume the page contains errors. Read pc/RULES.md and build/SCHEMA.md.

Inputs: build/content/<slug>.json (the page), pc/context_<slug>.md (the writer's research notes), pc/anth.txt (AQA anthology = master wording), pc/exam_materials.md (verified AQA text), pc/theme_tags.md (AQA-backed theme tags), pc/verify*.md (earlier corrections).

Check and FIX IN PLACE (edit the JSON directly; keep it valid):
1. Every quotation (<q>, quotes[].q, <mark>, poem_blocks text) matches anth.txt exactly. For copyright:true poems, no quotation run longer than ~12 consecutive words of the poem anywhere.
2. Every context item: re-open its source URL (from the research notes) and confirm the page really says it. Overclaims → reword or add "care". Unsupported → delete. Blocked site → keep only if the research notes give an exact sentence and label it accordingly.
3. Theme tags: aqa:true only if theme_tags.md supports it for this poem; otherwise set aqa:false, src "our reading".
4. Every AQA quote or claim ("AQA: 2018 mark scheme", examiners' report quotes, "printed in …") matches exam_materials.md.
5. Readings and plain-English summaries: no misreadings of the poem (read it in anth.txt). Line numbers in the synopsis match anth.txt.
6. Form claims (stanza counts, rhyme, metre, person) match the text or a cited source.
7. Plain English for a 15–16-year-old; jargon explained.
8. No family names, file paths or study-guide sites cited as sources (York Notes, LitCharts, SparkNotes, BBC Bitesize, Save My Exams; PMT only as a lead, never as the sole source of a fact shown).

Write a short log to pc/verify_page_<slug>.md (FIXED / CARE / OK). Validate JSON. Return 5 lines: number of fixes and the most important ones.
