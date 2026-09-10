# Trust Score — Gold_Report_17Jul2026.md (D = 2026-07-17, RUN_ID = gold_regen_qa1)

Level file used: `data/levels/XAUUSD_by_date/2026-07-17.csv` — `last_bar_date = 2026-07-16 < date = 2026-07-17` ✓ leak-free, confirmed before use.
Report's claimed basis: "Spot, loco London, immediate settlement" / 24-hour market (§2, §3) → checked against **`_full`** columns throughout (cash-session `_cash` columns checked as a secondary cross-check where noted).

## 1. Section 7 checklist

| Row | Notes | Evidence | Score (0–5) | Action if below threshold |
|---|---|---|---|---|
| 1.1 Variables respected | Asset, LBMA loco-London, USDX mandatory counter, ≥6 sources (7 given), USD/oz, tick name/size all correctly stated and used consistently. **But** §5 states the CME futures read "carr[ies] full weight" and is one of exactly two reads the consensus price is built as "the centre of gravity of" — futures is used as a **primary, load-bearing consensus input**, not corroboration-only as the brief's restriction requires. One clear, explicit restriction breach. | §2, §4, §5 | 3 | List: futures-as-primary-input breach |
| 1.2 Coverage & currency consistent | Every date in §2/§4/§6/§13/§21 is D−1 (16 Jul) or earlier for data, D (17 Jul) for the session; no USD/oz-tick unit drift anywhere in the report. | whole report | 5 | — |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals register held throughout; institutional trading/risk framing; no retail tone. | §1, §18 | 5 | — |
| 2.1 Sections present & ordered | All 21 top-level sections present, correctly ordered, headings match spec (incl. §13a–d, §21a–d). | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a real table but uses a single "Corroboration" column ("Dual-source") instead of the specified Source A / Source B / Validation columns — less granular than spec, no data lost. §11: weekly and monthly tables are correctly R3→P→S3 (3-each-side); the **daily** table shows R5→P→S5 (5-each-side) instead of the specified 3-each-side — extra, not missing, information. | §6, §11 | 4 | — |
| 2.3 Method steps visible | §4–§5 show observation → normalisation → consensus with the futures-to-spot adjustment stated (15-pt carry); §8 is candle-by-candle; §9 gives regime + persistence + KER + VOLator explicitly; §7 charts suppressed with a disclosed reason per the accepted placeholder convention (not scored down). | §4–§9 | 5 | — |
| 3.1 Quantitative claims sourced | Nearly every figure in §1/§12/§14 carries a source or points to §4/§6/§13; a few macro claims (WGC "~15 consecutive years", central-bank accumulation) are attributed only loosely. | text | 4 | — |
| 3.2 Citations spot-checked (3) | CME futures row: named, dated, used consistently (§4→§5). Investing.com real-time row: named, dated, quote falls inside its own cited session range — consistent. TradingView row: labelled "16 Jul, close" in the Date/Time column but its own Notes describe it as an "earlier-session print… stale relative to NY afternoon" — the column label and the note contradict each other on what the quote actually is (not a genuine close). Sloppy, not impossible/fabricated — no override triggered. | §4 | 3 | Flag TradingView row's self-contradictory date/label for correction |
| 3.3 Calculations transparent | RSI2 (§6) reproduces exactly from the report's own 5 stated closes (verified: RS=12.80/35.19=0.364 → RSI2=26.7 ✓). All three §11 pivot tables reproduce exactly from the report's own stated H/L/C (verified for daily, weekly, monthly). ATR14 (62.50) is disclosed as an "estimate" without a shown 14-session derivation — the one genuine transparency gap. | §6, §11, §19 | 4 | — |
| 3.4 Numbers reconcile — internal AND external (level file) | **Internal:** D−1 close (3,990.00) identical across §1/§3/§4/§6/§21b MARKET entry ✓; §11 pivots match the cards ✓; ATR in §9/§19/§21 consistent (62.50) ✓. **External — fails on every checkable figure:** D−1 close 3,990.00 vs file 3,976.47 (`_full`), diff 13.53 > failure threshold 11.34; RSI2 26.7 vs file 8.21, diff 18.5 > 15; ATR14 62.50 vs file 98.645, 36.7% relative > 25%; daily pivots S1/S3 fail, P/R1/S2 in discrepancy band; **entire weekly pivot table fails** (diffs 13.0–88.9 vs 11.34 threshold); **entire monthly pivot table beyond P fails**, most by 150–340 points (root cause below). See §4 of the feedback file for the numbers. | cross-section + level file | 0 | Rebuild §6/§11 from the level file's `_full` series |
| 4.1 Pillars conclude | §8 ("DOWN, high conviction"), §9 (TREND_DOWN, confirms), §10 (per-row Confirms/Neutral/Contradicts + explicit flag) all reach clear conclusions; §12/§14 are directionally clear but end in narrative rather than an explicit direction label. | those sections | 4 | — |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per instrument (dollar-denomination, real-yield opportunity cost, silver as high-beta complex proxy, crude's second-order inflation-expectations channel) — genuinely interpreted, not a correlation list. | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | The crude/gold contradiction is flagged, explained (second-order rates channel dominating the first-order haven channel) and carried consistently into §15/§16/§18; KER vs regime explicitly checked and shown to agree; §17 and §21a point the same direction with no unflagged conflict. | §15–§18, §21a | 5 | — |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence stated as MEDIUM with an explicit two-part rationale (§3, §18); hedge language ("likely", "most plausible") used appropriately, not stacked. | §3, §17 | 4 | — |
| 4.5 Card construction (M5 rules, scored under C4 per brief) | Cards are structurally clean (linter: 0 DUD / 0 WARN — see §4 of this file) — three equal units, correct TP/stop ordering, BE-on-Unit-2 rule, anchor explicit and correctly converted (00:00 UK → 02:00 broker) on all three cards. **But** the volatility inputs feeding every card are materially wrong: ATR14 used (62.50) is 36.7% below the leak-free ATR14 (98.645), which understates every 0.25×ATR stop buffer by ~9 points. More seriously, Trade 3A's qualifying-swing check ("136.24 = 2.18×ATR, clears the 2× threshold" — M5 rule requires magnitude ≥ 2×ATR) does **not** clear 2× against the leak-free ATR14: 136.24/98.645 = 1.38×; even substituting the level file's true 5-day swing (4,134.83−3,969.30 = 165.53) gives 165.53/98.645 = 1.68× — still short of 2×. Under leak-free data, Trade 3A should not have qualified. | §21a, §21b, §20 | 2 | Rebuild ATR14 and re-check the 3A swing-qualification test against leak-free data |
| 5.1 Data dated; staleness flagged | Every price and article carries a date/time; single-source items (weekly/monthly pivots, DXY/SPX/VIX/WTI, DAX gap) are explicitly flagged as such throughout §11 and §19. | §4, §6, §13, §19 | 5 | — |
| 5.2 Assumptions up front | Futures-to-spot carry (15 pts) stated with its size; the daily-open anchor override is stated in §2 and logged in §20 with the same converted time (00:00 UK) carried onto every card; single-source pivot propagation into Trade 2's confluence stack is explicitly caveated on the card. One wrinkle: §20's anchor note says the override "resolves to the same value the instance already carried, so no behavioural change results" — self-contradictory as written (an override to an unchanged value is not an override), though harmlessly so since it is still logged and converted consistently everywhere. | §21b, §19, §20 | 4 | — |
| 5.3 Red flags surfaced | Crude contradiction and confluence-shelf thinness surfaced in §12/§15; the 17-Jul UMich event collision is carried explicitly onto all three §21b cards, not just mentioned in §13d. | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No bracketed variable names, module codes, or framework name anywhere in the body; retail FX-broker quotes excluded per the stated restriction (§4 footnote); OHLC basis not left un-normalised. **But** "futures corroboration-only" is openly breached (see 1.1) — futures is one of two full-weight primary inputs to the consensus number, not corroboration. | whole report | 1 | Restrict futures to corroboration-only in §5's weighting scheme |

## 2. Category roll-up

| Cat | Rows averaged | Mean | Level (rounded) | Override applied | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1–1.3: 3,5,5 | 4.33→4 | **3** | −1 level (restriction breach) | 0.65 | 20 | 13.00 | Variables otherwise solid; reduced one level for the futures-corroboration-only breach |
| C2 Structural alignment | 2.1–2.3: 5,4,5 | 4.67 | **5** | — | 1.00 | 20 | 20.00 | All 21 sections present/ordered; only minor table-format deviations |
| C3 Accuracy & evidence | 3.1–3.4: 4,3,4,0 | 2.75 | **3** | — | 0.65 | 25 | 16.25 | Sourcing/transparency strong; external reconciliation against the level file fails on nearly every checkable figure (3.4) |
| C4 Reasoning & judgment | 4.1–4.5: 4,5,5,4,2 | 4.00 | **4** | — | 0.85 | 20 | 17.00 | Strong pillar conclusions and synthesis; card construction undermined by wrong ATR / failed swing-qualification test |
| C5 Currency & transparency | 5.1–5.4: 5,5,5,1 | 4.00 | **4** | — | 0.85 | 15 | 12.75 | Excellent dating/assumption/red-flag disclosure; one open restriction breach (5.4) |

## 3. Total, band, override

c1=3
c2=5
c3=3
c4=4
c5=4
total=79
band=Moderate
override=restriction_breach

**Total = 13.00 + 20.00 + 16.25 + 17.00 + 12.75 = 79.00 → 79.**

Raw total (79) would map to High Trust (75–89) unmodified. **Restriction-breach override applies** (§5's consensus build uses CME futures as a full-weight primary input rather than corroboration-only — an open breach of the stated "futures corroboration-only" restriction), which caps the band at **Moderate Trust (60–74)** regardless of total, and requires C1 reduced by at least one level (applied above: 4→3). Hallucinated-source override was checked and **not** triggered — no cited source is fabricated or impossible; the TradingView row's self-contradictory label (3.2) is sloppiness, not fabrication.

## 4. Card Integrity (linter rows, copied verbatim — not re-derived)

| card_id | strategy | flags | dud | Card Integrity (100 − 40·#DUD − 10·#WARN) |
|---|---|---|---|---|
| 2026-07-17_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-07-17_Trade_2 | Trade 2 — Pivot (regime-aware), TREND_DOWN trend-continuation variant | CLEAN | False | 100 |
| 2026-07-17_Trade_3A | Trade 3A — Momentum-Pullback, 4-session lookback | CLEAN | False | 100 |

card_integrity=100
n_cards=3
n_duds=0
n_warns=0

(Card Integrity is a separate, deterministic score per the linter's static checks and is not part of the 100-point total above. Note: the linter's static checks do not verify the card's ATR/swing inputs against market data — see 4.5 above and the feedback file for the substantive, leak-free-data-derived defects the static linter cannot catch.)
