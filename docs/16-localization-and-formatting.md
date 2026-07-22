# Localization and Formatting

## Text expansion

English is often shorter than translated text. Validate longer labels, navigation terms, actions, status, table headings, error messages, and overlay content.

Do not rely on fixed string widths. Preserve essential actions and complete meaning through reflow, wrapping, disclosure, or accessible truncation.

## Script and input diversity

Support the scripts and input methods required by the product. Account for:

- composition-based input;
- scripts without spaces;
- combining characters;
- different capitalization rules;
- right-to-left direction when supported;
- different name and address structures.

Do not apply English-specific assumptions to validation, truncation, sorting, or search without a product requirement.

## Numbers and units

Use explicit locale-aware rules for:

- decimal and grouping separators;
- percentages;
- currencies;
- measurement units;
- compact notation;
- plural forms;
- negative values and ranges.

Keep the underlying value and displayed value distinct. Do not parse a localized display string as if it were a universal machine format.

## Dates and times

Specify:

- source timezone;
- display timezone;
- date and time format;
- whether seconds matter;
- whether relative time is appropriate;
- how daylight-saving transitions are handled;
- whether a date represents an instant, a local calendar date, or a reporting period.

Avoid ambiguous numeric dates. A relative label such as “today” or “3 hours ago” needs an accessible exact timestamp when precision matters.

## Sorting and search

Sorting and comparison should use locale and product semantics, not raw code-point order, when users expect natural language behavior.

Search should define normalization, case, accents, tokenization, and transliteration behavior rather than inheriting accidental browser or database defaults.

## String composition

Avoid constructing user-facing sentences by concatenating fragments whose order assumes English grammar. Use complete translatable messages with named values and plural-aware variants.

## Missing translations

A missing translation must not expose an internal key or silently remove an action. Define a safe fallback language and a way to detect missing coverage in testing.
