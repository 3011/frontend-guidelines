# Detailed Guidance

The compact normative requirements live in [`../FRONTEND_SPEC.md`](../FRONTEND_SPEC.md). These chapters provide rationale, scope, failure modes, and acceptance guidance without prescribing a framework or UI library.

## Reading map

| Chapter | Use it for |
| --- | --- |
| [`00-using-this-spec.md`](00-using-this-spec.md) | selecting the minimum reading set and citing rules |
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
| [`15-permissions-security-and-privacy.md`](15-permissions-security-and-privacy.md) | capability UI, authorization boundaries, secrets, untrusted data |
| [`16-localization-and-formatting.md`](16-localization-and-formatting.md) | text expansion, locales, numbers, units, dates, timezones |
| [`17-state-routing-and-persistence.md`](17-state-routing-and-persistence.md) | URL state, browser history, restoration, drafts, conflicts |
| [`18-editability-and-lifecycle.md`](18-editability-and-lifecycle.md) | editable vs read-only presentation, locked and lifecycle states |

Requirements in `FRONTEND_SPEC.md` take precedence over explanatory wording in these chapters. When wording appears inconsistent, clarify or correct the specification rather than silently choosing one interpretation.
