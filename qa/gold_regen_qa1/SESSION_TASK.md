# Stage 1 task — QA-score ONE gold report

You are one of 57 independent review sessions. Follow `prompts/P1_qa_score_report.md` as amended here.

## Read, and nothing else
- `qa/gold_regen_qa1/REVIEWER_BRIEF.md` — read this first, in full
- `docs/AI_Output_Trust_Score_Framework_v3.7.txt` Sections 4–7 · `docs/QA_PROTOCOL_TRADE_CARDS.md`
- `reports/md/<REPORT_FILE>` — your report, for date D
- `data/levels/XAUUSD_by_date/<D>.csv` — the leak-free data-derived levels for D (check its
  `last_bar_date` < D yourself before using it)
- `data/slices/XAUUSD/XAUUSD_upto_<D-1>.csv` — the raw M15 bars behind that file, if you want them
- `cards/baseline/gold/by_date/<D>.json` — the transcribed cards
- `qa/gold_regen_qa1/lint_static/<D>.csv` — the linter rows for D (already leak-free: no
  market-relative flags). Copy them verbatim for Card Integrity; do not re-derive or re-run the linter.
- `modules/` if you need the rule text

## Never open
`results/`, `data/raw/`, `data/levels/XAUUSD_levels.csv`, `qa/gold_regen_qa1/lint_baseline.csv`, any
other date's level file or slice, any report dated after D, the web. Those first four are not in the
tree during this stage; if you find them, stop and say so — something is wrong.
**You do not know what price did on or after D. Do not speculate about it.**

## Do
1. Score the five categories against the Section 7 checklist in the brief. For Category 3, compare
   the report's stated D−1 OHLC, RSI2, ATR14, and its daily / weekly / monthly pivots against your
   level file, using the tolerances in brief §4 and the basis (`_cash` / `_full`) the report claims.
   Record every discrepancy with its location and size.
2. Compute Card Integrity from the linter rows: per card 100 − 40·(#DUD) − 10·(#WARN), floored at 0;
   report level = mean over non-suppressed cards. It is separate from the 100.
3. Write `qa/gold_regen_qa1/<D>_trust_score.md` in the protocol's "Output per report" layout. It must
   state, explicitly and on their own lines: `c1=`, `c2=`, `c3=`, `c4=`, `c5=` (levels 0–5),
   `total=`, `band=`, `override=` (`none` / `hallucinated_source` / `restriction_breach`),
   `card_integrity=`, `n_cards=`, `n_duds=`, `n_warns=`.
4. Write `qa/gold_regen_qa1/<D>_feedback.md`: numbered, specific, actionable. Per card: the defect,
   the rule it violates, and the numeric condition a compliant level must satisfy, using your level
   file's numbers. Never say whether a trade would have worked.
5. Do NOT touch `trust_scores.csv` and do NOT commit — 57 sessions cannot append to one file or
   commit concurrently. The roll-up is done centrally afterwards.

## Reply
Keep your reply under 12 lines: the score line (`c1..c5 total band override card_integrity`), then
the three most consequential defects you found, one line each. Nothing else.
