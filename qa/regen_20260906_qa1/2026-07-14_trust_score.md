# Trust Score — 2026-07-14 — SP500_Report_14Jul2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (503 constituents), not ES futures. Counters USDX · VIX · DAX 40, USDX listed first. Lookback 5 sessions (execution) + 20 (regime). USD / index points. §4 carries 6 sources spanning index provider (S&P DJI), aggregators and sell-side (Bloomberg via Reuters). **Fails on as-of**: §2 sets "most recent completed session 10 July 2026" but D-1 is Mon 13 Jul 2026, a full trading session present in the slice (cash O 7550.8 / H 7565.8 / L 7507.0 / C 7518.2). **Fails on anchor**: the 07:00 UK daily-open anchor is never stated in the report; §2/§20 instead declare an unspecified "override". | §2 table, §4 table, §20 bullets 1–2, §21b Trade 1 entry line | 2 | State the as-of as the NY close of 13 Jul 2026 and name the 07:00 UK anchor explicitly on Trade 1. |
| 1.2 Coverage & currency consistent | No currency or unit drift — everything is USD index points on a cash basis throughout. No data point postdates D. But the whole evidence window is one session short: §6 covers 6–10 Jul instead of 7–13 Jul; §11 weekly pivots use "29 Jun–2 Jul" instead of the prior completed week 6–10 Jul; §21c backtest runs t−5..t−1 = 6–10 Jul instead of 7–13 Jul. Every dated block therefore ends one session before D-1. | §2, §6, §11, §21c | 1 | Re-anchor §6, §11, §13c and §21c on the 13 Jul session. |
| 1.3 Audience & tone | Sustained senior-strategist register: regime labels, conviction score, event-risk framing, invalidation levels. Footer signs "Senior US Equity Strategist". No retail promotional language anywhere; §21d carries the limitations boilerplate rather than a performance pitch. | §1, §18, §21d footer | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in the prescribed order. §13 fully decomposed into 13a per-article table, 13b aggregate with a numeric tilt (+0.21), 13c previous-period calendar, 13d upcoming calendar. §21 decomposed into 21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working + limitations boilerplate. §17 is a single sentence. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a genuine table with Date / O / H / L / C / RSI2 / Trend / Source A-B / Validation; the "Final" column is folded into the bolded Close rather than shown separately. §11 gives three pivot tables (daily, weekly, monthly) ordered top-down R→P→S. Deviation: each table carries **five** tiers a side (R5…S5) where the spec is three (R3→P→S3). | §6, §11 | 4 | Restore a separate Final column in §6; trim §11 to R3→P→S3. |
| 2.3 Method steps visible | §4 lists raw observations with basis and relevance; §5 states the weighted-median build, the ±0.10-pt tolerance, what was excluded as directional and why. §8 is candle-by-candle for all five sessions with an explicit sequence assessment. §9 gives persistence 0.47 (9 up / 19), net move, VOLator readings and the KER dual-gate resolution. §7 carries five chart captions with pandoc-dropped image placeholders — accepted as evidence per protocol and noted. | §4–§9 | 5 | None (chart images dropped by pandoc; captions accepted). |
| 3.1 Quantitative claims sourced | Several §1/§12 numbers carry no source or §4/§6/§13 pointer: "Nvidia +4%, Meta +6% on 10 Jul" (§1), "Russell 2000 lagging (−0.5% on 10 Jul)" (§12), "WTI spiked (+4–9% intraday)" (§12), "KBW additions" (§12). Two attributions have no matching §13a row: Goldman's "critical test" phrase and "Goldman estimates a 10% dollar depreciation adds 2–3% to EPS". **Direct internal contradiction**: §10 says "~28% of S&P 500 revenue earned abroad", §12 says "~42% of S&P 500 sales that are international (FactSet)" — same quantity, two figures. | §1, §10, §12, §14 | 2 | Source or delete each bare number; reconcile 28% vs 42% to one sourced figure. |
| 3.2 Citations exist & contain data | Spot-check 1 — **CNBC 10 Jul**: quote "+0.42%" and 7,575.39 are used consistently in §4, §13c and §1; internally coherent. Spot-check 2 — **Forbes/Glenview 5 Jul**: named and dated, quote "earnings projected to grow 23.3% year-over-year", but §1 and §12 both state "22–23%", so the report's own headline figure sits outside the range it quotes. Spot-check 3 — **Goldman Sachs 28 Jun**: named, dated, quote coherent with §1/§12 direction, but the "critical test" wording and the FX-to-EPS estimate attributed to Goldman in §12 appear in no cited row. Source-hygiene failures: "BofA (Subramanian)" carries host `eciks.org/Reuters` (publisher and host do not match) and is dated only "Jun"; "Reuters (via TheStreet)" carries host `finance.yahoo.com` and is dated only "early Jul". **No source is demonstrably impossible or self-refuting on its own quote, so the fabricated-source override is NOT applied** — see §3 below. | §4, §13a, §12 | 2 | Date the two undated rows to the day; align publisher and host; attach the "critical test" and 2–3% EPS claims to a dated row or drop them. |
| 3.3 Calculations transparent | RSI2 reproduces **exactly** from the report's own close sequence on all three testable rows (Jul 08 0.0, Jul 09 74.2, Jul 10 100.0 — helper output identical); Jul 06/07 are untestable from five closes alone. Trend labels follow the stated rule on all five rows (Jul 08 correctly Neutral on C>O with RSI2 0). §11 daily pivots reproduce to 0.01 from the report's own 10-Jul H/L/C (P 7,554.49 / R1 7,600.83 / R2 7,626.26 / R3 7,672.60 / S1 7,529.06 / S2 7,482.72 / S3 7,457.29). §8 close-in-range percentages all reproduce (72%, 44%, 91%, 95%, 94%). §21a score reproduces to +0.278 ≈ +0.28 on the mandated 0.25/0.20/0.10/0.15/0.15/0.15 weights. Gaps: ATR(14)=84.1 is stated only in §21b, not §9; KER is given as a value (0.21 / +0.15) without the 13-period / EMA-3 parameters. | §6 note, §8, §11, §21a, §20 bullet 7 | 4 | State ATR(14) in §9 and the KER(13, EMA 3) parameters alongside the value. |
| 3.4 Numbers reconcile | Internally the report is tight: 7,575.39 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry, and §11 pivots equal the pivots quoted on the cards. But it reconciles to the **wrong session**. Against the slice's true D-1 (13 Jul): close 7,518.20 (Δ 57.19), daily P 7,554.49 vs 7,530.33 (Δ 24.16), weekly P 7,457.62 vs 7,524.93 (Δ 67.31), June monthly implied high 7,577.92 vs slice 7,624.60 (Δ 46.68). Further internal breaks: §21d states Trade 1 TP1/TP2 hit rates 75%/25% while its own §21c table shows 2 of 4 triggered reaching +1R and 0 of 4 reaching +2R; §21c enters Trade 1 at session opens (7,507 / 7,517 / 7,492 / 7,548) while the live card enters at the prior close; §3 gives a range 7,543–7,580 described as "the last two sessions' closes bracketing the level" when those closes are 7,543.64 and 7,575.39; §9 net move +2.5% vs slice +1.91% on the report's own 10-Jul basis and −0.6% on the true D-1 basis. | §1/§3/§4/§6/§11/§21b/§21c/§21d cross-check, slice | 1 | Rebuild §6/§11/§21 on the 13 Jul session; correct the §21d hit rates; align the backtest entry rule with the live card. |
| 4.1 Pillars conclude | Every pillar ends in a direction label consistent with its own content: §8 "Bullish continuation", §9 "Transitional with upward bias / Bias: Bullish", §10 "Aggregate cross-asset read: MIXED" with a per-counter confirm status, §12 labels every theme (price-supportive / mixed / price-negative / neutral-to-supportive / supportive), §14 closes on a directional watch item. One internal slip: §8 calls the 8 Jul candle "the red close" when the report's own table has C 7,482.71 > O 7,476.54 (an up body, correctly labelled Neutral in §6). | §8, §9, §10, §12, §14 | 4 | Fix the 8 Jul "red close" wording to match the §6 body. |
| 4.2 Peer/cross-asset interpreted | §10 gives a transmission mechanism for each counter rather than a correlation list: USDX through the foreign-revenue earnings-translation channel, VIX through hedging demand and the multiple, DAX as a common global-risk factor. The USDX contradiction is raised explicitly ("Contradiction flag"), not resolved silently, and is carried forward into §14, §15 and §17. | §10, §14, §15, §17 | 5 | None. |
| 4.3 Synthesis reconciles tensions | Prose synthesis is good: §9 explicitly reconciles the Trending-Up KER against the formal Transitional label via the dual-gate rule; §15 balances four bull against four bear items; §16 ties regime to levels and states invalidation; §21a records "Conflict flag: none" consistent with §17. **Card construction, scored here, fails on all three cards**: Trade 1 takes the stop at daily S1 with no 0.25×ATR buffer and never logs the 5-day swing extreme it is meant to compare against; Trade 2 is labelled "TREND bias" but matches none of M5's three recipes (it uses entry = P, stop = S2, TPs R1/R2/R3 where TREND requires entry P+0.10×(R1−P), stop P−0.8×(P−S1), TPs R1/R1.5/R2) — and §9's consolidated regime is TRANSITION, under which M5 permits the breakout side only; Trade 3A is labelled a trend momentum-pullback but is built as a breakout stop-entry, with no 57.5% retrace entry, no qualifying-swing endpoints logged and no 38.2%/0%/100% TP ladder. §9's "preferred trade protocol: trend-pullback longs" is never reconciled with the TRANSITION restriction. | §9, §15, §16, §21a, §21b all three cards | 2 | Rebuild all three cards to their M5 recipes; reconcile the TRANSITION label against the Trade 2 construction. |
| 4.4 Calibrated language | §17 is exactly one sentence, single-clause direction with a named contingency, no hedge stacking. Confidence "High" is stated in §3 and repeated in §18; tone stated in §1 and §3. Deduction: §21d asserts precise hit rates (75% / 25% / 0%) that its own §21c table does not support — an uncalibrated performance claim in an otherwise well-hedged report. | §3, §17, §18, §21d | 4 | Restate the §21d hit rates from the §21c rows. |
| 5.1 Data dated; staleness flagged | Every §4 and §6 row is dated; §19 declares no single-source-indicative OHLC or pivot fields; §20 discloses the FRED (stale, cached May 2026) and Stooq (network-blocked) gaps and states corroboration was achieved without them — that part is exemplary. But the central staleness is **not** flagged: the report presents 10 Jul as "the most recent completed session" for a 14 Jul session date when 13 Jul is a completed session sitting in the slice, and nowhere warns that its prices, pivots, ATR, backtest and card levels are one session behind. Two §13a rows are undated ("Jun", "early Jul"). | §2, §6, §13a, §19, §20 | 1 | Use the 13 Jul session, or flag prominently that data are one session stale and why. |
| 5.2 Assumptions up front | §2 note and §20 bullet 2 both record that "the configured daily-open anchor was overridden at analyst instruction", but neither states what it was overridden **from** or **to** — the 13 Jul report, by contrast, recorded "overridden to NY open". The baseline card carries `anchor_broker` 09:00 (= 07:00 UK), i.e. the configured M1 anchor, which contradicts the claim that an override was applied. Single-source pivot propagation is addressed properly (§19 and the Trade 2 caveat both state no tier is single-source, so no suppression). §21d limitations boilerplate present. | §2 note, §19, §20, §21b Trade 2 caveats, card JSON | 2 | State the override's from/to explicitly, or remove the override claim so it matches the 07:00 UK anchor actually used. |
| 5.3 Red flags surfaced | §12 carries the oil/US–Iran and 2026-hike tail risks; §15 lists four downside risks including the BofA 7,100 red-flag warning and concentration risk; §13d marks the 14–15 Jul bank-earnings collision as the Tier-1 event and it is carried into the Trade 1 and Trade 2 caveat lines and the Trade 3A caveat; §10's USDX contradiction flag propagates to §15/§16. | §12, §13d, §15, §16, §21b caveat rows | 5 | None. |
| 5.4 Restrictions honoured | Grep across the report returns no module codes (M1–M5), no framework name, no bracketed or braced variable placeholders. Instruments are named in common form ("S&P 500 cash index", "USDX", "VIX", "DAX 40"). No ES/E-mini quote appears anywhere, so the confirmation-only rule is not engaged. The OHLC basis is Investing.com × Yahoo ^SPX — no retail CFD quotes. No price is presented as synthesised or interpolated. **No restriction breach; the restriction-breach override is not applied.** | Whole report (grep-verified), §4, §6, §19 | 5 | None. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Mean of 1.1/1.2/1.3 = (2+1+5)/3 = 2.67 → 3. Asset, counters, units, source count and tone all correct; the as-of session and the whole coverage window are one session short of D-1 and the 07:00 UK anchor is never named. |
| C2 Structural alignment (max 20) | 5 | 1.00 | 20.00 | Mean of 2.1/2.2/2.3 = (5+4+5)/3 = 4.67 → 5. Every section and sub-section present and ordered, method chain visible end to end; only cosmetic deviations (five pivot tiers instead of three, Final column folded into Close). |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Mean of 3.1/3.2/3.3/3.4 = (2+2+4+1)/4 = 2.25 → 2. Arithmetic is clean and reproducible, but the evidence base is the wrong session, two source rows are undated with mismatched hosts, several numbers are unsourced, and §10 contradicts §12 on the same quantity. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Mean of 4.1/4.2/4.3/4.4 = (4+5+2+4)/4 = 3.75 → 4. Pillar logic, cross-asset mechanism and tension handling are strong and the conviction score is fully traceable; card construction, scored here, deviates from the M5 recipe on all three cards. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Mean of 5.1/5.2/5.3/5.4 = (1+2+5+5)/4 = 3.25 → 3. Restrictions fully honoured and red flags well surfaced; undermined by unflagged one-session staleness and an anchor-override note that states neither its from nor its to. |
| **Total** | | | **69.75 → 70** | |

## 3. Total, band, override check

- Raw total: 13.00 + 20.00 + 10.00 + 17.00 + 9.75 = **69.75**, rounded to **70**.
- Band: **Moderate** (60–74).
- **Fabricated-source override — not applied.** Three cited sources were spot-checked for internal consistency (CNBC 10 Jul, Forbes/Glenview 5 Jul, Goldman Sachs 28 Jun). None is impossible or self-refuting on its own quote: the CNBC row is consistent with §4 and §13c; the Goldman row's quote is coherent with the use made of it, though §12 adds two Goldman attributions with no cited row; the Forbes row's "23.3%" is at the edge of, not contradictory to, the "22–23%" the report states elsewhere. The two weak rows — "BofA (Subramanian)" on host `eciks.org/Reuters` and "Reuters (via TheStreet)" on host `finance.yahoo.com`, both dated only to a month or "early Jul" — are publisher/host mismatches and dating failures, scored under 3.2 and 5.1, but neither is demonstrably invented. C3 is therefore scored 2, not zeroed, and no cap at 59 applies.
- **Restriction-breach override — not applied.** Grep confirms no module codes, no framework name and no bracketed variable placeholders; no ES futures quote; no retail CFD quote in the OHLC basis; no price presented as synthesised; instruments in common names. C1 is not dropped a level and no cap at 74 applies. (The total is 70 in any case, already inside Moderate.)
- Final Trust Score: **70 / 100 — Moderate**, override `none`.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-14.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-14_Trade_1 | 2026-07-14 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-14_Trade_2 | 2026-07-14 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-07-14_Trade_3A | 2026-07-14 | Trade 3A - Momentum-Pullback (breakout stop) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-14_Trade_1 | 0 | 0 | 100 |
| 2026-07-14_Trade_2 | 0 | 0 | 100 |
| 2026-07-14_Trade_3A | 0 | 0 | 100 |

Non-suppressed cards: 3. **Report Card Integrity = 100.0.**

Note for interpretation: the static linter is leak-free and self-referential — it validates each card against the D-1 close the *report* states (7,575.39). Measured against the slice's actual D-1 cash close (7,518.20), Trade 1's MARKET entry is 57.19 pts away from the D-1 close and Trade 2's BUY LIMIT at 7,554.49 sits 36.29 pts *above* the D-1 close, i.e. on the wrong side for a buy limit. These are recorded under rows 3.4 and 4.3 and in the feedback; they do not alter the linter-derived integrity number, which is copied verbatim and not re-derived.

## 5. Data reconciliation log

Basis: `data/slices/US500/US500_upto_2026-07-13.csv`, cash session 16:30–23:00 broker (09:30–16:00 ET), via `engine/qa_slice_stats.py`. Tolerance per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

| Section | Report value | Slice value (cash) | Delta | Verdict |
|---|---|---|---|---|
| §2 as-of | most recent completed session = 10 Jul 2026 | D-1 = 13 Jul 2026 is a complete cash session in the slice (O 7,550.8 H 7,565.8 L 7,507.0 C 7,518.2) | one session | **FAIL** — as-of is not D-1; the entire report is built on t−2 |
| §6 row Jul 06 Open | 7,506.96 | 7,513.90 | −6.94 | OK (≤8) |
| §6 row Jul 06 High | 7,551.31 | 7,552.40 | −1.09 | OK |
| §6 row Jul 06 Low | 7,500.97 | 7,502.40 | −1.43 | OK |
| §6 row Jul 06 Close | 7,537.43 | 7,542.60 | −5.17 | **DISCREPANCY** (>3 on a close) |
| §6 row Jul 07 Open | 7,516.63 | 7,531.50 | −14.87 | **DISCREPANCY** (>8) |
| §6 row Jul 07 High | 7,536.06 | 7,538.40 | −2.34 | OK |
| §6 row Jul 07 Low | 7,478.63 | 7,480.50 | −1.87 | OK |
| §6 row Jul 07 Close | 7,503.85 | 7,504.30 | −0.45 | OK |
| §6 row Jul 08 Open | 7,476.54 | 7,459.60 | +16.94 | **DISCREPANCY** (>8) |
| §6 row Jul 08 High | 7,488.51 | 7,488.10 | +0.41 | OK |
| §6 row Jul 08 Low | 7,421.82 | 7,421.10 | +0.72 | OK |
| §6 row Jul 08 Close | 7,482.71 | 7,478.60 | +4.11 | **DISCREPANCY** (>3 on a close) |
| §6 row Jul 09 Open | 7,491.60 | 7,498.80 | −7.20 | OK (≤8) |
| §6 row Jul 09 High | 7,546.89 | 7,547.40 | −0.51 | OK |
| §6 row Jul 09 Low | 7,481.73 | 7,482.30 | −0.57 | OK |
| §6 row Jul 09 Close | 7,543.64 | 7,542.80 | +0.84 | OK |
| §6 row Jul 10 Open | 7,547.64 | 7,544.70 | +2.94 | OK |
| §6 row Jul 10 High | 7,579.93 | 7,579.50 | +0.43 | OK |
| §6 row Jul 10 Low | 7,508.16 | 7,505.60 | +2.56 | OK |
| §6 row Jul 10 Close | 7,575.39 | 7,574.20 | +1.19 | OK |
| §6 row for D-1 (13 Jul) | absent | O 7,550.80 H 7,565.80 L 7,507.00 C 7,518.20, RSI2 35.93 | whole row | **FAIL** — the D-1 session is missing from the 5-day table |
| §6 RSI2 Jul 06 | 100.0 | 100.00 (slice closes) | 0.00 | OK; not testable from the report's own five closes |
| §6 RSI2 Jul 07 | 61.7 | 49.80 (slice closes) | +11.90 | Basis-driven; not testable from the report's own five closes |
| §6 RSI2 Jul 08 | 0.0 | 0.00 (slice) / **0.0 recomputed from the report's own closes** | 0.00 / 0.00 | OK — arithmetic exact |
| §6 RSI2 Jul 09 | 74.2 | 71.41 (slice) / **74.2 recomputed from the report's own closes** | +2.79 / 0.00 | OK — arithmetic exact |
| §6 RSI2 Jul 10 | 100.0 | 100.00 (slice) / **100.0 recomputed from the report's own closes** | 0.00 / 0.00 | OK — arithmetic exact |
| §11 daily pivots vs the report's own 10-Jul H/L/C | P 7,554.49 R1 7,600.83 R2 7,626.26 R3 7,672.60 S1 7,529.06 S2 7,482.72 S3 7,457.29 | recomputed from H 7,579.93 / L 7,508.16 / C 7,575.39: identical to 0.01 | 0.00 | OK — pivots reproduce from the report's own inputs |
| §11 daily P vs the true D-1 (13 Jul) session | 7,554.49 | 7,530.33 | +24.16 | **FAIL** — daily pivots are struck off the wrong session |
| §11 daily R1 / S1 vs true D-1 | 7,600.83 / 7,529.06 | 7,553.67 / 7,494.87 | +47.16 / +34.19 | **FAIL** |
| §11 weekly window | "prior week 29 Jun–2 Jul" | prior completed week for D is 6–10 Jul (3 Jul is a trading session, so even the stated week is truncated) | — | **FAIL** — wrong week |
| §11 weekly P | 7,457.62 | 7,524.93 (6–10 Jul) | −67.31 | **FAIL** |
| §11 weekly R1 | 7,566.37 | 7,628.77 (6–10 Jul) | −62.40 | **FAIL** — the "close above weekly R1" narrative in §11/§15/§16 and the Trade 2 confluence rest on this |
| §11 weekly implied prior-period C | 7,483.25 (back-solved from P/R1/S1) | 7,504.60 (3 Jul cash close) | −21.35 | **DISCREPANCY** — consistent with dropping 3 Jul from the week |
| §11 monthly (June) implied High | 7,577.92 (back-solved) | 7,624.60 | −46.68 | **DISCREPANCY** |
| §11 monthly (June) implied Low | 7,257.33 (back-solved) | 7,243.10 | +14.23 | **DISCREPANCY** (>8) |
| §11 monthly P | 7,444.87 | 7,453.67 | −8.80 | **DISCREPANCY** |
| §21b ATR(14) | 84.1 pts | 79.00 cash / 84.20 full-day (to 13 Jul) | +5.10 / −0.10 | OK against the full-day basis; note the report gives no basis and computes it to 10 Jul |
| §9 20-session net move | +2.5% | +1.91% to 10 Jul; −0.6% to 13 Jul | +0.59pp / +3.1pp | **DISCREPANCY** — sign-flips on the correct D-1 basis |
| §1/§16 all-time high | 7,620.90 | June cash high in slice 7,624.60 | −3.70 | Note only — the ATH may predate the slice window |
| §21b Trade 1 MARKET entry vs D-1 close | 7,575.39 | 7,518.20 | +57.19 | **FAIL** — a MARKET entry must equal the D-1 close |
| §21b Trade 2 BUY LIMIT vs D-1 close | 7,554.49 | 7,518.20 | +36.29 | **FAIL** — a buy limit must sit below the D-1 close |
| §21b Trade 3A BUY STOP vs D-1 close | 7,581.00 | 7,518.20 | +62.80 | OK — correct side for a buy stop |
| §21c backtest window | t−5…t−1 = 6–10 Jul | t−5…t−1 = 7, 8, 9, 10, 13 Jul | one session | **FAIL** |
| §21d Trade 1 TP1 / TP2 hit rates | 75% / 25% | §21c shows 2 of 4 triggered at +1R, 0 of 4 at +2R = 50% / 0% | −25pp / +25pp | **DISCREPANCY** — internal, against the report's own table |
| §10 vs §12 international revenue share | 28% (§10) vs 42% (§12, "FactSet") | — | 14pp | **DISCREPANCY** — internal contradiction, same quantity |
| Cross-report (13 Jul report, dated before D) | Same §6 O/H/L/C rows for 6–10 Jul, but RSI2 93.4 / 48.3 / 30.0 / 78.0 / 87.2 | 14 Jul report states 100.0 / 61.7 / 0.0 / 74.2 / 100.0 for the identical closes | — | **DISCREPANCY** — two reports give different RSI2 for one close sequence; the 14 Jul values are the ones that reproduce |
