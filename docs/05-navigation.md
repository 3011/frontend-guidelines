# Navigation

## Orientation

Users should understand:

- where they are;
- which navigation item is active;
- what the parent context is;
- how to return;
- which context, organization, project, or entity they are operating on.

Do not use color as the only active-state signal.

## Sidebar behavior

When expanded labels are visible, avoid redundant tooltips.

Treat collapse and expansion as a complete transition:

1. transition begins;
2. width and content change;
3. layout stabilizes;
4. interactions specific to the final state become active.

Tooltip availability, label visibility, hit areas, and focus must switch at the correct phase. Bulk tooltip flashes, moving click targets, transient overlap, and inaccessible intermediate states are defects.

## Labels and grouping

Navigation labels should be short, familiar, stable, and unique enough to scan. Do not place detailed explanation, volatile status, implementation terms, or long counters inside the label.

Group navigation by user mental model, not source-code modules or backend services.

## Browser history and deep links

Back, forward, refresh, and direct links should preserve meaningful user context. Decide which states deserve a URL representation, including:

- selected tab or view;
- entity or detail context;
- search and filters;
- page and sort;
- an open detail panel when it represents a shareable destination.

Do not create history entries for every transient hover, tooltip, or local expansion. Do not trap the user in repeated modal history steps.

## Mobile navigation

Mobile navigation must open, operate, and close without losing context. After selecting a destination, close the navigation and move focus to a useful point on the new page.

Persistent navigation controls must not cover content or primary actions, including with safe-area insets and browser controls visible.
