# Repo conventions — storing and referring to files

## Identifiers
- **report_date** `YYYY-MM-DD` — the session the report is FOR (not when it was written).
- **card_id** `<report_date>_<Trade_N>` e.g. `2026-05-19_Trade_3A`. Unique within a card set.
- **run_id** `regen_<YYYYMMDD>_<short-tag>` for regeneration runs, e.g. `regen_20260906_qa1`.
  Draw index appended for multiple regenerations: `..._draw1`, `_draw2`.
- **policy** one of `card | midnight | usopen | band0845`; management suffix `_betp1` when `--be tp1`.

## Where things live
| Thing | Path | Written by |
|---|---|---|
| Source report | `reports/docx/<original name>.docx` | operator |
| Readable report | `reports/md/<same stem>.md` | pandoc (Stage 0) |
| Baseline card set | `cards/baseline/cards_baseline.csv` + `by_date/<D>.json` | provided |
| Regenerated cards | `cards/regenerated/<run_id>/by_date/<D>.json` + `cards_<run_id>.csv` | Stage 2 |
| QA sheet per report | `qa/<run_id>/<D>_trust_score.md` | Stage 1 |
| QA feedback per report | `qa/<run_id>/<D>_feedback.md` | Stage 1 |
| QA roll-up | `qa/<run_id>/trust_scores.csv` | Stage 1 |
| Lint output | `qa/<run_id>/lint_<set>.csv` | Stage 3 |
| Scored ledger | `results/<set>_<policy>/ledger.csv` | Stage 4 |
| Scored summary | `results/<set>_<policy>/summary.csv` | Stage 4 |
| Comparisons | `results/compare/<name>.md|.png|.csv` | Stage 5 |

`<set>` is `baseline` or the `run_id`.

## Referring to files in prompts
Always give the agent the **exact path**. Never say "the data" — say
`data/slices/US500/US500_upto_2026-05-18.csv`. Never say "the report" — say
`reports/md/SP500_Daily_Report_19May2026.md`. The `report_file` column in `cards_baseline.csv`
maps each report_date to its source filename; the manifest in `data/slices/<asset>/MANIFEST.csv`
maps each report_date to its slice.

## Immutability
`data/raw`, `reports/docx`, `cards/baseline`, `cards/schema` are never modified after commit.
Every stage writes to a new path keyed by run_id. Re-running a stage means a new run_id, not an overwrite.

## Commit discipline
One commit per stage per run_id, message `stage<N>: <run_id> <one line>`. Module prompt changes
(`modules/`, if you add them) are their own commits so an R delta can be attributed.
