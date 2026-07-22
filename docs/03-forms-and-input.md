# Forms and Input

## Field structure

A field should form a stable relationship:

```text
Label
Optional decision-supporting help
Input or value
Error, status, or constraint feedback
```

Do not rely on a placeholder as the only label. Show units, formats, range, and examples only when they help users enter a valid value.

## Group by user decisions

Organize complex forms around the order users make decisions, not the order of backend fields. Related fields belong together under a clear section title.

When advanced options are collapsed, users should still be able to tell:

- that advanced options exist;
- whether defaults are active;
- whether the section contains validation errors or non-default values;
- what kind of decisions are inside.

## Focus and identity stability

These are defects:

- typing one character causes focus loss;
- filtering remounts the input;
- refresh moves the caret;
- conditional rendering replaces the active control;
- a validation update moves focus to an unrelated element;
- opening helper content makes it impossible to return to the field.

Investigate unstable keys, remounts, state ownership, conditional trees, request races, and focus side effects rather than adding a local focus workaround first.

## Input method composition

During composition, unfinished text must not be treated as a final query or validated destructively.

Validate this sequence:

1. begin composition;
2. change the composition candidate without losing focus;
3. confirm the text;
4. update search or validation after confirmation;
5. continue typing, delete, and switch input methods;
6. ensure an older request cannot replace newer results.

The requirement applies to Chinese, Japanese, Korean, speech input, predictive keyboards, and other composition-based input.

## Validation timing

- Validate immediately only when feedback is safe and useful during entry.
- Validate on blur or submit when the complete value is required.
- Do not show persistent errors before users have had a reasonable chance to finish.
- Explain how to recover, not only what is invalid.
- On failed submission, guide focus to the first actionable error and provide a summary when several errors are difficult to discover.

## Defaults and derived values

Defaults must be understandable and safe. A default value should not look like user-confirmed intent when it triggers a costly, destructive, or broad action.

Derived, inherited, or server-controlled values should identify their source when users may otherwise believe they can edit or override them.

## Save, cancel, and drafts

Closing, navigating away, changing entity, refreshing, or session expiry must not silently discard meaningful work. Use one or more of:

- explicit save and discard decisions;
- safe auto-save with visible status;
- recoverable drafts;
- a clear warning that identifies what will be lost.

Do not ask only “Are you sure?” State the consequence.

## Read-only and locked fields

Do not present non-editable data as enabled input controls. Use a presentation that communicates value and state. When useful, explain why editing is unavailable and what condition would allow it.

Read-only does not mean inaccessible: values must remain selectable, readable, and available to assistive technology where appropriate.
