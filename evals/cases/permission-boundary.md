# Permission-Dependent Action

## Scenario

A page hides an administrative delete button for ordinary users. The backend endpoint still accepts the action when called directly.

## Expected rule recognition

- `FG-ACTION-006`
- `FG-SEC-001`
- `FG-SEC-004`
- `FG-CONTENT-003`

## Required outcome

The agent should keep capability-aware UI for clarity while requiring server-side authorization, explicit risk communication, and appropriate confirmation for the destructive action.

## Failure conditions

- Treating the hidden button as sufficient authorization.
- Showing every user a disabled control with internal permission details.
- Fixing only the frontend and claiming the security issue is resolved.
