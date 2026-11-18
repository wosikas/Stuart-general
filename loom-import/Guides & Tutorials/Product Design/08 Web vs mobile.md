# Web vs mobile

Part of [[Product Design Prompt Kit]].

Name the platform in every prompt. The conventions differ enough that a design for one feels wrong on another.

| Concern | iOS (Apple HIG) | Android (Material 3) | Web |
|---|---|---|---|
| **Primary navigation** | Tab bar at the bottom; navigation stack with a back chevron top-left | Navigation bar at the bottom (rail on tablets); top app bar | Top bar or sidebar; URLs and the browser back button matter |
| **Minimum target** | 44 × 44 pt | 48 × 48 dp | 24 × 24 CSS px minimum under WCAG 2.2; 44 px is comfortable for touch |
| **Going back** | Swipe from the left edge, or the back button in the nav bar | System back gesture or button | Browser back; every meaningful state should have a URL |
| **Base text size** | 17 pt body, scales with Dynamic Type | 14–16 sp body, scales with the font size setting | 16 px minimum body, scales with browser zoom |
| **Overlays** | Sheets (resizable), action sheets, alerts | Bottom sheets, dialogs, snackbars | Modals, drawers, popovers, toasts |
| **Primary action** | Top-right nav button or bottom button | Floating action button (FAB) or bottom button | Prominent button, plus a keyboard shortcut for frequent actions |
| **Input** | Touch, gestures, haptics | Touch, gestures, haptics | Mouse, keyboard and touch; hover exists but can't be relied on |
| **System font** | SF Pro | Roboto | Your choice; always define a fallback stack |
| **Guideline source** | Apple Human Interface Guidelines | Material Design 3 | WCAG 2.2, plus your design system |

Figures follow Apple HIG, Material 3 and WCAG 2.2 as published. Check the live guidelines before shipping.
