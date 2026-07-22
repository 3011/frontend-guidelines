# Editability and Lifecycle

## Editable appearance must match capability

A value that users can edit should look and behave editable. A value they cannot edit should be presented as information, not as a normal enabled input.

Avoid these misleading states:

- an enabled-looking input that rejects all changes;
- a select that opens but cannot commit;
- a disabled form used only to display completed data;
- a lock icon without an explanation users can discover;
- a hidden save button while fields still look editable.

## Read-only presentation

Read-only information may still need:

- selection and copy;
- complete value disclosure;
- labels and relationships;
- keyboard navigation when interactive actions remain;
- source or inheritance explanation;
- a clear path to request or obtain edit access.

Do not reduce contrast so far that read-only content looks disabled or unavailable.

## Disabled controls

Use disabled controls when the same action or field is part of the current task but temporarily unavailable. Explain the recovery condition for important controls.

Do not use a disabled control as the primary presentation of historical, completed, archived, or immutable data.

## Lifecycle states

Design explicit presentations for states such as:

- draft;
- active;
- pending approval;
- running;
- completed;
- stopped;
- locked;
- archived;
- deleted or scheduled for deletion.

Each state should define:

- editable fields;
- available actions;
- status explanation;
- allowed transitions;
- whether changes are immediate or queued;
- whether the state can be reversed.

## Permissions and lifecycle together

Editability may depend on both role and resource state. A user with edit permission may still be unable to change a completed or locked record.

Explain the relevant reason without exposing unnecessary internal policy. Keep server enforcement authoritative.

## Transition into read-only state

When a save, submit, lock, or completion action makes a form read-only:

- show a clear completion result;
- replace editable controls with stable presentation;
- preserve access to submitted values;
- move focus to the new status or next action;
- prevent stale controls from accepting local edits;
- handle server rejection by restoring an editable recovery state.

## Reopening or cloning

If users need to modify completed data, define whether they reopen, create a revision, clone, or start a new record. Do not silently turn immutable history back into an editable object.
