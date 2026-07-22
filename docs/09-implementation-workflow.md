# Frontend Implementation Workflow

## 1. Establish context

Before editing, inspect:

- the page entry point and primary user task;
- the framework, UI system, and existing patterns;
- routing, state ownership, data fetching, and mutation behavior;
- permission and lifecycle states;
- sibling pages and shared components;
- existing tests, fixtures, and run commands;
- browser, locale, device, theme, and accessibility commitments.

## 2. Reproduce and describe the symptom

Record:

- the observable failure;
- exact trigger conditions;
- stable vs transition-state behavior;
- affected viewports, input methods, roles, and data sizes;
- evidence such as measured geometry, focus state, route state, or request order.

Do not infer the implementation only from the screenshot or symptom.

## 3. Identify the root cause

Determine whether the cause is in:

1. server or data semantics;
2. client state ownership or request ordering;
3. a shared interaction pattern;
4. page composition;
5. an isolated instance.

Document why the selected boundary is the smallest correct fix.

## 4. Plan the state matrix

Select applicable states before implementation:

- normal, loading, stale, empty, partial, error, timeout;
- long content, translation expansion, zoom, narrow screen;
- keyboard, focus, IME composition, touch;
- disabled, read-only, locked, permission denied;
- transition, cancellation, duplicate submission;
- conflict and restoration.

Use [`../templates/FRONTEND_TASK_PLAN.md`](../templates/FRONTEND_TASK_PLAN.md) for complex tasks.

## 5. Implement

- Keep the change focused on the root cause.
- Reuse the project's visual and interaction language.
- Avoid new dependencies without a clear capability gap.
- Do not rewrite unrelated surfaces.
- Make state ownership explicit.
- Define timing for complex transitions.
- Preserve user input, browser history, and authoritative permission checks.
- Keep the change reversible.

## 6. Run static and automated checks

Run the project's formatter, lint, type checks, unit tests, component tests, and production build as applicable.

A passing build proves only that the application compiles. It does not prove geometry, focus, overflow, input method, route restoration, or animation behavior.

## 7. Validate in a real browser

Verify observable outcomes at the relevant viewports and states. For animation, positioning, and focus defects, inspect:

- before the transition;
- during the transition;
- after the transition settles.

Use representative content and roles, including long values and permission-restricted states.

## 8. Audit sibling surfaces

Search every meaningful usage of the changed pattern and determine:

- whether it receives the fix automatically;
- whether any surface relies on the previous behavior;
- whether migration is required;
- whether the same defect appears in another form;
- where regression coverage belongs.

## 9. Deliver evidence

The delivery report must include:

```text
User-visible outcome:
Root cause:
Fix layer:
Rules applied:
Sibling surfaces reviewed:
Automated checks:
Browser evidence:
Not verified:
Remaining risk:
Rollback path:
```

Do not describe untested behavior as verified.
