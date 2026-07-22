# Anchored Popup Positioning

## Scenario

A select popup partially overlaps its trigger and leaves part of the trigger border visible. The component library describes this as its default selected-item alignment behavior.

## Expected rule recognition

- `FG-CORE-004`
- `FG-OVERLAY-002`
- `FG-OVERLAY-003`
- `FG-QUALITY-004`

## Required outcome

The agent should judge the final geometry rather than accept the library default, identify whether the fix belongs in a shared popup primitive, and verify alignment, width, viewport collision, keyboard use, and transition completion.

## Failure conditions

- Calling the behavior correct only because it is documented by the library.
- Adding a page-specific offset without reviewing shared usages.
- Measuring geometry before the opening transition has completed.
