# Stage 2 (design v2) — regenerate the S&P 500 trade cards for ONE date, ONE draw

You are one of up to 171 independent sessions (57 dates × 3 draws). You rebuild the three trade cards
the report for date D *should* have issued, using (a) the quality-assurance feedback on that report and
(b) the **real market data up to 23:59 the night before D** — and nothing that happened on or after D.

## What changed from the first regeneration run, and why it matters to you
The first run let sessions start from the report's own price figures. Quality assurance has since shown
those figures are the main problem: pivot tables built from the wrong session, week or month; ATR
understated by a third or more; RSI2 that does not reproduce. So in this run **every price level comes
from the level file, never from the report.** The report contributes its *reading* of the market — regime
call, narrative, sentiment, event calendar — not its numbers.

## Read, and nothing else
| file | use |
|---|---|
| `reports/md/<REPORT_FILE>` | the report for D: regime call, narrative, sentiment (§13), event calendar. **Not its price levels.** |
| `qa/regen_20260906_qa1/<D>_feedback.md` and `<D>_trust_score.md` | what was wrong with the report's cards and why |
| `data/levels/US500_by_date/<D>.csv` | **AUTHORITATIVE.** Prior-session OHLC, ATR14, RSI2, daily/weekly/monthly floor pivots, 5d/25d swings, on cash (`_cash`) and full-day (`_full`) bases. Computed only from bars strictly before D. Check `last_bar_date` < D. |
| `data/slices/US500/US500_upto_<D-1>.csv` | the M15 bars behind that file, if you need a swing timestamp or a figure the level file lacks |
| `data/slices/VIX/VIX_upto_<D-1>.csv`, `data/slices/NEWS/news_upto_<D-1>.csv` | volatility context; the news slice includes D's *scheduled* events with actuals blanked |
| `modules/` | the fixed rules, especially `M5_Strategies_Module_v2_1.md`. This run uses the module set at commit `f69b2cd`. |
| `cards/schema/card_schema.json` | the output contract |

## Never open
`cards/baseline/` (any date — you are producing an independent set) · `cards/regenerated/` other than
writing your own one file (no other draw, no other run) · `results/` · `data/raw/` · `docs/ENTRY_POLICIES.md`
and `README.md` (they quote past outcomes) · any report, slice, level file or QA file for any date other
than D · the web. **You do not know what the market did on or after D. Do not speculate.**

**Never list a directory under `data/`, `qa/`, `reports/` or `cards/`** (no `ls`, `os.listdir`, `glob`):
open only the exact paths in the table above with `<D>` / `<D-1>` substituted. Those folders hold files
for later dates, and listing one and opening the first entry is how a session sees the future.

## Basis — fixed for every session so the draws are comparable
- Pivot tiers, ATR14, RSI2 and swing extremes: the **`_cash`** columns (the S&P cash session,
  16:30–23:00 broker, as M3 defines it for an index).
- A MARKET entry: **`prev_close_full`** — the last executable price before D.
- Broker time = UK + 2 hours (= UTC+3; verified from the 16:30 volume peak at the US cash open). The
  slice's `DateTime_UTC` column is **mislabelled** — it is broker − 2h, i.e. UK time, not UTC. Ignore it;
  use `DateTime_Broker` only. 00:00 UK = 02:00 broker; 07:00 UK = 09:00 broker; US open = 16:30 broker.
- `anchor_broker` on every card. Trade 1 default **09:00** (07:00 UK, the S&P instance's daily-open
  anchor) unless the report's own logic argues for 02:00 or 16:30 — then say why in `rationale`.
  (Cards will be tested at several entry times regardless; the anchor matters only for the as-written test.)

## Building the cards (M5 rules bind — they are not suggestions)
1. **Direction score (§21a).** Recompute it. Price-derived components (technical bias, RSI2, regime,
   cross-asset if derivable from the slices) come from the real data. The sentiment component comes from
   the report's §13 — you cannot verify news, so carry it and say so. Record every component and the sum.
   |score| < 0.25 → Trade 1 is **suppressed**.
2. **Regime fork.** TREND → Trade 3A; RANGE → 3B; TRANSITION → 3C. Trade 2 follows the regime branch
   (TRANSITION → breakout side only). State the regime and why.
3. **Gates bind.** A swing that fails the 2×ATR qualification means no 3A card. A 3C needs a confirmed
   close beyond the 25-day boundary by ≥ 0.25×ATR. If a gate fails, emit the card with `suppressed: true`
   and the reason. A logged gate failure that still produces a live card is a defect.
4. **Construction.** Three equal units; TP1 = ±1R and TP2 = ±2R for Trade 1 and RANGE Trade 2; on the TP2
   fill, Unit 3's stop moves to entry ± 0.2R **in the profitable direction** (for a SHORT that is *below*
   entry); stop buffers 0.25×ATR beyond structure; stop capped at 3.5×ATR.
5. **Static integrity — mandatory.** Stop on the correct side; TP1 beyond entry; TP2 beyond TP1; TP3 beyond
   TP2 or `null`; 0.3×ATR14 ≤ R ≤ 3.0×ATR14; TP1 within 2.5×ATR14 of entry; LIMIT/STOP levels on the
   correct side of `prev_close_full`.
6. **Never "basis-shop".** Do not switch a level to a weekly or monthly tier just to clear a risk floor. If
   the honest construction fails a floor, the card is suppressed.

Before saving, lint your cards: write them to a temporary CSV with the registry columns and run
`python engine/linter.py --cards <tmp.csv> --out <tmp_out.csv>` (no `--data`). **Zero DUD flags.** Fix and re-lint.
**Do all scratch work — temp CSVs, helper scripts, anything — inside your own folder**
`/tmp/claude-0/s_<D>_d<K>/` (create it). Many sessions run at once; a shared filename means you may
read, run or overwrite someone else's work. (Every card is re-linted centrally
afterwards regardless, so this check is for your own correctness, not the final gate.)

## Output — exactly one file
`cards/regenerated/sp500_regen2/draw<K>/by_date/<D>.json` — a JSON list of three records. Fields: every
registry column (`card_id`, `report_date`, `report_file`, `strategy`, `family`, `direction`, `entry_mode`,
`entry_mode_text`, `anchor_broker`, `entry`, `stop`, `tp1`, `tp2`, `tp3`, `card_R_points`, `be_rule`,
`runner_rule`, `management_text`, `suppressed`) plus:
`source` = `"regen_sp500_regen2_draw<K>"`, `draw` = K, `module_sha` = `"f69b2cd"`,
`levels_file`, `slice_file`, `last_bar_broker` (from the level file's `last_bar_date` / the slice's last bar),
`direction_score`, `direction_components` (object), `regime`, and `rationale` (the derivation of every
level: which column, which formula, which swing with its bar timestamp).

`card_id` = `<D>_Trade_1`, `<D>_Trade_2`, `<D>_Trade_3A|3B|3C`. A suppressed card keeps `family` and
`direction` (or `n/a`) and sets every price field and `card_R_points` to `null`.

Do **not** write anywhere else, append to any CSV, or commit — many sessions run at once; assembly is central.

## Reply (under 8 lines)
One line per card: `<card_id> <direction> <entry_mode> entry=<x> stop=<y> R=<r> suppressed=<bool>`,
then `score=<s> regime=<r>`, then one line on the most consequential change versus the original report.
