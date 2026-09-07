# Trust Score — 2026-06-09 — SP500_Report_09Jun2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 All Variables visibly respected | Asset = S&P 500 cash index (not ES) OK; counters USDX · VIX · DAX 40 in the required order OK; ≥6 sources OK (6 observations in §4, 12 endpoints attempted in §20); USD / index points OK. Three variables NOT respected: (a) as-of must be the NY close of D-1 = **8 Jun 2026**, the report uses **5 Jun 2026**; (b) lookback must be the 5 sessions ending D-1 (2–8 Jun), the report uses 1–5 Jun; (c) daily-open anchor must be **07:00 UK**, the report overrides it to 00:00 UK and remaps Trade 1 to the cash open. Tick 0.01 is absent from §2 altogether (the 08 Jun report carries it). | §2 Market Definition table + §2 anchor note; §6 header "5-Day"; §20 anchor-override bullet | 1 | List the unrespected variables: coverage window (wrong session), daily-open anchor, tick. Rebuild §2/§6/§11/§13c/§21 on D-1 = 2026-06-08. |
| 1.2 Coverage period and currency consistent throughout | No currency or unit drift anywhere (index points/USD used consistently). But the coverage error is uniform rather than sporadic: §2 ("most recent completed session 5 June 2026"), §6 (1–5 Jun), §11 ("from 5 June H/L/C"), §13c ("Previous Period (1–5 Jun)") and §21c (t−1 = 5 Jun) are all one session stale. The slice contains a completed 8 Jun cash session (O 7451.8 / H 7471.3 / L 7398.8 / C 7411.0). §20 concedes the run timestamp is 8 June, i.e. the report was built before the 8 June close and issued unrefreshed for the 9 June session. | §2, §6, §11, §13c, §20, §21c vs `US500_upto_2026-06-08.csv` | 1 | Advance every date-bearing section by one session; the 8 Jun row must appear in §6 and become the pivot prior period. |
| 1.3 Audience and tone match Purpose & Audience | Register is consistently institutional — "Senior US Equity Strategist" in the footer, §18 "Final Analyst Judgement", risk framed for a trading-and-risk review. No retail tone, no promotional language, no unhedged advice. | §1, §18, footer line | 5 | None. |
| 2.1 All sections present and correctly ordered | §1–§21 all present in the mandated order, including §13a/b/c/d and §21a/b/c/d. §7 carries five image references (pandoc retained the links). §17 is present as a single sentence. Only omission inside a section is the Tick row in §2. | Headings throughout; §7 image refs; §13a–d; §21a–d | 5 | None (fix the §2 Tick row under 1.1). |
| 2.2 Key Metrics Scorecard rendered as a table | §6 is a proper table with Date/O/H/L/C/RSI2/Trend/Src A/Src B/Validation — fully compliant. §11 is malformed: the daily table is a 2-up Level/Value grid running R5→R4→R3→R2→R1→R1.5 against P→S1→S2→S3→S4→S5→S1.5, not the required R3→P→S3 with three levels a side, and it carries a dangling "--- / ---" cell. The **weekly and monthly pivot tables are absent entirely** — replaced by one sentence ("Weekly and monthly pivots are likewise built on indicative prior-period extremes"). Two of the three required pivot tables are missing. | §6 table; §11 daily grid and the sentence closing §11 | 2 | Re-render §11 as three tables (daily, weekly, monthly), each R3→P→S3, three levels a side. |
| 2.3 Method steps visibly addressed | §4 lists observations with class, §5 states the normalisation and weighted-median build and names the two exclusions — a clean observations → classification → consensus chain. §8 is genuinely candle-by-candle for all five rows and closes with a sequence assessment. §9 states regime, bias, VOLator and the Kaufman gate. §7 charts present as captions/image refs (pandoc-dropped images accepted as evidence, noted). Weakness: §9 gives no numeric persistence/overlap and no numeric KER; VOLator values are asserted as "indicative". | §4, §5, §7, §8, §9 | 4 | State the numeric persistence/overlap and KER(13, EMA 3) values behind the §9 regime call. |
| 3.1 Every quantitative claim sourced | §1 numbers trace to §6/§13, §12 macro block cites the BLS, §14 explicitly cross-references §10 and §13d — the referencing discipline is real. But several load-bearing numbers carry no source and no anchor: "20Y/30Y yields back above 5%" (§12, §14), "core inflation near 2.6%" (§14, §13d), USDX at "a roughly 1.75-month high" (§12), the DAX level 24,759.05 / −0.75% (§10, §19 — no quote in §4 or §13a), and the VIX figures 21.51 / +39.7% which appear only as an unquoted §19 assertion. ISM "54 (vs 53.2)" in §13c is unsupported by the calendar slice (consensus there is 50.3, previous 52.7, actual not published). NFP "~85k expected" vs the slice consensus of 77.0. | §1, §10, §12, §13c, §14, §19 vs `news_upto_2026-06-08.csv` | 2 | Attach a named, dated source to each yield, CPI, USDX, DAX and VIX figure, or drop the claim. |
| 3.2 Spot-checked citations exist and contain the cited data | Three checks. **(1) Fortune/AP (§4)** — quotes 7,383.74 with a −200.57 point change; 7,584.31 − 200.57 = 7,383.74 and −200.57/7,584.31 = −2.645%, matching the −2.64% used in §1/§8. Internally consistent — PASS. **(2) Barchart (§4)** — quoted at 7,553.68 and *excluded* as a "stale/late-week last price", yet the same Barchart is Src B corroborating the 3 Jun close of 7,553.47 in §6. The same citation is simultaneously excluded and load-bearing, and 7,553.68 vs 7,553.47 is 0.21 pt apart — outside the ±0.10-pt corroboration tolerance the report itself declares in §3 and §19, while §6 still stamps the row "Close CORROBORATED". FAIL. **(3) Yahoo VIX (§19, "Yahoo 21.51 close")** — this figure drives §1, §10, §12, §14 and §15. It is contradicted inside the report by §4, which cites an AP table with VIX 18.71 on the same 5 Jun and discards it as "stale". Against the slice the 5 Jun VIX cash close is 18.46 (prior 16.21, i.e. **+13.9%**, not +39.7%) and the full-day close is 18.96 (prior 16.36, +15.9%); the 5 Jun full-day high is 19.01, so the VIX never reached 20 on any basis. A "+39.7% to 21.51" would require a prior close of 15.40, which exists nowhere in the report or the slice. The quoted figure does not match its own quote and is impossible on the data basis — **fabricated source**. | §4 Fortune/AP and Barchart rows; §6 Jun 3 Src B; §19 corroboration bullet; §10, §12; VIX slice 2026-06-04/05/08 | 0 | Trigger the hallucination override. Withdraw 21.51 / +39.7% / ">20 threshold" and rebuild §10/§12/§14/§15 on the D-1 VIX (8 Jun cash close 18.17). |
| 3.3 Calculations transparent | Strong where shown: the helper reproduces the report's own RSI2 column from its own closes **exactly** (14.8 / 35.4 / 13.3 for Jun 3/4/5), and every §11 daily pivot reproduces to the cent from the report's stated 5 Jun H/L/C (P = (7585+7380+7383.74)/3 = 7449.58; R1 7519.16; S1 7314.16; R2 7654.58; S2 7244.58; R3 7724.16; S3 7109.16). Gaps: ATR(14) is never stated — §21b only says "≈1.4× indicative ATR"; KER(13, EMA 3) is never given a number or parameters; VOLator readings are asserted with no derivation; §21a lists the weights and the six contributions but not the signal→weight mapping, and the Kaufman contribution of −0.11 against the 0.10 weight implies a signal of −1.10, outside the stated −1…+1 range. | §6 RSI2 column vs helper; §11 arithmetic; §9; §20 and §21a contribution list | 3 | State ATR(14) and KER numerically; publish the §21a signal×weight table with every |signal| ≤ 1. |
| 3.4 Numbers reconcile | Internally the report is tidy: 7,383.74 is identical in §1, §3, §4, §6 and the §21b Trade 1 reference; §11 pivots (7,449.58 / 7,519.16 / 7,244.58) are the same numbers quoted on both cards; RSI2 13.3 agrees across §1, §6 and §8. Against the slice nothing reconciles, because the basis is one session stale (see 1.2 and §5 below), and four separate internal breaks remain: (i) ATR is never stated so "1.4× indicative ATR" cannot be checked; (ii) Trade 3A's TP1 field states the method and then contradicts it — "38.2% retrace … ≈ 7,472 is above entry; structural TP1 set at 7,380"; (iii) the extracted Trade 1 card carries TP3 = 7,100, a number that appears nowhere in the report text; (iv) §4's Barchart 7,553.68 vs §6's Barchart-corroborated 7,553.47. | §1/§3/§4/§6/§21b close; §11 vs cards; §21b Trade 3A TP1 row; card JSON vs §21b | 2 | Identify and close each break; re-derive the whole chain from the 8 Jun close of 7,411.00. |
| 4.1 Each pillar reaches a defended conclusion | Every pillar terminates in an explicit label: §8 "Judgement label: Exhaustion — reversal risk"; §9 "Regime: Transitional / Bias: Bearish"; §10 "Aggregate cross-asset read: CONFIRM"; §12 tags each block (price-negative, cyclical); §14 closes on a named watch item. Form is fully compliant. The defence is weakened where it rests on unverifiable inputs — §10's CONFIRM leans on the impossible VIX reading and on a DAX level with no cited quote, so two of its three legs are not actually supported. | §8, §9, §10, §12, §14 | 3 | Re-defend §10 once the VIX and DAX inputs are sourced from D-1. |
| 4.2 Peer / cross-asset context interpreted, not listed | §10 gives a genuine transmission mechanism for each counter rather than a correlation table: USD strength tightening global financial conditions and hitting multinational earnings translation; the implied-vol spike marking a risk-off regime shift and hedging demand; DAX as European beta to the same global risk factor. Each row then states status and implication for the index. This is the strongest part of the report. | §10 Mechanism and Implication columns | 5 | None. |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles a strongly negative Kaufman read against an unresolved 25-session frame and explains why the composite stays Transitional rather than TREND_DOWN. §15 sets oversold-bounce risk against pivot location. §16 states a concrete base-case invalidation (a close back above 7,584.31). §21a runs the conflict check against §17 and records "no conflict". Where synthesis fails is the strategy layer: §21b suppresses Trade 2 **because** every pivot tier is single-source-indicative, then Trade 3A places a sell limit at that same indicative pivot (7,449.58) and Trade 1 anchors its stop on it — and §20 separately records a user instruction "to not suppress strategies on corroboration grounds", which contradicts the Trade 2 suppression it sits beside. | §9, §15, §16, §21a; §21b Trade 2 Status vs Trade 3A Entry; §20 strategy-note bullet | 3 | Reconcile the suppression rule with the card entries: either the pivots are usable for execution or no card may reference them. |
| 4.4 Calibrated language and confidence | §17 is exactly one sentence, no hedge stacking, and §3 states confidence explicitly (High). But the calibration is not earned: "High" confidence is attached to a close that is one session out of date, and §13b asserts "not low-confidence" without derivation. Card calibration is the larger failure (card construction scores here per the protocol): Trade 3A is labelled 3A momentum-pullback but abandons every 3A rule — no swing endpoints logged, no 2×ATR magnitude test, entry is a pivot rather than a 57.5% retrace, TP1 is not the 38.2% level (the card says so out loud), TP2 is not the 0% anchor, TP3 is a pivot rather than a 100%+ extension, and its thesis invalidation (7,519.16) sits 1.84 pts from its stop (7,521) rather than being separate from it. Trade 1 runs R = 100 pts against ATR14 = 70.84 without raising the required wide-stop flag. | §3, §13b, §17; §21b Trade 1 Stop/Risk rows and Trade 3A TP1/Stop/Thesis rows | 2 | Rebuild both cards to the M5 constructions; raise the wide-stop flag whenever R > 1×ATR. |
| 5.1 Data dated, staleness flagged | Dating discipline is present in form — every §6 row, §4 observation and §13a article carries a date, and single-source O/H/L are asterisked in §6 and restated in §19. The substantive staleness is undetected: the report calls 5 June "the most recently completed session" when the 8 June cash session had completed and sits in the slice, and §20's own run timestamp ("8 June 2026, report dated for 9 June 2026 session") admits the report was assembled before that close and shipped without refresh. This is precisely the failure this row exists to catch, and no staleness flag is raised anywhere. | §1, §2, §6, §19 data-gaps bullet, §20 run-timestamp bullet | 1 | Add the 8 Jun session and re-date every section; flag any residual gap explicitly. |
| 5.2 Assumptions stated up front | Genuinely well handled. The anchor override is disclosed four times — in the §2 table, the italic note under §2, the §20 Agent Log, and the Trade 1 Caveats row — with the consequence spelled out (the cash index does not trade at 00:00 UK, so entry maps to the cash open). Single-source pivot propagation is declared in §6, §11 and §19 and repeated in both card Caveats rows. The backtest's fill-realism limitation is disclosed in §20 and §21c. | §2 note, §19, §20, §21b Caveats rows, §21c preamble | 5 | None. |
| 5.3 Red flags surfaced | §12 carries five risk blocks each tagged with sign and type. §15 is a balanced four-a-side bull/bear table that names the pivot location, the FOMC and the yield channel. §13d identifies the 16–17 June FOMC as the highest-impact event and both cards carry it forward as an explicit event-risk caveat ("holding period brackets the 16–17 Jun FOMC"), so the calendar collision does reach the cards as required. | §12, §13d, §15, §21b Caveats rows | 5 | None. |
| 5.4 Restrictions honoured | Clean on the textual restrictions: no bracketed variable names, no M1–M5 module codes, no framework name, instrument common names used throughout, no ES-futures references, and no retail CFD quotes in the OHLC basis. Two breaches remain. (a) The report states its own no-synthesis restriction — indicative O/H/L and pivots "cannot be used for pivot prior-period calculations or as definitive entry/stop references" (§6) and "cannot anchor definitive limit orders" (§11) — and then §21b sets Trade 1's stop from daily P and places Trade 3A's sell **limit** at daily P; §20 records the decision to proceed anyway. (b) The 07:00 UK daily-open anchor variable is replaced with 00:00 UK. Minor: §20 leaks an internal version token ("v2.1 baseline, within the 20-session lock"). | §6 asterisk note, §11 source-status note, §19; §21b Trade 1 Stop and Trade 3A Entry rows; §20 anchor and strategy-note bullets | 1 | Restriction-breach override applies. Either restore corroborated D-1 H/L so pivots are executable, or remove all pivot-referenced entries and stops. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence and instruction compliance (20) | 1 | 0.20 | 4.00 | Rows 1.1/1.2/1.3 = 1/1/5, mean 2.33 → level 2; the restriction-breach override drops C1 one further level to 1. The report is built for the wrong session (D-1 = 8 Jun, report uses 5 Jun), the 07:00 UK anchor is overridden, and the tick variable is absent. |
| C2 Structural and modular framework alignment (20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/4/2 → mean 3.67 → level 4. All 21 sections and every subsection present and correctly ordered, §6 fully compliant as a table, method chain visible; the loss is §11, where the daily pivot grid is not R3→P→S3 and the weekly and monthly pivot tables are missing. |
| C3 Accuracy, evidence and factual reliability (25) | 0 | 0.00 | 0.00 | Rows 3.1/3.2/3.3/3.4 = 2/0/3/2 → mean 1.75 → level 2, then **set to 0 by the hallucinated-source override**. The §19 Yahoo VIX citation (21.51 close, +39.7%, ">20") is contradicted by the report's own §4 AP citation (18.71) and is impossible against the slice (5 Jun cash close 18.46, +13.9%; full-day high 19.01). |
| C4 Reasoning, judgment and evaluation quality (20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 3/5/3/2 → mean 3.25 → level 3. The analytic prose is the report's strength — §10 gives real mechanisms, §9 and §16 reconcile the short/medium tension and state an invalidation. The strategy layer drags it down: Trade 3A violates every M5 3A rule while carrying the 3A label, Trade 1 omits the required wide-stop flag, and the suppression logic contradicts the card entries. |
| C5 Currency, risk awareness, restrictions and transparency (15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 1/5/5/1 → mean 3.00 → level 3. Assumption disclosure and red-flag surfacing are exemplary — the anchor override and the indicative-pivot caveat propagate all the way to the cards. Offsetting that, the one-session staleness is never detected and the report's own no-synthesis restriction is breached in §21b. |
| **Total** | — | — | **43.75 → 44** | Σ(multiplier × max) = 4.00 + 17.00 + 0.00 + 13.00 + 9.75 = 43.75, rounded to 44. |

## 3. Total, band, override check

- **Raw total (post-override category levels): 43.75 → 44**
- **Band: Low Trust (40–59)**
- **Override: `hallucinated_source` (binding). `restriction_breach` also fired.**

Override reasoning:

1. **Hallucinated-source override — FIRED, binding.** Row 3.2 spot-check 3 fails. §19 cites "Yahoo 21.51 close" for the 5 June VIX, and §1/§10/§12 build on it ("a 40% one-day spike", "+39.7% to 21.51", "crosses the elevated-risk threshold (>20)"). The report contradicts itself: §4 cites an AP table carrying VIX 18.71 for the same 5 June and discards it as stale. The slice settles it — 5 Jun VIX cash close 18.46 against a prior close of 16.21 (**+13.9%**), full-day close 18.96 against 16.36 (+15.9%), and a full-day high of 19.01, so the index did not touch 20 on any basis. "+39.7% to 21.51" would require a prior close of 15.40, a value that exists nowhere. The cited figure does not match its own quote and is impossible on the data basis. Per framework §6, Category 3 is set to 0 and the report is capped at the Low Trust band (40–59).
2. **Restriction-breach override — FIRED.** §6, §11 and §19 state that indicative O/H/L and the pivots derived from them cannot serve as definitive entry/stop references or anchor limit orders; §21b then anchors Trade 1's stop on daily P (7,449.58) and places Trade 3A's sell **limit** at that same P, with §20 recording the decision to proceed. The 07:00 UK daily-open anchor variable is separately overridden to 00:00 UK. Per framework §6 this caps the report at Moderate Trust (60–74) and reduces Category 1 by at least one rubric level — C1 has been taken from 2 to 1 accordingly.
3. **Cap arithmetic.** The computed total of 44 already sits inside the Low band, so neither cap (≤59 from the hallucination override, ≤74 from the restriction breach) reduces it further. Final Trust Score **44 — Low Trust**. Operational action per framework §6: full prompt review and regeneration; investigate whether the prompt template was correctly applied, since the run was assembled against the previous session's data basis.

## 4. Card Integrity

Linter rows, copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-09.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-09_Trade_1 | 2026-06-09 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-09_Trade_3A | 2026-06-09 | Trade 3A - Momentum-Pullback (sell limit daily P) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-09_Trade_1 | 0 | 0 | 100 |
| 2026-06-09_Trade_3A | 0 | 0 | 100 |

**Report-level Card Integrity = mean over non-suppressed cards = 100.0** (n_cards = 2, n_duds = 0, n_warns = 0).

Notes on the count. The lint file carries **fewer than three cards** — two rows, not three. This is not a missing card: §21b emits Trade 2 as an explicit **SUPPRESSED** row ("all accessible daily/weekly/monthly pivot tiers are SINGLE-SOURCE-INDICATIVE per §19"), which is the form M5 requires, and a suppressed card is out of scope for the static linter and excluded from the integrity mean. All three trades are therefore accounted for.

The perfect integrity score reflects only what the static linter tests, and both cards do pass those tests on their own stated numbers: stops on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R within 0.3–3.0×ATR14 (Trade 1 R = 100 and Trade 3A R = 71 against ATR14 = 70.84), TP1 within 2.5×ATR14 of entry, and Trade 3A's sell limit at 7,449.58 correctly above the D-1 close on either basis. It is silent on the M5 construction failures assessed under row 4.4 — the wrong MARKET entry level, the missing wide-stop flag, the non-3A construction of Trade 3A, and the anchor override — because the linter runs leak-free on the card's own numbers and cannot see the slice.

## 5. Data reconciliation log

Slice basis: `data/slices/US500/US500_upto_2026-06-08.csv`, cash session 16:30–23:00 broker, via `engine/qa_slice_stats.py`. Tolerances per the brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

**A. §6 five-row OHLC table, row by row**

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 Jun 1 | Open | 7,585* | 7,575.2 | +9.8 | OUT OF WINDOW — row should not be in a D-1-anchored table; also outside the 8-pt O/H/L tolerance |
| §6 Jun 1 | High | 7,604* | 7,623.6 | −19.6 | OUT OF WINDOW / FAIL |
| §6 Jun 1 | Low | 7,575* | 7,568.5 | +6.5 | OUT OF WINDOW / within tolerance |
| §6 Jun 1 | Close | 7,599.96 | 7,607.7 | −7.74 | OUT OF WINDOW / FAIL (>3 pts) |
| §6 Jun 2 | Open | 7,601* | 7,590.8 | +10.2 | FAIL (>8 pts) |
| §6 Jun 2 | High | 7,620.90 | 7,624.6 | −3.70 | PASS (≤8 pts) |
| §6 Jun 2 | Low | 7,592* | 7,588.3 | +3.70 | PASS |
| §6 Jun 2 | Close | 7,609.78 | 7,615.8 | −6.02 | FAIL (>3 pts) |
| §6 Jun 3 | Open | 7,607* | 7,602.0 | +5.00 | PASS |
| §6 Jun 3 | High | 7,612* | 7,608.0 | +4.00 | PASS |
| §6 Jun 3 | Low | 7,548* | 7,556.0 | −8.00 | PASS (at the limit) |
| §6 Jun 3 | Close | 7,553.47 | 7,565.2 | −11.73 | **CATEGORY 3 FAILURE** (>10 pts) |
| §6 Jun 4 | Open | 7,556* | 7,541.3 | +14.70 | FAIL (>8 pts) |
| §6 Jun 4 | High | 7,590* | 7,604.3 | −14.30 | FAIL (>8 pts) |
| §6 Jun 4 | Low | 7,549* | 7,535.0 | +14.00 | FAIL (>8 pts) |
| §6 Jun 4 | Close | 7,584.31 | 7,592.7 | −8.39 | FAIL (>3 pts) |
| §6 Jun 5 | Open | 7,580* | 7,540.5 | +39.50 | FAIL (>8 pts, ~5× tolerance) |
| §6 Jun 5 | High | 7,585* | 7,545.3 | +39.70 | FAIL (>8 pts, ~5× tolerance) — this value feeds §11 |
| §6 Jun 5 | Low | 7,380* | 7,372.8 | +7.20 | PASS — this value feeds §11 |
| §6 Jun 5 | Close | 7,383.74 | 7,392.5 | −8.76 | FAIL (>3 pts) |
| §6 | **Jun 8 row (D-1)** | **absent** | O 7,451.8 / H 7,471.3 / L 7,398.8 / C 7,411.0 | n/a | **MISSING ROW — the D-1 session is not in the table at all** |

Jun 1 slice figures are recomputed on the same 16:30–23:00 cash window; the helper prints only the five sessions ending D-1 (2–8 Jun), so that row carries roughly ±4 pts of convention uncertainty. It is listed for completeness — under a D-1 anchor it should not appear at all.

**B. RSI2 column — two independent tests**

| Section | Field | Report value | Reference | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | RSI2 Jun 2 | 100 | helper on slice closes: 100.00 | 0.00 | PASS |
| §6 | RSI2 Jun 3 | 14.8 | helper on slice closes: 16.23 | −1.43 | PASS (consistent with the close delta) |
| §6 | RSI2 Jun 4 | 35.4 | helper on slice closes: 35.21 | +0.19 | PASS |
| §6 | RSI2 Jun 5 | 13.3 | helper on slice closes: 12.08 | +1.22 | PASS |
| §6 | RSI2 Jun 3 | 14.8 | helper recomputed from the **report's own** closes: 14.8 | 0.00 | **PASS — exact** |
| §6 | RSI2 Jun 4 | 35.4 | helper recomputed from the report's own closes: 35.4 | 0.00 | **PASS — exact** |
| §6 | RSI2 Jun 5 | 13.3 | helper recomputed from the report's own closes: 13.3 | 0.00 | **PASS — exact** |
| §6 | RSI2 Jun 1 / Jun 2 = 100 | 100 | not testable from five closes alone (needs the seeding closes); slice gives 100.00 for Jun 2 | — | PASS on Jun 2; Jun 1 unverifiable from the stated window |
| §6 | RSI2 for D-1 (Jun 8) | absent | 8.46 | n/a | MISSING |

The RSI2 arithmetic is correct: it reproduces to the decimal from the report's own close sequence, and the small gaps against the slice are fully explained by the close deltas in table A. The failure is the input series, not the formula.

**C. §11 pivots — reproduction from the report's own D-1 H/L/C, and against the correct D-1**

| Section | Field | Report value | Recomputed from the report's own 5 Jun H 7,585 / L 7,380 / C 7,383.74 | Delta | Verdict |
|---|---|---|---|---|---|
| §11 | P | 7,449.58 | (7585+7380+7383.74)/3 = 7,449.58 | 0.00 | PASS — reproduces |
| §11 | R1 | 7,519.16 | 2P − L = 7,519.16 | 0.00 | PASS |
| §11 | S1 | 7,314.16 | 2P − H = 7,314.16 | 0.00 | PASS |
| §11 | R2 | 7,654.58 | P + (H−L) = 7,654.58 | 0.00 | PASS |
| §11 | S2 | 7,244.58 | P − (H−L) = 7,244.58 | 0.00 | PASS |
| §11 | R3 | 7,724.16 | H + 2(P−L) = 7,724.16 | 0.00 | PASS |
| §11 | S3 | 7,109.16 | L − 2(H−P) = 7,109.16 | 0.00 | PASS |

The pivot formulas are applied correctly. The inputs are wrong twice over — the wrong session (5 Jun instead of 8 Jun) and, within that session, a High overstated by 39.7 pts. Against the correct D-1:

| Section | Field | Report value | Slice value (D-1 = 8 Jun cash) | Delta | Verdict |
|---|---|---|---|---|---|
| §11 | P | 7,449.58 | 7,427.03 | +22.55 | FAIL |
| §11 | R1 | 7,519.16 | 7,455.27 | +63.89 | FAIL |
| §11 | R2 | 7,654.58 | 7,499.53 | +155.05 | FAIL |
| §11 | R3 | 7,724.16 | 7,527.77 | +196.39 | FAIL |
| §11 | S1 | 7,314.16 | 7,382.77 | −68.61 | FAIL |
| §11 | S2 | 7,244.58 | 7,354.53 | −109.95 | FAIL |
| §11 | S3 | 7,109.16 | 7,310.27 | −201.11 | FAIL |
| §11 | Weekly pivot table | absent | P 7,463.30 / R1 7,553.80 / R2 7,715.10 / R3 7,805.60 / S1 7,302.00 / S2 7,211.50 / S3 7,050.20 | n/a | MISSING TABLE |
| §11 | Monthly pivot table | absent | not printed by the helper | n/a | MISSING TABLE |

**D. Cross-asset and derived values**

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §1, §9, §10, §12, §14 | VIX 5 Jun close | 21.51 | 18.46 (cash) / 18.96 (full day) | +3.05 / +2.55 | **FAIL — fabricated (see override 1)** |
| §1, §9, §10, §12 | VIX one-day change | +39.7% (§1: "40%") | +13.9% (cash) / +15.9% (full day) | +25.8 pp | **FAIL — impossible** |
| §10, §12, §14, §15 | VIX above the 20 threshold | asserted crossed | 5 Jun full-day high 19.01; never reached 20 | n/a | FAIL — claim unsupported on any basis |
| §19, §10 | VIX at D-1 | not reported (report stops at 5 Jun) | 8 Jun cash close 18.17 | n/a | MISSING |
| §10, §12 | USDX direction over 5 sessions | Rising | 99.22 (2 Jun) → 100.03 (8 Jun) | — | PASS on direction |
| §12 | USDX "roughly 1.75-month high" | asserted | not verifiable from the 60-session slice window; unsourced | n/a | UNSOURCED |
| §10, §19 | DAX 40 −0.75% / 24,759.05 | asserted | no DAX slice supplied | n/a | NOT VERIFIABLE — and carries no cited quote in §4 or §13a |
| §21b | ATR(14) | never stated; implied ≈71.4 from "100 pts ≈ 1.4× ATR" | 70.84 (cash) / 84.69 (full day) | ≈0.6 vs cash | Implied value consistent with the cash ATR, but the figure is never stated as required by row 3.3 |
| §1, §3, §4, §6, §21b | D-1 close used as the card entry basis | 7,383.74 | 7,411.00 (8 Jun cash) | −27.26 | FAIL — the MARKET entry cannot equal the D-1 close |
| §8 | Jun 5 range | 7,585 − 7,380 = 205 | 7,545.3 − 7,372.8 = 172.5 | +32.5 | FAIL — the "extended range" characterisation rests on an overstated high |
| §1, §8 | Jun 5 session change | −2.64% | −2.64% (7,392.5 from 7,592.7) | 0.00 pp | PASS — the percentage is right even though the levels are not |
| §12, §13c | May Non-Farm Payrolls actual | 172,000 | 172.0 | 0.0 | PASS |
| §12, §13c | May NFP consensus | "~85,000 expected" | 77.0 | +8.0k | MINOR FAIL — hedged with "~" but misstated |
| §12, §13c | Unemployment rate | steady at 4.3% | actual 4.3, previous 4.3 | 0.0 | PASS |
| §13c | ISM Manufacturing 1 Jun | 54 (vs 53.2), prior 52.7 | consensus 50.3, previous 52.7, actual not published in the slice | consensus +2.9 | FAIL — actual unsupported, consensus misstated |
| §13c | Coverage window | 1–5 Jun | must be 2–8 Jun | one session | FAIL — 8 Jun calendar items (CB Employment Trends Index 107.01 vs 105.92 consensus, 3M/6M bill auctions) are absent |
| §13a | Article dates | 2, 4, 5 Jun | window must be 2–8 Jun | — | FAIL — no article from 8 Jun; the tilt of −0.16 is computed on a stale set |
| §13a | CNBC vs Fortune, both 5 Jun | "worst day since April 2025" vs "worst day since October" | — | n/a | FAIL — two cited quotes make mutually exclusive claims; §1 adopts "since October" without reconciling them |
| §4 vs §6 | Barchart quote | 7,553.68 (excluded, §4) vs Src B corroborating 7,553.47 (§6) | — | 0.21 | FAIL — outside the report's own ±0.10-pt corroboration tolerance while §6 stamps the row CORROBORATED |
| §21a | Direction score | −0.68 | sum of the six stated contributions = −0.68 | 0.00 | PASS on the sum; the Kaufman contribution of −0.11 against the 0.10 weight implies a signal of −1.10, outside the ±1 range |
