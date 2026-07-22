# Layout and Visual Hierarchy

## Spacing system

A project may use its own scale, but it must preserve semantic levels:

- tightly related elements use a small gap;
- fields or controls within one group use a standard gap;
- independent semantic sections use a larger gap;
- major page regions use the largest separation.

A reference relationship such as 8 / 16 / 24 / 32 units may be useful, but the rule is about hierarchy and consistency, not mandated values.

## Dividers

A divider supports hierarchy; it does not create hierarchy by itself. Both sides need enough whitespace to prevent the adjacent content from appearing attached to the line.

Incorrect:

```text
Description
----------------
Next section
```

Better:

```text
Description

----------------

Next section
```

If a section needs a divider, it usually also needs a heading, spacing, or both.

## Alignment and stability

Primary actions, status markers, identifiers, and comparison columns should stay in predictable locations. Test changes caused by:

- short to long text;
- optional icons or badges;
- loading placeholders becoming content;
- refresh and sorting;
- expanded and collapsed state;
- validation messages appearing;
- translation and browser zoom.

Do not let content length push controls off-screen or make the same action appear at a different visual position in every row.

## Long content

Validate at least:

- long translated text;
- identifiers without spaces;
- long numbers, addresses, paths, or URLs;
- browser zoom and enlarged text;
- narrow screens;
- missing or unknown values.

Wrapping, truncation, scrolling, disclosure, or reflow may be appropriate. Essential actions cannot disappear. Truncated information needs an accessible way to obtain the full value when the full value matters.

## Density

Density follows frequency, comparison needs, device, and risk:

- high-frequency operational lists may be compact;
- creation and editing need readable grouping;
- risky confirmation needs explicit scope and consequence;
- dashboards should not force every metric to compete at equal prominence.

Reducing whitespace without preserving grouping is not a density strategy.

## Hierarchy before decoration

Use order, grouping, typography, and spacing before adding borders, cards, shadows, or colors. Excess containers weaken hierarchy by making every area look equally important.

## Stable regions during loading

Loading placeholders should approximate the final structure when practical. Background refresh should preserve usable content rather than replacing the entire page with a blank or blocking state.
