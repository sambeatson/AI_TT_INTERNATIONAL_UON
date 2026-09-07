# Trust Score — 2026-07-16 — SP500_M1_Report_16Jul2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-07-16 (Thursday) · D-1 = 2026-07-15 (Wednesday)
Evidence base: report text; `data/slices/US500/US500_upto_2026-07-15.csv` via `engine/qa_slice_stats.py`;
VIX/USDX/NEWS slices to D-1; `cards/baseline/by_date/2026-07-16.json`; lint rows for 2026-07-16.

Helper output used throughout (cash session 16:30–23:00 broker):
D-1 2026-07-15 O 7569.10 · H 7582.80 · L 7528.60 · C 7573.90 · RSI2 100.00 · ATR14 72.52 (full-day 79.79)
D-1 daily pivots P 7561.77 · R1 7594.93 · R2 7615.97 · R3 7649.13 · S1 7540.73 · S2 7507.57 · S3 7486.53
Weekly (06–10 Jul) P 7524.93 · R1 7628.77 · R2 7683.33 · S1 7470.37 · S2 7366.53
5d swing high 7582.80 (15-Jul) / low 7482.30 (09-Jul) · 25d swing high 7583.40 (15-Jun) / low 7260.00 (11-Jun)

**Headline finding:** the report's as-of session is **14-Jul-2026**, i.e. **D-2**. 15-Jul-2026 is a full
cash session present in the slice (close 7,573.90). Every "prior close", the 5-day OHLC window, the swing
extremes, all pivots and every card level are therefore built on the wrong session and are one session stale.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the cash index (^GSPC), not ES — correct. Counters listed USDX first, then VIX, then DAX 40 — correct. Units index points, tick convention consistent. **As-of session is 14-Jul (D-2), not the NY close of D-1 (15-Jul).** Lookback is 5 sessions but the window is 08–14 Jul instead of 09–15 Jul. **Daily-open anchor overridden from 07:00 UK to 00:00 UK** — a deviation under the M1 instance, disclosed but still non-conforming. Source count: the report itself states "Sources attempted before corroboration: 5" against a ≥6 requirement. | Header block ll.5–28; §2 override table; §3 source table; §16a | 1 | Rebuild against the 15-Jul close; restore the 07:00 UK anchor or carry it as an explicit non-conformance; attempt ≥6 sources. |
| 1.2 Coverage & currency consistent | Report is "for session 16-Jul" but every data field stops at 14-Jul; the 15-Jul session is absent from the OHLC table, the swing set and the pivots. Cross-asset dating is internally mixed: VIX quoted at a "14-Jul close", Yahoo quotes cited as "live 15-Jul", USDX undated. §9 states no calendar could be obtained for 16-Jul, yet 48 D-dated USD events exist in the project's news slice. No currency/unit drift (all USD index points). | §4 table; §7 VIX note; §9 para 3; NEWS slice 2026-07-16 rows | 1 | Re-date the whole report to a single D-1 basis (15-Jul) and populate the calendar sections. |
| 1.3 Audience & tone | Senior US Equity Strategist role declared and sustained; institutional trading-and-risk register; no retail framing, no promotional language; caveats written for a risk reviewer. Strongest aspect of the report. | Header "Role"; §1; §14; §17 warning box; closing note | 5 | None. |
| 2.1 Sections present & ordered | The mandated 21-section scheme is not followed: the report runs to 17 differently numbered sections. Absent entirely: Consensus Price Call, Consensus Build, Charts, Short-Term Technical (candle-by-candle), and the whole Sentiment/News/Calendar block (§13a per-article table, §13b aggregate tilt section, §13c previous-period calendar, §13d upcoming calendar). §21c backtest and §21d limitations are present inside the report's §17. | Headings ll.55–937; sentiment tilt +0.20 appears only as a row in the §5 surface table with no §13 to support it | 1 | Restore the 21-section scheme and the five missing sections. |
| 2.2 Scorecard as a table | The OHLC table is a table but carries Session/Open/High/Low/Close/Change/Range only — **RSI2, Trend, Source A, Source B, Final and Validation columns are all absent** (6 of 11 required). Pivots: daily table has R3→S3 plus R1.5/S1.5 (3 levels each side, correct); **weekly table has only R2/R1/P/S1/S2 (2 levels each side)**; **no monthly pivot table at all**. | §4 table ll.243–256; §8a; §8b | 1 | Add the six missing columns; extend weekly to R3/S3; add the monthly pivot table. |
| 2.3 Method steps visible | Regime derivation is genuinely well shown (gate table with requirement/actual/pass, explicit fall-through to TRANSITION), and the direction-score decomposition is fully itemised. Against that: no charts and no caption or placeholder of any kind; no observations→classification→consensus build; no candle-by-candle short-term sequence. | §6 gate table; §17a component table; no §7-equivalent charts anywhere | 2 | Add charts (or captioned placeholders), the consensus build, and the candle-by-candle sequence. |
| 3.1 Quantitative claims sourced | §1/§5 figures trace back to the report's own §3a/§4 tables. But the single-stock claims in §9 (NVDA +4.06%, MU +4.92%, SNDK +5.01%, AMD +2.57%, IBM −25.21% on 67.44M, HCA −6.95%, ISRG −6.78%, SYK −6.15%, BIIB −8.17%) carry **no source at all**, and the §10 macro table (10Y 4.593%, 30Y 5.107%, 10-2 spread 31.32bp, WTI 79.72) is likewise unsourced and undated. | §9; §10 | 2 | Attach a named, dated source to every §9/§10 figure or remove it. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) Investing.com/FRED close pair: named, dated, and the 7,543.59 figure is used consistently in §1, §3a, §4, §5, §12, §17b — internally consistent. (b) **Barchart**: "last price 7,553.68 + 52wk high 7,620.90 matched Source A" is **undated**, and 7,553.68 appears nowhere in Source A's own 20-session table; the 52wk high 7,620.90 is unsupported by any data shown in the report. (c) **VIX readings**: 16.50 attributed to a 14-Jul close and 16.26 to a 15-Jul Yahoo quote — the slice's 14-Jul VIX cash session ranges 17.22–17.47 (close 17.42) and the 15-Jul session 16.94–17.49 (close 16.99), so **both quoted values sit outside the session range they are dated to**. Not scored as fabrication (the report discloses the readings are not date-matched and no impossible URL/date pair is asserted), but the citations do not carry the data they are said to carry. | §3 source table; §7 VIX note; §16a; VIX slice | 2 | Date the Barchart quote and reconcile it to Source A; re-source or drop the VIX levels. |
| 3.3 Calculations transparent | Pivot arithmetic reproduces **exactly** from the report's own 14-Jul H/L/C (7,557.44 / 7,513.23 / 7,543.59): P 7538.09, R1 7562.94, S1 7518.73, R2 7582.30, S2 7493.88, R3 7607.15, S3 7474.52, and the floor identity holds (R2−P = P−S2 = 44.21); R1.5/S1.5 are correct midpoints. Direction score reproduces exactly (weights 0.25/0.20/0.10/0.15/0.15/0.15, contributions sum to +0.2750). Stop/TP/ATR-cap arithmetic reproduces. **RSI2 is neither shown per session nor reproducible**: the stated 58.01 recomputes to 32.0 from the report's own five closes and to 33.49 (14-Jul) / 100.00 (15-Jul) on slice closes. Trend classification rule is never applied (no Trend column). ATR(14) 78.26 and KER(13, EMA 3) +0.3252 are asserted without derivation or basis. | §4 note l.263; §5; §8a; §17a; §17b; helper `--closes` output | 2 | Publish RSI2 per session with RS = mean gain / mean loss over 2 periods; add the Trend column; state ATR/KER inputs. |
| 3.4 Numbers reconcile | Internally the report is tight: 7,543.59 is identical in §1, §5, §8a distance column, §12, §17b entry and §18; §8a pivots equal the levels quoted on the Trade 2 card; ATR 78.26 is consistent between §5 and §17b; RSI2 58.01 is consistent between §1, §5 and the §17a W_SHORT_TECH basis. But the anchor reconciliation fails against the world outside the report: the "last corroborated close" is **30.31 pts** from the true D-1 cash close (7,543.59 vs 7,573.90). And the baseline card JSON does not reconcile to the report: Trade 2 carries `tp3 = 7590.0`, a level that appears nowhere in the report, and Trade 1 is `entry_mode MARKET` at `anchor_broker 16:30` while §17b describes a pending order on a 00:00 UK anchor. | §1/§5/§8a/§17b cross-refs; `cards/baseline/by_date/2026-07-16.json` | 1 | Re-anchor to 15-Jul and make the card JSON match the report text field for field. |
| 4.1 Pillars conclude | Regime → "regime_label = TRANSITION"; cross-asset → "cross_asset_confirm = MIXED"; pivots → "neutral pivot position"; macro → "mildly supportive but not decisively so". All four conclude cleanly and consistently with their own content. Weakened by there being no short-term technical pillar at all, and §9 Key Market Considerations ending in narrative with no direction label. The strategy layer then contradicts the regime pillar it inherits (see 4.3). | §6; §7; §8a; §9; §10 | 3 | Add the short-term technical pillar and a direction label to §9. |
| 4.2 Peer/cross-asset interpreted | §7 gives mechanism, not correlation: dollar softness → multinational earnings translation; VIX below 20 → risk appetite intact; DAX −0.46% against SPX +0.38% → global equity not confirming, explicitly flagged as contradiction rather than smoothed away, with the resulting +0.10 pre-weight contribution traced into §17a. This is the report's best analytical section. | §7 table and following paragraphs; §17a W_CROSS_ASSET | 4 | Date the counter quotes to D-1. |
| 4.3 Synthesis reconciles tensions | Prose synthesis is strong: §1 names the short-firm/medium-flat tension up front, §6 reconciles positive KER against negative VOLator as a late-trend signature, §14 sets confidence LOW for an explicitly data-quality reason rather than a directional one, §17a flags the signal as narrow and concentrated. **But an unreconciled contradiction survives into the score**: the same VOLator slope of −0.0395 that FAILS the TREND_UP gate in §6 is scored **+0.25** in §17a and described as supportive, with no reconciliation of the opposite sign treatment. **And the strategy layer contradicts its own regime call**: §6 sets TRANSITION and §17c states the pivot card should not exist, yet a long pivot card at P targeting R1 is produced anyway. | §6; §17a W_VOLATOR row; §17c note | 2 | Reconcile the VOLator sign treatment; make the card set obey the regime fork. |
| 4.4 Calibrated language | §13 forecast is exactly one sentence and states a level band, a mechanism and an invalidation without hedge stacking. Confidence is explicitly LOW in §14 with a stated reason. §12 pairs direction with conviction ("mildly higher, with low conviction"). No overclaiming anywhere; the "no statistical weight whatsoever" note on the 2-trade backtest is appropriately calibrated. | §12; §13; §14; §17f | 4 | None material. |
| 5.1 Data dated; staleness flagged | Every price row and every source outcome is dated, and the single-source O/H/L limitation is flagged in the header box, §3, §4 column markers, §5 surface rows, §8 box, §15 and §17 — thorough. **What is not flagged is the staleness that matters**: the report never acknowledges that the 15-Jul session exists and is missing, and presents a D-2 close as "the prior corroborated close" for a 16-Jul session. Counter quotes are dated inconsistently (14-Jul vs "live 15-Jul"). | Header box; §4 †/✓ legend; §15; §7 VIX note | 2 | Flag the missing session explicitly, or rebuild on 15-Jul. |
| 5.2 Assumptions up front | Exemplary. A DATA INTEGRITY SUMMARY box before §1; §2 override table naming both deviations; §2a explaining precisely why a 00:00 UK anchor cannot fill on a cash index and what the entry therefore is; single-source pivot propagation stated at the point of use in §8 and re-stated on both trade cards; §15 normalisation statement ("none applied"); §16 agent log; closing note. | Header box; §2/§2a; §8 box; §15; §16; §17 box | 5 | None. |
| 5.3 Red flags surfaced | §11 bull/bear is balanced and specific; §14 names a single watch item with a level; §17 opens with an execution warning; §16f logs four anomalies including the unexplained IBM move and the FRED snapshot mismatch. **But §13d event-collision checks are simply declared impossible** ("no corroborated calendar data for the 16-Jul session"), so no event caveat is carried into any card — while the project's own news slice holds 48 D-dated USD events, several inside the cash session (Pending Home Sales m/m 17:00 broker, Retail Inventories m/m 17:00, EIA gas 17:30, 4-/8-week bill auctions 18:30). §9 also asserts FOMC/NFP/CPI as the catalysts without checking them against any calendar. | §11; §14; §16f; §9 para 3; NEWS slice | 3 | Populate §13c/§13d and propagate collisions into the card caveats. |
| 5.4 Restrictions honoured | **BREACH.** Bracketed variable names appear throughout the body: `[DAILY_OPEN_ANCHOR]`, `[W_*]`, `[PRODUCE_STRATEGY_RECOMMENDATIONS]`, `[ADDITIONAL_CONTEXT]`, `[PRODUCE_PIVOT_TRADE]`, `[MAX_SIMULTANEOUS_LONG_SHORT]`, `[BACKTEST_LOOKBACK_DAYS]`. Module codes appear in prose and in a section heading: "M1 — S&P 500 (Cash Index) v2.1", "5. Technical Indicators — M3 §11 Named Output Surface", "M3 §11b", "M2 §13b", "M5 §4a", "M5 §5.1", "M1/M2/M3/M4/M5 v2.1", "PATCHES_v1_2 §P6". Restrictions that ARE honoured: no synthesised or interpolated price is presented as sourced (§15 states this explicitly and the labelling supports it); no retail CFD quotes enter the OHLC basis; ES futures are referenced only as out-of-scope commentary, never as data. | §2 table; §5 heading; §6; §9; §16c–d; §17a; §17c; §17d; §2a | 1 | Strip every bracketed variable name and every module/patch code; use plain instrument and field names. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 1 | 0.20 | 4.00 | Rows 1.1/1.2/1.3 = 1/1/5, mean 2.33 → level 2; **restriction-breach override drops C1 one level to 1**. Wrong as-of session, wrong 5-session window, anchor override, 5 sources against a ≥6 requirement; tone fully compliant. |
| C2 Structure & completeness (max 20) | 1 | 0.20 | 4.00 | Rows 2.1/2.2/2.3 = 1/1/2, mean 1.33 → 1. Five mandated sections missing (consensus price call, consensus build, charts, short-term technical, the entire §13 news/calendar block); 6 of 11 scorecard columns missing; weekly pivots truncated and monthly pivots absent. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/2/2/1, mean 1.75 → 2. Pivot and score arithmetic reproduce exactly and the stated sessions sit within CFD-vs-cash basis, but the anchor close is 30.31 pts from the true D-1 close, RSI2 does not reproduce from the report's own closes (58.01 vs 32.0), and §9/§10 numbers are unsourced. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 3/4/2/4, mean 3.25 → 3. Cross-asset mechanism and calibration are strong; the strategy layer contradicts the report's own TRANSITION fork and its own suppression rule, and the VOLator sign is treated oppositely in §6 and §17a. Card-construction defects (thesis invalidation = stop, TP3 < TP2, pivot card produced under TRANSITION, R = 0.24×ATR) are carried in 4.1/4.3. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/5/3/1, mean 2.75 → 3. Assumption disclosure is the best feature of the report; undermined by an unflagged stale session, an unpopulated calendar, and a clear restriction breach on bracketed variables and module codes. |
| **Total** | — | — | **40.75 → 41** | Sum of category points, rounded. |

## 3. Total, band, override check

- Raw total: 4.00 + 4.00 + 10.00 + 13.00 + 9.75 = **40.75 → 41**.
- **Override applied: `restriction_breach`.** Prompt restriction 5.4 (no bracketed variable names, no module codes M1..M5) is breached in at least twelve places, including a section heading. Consequences per framework §6: total capped at 74 — **not binding, the raw total is already 41** — and C1 dropped one level, which **is** applied above (level 2 → level 1, −4.00 points).
- **Fabricated-source override: NOT triggered.** The Barchart last price (7,553.68, undated, matching nothing in Source A's own table) and the two VIX levels that fall outside the session ranges they are dated to are accuracy failures scored in 3.2 and 3.4, but no cited source is internally impossible in the sense the protocol requires (no wrong-date URL, no figure contradicting its own quote), and the report itself discloses that the VIX readings are not date-matched. C3 therefore stands at 2, not 0, and no cap at 59 applies.
- **Band: Low (40–59).** Final Trust Score **41 / 100**.
- Note for the regeneration agent: the single change with the largest score effect is re-anchoring the report to the 15-Jul session. It moves 1.1, 1.2, 3.4, 5.1 and every card level at once.

## 4. Card Integrity

Lint rows verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-16.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-16_Trade_1 | 2026-07-16 | Trade 1 - Daily Directional | WARN_TP3_ORDER | False |
| 2026-07-16_Trade_2 | 2026-07-16 | Trade 2 - Pivot (buy limit daily P) | WARN_R_TINY(0.24xATR) | False |
| 2026-07-16_Trade_3C | 2026-07-16 | Trade 3C - Transition Breakout | SUPPRESSED | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-16_Trade_1 | 0 | 1 (WARN_TP3_ORDER) | 90 |
| 2026-07-16_Trade_2 | 0 | 1 (WARN_R_TINY) | 90 |
| 2026-07-16_Trade_3C | 0 | 0 | suppressed — excluded from the mean |

**Report Card Integrity = 90.0** (mean over the 2 non-suppressed cards). Cards in lint file: 3 · DUD flags: 0 · WARN flags: 2.

M5 rule assessment (feeds row 4.x, not the integrity number):

- **Trade 1** — thesis invalidation (7,402.26) is stated as "coincides with SL", but the rule requires it to be a level separate from the stop. TP3 (7,778.37) sits below TP2 (7,826.26); the rule requires TP3 beyond TP2 or null, and the report notices the inconsistency but ships it anyway. A MARKET entry must equal the D-1 close: the card entry 7,543.59 is the D-2 close and is 30.31 pts from the D-1 cash close 7,573.90. The stop is built on `swing_low_5d` 7,421.82, which is the low of a stale window — the true 5-session low is 7,482.30. Anchor is explicit but is the 00:00 UK override rather than 07:00 UK, and the card JSON records `MARKET` at broker 16:30 while §17b describes a pending order — the report and the card disagree. Correctly present: three equal units, TP1/TP2 at ±1R/±2R, Unit 3 → entry + 0.2R on fill, 3×ATR / session-close runner, wide-stop flag raised at 1.81×ATR.
- **Trade 2** — produced in breach of two M5 rules. Regime is TRANSITION, for which Trade 2 is breakout-side only; a buy limit at the daily pivot targeting R1 is the RANGE/TREND expression. And the card must be suppressed when every pivot tier is single-source-indicative — which is exactly what §8 and §17c assert. R = 19.36 pts = 0.24×ATR(78.26), below the 0.3×ATR static floor (the lint WARN). The card's `tp3 = 7590.0` appears nowhere in the report and matches no pivot tier. No three-unit structure and no BE rule are specified.
- **Trade 3C** — correctly not triggered: the regime fork to 3C is right, and the anchor close sits inside the 25-day range so no confirming close exists. The confirmation arithmetic is internally correct (7,579.93 + 0.25×78.26 = 7,599.50). But the boundaries come from stale/incorrect 25-day extremes (report 7,579.93 / 7,294.18 vs slice 7,583.40 / 7,260.00 — the low is off by 34.18 pts), and the 3C stop rule (low + 0.40×width) and TP rules (1.0×width, 1.5×width) are never stated even contingently.

## 5. Data reconciliation log

Tolerance per the brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low. Slice values are cash-session
(16:30–23:00 broker) from `engine/qa_slice_stats.py`.

**5a. §4 OHLC table (the report's "Validated OHLC + RSI2 (5-Day)") — row by row**

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §4 | 08-Jul Open | 7,476.54 | 7,459.60 | +16.94 | **DISCREPANCY** — exceeds the 8-pt open tolerance |
| §4 | 08-Jul High | 7,488.51 | 7,488.10 | +0.41 | consistent |
| §4 | 08-Jul Low | 7,421.82 | 7,421.10 | +0.72 | consistent |
| §4 | 08-Jul Close | 7,482.71 | 7,478.60 | +4.11 | **DISCREPANCY** — exceeds the 3-pt close tolerance |
| §4 | 09-Jul Open | 7,491.60 | 7,498.80 | −7.20 | consistent (within 8) |
| §4 | 09-Jul High | 7,546.89 | 7,547.40 | −0.51 | consistent |
| §4 | 09-Jul Low | 7,481.73 | 7,482.30 | −0.57 | consistent |
| §4 | 09-Jul Close | 7,543.64 | 7,542.80 | +0.84 | consistent |
| §4 | 10-Jul Open | 7,547.64 | 7,544.70 | +2.94 | consistent |
| §4 | 10-Jul High | 7,579.93 | 7,579.50 | +0.43 | consistent |
| §4 | 10-Jul Low | 7,508.16 | 7,505.60 | +2.56 | consistent |
| §4 | 10-Jul Close | 7,575.39 | 7,574.20 | +1.19 | consistent |
| §4 | 13-Jul Open | 7,547.53 | 7,550.80 | −3.27 | consistent |
| §4 | 13-Jul High | 7,565.37 | 7,565.80 | −0.43 | consistent |
| §4 | 13-Jul Low | 7,506.41 | 7,507.00 | −0.59 | consistent |
| §4 | 13-Jul Close | 7,515.34 | 7,518.20 | −2.86 | consistent (at the edge of tolerance) |
| §4 | 14-Jul Open | 7,536.70 | 7,535.70 | +1.00 | consistent |
| §4 | 14-Jul High | 7,557.44 | 7,559.70 | −2.26 | consistent |
| §4 | 14-Jul Low | 7,513.23 | 7,512.90 | +0.33 | consistent |
| §4 | 14-Jul Close | 7,543.59 | 7,546.40 | −2.81 | consistent |
| §4 | 15-Jul row (D-1) | **absent** | O 7,569.10 / H 7,582.80 / L 7,528.60 / C 7,573.90 | n/a | **FAILURE** — the D-1 session is missing from the 5-day window entirely; the table covers 08–14 Jul instead of 09–15 Jul |

**5b. As-of session and anchor close**

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| Header / §1 / §5 / §17b — "last corroborated close" | 7,543.59 (14-Jul, stated as Tuesday — the day name is correct for 14-Jul) | 7,573.90 (15-Jul cash close, the true D-1) | −30.31 | **FAILURE** — as-of session is D-2, not D-1; 15-Jul is a full trading session present in the slice |
| §1 five-session change (+60.88) | 7,543.59 − 7,482.71 | on D-1 basis: 7,573.90 − 7,542.80 = +31.10 | −29.78 | derived failure — follows from the stale window |
| §1 close vs 5-day mean (+11.46) | mean 7,532.13 from the report's own five closes | D-1 basis mean 7,551.10, close +22.80 | −11.34 | derived failure |

**5c. RSI2**

| Section | Report value | Reference | Delta | Verdict |
|---|---|---|---|---|
| §4 note / §5 / §1 / §17a | RSI2 latest = 58.01 | recomputed from the **report's own five closes** (7,482.71 / 7,543.64 / 7,575.39 / 7,515.34 / 7,543.59) = **32.0** | +26.01 | **FAILURE** — does not reproduce from the report's own data; a Category 3 failure under the brief |
| §4 note / §5 | RSI2 latest = 58.01 | helper RSI2 on slice cash closes, 14-Jul = 33.49 | +24.52 | **FAILURE** |
| §4 note / §5 | RSI2 latest = 58.01 | helper RSI2 on slice cash closes at D-1, 15-Jul = 100.00 | −41.99 | **FAILURE** — the correct D-1 reading is an extreme, not "mid-range"; this propagates into §1 ("no short-term exhaustion signal") and into §17a W_SHORT_TECH ("RSI2 58 (no extreme)") |
| §4 | Trend column | required by the scorecard spec (Close>Open & RSI2>50 → Bullish, etc.) | n/a | **MISSING** — rule never applied |

**5d. §8 pivots — internal reproduction and the floor identity**

| Section | Check | Result | Verdict |
|---|---|---|---|
| §8a | P = (H+L+C)/3 from the report's own 14-Jul 7,557.44 / 7,513.23 / 7,543.59 | 7,538.087 vs stated 7,538.09 | reproduces |
| §8a | R1 = 2P − L | 7,562.943 vs stated 7,562.94 | reproduces |
| §8a | S1 = 2P − H | 7,518.733 vs stated 7,518.73 | reproduces |
| §8a | R2 = P + (H−L) | 7,582.297 vs stated 7,582.30 | reproduces |
| §8a | S2 = P − (H−L) | 7,493.877 vs stated 7,493.88 | reproduces |
| §8a | R3 = H + 2(P−L) | 7,607.153 vs stated 7,607.15 | reproduces |
| §8a | S3 = L − 2(H−P) | 7,474.523 vs stated 7,474.52 | reproduces |
| §8a | **Identity R2 − P = P − S2** | 44.21 = 44.21 | **holds** |
| §8a | R1.5 / S1.5 midpoints | (R1+R2)/2 = 7,572.62 ✓ · (S1+S2)/2 = 7,506.305 → 7,506.30 ✓ | reproduce |
| §8a | Distance-from-close column | R3 +63.56, R2 +38.71, R1 +19.35, P −5.50, S1 −24.86, S1.5 −37.29, S2 −49.71, S3 −69.07 | all reproduce from 7,543.59 |
| §8a | **Basis** | computed from the 14-Jul session; D-1 pivots from the slice are P 7,561.77 · R1 7,594.93 · S1 7,540.73 · R2 7,615.97 · S2 7,507.57 · R3 7,649.13 · S3 7,486.53 | **DISCREPANCY** — Δ on P is −23.68; every level is one session stale |
| §8b | Weekly P 7,525.71 / R1 7,629.61 / R2 7,683.82 / S1 7,471.50 / S2 7,367.60 | slice weekly (06–10 Jul) P 7,524.93 / R1 7,628.77 / R2 7,683.33 / S1 7,470.37 / S2 7,366.53 | Δ +0.78 / +0.84 / +0.49 / +1.13 / +1.07 — **consistent**; correct prior week; but R3/S3 are missing |
| — | Monthly pivots | not produced | **MISSING** |

**5e. Derived quantities and swing extremes**

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §5 | atr_14 = 78.26 | cash-session ATR14 72.52 (full-day 79.79) | +5.74 vs cash / −1.53 vs full-day | acceptable — consistent with a full-day ATR basis; basis should be stated |
| §5 | swing_high_5d = 7,579.93 | 7,582.80 (15-Jul) | −2.87 | window-shift artefact — the correct D-1 5-day high is a different session |
| §5 | swing_low_5d = 7,421.82 | 7,482.30 (09-Jul) | −60.48 | **DISCREPANCY** — stale window; this value is the direct input to the Trade 1 stop |
| §5 | swing_high_25d = 7,579.93 | 7,583.40 (15-Jun) | −3.47 | within high/low tolerance, but the extreme is attributed to the wrong session |
| §5 | swing_low_25d = 7,294.18 | 7,260.00 (11-Jun) | +34.18 | **DISCREPANCY** — far outside tolerance; this value anchors the Trade 3C lower boundary |
| §17d | 25-day range width 285.75 (= 7,579.93 − 7,294.18, internally correct) | 323.40 (= 7,583.40 − 7,260.00) | −37.65 | derived discrepancy; also drives the "3.65 × ATR" qualification claim |
| §17a | Direction score +0.2750 | recomputed from the report's own weights and component scores: 0.125 − 0.010 + 0.025 + 0.090 + 0.030 + 0.015 | 0.000 | reproduces exactly; weights 0.25/0.20/0.10/0.15/0.15/0.15 sum to 1.00 and match the required order |

**5f. Cross-asset counters**

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §7 / §10 | ^VIX 16.50, "Investing.com 14-Jul close", −3.85% | 14-Jul cash close 17.42 (session range 17.22–17.47); 14-Jul change −0.74% | −0.92 on level; −3.11pp on change | **DISCREPANCY** — the quoted level lies below the entire 14-Jul session range |
| §7 | ^VIX 16.26, "Yahoo, live 15-Jul" | 15-Jul cash close 16.99 (session range 16.94–17.49) | −0.73 | **DISCREPANCY** — below the whole D-1 session range |
| §7 / §10 | DX-Y.NYB 100.597, −0.11% | 14-Jul close 100.92 (−0.36%); 15-Jul close 100.492 (−0.42%) | −0.32 vs 14-Jul / +0.105 vs 15-Jul | **DISCREPANCY / undated** — the level matches D-1 far better than the stated 14-Jul basis, but the −0.11% change matches neither session |
| §7 | ^GDAXI 25,030.21, −0.46% | no DAX slice available in this run | n/a | not verifiable |
| §7 / §10 | US 10Y 4.593%, 30Y 5.107%, 10-2 spread 31.32bp, WTI 79.72 | no slice available | n/a | not verifiable and unsourced in the report |

**5g. Calendar**

| Section | Report claim | Slice evidence | Verdict |
|---|---|---|---|
| §9 / §15 / §17 | "no corroborated calendar data for the 16-Jul session; §13d event-collision checks could not be completed" | `data/slices/NEWS/news_upto_2026-07-15.csv` holds **48 rows dated 2026-07-16** (actuals withheld, consensus/previous present), several landing inside the cash session — Pending Home Sales Index / m/m / y/y and Retail Inventories m/m at 17:00 broker, EIA Natural Gas Storage Change at 17:30, 4-week and 8-week Bill Auctions at 18:30 | **FAILURE** — D-dated scheduled calendar was available and was not used; §13c/§13d absent and no event caveat reaches any card |
