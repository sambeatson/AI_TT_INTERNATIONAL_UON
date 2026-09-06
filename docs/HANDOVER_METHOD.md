# Strategy-Card Scoring — Handover Note

**Purpose.** Score institutional research trade cards against M15 broker data to produce, per asset: a per-unit result ledger (CSV), a per-card summary (CSV), and an equity curve (PNG). One asset at a time.

**Status.** Method validated on 159 S&P 500 cards, 11 May – 31 Jul 2026, 54 sessions. Next: WTI, BTCUSD, EURUSD, USDX, and others.

---

## 0. Timezone — do this first, every time

**The `DateTime_UTC` column in the MT5 exports is mislabelled.** It is broker minus 2 hours, but the broker server is UTC+3, so the column is actually **UTC+1 (London BST)**, not UTC.

Verified empirically from tick-volume profiles across the project files:

| Asset | Peak mean TickVolume at broker time | Known event | Implied offset |
|---|---|---|---|
| US500 | 16:30 | US cash open 09:30 ET = 13:30 UTC | UTC+3 |
| XAUUSD | 16:30 | same | UTC+3 |
| UK100 | 10:00 | FTSE open 08:00 London = 07:00 UTC | UTC+3 |

**Correct mapping (BST period):**

```
broker time = true UTC + 3
broker time = UK clock + 2
```

**Mandatory verification step for every new asset file.** Do not trust either column label. Run:

```python
d['t'] = pd.to_datetime(d['DateTime_Broker']).dt.time
d.groupby('t')['TickVolume'].mean().sort_values(ascending=False).head(5)
```

Confirm the peak lands on the asset's known liquidity event (US cash open for equities and gold; London/NY overlap for FX; NYMEX pit open for WTI). If it doesn't, stop and resolve the offset before scoring anything. **Always index bars by `DateTime_Broker`, never by the `DateTime_UTC` column.**

> **Known impact on prior work.** The original S&P scoring pass (basis 1) converted anchors as `uk = DateTime_UTC + 1h`, which was one hour late. Bar-sequence resolution of stops and targets is unaffected — touch order does not depend on clock labels — but entry-bar selection was off by four M15 bars on card-anchored entries. The 06:45 and 08:45 rebases used `DateTime_Broker` directly and are correct as published.

---

## 1. Anchor translation

Cards state anchors in UK clock or ET. Convert to broker time before use:

| Card wording | Broker time |
|---|---|
| 00:00 UK (day-boundary anchor) | 02:00 |
| 07:00 UK (European pre-open) | 09:00 |
| 13:30 UK (pre-NY positioning) | 15:30 |
| 14:30 UK / 09:30 ET (US cash open) | 16:30 |
| 21:00 UK / 16:00 ET (NY cash close) | 23:00 |

## 2. Monitoring windows by asset class

Entry monitoring opens at the **card's own stated anchor** translated to broker time, and stays live until the asset's **last-opportunity cut-off**. If the required price is not available by the cut-off, the order expires unfilled.

| Asset class | Instruments | Monitoring opens | Last opportunity |
|---|---|---|---|
| Equity index | US500, UK100, NAS, EuroStoxx | card anchor (typically 09:00 or 16:30 broker) | **23:00 broker** |
| FX | EURUSD, USDX, GBPUSD | **09:00 broker** (= 07:00 UK) | **18:00 broker** |
| Energy / metals | SpotCrude (WTI), XAUUSD | card anchor | 23:00 broker |
| Crypto | BTCUSD | card anchor (24/7 feed) | 23:00 broker, same calendar day |

Where a card specifies its own timing explicitly, the card wins — that is the point of scoring the card as written. The table above is the default when the card is silent.

**Entry session** is the trading session *after* the report date, unless the card states same-session execution. For conditional/breakout cards, it is the session after the confirming daily close.

---

## 3. Dud screen (before any market data)

Reject the card outright, score 0R, and record the reason. These are card-construction faults, not market outcomes:

- **Stop on the wrong side of entry** — for a long, SL ≥ entry.
- **TP1 on the wrong side of entry** — e.g. a short whose TP1 sits above entry.
- **TP2 not beyond TP1** — including TP2 == TP1.
- **Zero risk distance** — entry == stop.

Record but still trade (flag only): **TP3 not beyond TP2** (inverted ATR-capped runner ladders are common and the runner simply caps out early).

*In the S&P sample this rejected 3 of 159 cards, all of which lost money on every other basis.*

---

## 4. Entry policy

Let `E` = card entry, `SL` = card stop, `Rc = |E − SL|`, `s = +1` long / `−1` short. Let `px` = open of the first bar at or after the monitoring anchor. Define improvement `imp = s·(E − px)/Rc` (positive means the market is offering better than the card).

**Acceptable entry band: `0R` to `+0.75R` of improvement.** That is, from the card entry up to 0.75R better. The 0.75R cap is the micro-R guard — it guarantees at least 0.25R of risk survives to the stop.

| Condition at anchor | Action |
|---|---|
| `0 ≤ imp ≤ 0.75` — price in band | **Take at market**, fill at `px` |
| `imp < 0` — price worse than entry | **Do not chase.** Rest at `E`; fill only if price returns to `E` before the cut-off. Fill price `E` |
| `imp > 0.75` — price beyond band (too close to or through the stop) | **Wait for recovery** to `E − 0.5R·s`; fill there if reached before the cut-off. Fill price is the recovery level |

**The stop never moves.** Always the card's original `SL`. Realised risk `Rr = |fill − SL|`, and all R-multiples are computed on `Rr`, not on `Rc`.

Take-profits are always the card's TP1/TP2/TP3 unchanged, regardless of fill improvement. A better fill therefore delivers a larger R-multiple on the same target — this is the whole point of the policy.

---

## 5. Resolution

- Three equal units. Unit 1 → TP1, Unit 2 → TP2, Unit 3 → runner.
- Units 1 and 2: first touch of target or stop, whichever comes first in bar order. Trace to resolution — no time limit unless the card specifies one.
- **Unit 3 exits at whichever of these fires first:** card-specified session-close time-stop (if the management text mentions "time-stop", "session close", or "cash close" — apply at the entry session's close), runner target, the breakeven trail, or the stop.
- **Breakeven trail** arms only on the *Unit 2 fill* (or on TP1 where the card says so). Level is `fill + s·0.2·Rr`. If TP2 is never reached, the trail never arms and Units 2 and 3 ride the original stop. This leak cost roughly 4R across the S&P sample — flag it per card.
- **Intrabar ambiguity:** if one M15 bar touches both stop and target, infer sequence from the bar's open — if the bar opened nearer the stop, assign the stop first. Record `INTRABAR SEQUENCE INFERRED` in the notes and report the conservative outcome.
- **Unresolved at end of data:** mark `OPEN_MTM` and value at the final close. Do not force a close.

---

## 6. R conventions

Report both, in adjacent columns:

- **Card R** — outcome measured from the card's stated entry, risk `Rc`. Answers *was the analysis right?*
- **Realised R** — outcome measured from the actual fill, risk `Rr`. Answers *would you have made money?*

They diverge whenever the card's stated entry was not a price the market was offering. Always carry `risk_vs_card = Rr / Rc`; anything below 0.25 should not exist under this policy, and anything below 0.5 warrants a flag.

---

## 7. Outputs per asset

**a. `<asset>_card_results.csv`** — one row per card × unit:

```
report_id, report_date, strategy, direction, card_entry, stop_loss, tp1, tp2, tp3,
card_R_points, management, entry_session, entry_rule, fill_status, fill_time_broker,
fill_price, R_points, risk_vs_card, unit, exit_price, exit_time_broker, exit_reason,
R, notes
```

`fill_status` ∈ {FILLED, NO FILL, NO TRIGGER, SUPPRESSED, REJECTED - DUD, UNPRICED}.
`entry_rule` records which of the three branches fired, with the improvement in R.

**b. `<asset>_card_summary.csv`** — one row per card, blended R across three units.

**c. `<asset>_equity.png`** — dark theme, 150 DPI, matplotlib `Agg` backend. Equity panel plus drawdown sub-panel. State the sizing assumption in the title. Fixed-dollar risk per card, not compounded, ordered chronologically by report date. Non-filled cards contribute 0R and no step.

Escape or avoid `$` in matplotlib title strings — it triggers mathtext and mangles the render.

---

## 8. Defect taxonomy to flag

From 159 S&P cards, 45 carried a construction defect (28%). Detect and label these automatically; they explain most of the loss:

| Defect | Test | Frequency |
|---|---|---|
| **Stale anchor** | `abs(fill − E) > 15` points, entry reference is a prior close | most common |
| **Misplaced limit** | long limit above market at anchor / short limit below | ~15 cards |
| **Misplaced stop-entry** | long stop-entry below market / short above | ~12 cards |
| **Malformed order** | stop on the wrong side of the actual fill | 9 cards |
| **Micro-R** | `Rr < 0.25·Rc` — stop too near the fill to survive noise | 14 cards pre-policy |
| **Unreachable target** | `Rc` sized to the 3.5×ATR cap, then TPs set at ±1R/±2R off it | several |
| **Ladder inversion** | TP3 < TP2 (ATR-capped runner vs R-derived TP2) | several |
| **Duplicate cards** | two cards in one report, or across consecutive reports, with identical entry/stop/targets | 2 pairs |

---

## 9. Sizing

R-scaling is linear, so the equity curve shape is fixed and only the axis changes.

On the S&P sample, the best basis (−9.40R over 71 fills, 22 winners / 49 losers) gives:

| Risk per card | Final on 1,000,000 | Max drawdown |
|---|---|---|
| 2.5% (25,000) | 765,050 | −51.7% |
| 1.0% (10,000) | 906,020 | −25.9% |
| 0.25% (2,500) | 976,505 | −7.4% |

With a hit rate near 30% on blended cards, 2.5% per card is not survivable through the observed loss clustering. Model at 0.25–1.0% and treat 2.5% as a stress case.

---

## 10. Per-asset execution checklist

1. Verify broker offset from the tick-volume profile. Record it.
2. Confirm session boundaries (first/last bar time) and the number of sessions in the file.
3. Extract cards: entry mode, entry, stop, TP1–3, stated R, management text, direction, suppression status.
4. Run the dud screen. Log rejections.
5. Determine entry session and anchor per card; apply the asset's monitoring window and cut-off.
6. Apply the entry policy. Record which branch fired and the improvement in R.
7. Resolve all three units. Honour card-specified runner time-stops.
8. Emit ledger CSV, summary CSV, equity PNG.
9. Report: total R, fill rate, win/loss, defect count by type, best and worst cards, month-by-month totals.
10. Flag anything the data cannot settle rather than estimating it.
