# Loom market research: delta between v1 (2026-09-25) and v2 (2026-09-28)

Date: 2026-09-28. Inputs: v1 = /home/user/Stuart-general/loom-market-research-2026-09-25.md (Sonnet 5 readers, Fable 5.1 synthesis, Reddit via search snippets and the 53-item v3 pull); v2 = /home/user/Stuart-general/loom-market-research-v2-2026-09-28.md (Opus 5.5 readers and sweeps, three Fable 5.1 fact-checkers, Reddit from a full archive pull of six subreddits plus Mac runs on X, YouTube, TikTok and Instagram). Both read in full. No time or effort figures appear here; v2's S/M/L labels are quoted only as labels. Evidence is at the end.

## 1. Summary

1. Yes, v2 is deeper, and the depth is concentrated on the demand side: what users say they want and hate. v1's demand evidence was 53 mostly title-only social items plus search snippets; v2's is about 1,840 Reddit posts across six subreddits, 232 Mac-run items on four other platforms, and roughly 230 quotes grepped with 158 claims refetched.
2. Two new S3 themes with direct product consequences appear only in v2: search that fails on meaning ("art matches chart") and locked-down or offline use where nothing can be installed. Neither is visible in v1.
3. Three v1 demand verdicts reverse: quick capture (v1 "unproven demand", v2 S3 with real threads), table views (v1 "no user asked", v2 about 12 threads), and cited chat over notes (v1 gap #3, v2 a dated single-source want, replaced by "search that understands, not a ChatGPT clone").
4. Two v1 strengths weaken: edit-files-outside-vault falls from "confirmed with community weight" to "single vendor release thread"; the graph hairball critique is found to be entirely out of window.
5. The product table is more accurate in v2 (Heptabase MCP, Reflect Open, Mem's Claude connector, Tana pricing) because official changelogs replaced aggregator listicles and three checkers refetched them.
6. v2's ranking is longer (17 vs 12), adds sizes, and reorders around one new principle: history and export before any AI write; search before chat.
7. v2 drops things worth keeping from v1: the multi-provider ecosystem read (Hermes, Codex, Pi on one vault), the company-brain commercialisation signal, the Granola consent suits as backdrop to CR-097, cited chat over PDFs, and the explicit "contradiction flag" habit.
8. Attribution is judgement: the Reddit archive explains most of the reversals; the tighter prompt explains the dated/window discipline and the shape-based product and repo lists; the model change is hardest to isolate and shows mainly in tallying by distinct thread and discounting builder and creator posts.
9. Act on v2. Carry over the v1 items listed in section 7.

## 2. Findings new, dropped, and changed

| Finding | v1 | v2 | Status |
|---|---|---|---|
| Search fails on meaning; substring-only search | absent | H5 S3, gap #2 (full text) and #2b (meaning) | **New in v2** |
| Locked-down work machines; no install; browser access | absent | H8 S3, W10 S2; hosted web app becomes a stated strength | **New in v2** |
| Sync conflicts and data loss (not just sync price) | H2 was about price and lock-in only | H1 S3 with data-loss threads in r/ObsidianMD and r/Notion | **New in v2** |
| AI memory forgets or cannot be forgotten; vendor memory is the wrong layer | absent (one "context window is working memory" quote under H8) | H6 S2; feeds stand-out #4 | **New in v2** |
| Notion MCP prompt-injects ads (trust shock) | absent | W1, top r/Notion post, feeds stand-out #2 | **New in v2** |
| "AI as librarian, not co-author"; suggests, never writes; false-positive auto-links | W11 (assist, not replace) | W4 S3, sharper: search and link suggestions welcome, generated insights not | **Changed: refined** |
| Hide a folder or note from search and AI; `private:` flag | absent | W11 S2, gap #12; Reflect Open's private flag | **New in v2** |
| Vault-health report (orphans, broken links, stale) | absent | gap #10, repo gap #9 | **New in v2** |
| Reviewed / unverified badge as its own gap | inside stand-out #1 | gap #13 | **New as a gap** |
| Whole-vault export as a trust promise | "Portability on the tin" stand-out #8 | gap #4 paired with history; stand-out #3 | **Changed: promoted to a gap** |
| Kanban hygiene; AI on a selected passage | absent | repo gaps #11, #14; new CR candidates | **New in v2** |
| Switching patterns and Loves sections | absent | present | **New in v2** |
| Quick capture demand | W5/H1: strong product evidence, "none of 53 social items", downgrade CR-092 | W3 S3, about 16 independent threads plus 406/66 cross-check; gap #3 | **Reversed: up** |
| Table views demand | W7: "No user asked for tables in the window" | W8 S2, about 12 r/ObsidianMD threads; CR-081 label out of date | **Reversed: up** |
| Cited chat over notes and PDFs | W2 S3; gap #3; new CR candidate "Ask my notes" | not a gap; "NotebookLM-style Q&A" listed as S1 dated; W4 says "not a chatgpt clone" | **Reversed: down** |
| Edit files outside the vault (CR-095) | "confirmed with real community weight", 1,113 upvotes | gap #14 Low; "single vendor release thread"; score is a snapshot (939 to 1,131) | **Changed: down** |
| Graph hairball | H6 S1 to S2, "structural critique no product has answered"; stand-out #5 | L3 contested; every hairball criticism is dated; gap #17 needs his input | **Changed: down** |
| Resurfacing / "what should I do now" (CR-099) | upgraded to S3 by the v3 merge | W7 S2; "resurfacing" itself S1 (creator funnels) | **Changed: down** |
| Web clipper (CR-098) | bundled with capture at gap #4, S3 on product evidence | S1, gap #15, "do not prioritise" | **Changed: down** |
| Encryption (CR-068) | W6 "strongest signal in v3 for CR-068" | S1 to S2, gap #16 Low, conflicts with server-side search | **Changed: down** |
| Guardrails on AI writes (diff, provenance) | W4 S3 fetched, "expert want" | W5 S2 in window plus dated HN and READMEs | **Changed: slightly down, same reading** |
| LLM wiki pattern | W1 S3 fetched; gap #2 | W2 S3 for the pattern; "independent user voices fewer than the post count suggests"; gap #5 | **Changed: same strength, more hedged** |
| Version history | gap #6, "prerequisite for #2" | gap #4, "prerequisite for any AI write", bundled with export | **Changed: up** |
| Import AI chat history | gap #12, new CR candidate | W6 S2; merged into gap #6 with CR-089 | **Changed: merged** |
| Hermes and multi-provider agents on one vault | ecosystem note; supports CR-089 | one X mention (omx0r, 1 like); CR-089 supported by low-engagement posts | **Dropped in substance** |
| Company brain (Almanac, ssp.sh) | W14 S3 adjacent | absent | **Dropped** |
| Granola / Otter / Fireflies consent suits | H4 backdrop | absent | **Dropped** |
| Whiteboard / canvas | W10 S3 on products; gap #10 | absent | **Dropped** |
| Voice capture | W8 S2 vendor-driven | S1 weak want | **Changed: down** |
| Citation-aware research notes (Lattics) | W13 S1 | folded into W9 (PDFs and files with notes around them, S2) | **Merged** |
| Building the knowledge base is itself the friction | H10 S2 | folded into W3 "no filing decision" | **Merged** |
| Part 0 inventory of the v3 pull | full section | one row in the evidence table | **Dropped as a section** |
| Notion as a profiled product | profiled | reference only (out of scope by D-111/113/114) | **Dropped** |
| Repos by raw star count (MCP servers monorepo, AppFlowy, AFFiNE, mem0, Joplin, Outline) | top 10 by stars | excluded by shape; replaced by basic-memory, obsidian-second-brain, llm-wiki-agent, SilverBullet, Trilium, Smart Connections, Copilot | **Changed: selection rule** |

## 3. Recommendation rankings side by side

| v1 rank | v1 gap | v2 rank | v2 gap | Moved | Why |
|---|---|---|---|---|---|
| 1 | Vault over MCP / API, read first | 1 (L) | Per-person MCP / API, read first, propose-only tier | held | Both S3; v2 adds that all ten products ship one, the Notion ad-injection trust shock, and the D-170 Mac-dependency argument |
| — | — | 2 (M) | Full-text search index in D1 | new | H5 is invisible in snippets; only the archive shows the "art matches chart" threads |
| 8 | Semantic related-notes panel | 2b (L) | Search by meaning; related-notes suggestions | up | Attached to H5 and W4; v1 had it as "smallest AI feature that does not write" |
| 2 | Claude writes the wiki, with receipts | 5 (L) | Inbox that Claude distils, approve / reject / diff | down | Still S3 for the pattern, but v2 hedges the user-voice count, makes history (#4) a prerequisite, and names the D-131 block |
| 3 | Cited chat over notes and PDFs | — | (not ranked) | out | Demand evidence reclassified as dated and single-source; users ask for search and a librarian, not a chat clone |
| 4 | Quick capture + web clipper / send-a-link-in | 3 (M) and 15 (M) | Quick capture, phone-width, Inbox-first; web clipper separately | split | Capture demand now S3 from Reddit; clipper stays S1, so v1's "send-a-link-in first" advice is reversed |
| 5 | Table views over properties | 9 (M) | Views over properties, tables, cards | down in rank, up in evidence | Now has user threads (S2) but is outranked by search, history and capture |
| 6 | Version history / restore | 4 (M+S) | Version history and a trust package with whole-vault export | up | Reframed as the guardrail people ask for most and the precondition for any AI write |
| 7 | Mobile/tablet browser story | 7 (L) | Mobile and offline | held, larger | v2 adds offline and the locked-down-machine angle (H8 S3) |
| 9 | Resurfacing / "what should I do now" | 8 (M) | "What matters now" and recent activity | held | Downgraded to S2; TaskFlow flagged as a builder post |
| 10 | Whiteboard / spatial canvas | — | — | out | No in-window demand; v1 already rated it low |
| 11 | PDF annotate, E2EE, publish | 11 (M) and 16 (L) | Import formats, PDF text, OCR, highlight-to-note; encryption | split | PDF held; E2EE demoted to S1 to S2 and Low fit |
| 12 | Import AI chat history | 6 (M) | AI world per person, more than Claude; import chat exports | up, merged | Joined to CR-089; W6 S2 |
| — | — | 10 (S) | Vault-health report | new | From repo READMEs and gist lint; no AI needed |
| — | — | 12 (S) | Hide from search and AI; `private:` flag | new | W11 S2; Reflect Open precedent |
| — | — | 13 (S) | Reviewed / unverified badge | new as a row | Was inside v1 stand-out #1 |
| — | — | 14 (L) | Edit files outside the vault | new row, Low | v1 treated it as confirmed under CR mapping; v2 ranks it explicitly and low |
| — | — | 17 (M) | Graph diagnostic lenses | new | Replaces v1 stand-out #5 "Map that prunes itself" with a smaller, contested-evidence item |

Stand-out features: v1 had eight; v2 has six. Kept in substance: the review boundary / diff-and-approve (v1 #1, #2 → v2 #1), the scoped agent contract (v1 #3 → v2 #2 propose-only tier), portable memory with provenance and staleness (v1 #4 → v2 #4), portability page (v1 #8 → v2 #3), capture that ends in use (v1 #6 → v2 #6). Dropped: "Your AI, not ours" as a stand-out (now gap #6), "Map that prunes itself" (now gap #17). New: "Search that finds the idea, then shows the source" (v2 #5).

The order of v2's "recommended next CRs" (MCP, full-text search, CR-092, CR-119 plus export, then CR-093/094 once D-131 is decided) differs from v1's implicit order (MCP, CR-094/093 with receipts, cited chat, capture) in one important way: v2 puts the two non-AI foundations (search, history) ahead of the AI writes, and puts capture ahead of the clipper.

## 4. Evidence depth compared

| Dimension | v1 | v2 |
|---|---|---|
| Social items | 53 from the v3 pull (Reddit 26, HN 16, YouTube 6, TikTok 3, Instagram 2, X 0); mostly title-only; 5 Reddit bodies removed; all 6 YouTube items outside the window | Reddit archive about 1,841 posts (r/ObsidianMD 500, r/logseq 21, r/Notion 484, r/NoteTaking 258, r/PKMS 78, r/ClaudeAI 500 of which 22 relevant) with 3,087 + 1,090 comments listed for two of them; Mac runs X 101, YouTube 61, TikTok 57, Instagram 13, Reddit 98 cross-check; plus the same 53-item v3 pull |
| Subreddits | r/PKMS (bulk), r/ObsidianMD, r/Zettelkasten, r/ClaudeCode, via the pull only | six read in full (r/ObsidianMD, r/logseq, r/Notion, r/NoteTaking, r/PKMS, r/ClaudeAI), coverage verdict PASS; r/Zettelkasten and r/ClaudeCode only via v3 |
| Reddit access | live pages blocked; quotes are WebSearch or last30days snippets | live pages still blocked; text is from Arctic Shift archive; scores are snapshots and said to be |
| Web sweep | about 10 supplement pages in the v3 file plus WebSearch snippets; Reddit, HN, Capterra, G2, Product Hunt, obsidian.md, notion.com, tana.inc blocked | hates: 9 pages plus 15 HN threads via Algolia; wants: 11 of 13 pages; LLM-wiki: 14 of 16 pages; HN reached via Algolia |
| Quote form | snippets unless marked "fetched" (gist, three repos) or "v3"; many quotes are from aggregator or competitor blogs (saner.ai, eesel.ai, aiproductivity.ai) | verbatim from the named source with post id, date, and score; vendor and competitor pages never stand alone; non-English quotes carry the reader's translation |
| Window discipline | "undated" marked; many 2025 and undated blog quotes counted toward S ratings | evidence window 2026-06-30 to 09-28; anything older marked [dated] and excluded from S counts |
| Strength rule | S = number of independent sources | S = independent non-vendor sources across platforms; builder and creator posts never sole support; counts are reader tallies of distinct threads |
| Products | ten from vendor listicles (Saner.AI ranks itself first); prices from aggregators | ten filtered by shape; official changelogs and pricing pages fetched 2026-09-28; Notion demoted to reference |
| Repos | top 10 by star count, fetched 2026-09-25 | 19 candidates via GitHub MCP search, READMEs via raw.githubusercontent.com, release atom feeds; selected by shape; excluded low-signal repos named |
| Fact-checking | one "skeptic pass"; corrections listed (about eight) but no count of claims checked | three adversarial passes: about 230 quotes grepped, 64 + 51 + 43 claims refetched; 3 attribution errors, 2 count problems, several paraphrases corrected; unverifiable claims labelled rather than dropped |
| Known thinness | v3 warns evidence concentrated in one source; 23 of 53 dated items in the last 7 days | r/ObsidianMD 500-post cap drops everything before 09-12; r/ClaudeAI three days; r/logseq 21 posts; tallies not re-tallied by checkers |

Net: v2 is deeper on demand (Reddit volume, platform spread, verbatim text) and on product facts (official pages, refetched). v1 is broader on ecosystem colour (Hermes, company brain, the lawsuits, the Odysseas and Dan Martell audiences) because it took the v3 pull's evergreen YouTube and HN items at face value; v2 discards most of that as dated or creator content. v1's Part 0 inventory is more transparent about the single raw file than v2's one-row treatment of it.

## 5. Corrections: v1 claims that v2's evidence overturns or materially qualifies

v2's fact-checkers checked v2's own sweeps, not v1; the list below is what a side-by-side reading shows. "Overturned" means v2's refetched evidence contradicts v1; "qualified" means v1 was true of its narrow data but not of the market.

| v1 claim | v2 finding | Verdict |
|---|---|---|
| Quick capture: "none of v3's 53 social items mention it, so it is a shipped feature, not a hot conversation"; downgrade CR-092 demand | About 16 independent threads across r/NoteTaking, r/Notion, r/ObsidianMD, r/PKMS; 1.14.0 quick-capture thread 406/66; W3 S3 | Qualified into reversal: the absence was an artefact of the 53-item pull |
| Table views: "No user asked for tables in the window" | About 12 r/ObsidianMD threads (1woxyrg 21/47, Rowbase 199/32) plus r/Notion | Overturned |
| "The recurring Reddit ask is 'I want ChatGPT/Claude to answer from my documents'" (timeln.app, undated); cited chat is gap #3 | In-window users say "search that understands your notes, not a chatgpt clone" and "I want a librarian, not a co-author"; NotebookLM-style Q&A rests on one dated XDA piece | Overturned in direction |
| CR-095 edit outside the vault "confirmed with real community weight: 1,113 upvotes / 99 comments" | Same thread shows 939, 1,113 and 1,131 across three snapshots; it is a vendor release thread and its comments are the only user voice; gap ranked Low | Qualified: the number is a snapshot and the weight is vendor-led |
| Graph hairball "a structural critique no product has answered" (aiproductivity.ai, 2026) | Every hairball criticism found is outside the window; graph is contested, loved on TikTok, asked for by Notion users | Qualified: not a live complaint |
| Heptabase: "No official API; community heptabase-mcp" | Official MCP that creates and edits notes (v1.105.0, 2026-08-24), CLI 0.6.0, ChatGPT plugin | Overturned |
| Heptabase pricing Pro $11.99 ($8.99 annual), Premium $23.99, Premium+ $71.99 | Pro $8.99 per 100 credits, Premium $17.99, Premium+ $53.99 (heptabase.com/pricing fetched) | Overturned on figures |
| Reflect: "$10/mo annual, no free tier; iOS only; no official MCP" | Reflect Open is MIT, plain files, free on Mac, BYO key with no Reflect server; the legacy app's MCP is dated and not in the Reflect Open README | Overturned for the product now relevant to Loom |
| Mem: "No MCP found" | Claude Connector exists (date not found); markdown export on every plan; offline on all platforms | Overturned |
| Tana: Plus $10 ($8 annual), Pro $18 ($14 annual) | Pro $20 early / $30, Max $80 / $120, confirmed by one checker, invisible to the other (JS-rendered) | Overturned, with v2's own caveat |
| Capacities: "Via MCP Chat Connectors (Pro)" | Hosted MCP at api.capacities.io/mcp, OAuth 2.1, read and write, `saveToDailyNote`; Plus $8.33 tier | Extended, not contradicted |
| Obsidian 1.14.0 iOS Quick Capture "shipped" (v1 treats it as GA) | 1.14.x is early access (Catalyst), not GA; mobile 1.14.0 dated 2026-09-02, widget 1.14.1 on 09-08 | Qualified |
| Obsidian has no CLI (not listed in v1's table) | Official CLI (requires app running) and headless Sync | Omission corrected |
| Karpathy gist treated as in-window fetched evidence with S3 | Gist itself is [dated 2026-04-04]; only its comments (09-10 to 09-23) count | Qualified (v1 did cite comment dates) |
| Guardrails on AI writes W4 "S3, fetched" | S2 in window; the HN threads v1 leaned on (47899844, 48351115) are dated | Qualified |
| E2EE "the strongest signal in v3 for CR-068" | About two independent HN voices in window, rest builder posts; S1 to S2 | Qualified |
| Absent from social items: "diff/approve or provenance for AI writes" | Present in window on X (obsidianstudio9 "append only"), gist comments, dev.to, YouTube | Overturned for the wider platforms |
| Resurfacing upgraded to S3 by the v3 merge | S1 for resurfacing proper (one independent comment; rest creator funnels); "what should I do now" S2 | Qualified |

Not overturned and consistent between the two: MCP as gap #1; the LLM-wiki pattern as the differentiator; CR-097's "AI must not think for me" as the dominant attitude (v1's R42 quote and v2's "generated notes are not notes", 355/44); Logseq's DB split as a cautionary tale; Obsidian Sync price tiers; SiYuan's agent direction; the smart-connections and basic-memory repos as references; Loom's markdown-on-R2 as a strength.

## 6. Attribution: model, data, prompt

This is judgement from reading the two reports, not a controlled comparison; the three changes were made together and no single-variable run exists.

- **Better Reddit data (largest share).** Every reversal in section 5 that concerns demand (quick capture, tables, search, sync data loss, locked-down machines, private flag, hairball recency) traces to threads that only exist in the archive pull. v1 had 26 Reddit items, mostly r/PKMS titles; v2 had about 1,840 posts across six subreddits plus comment text. A Sonnet reader with the archive would very likely have found H5 and H8; an Opus reader with only snippets could not have. The Mac runs on X and TikTok also supplied the in-window "append only" and "raw/ frozen" voices that let v2 keep W5 alive after discarding the dated HN threads.
- **Tighter prompt (second).** The 2026-06-30 window with [dated] marking, "vendor pages never stand alone", S/M/L sizes, products and repos selected by shape rather than listicle or star count, Notion demoted, Part 0 dropped, and the mandate for three adversarial fact-check passes are all framing choices. They explain the product-table corrections (Heptabase, Reflect Open, Mem, Tana) because checkers were told to refetch official pages, and they explain why v1's ecosystem colour (Hermes, company brain, lawsuits) disappears: it was dated or creator content under the new rule, not wrong.
- **Model change (smallest and least separable).** Where v2 reads better in a way the data and prompt do not force, it is in judgement calls: tallying distinct threads rather than counting items, separating "AI exists" from "AI is in the way and I can't remove it" and saying that rests on 3 comments in 2 threads, spotting that a Show HN quote was not Anytype's founder, noticing the same thread's score varies by snapshot, and hedging W2's user-voice count against its post count. Those look like reader quality. But v1's Fable synthesis already did similar hedging ("expert want, not a mass one", "contradiction flag"), so the synthesis layer did not change much; the reader layer did.
- **Fact-checkers.** Three passes versus one skeptic pass is a process change that belongs under prompt, but the specific catches (attribution errors, count problems, dated items sweeps had placed in window) are the reason v2's claims can be cited with less hedging than v1's.

If forced to a rough split for the difference in conclusions: data roughly half, prompt and process roughly a third, model the remainder. Treat that as an opinion.

## 7. Recommendation

Act on v2. Its ranking is built on demand evidence that v1 did not have, its product facts were refetched from official pages, and its ordering (search and history before AI writes; capture before clipper; MCP first) is the one that survives the fact-checks.

What v1 got right that v2 should keep or restore:

1. **Multi-provider ecosystem as the basis for CR-089.** v1's Hermes, Codex, Pi and Claude Code on one vault (TK62, NetworkChuck) is dated or creator content under v2's rule, but the design consequence (per-person AI world, not Claude-only) is still correct and v2 supports it only with low-engagement posts. Keep the argument even if the evidence is labelled dated.
2. **Cited answers over PDFs.** v2 rightly demotes chat-as-product, but Loom has PDF notes and v1's "citations link to the note/PDF page" is a concrete acceptance criterion for v2's gap #2b and #11. Keep it as a search feature, not a chat feature.
3. **Contradiction flags in-line.** v1 marked where product evidence and demand evidence disagreed at the point of the claim. v2 moves that into Caveats. Restore the in-line habit.
4. **Part 0 transparency about the raw pull.** v1's inventory table and "what v3 said then" made the single raw file's limits visible. v2's one-row treatment hides how thin the v3 pull was; keep a short inventory per raw source.
5. **Granola/Otter/Fireflies consent suits and Notion's AI pricing move as backdrop for CR-097.** They are out of window and allegations only, but they are the market context that makes "no AI unless I ask" a selling point, and v2's Help/FAQ promise (stand-out #3) would be stronger for citing them as [dated] context.
6. **Time-aware facts.** v1's stand-out #4 ("true as of" and "learned on" stored separately) is more specific than v2's "last confirmed" property. Fold the two-field design into v2's stand-out #4.
7. **Map that prunes itself.** v1's default-to-focus-mode design is a concrete answer to v2's "graph contested" verdict; v2's "diagnostic lenses" is vaguer. Keep v1's proposal as the candidate for CR-078/CR-125 discussion.
8. **Company brain as a commercialisation signal.** Out of scope for Loom, but v1's observation that the agent-over-markdown pattern is being sold to teams (Almanac, ssp.sh) is a market-direction fact v2 loses.

What v2 should also fix before it is treated as final: the r/ObsidianMD 500-post cap (nothing before 09-12), the three-day r/ClaudeAI sample, and the un-re-tallied thread counts; all three are disclosed in v2's Caveats and none changes the top five.

## 8. Evidence

- v1: /home/user/Stuart-general/loom-market-research-2026-09-25.md (303 lines, read in full). Sections cited: 1 Summary, 2 Part 0, 3 Part 1 (H1–H10, W1–W14, Ecosystem note), 4 Part 2 table, 5 gap ranking #1–#12, 6 stand-outs #1–#8, 7 repos, 8 CR mapping, 9 Caveats, 10 Evidence.
- v2: /home/user/Stuart-general/loom-market-research-v2-2026-09-28.md (404 lines, read in full). Sections cited: 1 Summary, 2 Evidence base table, 3 Part 1 (H1–H8, W1–W11, weak wants, L1–L3, switching, AI attitudes), 4 Part 2 table and cross-product facts, 5 gap ranking #1–#17, 6 stand-outs #1–#6, 7 repos and repo gaps #1–#14, 8 CR mapping, 9 Caveats, 10 Evidence.
- Figures quoted (53 items; 500/21/484/258/78/500 posts; 101/61/57/13/98 Mac-run items; about 230 quotes; 64 + 51 + 43 claims; 3 attribution errors; 2 count problems; 939/1,113/1,131 snapshots; 406/66; 355/44; 223/26) are as printed in the two reports and were not re-fetched or re-computed here.
- No web, Reddit, GitHub or product page was fetched for this delta; every claim is a comparison of the two documents.

Skills/MCPs used: Read tool (both reports, four pages), Write tool (this file). No web tools, no MCP servers, no sub-agents.
