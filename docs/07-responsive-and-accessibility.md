# Responsive Behavior and Accessibility

## Responsive behavior

Responsive design is not a scaled-down desktop page. On narrow screens, decide again:

- which information has priority;
- which actions must remain reachable;
- whether a table becomes a grouped list or card view;
- how multi-column forms become a logical sequence;
- how overlays preserve title, context, errors, and actions;
- whether secondary details collapse without hiding active state.

Validate at least one representative desktop width and one representative phone width. Include actual interaction, not only static screenshots.

## Zoom and text enlargement

The interface must remain usable with browser zoom and enlarged text. Essential controls cannot overlap, disappear, or require two-dimensional scrolling simply because text grows.

## Touch

Targets must be practical to hit and separated from destructive neighbors. Hover-only behavior requires a visible touch alternative. Gesture shortcuts require a conventional control when the gesture is not obvious or accessible.

## Keyboard

Core flows should support:

- Tab and Shift+Tab navigation;
- Enter or Space activation where appropriate;
- Escape for applicable overlays;
- arrow-key behavior for menus, options, and composite widgets;
- logical focus order and restoration.

Focus must not enter hidden content, disappear after an update, or move because an animation changes layout.

## Focus visibility

Keyboard focus must be clearly visible on light, dark, selected, disabled-adjacent, and high-density backgrounds. A subtle color change alone is not enough.

## Color and status

Error, success, warning, selection, required state, and disabled state cannot rely only on color. Combine color with text, icons, shape, pattern, or position.

## Motion

Motion should explain relationship or state change, not delay interaction. Respect reduced-motion preferences and ensure shorter or removed motion still results in valid timing, focus, and tooltip behavior.

## Semantics and assistive technology

Use semantics that match behavior. Names, roles, states, relationships, errors, and live updates should be exposed in a way assistive technology can understand.

Avoid announcing every background refresh. Announce meaningful changes and errors without creating repetitive noise.
