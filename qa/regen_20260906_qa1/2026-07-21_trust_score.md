# Trust Score — 2026-07-21 — SP500_Report_21-Jul-2026.md

Run: `regen_20260906_qa1` · Asset: US500 (S&P 500 cash index) · D = 2026-07-21 · D-1 slice = 2026-07-20
Evidence base: the report, `data/slices/{US500,VIX,USDX,NEWS}` to 2026-07-20, `cards/baseline/by_date/2026-07-21.json`,
`qa/regen_20260906_qa1/lint_static/2026-07-21.csv`, `reports/md/SP500_Report_20Jul2026.md` (prior report, cross-consistency only),
`engine/qa_slice_stats.py`. Nothing dated on or after D was opened.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is correctly the S&P 500 cash index (^GSPC), not ES futures. Counters are USDX · VIX · DAX 40 with USDX first, matching the required order. Lookback is 5 sessions (14–20 Jul) and §6 carries exactly five rows. Units are index points / USD throughout; §11 quotes to 0.01 tick. Six close observations are listed, meeting the ≥6 minimum, but all six sit in only two tiers (index provider via FRED, and financial media) — no exchange or sell-side tier appears. The daily-open anchor is described only as "session open anchor for 21 Jul (overridden anchor)"; the required 07:00 UK clock time is never written on the card or in §20 (the extracted card carries `anchor_broker 09:00`, i.e. 07:00 UK, so the intent is right but the report does not state it). The as-of field is set to 21 July 2026 rather than the NY close of D-1; the underlying price basis is genuinely the 20 Jul close, so this is a labelling deviation, not a data-currency error. | §2 (Asset, Lookback, As-of), §4 source list, §10 counter order, §20 anchor-override line, §21b Entry row | 3 | State the anchor as "07:00 UK" explicitly on the Trade 1 card; set the as-of field to the D-1 NY close; add at least one exchange or sell-side tier source, or state why the tier is unobtainable. |
| 1.2 Coverage & currency consistent | Every price observation is dated 20 Jul or earlier and the session labelled is D — correct in principle. No currency or unit drift anywhere. Two coverage faults: (a) the §10/§14 cross-asset levels are stale — VIX is given as "16.5 → 18.8" and USDX as "~100.7", which are the 17 Jul figures carried over from the prior report (the 20 Jul report quotes "VIX at 18.77"); the D-1 slice closes are VIX 18.02 and USDX 100.968, so the counter state presented as current is two sessions old. (b) §13a cites a CNBC article dated 19 Jul headlined "S&P 500 closes slightly lower on oil" — 19 July 2026 is a Sunday and there is no cash session on 18 or 19 Jul in the slice, so no close occurred on that date. | §10 counter table, §14 Liquidity & Positioning bullets, §13a row 4, VIX/USDX slices to 2026-07-20 | 2 | Refresh all §10/§14 counter levels to the D-1 (20 Jul) close and date them in-line; re-date or remove the 19 Jul article. |
| 1.3 Audience & tone | Register is consistently that of a senior US equity strategist writing for trading-and-risk review: labelled judgements, explicit invalidation levels, corroboration status stated rather than asserted. No retail framing, no promotional language, no advice-to-individual tone anywhere in §1, §18 or §21. | §1, §18, §21a–d | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 are present in the prescribed order. §13 carries all four sub-parts (13a per-article table, 13b aggregate with a numeric tilt of −0.34, 13c previous-period calendar, 13d upcoming calendar). §21 carries all four sub-parts (21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working plus the limitations boilerplate). §17 is a single sentence. §13d is present but every row is dated "This week" or "Ongoing" rather than to a session — weak, though the sub-section itself is not missing. | Headings throughout; §13a–d; §21a–d | 5 | Give §13d rows actual dates. |
| 2.2 Scorecard as a table | §6 is a proper table and carries all eleven required columns (Date/O/H/L/C/RSI2/Trend/Src A/Src B/Validation). §11 fails on two counts: the daily table runs R5→S5 (five levels each side) instead of the required R3→P→S3 three-a-side, and the **monthly pivot table is entirely absent** — the required set is daily, weekly and monthly, and the prior report (20 Jul) does carry a monthly block with P 7,457.15, so this is an omission in this run rather than an unsupported requirement. | §6 header row; §11 daily table (R5..S5), §11 weekly table, absence of any monthly block | 2 | Trim the daily pivot table to R3→P→S3 and add the missing monthly pivot table. |
| 2.3 Method steps visible | The chain is legible end to end: §4 lists raw observations with basis and relevance, §5 explains normalisation and why the weighted median collapses to a single value, §6 validates. §8 walks the five sessions candle-by-candle and then states a sequence assessment. §9 gives the regime with persistence, overlap, VOLator readings and a KER confirmation step. §7 carries five chart images (pandoc preserved the image references rather than dropping them) plus a VOLator caption. | §4→§5→§6 chain; §8 per-session bullets + Sequence assessment; §9 regime/VOLator/Kaufman; §7 five image refs | 5 | None. |
| 3.1 Quantitative claims sourced | Numbers that trace back to §6 or §11 are properly pointed ("see §6", "§13d", "daily S1 7,417"). But several load-bearing figures carry no source and no pointer: §12's "IBM's ~25% drop" and "SMH down ~9% over four weeks"; §1's "oil toward $90" and "VIX up more than 12%"; §14's "decliners > advancers ~1.9:1 on the NYSE 17 Jul"; and every level in the §10 counter table (USDX ~100.7, VIX 16.5→18.8, DAX 25,147→24,831) is unattributed. §13c's "−1.6% weekly index loss" and "VIX +12%" likewise have no source; the slice shows VIX 17 Jul 18.17 → 20 Jul 18.02, i.e. slightly lower over the 18–20 Jul window the row describes. The one macro claim that does check out is §13c's 14 Jul June CPI as "cooler than expected" — the calendar slice confirms CPI m/m −0.4 vs 0.5 consensus and y/y 3.5 vs 3.8. | §12 bullets 1 and 3, §14 bullets 3 and 5, §10 counter table, §13c rows 3–4; `data/slices/NEWS/news_upto_2026-07-20.csv` 2026-07-14 CPI rows | 2 | Attach a named, dated source to every §10/§12/§14 figure or delete the figure. Recompute the VIX percentage move over the window actually described. |
| 3.2 Citations exist & contain data | Three spot-checks all pass internal consistency: CNBC .SPX 20 Jul "−0.19% → 7,443.28" reconciles against the 17 Jul close (7,443.28/7,457.69 − 1 = −0.193%); Globe & Mail/Zacks 17 Jul "7,457.69 (−1.0%)" reconciles against the 16 Jul close (−1.010%); CNBC live blog 16 Jul "7,533.77 (−0.51%)" reconciles against the 15 Jul close (−0.510%). Two citations, however, sit at the fabrication boundary. (a) The §13a CNBC row dated 19 Jul is headlined "S&P 500 closes slightly lower" on a Sunday, when no cash session existed. (b) §6's 14 Jul row asserts "Close CORROB. (Δ0.00)" with Src A = S&P DJI and Src B = CNBC — but §4, which claims to hold all six close observations, contains **no 14 Jul close from any source** (its six closes cover only 15, 16, 17 and 20 Jul), and §5 states that this exact figure, 7,543.59, is what the *excluded* Investing.com CFD-derived series prints for 14 Jul. The prior report confirms the provenance: its §6 sources the 14 Jul row to "Investing / CORROBORATED". So a corroboration record is asserted for a session the report's own evidence table does not cover, naming two sources that are contradicted elsewhere in the same document. See §3 below for the override treatment. | §4 evidence table (no 14 Jul row), §5 CFD parenthetical, §6 Jul-14 Src A/Src B and Validation cells, §13a row 4 date, `reports/md/SP500_Report_20Jul2026.md` §6 | 1 | Remove the 14 Jul Src A/Src B corroboration claim unless a real 14 Jul close observation is added to §4; re-date or drop the 19 Jul article. |
| 3.3 Calculations transparent | Strong where it is shown. RSI2 reproduces **exactly** from the report's own close sequence for the three rows that can be tested without prior history: recomputation from (7,543.59 · 7,572.40 · 7,533.77 · 7,457.69 · 7,443.28) returns 42.7 / 0.0 / 0.0 against the report's 42.7 / 0.0 / 0.0, and the helper's RSI2 on slice closes (33.49 / 100.00 / 42.18 / 0.00 / 0.00) agrees within 1.49. All five Trend labels are correct under the stated rule. Daily pivots reproduce to the cent from the report's own 20 Jul H/L/C (7,491 / 7,429 / 7,443.28 → P 7,454.43, R1 7,479.85, R2 7,516.43, R3 7,541.85, S1 7,417.85, S2 7,392.43, S3 7,355.85) and the floor identity holds exactly: R2−P = 62.00 = P−S2. Weekly pivots are internally consistent too — inverting them gives H 7,588.99 / L 7,448.99 / C 7,457.70, and R2−P = 140.00 = P−S2. ATR (≈66) and KER (−0.12 against a ±0.13 band) are both stated. Three derivations fail to reproduce: (a) §21a lists five weighted signals summing to −0.565 against a stated score of −0.61, only five of the six defaulted weights are used, and no signal-to-weight mapping is given; (b) Trade 1's stop of 7,502 does not follow from its own stated anchor — the 16–17 Jul supply shelf at 7,500 plus 0.25×ATR(66) is 7,516.5; (c) Trade 3C's stop of 7,530 does not follow from its own stated formula — range_low 7,266 + 0.60×width 323 is 7,459.8. | Helper output (RSI2 rows 3–5 exact); §11 daily and weekly identity checks; §9 KER; §19 ATR; §21a signal list; §21b Trade 1 Stop row, Trade 3C Stop row | 2 | Show the §21a signal-to-weight mapping and make the components sum to the stated score. Recompute both card stops from their stated anchors and formulas, or restate the anchors actually used. |
| 3.4 Numbers reconcile | The headline close reconciles perfectly: 7,443.28 appears identically in §1, §3, §4, §6, §18 and as the Trade 1 entry reference in §21b. Card levels tie to §11 exactly (daily P 7,454, S1 7,417, S2 7,392, S3 7,356, R2 7,516; weekly S2 7,359). ATR ≈66 is consistent between §19 and both cards, and RSI2 is identical between §6, §8 and the §21a input. Five reconciliation failures: (a) **§6's 17 Jul row is an impossible bar — High 7,490.00 is below Open 7,500.00**; the prior report had a coherent 17 Jul bar (O 7,490.30 / H 7,498.47 / L 7,431.26) that matches the slice closely, so this run restated it into an invalid one. (b) §1 calls 7,572 the "intraday-week peak" while §6 and §8 give the week's intraday high as 7,589 — 7,572.40 is the 15 Jul *close*. (c) §8 places the 5-day swing low at 7,429 on 20 Jul; the slice puts it at 7,431.60 on 17 Jul — wrong session as well as wrong level. (d) Trade 3C's entry reference is 7,417 in the card text but 7,443 in the extracted card, and the extract carries a TP3 of 6,800 that appears nowhere in the report. (e) §21c implies three different R values across the five Trade 1 rows (7,537→7,543 at +0.1R implies R≈60; 7,566→7,534 at +0.5R implies R≈64; 7,500→7,458 at +1.0R implies R≈42) and labels the 17 Jul row "(TP1)" when 42 points falls short of a 60-point 1R. | §6 Jul-17 row; §1 vs §6/§8; §8 Nearest support line vs helper 5d swing; §21b Trade 3C vs `cards/baseline/by_date/2026-07-21.json`; §21c Outcome column | 2 | Fix the 17 Jul bar so H ≥ max(O,C) and L ≤ min(O,C). Reconcile the §1 peak, the §8 swing-low session, the Trade 3C entry between text and card, and the §21c R denominators. |
| 4.1 Pillars conclude | Every pillar terminates in an explicit label consistent with its own content: §8 "Judgement label: Bearish continuation"; §9 "Bias: Bearish" plus a preferred trade protocol; §10 "Aggregate cross-asset: CONFIRM (bearish)"; §12 tags each of its five drivers (PRICE-NEGATIVE / NEUTRAL-TO-NEGATIVE / etc.); §14 tags each of its five bullets. Two soft spots: §12's FX bullet carries a double label ("MILDLY SUPPORTIVE / net NEUTRAL"), and §14 labels its bullets but never states an aggregate macro direction the way §8/§9/§10 do. | §8 Judgement label, §9 Bias, §10 Aggregate line, §12 and §14 bullet tags | 4 | Add an aggregate direction label to §14; resolve the §12 FX double label to one. |
| 4.2 Peer/cross-asset interpreted | §10 does give real transmission mechanisms rather than a correlation list — weaker USD easing financial conditions, higher implied vol as a direct inverse to SPX, DAX as the European leg of a common global-risk factor — and it aggregates them into CONFIRM with the dissenting counter identified. The weakness is that the USDX mechanism is built on a directional read the data does not support: §10 says "Flat / slightly lower", and §12/§14 then build a "softening USD" earnings-translation argument on it, but the slice shows USDX flat-to-slightly-higher across the window (14 Jul 100.910 → 20 Jul 100.968). The mechanism is sound; the direction it is applied to is not. | §10 Mechanism column and Aggregate line; §12 Macro/FX bullet; §14 Liquidity & FX bullet; USDX slice to 2026-07-20 | 3 | Re-read the USDX direction off the D-1 slice and restate the FX mechanism to match it. |
| 4.3 Synthesis reconciles tensions | §16 does reconcile the short- and medium-term reads and names a base-case invalidation (a daily close above 7,516); §15 balances upside and downside with section pointers; §18 stays consistent with both; §17 and §21a both resolve SHORT with no conflict. §9 explicitly declines to resolve the KER-vs-VOLator conflict ("flagged rather than resolved") — defensible, but it pushes the reconciliation downstream. The dominant failure in this row is **card construction**, which the protocol scores here. Trade 2's suppression is correct and correctly presented as a SUPPRESSED row. Trade 1 is geometrically clean (R = 59 pts = 0.89×ATR; TP1/TP2 exactly at 1R/2R; three equal units; correct runner rule) but its stop does not derive from its stated anchor, and its confluence claim is wrong — TP1 7,384 is 28 pts from daily S3 7,356 and 25 pts from weekly S2 7,359, while daily S2 7,392.43 sits 8 pts away and is not mentioned. Trade 3C breaks the 3C rule set in three places: the confirmation trigger is a pivot (a close below daily S1 7,417) rather than a close beyond the 25-day boundary by ≥0.25×ATR; the stop uses a 0.60×width coefficient where the rule specifies 0.40×width, and even then does not compute; and TP1 is anchored to the pivot rather than the broken boundary, landing 4.51×ATR from entry against a 2.5×ATR ceiling. The card also states no R in points. | §16 invalidation; §9 Kaufman confirmation paragraph; §21b all three cards; `cards/baseline/by_date/2026-07-21.json`; lint row `WARN_TARGET_FAR(4.51xATR)` | 2 | Rebuild Trade 3C against the 25-day boundary (see feedback items 4–8); re-derive the Trade 1 stop and correct its confluence. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single clean conditional and no hedge stacking; confidence is stated as High in both §3 and §18; §21a states the score and that it clears the threshold. Against that, §21d overstates its own evidence: it claims "TP1/TP2/TP3 hit rates ≈ 60% / 0% / 0%" when the §21c table it aggregates shows at most two of five Trade 1 rows reaching TP1 (40%), and one of those is only a "TP1 partial". §21c's own "+1.0R (TP1)" label on 17 Jul is similarly uncalibrated against a 42-point move. The mean R of +0.44 does reproduce from the table's own R values. | §17; §3 and §18 confidence; §21d hit-rate sentence vs §21c Outcome column | 4 | Recompute the §21d hit rates from the §21c rows, or state the count rather than a percentage on n=5. |
| 5.1 Data dated; staleness flagged | This is the report's genuine strength. Every price row in §4 and §6 carries a date, every §13a article carries a date, and the single-source-indicative status of Open/High/Low is flagged consistently and in four separate places (§4 note, §6 note, §11 Source status, §19), with the consequence spelled out (indicative levels cannot anchor limit orders, which propagates to the Trade 2 suppression). §19 also flags the ATR as indicative because it is built on indicative H/L. Two failures pull the score down: the §10/§14 counter levels are undated and are in fact the 17 Jul values presented as the current state, and the 19 Jul article date is not a viable session date. | §4 note, §6 note, §11 Source status, §19 bullets 1–4; §10 counter table (undated); §13a row 4 | 3 | Date the §10/§14 counter readings and refresh them to D-1. |
| 5.2 Assumptions up front | The anchor override is disclosed in §20 and echoed on the Trade 1 card as "(overridden anchor)". The single-source pivot propagation is stated in §11 and §19 and is actually honoured downstream — Trade 2 is suppressed for exactly that reason and both live cards carry an "Indicative O/H/L & ATR" caveat. The gap is that neither §20 nor the card states the anchor's clock time, so a reader cannot tell which open the entry is struck at; the framework asks for the assumption to be explicit, and "session open anchor" is not. | §20 anchor-override bullet; §21b Entry and Caveats rows; §11 Source status; §19 bullet 4 | 4 | Write the anchor time (07:00 UK) into both §20 and the Trade 1 card. |
| 5.3 Red flags surfaced | Risks are surfaced properly and carried through. §12 flags the AI/semiconductor de-rating, the geopolitical oil channel and the earnings cluster; §15 sets them against named upside risks with section pointers; §19 discloses the data gaps and their consequences; §20 logs the blocked and excluded sources by name. Critically for this row, the §13d event collision is carried into the card caveats — both live cards state "earnings-event risk (§13d)" — and §21b Trade 1's caveat names the holding-period collision explicitly. | §12 bullets, §15 table, §19 Data gaps bullet, §20 Sources attempted, §21b Caveats rows on both live cards | 5 | None. |
| 5.4 Restrictions honoured | **Breached.** §20 contains the bracketed variable name `[DAILY_OPEN_ANCHOR]`, which the instance restrictions prohibit outright, and the same section leaks further engine tokens into the delivered text: `regime_label = TRANSITION`, `TREND_DOWN/RANGE`, and "Step-4 synthesis". §4 and §19 additionally leak prompt-layer language into the report body ("per instance restrictions", "the instance's no-CFD restriction", "per the run instruction"). Separately, the no-CFD-in-OHLC restriction is at best in doubt: §5 identifies 7,543.59 as the Investing.com CFD-derived 14 Jul close and §6 carries 7,543.59 as that session's validated close, attributed to S&P DJI × CNBC — and the prior report sourced the same row to Investing.com. On the credit side, ES futures are not cited anywhere and instrument common names are used throughout. | §20 `[DAILY_OPEN_ANCHOR]`, `regime_label`, `TREND_DOWN/RANGE`; §4 Notes column; §19 bullets 1 and 5; §5 CFD parenthetical vs §6 Jul-14 row | 1 | Strip all bracketed variable names, engine tokens and prompt-layer references from the delivered text; establish and state a non-CFD provenance for the 14 Jul close or drop its corroboration claim. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 · Prompt adherence and instruction compliance (max 20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 3/2/5, mean 3.33 → level 3; the restriction-breach override then drops C1 one level to 2. Asset, counters, lookback and units are all respected, but the anchor time is never stated, the as-of is labelled D rather than the D-1 NY close, and the counter block is two sessions stale. |
| C2 · Structural and modular framework alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/2/5, mean 4.0. All twenty-one sections and every sub-section are present, ordered, and the method chain is fully visible; the loss is confined to §11, which omits the monthly pivot table and runs five levels a side instead of three. |
| C3 · Accuracy, evidence, and factual reliability (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/1/2/2, mean 1.75 → 2. RSI2, the trend rule and both pivot sets reproduce exactly and the headline close reconciles across every section — but §6 contains an impossible 17 Jul bar, four O/H/L values miss the slice by 12–56 pts, the 14 Jul corroboration is unsupported by §4, and several §10/§12/§14 figures carry no source at all. |
| C4 · Reasoning, judgment, and evaluation quality (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 4/3/2/4, mean 3.25 → 3. Pillars conclude cleanly and §10 supplies real mechanisms, but the USDX direction is wrong, §21d overstates its own hit rates, and card construction — which the protocol scores here — breaks the 3C rule set in three places and leaves the Trade 1 stop underived. |
| C5 · Currency, risk awareness, restrictions, transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 3/4/5/1, mean 3.25 → 3. Dating, indicative-status flagging and red-flag propagation to the cards are genuinely strong; the row is dragged down by a plain restriction breach in §20 and by stale, undated counter levels. |
| **Total** | — | — | **57.75 → 58** | Σ(multiplier × max) = 8.00 + 17.00 + 10.00 + 13.00 + 9.75. |

## 3. Total, band, override check

**Raw total: 57.75, rounded to 58. Band: Low Trust (40–59). Override applied: restriction_breach.**

*Restriction-breach override — APPLIED.* §20 of the delivered report contains the bracketed variable name
`[DAILY_OPEN_ANCHOR]`, together with the engine tokens `regime_label = TRANSITION` and `TREND_DOWN/RANGE`, and
§4/§19 carry prompt-layer language ("per instance restrictions", "per the run instruction") into the report body.
The instance restrictions prohibit bracketed variable names and module/engine codes in the output. Per the framework
this caps the total at Moderate Trust (60–74) and reduces Category 1 by at least one rubric level. Category 1 has
been reduced from its checklist mean of 3 to 2, which is reflected in the roll-up above. The 74 cap does not bind,
because the total of 58 already sits below it.

*Hallucinated-source override — CONSIDERED, NOT APPLIED.* Two citations sit at the boundary and both are recorded
under row 3.2. (a) §13a cites a CNBC article dated 19 Jul 2026 — a Sunday, with no cash session on 18 or 19 Jul in
the slice — headlined "S&P 500 closes slightly lower on oil"; a close cannot have occurred on that date, although a
weekend recap piece published on a Sunday is not in itself impossible, which is why this is treated as a dating error
rather than an invention. (b) §6's 14 Jul row claims "Close CORROB. (Δ0.00)" naming S&P DJI and CNBC, while §4
contains no 14 Jul close observation from any source and §5 attributes that exact figure to the *excluded*
Investing.com CFD series; the prior report confirms the 14 Jul row originated from Investing.com. This is a real
source mis-attributed to an uncorroborated figure, not a source that does not exist, so it is scored as an evidence
failure (row 3.2 = 1, driving C3 to 2) rather than as fabrication. **A reviewer applying the brief's
"self-contradictory or impossible counts as fabricated" clause strictly would trigger the override**, setting C3 = 0
and the total to 8.00 + 17.00 + 0 + 13.00 + 9.75 = 47.75 → 48. The band is **Low Trust under either reading** and the
required action — full regeneration — is identical, so the choice of override does not change the operational outcome.

*Band consequence.* Low Trust: not suitable for use; may be salvaged for skeleton or framing only. Full prompt review
and regeneration required, and the prompt template should be investigated — the bracketed-variable leak and the
restated-into-invalid 17 Jul bar both suggest a template or hand-off fault rather than a one-off slip.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-21.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-21_Trade_1 | 2026-07-21 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-21_Trade_2 | 2026-07-21 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False |
| 2026-07-21_Trade_3C | 2026-07-21 | Trade 3C - Momentum-Breakout (conditional short) | WARN_TARGET_FAR(4.51xATR) | False |

Per-card integrity, `100 − 40·(#DUD) − 10·(#WARN)`, floored at 0:

| Card | #DUD | #WARN | Integrity | Note |
|---|---|---|---|---|
| 2026-07-21_Trade_1 | 0 | 0 | **100** | CLEAN. Stop 7,502 is on the correct side of a short entry at 7,443; TP1 7,384 is beyond entry and TP2 7,325 beyond TP1; TP3 7,245 beyond TP2; R = 59 pts = 0.89×ATR(66), inside the 0.3–3.0×ATR band; TP1 is 0.89×ATR from entry, inside the 2.5×ATR ceiling; the MARKET entry equals the stated D-1 close. |
| 2026-07-21_Trade_2 | — | — | **suppressed — excluded from the mean** | Correctly suppressed under the M5 rule that Trade 2 is suppressed when every pivot tier is single-source-indicative, and correctly presented as a SUPPRESSED row rather than omitted. |
| 2026-07-21_Trade_3C | 0 | 1 | **90** | One WARN: TP1 7,094 sits 4.51×ATR from the extracted entry of 7,443, against the 2.5×ATR ceiling. Geometry is otherwise valid — stop 7,530 above a short entry, TP1 beyond entry, TP2 6,933 beyond TP1, TP3 6,800 beyond TP2, R = 87 pts = 1.32×ATR. |

**Report-level Card Integrity = mean over non-suppressed cards = (100 + 90) / 2 = 95.0**

Counts for the roll-up CSV: n_cards = 3 (all rows in the lint file), n_duds = 0, n_warns = 1.

Note that Card Integrity is a static-geometry score and is deliberately not folded into the 100. It is high here
because both live cards are internally well-formed; the substantive card faults — Trade 3C triggering off a pivot
instead of the 25-day boundary, the wrong stop coefficient, and Trade 1's underived stop — are rule-construction
failures that the static linter cannot see, and they are scored under row 4.3 instead.

## 5. Data reconciliation log

Slice basis: `data/slices/US500/US500_upto_2026-07-20.csv`, cash session 16:30–23:00 broker (09:30–16:00 ET), via
`engine/qa_slice_stats.py`. Tolerances per the reviewer brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.
Sign convention: delta = report − slice.

### 5.1 §6 Validated OHLC table vs slice cash session

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | Jul 14 Open | 7,536.70 | 7,535.70 | +1.00 | OK |
| §6 | Jul 14 High | 7,557.44 | 7,559.70 | −2.26 | OK |
| §6 | Jul 14 Low | 7,513.23 | 7,512.90 | +0.33 | OK |
| §6 | Jul 14 Close | 7,543.59 | 7,546.40 | −2.81 | OK (within 3) — but see §5.5, provenance disputed |
| §6 | Jul 15 Open | 7,548.00 | 7,569.10 | **−21.10** | DISCREPANCY (>8) |
| §6 | Jul 15 High | 7,589.00 | 7,582.80 | +6.20 | OK |
| §6 | Jul 15 Low | 7,541.00 | 7,528.60 | **+12.40** | DISCREPANCY (>8) |
| §6 | Jul 15 Close | 7,572.40 | 7,573.90 | −1.50 | OK |
| §6 | Jul 16 Open | 7,566.00 | 7,554.00 | **+12.00** | DISCREPANCY (>8) |
| §6 | Jul 16 High | 7,566.00 | 7,572.20 | −6.20 | OK |
| §6 | Jul 16 Low | 7,500.00 | 7,506.00 | −6.00 | OK |
| §6 | Jul 16 Close | 7,533.77 | 7,536.20 | −2.43 | OK |
| §6 | Jul 17 Open | 7,500.00 | 7,443.70 | **+56.30** | DISCREPANCY (>8), largest in the table |
| §6 | Jul 17 High | 7,490.00 | 7,497.30 | −7.30 | OK on magnitude, but **invalid bar: High 7,490.00 < Open 7,500.00** |
| §6 | Jul 17 Low | 7,449.00 | 7,431.60 | **+17.40** | DISCREPANCY (>8) |
| §6 | Jul 17 Close | 7,457.69 | 7,456.60 | +1.09 | OK |
| §6 | Jul 20 Open | 7,455.00 | 7,495.30 | **−40.30** | DISCREPANCY (>8) vs cash; vs full-day open 7,450.10 it is +4.90 (basis ambiguity, but the report declares a cash basis in §2) |
| §6 | Jul 20 High | 7,491.00 | 7,512.80 | **−21.80** | DISCREPANCY (>8) on both cash and full-day bases |
| §6 | Jul 20 Low | 7,429.00 | 7,439.30 | **−10.30** | DISCREPANCY (>8) vs cash; −8.80 vs full-day 7,437.80 |
| §6 | Jul 20 Close (D-1) | 7,443.28 | 7,446.60 | **−3.32** | Marginal discrepancy (>3 by 0.32); −1.02 vs the full-day close 7,444.30. Not a Category 3 failure (well under 10 pts) |

### 5.2 §6 RSI2 column — two independent tests

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | Jul 14 RSI2 | 32.0 | 33.49 (helper, slice closes) | −1.49 | OK |
| §6 | Jul 15 RSI2 | 100.0 | 100.00 (helper, slice closes) | 0.00 | OK |
| §6 | Jul 16 RSI2 | 42.7 | 42.18 (helper, slice closes) | +0.52 | OK |
| §6 | Jul 16 RSI2 | 42.7 | **42.7** (recomputed from the report's own closes) | 0.00 | **PASS — arithmetic exact** |
| §6 | Jul 17 RSI2 | 0.0 | **0.0** (recomputed from the report's own closes) | 0.00 | **PASS — arithmetic exact** |
| §6 | Jul 20 RSI2 | 0.0 | **0.0** (recomputed from the report's own closes) | 0.00 | **PASS — arithmetic exact** |
| §6 | Jul 14/15 RSI2 | 32.0 / 100.0 | n/a | — | Not testable from the report's own closes alone (needs history before the window); both agree with the slice within 1.49 |
| §6 | Trend column | Neutral/Bullish/Bearish/Bearish/Bearish | Rule applied to the report's own O/C and RSI2 | — | PASS — all five labels correct |

### 5.3 §11 Floor pivots — reproduction and identity

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §11 daily | P | 7,454.43 | 7,454.43 from the report's own 20 Jul H 7,491 / L 7,429 / C 7,443.28 | 0.00 | PASS — reproduces |
| §11 daily | R1 / S1 | 7,479.85 / 7,417.85 | 7,479.85 / 7,417.85 | 0.00 / 0.00 | PASS |
| §11 daily | R2 / S2 | 7,516.43 / 7,392.43 | 7,516.43 / 7,392.43 | 0.00 / 0.00 | PASS |
| §11 daily | R3 / S3 | 7,541.85 / 7,355.85 | 7,541.85 / 7,355.85 | 0.00 / 0.00 | PASS |
| §11 daily | Floor identity | R2−P = 62.00 | P−S2 = 62.00 | 0.00 | **PASS — identity holds exactly** |
| §11 daily | Table shape | R5→S5, five levels each side | R3→P→S3 required | — | Structural deviation (row 2.2) |
| §11 daily | P (vs slice) | 7,454.43 | 7,466.23 (slice cash D-1) | −11.80 | Propagated from the wrong 20 Jul H/L |
| §11 daily | R1 / R2 / R3 (vs slice) | 7,479.85 / 7,516.43 / 7,541.85 | 7,493.17 / 7,539.73 / 7,566.67 | −13.32 / −23.30 / −24.82 | Propagated error, resistance side understated |
| §11 daily | S1 / S2 / S3 (vs slice) | 7,417.85 / 7,392.43 / 7,355.85 | 7,419.67 / 7,392.73 / 7,346.17 | −1.82 / −0.30 / +9.68 | Support side lands close despite the input error |
| §11 weekly | Implied H / L / C | 7,588.99 / 7,448.99 / 7,457.70 | Inverted from the report's own R1/S1/P | — | PASS — internally consistent; C matches the 17 Jul close 7,457.69 |
| §11 weekly | Floor identity | R2−P = 140.00 | P−S2 = 140.00 | 0.00 | **PASS — identity holds exactly** |
| §11 weekly | P (vs slice) | 7,498.56 | 7,490.33 | +8.23 | Minor, from indicative weekly H/L |
| §11 weekly | S2 / S3 (vs slice) | 7,358.56 / 7,268.13 | 7,339.13 / 7,246.67 | +19.43 / +21.46 | Discrepancy, propagated from indicative bounds |
| §11 monthly | entire table | **absent** | required | — | **MISSING SECTION** (present in the prior report) |

### 5.4 Derived levels, ATR, swings and counters

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §19 / §21b | ATR(14) | ≈ 66 | 69.70 (cash) / 77.46 (full-day) | −3.70 / −11.46 | Acceptable against cash given indicative H/L; flagged indicative in §19 |
| §8 | 5-day swing low | 7,429, attributed to 20 Jul | 7,431.60, set on **17 Jul** | −2.60 | Wrong session; level marginal |
| §8 | 5-day swing high | 7,589 (15 Jul) | 7,582.80 (15 Jul) | +6.20 | OK, session correct |
| §9 / §21b | 25-day range high | 7,589 | 7,582.80 | +6.20 | OK |
| §9 / §21b | 25-day range low | 7,266 | 7,303.10 (26 Jun) | **−37.10** | DISCREPANCY — drives the Trade 3C boundary error |
| §21b | 25-day range width | 323 | 279.70 | **+43.30** | DISCREPANCY — inflates every 3C measured-move target |
| §10 / §14 | VIX level | 18.8 ("high-18s") | 18.02 (20 Jul close) | +0.78 | Stale: 18.8 is the 17 Jul figure carried from the prior report |
| §10 | VIX 5-day start | 16.5 | 17.37 (14 Jul close) | −0.87 | Start value does not occur in the window (window low 17.47 on 20 Jul; 16.61 was 10 Jul) |
| §1 / §13c | VIX move | "+12%" / "more than 12%" | 17.37 → 18.02 = +3.7% over the window; 18.17 → 18.02 = −0.8% over the 18–20 Jul window §13c describes | ≈ −8 to −13 pp | DISCREPANCY — move materially overstated |
| §10 / §12 / §14 | USDX level | ~100.7, "flat / slightly lower", "softening" | 100.968 (20 Jul close); 100.910 (14 Jul close) | −0.27; direction flat-to-**higher** | Stale (100.751 is the 17 Jul close) and the stated direction is not supported |
| §10 | DAX 40 | 25,147 → 24,831 | not verifiable — no DAX slice in the permitted input set | — | Unverified; unsourced in the report |
| §13c | 14 Jul June CPI "cooler than expected" | qualitative | CPI m/m −0.4 vs 0.5 consensus; y/y 3.5 vs 3.8 | — | **PASS — confirmed by the calendar slice** |

### 5.5 Cross-section and cross-report reconciliation

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §1 / §3 / §4 / §6 / §18 / §21b | D-1 close | 7,443.28 in all six locations | — | 0.00 | **PASS — fully reconciled** |
| §11 vs §21b | Card pivot levels | S3 7,356 · S2 7,392 · S1 7,417 · P 7,454 · R2 7,516 · weekly S2 7,359 | §11 values 7,355.85 · 7,392.43 · 7,417.85 · 7,454.43 · 7,516.43 · 7,358.56 | ≤ 0.56 | **PASS — cards quote §11 correctly** |
| §6 vs §8 vs §21a | RSI2 | 32.0 / 100.0 / 42.7 / 0.0 / 0.0 | identical in all three | 0.00 | **PASS** |
| §19 vs §21b | ATR | ≈66 in both | — | 0.00 | **PASS** |
| §1 vs §6 / §8 | "7,572 intraday-week peak" | 7,572 | 7,589 is the week's intraday high; 7,572.40 is the 15 Jul close | −17 | Internal inconsistency (a close described as an intraday peak) |
| §5 vs §6 | 14 Jul close 7,543.59 | §6: official close, Src A S&P DJI / Src B CNBC, "CORROB. (Δ0.00)" | §5: the Investing.com CFD-derived close "on a shifted basis"; §4 contains no 14 Jul close at all | — | **CONTRADICTION** — same figure, two mutually exclusive provenances |
| §6 vs prior report §6 | 14 Jul row source | S&P DJI / CNBC | `SP500_Report_20Jul2026.md` §6: "Investing / CORROBORATED" | — | Cross-report contradiction; supports the §5 reading |
| §6 vs prior report §6 | 17 Jul O/H/L | 7,500.00 / 7,490.00 / 7,449.00 | prior report 7,490.30 / 7,498.47 / 7,431.26 (matches the slice to ~1 pt on H and L) | +9.70 / −8.47 / +17.74 | **REGRESSION** — a previously coherent, slice-consistent bar was restated into an invalid one |
| §6 vs prior report §6 | 15 / 16 Jul O/H/L | rounded to whole points | prior report carries two-decimal values throughout | — | O/H/L for four of five sessions are rounded to whole points, consistent with re-estimation rather than sourcing |
| §21b vs baseline card | Trade 3C entry | 7,417 (card text reference) | 7,443 (`cards/baseline/by_date/2026-07-21.json`) | −26 | Card text and extracted card disagree |
| §21b vs baseline card | Trade 3C TP3 | "discretionary trail", no number | 6,800 in the extracted card | — | Extracted level has no basis in the report text |
| §21a | Direction score | −0.61 | −0.565 (sum of the five stated components) | −0.045 | Components do not sum to the stated score; one of six weighted signals is unstated |
| §21c | Implied R per row | +0.1R on 6 pts, +0.4R on 24 pts, +0.5R on 32 pts, +1.0R on 42 pts, +0.2R on 12 pts | implies R ≈ 60 / 60 / 64 / 42 / 60 | — | Inconsistent R denominator; the 17 Jul row is labelled "(TP1)" on a move short of its own 1R |
| §21c / §21d | Mean R | +0.44 | (0.1+0.4+0.5+1.0+0.2)/5 = 0.44 | 0.00 | PASS — reproduces from the table |
| §21d | TP1 hit rate | ≈ 60% | 2 of 5 Trade 1 rows reach TP1 (one of them a "partial") = 40% | −20 pp | Not supported by §21c |
| §13a | CNBC article date | 19 Jul 2026, "S&P 500 closes slightly lower" | 19 July 2026 is a Sunday; no 18 or 19 Jul session exists in the slice | — | Impossible session date for the headline |
| §2 / header | As-of | 21 July 2026 | required: NY close of D-1 (20 July 2026) | — | Labelling deviation; the underlying price basis **is** genuinely D-1 (20 Jul close, confirmed against the slice) |
