# Trust Score — XAUUSD Gold_Report_09Jun2026.md (D = 2026-06-09) — run gold_regen_qa1

`last_bar_date` in `data/levels/XAUUSD_by_date/2026-06-09.csv` = 2026-06-08, which is < D. Leak-free, usable.

Report's claimed basis: "Spot XAU/USD (loco London)", §3 basis "Spot, immediate settlement (loco London)" — a
continuous 24h basis. All Category 3 external checks below use the level file's `_full` columns per brief §4
("use the basis the report itself claims"). `_cash` is shown alongside where it changes the verdict; here it
does not — every external failure below fails under both bases.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot loco-London, not COMEX (GC=F named "corroboration" only, never blended). USDX is first row of §10. As-of = Mon 08-Jun = D−1 ✓. Lookback 5 sessions (02–08 Jun) stated; 25-session window referenced only qualitatively (§9 "bottom third of 25-session range"), no explicit 25d figures used. USD/oz stated in §2. 7 sources in §4 (≥6 ✓). Ticks are used with a consistent implicit conversion (1 tick = $0.01/oz: $91→9,100 ticks, $47→4,700, $149→14,900, all exact ×100) but the tick size/name is never explicitly stated anywhere in the report body. | §2, §4, §10, §21b | 4 |
| 1.2 Coverage & currency consistent | Every date in §2/§4/§6/§13/§21 is D−1 or earlier for data, D for the session date. No unit drift — USD/oz used throughout, ticks used only inside cards with a consistent ratio. | whole report | 5 |
| 1.3 Audience & tone | "Senior Commodities Analyst — Precious Metals"; institutional register throughout, no retail tone. | header, §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including all four §13 sub-sections and all four §21 sub-sections. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a correctly-columned table (Session/O/H/L/C/RSI2/Source A/Source B/Validation). §11 daily pivots: full R5→S5 table (contains the required R3→S3) — compliant. §11 **weekly pivots: only R2→S2 given, R3/S3 missing.** §11 **monthly pivots: entire table absent** — no monthly P/R/S anywhere in the report, though the framework and the level file both carry it. | §6, §11 | 2 |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus; futures policy stated as "noted for direction only, not blended" (a valid alternative to a stated adjustment, and stated clearly). §8 is genuinely candle-by-candle. §9 gives persistence/overlap/VOLator explicitly. §7 chart headings are present but carry no caption or placeholder text at all under any of the five — brief §2.3 allows a caption/placeholder as sufficient evidence, but there isn't even that; not scoring the conversion itself, but the total absence of any caption is a minor gap. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 numbers carry a source or point to §4/§6/§13 (NFP, USDX, WGC demand figure with WGC named, CPI). One notable exception: §14's "VIX spiked ~+40% to ~21.5 Friday" carries no citation anywhere in §4/§13. | text | 4 |
| 3.2 Citations exist & contain data (3 spot-checked) | TradingEconomics (05 Jun, "lowest level of 2026 ... weekly decline of nearly 4%") — consistent with §6's Fri close 4,365. USAGOLD (08 Jun, "rate-hike odds surge to 72%") — consistent with §12's "72% odds of a December hike". CNBC (08 Jun, "strong jobs data boosts rate-hike bets") — consistent with the NFP narrative. All three named, dated, and used consistently elsewhere; none self-contradictory. No hallucination override triggered. | §4, §13a | 5 |
| 3.3 Calculations transparent | RSI2 for Mon 08-Jun reproduces exactly from the report's own last-3 closes (4,461→4,365→4,313, both losses, RS=0, RSI2=0 — matches the report's stated 0.0). Daily and weekly pivots reproduce exactly from the report's own stated H/L/C via the standard formulas (checked P/R1/S1/R2/S2/R3/S3 for daily, P/R1/S1/R2/S2 for weekly — all match to rounding). KER stated as a number (≈−0.76). **ATR14 is never stated anywhere as an explicit number** — it is only inferable from card arithmetic (Trade 1 stop = R1-resistance + 0.25×ATR ⇒ ATR≈108; Trade 1's "3×ATR" runner cap ⇒ ATR≈106.3; Trade 3A's stop/TP math ⇒ ATR≈108, self-consistent with each other but never disclosed as a figure). This omission is what causes the 3.3/3.4 defect flagged below. | §6, §11, §9 | 3 |
| 3.4 Numbers reconcile (internal **and** vs. level file) | **Internal:** D−1 close ($4,313) identical across §1/§3/§4/§6/§21b MARKET entry — no internal break. §11 daily pivots (P/R1/S1) match the values quoted on Trade 2's card. **External, vs. `XAUUSD_by_date/2026-06-09.csv` `_full` (report's own claimed basis):** Close 4,313 vs file 4,329.93 → diff $16.93 > 0.115×ATR14($11.34) → **FAIL**. Open 4,307 vs 4,328.48 → diff $21.48 > 0.20×ATR14($19.72) → **FAIL**. High 4,377.5 vs 4,353.35 → diff $24.15 > $19.72 → **FAIL**. Low 4,268.4 vs 4,268.65 → diff $0.25 → consistent (this is the only OHLC field that lands inside tolerance). Daily pivots: P diff $2.69 (consistent), R1 diff $5.03 (discrepancy band), but **S1 diff $19.27, R2 diff $26.99, S2 diff $21.61, R3 diff $29.33, S3 diff $43.57 — all five exceed the $11.34 failure threshold**. Weekly pivots: P diff $27.87 (FAIL), R1 diff $19.56 (FAIL), S1 diff $46.61 (FAIL), S2 diff $54.92 (FAIL); only R2 (diff $0.82) lands inside tolerance, apparently by coincidence. Monthly pivots cannot even be compared — the report has none. Implied ATR (~106–108) vs. `atr14_full` 98.62 is the one figure that stays inside the "consistent" band (~8–10% relative). This is not a small-gap pattern — it is a majority of the checkable Category-3 figures failing outright, with no fabrication detected, so this is recorded as multiple Category 3 failures rather than the hallucination override. | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8 ends "Bearish continuation" label; §9 ends "Trending Down — Strong"; §10 ends "CONFIRM"; §12 and §14 tag every line with a directional implication. Trade 1's own "Wide stop (>1×ATR) flagged" caveat is inconsistent with the card's own implied ATR (~106–108 > R=$91, so R is *not* >1×ATR by the card's own math) — a methodology-application slip that belongs here as well as under 3.3. | those sections, §21b Trade 1 | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism for each counter (USD pricing/real-yield channel for USDX; shared rate-repricing driver for S&P/DAX), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15 explicitly weighs the one genuine tension in the report — structural central-bank demand (bullish, long-horizon) against the cyclical hawkish-repricing case (bearish, near-term) — and states a balance. §9/§21a explicitly note "no conflict" between short- and medium-term reads and between §17 and §21a, which is accurate (both are bearish this session) rather than a reconciliation exercise. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence, conditional ("unless... surprises"), no hedge-stacking. Confidence stated explicitly as "Medium" in §3 and §18. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | §4 dates every source; §6/§11/§19 flag single-source-indicative H/L explicitly and exclude them from pivot inputs. | §4, §6, §11, §19 | 5 |
| 5.2 Assumptions up front | Futures-non-blend policy stated (§5); daily-open anchor override stated **both** on the Trade 1 card ("(overridden anchor)") **and** in §20 with the from/to values and the reason — this is the compliant handling the brief specifically asks reviewers to check for, and the report does it correctly. Single-source pivot propagation is carried into both Trade 1 and Trade 2 caveats. Gap: the ATR14 figure that several card computations depend on (§3.3 above) is never disclosed as an assumption/input, so a reader cannot verify the stop-sizing math without reverse-engineering it. | §21b, §19, §20 | 4 |
| 5.3 Red flags surfaced | §12 and §15 both carry a well-developed Risks list. §13d correctly identifies Wed 10-Jun CPI as the single highest-impact upcoming event, landing inside the horizon of all three trade cards. **None of the three cards' Caveats fields mention the CPI event collision** — Trade 1's caveats are wide-stop and indicative-supports only, Trade 2's is indicative pivots only, Trade 3A's is bounce-may-not-occur only. This specific linkage (13d → card caveats) is called out explicitly in the brief and is absent throughout. | §12, §15, §21b | 2 |
| 5.4 Restrictions honoured | No synthesised/interpolated price presented as sourced (§19 explicit). JM Bullion retail print correctly excluded rather than blended un-normalised. Futures held to corroboration-only, consistently (header, §5, §19). No bracketed variable names, no module codes (M1..M5), no internal framework name in the report body (checked by search — none found). Instrument common names used throughout. | whole report | 5 |

## 2. Category roll-up

| Cat | Rows avg | Level (rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (4+5+5)/3 = 4.67 | 5 | 1.00 | 20 | 20.00 | All Variables correctly and explicitly respected; only gap is an unstated (though consistently-used) tick size. |
| C2 Structure | (5+2+4)/3 = 3.67 | 4 | 0.85 | 20 | 17.00 | All Module-3-equivalent sections present and ordered; §6 is a real table; but §11's weekly pivots are missing R3/S3 and the monthly pivot table is absent entirely. |
| C3 Accuracy & evidence | (4+5+3+1)/4 = 3.25 | 3 | 0.65 | 25 | 16.25 | Internal arithmetic (RSI2, pivots-from-own-H/L/C) is sound and citations spot-check clean, but the majority of externally-checkable figures (D−1 open/high/close, five of seven daily pivots, four of five weekly pivots, and the entirely-missing monthly set) fail the level-file tolerance, and ATR14 is never stated as a number. |
| C4 Reasoning & judgment | (4+5+4+5)/4 = 4.5 | 4 | 0.85 | 20 | 17.00 | Pillars conclude, cross-asset mechanism is interpreted not listed, synthesis addresses the one real tension, language is calibrated; held to 4 (not 5) because Trade 1's "wide stop" caveat contradicts the card's own implied-ATR math, a card-construction reasoning slip that this category is charged with catching. |
| C5 Currency & transparency | (5+4+2+5)/4 = 4.00 | 4 | 0.85 | 15 | 12.75 | Data dated, anchor override logged compliantly on both the card and in §20, restrictions honoured; held down by the missing CPI-collision caveat on all three cards and the undisclosed ATR assumption. |

**Total = 20.00 + 17.00 + 16.25 + 17.00 + 12.75 = 83 → 83/100**

## 3. Band & override

- **Band: High Trust (75–89).**
- Hallucinated-source override: not triggered — all three spot-checked citations are named, dated, and internally consistent.
- Restriction-breach override: not triggered — no bracketed variable/module leakage, no synthesised price presented as sourced, anchor deviation logged as a non-conformance (not silently presented as the anchor) per the brief's explicit test.
- `override = none`

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-09.csv`)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-06-09_Trade_1 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-09_Trade_2 | Trade 2 - Pivot (TREND_DOWN, breakout-follow) | CLEAN | False |
| 2026-06-09_Trade_3A | Trade 3A - Momentum-Pullback (TREND_DOWN) | CLEAN | False |

Card Integrity per card = 100 − 40×0 − 10×0 = 100 (all three; no DUD, no WARN).
**Report-level Card Integrity = 100** (mean over 3 non-suppressed cards).

## Summary line

```
c1=5  c2=4  c3=3  c4=4  c5=4
total=83  band=High Trust  override=none
card_integrity=100  n_cards=3  n_duds=0  n_warns=0
```

See `qa/gold_regen_qa1/2026-06-09_feedback.md` for the numbered, actionable defect list.
