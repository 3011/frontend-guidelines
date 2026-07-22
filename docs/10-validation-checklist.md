# Frontend Completion Checklist

Apply this checklist according to task scope. A “not applicable” item requires a reason; it cannot hide an unavailable test.

## User task and scope

- [ ] The primary user task remains clear.
- [ ] The change fixes the root cause at the correct layer.
- [ ] Unrelated layout, wording, and behavior were not changed without scope.
- [ ] Relevant sibling surfaces were inspected.

## Layout and hierarchy

- [ ] Related elements and independent sections use distinguishable spacing.
- [ ] Dividers and borders do not touch adjacent content.
- [ ] Headings, status, identifiers, and primary actions remain aligned.
- [ ] Long text, identifiers, numbers, translation expansion, and zoom do not break the layout.
- [ ] Loading and refresh do not introduce unnecessary layout shifts.
- [ ] Essential actions remain reachable on narrow screens.

## Forms and input

- [ ] Every field has an identifiable label and correct help/error association.
- [ ] Typing does not lose focus, caret position, or entered text.
- [ ] IME composition completes before destructive search or validation updates.
- [ ] Older requests cannot overwrite newer search results.
- [ ] Read-only values do not look editable.
- [ ] Unsaved work is preserved, saved, or explicitly discarded.
- [ ] The first actionable error can be found and corrected.

## Overlays and floating UI

- [ ] The modal or side-panel choice matches the task.
- [ ] Anchored popups align predictably without partial overlap or exposed trigger edges.
- [ ] Floating content remains inside the usable viewport and handles long content.
- [ ] Tooltips do not appear from mount, restoration, scrolling, or layout transition.
- [ ] Opening and closing place focus logically.
- [ ] Escape, outside interaction, close controls, and browser navigation behave consistently.
- [ ] Nested overlays do not create hidden or unreachable layers.

## Navigation and route state

- [ ] The current location and active item are identifiable without color alone.
- [ ] Collapse and expansion have no bulk tooltips, flashing labels, or moving targets.
- [ ] Back, forward, refresh, and direct links preserve expected context.
- [ ] Search, filters, page, and view state are restored or intentionally reset.
- [ ] Mobile navigation opens, operates, and closes completely.

## Data and feedback

- [ ] Initial loading, background refresh, stale, empty, partial, error, and success states are handled where relevant.
- [ ] No-data and filtered-no-results states are distinct.
- [ ] Counts distinguish displayed, loaded, selected, total, and estimated values.
- [ ] Bulk selection scope is explicit.
- [ ] Progress does not claim false precision.
- [ ] Failures explain recovery and whether retry is safe.
- [ ] Optimistic changes reconcile or roll back on rejection.

## Actions, permissions, and lifecycle

- [ ] Each clear scope has an understandable primary action.
- [ ] Action placement and hit areas remain stable.
- [ ] Icon-only actions have an accessible name and clear meaning.
- [ ] Duplicate submission is prevented safely.
- [ ] Destructive actions state object, scope, effect, and recovery.
- [ ] Capability-dependent actions match the current role without claiming to enforce authorization.
- [ ] Locked, archived, completed, or read-only states use presentation rather than editable controls.

## Responsive behavior and accessibility

- [ ] A representative desktop viewport was exercised.
- [ ] A representative phone viewport was exercised.
- [ ] Browser zoom or enlarged text was considered.
- [ ] Core flows are keyboard-completable.
- [ ] Focus remains visible and ordered logically.
- [ ] Status is not communicated only by color.
- [ ] Touch and hover interactions have appropriate alternatives.
- [ ] Reduced-motion behavior remains functional.

## Performance and resilience

- [ ] Typing and common controls remain responsive under expected data size.
- [ ] Large collections use a bounded rendering strategy.
- [ ] Slow requests, timeouts, retries, and offline transitions do not lose input or duplicate actions.
- [ ] Background refresh preserves usable content where appropriate.

## Security, privacy, and localization

- [ ] No secret or sensitive value is exposed through UI, URL, logs, analytics, clipboard, or errors without explicit need.
- [ ] Untrusted content is not interpreted as executable markup.
- [ ] Locale-aware number, date, unit, plural, sort, and timezone behavior is correct where relevant.
- [ ] Longer translated text does not hide essential content or actions.

## Content

- [ ] The page contains no developer notes or implementation details for ordinary users.
- [ ] Actions use explicit verbs and objects.
- [ ] The same concept uses consistent terminology.
- [ ] Error copy is user-facing and recoverable.
- [ ] Risk and scope are explained before impactful actions.

## Evidence and delivery

- [ ] Static checks and existing automated tests passed.
- [ ] Browser validation covers the original failure and applicable state matrix.
- [ ] A regression test targets the root cause where practical.
- [ ] Verified and unverified behavior is clearly separated in the delivery report.
- [ ] Remaining risk and rollback are documented.
