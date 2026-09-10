# Trust Score — XAUUSD Gold Daily Report — 2026-07-31

Run: `gold_regen_qa1` · Report: `reports/md/Gold_Report_31Jul2026.md` · Level file: `data/levels/XAUUSD_by_date/2026-07-31.csv`
(`last_bar_date`=2026-07-30 < D=2026-07-31 — confirmed leak-free before use.)
Basis used for Category 3 checks: **`_full`** (report states "Spot, immediate settlement (loco London)"; the `_cash`
columns give an equally poor or worse match everywhere it was cross-checked, e.g. D−1 close $4,112.12 cash vs
$4,066.38 reported).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot loco London with GC=F named as corroboration only (never actually quoted — see 2.3/5.2); USDX listed first among counters; ≥6 sources (8 listed); tick 0.01 USD/oz stated and used consistently in tick math ($71→7,100 ticks, $45→4,500 ticks). Daily-open anchor deviation (00:00 UK→07:00 UK) is handled exactly as the module requires: logged as a non-conformance in §20, restated on the card and in §21/footer, same converted time (09:00 broker) throughout. | §2, §4, §20, §21, card JSON `anchor_broker` | 5 |
| 1.2 Coverage & currency consistent | All dated items fall in 24–31 Jul (D−1 block) or D; USD/oz used throughout, no unit drift. | whole report | 5 |
| 1.3 Audience & tone | Institutional, "Senior Commodities Analyst" register maintained; no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 (incl. 13a–d, 21a–d) present and correctly ordered. | headings | 5 |
| 2.2 Scorecard as table | §6 is a real table but collapses Source A/B into one "Src A / B" column (spec: two columns). §11 daily pivot table shows **5** levels each side (R5..S5) instead of the specified 3 (R3→P→S3); weekly/monthly tables correctly show 3 each side. | §6, §11 | 4 |
| 2.3 Method steps visible | §5 explicitly claims a third source category — "futures-linked reads" — that is normalised and blended into the consensus. **No futures-linked (GC=F) quote appears anywhere in §4, and no contango/normalisation size is ever stated.** The futures-to-spot adjustment step is announced but not shown; this is a real evidence gap, not merely an omitted category. | §4, §5 | 3 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§13 (WGC 244t/89%, Fed 3.50–3.75%, USDX~100). §14's "US CPI 3.5% (Jun)" has no source and does not appear in §13c/§13d. | §14 | 4 |
| 3.2 Citations exist & contain data | 3 spot-checked (WGC 89% figure, FXLeaders "central bank buying offsets…", RoboForex "towards 3,975") are each named, dated and used consistently with §1/§4/§12. No fabrication found. | §4, §13a | 5 |
| 3.3 Calculations transparent | RSI2 formula/basis stated (§6 note) and reproduces from the report's own 5 closes (two up-closes in the trailing 2-period window ⇒ RSI2=100, matches report). Pivot formulas not shown inline (acceptable, fixed by module). **ATR14 is never stated as an explicit figure anywhere in §9** — only inferable by back-solving card multiples ($23.64/0.25≈$94.6, $4,350 cap/3≈$94.7), which is not the same as "ATR(14) stated." | §6, §9, §21b | 3 |
| 3.4 Numbers reconcile — incl. vs level file | **Internally** consistent (§1/§3/§4/§6/§11 all point to the same ~$4,066 close/pivot cluster). **Externally, against `data/levels/XAUUSD_by_date/2026-07-31.csv` (`_full`), this fails badly and pervasively:** D−1 close off by $37.23 (fail threshold $9.99 — ~3.7×over), D−1 open off by $18.34 (fail threshold $17.38), daily P/R1/S1/S2/R3/S3 all fail (diffs $14.49–$35.48 vs a $9.99 failure line), weekly P/R1/S1/R2/R3 all fail (diffs $12.61–$61.22), every monthly level fails (diffs $53.66–$272.64), and the 25-day swing high used for Trade 3C ($4,382.85) is $180.14 above the file's $4,202.71 (the June $4,383 high the report cites is outside the file's 25-session full-basis window). Only D−1 high, D−1 low, daily R2, weekly S2/S3, and the two 5-day swings reconcile within tolerance. | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8 "Indecision", §9 "Neutral-to-bearish"/Transitional, §10 "MIXED", §12 bullets each carry a supportive/negative/neutral label. §14 ends without an explicit direction label (implicit only). | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanism (opportunity cost via USDX, risk-on capital competition), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly reconcile the USDX/silver-vs-equities tension; §21a explicitly flags "no directional conflict to resolve" between the NEUTRAL score and the §17 range call. | §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is one sentence; confidence stated as Medium in §3. | §3, §17 | 4 |
| **Card construction (folds into C4)** | Trade 2 and Trade 3C formulas are correctly applied to their own (wrong-base) inputs — internally sound arithmetic. **Trade 1's stop is not actually built from its own stated formula:** the card says "5-day swing low $3,996 + 0.25×ATR buffer" but sets stop at $3,995 — only ~$1 below the swing low, not swing_low − 0.25×ATR14 (~$21.72 on the file's ATR). Trade 1's "wide-stop flag" is also inconsistent with its own rule (flag fires only if R > 1×ATR; R=$71 < ATR≈$87–95). Linter (static, leak-free): Trade 1 CLEAN, Trade 2 CLEAN, Trade 3C WARN_R_HUGE(3.30×ATR) + WARN_TARGET_FAR(4.78×ATR), no DUDs. | cards JSON, lint_static, §21b | 3 |
| 5.1 Data dated; staleness flagged | Every price/article dated; single-source O/H/L explicitly flagged SINGLE-SOURCE INDICATIVE throughout §4/§6/§11/§19. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Daily-open anchor override stated on card + §20 + body (compliant). Single-source pivot propagation is disclosed on all 3 cards. **The futures-to-spot normalisation is claimed in §5 ("Provider types...futures-linked reads...were not blended") but its size is never stated because no futures figure is ever shown** — an assumption announced but not actually surfaced. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 risks present and reasonably framed. §13d flags the 31 Jul Chicago PMI/UMich print as the "Highest-impact upcoming event" — **but none of the three §21b card caveat rows mention this same-day event risk**, even though Trade 1 executes at the 31 Jul open, i.e. into that print. | §12, §15, §21b | 3 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) in the body; instrument common names used; GC=F correctly kept out of the price-evidence blend (though also never shown at all — see 2.3/5.2). | whole report | 4 |

## 2. Category roll-up

| Cat | Checklist mean | Level (rounded) | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (5+5+5)/3 = 5.00 | 5 | 1.00 | 20 | 20.00 | All variables respected; anchor deviation logged exactly as the module requires. |
| C2 Structure | (5+4+3)/3 = 4.00 | 4 | 0.85 | 20 | 17.00 | All sections present/ordered; scorecard column and pivot-count deviations; futures normalisation step announced but never evidenced. |
| C3 Accuracy & evidence | (4+5+3+1)/4 = 3.25 | 3 | 0.65 | 25 | 16.25 | Internally self-consistent but the D−1 close, nearly every daily/weekly/monthly pivot, and the 25-day swing high all fail external reconciliation against the leak-free level file by multiples of the tolerance. |
| C4 Reasoning & judgment | (4+5+5+4+3)/5 = 4.20 | 4 | 0.85 | 20 | 17.00 | Pillars conclude and synthesis reconciles tensions well; card construction is formulaically sound on Trades 2/3C but Trade 1's stop-buffer is not actually applied and its wide-stop flag misfires against its own rule. |
| C5 Currency & transparency | (5+3+3+4)/4 = 3.75 | 4 | 0.85 | 15 | 12.75 | Data well-dated and anchor override well-disclosed; futures-normalisation size and the 31 Jul event-collision caveat are both missing from where the framework requires them. |

## 3. Total, band, override

- **Total = 20.00 + 17.00 + 16.25 + 17.00 + 12.75 = 83 → total=83**
- **band=High** (75–89)
- **override=none** — no fabricated/hallucinated source found in the 3 spot-checked citations (§3.2); no prompt restriction openly breached (the daily-open-anchor deviation was logged as a non-conformance per protocol, which is the compliant path, not a breach).

```
c1=5
c2=4
c3=3
c4=4
c5=4
total=83
band=High
override=none
card_integrity=93.33
n_cards=3
n_duds=0
n_warns=2
```

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-31.csv`, copied verbatim)

| card_id | strategy | flags | dud | integrity (100−40·dud−10·warn) |
|---|---|---|---|---|
| 2026-07-31_Trade_1 | Trade 1 — Daily Directional (long bias, override-produced) | CLEAN | False | 100 |
| 2026-07-31_Trade_2 | Trade 2 — Pivot, regime-aware (TRANSITION → breakout side) | CLEAN | False | 100 |
| 2026-07-31_Trade_3C | Trade 3 — Momentum-Breakout (3C, TRANSITION regime) | WARN_R_HUGE(3.30xATR)\|WARN_TARGET_FAR(4.78xATR) | False | 80 |

Report-level Card Integrity = mean(100, 100, 80) = **93.33** (n_cards=3, n_duds=0, n_warns=2). Separate from the 100-point Trust Score total.

Feedback: see `qa/gold_regen_qa1/2026-07-31_feedback.md`.
