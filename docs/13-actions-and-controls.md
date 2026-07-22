# Actions and Controls

## Action hierarchy

Every page, card, modal, panel, or row has an action scope. A clear scope normally has one primary action.

Typical hierarchy:

```text
Primary: advances or completes the current task
Secondary: optional or supporting action
Cancel/back: leaves the current workflow
Destructive: deletes, stops, revokes, or resets
```

Do not make every button equally prominent or use many colors as a substitute for hierarchy.

## Position and hit-area stability

Place save, cancel, close, and destructive actions consistently across equivalent flows. A loading state may show progress, but should not drastically change button width, order, or hit area.

For repeated row actions, long names must not push actions out of view or compress them into impractical targets. Reflow information before sacrificing operability.

## Icon-only actions

Use icon-only controls for frequent, widely understood, space-constrained actions. They still require:

- an accessible name;
- visible keyboard focus;
- an adequate pointer and touch target;
- stable placement;
- supplemental explanation when meaning is uncertain.

Delete, terminate, permission change, and other consequential actions should not rely on an ambiguous icon alone.

## Loading and duplicate submission

After submission begins:

- prevent accidental duplicate effects;
- preserve focus or move it deliberately;
- keep the action state understandable;
- allow safe retry after failure;
- distinguish request acceptance from remote completion.

Do not permanently disable a control after a failed request.

## Destructive actions

Destructive actions should:

- be separated visually or spatially from routine actions;
- state object, count, scope, and downstream effect;
- request confirmation only when it prevents meaningful harm;
- name the confirmation with the actual action;
- avoid default focus;
- explain whether the action can be reversed or cancelled.

Repeated confirmations for harmless actions train users to ignore warnings. Match friction to risk.

## Capability-dependent actions

The UI should reflect what the current user can do:

- omit irrelevant actions when absence is understandable;
- show a disabled action with explanation when discovering the capability matters;
- present read-only information when editing is unavailable;
- update when role or lifecycle state changes.

This behavior communicates capability. It does not replace server-side authorization.

## Action menus

Place infrequent secondary actions in a menu only when discoverability remains acceptable. Do not hide the primary action or high-risk state behind an unlabeled menu without a clear reason.

Menu items should use the same terms as standalone actions and preserve destructive separation.
