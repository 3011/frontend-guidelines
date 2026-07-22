# User Interface Language

## Use product language

The interface should show only information users need to understand or complete their task.

Do not expose statements such as:

- “Authorization is enforced by the backend.”
- “This feature will be implemented later.”
- “This endpoint is kept for compatibility.”
- “This screen uses a particular component.”
- internal migration notes, technical debt, or developer comments.

Such content belongs in engineering documentation, release notes, diagnostics, or administration surfaces designed for that audience.

## Name actions explicitly

Prefer a verb and object:

- Save settings
- Create task
- Stop scan
- Delete record
- Reconnect account

Use “Confirm,” “Done,” or “Process” only when the result is already unmistakable from the immediate context.

## Help text supports a decision

Useful help answers one or more of:

- What does this option change?
- When should it be changed?
- What is the default behavior?
- What risk or cost does it introduce?
- Where does this value come from?

Do not repeat the label or explain implementation details.

## Error messages

Lead with a user-understandable problem and a recovery path. Preserve entered data when possible. A diagnostic code may be secondary information for support, not a substitute for the explanation.

Avoid blaming users. State the constraint and next step.

## Consistent terminology

Use one term for the same concept across navigation, headings, actions, status, empty states, documentation links, and errors. A terminology change requires a search across the product, not a one-page alias.

## Risk and scope language

Before an impactful action, name:

- the exact object or population affected;
- whether the effect is immediate or queued;
- whether it is reversible;
- what dependent data or users may be affected.

Confirmation copy must not hide scope behind generic words.

## Concision and scanning

Use short headings, direct sentences, and lists only when they improve scanning. Avoid repeated explanations in adjacent labels, help text, and tooltips.
