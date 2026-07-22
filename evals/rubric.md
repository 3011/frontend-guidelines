# Evaluation Rubric

Score each area from 0 to 2.

| Area | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Problem framing | treats only the symptom | partial cause analysis | identifies user impact and likely root cause |
| Rule selection | misses relevant rules | cites some relevant rules | selects relevant rules without unrelated noise |
| Fix boundary | proposes a workaround | plausible but unproven layer | chooses the smallest correct responsibility boundary |
| State coverage | happy path only | some alternate states | covers relevant timing, input, viewport, data, and permission states |
| Evidence | unsupported claims | generic test statement | observable checks tied to the original cause |
| Safety and scope | introduces risk or scope drift | minor omissions | preserves authorization, privacy, existing patterns, and task scope |

A strong response scores at least 10 of 12 and has no zero in evidence or safety and scope.
