# Frontend Guidelines

Framework-agnostic frontend engineering guidance for human developers and AI agents.

This repository defines **what user experience to produce, how to choose interaction patterns, and how to verify the result**. It intentionally contains no UI components, framework adapters, design tokens, or application code. The guidance applies to React, Vue, Svelte, native Web applications, and other frontend stacks.

## Purpose

This repository is an executable frontend contract covering:

- page structure, visual hierarchy, spacing, density, and alignment;
- forms, overlays, navigation, data views, filters, actions, and feedback;
- focus, keyboard, input method editors, responsive behavior, and accessibility;
- performance, resilience, permissions, privacy, localization, and route state;
- user-facing language and the boundary between product copy and developer notes;
- the workflow an AI agent must follow before, during, and after a frontend change;
- observable acceptance criteria and regression checks.

## Non-goals

This repository is **not**:

- a UI component library;
- a design token package;
- a framework starter;
- documentation for a specific UI library;
- a source of application components or copy-paste implementation code.

Requirements must not depend on component names, CSS utilities, framework APIs, or library-specific defaults.

## Start here

An AI agent must read these files in order:

1. [`AGENTS.md`](AGENTS.md) — execution contract and rule precedence;
2. [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md) — compact normative rules with stable IDs;
3. the relevant topic files under [`docs/`](docs/);
4. [`docs/10-validation-checklist.md`](docs/10-validation-checklist.md) before delivery.

The agent does not need to read every topic file for every task. `AGENTS.md` and `FRONTEND_SPEC.md` are always required; detailed chapters are selected by task scope.

## Adopt in another project

Pin this repository to an explicit version and place it where the agent can read it locally, for example:

```text
docs/frontend-guidelines/
```

Use a Git submodule, subtree, vendored copy, or another versioned mechanism. Do not rely only on a remote link because an execution environment may not have network access.

Then:

1. merge [`templates/PROJECT_AGENTS_SNIPPET.md`](templates/PROJECT_AGENTS_SNIPPET.md) into the project-level `AGENTS.md`;
2. complete [`templates/PROJECT_FRONTEND_PROFILE.md`](templates/PROJECT_FRONTEND_PROFILE.md);
3. optionally use [`templates/FRONTEND_TASK_PLAN.md`](templates/FRONTEND_TASK_PLAN.md) for non-trivial changes;
4. use [`templates/FRONTEND_CHANGE_REPORT.md`](templates/FRONTEND_CHANGE_REPORT.md) for delivery evidence.

Explicit product requirements and documented project constraints take precedence over this general specification. Any deviation must record its reason, impact, safeguards, validation, and review condition.

## Requirement language

The specification uses the following levels:

- **MUST** — required;
- **MUST NOT** — prohibited;
- **SHOULD** — required unless a documented reason justifies a deviation;
- **MAY** — optional.

Every normative rule has a stable identifier such as `FG-OVERLAY-002`. Agents should cite these IDs in plans, reviews, tests, and delivery reports.

## Repository structure

```text
AGENTS.md                   AI execution contract and precedence
FRONTEND_SPEC.md            compact normative rule catalog
docs/                       rationale, scope, and acceptance guidance
examples/                   framework-agnostic good/bad examples
templates/                  project adoption and delivery templates
scripts/validate.py         repository, language, rule, and link validation
```

## Versioning

The current version is in [`VERSION`](VERSION). Semantic versioning is used:

- **PATCH** — clarification that does not change required behavior;
- **MINOR** — compatible new rules, chapters, or validation guidance;
- **MAJOR** — removal of a published rule or a meaningfully incompatible requirement change.

Published rule IDs are never reused for a different meaning.

## License

[MIT](LICENSE)
