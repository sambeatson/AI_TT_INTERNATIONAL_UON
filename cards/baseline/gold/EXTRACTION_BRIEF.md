# Baseline card extraction brief — XAUUSD

You are transcribing trade cards out of one institutional gold research report into the registry
schema. **You are a transcriber, not an analyst.** The baseline arm must record what the report
actually said, including its mistakes. That is the entire point of the comparison.

## Absolute rules

1. **Read only your assigned report file.** Do not open `data/`, `results/`, `qa/`, `cards/`,
   `data/levels/`, any other report, or the web. If a level in the report looks wrong, **transcribe
   it anyway** — do not correct, recompute, or "fix" a single number.
2. **Never infer a price the report does not state.** If a field is genuinely absent, use `null`.
3. Transcribe to the number of decimals the report gives. Strip thousands separators and the `USD`
   / `/oz` decoration: `USD 4,715/oz` → `4715`.

## Where the cards are

`§21 Strategy Recommendations` → `§21b Trade Cards (1–3)`. Three cards per report: Trade 1, Trade 2,
Trade 3 (the third carries a variant letter — 3A momentum-pullback, 3B range/mean-reversion,
3C transition). Section numbering varies slightly between reports; find the trade-card tables, not
the literal string "§21b". **Ignore `§21c` (the 5-session backtest) entirely** — those are historical
reconstructions, not cards.

## Fields

| field | how to fill it |
|---|---|
| `card_id` | `<report_date>_Trade_1` / `_Trade_2` / `_Trade_3A` (use the variant letter the report gives; bare `_Trade_3` only if the report names no variant) |
| `report_date` | the session the report is FOR (from the title), `YYYY-MM-DD` |
| `report_file` | the `.docx` basename, e.g. `Gold_Report_11_May_2026.docx` |
| `strategy` | the card's own "Trade type" label, trimmed, e.g. `Trade 2 - Pivot (TREND_UP breakout, daily)` |
| `family` | `Trade 1` / `Trade 2` / `Trade 3A` / `Trade 3B` / `Trade 3C` |
| `direction` | `LONG` / `SHORT`, or `n/a` if suppressed with no side |
| `entry_mode` | see below |
| `entry_mode_text` | the entry cell's wording, trimmed to the clause that describes the order |
| `anchor_broker` | see below |
| `entry`, `stop`, `tp1`, `tp2`, `tp3` | floats; `tp3` is `null` when the runner is a time-stop or an ATR cap rather than a price |
| `card_R_points` | the R the card states. If the card gives R only as ticks, convert with the report's own tick definition and say so in `notes` |
| `be_rule` | `BE_0.2R_ON_TP2` if the card moves the runner stop to entry+0.2R on TP2 fill; `BE_ON_TP1` if on TP1; else `NONE` |
| `runner_rule` | `SESSION_CLOSE_TIMESTOP` if the runner exits at a session close or time-stop; `TRACE` if it trails/targets a price |
| `management_text` | the tranche-management clause, verbatim |
| `suppressed` | `true` only if the report itself declines the card |
| `source` | `baseline` |
| `notes` | anything you had to judge, and any defect you noticed but transcribed anyway |

### `entry_mode`
- `MARKET` — market/"just-fillable" order at a stated clock time (e.g. the 00:00 UK daily reset).
- `LIMIT` — a resting order **better** than current price (buy below / sell above).
- `STOP` — a resting order **worse** than current price (buy above / sell below), i.e. a breakout.
- `CONDITIONAL` — requires a confirming close or an event before the order becomes live.

Decide from the order's *wording*, not from where the level sits. "Buy limit on pullback to daily P"
is `LIMIT` even if you think the level is above the market. Do not check it against price data.

### `anchor_broker`
Broker time is **UTC+3**; the report's UK clock is BST (UTC+1), so **UK + 2 hours = broker**.
- "00:00 UK daily reset" → `02:00`
- "London open 08:00 UK" → `10:00`
- "US cash open" → `16:30`
- No time stated → `02:00` for a card that rests from the day boundary; otherwise the session open
  the card names. Record what you assumed in `notes`.

### Suppression
A card is `suppressed: true` only when the **report** declines it — conviction below the 0.25
threshold, a regime gate not met, an event blackout, no qualifying fib swing. Then set `direction`
to the side if the report names one (else `n/a`), leave `entry`/`stop`/`tp1`/`tp2`/`tp3`/
`card_R_points` as `null`, and put the report's stated reason in `notes`.
A card that is merely *flagged* (wide stop, event collision, single-source-indicative) is **live**,
not suppressed.

## Output

Write exactly one file, `cards/baseline/gold/by_date/<report_date>.json`, a JSON list of three
objects. Create nothing else. Then reply with one line per card:
`<card_id> <family> <direction> <entry_mode> entry=<x> stop=<y> R=<r> suppressed=<bool>`
and a second short paragraph listing anything ambiguous you had to resolve.
