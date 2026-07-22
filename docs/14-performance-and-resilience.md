# Performance and Resilience

## User-perceived responsiveness

Performance is part of interaction correctness. Typing, opening controls, changing a selection, scrolling, and invoking frequent actions should provide prompt feedback under expected device and data conditions.

A delayed operation should acknowledge input immediately even when completion is asynchronous.

## Main-thread and rendering pressure

Large synchronous work must not block typing, focus, animation, or pointer input. Investigate:

- unnecessary rerenders;
- expensive formatting in repeated rows;
- rendering hidden content;
- large option sets;
- repeated layout measurement;
- event handlers that perform network or parsing work synchronously.

The specification does not mandate a particular optimization technique. It requires stable interaction under expected load.

## Large collections

Use a bounded strategy appropriate to the task:

- server or client pagination;
- incremental loading;
- virtualization;
- search before display;
- grouping or summarization;
- capped logs with explicit access to history.

Do not render an unbounded table, menu, log, or tree merely because the first test dataset is small.

## Layout stability

Loading, images, charts, validation, and late-arriving metadata should reserve or transition space without large unexpected shifts. Preserve the user's reading position and click target.

Avoid replacing a usable page with a blocking loader for background work.

## Slow networks

Test realistic delay and out-of-order responses. The interface should:

- preserve entered data;
- prevent duplicate effects;
- ignore or reconcile stale responses;
- identify ongoing work;
- allow navigation when safe;
- distinguish timeout from permanent failure.

## Retry

Retry behavior must be safe. Define whether an operation is idempotent, whether the original request may still complete, and how duplicate results are reconciled.

Do not automatically retry destructive or expensive operations without a clear safety model.

## Offline and reconnect

When offline use is relevant:

- distinguish local edits from server-confirmed state;
- explain whether work is queued or only saved locally;
- reconcile conflicts on reconnect;
- avoid presenting local success as remote completion;
- preserve a path to copy or recover unsent work.

## Performance evidence

Use evidence appropriate to the defect, such as:

- interaction timing under representative data;
- render count or profile evidence;
- layout-shift observation;
- bounded DOM size;
- slow-network browser testing;
- verification that typing and focus remain stable during refresh.

A synthetic score alone does not prove the affected workflow is usable.
