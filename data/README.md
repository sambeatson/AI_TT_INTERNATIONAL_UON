# data/

`raw/`     Full-history M15 files exactly as exported from MT5. Never edited. Columns:
           DateTime_Broker, DateTime_UTC (mislabelled, ignore), Open, High, Low, Close, TickVolume, Spread, RealVolume
           Present: US500 NAS100 UK100 XAUUSD SpotCrude BTCUSD EURUSD USDX VIX  (1 Apr - 3/4 Sep 2026, all verified UTC+3).

`slices/`  Built by `engine/slices.py`. One file per report date containing ONLY bars with broker date < report date.
           This is the only data a QA or regeneration agent may open. See docs/LEAKAGE_PROTOCOL.md.

`news/`    see news/README.md - refined MT5 calendar, broker-time timestamps, sliced with --news.