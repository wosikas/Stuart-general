# Vocabulary

Part of [[Product Design Prompt Kit]].

The terms designers use daily, what they mean, and how each sounds inside a prompt. The precise term tells the AI which body of practice to draw on.

## Strategy and research

- **Job to be done (JTBD)**: The progress a person is trying to make in a situation. Focuses on the goal, not the feature. *In a prompt:* "Frame this around the job: when I have a passing thought, I want to park it instantly so I can get back to what I was doing."
- **Problem statement**: One sentence naming the user, their need and why it matters, with no solution baked in. *In a prompt:* "Start from this problem statement and don't assume the answer is a new screen."
- **How might we (HMW)**: A question that reframes a problem as an opportunity, used to generate ideas. *In a prompt:* "Give me 10 "How might we" questions from these pain points."
- **Persona / proto-persona**: A representative user profile. "Proto" means based on assumptions, not research yet. *In a prompt:* "Design for the proto-persona "the interrupted thinker", not a generic user."
- **Mental model**: What users believe about how a system works. Good design matches it. *In a prompt:* "What mental model do users bring from Apple Notes, and where does our design break it?"
- **HEART metrics**: Google's framework: Happiness, Engagement, Adoption, Retention, Task success. *In a prompt:* "Define HEART metrics for this feature with one signal each."
- **MVP / v1 scope**: The smallest version that tests the core value. Everything else is explicitly deferred. *In a prompt:* "Cut this to the smallest lovable v1 and list what is deferred."
- **Assumption mapping**: Listing beliefs and ranking them by importance and evidence to decide what to test first. *In a prompt:* "Map the assumptions behind this design on importance versus evidence."

## Structure and flow

- **Information architecture (IA)**: How content is organised, labelled and connected so people can find things. *In a prompt:* "Propose the IA before any screens, with labels in users' words."
- **Sitemap**: A hierarchy of every page or screen. *In a prompt:* "Give me the sitemap as a nested list."
- **User flow**: The path a user takes through screens and decisions to finish a task. *In a prompt:* "Map the user flow including every error branch."
- **Happy path**: The ideal route with no errors or detours. Design it first, but never only it. *In a prompt:* "Show the happy path, then every unhappy path."
- **Edge case**: An unusual but real situation: empty data, huge data, no network, odd input. *In a prompt:* "List the edge cases for this screen and show how each is handled."
- **Empty state**: What a screen shows when there is no content yet. A chance to teach and invite action. *In a prompt:* "Design the empty state with a one-line explanation and a clear first action."
- **Progressive disclosure**: Showing only what is needed now and revealing advanced options on demand. *In a prompt:* "Use progressive disclosure: hide folder choice behind "More options"."
- **Onboarding / first-run experience**: How a new user learns the product on first open. *In a prompt:* "Design a first-run experience that reaches the first saved note in under 30 seconds."
- **Navigation model**: The overall pattern for moving around: tab bar, sidebar, stack, hub-and-spoke. *In a prompt:* "Which navigation model fits, and why not the alternatives?"
- **Entry point**: Where a user starts a flow: widget, notification, deep link, button. *In a prompt:* "List every entry point into capture and design for each."

## Layout and visual

- **Visual hierarchy**: The order in which the eye reads a screen, set by size, weight, colour and position. *In a prompt:* "Tighten the visual hierarchy so the note field dominates and metadata recedes."
- **Grid / 8-point system**: A layout grid plus a spacing scale in multiples of 8 (or 4) for consistent rhythm. *In a prompt:* "Align everything to an 8-point spacing scale: 4, 8, 16, 24, 32, 48."
- **Type scale**: A fixed set of font sizes with defined ratios, line heights and weights. *In a prompt:* "Use a type scale of no more than 5 sizes and name each step."
- **Whitespace**: Empty space that groups, separates and gives focus. *In a prompt:* "Increase whitespace around the input so it feels calm."
- **Density**: How much information fits in a space. Compact suits experts, comfortable suits casual use. *In a prompt:* "Offer comfortable and compact density for the list view."
- **Contrast**: Difference in brightness or colour between elements. Needed for legibility and emphasis. *In a prompt:* "Check every text colour for WCAG contrast in both themes."
- **Semantic colour roles**: Colours named by purpose (primary, surface, error) rather than by hue. *In a prompt:* "Define colours as semantic roles, not hex values scattered in components."
- **Gestalt principles**: How people group what they see: proximity, similarity, alignment, common region. *In a prompt:* "Use proximity to group title and date instead of adding a divider."
- **Elevation**: Perceived depth via shadow or tone, showing what sits above what. *In a prompt:* "Use elevation only for the sheet and toasts; keep the list flat."
- **Iconography**: A consistent icon set with matching stroke, size and metaphor. *In a prompt:* "Use one outline icon set at 24 px, and pair unfamiliar icons with a label."

## Design systems

- **Design system**: Shared tokens, components, patterns and guidelines that keep a product consistent. *In a prompt:* "Build this using our design system components only."
- **Design tokens**: Named values for colour, type, spacing, radius and motion that design and code share. *In a prompt:* "Output the design tokens as CSS custom properties and JSON."
- **Component**: A reusable UI piece, such as a button or card, with defined variants and states. *In a prompt:* "Treat the note row as a component with variants."
- **Variant**: A version of a component for a purpose or size: primary, secondary, destructive, small. *In a prompt:* "Give the button primary, secondary, ghost and destructive variants."
- **Component states**: Default, hover, focus, pressed, disabled, loading, selected, error. *In a prompt:* "Show every state of this input, including focus-visible and error."
- **Atomic design**: Brad Frost's model: atoms, molecules, organisms, templates, pages. *In a prompt:* "Break this screen down into atoms, molecules and organisms."
- **Pattern**: A reusable solution to a recurring problem: search, filters, inline edit. *In a prompt:* "Use the standard inline-edit pattern rather than a separate edit screen."

## Interaction

- **Affordance**: What an element's properties suggest you can do with it. A button looks pressable. *In a prompt:* "Make the swipe action discoverable. Right now it has no affordance."
- **Signifier**: A visible cue showing where and how to act, such as a grabber handle. *In a prompt:* "Add a signifier that the sheet can be dragged down."
- **Feedback**: The system's immediate response to an action, so users know it worked. *In a prompt:* "Give instant feedback on save with a subtle haptic and a toast."
- **Microinteraction**: A small, single-purpose moment: a toggle, a like, a pull-to-refresh. *In a prompt:* "Design the save microinteraction: trigger, rules, feedback, loops."
- **Optimistic UI**: Showing the result immediately and syncing in the background, rolling back on failure. *In a prompt:* "Use optimistic UI for saving; queue offline and show a sync badge."
- **Undo over confirm**: Letting people reverse an action instead of interrupting them with "Are you sure?" *In a prompt:* "Replace the delete confirmation dialog with a 5-second undo toast."
- **Modal, sheet, drawer, popover**: Overlays of different weight. A modal blocks, a sheet keeps context, a popover is lightweight. *In a prompt:* "Use a bottom sheet instead of a full-screen modal so context stays visible."
- **Toast / snackbar**: A brief non-blocking message, often with one action. *In a prompt:* "Confirm with a snackbar that includes an Undo action."
- **Skeleton screen**: A grey placeholder shaped like the content, shown while loading. *In a prompt:* "Use skeleton screens rather than a spinner for the notes list."
- **Motion and easing**: Animation duration and acceleration curves that make changes feel natural. *In a prompt:* "Keep transitions to 150–250 ms, ease-out on enter and ease-in on exit."
- **Inline validation**: Checking input next to the field as the user goes, not after submit. *In a prompt:* "Validate inline on blur and never clear the user's input on error."

## Mobile

- **Thumb zone**: The area of a phone screen reachable comfortably with one thumb, mostly the lower half. *In a prompt:* "Move primary actions into the thumb zone."
- **Touch target**: The tappable area of a control. Minimum 44×44 pt on iOS, 48×48 dp on Android. *In a prompt:* "Make every touch target at least 44 pt, even if the icon is smaller."
- **Safe area**: The screen region clear of notches, rounded corners and system bars. *In a prompt:* "Respect safe areas so nothing sits under the home indicator."
- **Tab bar / navigation bar**: Bottom navigation with 3 to 5 top-level destinations. *In a prompt:* "Use a tab bar with no more than 4 destinations."
- **Bottom sheet**: A panel sliding up from the bottom for a focused task or options. *In a prompt:* "Present capture as a resizable bottom sheet with a grabber."
- **Haptics**: Tactile feedback from the device for key moments. *In a prompt:* "Add a light haptic on successful save only."
- **Dynamic Type / font scaling**: The user's system text-size setting. Layouts must adapt to it. *In a prompt:* "Test the layout at the largest Dynamic Type size."
- **Deep link**: A link that opens a specific screen inside the app. *In a prompt:* "Support a deep link that opens capture directly from a widget."

## Accessibility

- **WCAG 2.2 AA**: The web accessibility standard most teams target. Level AA is the usual bar. *In a prompt:* "Audit this against WCAG 2.2 AA and cite success criteria."
- **Contrast ratio**: Normal text needs at least 4.5:1 against its background; large text and UI parts need 3:1. *In a prompt:* "Check all text for 4.5:1 contrast, including placeholder text."
- **Focus state**: A visible indicator showing which element has keyboard focus. *In a prompt:* "Design a clear focus-visible state for every interactive element."
- **Screen reader label**: Text a screen reader announces for an element, especially icon-only buttons. *In a prompt:* "Give every icon-only button an accessible label."
- **Colour-independent meaning**: Never use colour as the only way to convey information. *In a prompt:* "Pair the error colour with an icon and text, never colour alone."
- **Reduced motion**: A system setting asking apps to minimise animation. *In a prompt:* "Respect reduced motion by swapping slides for fades."

## Content

- **Microcopy**: The small words: labels, hints, errors, empty states. *In a prompt:* "Rewrite the microcopy to be shorter and verb-first."
- **Voice and tone**: Voice is the constant personality. Tone adapts to the moment. *In a prompt:* "Voice: calm and plain. Tone: warmer on empty states, direct on errors."
- **Content-first design**: Designing with real content before styling, to expose real lengths and priorities. *In a prompt:* "Use real note content, including a very long one, not lorem ipsum."

## Validation and handoff

- **Fidelity (lo, mid, hi)**: How finished a design looks. Low is fast to change, high is close to final. *In a prompt:* "Stay at low fidelity until the flow is agreed."
- **Prototype**: An interactive simulation used to test flows before building. *In a prompt:* "Build a clickable prototype of the capture flow I can tap through."
- **Heuristic evaluation**: An expert review against a set of principles, usually Nielsen's 10. *In a prompt:* "Run a heuristic evaluation and score severity 0 to 4."
- **Usability test**: Watching real users try realistic tasks to find where they struggle. *In a prompt:* "Write 5 task scenarios for a usability test, with no hints in the wording."
- **A/B test**: Shipping two variants to live users to compare a metric. *In a prompt:* "What would we A/B test here, and which metric decides it?"
- **Design critique**: Structured feedback against goals, not taste. *In a prompt:* "Critique this against the brief's goals, not aesthetics."
- **Handoff / redlines**: Specs for engineering: measurements, tokens, states, behaviour. *In a prompt:* "Produce handoff redlines with spacing expressed in tokens."

## Laws of UX

- **Fitts's law**: The time to hit a target depends on its size and distance. Big and close is fast. *In a prompt:* "Apply Fitts's law: make Save large and near the thumb."
- **Hick's law**: More choices mean slower decisions. *In a prompt:* "Apply Hick's law: reduce the capture options to one."
- **Jakob's law**: Users spend most of their time in other apps and expect yours to work the same way. *In a prompt:* "Follow Jakob's law and use patterns people know from Notes and Keep."
- **Tesler's law**: Complexity can't be removed, only moved. Decide whether the user or the system carries it. *In a prompt:* "Where can the system absorb complexity instead of the user?"
- **Doherty threshold**: Responses under about 400 ms keep people in flow. *In a prompt:* "Keep capture under the Doherty threshold with an optimistic save."
- **Peak-end rule**: People judge an experience by its peak and its end. *In a prompt:* "Design a satisfying end moment when a note is saved."
- **Von Restorff effect**: The item that differs is the one remembered, so reserve distinctiveness for what matters. *In a prompt:* "Make only the primary action visually distinct."
