# Reviewer brief — Trust Score v3.7 applied to the XAUUSD daily reports (run `gold_regen_qa1`)

Distilled from `modules/` (the prompt stack the reports were produced under) and
`docs/QA_PROTOCOL_TRADE_CARDS.md`. It contains no market information beyond what your own date's
level file gives you. It exists so that 57 independent review sessions apply the same anchors.
Where this brief and the framework text disagree, the framework
(`docs/AI_Output_Trust_Score_Framework_v3.7.txt`, Sections 4–7) wins.

## 0. What is different about the gold run

**There is no gold M1 instance module.** `modules/` ships `M1_SP500_v2_1.md` and the generic
`M1_Variables_v2_1.md`, and nothing gold-specific. So you cannot check §2's declared variables
against a populated gold instance. Instead:

- Check the report's declared variables against `M1_Variables_v2_1.md` (the generic spec: what each
  variable *means* and which are fixed) and for **internal consistency across the report**.
- Do **not** penalise a gold report for differing from the S&P instance (different counters, a
  different tick name, a different anchor). Do penalise it where it contradicts a value the
  framework or the variable module fixes, or where it contradicts itself.

**You are given the real market data for your date.** `data/levels/XAUUSD_by_date/<D>.csv` holds one
row, computed from the broker execution feed using only bars strictly before D. It gives the prior
session's O/H/L/C, ATR14, RSI2, daily / weekly / monthly floor pivots and 5d/25d swing extremes, each
on both a cash-session and a full-day basis. Every number in it is leak-free by construction and was
asserted so when the file was written (`last_bar_date` < `date`; check it yourself).

This changes what Category 3 means here. You are not judging whether the report's pivots are
*plausible* — **you can check them.** Recompute nothing by hand; the file has already done it.

## 1. Scoring mechanics (framework §4, §6, §7)
- Five categories, each 0–5, converted by multiplier: 5→1.00, 4→0.85, 3→0.65, 2→0.40, 1→0.20, 0→0.00.
- Maxima: C1 Prompt adherence 20 · C2 Structure 20 · C3 Accuracy & evidence 25 · C4 Reasoning & judgment 20 ·
  C5 Currency, restrictions & transparency 15. Total = Σ(multiplier × max), rounded to a whole number.
- Category level = mean of its Section 7 checklist rows, rounded to the nearest whole level.
- Bands: Very High 90–100 · High 75–89 · Moderate 60–74 · Low 40–59 · Very Low 0–39.
- Overrides: a fabricated source → cap at Low (40–59) and C3 = 0. A breached prompt restriction →
  cap at Moderate (60–74) and C1 down at least one level.
- Card Integrity is SEPARATE (not part of the 100): per card 100 − 40·(#DUD) − 10·(#WARN), floored at
  0; report level = mean over non-suppressed cards. Copy the linter rows verbatim; do not re-derive.

## 2. Section 7 checklist mapped to these reports

| Row | What to check here | Where |
|---|---|---|
| 1.1 Variables respected | Asset = XAU/USD spot gold (LBMA loco-London convention), **not** COMEX GC front-month — futures may appear as corroboration only, normalised · USDX is the mandatory first counter (`M1_Variables` §D) · as-of = last completed session strictly before D · lookback 5 sessions short / 25 medium · USD per troy ounce · ≥ 6 independent sources for the consensus build · tick name/size stated and used consistently | §2, §4, §10, §13, §21b |
| 1.2 Coverage & currency consistent | Every date in §2/§6/§13/§21 is D−1 or earlier for data and D for the session; no unit drift between USD/oz, ticks and "points" | whole report |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals; institutional trading-and-risk use; no retail tone | §1, §18 |
| 2.1 Sections present & ordered | §1 Executive Snapshot · §2 Market Definition · §3 Consensus Price Call · §4 Price Evidence Table · §5 Consensus Build · §6 Validated OHLC+RSI2 · §7 Charts · §8 Short-Term Technical · §9 Medium-Term Regime & VOLator · §10 Cross-Asset · §11 Floor Pivots · §12 Key Market Considerations · §13 Sentiment/News/Calendar (§13a per-article, §13b aggregate with numeric tilt, §13c prior calendar, §13d upcoming) · §14 Macro · §15 Bull/Bear · §16 Forward View · §17 Forecast (ONE sentence) · §18 Final Judgement · §19 Source Discipline Note · §20 Agent Log · §21 Strategy (§21a conviction, §21b cards, §21c 5-session backtest, §21d what-is-working + limitations) | headings |
| 2.2 Scorecard as a table | §6 is a table with Session/O/H/L/C/RSI2/Source A/Source B/Validation; §11 pivot tables ordered R3→P→S3 (three levels each side) for daily, weekly, monthly | §6, §11 |
| 2.3 Method steps visible | §4–§5 show observations → normalisation → consensus, with the futures-to-spot adjustment stated; §8 candle-by-candle; §9 regime with persistence/overlap/VOLator; §7 charts present (the .docx→.md conversion drops images — accept a caption or placeholder as evidence and note it; do not score the conversion) | §4–§9 |
| 3.1 Quantitative claims sourced | Every number in §1, §12, §14 carries a source or points to §4/§6/§13 | text |
| 3.2 Citations exist & contain data | You cannot fetch. Pick three cited sources: each must be named, dated, and quote a figure used consistently elsewhere. A source that is self-contradictory or impossible (wrong date, figure not matching its own quote) counts as fabricated and triggers the C3 override | §4, §13a |
| 3.3 Calculations transparent | RSI2 shown or reproducible: RS = mean gain / mean loss over 2 periods, RSI2 = 100 − 100/(1+RS) · pivots P=(H+L+C)/3, R1=2P−L, S1=2P−H, R2=P+(H−L), S2=P−(H−L), R3=H+2(P−L), S3=L−2(H−P) · ATR(14) stated · KER(13, EMA 3) stated · §21a score = Σ signal×weight | §6, §11, §9, §21a |
| 3.4 Numbers reconcile — **and reconcile against the level file** | Internally: D−1 close identical in §1, §3, §4, §6 and the §21b MARKET entry; §11 pivots = pivots quoted on the cards; ATR in §9 = §21. **Externally: §11's daily/weekly/monthly pivots, §6's O/H/L/C, the ATR14 and the swing extremes against `data/levels/XAUUSD_by_date/<D>.csv`.** See §4 below for tolerances | cross-section + level file |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a direction label consistent with their own content | those sections |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism (why USDX / real yields / silver / equity risk appetite matter for gold), not a correlation list | §10 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address conflicts between short- and medium-term reads, KER vs regime, §17 vs §21a | §15–§18, §21a |
| 4.4 Calibrated language | §17 exactly one sentence, no hedge stacking; confidence H/M/L stated where the framework asks | §3, §17 |
| 5.1 Data dated; staleness flagged | Every price and article dated; any single-source O/H/L flagged as indicative | §4, §6, §13, §19 |
| 5.2 Assumptions up front | The futures-to-spot normalisation stated with its size; any anchor override stated on the card AND in §20; single-source pivot propagation carried into the cards | §21b, §19, §20 |
| 5.3 Red flags surfaced | §12/§15 risks; §13d event collisions carried into card caveats | §12, §15, §21b |
| 5.4 Restrictions honoured | No synthesised or interpolated price presented as sourced; no retail dealer premium left un-normalised in the OHLC basis; futures corroboration-only; no bracketed variable names, no module codes (M1..M5), no framework name in the report body; instrument common names | whole report |

Card construction is ALSO scored under Category 4: see §3.

### The daily-open anchor — check this explicitly
`M1_Variables_v2_1.md` fixes `[DAILY_OPEN_ANCHOR]` to one of **00:00 UK or 07:00 UK**, selected once
at instance set-up, governing every run of that instance, and "**not re-selected at run time, per
session, or to suit when an analysis happened to finish**". A departure from the populated value is,
in the module's own words, "a logged non-conformance, not an anchor" — it must be recorded as such,
with the same converted time on the card, in the handoff record and in the report body, and must
never be presented as the instance's anchor value.

You cannot see the populated gold value (there is no gold M1). So judge what your own report does:
does it name an anchor, and does it treat a change as an override *logged as a non-conformance*
(compliant handling) or silently present it as the anchor (a 5.2 / 1.1 failure)? Report what you
find; do not assume what the other 56 reports do.

## 3. Card construction rules (M5, fixed) — what a compliant card must satisfy
- Direction score = Σ signal×weight; |score| < 0.25 → Trade 1 SUPPRESSED (an explicit SUPPRESSED row, not omission).
- Three equal units on every card. TP1 = entry ± 1R, TP2 = entry ± 2R for Trade 1 and RANGE Trade 2; on
  Unit 2 fill, Unit 3 stop → **entry ± 0.2R in the profitable direction** (for a SHORT that is *below*
  entry). Runner: session-close time-stop OR 3×ATR(14) price cap (Trade 1).
- Trade 1: market at the daily-open anchor. Stop = tighter of (5-day swing extreme, nearest S/R) +
  0.25×ATR buffer, capped at 3.5×ATR. Wide-stop flag if R > 1×ATR.
- Trade 2 by regime: RANGE → limit at S1/S1.5/S2 (long) or R1/R1.5/R2 (short), tier by distance in ATR,
  stop 3.5×ATR or structural + 0.25×ATR. TREND → entry at P + 0.10×(R1−P) (long), stop P − 0.8×(P−S1),
  TPs R1/R1.5/R2. TRANSITION → breakout side only.
- Trade 3A (trend): entry 57.5% retrace of a qualifying swing (magnitude ≥ 2×ATR, 4–10 session lookback,
  endpoints logged), stop beyond the 0% anchor by 0.25×ATR, TP1 38.2%, TP2 0%, TP3 100%+ extension.
  3B (range): limits at 11.4–21.4% / 78.6–88.6% of the 25-day range, stops 10% of width inside, TP1 mid,
  TP2 far side −10%. 3C (transition): confirmed close beyond the 25-day boundary by ≥ 0.25×ATR, stop at
  the boundary + 0.40×width, TP1 = +1.0×width, TP2 = 1.5×.
- Every card: thesis invalidation separate from the stop; confluences listed; stops and targets in both
  price and native units.
- Static integrity the scoring engine enforces: stop on the correct side; TP1 beyond entry; TP2 beyond
  TP1; TP3 beyond TP2 or null; 0.3×ATR14 ≤ R ≤ 3.0×ATR14; TP1 within 2.5×ATR14 of entry; a MARKET entry
  equals the D−1 close; a LIMIT/STOP level on the correct side of the D−1 close; anchor explicit.

### On the pivot-corroboration flag
A card's tier is CORROBORATED when the H/L/C used to compute it can be established. **The flag
describes the provenance of the H/L/C actually used to compute the tier, not the provenance of any
figure quoted elsewhere in the report.** Where the report struck a tier from a narrative or
aggregator quote whose true prior-period H/L cannot be established, the indicative flag is correct
and suppression may follow. Where you can now confirm the tier against the level file, say so — the
level file *is* the execution series, so a tier matching it is corroborated by construction. Do not
score a report down for an indicative flag that its own quoted evidence justified at the time, and
do not score it up for a tier that happens to match by luck while its stated basis was unsound.

## 4. Data basis for Category 3 checks — tolerances

The level file is the broker CFD/spot feed (broker time = UTC+3 = UK+2). Cash session = 16:30–23:00
broker, which is the US session and the gold volume peak. Both bases are given; **use the basis the
report itself claims**. A report quoting "spot, loco London, continuous" should be checked against
the `_full` columns; one quoting a US-session range against `_cash`.

Compare like with like. These reports normalise COMEX futures settlements to spot by subtracting a
stated contango of roughly USD 10–25. **A gap of that size against a figure the report itself labels
a futures settlement is expected and is not a defect** — the defect would be failing to state the
normalisation (row 5.2), or applying it inconsistently.

Tolerances, expressed against that date's `atr14_full` (typically ≈ USD 100/oz on gold, so the
absolute figures below are indicative):

| check | consistent | discrepancy to record | Category 3 failure |
|---|---|---|---|
| a close | ≤ 0.04×ATR14 (≈ USD 4) | 0.04–0.115×ATR | > 0.115×ATR14 (≈ USD 11.5) |
| an open / high / low | ≤ 0.09×ATR14 (≈ USD 9) | 0.09–0.20×ATR | > 0.20×ATR14 |
| a pivot level | ≤ 0.04×ATR14 | 0.04–0.115×ATR | > 0.115×ATR14 |
| ATR14 itself | ≤ 10% relative | 10–25% | > 25% |
| RSI2 | ≤ 5 points | 5–15 | > 15, or does not reproduce from the report's own five closes |

An RSI2 that does not reproduce from the report's own stated closes is a Category 3 failure
regardless of how close it lands to the file — that is an arithmetic error, not a basis difference.

## 5. What feedback may and may not contain
- **May**: the defect, the rule it violates, and the numeric condition a compliant level must satisfy,
  using the numbers in the level file (D−1 close, ATR14, pivots, swings). May: which reconciliation
  failed, which section is missing or malformed, which restriction was breached.
- **May not**: anything about what price did **on or after D**, or whether a trade would have worked.
  Your level file stops before D and that is the whole of your permitted knowledge. Do not open
  `data/raw/`, `results/`, any other date's level file, any other report, or the web.
