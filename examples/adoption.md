# Adoption Example

This example shows the minimum information flow for a project using the guidelines.

## Project setup

The project vendors a released guideline version at `docs/frontend-guidelines/`, adds the project snippet to its root `AGENTS.md`, and completes `PROJECT_FRONTEND_PROFILE.md` with its framework, existing patterns, permissions, supported viewports, and test commands.

## Task

A searchable list loses input focus after every character and does not support IME composition reliably.

## Agent reading path

1. project instructions and profile;
2. guideline `AGENTS.md` and `CORE_RULES.md`;
3. the forms, data/filter, and implementation chapters selected through `docs/README.md`;
4. applicable rules `FG-FORM-002`, `FG-FORM-003`, `FG-FILTER-001`, `FG-QUALITY-002`, and `FG-QUALITY-006`;
5. the validation checklist before delivery.

## Plan summary

- User outcome: uninterrupted typing and correct results.
- Root cause: result updates remount the input because component identity is unstable.
- Fix layer: shared search-result state ownership, not a page-level refocus workaround.
- Sibling review: all screens using the shared search pattern.
- Validation: focus, caret, IME composition, rapid input, stale request ordering, empty results, errors, and narrow viewports.

## Delivery summary

The agent reports the shared fix, sibling surfaces reviewed, rule IDs applied, automated and browser evidence, and any unavailable checks. The report does not claim unverified behavior.
