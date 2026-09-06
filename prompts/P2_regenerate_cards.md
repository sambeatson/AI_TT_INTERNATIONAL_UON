# P2 — Regenerate the cards for ONE report date (run once per date per draw, fresh session)

**Inputs you may open — and nothing else:**
- `reports/md/<REPORT_FILE>` — the report for D (its analysis sections are the ONLY research you have)
- `qa/<RUN_ID>/<D>_feedback.md` and `<D>_trust_score.md`
- `data/slices/<ASSET>/<ASSET>_upto_<D-1>.csv` (+ `data/slices/VIX/VIX_upto_<D-1>.csv` and `data/slices/NEWS/news_upto_<D-1>.csv` — the news slice already contains D's scheduled calendar with actuals blanked; use it)
- `cards/schema/card_schema.json`, `docs/ENTRY_POLICIES.md` (so you know how cards will be executed)
- the M5 strategy module text if present in `modules/` (fixed rules: three units, BE rule, runner rule)

**You must not open:** `cards/baseline/` for D (you are producing an independent set), `results/`, any
report or slice dated ≥ D, the web. No new research. No knowledge of what happened on D or later.

**Produce** `cards/regenerated/<RUN_ID>/by_date/<D>.json` — a list of card records matching the schema —
for Trade 1, Trade 2, and Trade 3 (variant per the report's regime call). Requirements:
- `anchor_broker` explicit on every card (HH:MM broker). Default 09:00 unless the report's own logic
  argues for 02:00 or 16:30 and you say why in `rationale`.
- Every level is a number derived from the slice (state the derivation in `rationale`: pivot formula,
  ATR14(D-1) value, swing anchors with their bar timestamps).
- Static integrity: stop on the correct side; TP1 beyond entry; TP2 beyond TP1; TP3 beyond TP2 or explicitly
  `null`; 0.3×ATR14 ≤ R ≤ 3.0×ATR14; TP1 within 2.5×ATR14 of entry.
- For a MARKET card the `entry` is the D-1 close (the last price you can see). For LIMIT/STOP cards the
  level must be on the correct side of the D-1 close.
- Honour the report's suppression rule: if the report's own conviction score is below its threshold,
  emit the card with `suppressed: true`.
- Provenance: `source: "regen_<RUN_ID>_draw<K>"`, `slice_file`, `last_bar_broker` (copy from the MANIFEST).
- Run the static linter on your output before saving: `python engine/linter.py --cards <tmp.csv> --out /tmp/l.csv`.
  Zero DUD flags is mandatory. Fix and re-lint.

Then append the records to `cards/regenerated/<RUN_ID>/cards_<RUN_ID>_draw<K>.csv` and commit:
`stage2: <RUN_ID> draw<K> cards <D>`.

Parameters: RUN_ID=<RUN_ID>  DRAW=<K>  D=<D>  REPORT_FILE=<REPORT_FILE>  ASSET=<ASSET>
