# Good and Bad Examples

These examples use framework-neutral structure and behavior descriptions.

## Form sections

Bad:

```text
[Field]
Description
----------------
Next section
```

Problem: the description, divider, and next section have no semantic spacing.

Better:

```text
[Field]
Description

----------------

Next section heading
[Field]
```

Rules: `FG-LAYOUT-001`, `FG-LAYOUT-002`.

## Anchored select popup

Bad:

```text
┌── Trigger ──────────┐
│ Current value       │
└─────────────────────┘
  ┌── Popup ────────────┐
  │ Option               │
  └──────────────────────┘
```

Problem: the popup partially overlaps the trigger and leaves an exposed edge.

Better:

```text
┌── Trigger ──────────┐
│ Current value       │
└─────────────────────┘

┌── Popup ────────────┐
│ Option              │
└─────────────────────┘
```

Rules: `FG-OVERLAY-002`, `FG-QUALITY-004`.

## Collapsible navigation tooltip

Bad sequence:

```text
Collapse requested
→ width transition starts
→ all tooltips become active immediately
→ several tooltips flash open
```

Better sequence:

```text
Collapse requested
→ suppress tooltip triggers during transition
→ layout reaches the collapsed state
→ enable tooltip behavior
→ show one tooltip only after explicit hover or focus
```

Rules: `FG-OVERLAY-004`, `FG-NAV-002`, `FG-A11Y-005`.

## Search input

Bad sequence:

```text
Type one character
→ result list refreshes
→ input is remounted
→ focus and composition are lost
```

Better sequence:

```text
Input identity remains stable
→ composition completes
→ query state updates
→ older responses cannot replace newer results
```

Rules: `FG-FORM-002`, `FG-FORM-003`, `FG-FILTER-001`.

## Read-only record

Bad:

```text
[Enabled-looking team name input]
[Enabled-looking match selector]

No save action is available.
```

Problem: the interface implies that editing is possible even though the record is locked.

Better:

```text
Team: North Division
Match: Game 3
Status: Locked after publication
Action: Create revision
```

Rules: `FG-FORM-006`, `FG-ACTION-006`, `FG-CONTENT-004`.

## Permission message

Bad:

```text
Authorization is enforced by the backend. The frontend only renders actions
allowed by the current role.
```

Better:

```text
You can view this configuration, but you do not have permission to edit it.
```

Rules: `FG-CONTENT-001`, `FG-SEC-001`, `FG-FORM-006`.

## Background refresh

Bad:

```text
Visible data
→ background refresh begins
→ entire page becomes blank loading state
→ refresh fails
→ user loses the last known result
```

Better:

```text
Keep last known data visible
→ show refreshing status
→ on failure, mark data as stale and provide retry
```

Rules: `FG-STATE-004`, `FG-PERF-002`, `FG-PERF-004`.

## Bulk selection

Bad:

```text
Select all
Selected: 50
Delete
```

The user cannot tell whether 50 means the page, loaded rows, filtered rows, or all data.

Better:

```text
50 rows on this page selected
[Select all 4,820 filtered results]
[Delete 50 selected rows]
```

Rules: `FG-DATA-004`, `FG-DATA-005`, `FG-CONTENT-003`.

## Route and filters

Bad:

```text
Apply several filters
→ open a detail page
→ press Back
→ all filters and scroll position are lost
```

Better:

```text
Meaningful filter, sort, and page state is restorable
→ Back returns to the previous working context
```

Rules: `FG-NAV-004`, `FG-FILTER-003`, `FG-ROUTE-001`.

## Destructive confirmation

Bad:

```text
Are you sure?
[Cancel] [Confirm]
```

Better:

```text
Delete 12 scan results?
This cannot be undone and does not stop active scans.
[Cancel] [Delete 12 results]
```

Rules: `FG-ACTION-004`, `FG-CONTENT-002`, `FG-CONTENT-003`.
