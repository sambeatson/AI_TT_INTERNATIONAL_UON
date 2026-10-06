# FTSE regeneration (ftse_regen1) — run log

| date | draw | incident | effect |
|---|---|---|---|
| 2026-07-03 | 1 | session ran `pip install python-dateutil pytz` (reported pandas would not import in its shell); environment checked afterwards, pandas imports normally | none on cards |
| 07-15, 07-20–07-23, 07-27–07-31 | 1 | session usage limit killed 10 draw-1 sessions mid-run; none had written an output file; re-queued | none |
| 05-11–05-15, 05-18–05-22 | 2 | same usage-limit kill, 10 draw-2 sessions; no outputs written; re-queued. The container was also recycled: scratch folders lost (sessions recreate their own) | none |
| 07-27, 07-28, 07-30 | 1 | **Container recycle wiped `data/slices/`** (git-ignored). Three draw-1 sessions completed without any slice (they fell back on QA notes for swings, cross-asset and calendar) → moved to `superseded/<D>_draw1_noslices.json`; one partial draw-2 file (05-18) → `superseded/2026-05-18_draw2_killed.json`. All 17 other sessions in flight were stopped. Slices rebuilt with `engine/slices.py` from the raw M15 files in git history (restored outside the tree) and `cards/baseline/ftse_report_dates.csv`; leak check: 57 dates × UK100/USDX/US500/VIX/NEWS, last bar < D everywhere, UK100 last bar = level-file `last_bar_date` on every date, no NEWS actuals on D. SESSION_TASK gained a "missing input = stop" rule. All affected jobs re-queued | outputs replaced |
| 06-18 | 1, 2, 3 | Trade 2 built on the **weekly** pivot tier because the daily tier gives R≈14 (< 0.3×ATR). Session cites the report's own weekly-P reading; this is a possible basis-shopping case under SESSION_TASK rule 6 — flagged for the central audit, card kept as issued | audit flag |
| 06-24 | 2 | `ls cards/regenerated/ftse_regen1/` showed the assembled `cards_regen_draw1.csv` (not opened). To remove the temptation, the assembled draw-1 registry and its lint were taken out of the tree until all draws finish (they are in git history and are rebuilt at assembly) | none |
| 07-17 | 2 | Trade 2 buy stop placed one pivot tier up (above R1) rather than at P+0.10×(R1−P), apparently to keep the order on the right side of the reference close — off-formula, flagged for the central audit, card kept as issued | audit flag |
| 05-28 | 1, 3 | Trade 2 built on the **weekly** cash pivot tier (session cites the report's own Trade 2 and QA item 24) — same pattern as 06-18; flagged for the central basis-shopping audit | audit flag |
| 06-15 | 3 | Trade 2 buy stop placed at daily R1 (not P+0.10×(R1−P)) with targets advanced one tier (R1.5/R2/R3; TP1 ≈ 0.2R) — off-formula, flagged for the central audit | audit flag |
| 07-17 | 3 | Trade 2 buy stop at cash R1 (targets R1.5/R2/R3, TP1 ≈ 0.19R), following QA feedback item 18 rather than the M5 P+0.10×(R1−P) formula — same QA-driven pattern as 07-17 d2 and 06-15 d3; flagged for audit | audit flag |
| 07-29 | 3 | Trade 2 buy stop at daily R1 (formula level sat below the close) with targets taken from daily/weekly/monthly R3 so TP1 clears 1R — off-formula and mixes pivot tiers; flagged for audit | audit flag |

## Assembly (all 171 sessions complete)
- `cards_regen_draw{1,2,3}.csv`: 171 cards each, 57/57 dates. Live cards: draw 1 = 75, draw 2 = 71, draw 3 = 73 (Trade 2 dominates; most 3rd cards are suppressed 3C because the regime reads TRANSITION and no 25-day break is confirmed).
- Central static lint (`lint/lint_static_draw*.csv`): 0 DUD in every draw; one WARN_DUPLICATE (2026-05-26 Trade 1, draw 3 — identical to another draw's card, expected when the construction is deterministic).
- Provenance check: every record carries the right draw, `source`, `module_sha=f69b2cd`, report_date and report_file — 0 problems.
- Audit flags above (06-18 d1–3 and 05-28 d1/d3 weekly-tier Trade 2; 06-15 d3, 07-17 d2/d3, 07-29 d3 off-formula Trade 2 entries) are kept as issued and reported as a sensitivity in the write-up.
