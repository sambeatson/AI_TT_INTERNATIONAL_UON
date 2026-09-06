# news_events.csv — MT5 economic calendar, 1 Apr – 4 Sep 2026, deduplicated

`timestamp_broker` is BROKER time (UTC+3): verified — NFP rows sit at 15:30 (08:30 ET) and FOMC at 21:00 (14:00 ET).
Columns: timestamp_broker, date, currency, event, sector, impact (NONE|LOW|MODERATE|HIGH), scheduled (Y),
actual, consensus (= MT5 Forecast), previous, source.

Leak rule (enforced by `engine/slices.py --news`): for a report dated D the agent receives
  - rows with date < D in full;
  - rows with date == D with `actual` BLANKED (the scheduled calendar is ex-ante information);
  - nothing dated > D.
Source file MT5_News.csv (2013–2026, 917k rows) is not shipped; this is the refined extract.
