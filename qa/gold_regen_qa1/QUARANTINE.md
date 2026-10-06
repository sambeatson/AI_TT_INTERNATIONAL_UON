# Leak-surface quarantine — active for Stages 1 and 2 of `gold_regen_qa1`

`docs/LEAKAGE_PROTOCOL.md` forbids a QA or regeneration session from seeing outcomes, later bars, or
market-relative lint. Instructing 57 sessions not to look is weaker than removing the files, so these
paths are **out of the working tree for the duration of Stages 1–2**, and their absence is committed
so the history records exactly when each was unreachable:

| path | why |
|---|---|
| `results/` | scored outcomes for both assets — the answer |
| `data/raw/` | full M15 feeds, unbounded in time. Sessions use `data/slices/XAUUSD/*_upto_<D-1>.csv` and `data/levels/XAUUSD_by_date/<D>.csv` instead, both bounded strictly before D |
| `data/levels/XAUUSD_levels.csv`, `data/levels/US500_levels.csv` | the full per-asset level tables, every date in one file |
| `qa/gold_regen_qa1/lint_baseline.csv` | linted against full data, so its STALE_ANCHOR / MISPLACED_* / MALFORMED_FILL flags are computed against the day-D anchor. `lint_static/<D>.csv` is the leak-free substitute and carries no market-relative flag |

Restore after Stage 2, then re-verify both regression fixtures before scoring anything:
US500 `band0845` = **−9.49 R**, gold `band0845` = **−0.59 R**.

Working copies are held outside the repo at
`/tmp/claude-0/QUARANTINE/` for this session; the durable copies are in git history at the commit
before this one.

## Added for the S&P re-run (`sp500_regen2`)
Four more files carry day-D price information and are now out of the tree for the duration of the S&P
regeneration: `qa/regen_20260906_qa1/lint_baseline.csv`, `lint_draw1.csv`, `lint_comparison.md` and
`qa/baseline/lint_baseline.csv` — all linted against full data, so their STALE_ANCHOR / MISPLACED_* flags
encode where the market opened on D. Held at `/tmp/claude-0/QUARANTINE/sp500_qa_leaky/`; durable copies in
history. `docs/ENTRY_POLICIES.md` and `README.md` stay in the tree (they define the engine) but quote past
aggregate outcomes, so regeneration sessions are now instructed not to open them — a tightening over
the first run, which allowed `ENTRY_POLICIES.md`.

## Restored after the S&P re-run (2026-10-06)
All quarantined paths were restored from git history (commits before `6327689` and `38411eb`) once the last
`sp500_regen2` session finished. Both fixtures re-verified: US500 `band0845` −9.49 R, gold `band0845` −0.59 R.
**Gold Stage 2 has not run yet: re-apply this quarantine before launching any gold regeneration session.**

## Re-applied for the FTSE run (`ftse_qa1` / `ftse_regen1`)
Same paths as above, plus the new full table `data/levels/UK100_levels.csv` (never committed; held at
`/tmp/claude-0/QUARANTINE/UK100_levels.csv`). Sessions get `data/levels/UK100_by_date/<D>.csv` and
`data/slices/UK100/UK100_upto_<D-1>.csv` only. Restore after the last FTSE regeneration session.
