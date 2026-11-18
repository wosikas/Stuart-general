# Anatomy of a prompt

Part of [[Product Design Prompt Kit]].

The difference isn't fancy words. Every decision the AI would otherwise guess has already been made.

## How most people ask

```
Design a quick capture screen for my notes app. Make it modern and clean.
```

The AI must guess the user, the platform, the entry point, what "done" means, which states matter and what to hand back. It guesses the average, which is why the result looks generic.

## How a product designer asks

| Part | Example |
|---|---|
| **Role** | Act as a senior product designer. |
| **Context** | Loom is a personal notes app. We are adding Quick Capture. |
| **User** | People who jot ideas all day, often one-handed and mid-task, who hate deciding where a note belongs. |
| **Job & success** | Capture a thought in under 5 seconds with no filing decision. Success: daily use, fewer lost ideas. |
| **Platform** | iOS app. Follow Apple HIG: bottom sheet, 44pt targets, Dynamic Type. |
| **Artefact** | Mid-fidelity screens for the capture sheet, reached from a home-screen widget and an in-app button. |
| **States & edges** | Show empty, typing, saving, saved (with undo), offline-queued, and a very long note. |
| **Constraints** | Calm, quiet brand. Works offline. Learn from Apple Notes lock-screen capture. |
| **Output** | HTML I can open, one frame per state, with a one-line rationale per key decision. |
| **Process** | Ask up to 3 clarifying questions first if anything critical is missing. |

## The same prompt, ready to copy

```
Act as a senior product designer.
Loom is a personal notes app. We are adding Quick Capture.
People who jot ideas all day, often one-handed and mid-task, who hate deciding where a note belongs.
Capture a thought in under 5 seconds with no filing decision. Success: daily use, fewer lost ideas.
iOS app. Follow Apple HIG: bottom sheet, 44pt targets, Dynamic Type.
Mid-fidelity screens for the capture sheet, reached from a home-screen widget and an in-app button.
Show empty, typing, saving, saved (with undo), offline-queued, and a very long note.
Calm, quiet brand. Works offline. Learn from Apple Notes lock-screen capture.
HTML I can open, one frame per state, with a one-line rationale per key decision.
Ask up to 3 clarifying questions first if anything critical is missing.
```

To assemble your own, see [[04 Prompt building blocks]] and [[05 Prompt templates]].
