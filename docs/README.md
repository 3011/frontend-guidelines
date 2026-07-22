# Detailed Guidance

[`FRONTEND_SPEC.md`](../FRONTEND_SPEC.md) is the normative source. These chapters explain rationale, common failures, and acceptance guidance without prescribing a framework or UI library.

## Select chapters by task

| Task | Read |
| --- | --- |
| page structure, spacing, hierarchy | `01`, `02` |
| forms, search, validation, focus, read-only state | `03`, `18` |
| modal, side panel, select, menu, tooltip | `04` |
| sidebar, navigation, URL or browser history | `05`, `17` |
| loading, empty, stale, error, notifications | `06` |
| tables, lists, selection, search, filters | `12` |
| buttons, icons, action hierarchy, destructive actions | `13` |
| narrow screens, keyboard, accessibility | `07` |
| labels, terminology, error and risk copy | `08` |
| latency, large collections, retry or offline behavior | `14` |
| permissions, sensitive data, untrusted content | `15` |
| locale, numbers, units, dates, timezones | `16` |
| implementation and delivery | `09`, `10` |
| justified guideline deviation | `11` |

For broad changes, read every affected chapter and the complete specification. For focused changes, read the matching specification sections and chapters rather than the repository mechanically from top to bottom.

## Chapters

| Chapter | Scope |
| --- | --- |
| [`01-principles.md`](01-principles.md) | product intent, consistency, root-cause reasoning |
| [`02-layout-and-hierarchy.md`](02-layout-and-hierarchy.md) | spacing, dividers, alignment, long content, density |
| [`03-forms-and-input.md`](03-forms-and-input.md) | labels, focus, IME, validation, drafts, read-only values |
| [`04-overlays-and-floating-ui.md`](04-overlays-and-floating-ui.md) | modals, side panels, selects, menus, tooltips, focus |
| [`05-navigation.md`](05-navigation.md) | sidebars, active state, mobile navigation, history |
| [`06-feedback-and-status.md`](06-feedback-and-status.md) | loading, stale, empty, error, progress, optimistic updates |
| [`07-responsive-and-accessibility.md`](07-responsive-and-accessibility.md) | narrow screens, keyboard, focus, motion, semantics |
| [`08-content-language.md`](08-content-language.md) | product copy, terminology, error messages, risk copy |
| [`09-implementation-workflow.md`](09-implementation-workflow.md) | analysis, fix-layer selection, implementation, delivery |
| [`10-validation-checklist.md`](10-validation-checklist.md) | pre-delivery state and behavior checks |
| [`11-exceptions.md`](11-exceptions.md) | documented deviations and review conditions |
| [`12-data-lists-and-filters.md`](12-data-lists-and-filters.md) | tables, lists, selection, search, filters, pagination |
| [`13-actions-and-controls.md`](13-actions-and-controls.md) | action hierarchy, hit areas, icons, destructive actions |
| [`14-performance-and-resilience.md`](14-performance-and-resilience.md) | responsiveness, large data, latency, retries, offline behavior |
| [`15-permissions-security-and-privacy.md`](15-permissions-security-and-privacy.md) | capability UI, authorization, secrets, untrusted data |
| [`16-localization-and-formatting.md`](16-localization-and-formatting.md) | text expansion, locales, numbers, units, dates, timezones |
| [`17-state-routing-and-persistence.md`](17-state-routing-and-persistence.md) | URL state, history, restoration, drafts, conflicts |
| [`18-editability-and-lifecycle.md`](18-editability-and-lifecycle.md) | editable, read-only, locked, completed, and archived states |

When explanatory wording conflicts with the specification, correct the inconsistency instead of silently selecting one interpretation.
