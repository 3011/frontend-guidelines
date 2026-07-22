# Principles

## User task first

Every surface should have a clear primary user task. Information order, visual emphasis, default focus, and the primary action should support that task.

Do not add metrics, controls, implementation notes, or explanations merely to display system capability. Technical detail belongs in the interface only when users need it to decide, diagnose, or recover.

## Consistency is not mechanical copying

Useful consistency means:

- equivalent tasks use the same information order;
- the same action uses the same name and placement;
- equivalent states use the same feedback intensity;
- equivalent risk uses the same confirmation model;
- route and restoration behavior remains predictable across sibling screens.

Do not copy a defective pattern simply because it already exists. Evaluate the pattern before reusing it.

## Fix the root cause

Separate three concepts:

- **symptom** — an element touches another, flashes, shifts, or loses focus;
- **root cause** — missing spacing hierarchy, unstable component identity, incorrect state ownership, timing, or permission assumptions;
- **fix layer** — data/state, shared interaction, page composition, or isolated instance.

The smallest change is not always the smallest number of edited lines. It is the smallest correct responsibility boundary that prevents recurrence without unrelated redesign.

## Observable outcomes are authoritative

Acceptance focuses on what users can observe:

- layout remains stable;
- the task can be completed;
- states are understandable;
- focus and browser history behave correctly;
- text remains readable and complete enough;
- errors are recoverable;
- transitions do not expose broken intermediate states.

A clean implementation is valuable, but it does not replace browser evidence.

## Preserve user agency

Users should understand when work starts, whether it is still running, whether they can leave, and what will happen to entered data. Avoid hidden state transitions, irreversible defaults, surprise navigation, or automatic actions that change remote data without clear intent.

## Progressive disclosure, not concealment

Advanced or infrequent options may be collapsed, but their existence, current effect, and default behavior should remain understandable. Progressive disclosure reduces cognitive load; it must not hide active risk, errors, or non-default state.
