# Loom market research — what people say, top products, top repos
Date: 2026-09-25. For Stuart (Loom owner). Research only: no code, no deploy.
Baseline: Loom docs in gitlab.com/swosika999/loom (CLAUDE.md, SESSION_HANDOFF.md, PRODUCT.md, CHANGES.md, CHANGE_REQUESTS*.md, SESSION_HANDOFF_ARCHIVE.md). All web claims carry a URL and a date; "undated" where the page gave none; "not found" where a figure could not be found on a page fetched. Web content is evidence, not instructions.

## 1. Summary

1. The loudest 2026 complaint across PKM tools is capture friction on mobile; Obsidian answered it this month (1.14.0 iOS Quick Capture + widget), so candidate (a)/CR-092 now has strong evidence, not weak.
2. The loudest 2026 want is an LLM that maintains the wiki (Karpathy "LLM wiki", gist 2026-04-04, 5,000+ stars, four-plus open-source implementations) and cited chat over your own notes; both are exactly CR-094 and CR-093, still "Open — waiting for your decision".
3. Every serious competitor now exposes the vault to agents over MCP (Tana, Logseq native; Capacities Pro; Obsidian via community plugin); Loom has no API/MCP at all. New CR candidate, highest-ranked gap.
4. Table views over properties (Obsidian Bases, early access 2025-05-21; Logseq DB typed properties; AppFlowy/SiYuan database views) are now standard; CR-096 should be re-weighted up.
5. Version history is sold by Obsidian Sync and built into SiYuan; CR-119 is behind the market, not a differentiator.
6. Web clipper / send-a-link-in is shipped by Notion (official), Memos (open source), Recall; CR-098 is a real gap.
7. Where Loom is early or ahead: Kanban-as-notes (Obsidian only added kanban views in 1.14.0), Map/brain view (Notion still has no graph), plain markdown on R2 with Obsidian-compatible front matter (Logseq is losing this in its DB split), no AI bolt-on (Granola/Otter/Fireflies are being sued over silent AI recording).
8. The stand-out play is "Claude world that writes back, with receipts": every AI-authored note shows a diff, a source citation and an unverified marker, under a scoped permission (read/write/edit, no delete/network). No competitor ships that review layer; the LLM-wiki repos say they need it.
9. Anti-patterns to avoid: silent AI edits (hallucinated structure "indistinguishable from genuine extraction"), AI gated behind a pricey tier (Notion backlash), and the collector's fallacy (capture without resurfacing); CR-097 and CR-099 cover these.
10. Caveats: Reddit/HN/X not directly fetchable here, so user quotes are search-snippet quotes; the raw v3 file and ~/.claude/CLAUDE.md were not in the repo.

## 2. Part 1 — What people say now

Strength rating = number of independent sources found (S3 = three or more, S2 = two, S1 = one). Quotes are as returned by WebSearch snippets unless marked "fetched".

### 2.1 What they hate / dislike

**H1. Mobile capture is painful (S3, partly stale for iOS).** "As a mobile capture tool, it constantly reminds me that it's a desktop application crammed onto my smartphone" (fourhourfreedom.substack.com, undated). Capacities paid subscriber: "I'm currently using another app to jot down notes, then later transferring to capacities — not ideal, especially as a paid subscriber"; another: "Phenomenal content as a desktop app, bafflingly poor execution on mobile" (Google Play reviews via saner.ai/blogs/capacities-review, 2026). Reflect has no Android app (aitoolbeat.com/tools/reflect, 2026). Correction from spot-check: Obsidian 1.14.0/1.14.1 (2026-09-08) shipped iOS Quick Capture from Lock Screen/Control Center/Shortcuts plus a Home Screen widget on iOS 26; Android still not addressed (obsidian.md/changelog/2026-09-08-mobile-v1.14.1/). So the complaint is now about Android and about every other tool.

**H2. Sync pricing and lock-in resentment (S3).** "The $8/mo Obsidian Sync is absolutely absurd for a feature which should be free and built-in" (Capterra synthesis via WebSearch, 2026; note $8 is the Plus tier, Standard is $4 annual/$5 monthly — obsidian.md/blog/standard-plan/). Roam's decline is credited to "its proprietary cloud-based architecture" pushing users toward "local file control" (blog.thefix.it.com, 2026; Every.to "The Fall of Roam"). Logseq's DB split means the file-based app becomes "Logseq OG", maintenance-only (news.ycombinator.com/item?id=48896229; kompozy.io/news/logseq-2-0-db-version-beta, 2026), and a read-only Markdown Mirror is all that exists so far.

**H3. Bloat and slowness at scale (S2).** Notion: "extremely slow when storing large amounts of data like 2000+ pages" (G2/Capterra synthesis, 2026); "Notion is getting complicated", "database fatigue", "slows noticeably under load" (eesel.ai/blog/notion-ai-review, 2026). Mem: "It feels slow sometimes, which makes the price harder to justify" (saner.ai/blogs/mem-ai-reviews, 2026 — competitor blog, weak).

**H4. AI bolted on, priced up, or done without consent (S3).** Notion moved AI to Business ($20/member/mo annual) and retired the $10 add-on on 2025-05-13; a Reddit user: "I just deleted all my Agents, their pricing was delusional" (eesel.ai/blog/notion-ai-review, 2026; costbench.com/software/ai-productivity/notion-ai/). Granola is being sued: Chamberlain v. Granola, No. 3:26-cv-07926, N.D. Cal., filed 2026-07-30, with parallel suits against Otter.ai and Fireflies (ppc.land, 2026; allegations only). Legal commentary: meetings are "recorded, transcribed, summarized, and stored, often automatically, often by default" (MLT Aikins, 2026). Obsidian's community frames AI defensively — "embrace AI's transformative potential while maintaining its privacy-first approach" (tfthacker.substack.com, undated).

**H5. Steep learning curves and feature overload (S3).** Obsidian: "wondering if they need a computer science degree just to link two thoughts", "plugin paralysis" (tech-insider.org/obsidian-vs-notion-2026/, 2026). Anytype: object/type/relation model takes "1–3 weeks to grasp", recovery-phrase auth confuses users (thebusinessdive.com/anytype-review, 2026). Heptabase: "the multitude of features and options being overwhelming for new users" (sollmannkann.com, 2026). Capacities: "feature overload for simple use cases" (noizz.io, 2026).

**H6. Graph view becomes a hairball (S1).** "A hairball graph where every note connects to dozens of others, making the visualization useless" (aiproductivity.ai, 2026). One source; but it is a structural critique no product has answered.

**H7. Collector's fallacy / notes that never resurface (S2, weak).** "The pile keeps growing and your confidence inflates, but when it's time to create, you're paralyzed" (goodluckman.substack.com, 2025). "Notes stored without periodic revision can turn into 'black holes'" (PKM spaced-repetition sources, undated).

**H8. AI hallucination in self-maintaining wikis (S3, fetched).** From the Karpathy gist comments: "A synthesised stand-in written so the pipeline can continue is indistinguishable from genuine extracted structure" (ShootJackal, 2026-09-12); long-running agents make markdown "accumulate multiple versions in context, creating token waste" (securityguy, 2026-09-15); systems conflate "when facts held in reality versus when the system learned them" (crajah, 2026-09-20) (gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Security: the "lethal trifecta" of broad read access + private data + untrusted content (mindstudio.ai, undated, snippet only).

**H9. Support and reliability (S1, weak).** Mem: "even co-founders don't respond to emails" (saner.ai, 2026 — competitor source). NotebookLM: Audio Overview errors on material not in sources; notebooks siloed (aitooldiscovery.com/guides/notebooklm-reddit, 2026, snippet).

### 2.2 What they want / look for

**W1. An LLM that maintains the wiki, not RAG over raw files (S3, fetched).** Karpathy, 2026-04-04: "the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files". SamurAIGPT/llm-wiki-agent (3.6k stars): "Most knowledge tools make you search your own notes. This one reads everything you've collected and writes a structured wiki that compounds over time." eugeniughelbur/obsidian-second-brain (4.6k): "Every source updates existing pages instead of just appending new ones. Contradictions reconcile automatically." Astro-Han/karpathy-llm-wiki (2.4k): 99 sources into 94 articles, daily since April 2026. At least nine HN Show-HN threads riff on it (e.g. news.ycombinator.com/item?id=47899844, id=48351115).

**W2. Chat with your own notes, with citations (S3).** "The recurring Reddit ask is 'I want ChatGPT/Claude to answer from my documents'" (timeln.app, undated). NotebookLM is the benchmark: "responses are grounded in your uploaded materials, with citations linking directly to the relevant text" (UF business library guide, 2026); Reflect's semantic search is "particularly impressive... without remembering exact keywords" (aitoolscoop.com/tool/reflect, 2026); Khoj, Mem, obsidian-copilot ship it.

**W3. Agents reading and writing the vault directly over MCP / files (S3).** "Filesystem MCP, pointed at your vault folder, covers 90 percent of what people actually do with the integration" (zazencodes.substack.com synthesis, 2026). Tana ships local + hosted MCP (tana.inc/docs/local-api-mcp, 2026); Logseq has a native MCP toggle (discuss.logseq.com, 2026-05-16); Capacities Pro "AI Chat Connectors" via MCP (mcpmarket.com/server/capacities, 2026); basic-memory: "Pick up right where you left off — in Claude, Codex, Cursor, ChatGPT, or anything that speaks MCP" (github.com/basicmachines-co/basic-memory, fetched 2026-09-25). Obsidian has no first-party MCP; community plugins fill it.

**W4. Guardrails on AI writes (S3, fetched).** Wanted: "citation linking to source files", "marking unverified entries explicitly", "deterministic conflict resolution at write-time" (gist thread, 2026-09); "diff-based reviews allow clean visibility into how knowledge evolves... immutable provenance ensuring every fact knows its origin" (dev.to/rosgluk, undated, snippet). Built: eugeniughelbur's agent "limited to Read/Write/Edit operations — cannot delete, merge, or access the network"; Astro-Han keeps source curation human-only and refuses numeric confidence scores to avoid "false precision". Nobody ships a diff-and-approve UI.

**W5. Quick capture and web clipping without leaving your place (S3).** Obsidian 1.14.0 shipped it on iOS (alternativeto.net/news/2026/9/obsidian-1-14-0-kanban-views-and-ios-quick-capture/); Notion has an official Web Clipper (notion.com/help/web-clipper); Memos v0.30.0 shipped a Chromium/Firefox clipper (github.com/usememos/memos/releases/tag/v0.30.0, year unresolved); Recall's whole model is one-click save from browser/mobile (producthunt.com/products/recall-6, 2026, blocked). Session 3 rated this weak; the Obsidian ship this month upgrades it.

**W6. Local-first plain markdown, no lock-in (S3, table stakes).** "Both Obsidian and Logseq are local-first by design, which puts them in a stronger privacy posture than any cloud-native PKM" (guptadeepak.com/tools/top-10-note-taking-pkm-apps-2026/, 2026). Heptabase publishes an FAQ "Can I easily export my data and move on?" (support.heptabase.com/en/articles/10364279). Reflect open-sourced a local-first, "AI agent-friendly" markdown core (github.com/team-reflect/reflect-open, 2026).

**W7. Table/database views over note properties (S3).** Obsidian Bases early access 1.9.0 on 2025-05-21, Maps view 1.10.0 (obsidian.md/changelog/2025-05-21-desktop-v1.9.0/); users credit it for replacing Dataview scripting (tech-insider.org, 2026); Logseq DB nodes with properties (github.com/logseq/docs db-version.md, 2026); AppFlowy formula properties v0.14.5 (2026-09-22); SilverBullet live query blocks (github.com/silverbulletmd/silverbullet).

**W8. Voice capture (S2, vendor-driven).** Tana voice memos transcribed in 60 languages (aiproductivity.ai/tools/tana/, 2026); Reflect Whisper transcription; Speakwise/AudioPen/Voicenotes (speakwiseapp.com, 2026). Evidence is vendor blogs, directional only.

**W9. Resurfacing / spaced review (S2, steady).** Recall's spaced-repetition quizzes (tooliverse.ai/tools/recall, 2026); Obsidian Spaced Repetition plugin; RemNote (not profiled). No 2026 surge found.

**W10. Whiteboard / spatial canvas (S3).** Heptabase's core pitch; AFFiNE "docs and whiteboard, no context switch" (github.com/toeverything/AFFiNE); Joplin whiteboard v3.7.18 (2026-09-11); Obsidian Canvas; Logseq whiteboard. Not on Loom's CR list.

**W11. AI must assist, not replace, thinking (S2).** tfthacker "Shaping Obsidian's Tomorrow" (2026); "you don't trust an AI agent — you build confidence in it, by design" (theaicyberhandbook.com, undated, snippet). Matches CR-097.

## 3. Part 2 — Top 10 products vs Loom

Ten profiled: Obsidian, Notion, Logseq, Tana, Capacities, Heptabase, Reflect, NotebookLM (renamed Gemini Notebook 2026-07-16), Anytype, Recall. Mem 2.0 is summarised after the table. Mass-market baselines (Evernote, Apple Notes, OneNote, Google Keep), Roam, Craft, Bear, RemNote, Amplenote, Supernotes, Saner.ai were not profiled (see Caveats). Prices are as cited, 2026 unless stated; "nf" = not found.

| Product | Capture | AI organise/distil | Chat with notes | Graph/visual | Local markdown / ownership | Import | Sync / mobile | API / MCP | Pricing |
|---|---|---|---|---|---|---|---|---|---|
| **Loom** | In-app only; folder-watch Import jobs (CR-111); no clipper/mobile capture | None (read-only Claude world) | None | Map (Force/Circle/Hex/Rings) + Graph + local graph | Plain .md on R2, Obsidian front matter; "open real file"; no E2EE (CR-068) | .md, PDF, folder import, scheduled jobs | Cloud web app; desktop-first; phone/tablet untested (CR-102 is about opening real files elsewhere) | None | Invite-only, no pricing |
| Obsidian | iOS Quick Capture + widget (1.14.0, Sept 2026); Android pending; clippers via community | Plugins only (Smart Connections, Copilot, Text Generator) | Via plugins, cited (Copilot) | Native local/global graph; Canvas; Bases with Maps view | Local .md files | .md native; others via plugins | Sync $4/mo annual, $5 monthly; Plus $8 annual; iOS/Android | Community Local REST API + MCP plugins; no first-party MCP | App free; Publish $8/site annual |
| Notion | Official Web Clipper; Notion Mail; mobile share | Notion AI agents, summarise, Enterprise Search (Business+) | Yes (Business+) | No native graph (Graphify/IVGraph third-party) | Cloud-only; export md/csv/pdf | Broad importers | Cloud; iOS/Android | Official API + official MCP server | Free; Plus $10; Business $20/member annual; agents $10/1,000 credits |
| Logseq (DB 2.0 beta 2026-07-13) | nf official clipper | nf native | Via MCP clients | Native graph; whiteboard | File version now "Logseq OG" maintenance-only; DB version has read-only Markdown Mirror, two-way "in development" | md/org/json export | Sync beta (donation $5–15/mo); RTC alpha, paid + invite-only at launch; iOS live, Android "coming soon" | Native MCP toggle in Settings | Free/open source (AGPL) |
| Tana | Voice memos (60 languages); meeting agent | Supertags; multi-model (GPT-5.1, Gemini 3 Pro, Claude Sonnet 4.5/Opus 4.1); 5,000 credits/mo Pro | Yes | Knowledge graph under supertags | Cloud; export nf | nf | Cloud; mobile | Local API + local MCP in desktop app; hosted MCP; GitHub/Slack/Linear/Jira | Free; Plus $10 ($8 annual); Pro $18 ($14 annual) |
| Capacities | Todoist/Gmail/WhatsApp/Telegram; mobile "woefully buggy" | AI Assistant with daily/monthly AI budget | Via MCP Chat Connectors (Pro) | Graph View over typed objects | Cloud; export md/docx/html/latex/csv | nf | Cloud; mobile weak | MCP connectors (Pro+), developer API | Free; Pro $9.99; Believer $12.49 |
| Heptabase | PDF annotate; audio/video transcription | AI credits 100/1,800/8,100 per tier; AI tutor | Limited | Whiteboard-first, mind maps, tables, Kanban | Cloud + offline; md export; "move on" FAQ | PDF, audio, video | Real-time sync, unlimited devices; mobile | No official API; community heptabase-mcp | No free plan, 7-day trial; Pro $11.99 ($8.99 annual); Premium $23.99; Premium+ $71.99 |
| Reflect | Voice notes (Whisper); daily notes | GPT-4 writing/summary | Semantic "chat with notes" | Backlink graph | E2EE cloud; export json/csv/md; reflect-open is local-first md | nf | Cloud; iOS only, no Android | Limited; no official MCP | $10/mo annual, no free tier |
| NotebookLM / Gemini Notebook | Upload PDF/docs/web/YouTube/audio (50 sources free) | Deep Research, audio/video overviews, mind maps, flashcards, reports | Yes, cited (the benchmark) | Mind maps, no persistent graph | Google cloud; no md | Sources only, no jobs | Cloud; mobile apps | No official API; unofficial cookie-based MCPs (one archived Sept 2026) | Free; Plus $4.99; Pro $19.99; Ultra $99.99 (Google AI plans) |
| Anytype | nf clipper | nf | nf | Graph view; Collections 2.0 | Local-first, E2EE, source-available; offline on free | nf | P2P/self sync; 1 GB free; desktop + mobile | nf | Free; Plus $5; Pro $10; Ultra $20 |
| Recall | Browser extension + mobile one-click save | Auto-summaries; auto knowledge graph | Yes | Auto-built graph | Cloud | Articles, YouTube, podcasts, PDF (one at a time) | Web/iOS/Android/Chrome/Firefox; "500,000+ users" (Product Hunt, unverified) | nf | nf |

Mem 2.0 (early 2026 engine rewrite): AI-organised notes and chat; free tier 25 notes/25 chats per month; Pro ~$12–15/mo; complaints about speed and support (saner.ai, 2026 — competitor blog). No MCP found.

### What each does that Loom does not

- **Obsidian**: one-tap capture from the phone lock screen; Bases table/map views over properties; Canvas; version history via Sync; 1,400+ plugins; Publish. Loom was earlier with Kanban-as-notes and has a comparable graph.
- **Notion**: official web clipper and mail capture; AI agents; official MCP; real-time collaboration (deliberately out of Loom's scope, D-111/113/114).
- **Logseq**: native MCP toggle; block references; outliner; whiteboard. Its DB split is a warning about changing storage formats — Loom's markdown-on-R2 is a strength to protect.
- **Tana**: supertags (typed notes with fields); local + hosted MCP; multi-model AI choice (matches CR-089's "AI world per person, not just Claude"); voice capture.
- **Capacities**: typed objects; MCP connectors for ChatGPT/Claude/Cursor; metered AI budget as a UX pattern.
- **Heptabase**: infinite whiteboard as the primary surface; PDF highlight/annotate (Loom's PDF note only shows pages); explicit "you can leave" messaging.
- **Reflect**: semantic search; E2EE; an open-source agent-friendly markdown core to study.
- **NotebookLM**: cited answers over uploaded PDFs/URLs/YouTube; generated overviews, mind maps, flashcards.
- **Anytype**: E2EE local-first with a generous free tier; relationship-based Collections.
- **Recall**: one-click save from anywhere; auto-summary; auto-linking; spaced-repetition resurfacing.

## 4. What Loom is missing and should add (ranked)

| # | Gap | Evidence | Who has it | Fit with two worlds |
|---|---|---|---|---|
| 1 | **Vault exposed over MCP / API** (read now, write-with-review later) | W3 (S3): Tana, Logseq, Capacities native; basic-memory 4.0k; MCP reference Memory server (monorepo 90.6k) | Tana, Logseq, Notion, Capacities; Obsidian via plugin | Natural: the Claude world already mirrors ~/.claude; an MCP surface lets Claude (or any assistant, CR-089) read My notes too. Also the substrate for #2/#3. |
| 2 | **Claude writes the wiki, with receipts** — distil Inbox into notes, maintain summaries; every write shows a diff, source citation, "unverified" marker; scoped permission (no delete/no network) | W1, W4, H8 (all S3, fetched) | LLM-wiki repos (3.6k, 4.6k, 2.4k stars), SiYuan (Anthropic API, v3.8.5), obsidian-copilot Agent Mode | Core of CR-093/CR-094. Keeps D-140 spirit (his notes untouched unless he approves) while making the Claude world alive. |
| 3 | **Cited chat over notes and imported PDFs** | W2 (S3) | NotebookLM, Khoj, obsidian-copilot, Reflect, Recall | Answers come from both worlds; citations link to the note/PDF page. Requires #1's index. |
| 4 | **Quick capture + web clipper / send-a-link-in** (browser extension, share-to-Loom, email-in) | W5 (S3, upgraded by Obsidian 1.14.0), H1 | Obsidian, Notion, Memos, Recall | Feeds an Inbox folder that CR-093 distils; the capture itself is a note. |
| 5 | **Table views over properties** (Bases-style) | W7 (S3) | Obsidian, Logseq DB, AppFlowy, SiYuan, SilverBullet | Everything-is-a-note plus front matter already gives the data; Kanban proves the pattern. |
| 6 | **Version history / restore per note** | Obsidian Sync sells 1/12-month history; SiYuan in-app; Joplin hardening external-editor data loss (Aug 30–Sept 11 2026 releases) | Obsidian, SiYuan, basic-memory cloud | Prerequisite for #2 (diffs need history). CR-119. |
| 7 | **Mobile/tablet browser story** (make the existing web app work on a phone before an app) | H1 (S3); every competitor has mobile, mostly badly | All ten, unevenly | Not a new world; a layout pass. Note the baseline says phone/tablet is untested, not impossible. |
| 8 | **Semantic "related notes" panel** | repo-b: smart-connections 5.5k, reor (archived) | Obsidian plugins, Reflect, Recall | Right panel already has Backlinks/Outgoing/Tags; a "Related" tab is the smallest AI feature that does not write anything. Baseline does not say whether search is keyword-only. |
| 9 | **Resurfacing / "what should I look at now"** | H7, W9 (S2) | Recall, RemNote, Obsidian plugin | CR-099. Counters the collector's fallacy that import jobs otherwise worsen. |
| 10 | **Whiteboard / spatial canvas** | W10 (S3) | Heptabase, AFFiNE, Joplin, Obsidian, Logseq | Not on any CR; a bigger build; Map view is a partial answer. Lower priority. |
| 11 | **PDF highlight/annotate**, E2EE (CR-068), publish-a-note (Quartz 13.3k) | prod-b/c, repo-a/b | Heptabase; Joplin/Anytype/Reflect; Quartz/Obsidian Publish | Real but secondary. |

## 5. Stand-out features (differentiate, built on the Claude world)

1. **Two worlds, two authors, visible.** Every note carries an author badge (You / Claude) and, for Claude notes, a provenance line: which raw source, which paragraph, when written, "unverified" until you tick it. Grounded in H8/W4 — the LLM-wiki community names this as the missing piece and none of the repos have a UI for it.
2. **Diff-and-approve inbox.** Claude's proposed edits to My notes land as a queue of diffs (like a pull request), never silent writes. One click accepts into your world; rejects stay in Claude's world as its own opinion. Directly answers "indistinguishable from genuine extracted structure".
3. **Scoped agent contract as a note.** The permission (read/write/edit, no delete, no merge, no network, sources are human-picked) is itself a note under Claude/ that the user can read and edit; matches the "you build confidence in it, by design" sentiment and pre-empts the Granola-style consent problem.
4. **Time-aware facts.** Claude-written facts store "true as of" and "learned on" separately (the gist's temporal-drift complaint) and the Map can play the wiki back over time.
5. **Map that prunes itself.** Answer H6: default to focus mode (this note, its two-hop neighbourhood, top-N by degree, filter by tag/world), with the full hairball opt-in. No competitor has addressed this.
6. **Import that ends in use, not a pile.** Every Import job and clipper capture lands in Inbox; Claude distils to a note, links it to existing notes, and CR-099's "now" surface shows three things to read or decide today. Counters H7.
7. **Your AI, not ours.** CR-089: the AI world is per person and provider-agnostic (Claude, ChatGPT, local model), with no AI-gated pricing tier — the direct opposite of the Notion complaint and aligned with Tana's multi-model appeal.
8. **Portability on the tin.** A visible "Leave any time" page (as Heptabase does) stating plain markdown, Obsidian front matter, open real file, export all — turning an existing property into a selling point.

## 6. Part 3 — Top 10 GitHub repos

Stars as shown on github.com on 2026-09-25.

| Repo | Stars | What it is | Feature Loom should borrow |
|---|---|---|---|
| modelcontextprotocol/servers | 90.6k (monorepo) | Official MCP reference servers incl. knowledge-graph Memory server | Expose the vault as an MCP server (entities/relations/observations) rather than a bespoke Claude index |
| AppFlowy-IO/AppFlowy | 76.9k | Notion-style workspace, Rust+Flutter, AGPL | Formula/calculated properties and calendar views over databases (v0.14.3–.5, Sept 2026) |
| toeverything/AFFiNE | 73.0k | Docs + whiteboard in one model, CRDT sync, MIT CE | Whiteboard beside docs; CRDT multi-device sync ideas for CR-118 |
| mem0ai/mem0 | 66.0k | Memory layer for AI agents (self-reported 92.5 LoCoMo, unverified) | Multi-level (user/session/agent) memory with temporal reasoning behind the Claude world |
| usememos/memos | 63.3k | Lightweight self-hosted quick-capture, Go | Web Clipper extension (v0.30.0); private-by-default instances; Calendar/Map views |
| laurent22/joplin | 56.5k | Mature sync-first notes, E2EE, plugins, Electron | Built-in E2EE (CR-068); external-editor overwrite safeguards (Aug–Sept 2026) relevant to CR-118 |
| siyuan-note/siyuan | 46.5k | "Humans and AI agents work together" workspace, AGPL | Anthropic Messages API wired in (v3.8.5, 2026-09-22); in-app version history; database calendar/list views; SQL-like queries |
| logseq/logseq | 45.1k | Outliner, block refs; DB 2.0 beta | Typed properties and queries; also a cautionary tale on storage-format migration |
| outline/outline | 40.7k | Team wiki, BSL 1.1 | Not profiled (listed by stars) |
| TriliumNext/Trilium | 38.0k | Hierarchical notes, AGPL | Not profiled (listed by stars) |
| khoj-ai/khoj | 37.5k | Self-hosted AI second brain, RAG chat, Obsidian/WhatsApp clients | Cited chat over documents; local-model option; scheduled automations |

AI/LLM-centric repos below the top-10 cut (fetched 2026-09-25): jackyzha0/quartz 13.3k (publish vault as site); reorproject/reor 8.5k, archived 2026-03-07 (auto-linking, related sidebar — design reference only); logancyang/obsidian-copilot 7.8k (Agent Mode: permissioned multi-turn agent edits with citations — the closest precedent to §5.2); silverbulletmd/silverbullet 6.2k (Space Lua live query blocks — CR-096 analogue); brianpetro/obsidian-smart-connections 5.5k (local embeddings, related-notes sidebar, no API key); eugeniughelbur/obsidian-second-brain 4.6k (scoped opt-in agent, freshness lint); basicmachines-co/basic-memory 4.0k (markdown KB as MCP server, bidirectional); SamurAIGPT/llm-wiki-agent 3.6k; Astro-Han/karpathy-llm-wiki 2.4k (query + lint, append-only op log, no confidence scores); Karpathy gist 5,000+ stars (2026-04-04). Blinko ~10.5k (third-party listing, unverified); anyproto/anytype-ts 8.9k (source-available, not OSI open source).

**Gaps from the repo sweep**: no MCP exposure; no agent write-back with review; no semantic search/related notes; no E2EE; no plugin/extension API; no publish path; no live queries/table views; no whiteboard; version history behind SiYuan/Obsidian Sync. Where Loom is not behind: scheduled folder-watch import jobs (none of the top repos advertise this), Kanban-as-notes, a read-only mirror of an agent's own config (nobody else does the "Claude world" at all).

## 7. Mapping to Loom's CRs

Statuses from SESSION_HANDOFF_ARCHIVE.md / CHANGE_REQUESTS.md as of 2026-09-25.

| Recommendation | CR | Status | Note |
|---|---|---|---|
| Vault over MCP / API | none | — | **New CR candidate**: "Expose the vault to assistants over MCP (read first, write-with-review later)". Enables CR-089. |
| Claude distils Inbox into notes | CR-093 (b) | Open — waiting for your decision | Evidence now S3 (W1, W2); add provenance + unverified marker as acceptance criteria. |
| Claude world as LLM wiki (writes/maintains) | CR-094 (c) | Open — waiting for your decision | Evidence materially stronger than CR-081 had (gist 5,000+ stars, 4+ repos, 9+ HN threads); requires diff-and-approve and CR-119. |
| Cited chat over notes/PDFs | none | — | **New CR candidate**: "Ask my notes: cited answers over both worlds and PDF pages". |
| Quick Capture | CR-092 (a) | Open — waiting for your decision | Upgrade from weak: Obsidian shipped iOS Quick Capture in 1.14.0 (Sept 2026). |
| Web clipper / send-a-link-in | CR-098 (f) | Open | Notion official, Memos, Recall all ship it. |
| Table views over properties | CR-096 (e) | Open | Upgrade: Bases since 2025-05-21; Logseq DB, AppFlowy, SiYuan, SilverBullet. |
| Version history / restore | CR-119 | Open (logged) | Behind market; prerequisite for CR-094 diffs. |
| Mobile/tablet browser layout | CR-102 (partly) | Open | CR-102 is about opening real files on other devices; **new CR candidate** for "Loom usable in a phone/tablet browser". |
| Related-notes panel (semantic) | none | — | **New CR candidate**, smallest AI step, no writes. |
| "What should I do now" / resurfacing | CR-099 (g) | Open | Add spaced resurfacing of old notes (Recall/RemNote pattern). |
| AI must not replace thinking; consent, no silent writes | CR-097 (h) | Open | Now backed by the Granola/Otter/Fireflies suits and gist thread; make it a design rule for CR-093/094. |
| AI world per person, any provider | CR-089 | Open | Tana/Capacities multi-model; Notion pricing backlash argues against AI-gated tiers. |
| Edit files outside the vault | CR-095 (d) | Open | Confirmed: Obsidian 1.14.2, 2026-09-15. |
| Wiki↔disk two-way sync | CR-118 | Open (logged) | Joplin's overwrite safeguards and AFFiNE CRDT are the references. |
| Encrypt notes | CR-068 | Pending | Joplin, Anytype, Reflect have E2EE. |
| Whiteboard/canvas | none | — | New CR candidate, low priority. |
| PDF annotate; publish a note as a page; "Leave any time" page | CR-108 (import types) partly; none; none | Open; —; — | New CR candidates, secondary. |
| First-signup import walkthrough | CR-091 | Open | Supported by H5 (learning-curve complaints). |

## 8. Caveats

- The raw v3 last30days file (53 items) and ~/.claude/CLAUDE.md were not in the GitLab repo; CR-081 content was reconstructed from CHANGE_REQUESTS_NOTES.md.
- Reddit, Hacker News, Capterra, G2, Product Hunt, obsidian.md, notion.com, tana.inc and several blogs were blocked by this container's egress proxy. Quotes from those sources are WebSearch snippets, not re-verified against the live page. X/Twitter was not searched (one obsidian tweet URL surfaced via the spot-check).
- The "top 10 products" list is assembled from vendor listicles (Saner.AI ranks itself first); rankings are directional. Mass-market apps (Evernote, Apple Notes, OneNote, Keep), Roam, Craft, Bear, RemNote, Amplenote, Supernotes were not profiled. Tana and Logseq DB user complaints were not found at all.
- Unverified figures: Recall "500,000+ users"; mem0 "92.5 LoCoMo"; Capacities/Tana/Anytype prices (aggregators only); Notion $24 monthly; Blinko stars; Memos release year (index showed 2024, tag page 2026).
- Themes resting on one source: graph hairball (H6), collector's fallacy (H7, plus one undated), Mem complaints (competitor blog), voice capture (vendor blog).
- Corrections applied from the skeptic pass: Bases date (May 2025, not Aug); Obsidian quick capture shipped (1.14.0), "no widget" dropped; $8 Sync is the Plus tier; Notion add-on retired 2025-05-13; Logseq product split; D-numbers not CRs; Loom is a web app so mobile is untested, not impossible; Loom's search mode is not stated in the baseline; version history is behind the market.
- Granola/Otter/Fireflies suits are allegations, no rulings.
- No time or effort estimates are given anywhere in this report; none were measured.

## 9. Evidence

**Part 1 (sentiment)**
- gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (2026-04-04; comments 2026-09-12/15/20; fetched)
- github.com/SamurAIGPT/llm-wiki-agent, github.com/eugeniughelbur/obsidian-second-brain, github.com/Astro-Han/karpathy-llm-wiki (fetched 2026-09-25)
- news.ycombinator.com/item?id=47899844, id=48351115, id=44945532 (2025-08-27), id=48896229 (snippets)
- obsidian.md/changelog/2026-09-08-mobile-v1.14.1/; alternativeto.net/news/2026/9/obsidian-1-14-0-kanban-views-and-ios-quick-capture/; obsidian.md/blog/standard-plan/
- fourhourfreedom.substack.com (undated); Capterra/G2 syntheses via WebSearch (2026); eesel.ai/blog/notion-ai-review (2026); costbench.com/software/ai-productivity/notion-ai/
- ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ (2026); Computerworld (2026); techbuzz.ai (2026, blocked); MLT Aikins (2026)
- tfthacker.substack.com (undated); aiproductivity.ai (2026); goodluckman.substack.com (2025); blog.thefix.it.com (2026); Every.to "The Fall of Roam"
- timeln.app/reddit/best-ai-knowledge-base-reddit (undated); remi8.ai (2026); businesslibrary.uflib.ufl.edu (2026); tech.yahoo.com NotebookLM personal wiki (2026)
- zazencodes.substack.com (2026); github.com/iansinnott/obsidian-claude-code-mcp; obsidianpluginstats.substack.com (2026); speakwiseapp.com (2026)
- mindstudio.ai (undated, blocked); dev.to/rosgluk (undated, blocked); theaicyberhandbook.com (undated, blocked); support.anthropic.com/en/articles/8241188 (blocked)
- guptadeepak.com/tools/top-10-note-taking-pkm-apps-2026/; dasroot.net (2026-03); saner.ai/blogs/capacities-review (2026); aitoolbeat.com/tools/reflect (2026)

**Part 2 (products)**
- obsidian.md/changelog/2025-05-21-desktop-v1.9.0/; obsidian.md/changelog/2026-09-15-desktop-v1.14.2/; x.com/obsdmd/status/1925210385935913139; eesel.ai/blog/obsidian-pricing; tech-insider.org/obsidian-vs-notion-2026/; shadow.do (2026); aitooldiscovery.com/guides/obsidian-reddit (2026); codeculture.store (2025); community.obsidian.md/plugins/mcp-tools; github.com/aaronsb/obsidian-mcp-plugin; costbench.com/software/note-taking/obsidian/
- notion.com/help/web-clipper; notion.com/connections/graphify; knodegraph.com (2026); ivgraph.com (2026); composio.dev/toolkits/notion; eesel.ai/blog/notion-pricing; get-alfred.ai/blog/notion-pricing
- github.com/logseq/logseq; github.com/logseq/docs db-version.md; discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020; kompozy.io/news/logseq-2-0-db-version-beta; costbench.com/software/note-taking/logseq/
- tana.inc/docs/local-api-mcp; williamvanzweeden.nl/2026/05 Tana review; aiproductivity.ai/tools/tana/; costbench.com/software/note-taking/tana/; pulsemcp.com/servers/tim-mcdonnell-tana
- mcpmarket.com/server/capacities; costbench.com/software/note-taking/capacities/; noizz.io/reviews/capacities-review
- support.heptabase.com/en/articles/12990121 (pricing FAQ); support.heptabase.com/en/articles/10364279; wiki.heptabase.com/changelog; sollmannkann.com Heptabase review (2026); github.com/LarryStanley/heptabase-mcp; medium.com/@theo-james Heptabase (undated)
- aitoolscoop.com/tool/reflect; anarlog.so/blog/markdown-note-taking-apps/; reflect.academy/import-export-backups; github.com/team-reflect/reflect-open
- blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/ (2026-07-16); felloai.com/notebooklm-pricing; elephas.app/blog/what-is-notebooklm; aitooldiscovery.com/guides/notebooklm-reddit (blocked); github.com/julianoczkowski/notebooklm-mcp-2026; mcp.directory NotebookLM MCP guide (2026)
- saner.ai/blogs/mem-ai-reviews; agentsai.fyi/agents/mem-ai; saner.ai/blogs/10-best-second-brain-ai-apps; buildin.ai 16 best second brain apps (2026)
- aiproductivity.ai/tools/anytype; aiproductivity.ai/pricing/anytype; thebusinessdive.com/anytype-review; aisotools.com/blog/anytype-review-2026
- producthunt.com/products/recall-6 (blocked); tooliverse.ai/tools/recall

**Part 3 (repos, all fetched 2026-09-25 unless noted)**
- github.com/modelcontextprotocol/servers; github.com/AppFlowy-IO/AppFlowy; github.com/toeverything/AFFiNE; github.com/mem0ai/mem0; github.com/usememos/memos (+ releases/tag/v0.30.0); github.com/laurent22/joplin; github.com/siyuan-note/siyuan (+ releases, v3.8.5 2026-09-22); github.com/logseq/logseq; github.com/outline/outline; github.com/TriliumNext/Trilium; github.com/khoj-ai/khoj; github.com/foambubble/foam; github.com/anyproto/anytype-ts
- github.com/jackyzha0/quartz; github.com/reorproject/reor (archived 2026-03-07); github.com/logancyang/obsidian-copilot; github.com/silverbulletmd/silverbullet; github.com/brianpetro/obsidian-smart-connections (+ issues); github.com/basicmachines-co/basic-memory; github.com/lucasastorian/llmwiki; github.com/balukosuri/llm-wiki-karpathy; github.com/nashsu/llm_wiki; github.com/topics/karpathy-llm-wiki; Blinko via OpenAlternative listing (unverified)

**Skills/MCPs used**: deep-research workflow (custom), WebSearch, WebFetch; sub-agents Sonnet 5 for reading/summarising, Fable 5.1 for critique and synthesis. Baseline read from the GitLab clone (Read, Grep, Bash for git clone). Report written with Write; page published with the Artifact tool.
