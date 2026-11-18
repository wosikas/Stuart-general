# Prompt building blocks

Part of [[Product Design Prompt Kit]].

Copy the lines you need into any prompt. On the web page these are assembled for you by the prompt builder.

## The skeleton

```
Act as a senior product designer.

CONTEXT
Product: [product, in one line]
In focus: [feature, screen or flow]
Users: [who they are, and their situation]
Job to be done: [what they need to get done, and what success looks like]
Platform: [one line from the Platform section below]

TASK: [ARTEFACT NAME]
[the task text from the template for that artefact]

Fidelity: [one line from the Fidelity section, for visual artefacts only]
Design system: [one line from the Design system section, for screens and components only]

CONSTRAINTS AND REFERENCES
[tech stack, brand adjectives, apps to learn from, things that must not change]

REQUIREMENTS
[lines from the Requirements section]

OUTPUT
[what you want back]

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

## Platform

**iOS app**

```
iOS app. Follow Apple Human Interface Guidelines: 44×44 pt minimum touch targets, tab bar and navigation stack, sheets for focused tasks, SF Pro with Dynamic Type, swipe-back gesture.
```

**Android app**

```
Android app. Follow Material 3: 48×48 dp minimum touch targets, navigation bar, top app bar, bottom sheets, a FAB where appropriate, Roboto, dynamic colour, system back.
```

**Cross-platform mobile**

```
Cross-platform mobile app (iOS and Android). Shared visual design, but native conventions for navigation, back behaviour and system controls on each platform.
```

**Responsive web**

```
Responsive web app. Mobile-first, breakpoints around 375, 768 and 1280 px. Must work with touch, mouse and keyboard.
```

**Desktop web**

```
Desktop web app. Denser layout, sidebar navigation, hover states, keyboard shortcuts and a command palette where useful.
```

## Fidelity

Wireframes are always low fidelity and mockups are always high. Choose a level only for prototypes, component specs, responsive layouts and motion specs.

**Low fidelity**

```
Low fidelity: greyscale boxes and real text, no styling. Focus on structure and priority.
```

**Mid fidelity**

```
Mid fidelity: real layout, spacing and type hierarchy, minimal colour.
```

**High fidelity**

```
High fidelity: final visual design with colour, type, spacing, icons and polish.
```

## Design system

**Propose one**

```
No design system yet. Propose a small token set (colour roles, type scale, 8-point spacing, radius) and use it consistently.
```

**Platform native**

```
Use the platform's native components and system styles wherever possible.
```

**Material 3**

```
Use Material 3 components and tokens.
```

**shadcn/ui + Tailwind**

```
Use shadcn/ui components with Tailwind CSS utility classes.
```

**Our own tokens**

```
Use our existing design tokens, pasted below: [paste tokens]. Do not invent new colours or sizes.
```

## Requirements

The first four apply to design artefacts such as flows, wireframes, mockups, prototypes and components. Leave them out of research artefacts such as briefs and interview guides.

**Every state**

```
Design every state: empty, loading, partial, error, success and offline.
```

**Edge cases**

```
Handle edge cases: first-time use, very long text, zero, one and many items, slow network, and permission denied.
```

**Accessibility (WCAG 2.2 AA)**

```
Meet WCAG 2.2 AA: text contrast of at least 4.5:1, visible focus, screen-reader labels, adequate target sizes and support for larger text.
```

**Dark mode**

```
Include dark mode using semantic colour tokens, not simply inverted colours.
```

**2 to 3 directions first**

```
Before detailing anything, give me 2 to 3 distinct directions with the trade-off of each, and recommend one.
```

**Rationale for decisions**

```
For each key decision, give a one-line rationale tied to the user's goal or a named UX principle.
```

**Clarifying questions first**

```
If anything critical is missing, ask me up to 3 clarifying questions before you start.
```
