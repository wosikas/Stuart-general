# How designers think

Part of [[Product Design Prompt Kit]].

## Work from the bottom plane up

Jesse James Garrett's five planes are how designers sequence decisions. Each plane constrains the one above it. Most weak AI output comes from asking for the top plane while the lower ones are still blank.

The planes run from concrete, what people see, down to abstract, why the product exists. Read the table from the bottom row up.

| Plane | What it covers | The question | Example prompt |
|---|---|---|---|
| **Surface** | Visual design | What does it look like? Colour, type, spacing, imagery, motion, polish. | "Apply our tokens to the wireframe. One primary action, clear type hierarchy, dark mode." |
| **Skeleton** | Interface and layout | Where does each element go on the screen, and in what priority? | "Wireframe these three screens at low fidelity, with annotations." |
| **Structure** | Flows and information architecture | How do screens connect? What are the steps, branches and navigation? | "Map the user flow from lock screen to saved note, including edge cases." |
| **Scope** | Features and requirements | What exactly are we building for v1, and what is out? | "List v1 requirements as user stories with acceptance criteria. Mark what is out of scope." |
| **Strategy** | User needs and business goals | Who is this for, what job do they need done, and how will we know it worked? | "Write a problem brief with the job-to-be-done and HEART success metrics." |

## The rule

Write one prompt per plane and feed each answer into the next. The strategy answer becomes context for the flow prompt. The flow becomes input for the wireframe prompt. This habit, more than any vocabulary, is what makes prompting sound like a designer.

Next: [[02 Artefacts by stage]]
