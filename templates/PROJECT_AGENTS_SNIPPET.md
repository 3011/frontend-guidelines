# Frontend Guidelines

Before any frontend development, read:

- `docs/frontend-guidelines/AGENTS.md`
- `docs/frontend-guidelines/FRONTEND_SPEC.md`
- the detailed chapters relevant to the task
- `docs/frontend-guidelines/docs/10-validation-checklist.md`
- the project root `PROJECT_FRONTEND_PROFILE.md`

Precedence: non-waivable legal/security/accessibility requirements > current user requirements > project constraints > established reasonable project patterns > shared guidelines > framework or UI library defaults.

For non-trivial changes, document the root cause, selected fix layer, affected sibling surfaces, relevant rule IDs, state matrix, and validation plan before implementation.

Any deviation must be recorded in `PROJECT_FRONTEND_PROFILE.md` with the rule ID, scope, reason, user impact, safeguards, validation, and review condition. A component library default is not a sufficient deviation reason.
