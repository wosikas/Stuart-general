# Loom market research v2: feature gaps and product direction

Date: 2026-09-28. Evidence window: 2026-06-30 to 2026-09-28. Anything older is marked **[dated]**. Sizes are S, M or L only; no time or effort figures appear anywhere in this report, by house rule. Quotes are verbatim from the source named. Where a figure was not on a page fetched or in a file read, it says "not found". Vendor and competitor pages never stand alone as support for a theme. Fact-check corrections from the two adversarial passes have been applied throughout; claims they marked unverifiable are labelled as such.

---

## 1. Summary

1. The loudest, best-supported wants across every platform are the same four: an agent or MCP door into the notes, search that finds meaning not substrings, capture that needs no filing decision, and proof the data is safe and can leave (history, export).
2. The loudest attitude is "AI must not think for me"; the accepted pattern is "it suggests, I click". This validates CR-097 and tells you how any AI CR must be shaped.
3. Loom's two-worlds split is, by accident of design, exactly the raw-versus-wiki boundary the LLM-wiki crowd is building by hand. That is the differentiator; nobody hosts it for you without an install.
4. Loom's biggest gaps, in order: no MCP or API (L), substring-only search (M for full-text, L for semantic), no quick capture (M), no version history or whole-vault export (M + S), no distil-into-Claude-world flow (L, blocked by D-131).
5. Every one of the ten closest products now ships an MCP, CLI or API; five of six in group B ship chat-over-your-notes with citations. Loom ships neither.
6. CR-081's old labels are stale: Quick Capture (CR-092) and table views (CR-096) now have real user threads, not only vendor pages. CR-095 (edit files outside the vault) still rests on a single vendor release thread.
7. Weak or single-source wants, which should not drive a CR yet: web clipper, resurfacing, voice capture, backlinks-with-context, status-on-a-link, notes-beside-PDF, encryption.
8. Recommended next CRs to pick: a per-person read-first MCP (new), full-text search index in D1 (new), CR-092, CR-119 plus whole-vault export, then CR-093/094 as a proposals flow once D-131 is decided.
9. Reddit coverage: PASS on all six subreddits; scores are archive snapshots; r/logseq (21 posts) and r/ClaudeAI (3 days) are thin.
10. Blocked: reddit.com live, most of github.com HTML, tana.inc pricing HTML, Medium, Evernote forum; those claims are marked unverifiable rather than dropped.

---

## 2. Evidence base

| Source | Items | Window covered | Notes |
|---|---|---|---|
| r/ObsidianMD (Arctic Shift archive) | 500 posts | posts dated 2026-09-12 to 2026-09-28 | 500-post cap cut off earlier weeks; header claims 08-29 |
| r/logseq | 21 posts | 2026-08-29 to 2026-09-28 | low volume, weak on its own |
| r/Notion | 484 posts, 3,087 comments listed | 2026-08-29 to 2026-09-28 | about top 12 comments kept per post |
| r/NoteTaking | 258 posts, 1,090 comments listed | same | 32 posts are self-promotion by regex |
| r/PKMS | 78 posts | 2026-08-31 to 2026-09-28 | about 12 app promotions, 3 removed |
| r/ClaudeAI | 500 posts (22 relevant, 398 off-topic, 80 removed) | actually 2026-09-26 to 2026-09-28 | 3-day sample only |
| Mac runs (last30days) | X 101, YouTube 61, TikTok 57, Instagram 13, Reddit 98 (cross-check only) | 2026-08-29 to 2026-09-28 | heavy off-topic noise; unique URLs found 103/64/58/13 |
| v3 pull (research/2026-09-22-pkm-market-pull-raw-v3.md) | 53 items: Reddit 26, HN 16, YouTube 6, TikTok 3, Instagram 2, X 0 | 2026-08-23 to 2026-09-22 | mostly title-only; all 6 YouTube items dated; tool's own "thin evidence" warning |
| Web sweep, hates | 9 pages fetched, 15 HN threads via Algolia | 2026-01-01 on, in-window flagged | reddit, Evernote forum, tumblr blocked |
| Web sweep, wants | 11 of 13 pages fetched | mixed; much dated | Karpathy gist comments are the in-window core |
| Web sweep, LLM-wiki trend | 14 of 16 pages fetched | mixed | GitHub API not open; years from page summaries unreliable |
| Products A and B | official changelogs, pricing pages, HN Algolia | fetched 2026-09-28 | tana.inc/releases 404; Mem changelog 404; Reflect changelog empty |
| Repos | 19 candidates via GitHub MCP search, READMEs via raw.githubusercontent.com, release atom feeds | fetched 2026-09-28 | api.github.com refused; issue reaction counts not shown |
| Fact-checks | about 230 quotes grepped; 64 + 51 + 43 claims refetched | 2026-09-28 | 3 attribution errors, 2 count problems, several loose paraphrases corrected |

**Reddit coverage verdict: PASS**, all six subreddits read in full. Scores and comment counts are approximate archive snapshots (the same thread shows 939, 1,113 and 1,131 across three snapshots). r/logseq is low-volume and r/ClaudeAI covers three days; any theme resting mainly on those two is single-source.

**Could not be reached:** reddit.com live pages (all Reddit evidence is from the archives); api.github.com and github.com HTML for Memos issue #6231, SiYuan and Trilium release pages from the sentiment checker's session (the product checker did reach them); tana.inc/pricing HTML (JS-rendered, so prices are confirmed by one checker and unverifiable by the other); discussion.evernote.com (403); Medium (403); cassolotl.tumblr.com (429); HN item 48184312 (403); tana.inc/releases (404); Mem changelog (404).

---

## 3. Part 1: what people say now

Strength: **S3** = three or more independent (non-vendor) sources across platforms; **S2** = two; **S1** = one, or vendor-heavy. Counts are the readers' own tallies of distinct threads, not figures from any page.

### Hates

**H1. Sync is fiddly, conflicts, data loss. S3.** r/ObsidianMD about 23 distinct threads plus about 11 reposts; r/Notion about 17 data-loss threads; HN in window. Platforms: Reddit, HN.
- Comment (10), 2026-09-20: "I use syncthing with multiple devices but I still get more sync conflicts than I would like, to the point I have to go through and clean them up weekly." https://www.reddit.com/r/ObsidianMD/comments/1wlw7cr/
- Post, 2026-09-14: "Turns out I was wrong and all my work of the last few months is gone." https://www.reddit.com/r/ObsidianMD/comments/1wfqyj2/
- Post, 2026-09-21: "I spent hours writing a second verse and hook and went back and it was gone." https://www.reddit.com/r/Notion/comments/1wmih10/
- Post, 2026-08-29: "if I had found out 5 days later, all of these pages would have been deleted permanently." https://www.reddit.com/r/Notion/comments/1w1xg5s/

**H2. Price hikes on locked-in data; paying just to sync. S3.** HN (Evernote, Bear, Obsidian Sync), r/Notion about 20 threads on AI credits and plan changes, X/TikTok (Goodnotes, Granola, Zoho). Platforms: HN, Reddit, X, TikTok.
- fuckinpuppers, 2026-09-13: "They just sent out pricing updates and it's nearly doubling the price I was paying before… It's just accelerated my exit plan." https://news.ycombinator.com/item?id=49680177
- Post, 2026-09-22: "Now, I'm suddenly facing a price of $240—a 150% increase." https://www.reddit.com/r/Notion/comments/1wnd3w5/ (Reddit-only; unverifiable on any official page)
- librasteve, 2026-09-28: "I do not want to pay $$ per month just to sync notes between iPhone and Mac." https://news.ycombinator.com/item?id=49874274
- Sid_899, 2026-09-27: "no official way to export everything out at once. This is software enshittification at it's finest." https://x.com/Sid_899/status/2104157903330361493

**H3. AI pushed into a simple notes app; can't switch it off. S3.** r/Notion and r/NoteTaking about 14 threads; r/PKMS 1w41j89 (14/29); HN largbae. Platforms: Reddit, HN.
- Comment (198), 2026-09-22: "Switched to Obsidian bc im sick of the AI and bloated UI" https://www.reddit.com/r/Notion/comments/1wngksq/
- Post, 2026-09-01: "the AI integration *absolutely* ruined it in my opinion. there is an option to turn it off but it wouldn't 100% go away." https://www.reddit.com/r/PKMS/comments/1w41j89/
- largbae, 2026-09-12: "No teams, no chat, definitely no AI. Just my notes on every device, searchable and silently synced." https://news.ycombinator.com/item?id=49673926
- Counter-voice (146), 2026-09-20: "Then just use it for note taking? I never even notice that there's an AI feature in Notion" https://www.reddit.com/r/Notion/comments/1wlbmw8/
- Reading: the complaint is less "AI exists" than "AI is in the way and I can't remove it". That nuance rests on 3 comments in 2 threads.

**H4. The tool becomes the job: tinkering, overwhelm, the "graveyard". S3.** r/ObsidianMD about 12 threads; r/Notion about 18; r/PKMS 8; HN essays. Platforms: Reddit, HN, blogs.
- Post, 2026-09-20: "All of tinkering, trying new css snippets, new plugins, in hope for the perfect vault setup, but in the end i rarely taking any notes..." https://www.reddit.com/r/ObsidianMD/comments/1wlkkh8/
- Post, 2026-09-17: "I had built a beautiful system for storing information and a terrible system for surfacing it." https://www.reddit.com/r/Notion/comments/1wiwki4/
- Comment (122), 2026-09-22: "You don't actually like using Notion. You just like building in it." https://www.reddit.com/r/Notion/comments/1wngksq/
- Korin, 2026-09-21: "You're spending hours tweaking plugins, tags, and folder trees to avoid a five-minute task you don't want to do." https://korin.uk/your-second-brain-wont-do-the-work

**H5. Search fails when you remember the idea but not the words. S3.** r/ObsidianMD 7 threads (one builder post among them), r/PKMS, XDA [dated]. Platforms: Reddit, web.
- Post, 2026-09-24: "My biggest gripe is that a search term of `art` will bring back results containing "chart" and "smart."" https://www.reddit.com/r/ObsidianMD/comments/1wonlxo/
- Comment (2), 2026-09-16: "Find that weird article about cats I saved a few months ago." when the article mentions *jaguars* or *leopards* but doesn't specifically include the word *cat*." https://www.reddit.com/r/PKMS/comments/1whuws4/
- Post, 2026-09-15: "I'm especially curious whether anyone has a workflow that surfaces relevant notes before or during a decision, rather than relying on you to remember that those notes exist." https://www.reddit.com/r/ObsidianMD/comments/1wgp2aa/

**H6. My AI forgets me between sessions; vendor memory goes stale or can't be forgotten. S2.** r/PKMS 6 threads, r/ClaudeAI 7 (3-day sample), TikTok/YouTube about 14 (mostly creators). Platforms: Reddit, TikTok, YouTube, X.
- Post, 2026-09-27: "it was 'remembering' things that I had specifically asked it to remove from memory, because situations had changed." https://www.reddit.com/r/ClaudeAI/comments/1wrecia/
- Comment (3), 2026-09-01: "the vendor memory features are the wrong layer for this in my experience. they are per provider, opaque, and recency weighted" https://www.reddit.com/r/PKMS/comments/1w4rav6/
- Comment, 2026-09-09: "a context window is working memory, not storage." https://www.reddit.com/r/PKMS/comments/1wbrqp7/

**H7. Stalled or perpetual-beta apps; format lock-in by a database rewrite. S2.** HN Logseq thread 2026-07-13; r/logseq about 7 of 21 posts. Platforms: HN, Reddit (low-volume).
- Valodim, 2026-07-13: "the supposed improvement is a database format… so I can no longer keep all my data as markdown files?" https://news.ycombinator.com/item?id=48896645
- Comment (8), 2026-09-02: "Funny that a huge selling feature for Logseq used to be the markdown files… Now the markdown version is disappearing" https://www.reddit.com/r/logseq/comments/1w5dwuo/

**H8. Mobile is slow, offline is missing, locked-down work machines can't install anything. S3.** r/Notion about 10; r/ObsidianMD 4 independent "no install allowed" threads; r/PKMS 8; HN. Platforms: Reddit, HN.
- Post title, 2026-09-20: "How to use Obsidian at work, when installing files is forbidden?" https://www.reddit.com/r/ObsidianMD/comments/1wlea3k/
- Comment (15), 2026-08-31: "Please for the love of God an ACTUAL offline mode." https://www.reddit.com/r/Notion/comments/1w3dwat/
- jamesboehmer, 2026-09-27: "every corporate laptop I've had for the last 10 years prohibits app store and icloud storage." https://news.ycombinator.com/item?id=49869398
- Post, 2026-09-23: "Only Google Drive is authorized, but it seems it's not possible to open a Vault from Google Drive on the iOS app." https://www.reddit.com/r/ObsidianMD/comments/1wo6hf0/

### Wants

**W1. An agent or MCP door into my notes; the notes app as the AI's memory. S3.** r/Notion about 20 threads; r/ObsidianMD about 20 (low score); r/PKMS 13; X/YouTube 7 on shared memory; gist comments. Platforms: Reddit, X, YouTube, GitHub gist, HN.
- Post, 2026-09-24: "I don't trust community claude plugins for security purposes, but I'd be open to some sort of obsidian MCP that my Claude Desktop could connect to" https://www.reddit.com/r/ObsidianMD/comments/1wp9ghh/
- Post, 2026-09-24: "Is there a free way to be able to allow claude to access my vault and make changes… from my phone without my computer being always on?" https://www.reddit.com/r/ObsidianMD/comments/1wp9kjz/ (score 0)
- Comment (10), 2026-09-23: "Use MCP with my free subscription and use it solely as my knowledge source." https://www.reddit.com/r/Notion/comments/1wo5671/
- @ShootJackal, gist, 2026-09-12: "Put the memory outside them, then connect each model to the same memory service. One canonical, Git-backed Markdown corpus." https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Trust shock, top r/Notion post (223/26), 2026-09-07: "Notion's official MCP connector prompt injects AI agents to advertise Notion Business to you mid-task" https://www.reddit.com/r/Notion/comments/1w9depq/

**W2. An LLM wiki: raw sources frozen, an agent keeps the wiki, a human promotes. S3 for the pattern; independent user voices are fewer than the post count suggests.** Mac runs about 33 posts (X 15, YouTube 9, TikTok 7, Instagram 3; about 6 independent X users, rest creator or course funnels); gist comments in window; r/PKMS 12 threads. Platforms: X, TikTok, YouTube, Instagram, GitHub gist, Reddit, HN [dated].
- NixFred, 2026-09-26: "An Obsidian vault that his AI builds and maintains. He never opens Obsidian. Codex and Claude write to it, recall from it" https://x.com/NixFred/status/2103926191656779984
- Instagram reel, 2026-09-19: "Raw is where you dump every note and idea with zero structure. Wiki is where Claude turns that mess into clean, structured knowledge" https://www.instagram.com/reel/DdeHzRAM5de/ (creator content)
- obsidianstudio9, 2026-09-25: "raw/＝受信箱・記事・素材。凍結して読み取り専用" (raw/ = inbox, articles, material; frozen and read-only) https://x.com/obsidianstudio9/status/2103623080228860329
- Top r/PKMS post (83/27), 2026-09-20: "First, re-importing the original data should never overwrite notes I wrote manually." https://www.reddit.com/r/PKMS/comments/1wlcbes/
- Karpathy gist [dated 2026-04-04]: "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."

**W3. Capture now, organise later; no filing decision; from the phone. S3.** r/NoteTaking and r/Notion about 12 threads; r/ObsidianMD about 4 independent plus vendor; r/PKMS 11 on capture friction; HN Workflowy; Obsidian shipped it in September (vendor). Platforms: Reddit, HN, X, YouTube, TikTok.
- Post (19/38), 2026-09-25: "every time I create a new page I get anxious thinking about where it belongs before I even write." https://www.reddit.com/r/NoteTaking/comments/1wpk5q7/
- Post (5/15), 2026-09-16: "I just need a plug in for my computer and phone so I can just quick capture an idea or something without creating an entirely new note for like 300 characters?" https://www.reddit.com/r/ObsidianMD/comments/1whmk2j/
- Comment (2), 2026-09-21: "Having to choose a folder or structure first is where a lot of note apps start feeling like work." https://www.reddit.com/r/NoteTaking/comments/1wm0chb/
- AbstractH24, 2026-07-13, on Workflowy: "the inability to email notes to it or otherwise push data to it from other sources was such a deal breaker." https://news.ycombinator.com/item?id=48898993
- Reddit cross-check from Mac runs: Obsidian 1.14.0 iOS quick capture thread scored 406/66 and 1.14.1 widget 224/50 (snapshot).

**W4. AI as librarian: find, suggest links and tags, never write. S3.** r/PKMS 8 threads; r/ObsidianMD Homing (builder post) and 1wpqy7v; r/Notion 9 threads; Notion "suggested edits" (vendor). Platforms: Reddit, YouTube, X.
- Post (11/16), 2026-09-03: "I don't want AI to develop my insights. I want to do that. But I do want it to organize, relate, and search/recover my notes. I want a research assistant." https://www.reddit.com/r/PKMS/comments/1w6hnx9/
- Comment (2), same thread: "I want a librarian, not a co-author. "You wrote something similar to this in March, want to link them?" is genuinely useful; generated "insights" I never thought are just noise wearing my name."
- Comment (2), same thread: "Ingestion and retrieval yes, linking no. ... enough false positives that i stopped trusting the graph and turned it off."
- Post (41/19), 2026-09-11: "it's search that understands your notes, not a chatgpt clone." https://www.reddit.com/r/Notion/comments/1wdoe35/
- Post, 2026-09-25: "If you delegate it, you own a very tidy archive of conclusions you never reached." https://www.reddit.com/r/ObsidianMD/comments/1wpqy7v/

**W5. Safe agent writes: append-only, diff, approve, provenance, trash not delete. S2 in window (gist comments, X), plus HN [dated] and repo READMEs.** Platforms: GitHub gist, X, YouTube, dev.to.
- obsidianstudio9, 2026-09-26: "上書きされたノートは ゼロ。vaultは増えるだけ。 ・追記のみ" (zero notes overwritten, the vault only grows; append only) https://x.com/obsidianstudio9/status/2103985468270678332
- @crajah, gist, 2026-09-20: "A wiki that compounds is a wiki whose early errors compound too." and "Citations are links."
- @sidleo, gist, 2026-09-15: "anything written without it is marked unverified."
- dev.to, 2026-09-24: "the LLM doing the summarizing can itself return untrustworthy output" https://dev.to/bokuwalily/i-dont-trust-the-llm-that-writes-my-shared-memory-3-regex-gates-before-claude-code-auto-commits-3i77
- YouTube (82,729 views), 2026-08-29: "The biggest danger of giving AI a memory isn't that it forgets. It's that it remembers something that was never true" https://www.youtube.com/watch?v=_bieksxg6oY

**W6. Save AI chats as notes; one memory across ChatGPT, Claude, Codex. S2.** r/ObsidianMD 5 distinct threads, 2 independent (both score 0); r/Notion 1w81gm5 and multi-AI relay posts (scores 0–8); X 6 posts. Platforms: Reddit, X.
- Post, 2026-09-25: "every so often it says something worth keeping - but the only way I've found is switching windows and pasting it somewhere by hand" https://www.reddit.com/r/ObsidianMD/comments/1wpr9zp/
- Post, 2026-09-05: "I have conversations scattered across ChatGPT, Claude, Gemini, Perplexity, Grok, Genspark, etc., so I've been importing all of them into one Notion database." https://www.reddit.com/r/Notion/comments/1w81gm5/
- omx0r, 2026-09-27: "one shared Source of Truth for ChatGPT, Claude, and my entire Hermes Agent fleet… I can manage it directly from my phone" https://x.com/omx0r/status/2104021309235646773 (1 like)

**W7. "What should I do now?", dashboards, recent activity. S2.** r/ObsidianMD about 7 threads (TaskFlow 90/26 is a builder post); r/Notion 18 "surfacing" threads; r/PKMS titles only. Platforms: Reddit.
- Post, 2026-09-22: "**I had plenty of tasks. I just didn't know which one to work on next.**" https://www.reddit.com/r/ObsidianMD/comments/1wnehzb/ (builder)
- Post, 2026-09-15: "What I needed was not five source summaries. I needed a current view of what I believed after reading all five." https://www.reddit.com/r/Notion/comments/1wgptwb/
- Post, 2026-09-23: "Is a home Dashboard on the works for Obsidian?" https://www.reddit.com/r/ObsidianMD/comments/1wo4a4k/

**W8. Table and database views; rollups. S2.** r/ObsidianMD about 12 threads (1woxyrg 21/47; Rowbase 199/32); r/Notion comment (39). Platforms: Reddit. The v3 pull had 0 posts, so CR-081's "blogs only" label is out of date.
- Comment (39), 2026-09-24: "For my use case, Obsidian simply cannot replace Notion's databases." https://www.reddit.com/r/Notion/comments/1woxf2g/
- Post, 2026-09-13: "once you have thousands of rows, thousands of little files isn't practical — and changing the schema means touching them all" https://www.reddit.com/r/ObsidianMD/comments/1wfcflo/

**W9. PDFs and files with notes around them; OCR; highlights as notes. S2.** r/ObsidianMD about 10 (Third Mind Reader 538/45 is a plugin announcement); r/PKMS 8; r/ClaudeAI OCR comment (27). Platforms: Reddit, X.
- Post, 2026-09-18: "Ideally I'd like to annotate PDFs, link specific sections/pages to notes, and keep everything local and under my control" https://www.reddit.com/r/ObsidianMD/comments/1wjz07a/
- Post (9/13), 2026-09-04: "Cloud storage is great for files but I cannot write notes around the file so..." https://www.reddit.com/r/PKMS/comments/1w6qsx5/
- Comment (27), 2026-09-27: "An OCR Tool using tesseract that OCR'd and embedded the text in hundreds of existing old PDFs with no text embedded." https://www.reddit.com/r/ClaudeAI/comments/1wrckhp/

**W10. Browser access with no install. S2 (4 independent threads).** https://www.reddit.com/r/ObsidianMD/comments/1wlea3k/ (0/40), 1wr0wff, 1wo6hf0, r/logseq https://www.reddit.com/r/logseq/comments/1wcrinu/ ("Browser mode would allow those who can't install apps use it"). HN flkiwi, 2026-07-13: "I can fire up my notes from literally anywhere, any device and see a consistent state without having to sync anything." https://news.ycombinator.com/item?id=48898361

**W11. Scoped views, hide a folder from search or AI, separate domains. S2.** r/Notion 6 threads; r/PKMS 6; r/ObsidianMD Spaces (153/22) and multi-vault (130/52). Platforms: Reddit.
- Comment (3), 2026-08-31: "Let us set some pages to NOT be searchable / indexable by AI." https://www.reddit.com/r/Notion/comments/1w3dwat/
- Post, 2026-09-16: "The suggestion to simply have multiple vaults always felt way too clunky and required too many clicks to switch contexts easily." https://www.reddit.com/r/ObsidianMD/comments/1wi1izj/

**Weak wants (S1), recorded but not CR-driving:** web clipper that survives link rot (1we53hr, 8/9; "~40% are 404" per post, the "600+" count is unverified); resurfacing or "on this day" (one independent comment, 1wigzar; rest creator funnels); voice capture (one forum comment in window, rest vendor); backlinks with context (one r/logseq post 1wakh14); status shown on a link (one Notion post 1wkhape, 36/16); notes beside each PDF page (1wno7wj); encryption (about two independent HN voices, Barrin92 and smokel, rest builder posts); NotebookLM-style Q&A (XDA, dated).

### Loves

**L1. Plain files you own; the software is ephemeral, the data is not. S3.** Every subreddit, HN, X.
- Post, 2026-09-16: "the software is ephemeral, the data is not." https://www.reddit.com/r/ObsidianMD/comments/1wi1izj/
- Comment (23), 2026-09-06: "Obsidian because you own your data. You can just move your text files into another markdown app and switch the app in worst case." https://www.reddit.com/r/PKMS/comments/1w94mqf/
- Post, 2026-09-10: "A folder of Markdown is the one format every AI tool already understands." https://www.reddit.com/r/logseq/comments/1wcrinu/
- Comment (34), 2026-09-18: "over the decades I've learned that vendor lock-in is the greatest danger to longevity." https://www.reddit.com/r/NoteTaking/comments/1wjutfm/

**L2. Simplicity and no built-in AI. S2.** Comment (11), 2026-09-01: "I use Obsidian and it does not have native AI features" (1w41j89). Comment (3): "Obsidian is dead simple and reliable if you don't mess with it too much." (1wmih10). The phone's built-in Notes app praised for being minimal (r/NoteTaking 1wfspzy, 15/15).

**L3. Graph and visual linking. Contested.** Loved on TikTok ("we love graphview", 1,745 views, 2026-09-19) and asked for by Notion users (comment (11), 1w3dwat: "A network diagram to show how pages are linked"); mocked ("folders with impressive graphs", YouTube, 258 views); every "hairball" criticism found is outside the window. Do not treat the graph as a proven draw.

### Switching patterns

- **To Obsidian from** Notion (about 6 r/ObsidianMD threads plus the r/Notion exodus: comment (155) "Migrating to obsidian. It was a nice ride."), Evernote (about 5, over pricing), OneNote (about 4), Bear (2), Standard Notes, Logseq.
- **Away from Notion to** Obsidian (most named), Google Docs (79/111 thread), Apple Notes, Capacities, Anytype, Craft, Fibery, AFFiNE, Logseq; or to Claude/ChatGPT over MCP instead of Notion AI.
- **Away from Obsidian to** Notion (1w9a9ko "Tried to Switch to Obsidian, Experienced Hell", 24/120), Apple Notes, Logseq DB, RemNote; reasons given are plugins, sync, setup.
- **Away from Logseq to** Tine (1wgd8vb, 45/39), SiYuan; some return.
- **Away from Evernote/OneNote to** Joplin, Notesnook, UpNote, Reflect, Harbor.
- **Agents:** ChatGPT to Claude Code ("it was a big pain to try to get at least some information out of ChatGPT", 1wbrqp7); Claude and Codex used side by side on one vault (X, several posts).

### AI attitudes, in one paragraph

Hostility to AI that writes or thinks for the user is the single most consistent signal across all five readers and all sweeps: the 149-score comment "generated notes are not notes" (1wf8oai, 355/44), r/ObsidianMD's "Rule 4: No slop", "Proudly human and still doing my own thinking!" (r/PKMS), TikTok "you didn't build a system, you built a diary". At the same time, the same people want AI as a librarian (W4), as a memory store reached over MCP (W1), and as a wiki-keeper whose output they review (W2, W5). The accepted contract is: it suggests, I click; drafts wait for promotion; raw sources are never rewritten; an off switch that really removes it. That is CR-097 stated by the market.

---

## 4. Part 2: top 10 products vs Loom

The ten are the products closest to Loom's shape (markdown or note-centred personal knowledge base with AI and linking), taken from the overlap of the Recall and Tana vendor lists filtered by that shape. Notion is a near miss (databases and teams, out of scope under D-111/113/114) and is used only as a reference in the text. Data fetched 2026-09-28 unless marked.

### Comparison table

| Product | Capture | AI organise / distil | Chat with notes | Graph / visual | Local markdown / ownership | Import | Sync / mobile | API / MCP | Pricing |
|---|---|---|---|---|---|---|---|---|---|
| **Obsidian** | iOS Quick Capture from Lock Screen/Control Center (mobile 1.14.0, 2026-09-02); Home Screen widget (1.14.1); Web Clipper | none native; plugins | plugins only | graph view, Canvas, Bases table/card/list/kanban (1.14.0, early access) | plain markdown, files are the format | opens files outside the vault (1.14.2, 2026-09-15, early access, desktop only) | Sync $4/user/mo annual; iOS/Android apps | official CLI (requires app running); headless Sync; no official MCP found | free app; Sync $4–5; Publish $8–10; Commercial $50/yr; Catalyst $25 |
| **Logseq** | mobile apps (Capacitor 8) | none native | none; `logseq-answer-machine` skill via CLI | graph view | 2.0 DB beta (2026-07-13) moves to a database; "Markdown Mirror" projects to disk | higher-fidelity markdown import (May, dated) | self-hosted sync URL (dated); sync open to sponsors; price not found | CLI; plugin API; no official MCP found | free, open source |
| **Heptabase** | inbox with triage (2026-09-16) | "Break down book" skill makes citation-backed whiteboards (08-14) | yes, whiteboards and PDF pages as context (08-04) | whiteboards, mini map (09-23); graph view not found | proprietary; PDF markdown export (08-24), CSV/Excel (08-27) | PDF | mobile with AI Agent (08-18); offline not found | MCP creates and edits notes (v1.105.0, 2026-08-24); CLI 0.6.0; ChatGPT plugin (09-23) | Pro $8.99/100 credits; Premium $17.99; Premium+ $53.99 |
| **Reflect (Open)** | daily notes; iPhone app in TestFlight | optional AI over your own markdown | BYO key (OpenAI, Anthropic, Google, OpenRouter), "no Reflect server involvement"; private notes blocked from AI | wiki links, backlinks; graph not found | open-source, MIT, plain files (2026-07-14) | not found | iCloud Drive or git; no account | CLI (`reflect today/search/show`); MCP belongs to the legacy app (dated), not found in Reflect Open README | Mac free; iPhone price not found |
| **Tana** | voice memos, transcription in 91 languages, fields auto-filled | AI fills supertag fields; meeting agent | AI chat | outliner; graph not found | JSON export ("technical, not user-friendly", dated review) | not found | apps; price gates AI | local API + MCP (2026-01-30, dated); "full MCP" on Pro | Free; Pro $20 early/$30; Max $80/$120 (confirmed by one checker; HTML had no figures for the other) |
| **Capacities** | web extension, email, WhatsApp, Telegram; audio recording (Release 71, 2026-09) | AI that can "edit and act" (R71); Related content (Pro) | yes (Pro) | graph view on free; no canvas | object model; export zip of markdown, csv, media | bulk markdown import | sync and offline on free plan; mobile criticised ("bafflingly poor execution on mobile", dated review) | hosted MCP at api.capacities.io/mcp, OAuth 2.1, read and write | Basic free with full-text search; Pro $9.99; Believer from $12.49; Plus $8.33 |
| **Anytype** | mobile apps | AI provider selection (0.57.0, 2026-09-22); local agent prototype (dated) | via chosen provider | graph (dated) | local-first, encrypted, AnyBlock v2 export preview | not found | paid sync (price not found); space-scoped grants | official anytype-mcp (525★) | app free; sync paid |
| **Mem** | web, desktop, mobile; offline (2.0, dated) | agentic chat that can "create, edit, and organize notes for you" (dated) | yes; "Deep Search" | not found | proprietary; Markdown export on every plan | not found | offline on all platforms (dated) | Claude Connector (date not found) | Free 25 msgs/25 notes; Plus $9; Pro $29; Pro 20× $199 |
| **Recall** | browser extension (Safari, Edge added 08-19); CSV import of 1,000 URLs (09-25) | AI turns saved content into cards | chat with several cards | Graph View 2.0 with Path Finder, Focus, Timeline (2026-01-12, dated) | proprietary; batch Markdown export (06-04) | EPUB (09-12), OCR on images | not found | MCP not found | not found |
| **Gemini Notebook** | upload sources | grounded answers with citations; Studio outputs | yes, notebook-scoped | not found | not found | sources | synced with Gemini app (2026-07-16) | not found | not found; cloud computer for Ultra/Workspace first |
| **Loom** | none (Inbox note only via "Write a note about it") | none (Claude world is seeded data, not a model) | none | Brain Map (Force/Circle/Hex/Rings, two worlds) and d3 graph with local graph | plain markdown in R2, Obsidian syntax; no user-facing whole-vault export found | .md and PDF; import jobs (Chrome/Edge only) | web only; one ≤799 px breakpoint; no offline | none public; seed service token only | not priced; invite only |

### What each does that Loom does not

- **Obsidian:** lock-screen quick capture and widgets; opens and edits files outside the vault (early access); Bases views over properties; a CLI for agents; headless sync for servers. Praised for ownership and speed; complained about for plugin security ("Community plugins are too risky running with full system access", HN, dated) and paid sync.
- **Logseq:** a CLI, plugin API and mobile apps. Its DB rewrite is the cautionary tale in H7: users who chose it for markdown feel betrayed.
- **Heptabase:** a read-and-write MCP, inbox triage, citation-backed AI breakdowns of books, find-and-replace, backlinks with search/sort/collapse, mobile AI. Complained about (dated) for growing complex.
- **Reflect Open:** BYO key with no vendor server in the loop, and a per-note private flag that keeps AI out. That flag is the cleanest expression of CR-097 shipped by anyone.
- **Tana:** voice capture that fills typed fields, local API and MCP. Complained about for overwhelming workflows and a "technical" export.
- **Capacities:** the widest capture surface (email, WhatsApp, Telegram, extension, audio), full-text search on the free plan, version history, hosted OAuth MCP with `saveToDailyNote`. Complained about for mobile.
- **Anytype:** local-first encryption, cross-space search, space-scoped API grants. In-window user voice is one comment: "Craft, AnyType, etc are janky, gimmicky or slow." (bernieo, HN 49866787, 2026-09-27). The "free as in: no logins… Syncing is paid" quote from the same thread is not verifiably Anytype's founder and is dropped as Anytype evidence.
- **Mem:** offline on every platform, agentic editing, "Heads Up" resurfacing, a Claude connector, markdown export on every plan. "Expensive upgrade" per Zapier (2026-08).
- **Recall:** the strongest web-capture pipeline (extension, bulk URL import, OCR, EPUB), text-or-AI search modes, graph Path Finder.
- **Gemini Notebook:** grounded Q&A with citations, praised for "not hallucinating" (msh, HN, 2026-07-17) and criticised for friction ("several minutes to make a podcast… disappear after a while", d4rkp4ttern). Its media outputs do not fit Loom.

**Cross-product facts that matter:** all ten (and Notion) ship an MCP, CLI or API. Five of six in group B ship chat grounded in your notes with citations. Version history is a paid feature at Capacities and standard at Trilium. Offline is still weak in cloud tools except Capacities and Mem. The "AI proposes, you approve" pattern is now vendor-shipped (Notion suggested edits, 2026-08-28; Copilot "Review Codex's plan", 2026-09-23).

---

## 5. What Loom is missing and should add

Ranked by pain × how often raised × fit with the two-worlds design. Fit is judged against D-111/113/114 (per-person isolation), D-131 (brought-in notes read only), D-170 (nothing may depend on his Mac) and CR-097 (AI never writes his notes unasked).

| # | Gap | Size | Evidence (strength) | Who has it | Fit with two worlds |
|---|---|---|---|---|---|
| 1 | **Per-person MCP server / public API**, read first, propose-only tier, scoped to the signed-in vault | L | W1 S3; H6; all 10 products plus Notion ship one; basic-memory, SiYuan (OAuth 2.1, 2026-09-28), Trilium REST | Capacities, Heptabase, Anytype, Tana, Notion, SiYuan | High. Lets any agent read the wiki and write only to the Claude world; replaces the Mac push (D-140, CR-085) so D-170 is met; D-114 by construction |
| 2 | **Search index**: full-text with ranking, prefix/word matching, snippets, in D1 | M | H5 S3; Trilium v0.106 ranking and snippets; Capacities free-plan full text | Capacities, Trilium, basic-memory | High. D-125 forbids an index file in the vault, not in D1. Fixes "art matches chart" directly |
| 2b | **Search by meaning and "related notes" suggestions** the user accepts or rejects | L | H5, W4 S3; Smart Connections, basic-memory, Khoj | Smart Connections, basic-memory, Recall, Mem | High; suggests, never writes (CR-097). Astro-Han's counter-point: grep suffices under about 100K tokens of curated wiki |
| 3 | **Quick capture**: phone-width capture page, PWA share target, unsent draft kept, lands in Inbox with no filing | M | W3 S3; H8 | Obsidian, Capacities, Memos, Trilium | High; capture lands in My notes |
| 4 | **Version history and a trust package**: per-note history with diff and restore, "we never auto-purge", one-click whole-vault download | M (history) + S (export) | H1 S3, H2 S3, W5 S2, L1 S3; basic-memory top requests #124/#59 | Capacities, Trilium, SilverBullet (Git), basic-memory, Mem export | High; both worlds. Prerequisite for any AI write |
| 5 | **Inbox that Claude distils into the Claude world, with approve / reject / diff** | L | W2 S3 (pattern), W4 S3, W5 S2 | claude-obsidian, llm-wiki-agent, Heptabase, Notion suggested edits | Exact fit: raw = brought-in read-only notes, Claude world = AI-kept wiki, wiki = only what he promotes. Blocked by D-131 until he decides |
| 6 | **AI world per person, more than Claude**; import ChatGPT/Claude chat exports as notes | M | W6 S2, H6 S2 | Notion (users do it by hand), obsidian-second-brain (7 agents) | High; fills the Claude side, never the wiki. Conflicts with D-140's Mac-only seed, which D-170 already wants gone |
| 7 | **Mobile and offline**: real phone UI (CR-102), offline decision (CR-069, D-108) | L | H8 S3, H1 S3 | SilverBullet PWA, Capacities, Mem | Medium; hosted web is already the answer to "no install" and "computer off"; the gap is UX |
| 8 | **"What matters now" and recent activity**: Today/overdue across boards, last-changed view | M | W7 S2 | TaskFlow, Memos calendar, obsidian-second-brain morning brief | High; reads Kanban and notes, writes nothing |
| 9 | **Views over properties**: saved searches, tables with filters, cards | M | W8 S2 | Obsidian Bases, Memos Views, SilverBullet queries, Trilium | High; D-130 everything is a note, front matter already exists |
| 10 | **Vault-health report**: orphans, broken links, stale notes, contradictions flagged | S | W5 S2; llm-wiki-agent, obsidian-second-brain `/obsidian-health`; gist lint | llm-wiki repos | High, both worlds; no AI needed for orphans and links |
| 11 | **More import formats, PDF text and OCR, highlight-to-note** | M | W9 S2 | llm-wiki-agent (markitdown), SiYuan OCR, Third Mind Reader, Heptabase | Medium; extends CR-107 |
| 12 | **Hide a folder or note from search and from AI**; a `private:` flag | S | W11 S2 | Reflect Open, Notion users asking | High; pairs with the world switch |
| 13 | **Reviewed / unverified badge** on notes, with overwrite protection | S | W5 S2; gist sidleo; obsidian-llm-wiki `reviewed: true` (unverifiable in fetch) | llm-wiki repos | High; seeded Claude notes start "unverified" |
| 14 | **Edit files outside the vault** | L | single vendor release thread (939–1,131 snapshot); comments are the only user voice | Obsidian (early access) | Low today: needs CR-121 helper app or CR-120 connectors under D-170, and a D-131 decision |
| 15 | **Web clipper / send a link in** | M | S1 | Recall, Memos, Obsidian, Capacities | Medium; only if capture (3) exists first |
| 16 | **Encryption so no admin can read notes** | L | S1–S2 | Anytype, Trilium per-note | Low; conflicts with server-side search and proxy |
| 17 | **Graph diagnostic lenses** (orphans, unlinked, stale) rather than more layouts | M | L3 contested | Recall Path Finder, Heptabase mini map | Medium; UX, needs his input |

Not gaps but strengths to state out loud: plain markdown in R2 that Obsidian opens; no plugins to sprawl; no in-app AI; per-person isolation (D-114); browser-first with no install; a two-worlds graph nobody else has.

---

## 6. Stand-out features that would differentiate Loom

Each is grounded in a pain above and sized S/M/L.

1. **The review boundary as a product.** Nobody hosts the raw → wiki → owner's-notes split; people build it by hand with folders and rules ("raw/ frozen and read-only", "append only"). Loom already has three tiers: brought-in read-only notes, the read-only Claude world, and the editable wiki. Make the boundary visible: a Proposals panel where anything an agent or an import produces waits, with approve / reject / diff, and nothing crosses into My notes without a click. Answers W2, W4, W5, H3 and CR-097 in one shape. **L**, depends on #4 history and either #1 MCP or CR-093.

2. **A hosted, per-person, read-first MCP with a propose-only tier.** The trust shock of the window was a vendor MCP injecting ads (223/26). Loom can publish its tool text, scope every token to one person's vault (D-114), and give agents "read wiki, write proposals" by default. It also ends the Mac dependency (D-170) for the Claude world. **L**.

3. **"Your vault, downloadable" as a promise page.** H2 and L1 say trust is decided by whether you can leave. One button, a zip of plain markdown, and Help/FAQ/site copy saying "sync is not a paid add-on, we never auto-purge, AI never writes your notes unasked". The copy is outward-facing and needs Stuart's call. **S**.

4. **The Claude world as portable memory with provenance and a staleness check.** H6 says vendor memory is opaque and cannot be forgotten. Loom's session and memory notes, with `unverified` badges, source links held as ordinary `[[links]]` in the graph (crajah's design), and a "last confirmed" property, would be the memory layer people say they want and can inspect. **M**, after CR-085.

5. **Search that finds the idea, then shows the source.** Full-text with snippets first; then "you wrote something similar in March, want to link them?" as a suggestion card, never an auto-link (the false-positive complaint in W4). **M then L**.

6. **Capture into Inbox from the phone with no filing.** The hosted app already answers "installing files is forbidden" and "computer always on"; a phone-width capture page with an unsent draft kept makes that concrete. **M**.

---

## 7. Part 3: top 10 repos

Stars, last push and licence are from GitHub MCP repository search fetched 2026-09-28. Release dates come from atom feeds or release pages, not page summaries (which mangled years). Issue reaction counts were not shown on fetched pages.

| Repo | Stars (2026-09-28) | Last push | Licence | What it is | What Loom should borrow |
|---|---|---|---|---|---|
| basicmachines-co/basic-memory | 4,053 | 2026-09-26 | AGPL-3.0 | MCP-native markdown memory for AI clients; v0.23.x 2026-08-24/25 | "AI and humans write to the same files; sync keeps them in step"; semantic search with reranking; point-in-time restore; tool annotations (read-only vs destructive) |
| eugeniughelbur/obsidian-second-brain | 4,628 | 2026-09-28 | MIT | memory and skills for Claude Code plus 7 other agents (repo description); created 2026-03-24 | morning brief, nightly consolidation, vault-health check, stale/overdue triage; the auto-rewrite ("The vault REWRITES itself") only inside the Claude world |
| SamurAIGPT/llm-wiki-agent | 3,583 | 2026-09-21 | MIT | raw/ ingest into an interlinked wiki; repo repurposed (created 2023) | contradiction flags at ingest; lint for orphans, broken links, missing pages; markitdown conversion of PDF, DOCX, PPTX, XLSX, EPUB and more |
| silverbulletmd/silverbullet | 6,163 | 2026-09-28 | MIT | browser-based, self-hosted, PWA; 2.11.1 on 2026-09-22 | "100% offline capable"; revisions kept in Git; query language as saved views; in-editor audio/video/PDF |
| TriliumNext/Trilium | 38,047 | 2026-09-28 | AGPL-3.0 | hierarchical notes; v0.106.0 2026-09-25 | note versioning; per-note encryption; REST API; web clipper; touch mobile front end; ranked search with exact-phrase and snippet cards; Kanban column limits and archive |
| siyuan-note/siyuan | 46,539 | 2026-09-28 | AGPL-3.0 | privacy-first workspace "with agents"; v3.8.6-beta.1 2026-09-28 | built-in MCP with OAuth 2.1; AGENTS.md instructions; PDF annotation links; OCR; table views; export to PDF/Word/HTML |
| logseq/logseq | 45,071 | 2026-09-28 | AGPL-3.0 | outliner; 2.0 DB beta 2026-07-13, "splitting into two versions" | CLI and plugin API; the DB migration backlash is a warning, not a model |
| brianpetro/obsidian-smart-connections | 5,471 | 2026-09-24 | NOASSERTION | related notes by local embeddings; v4.7.x 2026-08-05/06 | a "related notes" panel by meaning: inline and footer connections, drop a file to compare; suggests, never writes |
| logancyang/obsidian-copilot | 7,762 | 2026-09-28 | AGPL-3.0 | agents inside the vault; v4.0.11 2026-09-23 | "Review Codex's plan before it starts making changes"; Quick Ask on a selection (explicit request only under CR-097); projects with their own instructions |
| usememos/memos | 63,387 | 2026-09-27 | MIT | capture-first notes; v0.30.0 2026-07-26 clipper, v0.31.0 2026-09-19 Views | "save without choosing a title, folder, or template"; saved filters as Views; calendar view; top open request #6231 "Offline PWA" (2026-08-24) |

Runners-up: khoj-ai/khoj (37,526★, pushed 2026-08-02) for answers over your docs from phone or WhatsApp; Astro-Han/karpathy-llm-wiki (2,376★, 2026-07-23) for the counter-argument that grep beats vectors on a curated wiki; AgriciDaniel/claude-obsidian (15,270★, v2.2.0 2026-09-10, created 3 days after the gist) for "one logical knowledge operation is one recoverable transaction". Excluded from evidence: KNN-07/ObsidiAI (0★, created 2026-09-20) and julianoczkowski/karpathy-llm-wiki (54★); kytmanov/obsidian-llm-wiki-local (828★) has not been pushed since 2026-05-26 and is in maintenance mode.

Excluded from the ten by shape: AppFlowy (76,974★), AFFiNE (73,053★), Outline (40,731★), Anytype-ts (8,861★) as Notion-style or team products; Quartz (13,297★) as a publisher; Foam (17,422★) as a VS Code extension; Joplin (56,516★) as close to Trilium.

### Repo gaps against Loom, in order

1. Version history and restore (Trilium, SilverBullet, basic-memory) → CR-119. **M**
2. MCP or API (basic-memory, SiYuan, Trilium, Logseq CLI) → new. **L**
3. LLM-wiki distillation in the Claude world (llm-wiki-agent, obsidian-second-brain, claude-obsidian) → CR-093/094. **L**
4. Offline PWA and phone UI (SilverBullet, Trilium, Memos #6231) → CR-069/102. **L**
5. Related notes by meaning (Smart Connections, basic-memory) → new. **M**
6. Ranked keyword search with snippets (Trilium v0.106) → new. **S–M**
7. Quick capture and clipper (Memos, Trilium) → CR-092/098. **M**
8. Saved views and tables (Memos, SilverBullet, SiYuan) → CR-030/096. **M**
9. Vault-health lint (llm-wiki-agent, obsidian-second-brain) → new. **S**
10. File conversion and OCR on import (llm-wiki-agent, SiYuan) → CR-108. **M**
11. AI on a selected passage, explicit request only (Copilot, Trilium) → new. **M**
12. Per-note encryption (Trilium) → CR-068. **L**
13. Export to PDF/Word/HTML (SiYuan) → CR-024 is narrower. **S–M**
14. Kanban hygiene: WIP limits, archive, stale-card triage (Trilium, obsidian-second-brain) → new. **S**

Out of scope by D-111/113/114: Memos Spaces, basic-memory Teams, Trilium multi-user (#4956).

---

## 8. Mapping to Loom CRs

Statuses are verbatim from CHANGE_REQUESTS.md as read in the baseline. Early CRs 001–041 that still read "open" are stale per CR-072 and are not listed as gaps.

| Recommendation | CR | Status line | Note |
|---|---|---|---|
| Per-person MCP / public API, read-first, propose tier | **new CR candidate** | — | nearest: CR-089 (AI world per person) `Open — logged, not started`; CR-085 (keep Claude world in step) `Open`. Becomes a CR only when he picks it |
| Full-text search index in D1 with ranking and snippets | **new CR candidate** | — | CR-030 (saved search view) `Open — logged, not started` is adjacent; CR-055 (large loads) `Open — waiting for your decision` |
| Search by meaning; related-notes suggestions | **new CR candidate** | — | must suggest only (CR-097) |
| Quick capture, phone-width, Inbox-first | CR-092 | `Open — waiting for your decision` | CR-081's "Obsidian changelog only" label is now out of date: about 4 independent r/ObsidianMD threads, about 12 in r/NoteTaking/r/Notion, Reddit cross-check 406/66 |
| Version history with diff and restore | CR-119 | `Open — logged, not started` | prerequisite for any AI write; also the guardrail people ask for most |
| Whole-vault export; "never auto-purge" statement | CR-069 | `Open — waiting for your decision` | D-108 leaves CR-069 ambiguous between one-off export and offline sync; the export reading is S, the offline reading is L |
| Inbox that Claude distils, approve/reject/diff | CR-093 | `Open — waiting for your decision` | now S3 for the pattern (was "blogs only"); blocked by D-131; must obey CR-097 |
| Claude world as an LLM wiki with provenance | CR-094 | `Open — waiting for your decision` (changes D-131) | evidence grew from "one post, 9 upvotes" to the gist comments and about 6 independent X users |
| AI world per person; import ChatGPT/Claude chat exports | CR-089 | `Open — logged, not started` | supported by 1w81gm5, r/PKMS 13 threads, X 7 posts (low engagement) |
| Keep the Claude world in step without the Mac | CR-085 | `Open` | MCP or an import path satisfies D-170; launchd/hook options do not |
| "What matters now" view | CR-099 | `Open — waiting for your decision` | S2; TaskFlow is a builder post |
| Recent activity view | CR-124 | `Open — logged, not started` | pairs with CR-099; resurfacing evidence is S1 so keep it simple |
| Views over properties, tables, cards | CR-096 | `Open — waiting for your decision` | CR-081's "blogs and forum" label is out of date: about 12 r/ObsidianMD threads |
| Phone UI; open brought-in files on other devices | CR-102 | `Open — logged, not started` | H8 S3 |
| Offline mode | CR-069 (offline reading) | `Open — waiting for your decision` | needs D-108 settled first |
| Vault-health report (orphans, broken links, stale) | **new CR candidate** | — | extends CR-021 struck-through links and CR-125 label pile-up |
| Hide folder/note from search and AI; `private:` flag | **new CR candidate** | — | design rule inside CR-097 as much as a feature |
| Reviewed / unverified badge with overwrite protection | **new CR candidate** | — | custom properties already exist |
| More import formats, PDF text, OCR, highlight-to-note | CR-108 | `Open — logged, not started` | "all main file formats" |
| Web clipper / send a link in | CR-098 | `Open — waiting for your decision` | still S1; do not prioritise on this evidence |
| Edit files outside the vault | CR-095 | `Open — waiting for your decision` | single vendor thread; depends on CR-121 `Open — logged, not started` or CR-120 `Open — logged, not started` under D-170, and a D-131 decision; CR-118 two-way sync is "later" |
| Encryption so no admin can read notes | CR-068 | `Open — waiting for your decision` | S1–S2 |
| Onboarding import walkthrough | CR-091 | `Open — logged, not started` | H4 overwhelm supports it; S |
| Graph diagnostic lenses | CR-078 Fly To / CR-125 | `Open — waiting for your decision` / `Open — logged, not started` | graph evidence contested; UX, ask him |
| Kanban hygiene (WIP limits, archive, stale triage) | **new CR candidate** | — | S |
| AI on a selected passage, explicit request only | **new CR candidate** | — | related to CR-089; CR-097 check |
| Email-me-a-code sign-in for locked-down work machines | CR-058 | `Open — waiting for your decision` | supports W10 |
| "No AI unless I ask" as a visible promise in Help, FAQ and site | CR-097 | `Open — waiting for your decision` | a design rule, not a build; the best-supported attitude in every source |
| Rename Import jobs to Job Scheduler | CR-126 | `Open — logged, not started` | no market evidence either way |

Under D-170 every item above must work for any signed-in person; none may depend on his Mac. Under D-114 every MCP or API token is scoped to one vault. Nothing is done until Help, the FAQ and the Guides, CHANGES.md and the ledger match.

---

## 9. Caveats

- **Archive scores are snapshots.** The same Obsidian 1.14.2 thread shows 939/92 (Arctic Shift), 1,113/99 (v3 pull) and 1,131/99 (Mac runs). Cite one and say so.
- **Reddit live pages were unreachable** to every sweep and both checkers, so Reddit-only claims (Notion "$240, 150%", the Notion MCP ad injection post) are confirmed against the archive text but unverifiable on any official page.
- **Thin samples:** r/logseq has 21 posts; r/ClaudeAI covers 2026-09-26 to 09-28 only; r/ObsidianMD's 500-post cap drops everything before 09-12; the v3 pull is 53 mostly title-only items with all six YouTube videos outside the window.
- **Vendor noise:** by regex, 56 r/Notion and 32 r/NoteTaking posts are "I built"; about 12 of 78 r/PKMS posts and about 12 of 53 v3 items are self-promotion; most Mac-run LLM-wiki and quick-capture items are creator, course-funnel or sponsored content (the 584,613-view "Obsidian in 24 Minutes" video is Genspark-sponsored). Builder posts were never sole support.
- **Attribution corrections applied:** the HN "free as in: no logins… Syncing is paid" quote is not verifiably Anytype's founder (it is a Show HN for a markdown editor) and is not used as Anytype evidence; the kepano headless-Sync line is articsputnik quoting kepano and actually reads "give tools like OpenClaw access to a vault without access to your full computer" [dated]; "capture something quickly → AI organizes it" sits under 1wi44ch, not 1wi4twu, and appears twice, not three times; the "600+ clips" figure is unverified; the "6 other CLI agents" line is a repo description and lists 7 other harnesses.
- **Product corrections applied:** Heptabase's 2026-08-24 MCP creates and edits, not read-only; Logseq 2.0 DB beta is 2026-07-13 (in window); Obsidian 1.14.x is early access (Catalyst), not GA; Reflect's MCP belongs to the legacy app and is not in the Reflect Open README; Notion's `mcp.notion.com` host and the Custom Agents "May 4" start are unverifiable; Obsidian CLI "100+ commands" is blog-only; Capacities lists 19 tool names under a "16 tools" heading; Notion skills export also targets Gemini and Grok; Tana prices were confirmed by one checker and invisible to the other (JS-rendered page).
- **Dated items that sweeps had placed in window:** HN 48351115 is 2026-06-01, so the NoWayDude1 and cyanydeez quotes are dated; HN 47899844 (2026-04-25) and 47640875 (2026-04-04) are dated; the Karpathy gist is 2026-04-04, with only its comments (2026-09-10 to 09-23) in window; every graph "hairball" criticism is dated.
- **Unverifiable and left as such:** gist "5,000+ stars" exact count (GitHub caps the display); basic-memory cloud "$15/month"; Trilium "cards from templates"; obsidian-llm-wiki `reviewed: true`, tag gate and "Smart Fix All"; claude-obsidian release year on the page (atom confirms 2026-09-10); Logseq sync price; Gemini Notebook, Recall and Reflect iPhone prices; Mem Claude Connector date; the scientific study on "degradation of output quality" cited by stingraycharles; the Microsoft/CMU survey snippet.
- **Counts are tallies**, made by readers from the files, not figures from any page, and theme sizes such as "about 23 threads plus 11 reposts" were not re-tallied by the checkers; read them as estimates of distinct threads.
- **Quotes from the Mac-run file** are as last30days recorded them; non-English quotes carry the reader's own translation. Archive text is cut off mid-sentence in places and was not completed.
- **Blocked in this session:** api.github.com and GitHub MCP release/issue tools for repos other than wosikas/stuart-general; github.com HTML from one checker's session; discussion.evernote.com; Medium; cassolotl.tumblr.com; HN 48184312; tana.inc/releases; the Mem changelog.

---

## 10. Evidence

### Part 1: sentiment

Reddit archive files (read in full): /home/user/Stuart-general/loom-research/reddit/archive-text/ObsidianMD.md, logseq.md, Notion.md, NoteTaking.md, PKMS.md, ClaudeAI.md, mac-runs-x-youtube-tiktok-instagram.md. v3 pull: /home/user/loom/research/2026-09-22-pkm-market-pull-raw-v3.md.

r/ObsidianMD: https://www.reddit.com/r/ObsidianMD/comments/1wlw7cr/ (2026-09-20); 1wlgslq; 1wmqk1c; 1wj64hi; 1wo6hf0 (09-23); 1wfqyj2 (09-14); 1wf9rvk (09-13); 1wjrhsd (09-18); 1wlea3k (09-20); 1wr0wff (09-26); 1wf8oai (09-13); 1wptcsf (09-25); 1wpqy7v (09-25); 1wq25a8 (09-25); 1wq7tw0 (09-25); 1wpszn3 (09-25, builder); 1wp9ghh (09-24); 1wp9kjz (09-24); 1wpr9zp (09-25); 1wgted1 (09-15); 1wh8r77 (09-15); 1wg8a64 (09-14, builder); 1wonlxo (09-24); 1wgp2aa (09-15); 1wlkkh8 (09-20); 1wmg4o2 (09-21); 1wlsdc6 (09-20); 1wi1izj (09-16); 1wk7uln (09-19); 1wov38g (09-24); 1wf2eg6 (09-13); 1woxyrg (09-24); 1wfcflo (09-13); 1wjz07a (09-18); 1whmk2j (09-16); 1wiq2n9 (09-17, vendor); 1wnehzb (09-22, builder); 1wo4a4k (09-23); 1wn3l6q (09-22); 1wpmnmx; 1wnvys9; 1wg6g8s; 1wfed1a (vendor); 1wnucsp (09-23); 1wlwc8q; 1wq1rpk; 1wl1lfm; 1wkzpzk.
r/logseq: https://www.reddit.com/r/logseq/comments/1wcrinu/ (09-10); 1w5dwuo (09-02); 1wakh14 (09-08); 1wgd8vb (09-14).
r/Notion: https://www.reddit.com/r/Notion/comments/1wnd3w5/ (09-22); 1w7h98m (09-04); 1woxf2g (09-24); 1wnk59m (09-22); 1wlbmw8 (09-20); 1wngksq (09-22); 1wkhmn0 (09-19); 1wmih10 (09-21); 1w1xg5s (08-29); 1wbshy5 (09-09); 1wiwki4 (09-17); 1w45yif (09-01); 1wgptwb (09-15); 1wi44ch (09-16); 1wjhb77 (09-18); 1wo5671 (09-23); 1w81gm5 (09-05); 1w7h5m6 (09-04); 1w9depq (09-07); 1wdoe35 (09-11); 1whlxht (09-16); 1wpdy2i (09-24); 1w3fvtb (08-31); 1w3dwat (08-31); 1wnduji (09-22); 1w9a9ko (09-06); 1wem2m3 (09-12); 1wkhape (09-19); 1wbti4a (09-09); 1we53hr (09-12); 1w847yv (09-05); 1wno7wj (09-22); 1wl2t46 (09-20).
r/NoteTaking: https://www.reddit.com/r/NoteTaking/comments/1w7eshs/ (09-04); 1wjutfm (09-18); 1wpk5q7 (09-25); 1wm0chb (09-21); 1wgceic (09-14, builder); 1wpm7qf (09-25); 1wpst0s (09-25); 1wfspzy; 1wl6klx (09-20); 1wrdxt5 (09-27).
r/PKMS: https://www.reddit.com/r/PKMS/comments/1w41j89/ (09-01); 1w6hnx9 (09-03); 1w63be9 (09-03); 1w9yjli (09-07); 1whuws4 (09-16); 1wnc747 (09-22); 1whb2b6 (09-15); 1wigzar (09-17); 1wgouq4 (09-15); 1w94mqf (09-06); 1w9iru9 (09-07); 1w7yyml (09-05); 1w4rav6 (09-01); 1wbrqp7 (09-09); 1wepbpe (09-12); 1wlcbes (09-20); 1w6qsx5 (09-04); 1w6oj89 (09-04); 1w7g02h (09-04); 1w91k3h (09-06); 1w4vx4h (09-02, vendor comment); 1woj39t (09-23); 1wjr8ki (09-18); 1wfx9pj (09-14); 1wecii9 (09-12); 1wjhdrr (09-18); 1w8rhv5 (09-06).
r/ClaudeAI: https://www.reddit.com/r/ClaudeAI/comments/1wrecia/ (09-27); 1wqy2h8 (09-26); 1wrgvqj (09-27); 1wrhukk (09-27); 1wrckhp (09-27); 1wr74y0 (09-27); 1wqxk90 (09-26).
Other subreddits from v3: https://www.reddit.com/r/Zettelkasten/comments/1wmbyyu/ (09-21); https://www.reddit.com/r/ClaudeCode/comments/1wga9u4/ (09-14, off-topic).
X: https://x.com/NixFred/status/2103926191656779984 (09-26); https://x.com/paulo_caelum/status/2103915232829526402 (09-26); https://x.com/obsidianstudio9/status/2103623080228860329 (09-25); https://x.com/obsidianstudio9/status/2103985468270678332 (09-26); https://x.com/obsidianstudio9/status/2103686001302589646 (09-26); https://x.com/omx0r/status/2104021309235646773 (09-27); https://x.com/bond_ai1/status/2104142502521700596 (09-27); https://x.com/skasper/status/2103479899964997646 (09-25, vendor); https://x.com/Sid_899/status/2104157903330361493 (09-27); https://x.com/VoibeAI/status/2104091410920042500 (09-27, competitor); https://x.com/ZohoNotebook/status/2102746978656673915 (09-23); https://x.com/XaiKeursang/status/2104144819954008356 (09-27); https://x.com/heartsker/status/2104108529179046338 (09-27, vendor); https://x.com/DanKornas/status/2099271662260675062 (09-13, showcase); https://x.com/sumika45379/status/2103975404046528682 (09-26).
YouTube: https://www.youtube.com/watch?v=4Hvkv_I8QDE (09-17, sponsored); https://www.youtube.com/watch?v=mZ8L3uVNxnM (09-09); https://www.youtube.com/watch?v=TChuHZ2RRDA (09-22); https://www.youtube.com/watch?v=zlFTFUIkKU8 (09-20, vendor); https://www.youtube.com/watch?v=_bieksxg6oY (08-29); https://www.youtube.com/watch?v=82hCt3xH9Gc (08-29, promo); https://www.youtube.com/watch?v=WDXzH8w4X9A (09-10); https://www.youtube.com/watch?v=4bpMXr3g41c (09-13); https://www.youtube.com/watch?v=oXYHcyV_1Nw (09-23); https://www.youtube.com/watch?v=yysILVsfLFM (09-07); https://www.youtube.com/watch?v=EOdXR6lU5ZA (09-25); https://www.youtube.com/watch?v=QEeInozatMQ (09-14, vendor); https://www.youtube.com/watch?v=G9cteLDjLrE (09-27); https://www.youtube.com/watch?v=a1FDaoF8Jog (2025-09-11, dated).
TikTok: https://www.tiktok.com/@jackroberts____/video/7685020032639847713 (09-13); https://www.tiktok.com/@migue.baena/video/7686505064327843094 (09-17); https://www.tiktok.com/@andersenbuilds/video/7689557425510190338 (09-25); https://www.tiktok.com/@moogletechnology/video/7685815623418498325 (09-15, vendor); https://www.tiktok.com/@luispdoesai/video/7682770424408624397 (09-07); https://www.tiktok.com/@lafrancesmendez/video/7685630780705410334 (09-15); https://www.tiktok.com/@se13naaaa/video/7682943701823343885 (09-07); https://www.tiktok.com/@sleepygmeow/video/7687059357523021070 (09-19); https://www.tiktok.com/@danielbrown.ia/video/7684395838424091924 (09-11); https://www.tiktok.com/@josh.castell7/video/7681335959241116942 (09-03); https://www.tiktok.com/@zazenalex/video/7680298004007390486 (08-31); https://www.tiktok.com/@pro.glitch/video/7687948660000165134 (09-21); https://www.tiktok.com/@thepremedvault/video/7688235386522389773 (09-22).
Instagram: https://www.instagram.com/reel/DdeHzRAM5de/ (09-19); https://www.instagram.com/reel/Dcrxx_Pux5K/ (08-31); https://www.instagram.com/reel/Ddhmc-kyHvK/ (09-20); https://www.instagram.com/reel/Ddp0ENdxseK/ (09-24); https://www.instagram.com/reel/DdBhk5lkfcI/ (09-08); https://www.instagram.com/reel/DdXHE4chGs4/ (09-16).
Hacker News (in window unless marked): https://news.ycombinator.com/item?id=49680177 (09-13); 49375701 (08-20); 49651241 (09-10); 49874274 (09-28); 49674420 (09-12); 49673926 (09-12); 49866787 (09-27); 49094907 (07-29); 48899393 (07-13); 48896645 (07-13); 48897269 (07-13); 48897020 (07-13); 49869781 (09-27); 48897616 (07-13); 48896816 (07-13); 48898993 (07-13); 48898361 (07-13); 48899408 (07-13); 49868904 (09-27); 49869398 (09-27); 49871505 (09-27, attribution unverifiable); 48944975 (07-17); 48948063 (07-17); 49645994 (09-10); 49670907 (09-12); dated: 47198413, 47197741, 47198841, 47826223, 47824945, 48088576, 48109970, 47197432, 48119082, 48111661, 48681662, 47197267, 47640875 (04-04), 47899844 (04-25), 48351115 (06-01), 47709940 (04-09), 47656181 (04-06), 49481969 (08-28), 47670947 (04-07).
Blogs and forums: https://alexkras.com/my-last-six-months-at-evernote-after-bending-spoons-took-over/ (09-12/17); https://brennan.day/what-have-note-taking-pkms-accomplished-really/ (07-17); https://korin.uk/your-second-brain-wont-do-the-work (09-21); https://withdocket.com/blog/why-im-building-a-note-taking-app-without-ai (undated, vendor); https://dessence.ai/blog/why-second-brains-keep-becoming-graveyards (05-21, dated, vendor); https://danholloran.me/posts/making-obsidians-graph-view-actually-useful (06-12, dated); https://tech.yahoo.com/apps/articles/evernotes-2026-price-hike-absurd-130514271.html (03-24, dated); https://forum.obsidian.md/t/request-to-speed-up-the-startup-speed-of-the-mobile-app/91272 (2024, dated); https://forum.obsidian.md/t/your-mobile-quick-capture-solution/102085 (2025-06-20, dated); https://forum.obsidian.md/t/voxtral-transcribe-dictate-and-type-at-the-same-time-into-your-notes-with-voice-commands-feedback-welcome/112674 (comment 08-07); https://forum.obsidian.md/t/vault-change-feed-let-your-ai-agents-see-what-you-changed-without-rescanning-your-vault/116541 (07-27); https://dev.to/huy_tieu/i-finally-built-a-second-brain-that-i-actually-use-6th-attempt-4075 (2025-10-15, dated); https://dev.to/bokuwalily/i-dont-trust-the-llm-that-writes-my-shared-memory-3-regex-gates-before-claude-code-auto-commits-3i77 (09-24); https://www.xda-developers.com/replaced-notion-and-obsidian-with-gemini-and-notebooklm/ (05-11, dated); https://gnu.support/articles/lack-of-thinking/Critique-of-LLM-Wiki-Tutorial-Limitations-and-Production-Readiness-124404.html (undated); https://sphelps.substack.com/p/a-shared-memory-for-claude-code (02-25, dated); https://systemsculpt.com/blog/obsidian-ai-agents-with-approvals (04-17, dated, vendor); https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (created 2026-04-04, dated; comments 09-10 to 09-23 in window).

### Part 2: products

https://obsidian.md/changelog/ ; https://obsidian.md/changelog/2026-09-02-desktop-v1.14.0/ ; https://obsidian.md/changelog/2026-09-15-desktop-v1.14.2/ ; https://obsidian.md/changelog/2026-09-08-mobile-v1.14.1/ ; https://obsidian.md/changelog/2026-02-27-desktop-v1.12.4/ (dated) ; https://obsidian.md/help/cli ; https://obsidian.md/pricing ; https://www.ctnet.co.uk/obsidian-review-2026/ (03-30, dated) ; https://www.notion.com/releases ; https://www.notion.com/pricing ; https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look (2025-07-15, dated) ; https://developers.notion.com/guides/mcp/overview ; https://www.eesel.ai/blog/notion-ai-review (05-07, dated, vendor) ; https://github.com/logseq/logseq/releases ; https://discuss.logseq.com/t/whats-new-with-logseq-db-april-26-2026/34977 (dated) ; https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020 (dated) ; https://dessence.ai/blog/logseq-alternatives-after-stalled-development-2026 (05-24, dated, vendor) ; https://outliner.tana.inc/blog/the-next-chapter-for-tana (undated) ; https://outliner.tana.inc/blog/tana-api-mcp-voice-ai-workflows (01-30, dated) ; https://tana.inc/docs/local-api-mcp ; https://tana.inc/pricing ; https://outliner.tana.inc/docs/mobile-voice-memos ; https://www.saner.ai/blogs/tana-reviews (03-16, dated) ; https://capacities.io/whats-new ; https://capacities.io/pricing ; https://docs.capacities.io/tutorials/input-integrations ; https://docs.capacities.io/developer/model-context-protocol ; https://docs.capacities.io/reference/import ; https://github.com/inconceivablelabs/capacitiesMCP ; https://wiki.heptabase.com/changelog/changelog ; https://heptabase.com/pricing ; https://reflect.app/blog/reflect-open (07-14) ; https://reflect.app/blog/tags/product-updates ; https://reflect.app/blog/edit-notes-with-coding-agents (04-28, dated) ; https://github.com/team-reflect/reflect-open ; https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/ (07-16) ; https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html (07-16) ; https://freedom.tech/posts/2026-09-22-anytype-desktop-0-57-0/ ; https://github.com/anyproto/anytype-ts/releases ; https://github.com/anyproto/anytype-mcp ; https://blog.anytype.io/february-community-update-2026/ (dated) ; https://feedback.recall.it/changelog ; https://feedback.getrecall.ai/changelog/recall-release-notes-jan-12-2026-graph-view-20-and-much-more (dated) ; https://docs.recall.it/recall-roadmap ; https://www.recall.it/compare/best-second-brain-apps ; https://get.mem.ai/blog/introducing-mem-2-0 (2025-10-01, dated) ; https://get.mem.ai/blog/your-favorite-llms-can-now-use-your-second-brain-as-context (date not found) ; https://get.mem.ai/pricing ; https://zapier.com/blog/best-ai-notes-apps/ (08) ; https://zapier.com/blog/best-note-taking-apps/ (2025-12, dated) ; https://tana.inc/blog/best-second-brain-apps-2026 (07, vendor) ; https://releasebot.io/updates/obsidian ; https://www.rdworldonline.com/is-karpathys-viral-llm-wiki-helpful-mostly-yes-one-month-in/.

### Part 3: repos

GitHub MCP `search_repositories`, 2026-09-28, for all 19 candidates. READMEs via raw.githubusercontent.com (main branch) and release atom feeds: https://github.com/basicmachines-co/basic-memory (+/releases, /issues/124, /issues/59) ; https://github.com/eugeniughelbur/obsidian-second-brain ; https://github.com/SamurAIGPT/llm-wiki-agent ; https://github.com/silverbulletmd/silverbullet (+/releases) and https://silverbullet.md/ ; https://github.com/TriliumNext/Trilium (+/releases, /releases.atom, /issues/8481) ; https://github.com/siyuan-note/siyuan (+/releases) ; https://github.com/logseq/logseq (+/releases) ; https://github.com/brianpetro/obsidian-smart-connections (+/releases) ; https://github.com/logancyang/obsidian-copilot (+/releases) ; https://github.com/usememos/memos (+/releases.atom, /issues/6231) ; https://github.com/khoj-ai/khoj ; https://github.com/Astro-Han/karpathy-llm-wiki ; https://github.com/AgriciDaniel/claude-obsidian (+/releases) ; https://github.com/kytmanov/obsidian-llm-wiki-local ; https://github.com/green-dalii/obsidian-llm-wiki ; https://github.com/julianoczkowski/karpathy-llm-wiki ; https://github.com/KNN-07/ObsidiAI ; https://github.com/team-reflect/reflect-open ; https://github.com/anyproto/anytype-mcp ; https://github.com/Myraxion/obsidian-cli ; https://github.com/pizza-bot-app/pizza-bot ; https://usealmanac.com/ ; https://www.kunalganglani.com/blog/llm-wiki-karpathy-local-knowledge-base (snippet only).

### Loom baseline

Files read under /home/user/loom/: CLAUDE.md, .claude/key_rules.txt, SESSION_HANDOFF.md, PRODUCT.md, CHANGES.md, CHANGE_REQUESTS.md, CHANGE_REQUESTS_DONE.md, CHANGE_REQUESTS_NOTES.md, SESSION_HANDOFF_ARCHIVE.md, DECISIONS.md, API_CONTRACT.md, worker/index.js, app/src/Sidebar.jsx, app/src/styles.css. The previous report, /home/user/Stuart-general/loom-market-research-2026-09-25.md, was not modified.

Skills/MCPs used: custom research workflow (Workflow tool), WebSearch, WebFetch, GitHub API, Arctic Shift archive, last30days (Mac runs), Artifact; sub-agents Opus 5.5 for reading and sweeps, Fable 5.1 for fact-checking and writing
