# Module changelog — revisions from QA run `regen_20260906_qa1`

Stage 1.5 of the protocol. Source: `qa/regen_20260906_qa1/STAGE1_SUMMARY.md`, `trust_scores.csv` and the
54 `<date>_feedback.md` files. No market data, no `results/`, no report bodies were opened, and no edit
was made because a level "would have worked" — every change closes a construction rule that the QA
sessions found stated in a way that allowed drift.

**32 distinct edits across 5 modules.** `M1_SP500_v2_1.md` was not edited (see *Values left alone*).
Strategy economics are unchanged: tranche structure, R-multiple targets, ATR caps, the conviction
threshold, the direction weights and the break-even offset all carry forward at their existing values.

## Principle applied

Almost every failure below is a rule that already existed. The edits make each one **explicit,
checkable and mandatory** — a stated formula with a worked check, a value that must be printed as a
number, a named session a derivation must use, or a gate that fails loudly — rather than new logic.

---

## M5 — Strategies (card construction)

| # | Section | Change | QA failure addressed (dates) | Verification in the next generation |
|---|---|---|---|---|
| 1 | ABSOLUTE RULES | New rule 8: the §10 suppression triggers, the §5.0 order rules and the §9a checklist are non-overridable; no run-time or user instruction may relax them or be cited as authority. | A card the rules require to be SUPPRESSED is issued anyway (54) | No regenerated report contains a phrase of the form "per user instruction / on instruction / not suppressed on…" attached to an emitted card. |
| 2 | New §5.0 | Order-side, anchor and reference-close rules binding on every card: the reference close is the last completed session strictly before the report date; MARKET = that close; buy limit / sell stop at or below it, sell limit / buy stop at or above it; the anchor is the populated instance value. | Entry on the wrong side of the D-1 close (43); as-of session is D-2 (9) | Every card prints entry, reference close, its date and the signed gap; the sign agrees with the order type on all cards. |
| 3 | §5.1 Entry | Removed the "(00:00 UK or 07:00 UK)" menu from the entry row; the populated instance value governs and the fill level is the §5.0 reference close. | Entry on the wrong side of the D-1 close (43) | One anchor value appears on card, handoff record and body, and it matches the instance. |
| 4 | §5.1 Sanity check | Made the check universal (every card, not Trade 1), required R to be printed in points *and* as R ÷ ATR(14) to two decimals, and stated that the wide-stop flag is set by the arithmetic, not by judgement; proxies barred. | No wide-stop flag where R exceeds 1×ATR (49) | Recompute R ÷ ATR(14) from each card's own printed figures; every card above 1.00 carries the flag. |
| 5 | §5.1 Thesis invalidation | Must be a different price from the SL, stated as a close-through condition on a named level. | Invalidation set equal to the stop (11) | No card shows invalidation equal to, or within 0.15×ATR of, its stop. |
| 6 | §6a Invalidation | Same rule at the general level: an invalidation equal to the stop, or within 0.15×ATR of it, is not an invalidation. Stop is intraday, invalidation is close-through. | Invalidation set equal to the stop (11) | As above, across all three cards. |
| 7 | §5.2 preamble | The branch is selected by the regime label and nothing else; one label governs the whole run; the branch must be named on the card and built only from that branch's row. Borrowing geometry across branches is a defect. | Card built on the wrong regime branch (11) | The label in the technical sections, the Trade 2 branch and the Trade 3 fork are the same on every date. |
| 8 | §5.2a Suppression | Defined "accessible" as every pivot timeframe toggled YES the card could draw from; made the test symmetric (state the flag ⇒ suppress; produce the card ⇒ show the corroborated tier and second source); distinguished *absent* from *indicative*. | SUPPRESSED card issued anyway (54) | No report both states that every pivot tier is indicative and issues a pivot card. |
| 9 | §5.3 preamble | Fixed the fork mapping explicitly (TREND→3A, RANGE→3B, TRANSITION→3C), required the fork and selecting label to be named, and barred substituting a different variant when the selected one's eligibility test fails. | Wrong regime branch (11); SUPPRESSED card issued anyway (54) | Card heading, geometry and regime label agree on every Trade 3. |
| 10 | §8 Handoff | Surface field, trigger and weight names are internal addresses, not report language — value plus plain English only, including in the Agent Log feed. | Module codes / variable tokens leaked into the body (31) | No surface field name appears in any regenerated report. |
| 11 | New §9a | A 12-row pre-emit checklist run per card before emission: reference close, suppression gates, order side, anchor, ATR stated, R and wide-stop flag, ladder order, branch and fork, derivation session, invalidation, units, naming. A FAIL is not a caveat — rebuild or suppress. | All ten listed failures; principally the four largest (54 / 49 / 45 / 43) | The trace records the row, the value tested and PASS/FAIL for each card; a report with a recorded FAIL and an emitted card is a protocol breach on its face. |
| 12 | §10 lead-in | Three points added: the triggers are not discretionary and no instruction reverses them; a suppressed card is a row with no entry/stop/R/TP ladder; the decision is logged even when the trigger does not fire. | SUPPRESSED card issued anyway (54) | No SUPPRESSED row carries a full ladder; every card, produced or not, has a logged trigger test. |

## M3 — Technical (indicator and pivot arithmetic)

| # | Section | Change | QA failure addressed (dates) | Verification in the next generation |
|---|---|---|---|---|
| 13 | Step 1a | Fix the as-of session first: the last completed regular session that closed strictly before the report date. Every window in the module ends there. A report assembled before that close is re-run, not shipped a session behind; an unsourceable D-1 is an error, not a licence to shift the window. | As-of session is D-2 (9) | The stated as-of date is the trading day immediately preceding the report date on every report. |
| 14 | Step 1b | A reconstructed field — read off a narrative percentage, interpolated, scaled from an ETF/CFD proxy, or from differently-houred hours — is not an observation: it may be shown only if labelled at every point of use, and never counted toward corroboration or used as an execution reference. Declare the table's basis once and state deltas for off-basis quotes. | §6 OHLC outside basis tolerance (40) | The OHLC table declares its basis; no row is both reconstructed and marked CORROBORATED. |
| 15 | Step 2 (RSI2) | Stated that the column must reproduce from the close column printed in the same table — no smoothing, seeding, carry-over or row shift; gave the two boundary cases (two up closes → 100.0, two down closes → 0.0) and a **worked check** with illustrative numbers; required the two changes and RS to be printed; extended the same discipline to the derived Trend column. Indicator itself unchanged (period still 2, same formula). | RSI2 does not reproduce from the report's own closes (45) | Recompute RSI2 from each report's own printed closes; every row matches, and the printed RS line reproduces. |
| 16 | New Step 5d | ATR(14) is a required published scalar: print it as a number with its window and bar basis, in the volatility section and on every card. Proxies, implied vol, range averages and carried-over figures barred; it may not be left implicit behind a buffer or cap. | ATR(14) never stated, or materially wrong (36) | ATR(14) appears as a number in the volatility section and on each card, and the two agree. |
| 17 | Step 8 | Defined the prior period against the as-of session: prior day = D-1 itself; prior week = the last **fully completed** calendar week, H/L across *every* session in it; prior month likewise. Required the H/L/C used and their dates to be printed above the levels. | Pivots built on a stale session or the wrong week (31) | Recompute pivots from the printed inputs; inputs are dated and fall in the correct period. |
| 18 | Step 8a | Added a self-check before publishing any pivot table: R2 − P = P − S2 = H−L, and the R1/S1 identity. Failure means the arithmetic is wrong; identities holding but levels disagreeing with a prior report means the inputs are wrong. Fix before any narrative or card cites a level. | Pivots on a stale session / wrong week (31) | The identity holds on every printed table, and levels for the same period agree across consecutive reports. |
| 19 | Step 11 surface | `atr_14` re-sourced to Step 5d, required to be computed on the 14 sessions ending at D-1, required to appear as a printed number, proxies barred from the field. | ATR(14) never stated (36) | The surface value and the printed value are the same number. |
| 20 | New Step 11d | Surface names are internal addresses, not report vocabulary — no field name, step or module code, or bracketed token in the deliverable. (Old 11d/11e renumbered to 11e/11f.) | Module codes / variable tokens leaked (31) | No surface identifier appears in any regenerated report. |

## M4 — Output structure

| # | Section | Change | QA failure addressed (dates) | Verification in the next generation |
|---|---|---|---|---|
| 21 | Presentation Rules | New rule 9, a **pre-emit naming scan** over the finished text — title, sections, tables, chart captions, footnotes, Agent Log, footer — against an explicit banned list: M1–M5 in any form, step/patch codes, framework or version strings, any square-bracketed token, any internal field/signal/weight/trigger identifier bracketed or not, and barred ticker codes. Each hit is replaced with plain language. Last action before issue. | Module codes, bracketed variables, framework identifiers in the body (31) | Grep each regenerated report for the banned patterns; zero hits, and the restriction-breach override count falls from 31. |
| 22 | §6 spec | RSI2 must reproduce from the table's own Close column, with a one-line working shown for the most recent session (two changes, mean gain, mean loss, RS, value) and any off-block seeding closes printed. Reconstructed O/H/L must be labelled in-row and cannot be shown CORROBORATED or used for pivots. | RSI2 does not reproduce (45); OHLC basis (40) | The working line is present and reproduces; no reconstructed field is marked CORROBORATED. |
| 23 | §9 spec | ATR(14) must be stated as a number with window and bar basis, matching the figure on each card; KER stated with period and smoothing. | ATR(14) never stated (36) | Present and equal to the card figure on every date. |
| 24 | §11 spec | Added an input row per pivot table: the prior-period H/L/C actually used with the date or date range, and confirmation that R2 − P = P − S2 holds. A table built on an earlier session, a part-week, or one session's extremes standing in for a week is wrong at the input. | Pivots on a stale session / wrong week (31) | Inputs printed and dated; identity confirmed; recomputation matches. |
| 25 | §21b Entry field | Exactly one order type (no "stop/limit" compounds); anchor stated as the populated value; print the reference close, its session date and the signed gap; stated the side rule; wrong-side entries are rebuilt or suppressed, not shipped with a note. Removed the "Market at 00:00 UK" example that was seeding the anchor drift. | Entry on the wrong side of the D-1 close (43) | Every card carries the gap figure with the correct sign for its order type. |
| 26 | §21b Risk (R) field | R must be followed by the same distance as a multiple of the stated ATR(14) to two decimals; above 1.00 the wide-stop flag is carried; the ATR figure used must be on the card. | No wide-stop flag where R > 1×ATR (49) | The multiple is printed and the flag presence matches it on every card. |
| 27 | §21b Thesis invalidation field | Must be a named structural level at a different price from the stop, as a close-through condition. Removed "May coincide with SL — recorded explicitly even when it does". | Invalidation set equal to the stop (11) | No card states an invalidation coincident with its stop. |
| 28 | §21b suppression paragraph | A required suppression is not negotiable — no run-time instruction converts it to a produced card, and such an instruction must not appear in the report; a report that states the condition in one section and issues the card in another contradicts itself in writing. The replacement is a row with no entry/stop/R/ladder; contingent arming levels go outside the card block as commentary. | SUPPRESSED card issued anyway (54) | No SUPPRESSED row carries a ladder; no report contains an instruction-based suppression waiver. |

## M2 — Research standard

| # | Section | Change | QA failure addressed (dates) | Verification in the next generation |
|---|---|---|---|---|
| 29 | §3 Data Quality Rules | Establish the as-of session before collecting anything and state its date; all evidence and windows end there; a settled close is required. Distinguish observed from reconstructed at every point of use — reconstructed values cannot corroborate, be called corroborated, or serve as execution references; state basis and delta for off-basis quotes. | §6 OHLC outside basis tolerance (40); as-of is D-2 (9) | The as-of date is stated and is D-1; the price-evidence table separates observed from reconstructed. |
| 30 | §8 article field table | Two rows added: **Date consistency** (publication date must be real and consistent with the trading calendar and the events described) and **Consistent use** (a source rejected for prices cannot corroborate prices elsewhere; mutually exclusive claims are resolved or dropped, not both carried forward). | Supporting fix for the fabricated-source override (12 dates zeroed C3); cited in the 3 Jun and 9 Jun reviews | No weekend-dated close citations; no source both rejected in the price stack and used as a corroborator. |

## M1 Variables — wording only, no values changed

| # | Section | Change | QA failure addressed (dates) | Verification in the next generation |
|---|---|---|---|---|
| 31 | `[AS_OF_DATE]` note | Clarified that this is the date of the **as-of session** — the last completed session closing strictly before the report date — not the run-execution date, and that it does not move back when D-1 is awkward to source. Value column untouched. | As-of session is D-2 (9) | The stated as-of is D-1 on every report. |
| 32 | `[DAILY_OPEN_ANCHOR]` note | Clarified that the two options are a set-up menu from which a populated instance selects **once**, that the instance value then governs every run, and that a deviation is a logged non-conformance carried identically on card, handoff record and body — never presented as the instance's anchor. Default value `00:00 UK` left as-is. | Entry / anchor drift feeding the wrong-side-of-close failure (43) | One anchor per report, matching the instance, identical in all three places. |

---

## Values left alone, and why

- **`M1_SP500_v2_1.md` was not edited at all.** Its parameters are the experiment's fixed settings.
- `[DAILY_OPEN_ANCHOR]` = **07:00 UK** in the instance. Repeatedly cited by QA as the value the cards
  failed to honour (00:00 UK, 14:30 UK and 23:00 UK all appeared). The value is right and the reports
  were wrong; left unchanged, and the ambiguity that allowed the misreading was closed in the M1
  Variables note and M5 §5.0 / §5.1 instead.
- `[AS_OF_DATE]` = **29 April 2026** in the instance, while the run covers 11 May – 31 July. This
  *looks* wrong: it is a static snapshot date on a field that must be repopulated per report date, and
  it is a plausible contributor to the nine D-2 dates. **Left unchanged** — it is an instance parameter,
  and the fix belongs in the definition of the field, which is where it was made (edits 13, 29, 31).
- The `M1_Variables` default `[DAILY_OPEN_ANCHOR]` = `00:00 UK` conflicts with the instance's 07:00 UK.
  Value left as-is (it is the contract default for 24-hour assets); only the note was clarified.

## Considered and deliberately not changed

- **Pivot table depth.** Several reviews ask for `R3 → P → S3`, three levels a side, while M3 §8b and
  M4 §11 mandate `R5 → P → S5`. That is a disagreement between the QA brief and the module spec, not a
  construction error, and narrowing the table would change the output specification rather than close a
  failure. Left as written; flagged here so a later reviewer does not read it as an oversight.
- **Indicator definitions.** RSI2's period, the ATR method, the KER parameters, the fib levels and the
  25-day range definition are untouched. The arithmetic-adherence failures were closed by stating the
  formula, requiring the working to be printed and naming the session — not by changing any indicator.
- **Strategy economics.** Three tranches, ±1R/±2R ladders, the 3×ATR runner cap, the 3.5×ATR stop cap,
  the 0.3–3.0×ATR R band, the 0.25 conviction threshold, the 0.2R break-even offset and the direction
  weights are all carried forward unchanged, as required.
- **Linter scope.** The summary notes the static linter cannot test whether the right recipe was
  applied. That is addressed inside the modules by the M5 §9a pre-emit checklist rather than by any
  change to `engine/`, which is outside the scope of a module revision.

---

## Correction, after Stage 2 draw 1

**M5 §5.2a and §10 — what the corroboration flag means when the execution series is in hand.**

Edit 8 above tightened the pivot-corroboration gate to stop reports stating that every tier was
single-source-indicative and then shipping the card anyway. That was the right fix for the failure it
addressed, but it left the flag's meaning unstated for the case where the pivots are computed from the
broker price series itself rather than quoted from a news aggregator.

Regeneration sessions read the flag as a property of the report and inherited it, suppressing cards whose
pivots they had just recomputed from the execution feed. That is wrong: the feed a card is filled and
settled against is the settlement source, not a secondary quote about the market, so a tier struck from it
is corroborated by construction and there is nothing for a second source to corroborate it against. The
gate is for tiers whose true prior-period H/L cannot be established at all.

**Effect on draw 1**: 28 of 162 cards (17% of the book, and 20 of the 54 Trade 2 cards) were suppressed on
this ground. Those cards are being rebuilt; the other 47 suppressions — 28 on conviction and 19 on an
unconfirmed break — are unaffected and stand.

**Verification in the next generation**: no card is suppressed as indicative where its pivot tier was
computed from the execution series; every produced pivot card names the series and session its tier came
from and records the flag as CORROBORATED.
