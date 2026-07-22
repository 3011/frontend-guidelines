# Sidebar Tooltip Transition

## Scenario

When a sidebar collapses, several menu tooltips flash at once while the pointer remains over the moving navigation region.

## Expected rule recognition

- `FG-OVERLAY-004`
- `FG-NAV-002`
- `FG-A11Y-005`
- `FG-QUALITY-004`

## Required outcome

The agent should treat the collapse animation as a real state, delay tooltip eligibility until the transition is complete, preserve keyboard behavior, and verify that no tooltip appears without deliberate hover or focus.

## Failure conditions

- Increasing only the tooltip delay.
- Hiding the flash with a global opacity rule.
- Testing only the final expanded and collapsed states.
