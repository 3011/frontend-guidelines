# Overlays and Floating UI

## Choose the correct container

### Focused modal

Appropriate for:

- creation and editing;
- a configuration decision requiring focused attention;
- destructive or high-risk confirmation;
- a workflow that must be completed or cancelled before returning.

For long content, keep the title and primary actions reachable while the central content area scrolls. Avoid nested modal flows.

### Side panel

Appropriate for:

- auxiliary details;
- context for the current page;
- mobile navigation;
- inspection or preview that does not block the primary task.

Do not place equivalent creation or editing workflows in different containers merely because one implementation is convenient.

## Anchored popups

Selects, menus, comboboxes, date pickers, and similar popups should normally:

- open below the trigger when space allows;
- align the logical start edge with the trigger;
- preserve a small visible separation when overlap is not intentional;
- be at least wide enough for the trigger and meaningful option content;
- avoid partial overlap and exposed trigger borders;
- flip or shift near viewport boundaries;
- preserve option text when icons, checks, or shortcuts are present;
- avoid covering the element that users must compare with the choices.

Verify geometry after the opening transition settles and inspect the transition itself for visible jumps.

## Viewport, keyboard, and safe areas

Floating content must account for:

- browser viewport edges;
- mobile on-screen keyboards;
- safe-area insets;
- fixed headers, footers, and sidebars;
- zoomed text;
- nested scroll containers.

Long content should scroll within a bounded area rather than placing actions outside reach.

## Tooltips

Tooltips provide brief supplementary information. They do not carry instructions required to complete the task.

Requirements:

- open only from explicit stable hover or keyboard focus;
- avoid duplicating text already visible;
- suppress triggers during layout and collapse transitions;
- do not appear automatically on mount or restoration;
- do not open in bulk after one layout change;
- remain dismissible and non-blocking;
- provide another path for touch users when the information is necessary.

## Closing and focus

Opening should place focus at a logical starting point. Closing should return focus to the trigger or another clear continuation point.

Escape, close controls, outside interaction, browser navigation, and selection completion must match the task. Do not allow accidental outside dismissal when unsaved or high-risk work would be lost.

## Stacking and nested overlays

Avoid multiple modal layers. When nesting cannot be avoided, define:

- which layer owns focus;
- which background is inert;
- which Escape action closes which layer;
- which layer controls scroll;
- where focus returns after each close.

An overlay must never appear behind another blocking layer or become visually visible but unreachable.
