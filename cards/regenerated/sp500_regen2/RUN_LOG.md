# sp500_regen2 — run log (incidents and deviations)

## Shared-scratch collisions, draw 1 (superseded and re-run)

The first 23 draw-1 sessions were launched before the task gave each session a private scratch folder.
Concurrent sessions wrote helper files to the same shared directory, and three reported reading another
session's output:

| date | what the session reported | exposure |
|---|---|---|
| 2026-05-12 | its self-lint printed **another date's cards** | cards of another date may contain later-dated price levels |
| 2026-05-20 | its helper script was **overwritten** by another session's | content seen is unknown |
| 2026-06-04 | an overwritten script briefly showed a **VIX close dated 2026-06-04 — day D itself** | a same-day price: a direct breach of the leakage rule |

All three said they did not act on what they saw. That is not verifiable, and the method's claim rests on
no session seeing D or later, so **all three outputs are superseded** (kept unmodified in `superseded/`
for audit) and the three dates are re-run in fresh sessions under the private-scratch task.

Fixes applied to `SESSION_TASK.md` during draw 1: (1) unique temp names for the self-lint, (2) a private
scratch folder per session, (3) a note that the slice's `DateTime_UTC` column is mislabelled. None changes
how a card is built, so draws remain comparable.

Twenty other early sessions ran on the shared directory without reporting a collision. Their outputs are
kept: a collision manifested as a visible error or as foreign data, and these sessions reported neither.
This is a residual risk, stated rather than hidden.

## Late-date QA
2026-06-23, 07-06, 07-07 were QA-scored late under the same brief as the other 54.
