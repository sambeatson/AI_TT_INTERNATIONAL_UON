# P1 — QA-score ONE report (run once per report date, fresh session each time)

**Inputs you may open — and nothing else:**
- `reports/md/<REPORT_FILE>` (the report for date D = <D>)
- `reports/md/` files for dates strictly before D, if you need to check consistency
- `data/slices/<ASSET>/<ASSET>_upto_<D-1>.csv` and the matching rows of any sliced auxiliary feeds
- `cards/baseline/by_date/<D>.json`
- `docs/QA_PROTOCOL_TRADE_CARDS.md`, `docs/AI_Output_Trust_Score_Framework_v3.7.pdf` (Sections 4–7)
- static linter output: run `python engine/linter.py --cards cards/baseline/cards_baseline.csv --out /tmp/lint.csv` and use only the rows for D

**You must not open:** `results/`, `qa/baseline/lint_baseline.csv`, any report dated after D, any slice
later than D-1, the web. You do not know what happened on or after D. Do not speculate about it.

**Do:**
1. Score the five categories with the Section 7 checklist. Category 3: compare every D-1 OHLC value the
   report states to the slice; compare the report's RSI2 to a recomputation from the slice; spot-check three
   cited sources for internal consistency (you cannot fetch them — check they are named, dated, and used
   consistently). Note every discrepancy with its location.
2. Compute Card Integrity from the linter rows.
3. Write `qa/<RUN_ID>/<D>_trust_score.md` exactly in the layout of the protocol's "Output per report".
4. Write `qa/<RUN_ID>/<D>_feedback.md`: numbered, specific, actionable. For each card, state the defect,
   the rule it violates, and what a compliant level would have to satisfy (e.g. "long limit must be at or
   below the D-1 close; TP1 must be above entry by ≥ 0.5×ATR14(D-1) = X pts"). Give numbers from the slice.
   Never say whether the trade would have worked.
5. Append one row to `qa/<RUN_ID>/trust_scores.csv`.
6. Commit: `stage1: <RUN_ID> QA <D>`.

Parameters for this run: RUN_ID=<RUN_ID>  D=<D>  REPORT_FILE=<REPORT_FILE>  ASSET=<ASSET>
