# FTSE regeneration (ftse_regen1) — run log

| date | draw | incident | effect |
|---|---|---|---|
| 2026-07-03 | 1 | session ran `pip install python-dateutil pytz` (reported pandas would not import in its shell); environment checked afterwards, pandas imports normally | none on cards |
| 07-15, 07-20–07-23, 07-27–07-31 | 1 | session usage limit killed 10 draw-1 sessions mid-run; none had written an output file; re-queued | none |
| 05-11–05-15, 05-18–05-22 | 2 | same usage-limit kill, 10 draw-2 sessions; no outputs written; re-queued. The container was also recycled: scratch folders lost (sessions recreate their own) | none |
| 07-27, 07-28, 07-30 | 1 | **Container recycle wiped `data/slices/`** (git-ignored). Three draw-1 sessions completed without any slice (they fell back on QA notes for swings, cross-asset and calendar) → moved to `superseded/<D>_draw1_noslices.json`; one partial draw-2 file (05-18) → `superseded/2026-05-18_draw2_killed.json`. All 17 other sessions in flight were stopped. Slices rebuilt with `engine/slices.py` from the raw M15 files in git history (restored outside the tree) and `cards/baseline/ftse_report_dates.csv`; leak check: 57 dates × UK100/USDX/US500/VIX/NEWS, last bar < D everywhere, UK100 last bar = level-file `last_bar_date` on every date, no NEWS actuals on D. SESSION_TASK gained a "missing input = stop" rule. All affected jobs re-queued | outputs replaced |
| 06-18 | 1, 2 | Trade 2 built on the **weekly** pivot tier because the daily tier gives R≈14 (< 0.3×ATR). Session cites the report's own weekly-P reading; this is a possible basis-shopping case under SESSION_TASK rule 6 — flagged for the central audit, card kept as issued | audit flag |
