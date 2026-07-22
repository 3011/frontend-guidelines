# Frontend Agent Instructions

Use this repository as a frontend engineering contract. Produce observable user outcomes; do not copy a framework-specific implementation from these documents.

## Reading workflow

Before changing a frontend:

1. read the target project's instructions and `PROJECT_FRONTEND_PROFILE.md`;
2. read this file and [`CORE_RULES.md`](CORE_RULES.md);
3. use [`docs/README.md`](docs/README.md) to select the relevant chapters;
4. read the applicable sections of [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md);
5. complete [`docs/10-validation-checklist.md`](docs/10-validation-checklist.md) before delivery.

Read the full specification for broad redesigns, new shared patterns, or changes that span several rule areas. A focused task may read only the applicable specification sections and chapters.

## Rule precedence

Resolve conflicts in this order:

1. law and non-waivable security, privacy, and accessibility requirements;
2. the current user's explicit requirements;
3. the target project's documented constraints and instructions;
4. established project behavior that is consistent and reasonable;
5. these shared guidelines;
6. framework, browser, or UI-library defaults.

A library default is not evidence that an observable defect is acceptable.

## Before implementation

- Identify the framework, UI system, routing, state ownership, data flow, and test strategy.
- Locate existing implementations of the same or a similar pattern.
- Separate the visible symptom from the root cause.
- Choose the correct fix layer: data/state, shared pattern, page composition, or isolated instance.
- Review sibling screens that may share the cause or depend on the current behavior.
- Define the relevant state matrix, viewports, input methods, permissions, data conditions, and failure paths.

Do not infer the full implementation from a screenshot, add another UI framework for a local issue, hide shared defects with one-off offsets, or claim success without evidence.

## During implementation

- Fix the smallest correct responsibility boundary.
- Reuse sound project patterns before creating a near-duplicate abstraction.
- Treat transitions, loading, stale, empty, error, disabled, long-content, and narrow-screen conditions as product states.
- Preserve focus, user input, browser navigation, and meaningful route state.
- Keep user-facing content limited to what helps users understand or complete their task.
- Keep backend authorization and validation authoritative.

## Plan and delivery

For a material change, state the user-visible problem, root cause, fix layer, affected sibling surfaces, applicable rule IDs, and validation plan. Use [`templates/FRONTEND_TASK_PLAN.md`](templates/FRONTEND_TASK_PLAN.md) when useful.

After implementation, report:

- what changed and where;
- the rule IDs applied;
- automated and browser checks performed;
- states, viewports, and input methods exercised;
- anything not verified and the resulting risk;
- remaining risks and rollback considerations.

Use [`templates/FRONTEND_CHANGE_REPORT.md`](templates/FRONTEND_CHANGE_REPORT.md) or an equivalent concise format.

## Deviations

A deviation from a `MUST` or `SHOULD` rule requires a higher-priority constraint and a record containing the rule ID, scope, reason, user impact, safeguards, validation, and review condition. Silent deviations are prohibited.

This repository must remain documentation-only and framework-neutral. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for repository boundaries.
