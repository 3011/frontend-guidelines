# Contributing

Contributions may add or improve framework-agnostic frontend rules, rationale, examples, templates, evaluations, and documentation validation.

By participating, follow the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Report sensitive issues according to [`SECURITY.md`](SECURITY.md).

## Rule changes

A new or modified rule must describe:

- the real user problem or observed failure;
- why current rules are insufficient;
- the requirement level and scope;
- observable acceptance criteria;
- compatibility impact on existing projects;
- migration or temporary deviation guidance when needed.

Published rule IDs remain stable. Retired IDs are documented and never reused for another meaning.

## Writing requirements

- Write normative content in English.
- Prefer observable outcomes over implementation prescriptions.
- Keep guidance independent from frameworks and UI libraries.
- Separate requirements from rationale and examples.
- Avoid fixed pixel values unless they illustrate an acceptance boundary rather than mandate implementation.
- Avoid repeating the same instruction across several entry documents.

## Repository boundary

Do not add UI components, framework code, stylesheets, project-specific business code, private screenshots, credentials, or customer data. Framework-neutral diagrams, state tables, pseudocode, acceptance criteria, and good/bad comparisons are welcome.

## Versioning

The current version is stored in [`VERSION`](VERSION):

- **PATCH**: clarification or repository improvement without changing required product behavior;
- **MINOR**: compatible new rules or meaningful guidance expansion;
- **MAJOR**: incompatible requirement changes or removal of a published rule.

## Before submitting

Update `VERSION` and `CHANGELOG.md` when required, then run:

```sh
python3 scripts/validate.py
```
