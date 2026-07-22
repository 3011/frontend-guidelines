# Core Frontend Rules

This is the minimum cross-task reading set. It is a concise guide, not a replacement for [`FRONTEND_SPEC.md`](FRONTEND_SPEC.md), which remains the normative source.

## Product and scope

- `FG-CORE-001`: structure and actions must serve the user's current task.
- `FG-CORE-002`: equivalent tasks should follow established, reasonable project patterns.
- `FG-CORE-003`: fix the root cause at the smallest correct responsibility boundary.
- `FG-CORE-004`: verify observable behavior instead of trusting framework or library defaults.
- `FG-CORE-005`: do not restyle or restructure unrelated surfaces without explicit scope.
- `FG-CONTENT-001`: use user language, not implementation notes or internal terminology.

## Interaction stability

- `FG-LAYOUT-001`: spacing must distinguish related items, sections, and major regions.
- `FG-LAYOUT-002`: dividers must not sit directly against content.
- `FG-LAYOUT-003`: primary actions, identifiers, and comparison columns must remain stable.
- `FG-LAYOUT-004`: long content must be treated as a normal state.
- `FG-FORM-002`: typing, focus, caret position, and selection must survive ordinary updates.
- `FG-FORM-003`: IME composition must not be interrupted by filtering or rerendering.
- `FG-FORM-005`: validation errors must be specific, local, and recoverable.
- `FG-FORM-006`: read-only information must not look editable.
- `FG-FORM-007`: unsaved work must not disappear without warning.

## Floating UI and navigation

- `FG-OVERLAY-002`: anchored popups must align cleanly without partial overlap.
- `FG-OVERLAY-003`: floating content must remain within the usable viewport.
- `FG-OVERLAY-004`: tooltips require deliberate hover or keyboard focus.
- `FG-OVERLAY-005`: opening and closing overlays must preserve predictable focus.
- `FG-NAV-002`: collapsing navigation must not create transient tooltip or layout noise.
- `FG-NAV-004`: browser history and direct links must preserve meaningful navigation.

## State, actions, and safety

- `FG-STATE-001`: loading, empty, error, success, and blocked states need explicit feedback.
- `FG-STATE-004`: stale data and background refresh must be distinguishable when relevant.
- `FG-STATE-005`: determinate progress must be based on real measurements.
- `FG-FILTER-001`: search and filtering must not interrupt input or apply stale responses.
- `FG-ACTION-004`: destructive actions must be visually and spatially separated.
- `FG-ACTION-005`: submissions must prevent accidental duplication.
- `FG-ACTION-006`: visible capabilities improve clarity but never replace authorization.
- `FG-SEC-001`: the backend remains the authoritative authorization boundary.
- `FG-SEC-002`: sensitive data must be minimized in UI, URLs, logs, analytics, and storage.

## Accessibility, responsive behavior, and delivery

- `FG-RESP-001`: narrow layouts must reprioritize content rather than merely shrink it.
- `FG-RESP-002`: essential actions must remain reachable in supported viewports.
- `FG-A11Y-001`: keyboard users must be able to complete core flows.
- `FG-A11Y-002`: keyboard focus must be visible and distinguishable.
- `FG-QUALITY-001`: validate the applicable state matrix, not only the happy path.
- `FG-QUALITY-002`: review sibling surfaces that share the same pattern or cause.
- `FG-QUALITY-004`: browser checks must cover geometry and transition timing when relevant.
- `FG-QUALITY-005`: disclose anything that was not verified and the resulting risk.
