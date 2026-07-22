# Frontend Guidelines

Framework-agnostic frontend engineering rules for human developers and AI coding agents.

The repository defines user-facing behavior, interaction decisions, and validation expectations. It contains documentation and evaluation material rather than UI components or framework-specific implementation code.

## For AI agents

Read in this order:

1. [`AGENTS.md`](AGENTS.md) for the execution workflow and precedence rules;
2. [`CORE_RULES.md`](CORE_RULES.md) for the cross-task baseline;
3. the task map in [`docs/README.md`](docs/README.md);
4. the applicable rules in [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md) and relevant detailed chapters;
5. [`docs/10-validation-checklist.md`](docs/10-validation-checklist.md) before delivery.

The full specification contains stable IDs such as `FG-OVERLAY-002`. Cite applicable IDs in plans, reviews, tests, and delivery reports, together with observable evidence.

## Adopt in a project

Pin a released version and place it where the agent can read it locally, for example:

```text
docs/frontend-guidelines/
```

A submodule, subtree, or vendored copy is preferable to a remote-only link. Then:

1. merge [`templates/PROJECT_AGENTS_SNIPPET.md`](templates/PROJECT_AGENTS_SNIPPET.md) into the project-level `AGENTS.md`;
2. complete [`templates/PROJECT_FRONTEND_PROFILE.md`](templates/PROJECT_FRONTEND_PROFILE.md);
3. use the task-plan and change-report templates for material changes.

See [`examples/adoption.md`](examples/adoption.md) for a compact end-to-end example.

## Repository map

- [`AGENTS.md`](AGENTS.md): AI execution contract
- [`CORE_RULES.md`](CORE_RULES.md): minimum cross-task baseline
- [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md): complete normative rule catalog
- [`docs/`](docs/): rationale, failure modes, and acceptance guidance
- [`templates/`](templates/): project profile, task plan, and delivery report
- [`examples/`](examples/): framework-neutral examples and adoption flow
- [`evals/`](evals/): cases for evaluating agent decisions

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Rule proposals should describe a real user problem, the specification gap, observable acceptance criteria, and compatibility impact.

Run repository validation before submitting:

```sh
python3 scripts/validate.py
```

## License

[MIT](LICENSE)
