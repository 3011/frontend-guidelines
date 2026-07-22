# Contributing

This repository accepts framework-agnostic frontend requirements, rationale, examples, templates, and documentation validation tooling.

## Rule changes

A new or modified rule must state:

- the real user problem or observed failure;
- why current rules are insufficient;
- the requirement level;
- applicable and non-applicable scope;
- observable acceptance criteria;
- compatibility impact on existing projects;
- whether a migration or temporary deviation may be required.

Published rule IDs remain stable. Retired IDs are documented and never reused for a different meaning.

## Writing requirements

- Write normative content in English.
- Prefer observable outcomes over implementation prescriptions.
- Keep guidance independent from frameworks and UI libraries.
- Separate a requirement from its rationale and examples.
- Avoid absolute pixel values unless they illustrate a ratio or acceptance boundary rather than mandate implementation.
- Do not duplicate a rule in several chapters with conflicting wording.

## Prohibited content

Do not submit UI components, framework code, CSS implementations, project-specific business code, private screenshots, credentials, or customer data.

## Before submitting

Run:

```sh
python3 scripts/validate.py
```

Update `VERSION` and `CHANGELOG.md` when the change affects published guidance.
