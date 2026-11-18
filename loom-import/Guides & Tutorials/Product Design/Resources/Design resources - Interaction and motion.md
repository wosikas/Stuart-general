# Design resources - Interaction and motion

Part of [[11 Resource library]] in the [[Product Design Prompt Kit]].

How an interface responds, moves and waits.

15 links. A star marks an essential. Last link check: 18 November 2026.

- **[Designing Fluid Interfaces](https://developer.apple.com/videos/play/wwdc2018/803/)** ★ (Apple · WWDC 2018; video; free). The talk that explains why iOS gestures feel right: interruptible, direct and responsive from the first frame. *In a prompt:* "Make the sheet interruptible and redirectable mid-gesture."
- **[Invisible Details of Interaction Design](https://rauno.me/craft/interaction-design)** (Rauno Freiberg; article; free). A close reading of small interaction decisions in iOS and elsewhere, and why each one is right. *In a prompt:* "Explain the interaction details that would make this gesture feel natural."
- **[7 Practical Animation Tips](https://emilkowal.ski/ui/7-practical-animation-tips)** (Emil Kowalski; article; free). Short, concrete rules: scale buttons on press, don't animate from zero, keep it under 300 ms. *In a prompt:* "Apply these animation rules: ease-out, under 300 ms, and scale from 0.95 not 0."
- **[Material 3: Motion](https://m3.material.io/styles/motion/overview/how-it-works)** (Google; guideline; free). Easing and duration tokens, and the transition patterns that explain where things come from and go to. *In a prompt:* "Use Material's standard easing and duration tokens for every transition."
- **[Apple HIG: Motion](https://developer.apple.com/design/human-interface-guidelines/motion)** (Apple; guideline; free). When to animate, when not to, and how to honour Reduce Motion. *In a prompt:* "Add purposeful motion only, and give a Reduce Motion alternative for each."
- **[Easings](https://easings.net/)** (Andrey Sitnik & Ivan Solovev; reference; free). A visual cheat sheet of easing curves with the code for each. *In a prompt:* "Use easeOutCubic for entrances and easeInCubic for exits."
- **[Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/)** (Jakob Nielsen · NN/g; article; free). The 0.1 second, 1 second and 10 second thresholds that decide what feedback each wait needs. *In a prompt:* "Specify the feedback for waits under 0.1 s, under 1 s and over 1 s."
- **[Skeleton Screens 101](https://www.nngroup.com/articles/skeleton-screens/)** (NN/g; article; free). When a skeleton helps, when a spinner or progress bar is better, and how to design each. *In a prompt:* "Use a skeleton for the list load and a progress bar for the export."
- **[Bottom Sheets: Definition and UX Guidelines](https://www.nngroup.com/articles/bottom-sheet/)** (NN/g; article; free). Modal versus non-modal sheets, and the usability problems to avoid. Directly relevant to the Quick Capture example. *In a prompt:* "Follow NN/g bottom sheet guidelines: clear dismissal and no stacked sheets."
- **[Confirmation Dialogs Can Prevent User Errors (If Not Overused)](https://www.nngroup.com/articles/confirmation-dialog/)** (NN/g; article; free). When to confirm, when to offer undo, and how to word the dialog. *In a prompt:* "Use undo for reversible actions; confirm only what can't be reversed."
- **[Microinteractions in User Experience](https://www.nngroup.com/articles/microinteractions/)** (NN/g; article; free). A short explanation of Dan Saffer's model: every microinteraction has a trigger, rules, feedback, and loops and modes. *In a prompt:* "Specify this microinteraction as trigger, rules, feedback, and loops and modes."
- **[Motion](https://motion.dev/)** (Motion; tool; free tier). The animation library AI builders most often use for React and plain JavaScript. *In a prompt:* "Implement transitions with Motion using spring physics, not fixed durations."
- **[LottieFiles](https://lottiefiles.com/)** (LottieFiles; tool; free tier). A library of lightweight vector animations for empty states, success moments and loaders. *In a prompt:* "Add one small Lottie animation to the success state, nowhere else."
- **[Great Animations](https://emilkowal.ski/ui/great-animations)** (Emil Kowalski; article; free). What makes interface animation feel right: natural easing, speed, purpose and interruptibility. *In a prompt:* "Animate only what has a purpose, keep it fast, and make it interruptible."
- **[Rauno: Craft](https://rauno.me/craft)** (Rauno Freiberg; blog; free). Interactive essays and prototypes exploring interaction details at a very high level. *In a prompt:* "What small interaction detail would make this feel considered?"
