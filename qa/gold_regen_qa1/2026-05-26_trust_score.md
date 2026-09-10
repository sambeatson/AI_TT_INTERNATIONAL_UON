# Trust Score — XAUUSD — 2026-05-26

Report: `reports/md/Gold_Report_26May2026.md` · Run: `gold_regen_qa1` · Reviewer basis claimed by
report: **spot, loco London, continuous (24h)** → checked against `_full` columns of
`data/levels/XAUUSD_by_date/2026-05-26.csv` (`last_bar_date`=2026-05-25 < D=2026-05-26, confirmed
leak-free before use). `atr14_full` = 98.6564.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score | Action |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/units/sources/lookback all correct (XAU/USD loco London not COMEX; USDX first counter in §10; 5d/25d lookback; ≥6 sources; tick=0.01 used consistently as "ticks"). But the daily-open anchor handling is self-contradictory: the card and §20 both label the anchor "00:00 UK" while simultaneously calling it "overridden for this run" without ever stating what the override changed the anchor *to* — it never actually switches to a different clock time, it substitutes the 25 May close as an entry-price *proxy* because the true 26 May 00:00 UK open doesn't exist yet at compile time. Calling a price-proxy substitution an "anchor override" conflates two different things the M1 module treats separately, and risks the override being read as a non-conformant anchor value when it is not one. | §20 "Daily-open anchor" row; §21b Trade 1 Entry field | 3 | List anchor-handling as the Variable not cleanly respected; regeneration must either (a) state plainly "anchor = 00:00 UK, unchanged; entry priced off 25 May close as a stated proxy because the true open has not printed" with no use of the word "override," or (b) if a genuine anchor change is intended, name the new clock time explicitly on the card. |
| 1.2 Coverage & currency consistent | Every date used is D-1 (25 May) or earlier for data, D (26 May) for the session; no USD/oz vs ticks/points drift found. | whole report | 5 | — |
| 1.3 Audience & tone | Senior Commodities Analyst register maintained throughout §1, §18; no retail tone. | §1, §18 | 5 | — |
| **Category 1 avg** | (3+5+5)/3 = 4.33 → **4** | | | |
| 2.1 Sections present & ordered | All §1–§21 present in the specified order, including §13a–d and §21a–d. | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a real table (9 cols: Date/O/H/L/C/RSI2/Trend/Sources/Outcome) — functionally equivalent to the Source A/B/Validation spec but collapses two source columns into one and uses "Outcome" for validation status. §11 pivot tables are correctly ordered top-to-bottom but the daily table shows 5 levels each side (R5…S5) rather than the spec's 3 (M1 default `PIVOT_ABOVE_BELOW_DAILY`=3) — extra, not missing, information, so non-material. | §6, §11 | 4 | Convert §6 to the named Source A/Source B/Validation columns for exact conformance. |
| 2.3 Method steps visible | §4→§5 shows observation→normalisation→consensus with the futures-to-spot adjustment stated (see 3.3 gap on its size); §8 full candle-by-candle; §9 regime with persistence/overlap/VOLator/Kaufman; charts have captions (image loss from docx→md conversion, per brief not scored). | §4–§9 | 5 | — |
| **Category 2 avg** | (5+4+5)/3 = 4.67 → **5** | | | |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims carry a source or point to §4/§6/§13. But the §6 Open/High/Low fields used for 25 May (4,509.38 / 4,602.30 / 4,505.10) have **no per-field citation anywhere in the report** — §4 sources only the *close*. The PBoC "17th consecutive month" streak and "market pricing assigns only a small probability of a cut" (§14) are also unsourced (no dataset/survey named). Combined with the OHLC accuracy failure below, this is a material sourcing gap, not a trivial one. | §6, §12, §14 | 2 | Cite a specific source and time for the 25 May H/L (not just the close); name the survey/futures-implied-probability source behind the Fed-cut-odds claim. |
| 3.2 Citations exist & contain data | Spot-checked USA Gold (25 May close 4,562.69 — used consistently in §1/§3/§4/§6/§21b), Trading Economics (22 May close 4,516.75 — used consistently in §4/§6), IFC Markets (25 May 4,571.04, §4 only). All three are named, dated, and used consistently; no self-contradiction or impossible date found; no fabrication detected. | §4, §6 | 4 | — |
| 3.3 Calculations transparent | RSI2 for 25 May (100.0) reproduces exactly from the report's own five stated closes (last two changes both gains → RS→∞ → RSI=100, matching the report's own saturation note). Daily pivot P = (4,602.30+4,505.10+4,562.69)/3 = 4,556.70 reproduces exactly. §21a direction score (0.25+0.10+0.00+0.03+0.06+0.05 = 0.49) is shown and correct. But: ATR(14)=95.06 is stated with no derivation shown (no TR series), and the futures-to-spot **contango adjustment is never quantified** — §5 says the CME June 4,655.35 print was normalised to "roughly USD 4,560" without ever stating the USD amount subtracted (≈USD 95, well outside the ≈USD 10–25 typical range this run's own convention assumes), so the size of a material assumption is not disclosed as the rules require. | §6, §11, §21a; §5 | 3 | Show the ATR(14) derivation (or at minimum the 14-session TR values feeding it); state the futures-basis adjustment as an explicit USD figure, not "roughly." |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally** the D-1 close (4,562.69) is identical across §1/§3/§4/§6/§21b; §11 pivots match the cards; §21 ATR matches §20 — clean. **Externally, against `XAUUSD_by_date/2026-05-26.csv` (`_full`), this is the dominant failure of the report:** 25 May Open/High/Low are all Category-3 failures (Open diff USD 33.88 > 19.73 threshold; High diff USD 22.34 > 19.73; Low diff USD 35.99 > 19.73); only the Close (diff USD 8.24) lands in the discrepancy-to-record band, not a failure. This drags six of seven **daily** pivot levels into failure (R1 diff 21.39, S1 diff 36.94, R2 diff 51.04, S2 diff 65.62, R3 diff 79.72, S3 diff 95.27 — all > USD 11.35 threshold; only P at 7.29 lands in the discrepancy band) even though the report labels every daily pivot "Corroborated" — the opposite of what the file supports. RSI2 (100.0 vs file 63.74 full / 64.39 cash) diverges by ~36 points, far past the 15-point failure line. The 25-session swing high used to justify Trade 3C's suppression (USD 4,889.70) diverges from the file's swing_high_25d_full (USD 4,833.05) by USD 56.65 — a clear factual error, though it happens not to change the suppression conclusion. By contrast: monthly pivots match the file almost exactly (largest diff USD 1.75, all consistent); weekly pivots are mostly consistent-to-discrepancy (only S3 fails, diff USD 13.28); the 5-day and 25-day swing **lows** match closely (diff USD 0.51). So the failure is localised and severe: the 25 May daily OHLC specifically, and everything computed from it. | level file cross-check | 1 | See feedback file — regenerate the 25 May daily OHLC from a sourced, corroborated feed and rebuild all daily pivots and RSI2 from the corrected values; re-label daily-pivot corroboration status only after that. |
| **Category 3 avg** | (2+4+3+1)/4 = 2.5 → tie, resolved to the **lower** level per framework §9 ("pick the lower rubric level when in doubt") → **2** | | | |
| 4.1 Each pillar reaches a conclusion | §8 "Bullish continuation (early-stage)"; §9 Transitional with an explicit bias statement; §10 "Aggregate cross-asset read: MIXED"; §12 each factor bold-tagged supportive/negative/cyclical; §14 each subsection ends in an implication. All conclude. | §8–§10, §12, §14 | 5 | — |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit causal mechanism per counter (USDX/SPX/DAX/Silver), not a bare correlation list, and explains why the equity reads are "mixed" rather than contradictory (shared catalyst, not rotation). | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §9, §13b, §16, §21a all explicitly carry forward and do not paper over the short-term-bullish vs. Kaufman-trending-down tension; §17 vs §21a agree and the report says so. | §15–§18, §21a | 5 | — |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge-stacking; confidence stated H/M/L (§3 "Medium"); "likely/modest/contingent" language used appropriately throughout. | §3, §17 | 5 | — |
| Card construction (M5, feeds Category 4) | Trade 1: stop, TP1/TP2, BE-trail and runner logic all reproduce exactly from the stated rule and the report's own ATR (95.06); thesis invalidation correctly kept distinct from the stop. Trade 2: TRANSITION-regime breakout-side-only rule correctly applied (no counter-side limit); entry/stop/TP arithmetic (P+0.10×(R1−P), P−0.8×(P−S1)) all reproduce exactly. One genuine construction wrinkle: Trade 2's "Buy-stop" at USD 4,561.86 sits USD 0.83 *below* the report's own stated D-1 close (4,562.69) — a buy-stop is conventionally a resting order above the reference price to catch a breakout; placed below it, the order would in practice already be marketable, not a stop. This is a formula-driven edge case (small R1−P spread), not a fabrication, and the linter's static correct-side check did not flag it — noted here as a Category-4 reasoning nuance, not a Card Integrity defect. | §21b; `cards/baseline/gold/by_date/2026-05-26.json` | 4 | State explicitly why a sub-close "buy-stop" is still a valid breakout order in this construction, or move the trigger above the close. |
| **Category 4 avg** | (5+5+5+5+card-construction note pulls the applied level to)  → **4** (Strong — see card-construction note; framework §9 favours the lower level when a genuine, if minor, mechanical question is open) | | | |
| 5.1 Data dated; staleness flagged | Every price/article dated; 19–21 May single-source intraday H/L explicitly flagged indicative. | §4, §6, §13, §19 | 5 | — |
| 5.2 Assumptions up front | Futures-to-spot normalisation is stated qualitatively (§5) but its size is never given as a number (see 3.3); the anchor-override disclosure is present in the card, §20 and §21b but is internally ambiguous about what changed (see 1.1); single-source pivot propagation into the Trade 2 caveat is done correctly. | §21b, §19, §20 | 3 | Same fixes as 1.1 and 3.3. |
| 5.3 Red flags surfaced | §12/§15 carry the Kaufman disagreement, dollar-reversal risk, and confluence-shelf-loss risk; §13d's 28 May GDP/claims collision is carried into both live cards' caveats. | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No module codes (M1–M5) or framework name appear in the body; instrument common names used throughout; GC=F correctly kept Directional/corroboration-only, never Core; retail bullion premia excluded per §5. The only softness is the unsourced §6 Open/High/Low noted at 3.1, which sits close to (but does not clearly cross into) presenting an unsourced figure as sourced. | whole report | 4 | — |
| **Category 5 avg** | (5+3+5+4)/4 = 4.25 → **4** | | | |

## 2. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification (one line) |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | 4 | 0.85 | 17.00 | All Variables respected except a self-contradictory anchor-override disclosure. |
| 2 | Structural alignment | 20 | 5 | 1.00 | 20.00 | All §1–§21 sections present, correctly ordered; scorecard/pivot tables real tables. |
| 3 | Accuracy & evidence | 25 | 2 | 0.40 | 10.00 | 25 May Open/High/Low, RSI2, and 6/7 daily pivot levels all fail the level-file tolerance despite being labelled "Corroborated"; monthly/weekly pivots and swing lows are largely sound. |
| 4 | Reasoning & judgment | 20 | 4 | 0.85 | 17.00 | Pillars, synthesis and card mechanics are all strong and rule-compliant; one Trade 2 order-type nuance (buy-stop sub-close) kept it off a 5. |
| 5 | Currency & transparency | 15 | 4 | 0.85 | 12.75 | Dating and red-flag surfacing are strong; the futures-basis size and anchor-override wording are the two disclosure gaps. |

**Total = 17.00 + 20.00 + 10.00 + 17.00 + 12.75 = 76.75 → 77 / 100**
**Band: High Trust (75–89)**

## 3. Override check

- Hallucinated-source override: **not triggered.** Three-citation spot-check (USA Gold, Trading Economics, IFC Markets) found each named, dated, and used consistently; no source is impossible or self-contradictory.
- Restriction-breach override: **not triggered.** No explicit prompt restriction (no synthesis, no module names, futures corroboration-only, instrument common names) is openly violated; the unsourced §6 O/H/L (3.1) is a gap, not a clear breach of a stated restriction.
- `override = none`

## 4. Card Integrity (separate score — linter rows copied verbatim, not re-derived)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-05-26_Trade_1 | Trade 1 - Daily Directional (LONG) | CLEAN | False |
| 2026-05-26_Trade_2 | Trade 2 - Pivot, regime-aware (TRANSITION → breakout side, LONG) | CLEAN | False |
| 2026-05-26_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION) | SUPPRESSED | False |

Per-card score = 100 − 40·(#DUD) − 10·(#WARN), floored at 0: Trade 1 = 100, Trade 2 = 100 (Trade 3C
suppressed, excluded from the mean per protocol).

**card_integrity = 100** (mean of the 2 non-suppressed cards) · **n_cards = 3** · **n_duds = 0** · **n_warns = 0**

---

## Score summary
```
c1=4
c2=5
c3=2
c4=4
c5=4
total=77
band=High Trust
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
