# Search Input Focus and IME

## Scenario

A search field loses focus after each character because updating results remounts the input. Chinese IME composition also commits prematurely, and older requests can replace newer results.

## Expected rule recognition

- `FG-FORM-002`
- `FG-FORM-003`
- `FG-FILTER-001`
- `FG-QUALITY-006`

## Required outcome

The agent should investigate unstable identity and state ownership, preserve composition, prevent stale response ordering, and add regression coverage for focus, caret position, IME, and rapid queries.

## Failure conditions

- Calling focus after every render.
- Adding a delay without fixing remounting.
- Ignoring composition events or request ordering.
