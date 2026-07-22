# State, Routing, and Persistence

## Assign state ownership deliberately

For each meaningful state, decide whether it belongs in:

- the URL;
- server-authoritative data;
- a recoverable draft;
- persisted local preference;
- session state;
- ephemeral component state.

Common states include search, filters, sort, page, selected entity, active tab, expanded section, view mode, wizard progress, and unsaved form data.

Do not let ownership emerge accidentally from the easiest component hook or storage API.

## URL state

Place state in the URL when users reasonably need to:

- refresh without losing context;
- use back and forward;
- bookmark or share a view;
- return from a detail page;
- open the same filtered dataset in another tab.

Avoid URLs that contain secrets, sensitive free-form text, unstable internal IDs without policy, or every transient interaction.

## Browser history

A history entry should represent a meaningful navigation state. Do not add entries for hover, tooltip, internal animation steps, or every keystroke unless the product explicitly requires it.

Back and forward must not:

- submit duplicate mutations;
- silently discard unrelated drafts;
- reopen destructive confirmation without context;
- trap users in repeated overlay states;
- restore an entity the user can no longer access without explanation.

## Restoration

On refresh, reconnect, or return navigation:

- restore enough context for orientation;
- avoid reviving stale destructive intent;
- validate stored IDs and permissions;
- indicate stale or refreshed data;
- clear state that is no longer valid;
- preserve user work where practical.

A restored screen must be understandable without relying on memory from the previous session.

## Local persistence

Persist preferences only when recurrence benefits users. Define scope by account, workspace, device, and environment.

Do not persist secrets or sensitive content in general browser storage without a security model. Provide a reset path when persisted state can make the interface confusing.

## Drafts

A draft should identify:

- what is saved;
- where it is saved;
- whether it syncs across devices;
- when it expires;
- how users discard it;
- how conflicts are resolved.

Do not present a locally saved draft as a server-confirmed change.

## Concurrent updates

When another user, tab, process, or background refresh can change the same data:

- detect stale writes where practical;
- explain the conflict;
- preserve the user's attempted changes;
- offer compare, reload, retry, or merge behavior appropriate to risk;
- avoid silent last-write-wins for consequential data.

## Route transitions and pending work

Define whether pending reads and mutations continue, cancel, or detach when navigation occurs. A route change must not produce duplicate requests or leave the user unable to find the result of long-running work.
