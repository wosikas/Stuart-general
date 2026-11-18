# Prompt templates

Part of [[Product Design Prompt Kit]].

20 prompts, one per standard artefact. Replace the bracketed parts. Run them roughly in stage order, pasting each answer into the next prompt as context.

## Discover

### Problem brief

What problem, for whom, and how will we know it worked? Ask for it when: before any screens exist.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Write a one-page product design brief for [feature]. Include: the problem statement in the user's own words, target users and their context of use, the core job-to-be-done, how people cope today, the assumptions we are making ranked by risk, success metrics using the HEART framework (happiness, engagement, adoption, retention, task success), v1 scope, what is explicitly out of scope, and open questions.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A structured document with a heading per part. Call out the single riskiest assumption. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Proto-personas and job stories

Who exactly are we designing for, and in what situation? Ask for it when: you have a rough audience but no research yet.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Draft 2 to 3 proto-personas for [product], clearly labelled as assumptions to validate. For each: goals, frustrations, context of use (device, place, time pressure, one hand or two), tech comfort, and one job story written as "When <situation>, I want to <motivation>, so I can <outcome>." Then list which assumptions a user interview should test first.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: One short card per persona, then a ranked list of assumptions to test. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Interview guide

What should we ask real users so we learn rather than confirm? Ask for it when: before building, to test the brief.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Write a 30-minute user interview guide to learn how [users] currently [do the job]. Open with a warm-up, then past-behaviour questions ("Tell me about the last time you..."). Avoid leading, yes/no and hypothetical "would you use" questions. Add follow-up probes for each question and a wrap-up. Include a 5-question screener to recruit the right participants.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: The screener, then the guide with timings per section. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Competitive UX audit

What patterns do users already expect, and where is the gap? Ask for it when: early, to avoid reinventing solved patterns.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Do a competitive UX audit of how [competitor apps] handle [job]. For each: entry point, number of taps on the happy path, UI patterns used, what they do well, and where users get stuck. Finish with the patterns that are now table stakes (Jakob's law: users expect your app to work like the ones they already use) and one gap we could own.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A comparison table, then table stakes, then the opportunity. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

## Define

### Journey map

Where in the whole experience does it hurt most? Ask for it when: you need to choose which moment to design for.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Create a current-state journey map for [persona] doing [job]. Stages across the top. For each stage list: actions, touchpoints, thoughts, emotional state (low, neutral, high), pain points and opportunities. Highlight the moment of highest friction and explain why.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A table with stages as columns, followed by the top three opportunities. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Requirements and user stories

What exactly is in v1, and how will we know each piece is done? Ask for it when: the problem is agreed and you are scoping.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Turn the brief for [feature] into v1 requirements. Write user stories as "As a <user>, I want <action>, so that <outcome>", each with acceptance criteria in Given/When/Then form. Prioritise with MoSCoW (must, should, could, won't) and list what is deliberately out of scope.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A prioritised table of stories with acceptance criteria. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Information architecture

How is everything organised and named, and how do people move around? Ask for it when: before designing navigation or adding a new area.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Propose the information architecture for [product]: a sitemap as a nested list, the primary navigation model and why (tab bar, sidebar, hub-and-spoke, etc.), what lives in global versus local navigation, section names in users' language rather than internal jargon, and where search fits. Give one alternative structure and the trade-off. Suggest a card-sorting study to validate the naming.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: Nested sitemap, navigation rationale, the alternative, and a validation plan. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### User flow

What are all the steps and branches to get the job done? Ask for it when: before wireframes. Flows come before screens.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Map the user flow for [task] from entry point to success. Show every screen and decision as a step. Do the happy path first, then branches for: first-time user, no network, validation errors, permission denied, empty data, interrupted mid-task, and undo. Count the taps on the happy path and suggest how to remove at least one.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A numbered step list, then a Mermaid flowchart of the whole flow. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

## Develop

### Wireframes

What goes on each screen, in what priority? Ask for it when: the flow is agreed and you want layouts that are cheap to change.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Produce low-fidelity wireframes for [screens]. Follow the agreed user flow if I have pasted one. Greyscale only, real content rather than lorem ipsum, and focus on layout, hierarchy and content priority. Annotate each screen with: the primary action, why key elements sit where they do, and what is hidden behind progressive disclosure.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: Simple HTML wireframes I can open in a browser, with numbered annotations beside each screen. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### High-fidelity mockup

What does the finished screen look and feel like? Ask for it when: wireframes are approved.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Design the high-fidelity UI for [screen]. Establish clear visual hierarchy with exactly one primary action. Use an 8-point spacing scale, a defined type scale, and colour roles (primary, surface, on-surface, and semantic success, warning, error). Show these states side by side: default, empty, loading (skeleton), error and success.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: Working HTML and CSS (or React with Tailwind) I can open in a browser, with the design tokens defined at the top. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Clickable prototype

Does the flow feel right when you actually tap through it? Ask for it when: before usability testing or showing stakeholders.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Build a clickable prototype of [flow] that I can tap through on a phone or in a browser. Link every screen in the flow, include realistic content, simulate loading and one error, and make transitions match the platform. Keep it throwaway: no backend.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A single HTML file with all screens and working navigation between them. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Design system and tokens

What are the reusable rules so every screen stays consistent? Ask for it when: you have two or more screens, or before building many.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Define a starter design system for [product]. Design tokens for: colour (a primitive palette plus semantic roles, in light and dark), typography (type scale with size, line height and weight per step), spacing (4- or 8-point scale), corner radius, elevation, and motion (durations and easing). Then a core component list: button, text input, select, checkbox, switch, card, list row, tabs, modal or sheet, toast, empty state. Brand personality: [three adjectives].

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: Tokens as JSON and as CSS custom properties, then a table of components with their variants. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Component spec

Exactly how does one component look and behave in every case? Ask for it when: handing a component to engineering, or standardising it.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Write a full spec for [component]. Include: anatomy (named parts), variants (for example primary, secondary, tertiary, destructive, and sizes), every state (default, hover, focus-visible, pressed, disabled, loading, selected, error), behaviour rules, content guidelines (label length, truncation), accessibility (role, keyboard interaction, screen-reader label, minimum target size) and do/don't examples.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A spec document plus a rendered HTML preview of every variant and state. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Interaction and motion spec

What happens when the user acts, and how does it feel? Ask for it when: screens exist but feel static or unclear.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Specify the interactions for [feature]. For each interaction: the trigger, the immediate feedback (within 100 ms), the transition with duration and easing, and what happens on failure. Use optimistic UI where it is safe. Prefer undo over confirmation dialogs for reversible actions. Respect the reduced-motion setting.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A table of interactions, then a short prototype of the key one. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### UX writing and microcopy

What exactly do the words say? Ask for it when: any time. Words are half the interface.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Write the microcopy for [flow]: screen titles, button labels (verb first, say what will happen), empty states (what this is, why it is empty, what to do next), error messages (what happened and how to fix it, no blame, no jargon), confirmations, tooltips and onboarding hints. Voice: [voice]. Give two options for each key string with character counts.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A table of strings grouped by screen. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

## Deliver

### Heuristic review

What is wrong with this design, and how bad is it? Ask for it when: after every significant AI output, or on your current app.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Run a heuristic evaluation of [screen], which I have attached or pasted below, against Nielsen's 10 usability heuristics. For each issue: the heuristic violated, where it occurs, severity from 0 (not a problem) to 4 (usability catastrophe), and a concrete fix. Then list the three changes that would most improve the experience.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: An issues table sorted by severity, then the top three fixes. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Accessibility audit

Can everyone use it, including with a screen reader or keyboard? Ask for it when: before hand-off and before launch.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Audit [screen], which I have attached or pasted below, against WCAG 2.2 level AA. Check: text contrast (4.5:1 for normal text, 3:1 for large text and UI parts), focus order and visible focus, keyboard-only operation, screen-reader names and roles, target size, meaning conveyed by colour alone, text enlarged to 200% or Dynamic Type, and reduced motion.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: Issues with the WCAG success criterion number, severity and the fix. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Responsive and platform adaptation

How does this work on every screen size and platform? Ask for it when: a design exists for one size only.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Adapt [screen] across breakpoints: mobile (about 375 px), tablet (about 768 px) and desktop (1280 px and up). Describe what reflows, what collapses into menus or sheets, what becomes hover versus tap, and how navigation changes (for example a bottom tab bar on mobile and a sidebar on desktop). On native, follow Apple HIG and Material 3 conventions respectively.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: The screen rendered at each breakpoint, with a list of changes between them. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Usability test plan

Does it actually work for real people? Ask for it when: you have a clickable prototype.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Write a moderated usability test plan for a prototype of [feature]. Include: goals, criteria for 5 participants, 4 to 6 realistic task scenarios worded without hints, what to observe, a success criterion per task, post-task questions including the Single Ease Question, and how to synthesise findings afterwards.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A test script I can read aloud, plus a note-taking grid. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```

### Developer handoff spec

Can engineering build it without guessing? Ask for it when: the design is final.

```
Act as a senior product designer.

Context: [product, in one line]. Users: [who they are and their situation]. Platform: [iOS / Android / responsive web / desktop web].

Task: Prepare a developer handoff spec for [screen]: layout and spacing in tokens, component names mapped to our library, all states and edge cases, responsive behaviour, interaction and animation values, final copy strings, accessibility notes, analytics events to fire, and open questions for engineering.

Constraints: [design system or tokens, brand adjectives, tech stack, reference apps, anything that must not change].

Output: A spec document organised by screen region, with an open-questions list at the end. Give a one-line rationale for each key decision.

If anything critical is missing, ask me up to 3 clarifying questions before you start.
```
