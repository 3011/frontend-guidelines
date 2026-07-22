# Data, Lists, and Filters

## Choose the data shape

### Tables

Use a table when users need to compare stable fields across rows, scan structured operational data, sort columns, or perform dense repeated actions.

A table is not the default answer. If fields vary widely, summaries are more important than comparison, or narrow-screen use dominates, a list or card view may be better.

### Lists and cards

Use a list or card view when:

- items have heterogeneous content;
- the primary task is browsing summaries rather than horizontal comparison;
- narrow screens need a vertical priority order;
- each item has only a few actions.

Do not add a border and shadow to every row without a hierarchy reason. Container emphasis should match information hierarchy.

## Table stability

Validate:

- long names and identifiers;
- optional badges or icons;
- one vs several row actions;
- sorting and refresh;
- missing and exceptional values;
- loading placeholders;
- large text and narrow widths;
- permission-dependent actions.

Keep primary identifiers, selection, and row actions predictable. Do not allow content length to place the same control at a different visual coordinate in every row.

## Sorting

Make current sort column and direction visible. Distinguish default order from explicit ascending or descending order.

Do not sort only the current page while presenting the result as if the full dataset were sorted. Clarify server-side vs loaded-subset behavior.

## Search and filters

Search supports fuzzy location; filters express explicit conditions. When combined, users should understand:

- the search scope;
- active filters;
- how conditions affect the count;
- how to clear one filter or reset all;
- whether conditions persist on refresh, return, or share.

Debouncing or request optimization must not alter entered text, lose focus, break composition, or let an older result replace a newer one.

## No results

Distinguish:

```text
The system contains no data.
The current search has no match.
The active filter combination has no match.
Data could not be loaded.
The current account cannot view the data.
Data exists outside the selected time or scope.
```

Each state requires a different explanation and next action.

## Counts and pagination

Identify whether a number is:

- visible rows;
- loaded rows;
- selected rows;
- current page size;
- filtered total;
- global total;
- an estimate.

Do not mix these meanings. Returning to a list should restore page, scroll, search, sort, and filters when that supports the workflow.

## Bulk selection

Selection controls must state their scope. “Select all” may mean:

- all visible rows;
- all rows on the current page;
- all loaded results;
- all filtered results;
- the entire dataset.

A filter, refresh, or page change must not silently broaden a destructive selection. Before execution, repeat the selected count and scope.

## Row expansion and details

Expanded content should not destabilize unrelated rows or hide the row identity. If details deserve navigation, bookmarking, or independent loading, prefer a route or dedicated detail surface over an oversized inline expansion.

## Freshness and source

When data drives operational decisions, expose relevant freshness and source information. Background refresh should preserve last-known data but distinguish stale content from a successful current result.
