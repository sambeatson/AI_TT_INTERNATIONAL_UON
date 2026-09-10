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
