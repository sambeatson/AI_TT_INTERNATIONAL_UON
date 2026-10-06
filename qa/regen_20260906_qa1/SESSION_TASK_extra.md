# Stage 1 task — QA-score ONE S&P 500 report (the three dates added late: 2026-06-23, 07-06, 07-07)

Score exactly as the other 54 S&P reports were scored, so the 57 form one consistent set.

**Read, and nothing else:** `qa/regen_20260906_qa1/REVIEWER_BRIEF.md` (first, in full) ·
`docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7 · `docs/QA_PROTOCOL_TRADE_CARDS.md` ·
`reports/md/<REPORT_FILE>` · `data/slices/US500/US500_upto_<D-1>.csv` (run
`python engine/qa_slice_stats.py --slice <that file> --date <D>` for the reference numbers; add
`--closes <the report's five stated closes>` to test its RSI2 arithmetic) · `cards/baseline/by_date/<D>.json` ·
`qa/regen_20260906_qa1/lint_static/<D>.csv` (copy verbatim for Card Integrity) · `modules/` for rule text.

**Never open:** `results/`, `data/raw/`, any other date's slice or report, any report dated after D,
`cards/regenerated/`, the web. You do not know what happened on or after D.

**Write** `qa/regen_20260906_qa1/<D>_trust_score.md` (state on their own lines: `c1=` … `c5=`, `total=`,
`band=`, `override=`, `card_integrity=`, `n_cards=`, `n_duds=`, `n_warns=`) and
`qa/regen_20260906_qa1/<D>_feedback.md` (numbered; per card: defect, rule violated, the numeric condition a
compliant level must meet, using the slice's numbers; never whether a trade would have worked).
Do not touch `trust_scores.csv`; do not commit. Reply in under 10 lines: the score line and the three
most consequential defects.
