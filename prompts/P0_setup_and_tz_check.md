# P0 — Setup, timezone verification, slices

You are working in the `card-scoring` repo. Read `README.md`, `docs/REPO_CONVENTIONS.md`,
`docs/LEAKAGE_PROTOCOL.md`. Do not open `results/` in this stage.

Tasks:
1. `pip install -r engine/requirements.txt`.
2. For every file in `data/raw/*_M15.csv` run `python engine/tz_check.py <file> --expect <HH:MM>` with the
   expected broker peak: US500/NAS100/XAUUSD/BTCUSD 16:30, UK100 10:00; EURUSD/USDX/VIX/SpotCrude peak later in the NY session (17:00–18:15) — report what you observe.
   If any file's peak contradicts UTC+3, STOP and report; do not proceed.
3. Confirm `reports/md/` has one .md per .docx in `reports/docx/` (run pandoc for any missing).
4. Build leak-free slices for the primary asset and every auxiliary feed present (VIX, DXY, news):
   `python engine/slices.py --data data/raw/<file> --dates cards/baseline/cards_baseline.csv --out data/slices/<ASSET>`
   (news: `--data data/news/news_events.csv --tscol timestamp_broker --news --out data/slices/NEWS`). Print each MANIFEST and check `last_bar_broker` < report_date for every row.
5. Regression: `python engine/resolver.py --cards cards/baseline/cards_baseline.csv --data data/raw/US500_p_M15.csv --policy band0845 --out results/baseline_band0845`
   must print TOTAL R −9.49. If not, stop and report.
6. Commit: `stage0: setup + slices + regression OK`.
