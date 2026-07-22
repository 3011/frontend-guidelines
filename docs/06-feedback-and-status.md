# Feedback and Status

## State matrix

For each async region, consider:

- initial loading;
- background refresh;
- usable but stale data;
- empty data;
- partial data;
- successful completion;
- recoverable error;
- terminal error;
- permission denial;
- offline state;
- timeout;
- cancellation;
- conflict with newer data.

Not every state needs a separate page, but blank space or indefinite loading is not an explanation.

## Loading

Keep layout stable when practical. Short operations should not block the entire page. Long work should identify a useful stage, indicate whether users may leave, and define cancellation or continuation behavior.

Do not replace still-valid data with a full-screen loading state during background refresh.

## Stale and refreshing data

When freshness matters, distinguish:

- last successfully loaded data;
- current refresh activity;
- refresh failure;
- the age or source of the displayed data.

A refresh error should not automatically erase usable last-known data. It should prevent users from mistaking stale data for a fresh result.

## Empty states

Distinguish:

- nothing has been created;
- no match under current search;
- no match under active filters;
- data failed to load;
- the account cannot access data;
- data exists but is outside the current time or scope.

Each state needs a suitable explanation and next action.

## Success feedback

When the result is already obvious in the updated page, avoid an additional blocking success message. Success feedback should be brief, truthful, and must not cover the next task.

For long-running or queued work, acknowledge acceptance separately from completion.

## Errors and retry

Error feedback should explain:

- what failed;
- whether user input or remote data was saved;
- whether retry is safe;
- how to recover or where to get help;
- whether currently displayed data is stale or incomplete.

Do not use raw exceptions, stack traces, provider messages, or internal codes as the primary user-facing explanation. Diagnostic identifiers may appear as secondary copy when useful for support.

## Progress

Use determinate progress only when the denominator is meaningful. Otherwise show a stage, elapsed state, or indeterminate activity without inventing a percentage.

Progress should not reset or move backward without explanation. Cancellation must clarify whether partial effects remain.

## Optimistic updates

An optimistic update requires:

- a defined authoritative response;
- duplicate prevention;
- rollback or reconciliation on failure;
- visible recovery when the server rejects or modifies the result;
- conflict handling when newer data arrives.

Never leave success styling after an operation failed.

## Destructive actions

Before execution, identify the target, scope, permanence, downstream effect, and recovery option. Name the confirmation action directly, for example “Delete 12 records,” rather than “Confirm.”
