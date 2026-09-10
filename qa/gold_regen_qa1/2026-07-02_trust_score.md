# Trust Score — Gold_Report_02Jul2026.md (D = 2026-07-02, run gold_regen_qa1)

Level file used: `data/levels/XAUUSD_by_date/2026-07-02.csv` — `last_bar_date=2026-07-01 < 2026-07-02` (checked, leak-free).
Report claims a continuous/loco-London spot basis (§2 "Global 24-hour market", "OTC London spot, T+2"; §3 "Spot, loco London") → checked against the `_full` columns per brief §4. `atr14_full = 111.6736`.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly scoped as spot XAU/USD with CME futures corroboration-only, normalised (§2, §5 ~$15 carry) — compliant. USDX mandatory first counter present (§10). As-of date correct (D−1 close). Lookback stated "~23-session" not the fixed 25-session medium block (§2), undisclosed as a deviation. **Tick size/name never stated anywhere in §2** despite §21 strategy cards being produced (M1 requires this). Daily-open anchor handling fails the module's own test (see below). | §2, §20, §21b | 2 | List: tick size/name missing from §2; anchor override not logged as a non-conformance from a stated original value; lookback stated as ~23 not 25 sessions, undisclosed |
| 1.2 Coverage & currency consistent | All dated items are D−1 or earlier for data, D for the session; USD/oz used consistently in narrative sections; no unit drift outside the cards | whole report | 4 | none material |
| 1.3 Audience & tone | Institutional register throughout, sign-off "Senior Commodities Analyst — Precious Metals" (§1, footer); no retail tone | §1, footer | 5 | none |
| 2.1 Sections present & ordered | §1–§21 all present, correctly ordered, with §13a–d and §21a–d subsections all present | headings | 5 | none |
| 2.2 Scorecard as a table | §6 is a table but uses Date/Open/High/Low/Close/RSI2/Trend/Validation — **Source A/Source B are pushed into a footnote, not table columns**, against the required Session/O/H/L/C/RSI2/Source A/Source B/Validation layout. §11 pivot tables show 5 levels/side (R5…S5) rather than the specified 3 (R3→P→S3), though correctly ordered high-to-low | §6, §11 | 3 | Convert §6 to the required column set; note the pivot-table tier count deviates from spec |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus with the futures-to-spot adjustment stated; §8 gives candle-by-candle commentary; §9 gives regime with persistence/overlap/VOLator; charts are captions/placeholders only, which the brief accepts as the docx→md conversion artefact | §4–§9 | 5 | none |
| 3.1 Quantitative claims sourced | §4/§6/§13 figures are sourced. Several §1/§12/§14 macro figures repeated report-wide (Fed hike odds ~67%, USDX ~101.2, 10Y ~4.47%) carry **no source name/date pointer** anywhere they appear | §1, §12, §14 | 3 | Flag unsourced macro figures for a citation pointer |
| 3.2 Citations exist & contain data | Spot-checked WGC 89% (reused §12+§13a, consistent), TradingEconomics 11% Q2 decline (reused §1+§13a, consistent), Goldman Sachs $4,900 target (named/dated but its figure is not reused/corroborated anywhere else in the report) | §4, §13a | 3 | Corroborate or drop the isolated Goldman Sachs figure |
| 3.3 Calculations transparent | RSI2 for 01 Jul reproduces from the report's own stated closes (two down days → RS=0 → RSI2=0, verified). Daily pivot table reproduces exactly from the report's own stated OHLC (P/R1–R3/S1–S3 all check out). **ATR(14) is never stated as a number anywhere in the report** despite being required and used implicitly in stop/cap logic. §21a gives only the final signal×weight contributions, not the underlying signal values, so the "Σ signal×weight" arithmetic cannot be checked | §6, §11, §9, §21a | 2 | Add an explicit ATR14 figure; show signal values feeding §21a, not just weighted contributions |
| 3.4 Numbers reconcile — incl. vs level file | Internally: D−1 close ($3,989.09) is identical across §1/§3/§4/§6 — consistent. **Externally, against `2026-07-02.csv` (`_full` basis):** D−1 Open $4,006.20 vs $4,012.31 (Δ$6.11, consistent) and Low $3,960.25 vs $3,960.17 (Δ$0.08, consistent) — but **Close $3,989.09 vs $4,031.08 (Δ$41.99 = 0.376×ATR, FAIL)**, **High $4,009.95 vs $4,115.53 (Δ$105.58 = 0.945×ATR, FAIL)**, **daily pivot P $3,986.43 vs $4,035.5933 (Δ$49.16, FAIL)**, and **RSI2 0.0 vs 72.0994 full / 100.0 cash (Δ72.1 / Δ100, both FAIL)**. Weekly pivots are close (P Δ$2.83 consistent; R1/S1 Δ~$5.4, discrepancy band) and monthly pivots are essentially exact (P Δ$0.03, R1 Δ$1.10, S1 Δ$0.52, all consistent) — so only the current-session (D−1) OHLC and everything derived from it (RSI2, daily pivots) is badly wrong; longer-horizon data is accurate | cross-section + level file | 1 | Re-source the 01 Jul H and C; recompute RSI2 and the daily pivot table from corrected OHLC |
| 4.1 Pillars conclude | §8/§9/§10/§12 each end in a clear direction label; §14 ends on a watch item rather than an explicit direction label. Trade 2 is labelled "regime-aware, TRANSITION" but its own construction (limit-fade sell at R1) contradicts the M5 rule for a TRANSITION regime card (breakout-side only) — an unsupported conclusion | those sections, §21b | 3 | Add an explicit §14 direction label; rebuild Trade 2 as a breakout-side card consistent with TRANSITION |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (USD cost-of-carry, equity risk-on eroding defensive demand, silver as high-beta PM proxy), not a bare correlation list | §10 | 5 | none |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address the short/medium tension and the KER-vs-overlap tension reasonably. Trade 3A is internally unreconciled: stated entry $3,982.00 and stop $4,010.00 give a $28.00 distance, but the card states R = $66.00 "from the trigger" ($3,944.00) — a different price than the stated entry, so the card's own R does not match its own entry/stop | §15–§18, §21b | 2 | Recompute Trade 3A's R from its stated entry and stop, not from the breakout trigger |
| 4.4 Calibrated language | §17 is one sentence with a stated conditional alternative (acceptable). §3/§18 state Medium confidence. §1 headline calls the tone "decisively bearish" while §21a's own composite score (−0.2) sits inside the neutral band (threshold 0.25) and is explicitly why Trade 1 is suppressed — the headline framing overstates the quantitative composite | §1, §21a | 3 | Soften §1's "decisively bearish" framing to match the near-neutral composite score, or explain the gap |
| 5.1 Data dated; staleness flagged | Price/article rows in §4/§6/§13 are dated; §11 and §19 flag pivot/OHLC rows as indicative given wide cross-feed dispersion. Recurring macro figures (USDX 101.2, 10Y 4.47%) lack a date/source tag | §4, §6, §13, §19 | 4 | Date-tag the recurring macro figures |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with size (~$15, within the expected $10–25 range) — compliant. **Daily-open anchor**: §2 and §20 state "override applied ... to 00:00 UK ... for this run per instruction" without ever naming the populated instance's original anchor value being deviated from, and frame it as a per-run selection rather than a logged non-conformance from a stated value — the module explicitly prohibits presenting a re-selected anchor "to suit when an analysis happened to finish" as if it were the anchor | §21b, §19, §20, §2 | 2 | Restate the anchor override as a logged non-conformance naming the value it deviates from, per M1 §H.1 |
| 5.3 Red flags surfaced | §12/§15 surface ETF-outflow, thin-liquidity and geopolitical risks; §13d NFP collision is carried into both card caveats (§21b) | §12, §15, §21b | 4 | none |
| 5.4 Restrictions honoured | No bracketed variable names or module codes appear in the body (checked, clean); futures kept corroboration-only; the Vantage CFD retail read is correctly excluded from the core comparable set, not left un-normalised. However §6 labels the 01 Jul row "Corrob. (Δ<$6)" — a validation claim the level-file cross-check (row 3.4) does not support for that row's High/Close, so the stated confidence overstates what was actually corroborated | whole report | 3 | Do not label a row "Corrob." at a tight delta unless the H/L/C used are independently confirmed against an execution feed |

## 2. Category roll-up

| Cat | Rows (score) | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1=2, 1.2=4, 1.3=5 | 3.67 | 4 | 0.85 | 20 | 17.00 | Asset/sources/counters compliant; tick declaration missing and anchor override mishandled |
| C2 Structure | 2.1=5, 2.2=3, 2.3=5 | 4.33 | 4 | 0.85 | 20 | 17.00 | All sections present and ordered; §6/§11 table shapes deviate from spec |
| C3 Accuracy & evidence | 3.1=3, 3.2=3, 3.3=2, 3.4=1 | 2.25 | 2 | 0.40 | 25 | 10.00 | D−1 High and Close, RSI2 and the daily pivot table are all badly wrong against the level file; weekly/monthly pivots are accurate |
| C4 Reasoning & judgment | 4.1=3, 4.2=5, 4.3=2, 4.4=3 | 3.25 | 3 | 0.65 | 20 | 13.00 | Pillars mostly well-argued, but Trade 2's construction contradicts its own regime label and Trade 3A's R does not reconcile with its own entry/stop |
| C5 Currency & transparency | 5.1=4, 5.2=2, 5.3=4, 5.4=3 | 3.25 | 3 | 0.65 | 15 | 9.75 | Assumptions mostly stated, but the daily-open anchor override is not logged as a non-conformance, and a row is over-labelled "Corrob." |

## 3. Total, band, override

c1=4
c2=4
c3=2
c4=3
c5=3
total=67
band=Moderate
override=none
card_integrity=95
n_cards=3
n_duds=0
n_warns=1

Override check: no cited source found fabricated/self-contradictory on spot-check (no C3-zeroing override); no openly-declared prompt restriction is violated in the body (no bracketed variables/module codes leaked) — so no restriction-breach override, though 5.2/1.1's anchor-handling and 5.4's over-labelled "Corrob." row are recorded as substantive deductions rather than an override trigger.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-02.csv`)

| card_id | strategy | flags | dud | integrity |
|---|---|---|---|---|
| 2026-07-02_Trade_1 | Trade 1 — Daily Directional | SUPPRESSED | False | excluded from mean (suppressed) |
| 2026-07-02_Trade_2 | Trade 2 — Pivot (regime-aware, TRANSITION → sell rally into resistance) | CLEAN | False | 100 |
| 2026-07-02_Trade_3A | Trade 3 — Complex (fork → 3A Momentum-Pullback, short side) | WARN_R_TINY(0.25xATR) | False | 90 |

Report-level Card Integrity = mean over non-suppressed cards = (100 + 90) / 2 = **95**.
n_cards = 3 (n_cards scored for integrity, excl. suppressed = 2), n_duds = 0, n_warns = 1.
