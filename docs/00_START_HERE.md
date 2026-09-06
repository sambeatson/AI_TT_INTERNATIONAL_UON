# Start here — operator steps (short form)

**Your part**

1. Create the GitHub repo. Unzip this package at the root. Commit as `init: card-scoring package`.
2. Data is included: nine M15 feeds in `data/raw/` (1 Apr – 3/4 Sep 2026) and the refined calendar in
   `data/news/news_events.csv`. All nine were checked: no duplicate bars, no null OHLC, volume peaks
   consistent with broker = UTC+3 (US500/NAS100/XAUUSD/BTCUSD 16:30, UK100 10:00). Nothing to add.
3. (nothing to do — retained for numbering)
4. Open a **fresh** Claude Code session at the repo root. Paste `prompts/P0_setup_and_tz_check.md`.
   It must report the 16:30 volume peak and the −9.40R regression before you continue.
5. Choose a RUN_ID (e.g. `regen_20260906_qa1`). For each of the 54 report dates, open a **fresh** session
   and paste `prompts/P1_qa_score_report.md` with the parameters filled in (D, REPORT_FILE from
   `cards/baseline/cards_baseline.csv` column `report_file`, ASSET=US500). One session per date — this is
   the leakage control, not a convenience. 54 sessions.
6. Optionally update the M-modules from the QA roll-up (`qa/<RUN_ID>/trust_scores.csv` will show the
   recurring failures). Commit module changes on their own.
7. For each date, and for each draw K = 1..3, open a **fresh** session and paste
   `prompts/P2_regenerate_cards.md` with parameters. 54 × 3 = 162 sessions. Batch them.
8. One session: paste `P3`, then `P4`, then `P5` in sequence (full data allowed from here on).
9. Read `results/compare/REPORT_<RUN_ID>.md`.

**What's fixed and what's yours**

- Fixed: the engine, the policies, the leakage rules, the Trust Score rubric and its mapping, the card schema.
- Yours: which dates, how many draws, whether to edit modules between QA and regeneration, sizing.

**Repeating for another asset (WTI, BTCUSD, EURUSD, USDX)**

Same steps with that asset's reports in `reports/`, its M15 file in `data/raw/`, and its OPEN/CUTOFF
(FX 09:00/18:00; others 09:00/23:00). Build its baseline card registry first by extracting cards from
its reports into the schema — the S&P registry in `cards/baseline` is the worked example of the format.
Run `tz_check.py` before anything else; the offset must be verified per file.

**Time budget (rough)**: P0 10 min · P1 ~10 min/date · P2 ~10 min/date/draw · P3–P5 ~30 min.
