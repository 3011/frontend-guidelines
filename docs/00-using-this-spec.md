# Using This Specification

## Minimum reading set

Every frontend task requires:

- the target project's own instructions and profile;
- root [`../AGENTS.md`](../AGENTS.md);
- root [`../FRONTEND_SPEC.md`](../FRONTEND_SPEC.md);
- detailed chapters relevant to the task;
- [`10-validation-checklist.md`](10-validation-checklist.md) before delivery.

Do not read the repository mechanically from top to bottom when the task is narrow. Select the relevant chapters, but never skip the compact specification.

## Select chapters by task

| Task | Required chapters |
| --- | --- |
| page restructuring, spacing, hierarchy | `01-principles.md`, `02-layout-and-hierarchy.md` |
| forms, search, validation, input focus | `03-forms-and-input.md`, `18-editability-and-lifecycle.md` |
| modal, side panel, select, menu, tooltip | `04-overlays-and-floating-ui.md` |
| sidebar, navigation, route state | `05-navigation.md`, `17-state-routing-and-persistence.md` |
| loading, empty, stale, error, notifications | `06-feedback-and-status.md` |
| table, list, selection, search, filters | `12-data-lists-and-filters.md` |
| buttons, icon actions, action hierarchy | `13-actions-and-controls.md` |
| narrow screens, keyboard, accessibility | `07-responsive-and-accessibility.md` |
| user copy, labels, terminology | `08-content-language.md` |
| latency, large collections, retries | `14-performance-and-resilience.md` |
| permissions, sensitive data, untrusted content | `15-permissions-security-and-privacy.md` |
| localization, numbers, dates, timezones | `16-localization-and-formatting.md` |
| implementation and delivery | `09-implementation-workflow.md`, `10-validation-checklist.md` |

## Project profile

Each project should maintain `PROJECT_FRONTEND_PROFILE.md` using the provided template. It records:

- product type and primary users;
- framework and existing UI system;
- routing, state ownership, and test environment;
- established patterns;
- browser, locale, device, accessibility, security, and performance constraints;
- explicit deviations from this specification.

The shared specification must not overwrite a documented and reasonable product requirement. It does require the agent to distinguish an intentional project decision from an accidental inconsistency.

## Cite rule IDs

Plans, reviews, tests, and delivery reports should cite stable rule IDs:

```text
Root cause: the filtered list remounts the active search input, violating
FG-FORM-002 and FG-FILTER-001.

Fix layer: shared search-result state ownership.

Evidence: focus, caret position, IME composition, and out-of-order requests
were verified in the browser.
```

Citing a rule does not prove compliance. Include observable evidence.

## Apply requirement levels

- A **MUST** or **MUST NOT** requirement is mandatory unless a documented higher-priority constraint applies.
- A **SHOULD** requirement is the default. A deviation requires an explicit reason.
- A **MAY** statement offers an option and does not establish a default.

Marking a check “not applicable” requires explaining why the state cannot occur. It is not a substitute for an unavailable test.
