# card-scoring — forward-test of research trade cards, leak-free

Score institutional research trade cards against M15 broker data; QA the reports that produced them;
regenerate cards from QA feedback with **no look-ahead**; compare.

```
repo/
  README.md                       this file
  docs/00_START_HERE.md           the short-form steps for the operator (read first)
  docs/REPO_CONVENTIONS.md        how files are named, stored, and referred to
  docs/LEAKAGE_PROTOCOL.md        the no-peeking rules (binding)
  docs/QA_PROTOCOL_TRADE_CARDS.md Trust Score v3.7 adapted to these reports
  docs/ENTRY_POLICIES.md          the four entry policies + management variants
  docs/STATS_PLAN.md              how results are compared and tested
  docs/HANDOVER_METHOD.md         original method note (timezone finding, defect taxonomy)
  prompts/P0..P5_*.md             stage prompts for the Claude Code session
  reports/docx/                   54 source reports (S&P 500, 11 May - 31 Jul 2026)
  reports/md/                     pandoc conversions (what the QA agent reads)
  cards/schema/card_schema.json   the card record contract
  cards/baseline/                 159 cards extracted from the source reports (cards_baseline.csv + by_date/*.json)
  cards/regenerated/<run_id>/     cards produced in Stage 2, one JSON per date, k draws
  qa/baseline/                    linter output for the baseline cards
  qa/<run_id>/                    Trust Score sheets + feedback per report
  data/raw/                       nine M15 files, 1 Apr - 3/4 Sep 2026: US500 NAS100 UK100 XAUUSD SpotCrude BTCUSD EURUSD USDX VIX
  data/slices/<asset>/            leak-free per-date slices built by engine/slices.py
  data/news/news_events.csv       MT5 calendar, window-only, deduplicated (5,892 rows); sliced with --news
  engine/                         tz_check, slices, linter, resolver, equity, stats
  results/<run_id>_<policy>/      ledger.csv + summary.csv per scored set
  results/compare/                equity overlays, stats reports
```

**Timezone (binding).** Broker = UTC+3 (BST period) = UK clock + 2. The `DateTime_UTC` column in the
MT5 exports is UTC+1 and mislabelled. Index by `DateTime_Broker` only. Verify every new file with
`engine/tz_check.py` (US500/XAUUSD peak 16:30, UK100 10:00).

**Regression fixture.** `cards/baseline` scored with `--policy band0845` must give TOTAL R **−9.49** on the
shipped `data/raw/US500_p_M15.csv` (1 Apr – 3 Sep 2026). (−9.40 on the earlier file that ended 7 Aug; the
difference is three positions that resolved in August.) If it doesn't reproduce, the engine or the data changed.

Install: `pip install -r engine/requirements.txt`
