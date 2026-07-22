# Frontend Agent Instructions

This repository defines a shared frontend engineering contract for any project that adopts it. It specifies user outcomes and validation expectations; it does not provide UI library code.

## 1. Required reading order

Before any frontend task:

1. read the target project's `AGENTS.md`, README, and frontend conventions;
2. read this file;
3. read [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md);
4. read the topic chapters relevant to the task;
5. complete [`docs/10-validation-checklist.md`](docs/10-validation-checklist.md) before delivery.

For non-trivial work, fill in [`templates/FRONTEND_TASK_PLAN.md`](templates/FRONTEND_TASK_PLAN.md) or provide equivalent information in the task plan.

## 2. Rule precedence

Resolve conflicts in this order:

1. law, security, privacy, and non-waivable accessibility requirements;
2. explicit requirements in the current user request;
3. the target project's `AGENTS.md` and `PROJECT_FRONTEND_PROFILE.md`;
4. established project behavior that is both consistent and reasonable;
5. this repository;
6. framework, browser, or UI library defaults.

A library default is never sufficient justification for retaining an observable usability defect.

## 3. Required pre-change analysis

The agent MUST:

- identify the framework, UI system, routing, state ownership, data flow, and test strategy;
- locate existing implementations of the same or a similar pattern;
- distinguish the observable symptom from the root cause;
- determine whether the correct fix belongs to data/state, a shared pattern, page composition, or one isolated instance;
- search for sibling screens that may share the same defect or depend on the current behavior;
- identify effects on desktop, narrow screens, keyboard use, focus, IME composition, reduced motion, themes, permissions, localization, and stale or failed data;
- identify which user-visible states require validation.

The agent MUST NOT:

- infer implementation solely from a screenshot;
- introduce another UI framework for a local visual change;
- use one-off offsets to hide a shared positioning or spacing defect;
- rewrite an interaction model before understanding existing project conventions;
- restyle unrelated areas without explicit scope;
- treat hidden controls as authorization enforcement;
- claim a behavior works without evidence.

## 4. Implementation principles

- Fix the smallest correct responsibility boundary, not merely the fewest lines.
- Reuse established project capabilities before creating a near-duplicate abstraction.
- Express behavior independently from a specific UI library.
- Treat animation and transition states as real product states.
- Treat loading, empty, error, stale, disabled, permission-denied, long-content, and narrow-screen conditions as normal states.
- Preserve browser navigation, focus, user-entered data, and meaningful route state.
- Keep user interfaces limited to information users need to understand or complete their task.
- Keep backend authorization and validation authoritative even when the UI reflects capabilities.

## 5. Required plan and delivery output

Before a material implementation, the agent SHOULD state:

- the user-visible symptom and root cause;
- the chosen fix layer;
- affected sibling surfaces;
- applicable rule IDs;
- the validation plan and known constraints.

After implementation, the agent MUST report:

- what changed and where;
- which rule IDs were applied;
- which automated and browser checks ran;
- evidence for the relevant states and viewports;
- what was not verified and why;
- remaining risks and rollback considerations.

Use [`templates/FRONTEND_CHANGE_REPORT.md`](templates/FRONTEND_CHANGE_REPORT.md) or an equivalent concise format.

## 6. Deviations

A MUST or SHOULD rule may be deviated from only when a product, legal, platform, accessibility, or documented project constraint requires it. The deviation MUST record:

- rule ID;
- scope;
- reason;
- user impact;
- compensating safeguards;
- validation method;
- review trigger or expiry condition.

Silent deviations are prohibited. “The library behaves this way,” “this is faster,” and “this screen is special” are not sufficient reasons by themselves.

## 7. Repository boundary

This repository MUST NOT contain:

- `.tsx`, `.jsx`, `.vue`, `.svelte`, `.css`, or equivalent UI implementation files;
- UI component source code;
- wrappers around a particular component library;
- copy-paste framework implementations;
- project-specific business components;
- screenshots that expose credentials, private customer data, or internal-only environments.

Framework-neutral diagrams, state tables, pseudocode, acceptance criteria, and good/bad comparisons are allowed.
