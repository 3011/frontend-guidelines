# Deviations and Exceptions

This specification supports product judgment; it does not replace it. A project may deviate, but the deviation must be explicit and reviewable.

## Acceptable reasons

Common valid reasons include:

- a legal or industry requirement;
- a target-device limitation;
- a specific accessibility need;
- a stable legacy pattern that cannot be migrated immediately;
- a deliberate product experiment with defined evidence;
- an explicit current user requirement;
- a security or privacy constraint that requires a different interaction.

“The library behaves this way,” “this is faster to implement,” and “this screen is special” are not sufficient reasons on their own.

## Required record

```text
Rule: FG-...
Scope: page, workflow, role, viewport, or pattern usage
Reason:
User impact:
Compensating safeguards:
Validation:
Review trigger or expiry:
Owner:
```

A deviation should be narrow. Do not use one exception to exempt an entire product when only one workflow differs.

## Temporary deviations

A temporary deviation requires a review condition or expiry. When the condition is met, remove the deviation or convert it into an intentional permanent project rule with evidence.

## Experiments

An experiment may temporarily vary a SHOULD requirement when:

- the hypothesis and success metric are defined;
- assignment does not create a legal, privacy, security, or accessibility violation;
- users can still complete the task;
- the losing variant is removed after evaluation.

Do not experiment by silently violating a MUST requirement.

## Not applicable

A rule may be marked not applicable when the state genuinely cannot occur. This does not require a deviation record. “Not tested,” “not implemented yet,” and “environment unavailable” are not equivalent to not applicable.

## Specification defects

When a rule is unclear or wrong for a broad class of products, open a specification change rather than accumulating project-level exceptions. Include real user evidence and migration impact.
