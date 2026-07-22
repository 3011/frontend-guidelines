# Frontend Specification

This file is the compact normative entry point. Detailed rationale, examples, exceptions, and acceptance guidance are in `docs/`.

## Core

### FG-CORE-001 — Prioritize the user task [MUST]

Structure, hierarchy, defaults, and actions must serve the user's current task. Do not add implementation details or controls that do not help the user understand or complete that task.

### FG-CORE-002 — Preserve reasonable project consistency [MUST]

Reuse established, sound patterns within the project. Equivalent tasks must not use different layouts, terms, or interaction models without a documented reason.

### FG-CORE-003 — Fix the root cause at the correct layer [MUST]

Fix the smallest responsibility boundary that removes the class of defect. Do not hide a shared cause with local offsets, duplicated conditions, or one-off styles.

### FG-CORE-004 — Verify defaults instead of trusting them [MUST]

Framework, browser, and UI library defaults are not acceptance evidence. Verify the final visual, interaction, responsive, accessibility, and failure behavior.

### FG-CORE-005 — Keep changes within product scope [MUST]

Do not restyle, rename, or restructure unrelated surfaces while fixing a focused issue. Broader consistency work requires explicit scope and validation.

## Layout and hierarchy

### FG-LAYOUT-001 — Spacing communicates hierarchy [MUST]

Related elements, fields within a group, independent sections, and major page regions must use distinguishable spacing levels. Separation between semantic sections should exceed spacing within a section.

### FG-LAYOUT-002 — Dividers must not touch content [MUST]

Dividers, borders, and section boundaries must not sit directly against headings, descriptions, controls, buttons, or cards. Dividers supplement hierarchy; they do not replace spacing.

### FG-LAYOUT-003 — Important alignment remains stable [MUST]

Text length, status changes, icon appearance, loading transitions, and data refresh must not cause primary actions, identifiers, or comparison columns to jump without purpose.

### FG-LAYOUT-004 — Long content is a designed state [MUST]

Long labels, identifiers, translations, numbers, zoomed text, and narrow screens must not hide essential information or actions. Truncation must preserve a way to access the full value.

### FG-LAYOUT-005 — Density follows task frequency and risk [SHOULD]

High-frequency scanning surfaces may be compact; creation, editing, and risky decisions need stronger grouping and breathing room. Compactness must not erase hierarchy or hit targets.

## Forms and input

### FG-FORM-001 — Field relationships are explicit [MUST]

Every input must have an identifiable label. Help text, units, constraints, status, and errors must be clearly associated with the correct field.

### FG-FORM-002 — Input state remains stable [MUST]

State updates, filtering, validation, and list reordering must not remount the active input, lose focus, move the caret, or discard uncommitted text.

### FG-FORM-003 — IME composition is respected [MUST]

Search, filtering, and live validation must support input method composition. Do not treat uncommitted composition text as final input or trigger destructive refreshes before composition completes.

### FG-FORM-004 — Forms follow user decisions [SHOULD]

Group complex forms by user intent and decision order rather than backend field order. Use headings and concise explanations; do not rely on dividers alone.

### FG-FORM-005 — Errors are local, specific, and recoverable [MUST]

Show errors near the affected field, explain how to recover, update them when corrected, and never rely on color alone.

### FG-FORM-006 — Read-only state must not look editable [MUST]

Values that cannot be edited must be presented as read-only information, not as enabled input or selection controls. Permission, lifecycle, or lock state must be understandable without trial and error.

### FG-FORM-007 — Unsaved work must not disappear silently [MUST]

Closing, navigating away, changing context, or reloading must not silently discard meaningful user input. Warn, preserve, or explicitly define safe auto-save behavior.

## Overlays and floating UI

### FG-OVERLAY-001 — Choose the container by task [MUST]

Use a focused modal for creation, editing, confirmation, or blocking decisions. Use a side panel for auxiliary detail, context, navigation, or non-blocking inspection. Equivalent workflows must be consistent.

### FG-OVERLAY-002 — Anchored popups must be visually complete [MUST]

Selects, menus, and similar popups must have stable placement. Prefer opening below and aligning the logical start edge; avoid partial overlap, exposed trigger edges, unexplained offsets, or width that clips meaningful options.

### FG-OVERLAY-003 — Floating content remains within the usable viewport [MUST]

Popups must avoid viewport edges, keyboards, safe areas, and fixed regions. Long content must scroll within a bounded region while essential actions remain reachable.

### FG-OVERLAY-004 — Tooltips require explicit user intent [MUST]

Tooltips may open only from stable hover or keyboard focus. Mounting, layout changes, collapse transitions, state restoration, and scrolling must not open one or many tooltips accidentally.

### FG-OVERLAY-005 — Close and focus behavior is predictable [MUST]

Escape, outside interaction, close controls, and browser navigation must have consistent effects appropriate to the task risk. Opening and closing must place focus in a logical location.

### FG-OVERLAY-006 — Stacking and background behavior remain coherent [MUST]

Nested overlays, scroll locking, background interaction, and focus containment must not create unreachable content, trapped users, hidden confirmations, or multiple competing modal layers.

## Navigation

### FG-NAV-001 — Current location is identifiable [MUST]

Users must be able to identify the current page, active navigation item, and return path. Do not communicate the current state with color alone.

### FG-NAV-002 — Collapsible navigation has no transient noise [MUST]

During collapse or expansion, navigation must not produce bulk tooltips, flashing labels, moving hit areas, or unusable intermediate states.

### FG-NAV-003 — Navigation labels stay concise and stable [SHOULD]

Navigation uses short, familiar, consistent terms. Long explanations, volatile status text, and implementation details belong in page content.

### FG-NAV-004 — Browser history and deep links remain meaningful [MUST]

Back, forward, refresh, and direct URLs must preserve or restore meaningful location and context. Do not trap navigation entirely in ephemeral component state when users need to return or share it.

## Feedback and status

### FG-STATE-001 — Critical states have explicit feedback [MUST]

Async regions must account for initial loading, background refresh, empty data, partial data, success, recoverable error, terminal error, permission denial, offline state, and timeout where relevant.

### FG-STATE-002 — Feedback intensity matches impact [MUST]

Use non-blocking feedback for lightweight success, visible recoverable feedback for failure, and clear pre-action explanation for destructive or broad-impact operations.

### FG-STATE-003 — Disabled actions explain recovery [SHOULD]

When a meaningful action is unavailable, users should be able to understand why and what condition will enable it. A disabled appearance alone is insufficient for important actions.

### FG-STATE-004 — Stale and refreshing data are distinguishable [MUST]

Background refresh must not erase usable data without need. When freshness matters, distinguish last known data, refreshing state, stale state, and failed refresh.

### FG-STATE-005 — Progress is truthful [MUST]

Progress indicators must not imply precision the system does not have. Long-running work should expose a meaningful stage, completion signal, cancellation policy, or safe way to leave.

### FG-STATE-006 — Optimistic changes are reversible or reconcilable [MUST]

Optimistic updates must define failure recovery, duplicate prevention, and reconciliation with authoritative data. Never leave the interface showing success after the server rejected the change.

## Data, lists, and filters

### FG-DATA-001 — Data shape follows the comparison task [MUST]

Use tables when users compare stable fields across rows; use lists or cards for heterogeneous summaries and narrow-screen priority. Do not choose a shape only because a component already exists.

### FG-DATA-002 — Key columns and row actions remain stable [MUST]

Refresh, long names, optional icons, and status changes must not move core identifiers, selection controls, or row actions unpredictably.

### FG-DATA-003 — Sort and filter state is visible [MUST]

Users must be able to identify the active sort, search scope, and filters. Clarify whether sorting applies to all data or only the loaded subset.

### FG-DATA-004 — Counts and ranges are precise [MUST]

Distinguish displayed count, loaded count, selected count, total count, and estimated count. Pagination and partial loading must not imply completeness that is not available.

### FG-DATA-005 — Selection has an explicit scope [MUST]

Bulk selection must make clear whether it applies to visible rows, the current page, loaded results, filtered results, or the full dataset. Refresh and filter changes must not silently broaden a selection.

### FG-DATA-006 — Data freshness and time context are visible when relevant [MUST]

When decisions depend on freshness, show the relevant timestamp, timezone, source, or update status. Do not present stale or locally formatted time as universally current.

### FG-FILTER-001 — Search and filtering do not interrupt input [MUST]

Result updates must not remount the input, steal focus, reset the caret, break IME composition, or roll results backward because an older request finished later.

### FG-FILTER-002 — Active filters are discoverable and removable [MUST]

Users must be able to identify each active filter and clear one or all. Distinguish an empty dataset from no results under the current filters.

### FG-FILTER-003 — Meaningful filter state can be restored [SHOULD]

When returning, refreshing, or sharing a view is part of the workflow, preserve search, sort, filter, page, and view state in an appropriate durable location such as the URL.

## Actions and controls

### FG-ACTION-001 — One primary action per clear scope [SHOULD]

A page, panel, dialog, card, or row normally has one visually dominant action. Secondary, cancel, and destructive actions must not compete with it.

### FG-ACTION-002 — Action position and hit area remain stable [MUST]

Equivalent flows place actions consistently. Text length, loading state, and icon changes must not cause severe movement or shrink the hit target below practical use.

### FG-ACTION-003 — Icons do not replace necessary meaning [MUST]

Icon-only actions require a widely understood meaning, an accessible name, keyboard access, and an adequate target. Risky, rare, or ambiguous actions require visible text.

### FG-ACTION-004 — Destructive actions are separated [MUST]

Delete, stop, reset, revoke, and similar actions must be visually or spatially distinct from routine actions and must not become the default focus.

### FG-ACTION-005 — Submission prevents accidental duplication [MUST]

A pending operation must prevent accidental duplicate submission without losing focus or recovery. Failure must return the control to a safe retry state.

### FG-ACTION-006 — Visible actions reflect capabilities, not security claims [MUST]

The interface should show only actions relevant to the current capability, but hiding or disabling an action is not authorization. Server-side enforcement remains authoritative.

## Responsive behavior and accessibility

### FG-RESP-001 — Responsive design reprioritizes information [MUST]

Narrow-screen behavior must reorder, group, collapse, or transform content according to user priority. It must not merely scale down the desktop layout.

### FG-RESP-002 — Essential actions remain reachable [MUST]

On narrow screens, zoomed text, touch keyboards, and safe-area insets must not hide primary actions, close controls, or error recovery.

### FG-RESP-003 — Touch targets and gestures have alternatives [MUST]

Touch targets must be practical to hit. Hover-only and gesture-only interactions require a visible or keyboard-accessible alternative.

### FG-A11Y-001 — Keyboard users can complete core flows [MUST]

Core tasks must work by keyboard with focus order matching the visual and logical order. Focus must not enter hidden content, disappear, or become trapped unexpectedly.

### FG-A11Y-002 — Keyboard focus is visibly distinct [MUST]

Every interactive element must have a clear keyboard focus indicator that remains visible across themes and backgrounds.

### FG-A11Y-003 — Dynamic changes are understandable [MUST]

Loading completion, errors, state changes, and opened overlays must provide appropriate focus and assistive information without producing repetitive announcement noise.

### FG-A11Y-004 — Color is never the only signal [MUST]

Selection, status, success, error, warning, and disabled state require text, shape, iconography, position, or another non-color signal.

### FG-A11Y-005 — Reduced motion preserves function [MUST]

Respect reduced-motion preferences. Removing or shortening motion must not remove information, prevent completion, or expose invalid intermediate states.

## Content and terminology

### FG-CONTENT-001 — User interfaces use user language [MUST]

Do not expose implementation notes, backend enforcement descriptions, compatibility layers, development plans, technical debt, stack traces, or internal comments unless the user's task specifically requires diagnostic detail.

### FG-CONTENT-002 — Actions use explicit verbs [SHOULD]

Use concrete labels such as “Save settings,” “Stop scan,” or “Delete 12 records.” Avoid vague labels such as “Confirm” when the action is not already obvious.

### FG-CONTENT-003 — Risk is explained before execution [MUST]

Before irreversible, broad-impact, or expensive actions, explain the object, scope, consequence, and recovery status.

### FG-CONTENT-004 — Help text supports decisions [SHOULD]

Help text should explain what changes, when the option matters, the default behavior, or the risk. It should not repeat the label or describe implementation.

### FG-CONTENT-005 — Terminology is consistent [MUST]

Use one user-facing term for the same concept across navigation, headings, actions, status, and errors. A terminology change requires a project-wide audit.

## Performance and resilience

### FG-PERF-001 — User input receives prompt feedback [MUST]

Typing, selecting, opening controls, and invoking common actions must remain responsive under expected data and device conditions. Heavy work must not block input without visible feedback.

### FG-PERF-002 — Loading preserves layout stability [SHOULD]

Placeholders and progressive rendering should avoid large, unnecessary layout shifts. Do not replace stable usable content with a blank full-screen loading state during background work.

### FG-PERF-003 — Large collections use bounded rendering [MUST]

Large tables, lists, menus, logs, and option sets must use pagination, incremental loading, virtualization, search, or another bounded strategy appropriate to the task.

### FG-PERF-004 — Failure and slow networks remain usable [MUST]

Expected latency, retries, partial failure, and offline transitions must not duplicate actions, lose input, or leave the interface in an indeterminate state.

## Permissions, security, and privacy

### FG-SEC-001 — The UI is not an authorization boundary [MUST]

Client-side visibility and disabled state may communicate capability but must never be the sole enforcement of permissions or data access.

### FG-SEC-002 — Sensitive data is minimized and protected [MUST]

Do not expose secrets, tokens, private identifiers, hidden fields, or sensitive diagnostics in visible UI, URLs, logs, analytics, clipboard content, or error messages without explicit need and protection.

### FG-SEC-003 — Untrusted content is treated as untrusted [MUST]

User-generated or remote content must not be rendered as executable markup or interpreted commands without an explicit sanitization and trust model.

### FG-SEC-004 — High-impact external effects are explicit [MUST]

Copying secrets, downloading sensitive files, opening external destinations, revoking access, or triggering broad remote actions must make the target and consequence clear before execution.

## Localization and formatting

### FG-I18N-001 — Layout tolerates text expansion [MUST]

Labels, actions, navigation, tables, and overlays must tolerate longer translations and scripts without relying on fixed English string lengths.

### FG-I18N-002 — Values use locale-aware formatting [MUST]

Dates, times, numbers, currencies, units, plural forms, and sorting must use explicit locale-aware rules appropriate to the product and data source.

### FG-I18N-003 — Timezone and relative-time semantics are explicit [MUST]

When time affects decisions, identify the timezone or source and avoid ambiguous phrases such as “today” across users, servers, and stored data.

## State, routing, and persistence

### FG-ROUTE-001 — User-relevant view state has deliberate ownership [MUST]

Decide explicitly whether search, filters, sort, page, selected entity, expanded section, and draft data belong in the URL, durable storage, server state, or ephemeral component state.

### FG-ROUTE-002 — Restoration is safe and understandable [MUST]

Refresh, return navigation, reconnect, and session restoration must not revive stale destructive intent, silently submit drafts, or place users in a context they cannot understand.

### FG-ROUTE-003 — Back and forward navigation preserve expectations [MUST]

Browser navigation must not unexpectedly close unrelated work, skip meaningful states, duplicate requests, or trap users in modal-only history entries.

### FG-ROUTE-004 — Concurrent edits and stale writes are handled [MUST]

When data may change elsewhere, detect or explain conflicts, preserve user work where practical, and avoid silently overwriting newer authoritative state.

## Quality and delivery

### FG-QUALITY-001 — Validate the relevant state matrix [MUST]

At minimum, validate normal, loading, empty, error, disabled, long-content, narrow-screen, keyboard, and transition states. Input work also validates IME composition; data work validates stale and partial states where relevant.

### FG-QUALITY-002 — Audit sibling surfaces [MUST]

After changing a shared pattern, inspect every meaningful usage for automatic improvement, incompatible assumptions, required migration, and regression coverage.

### FG-QUALITY-003 — Tests assert observable outcomes [SHOULD]

Automated tests should assert user-visible behavior, focus, state, and critical geometry rather than a particular UI library's private structure.

### FG-QUALITY-004 — Browser validation covers time and geometry [MUST]

Positioning, animation, focus, overflow, and responsive defects require real browser validation at stable states and relevant transition points.

### FG-QUALITY-005 — Unverified claims are disclosed [MUST]

Delivery reports must distinguish verified evidence, inferred behavior, skipped checks, and environmental limitations. “Should work” is not evidence.

### FG-QUALITY-006 — Regression coverage matches the root cause [SHOULD]

Add or update the smallest durable test that would fail for the original defect, especially for shared interactions, focus loss, popup geometry, navigation state, and permission-dependent actions.
