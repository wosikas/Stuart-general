# Claude design kit

Makes Claude Code behave like a UX/UI designer. Every new design or major change starts
with up to three high-fidelity options, and the user picks one before any production UI
code is written. All design work lives on one design board per project, organised into
standard sections.

This folder is a template. It is deliberately not in `.claude/`, so it does nothing in
this repo. Copy it into the repo where you do UI work.

## The design board

One board per project, published as one Artifact link that never changes. In Figma
projects it is one page called "Design board" with a Figma Section per part.

```
Design board
├── Index (sticky, links to every section)
├── Foundations: tokens, type, colour, spacing, radii, core components
└── Feature sections, newest first
    ├── 1. Brief
    ├── 2. Options A / B / C (desktop + mobile side by side)
    ├── 3. States (empty, loading, error, long content)
    ├── 4. Recommendation
    ├── 5. Decision ("Awaiting decision" until picked)
    └── 6. Built vs mockup (after implementation)
```

Decided and built sections collapse to a summary card so the board stays readable.

## Install into a project

```bash
cd /path/to/your-app
mkdir -p .claude/hooks design/board design/decisions
cp /path/to/claude-design-kit/hooks/*.sh .claude/hooks/
chmod +x .claude/hooks/*.sh
cat /path/to/claude-design-kit/CLAUDE.design.md >> CLAUDE.md
# Merge settings.hooks.json into .claude/settings.json (or copy it if you have none)
cp -n /path/to/claude-design-kit/settings.hooks.json .claude/settings.json
```

The hooks need `jq` and `git`.

## What each piece does

| Piece | When it runs | What it does |
|---|---|---|
| `CLAUDE.design.md` | Session start and after compaction | The design stance, the gate and the board structure |
| `design-lens.sh` | Every prompt that looks like UI work | Short reminder to classify the change and use the board |
| `design-gate.sh` | Before Claude creates a file | Blocks new UI files until a decision file in `design/decisions/` was written in the last 12 hours |
| `design-check-on-stop.sh` | When Claude finishes a turn | If UI files changed, reminds it to screenshot, add Built vs mockup, and critique |

## Tuning

- **Which files count as UI.** Edit `UI_PATTERN` in `design-gate.sh` to match your
  folder layout.
- **How long a decision unlocks building.** Edit `WINDOW_MIN` in `design-gate.sh`.
- **Too strict.** Remove the `PreToolUse` block from settings. The rule in CLAUDE.md
  still applies, it just is not enforced.

## Known limits

- The gate only catches new UI files. A major redesign done by editing existing files
  is governed by the CLAUDE.md rule, not the hook.
- The prompt keyword match in `design-lens.sh` is a heuristic and will sometimes fire
  on non-UI prompts. The reminder is short, so the cost is small.
- The Artifact link only stays stable while Claude republishes from the same board file
  path or to the link stored in `design/board/LINK`.
