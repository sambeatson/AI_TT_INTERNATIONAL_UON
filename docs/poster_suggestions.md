# Poster review: suggested edits (UKFin+ A0 poster, draft 1)

The poster's claims were checked against the repository on branch `claude/asset-scoring-process-pr4eon`.
Edits are shown as **Before / After**, numbered by poster panel.

- **[CHECK]** marks a fact I cannot verify from the repo. The Bitcoin, WTI and Shanghai reports are not in it.
- **[n]** is a placeholder for a number you need to fill in.

---

## 0. Priority list

| # | Panel | Issue | Severity |
|---|---|---|---|
| 1 | 01 | Asset list incomplete (WTI and Shanghai missing); total of 211 will change | High |
| 2 | 01 | FTSE count of 58 is files, not report dates (57). Date range 10 May–2 Aug does not match the repo (11 May–31 Jul) | High |
| 3 | 05 | Findings are qualitative only. You now have hard QA and strategy numbers for S&P and FTSE (gold QA too) | High |
| 4 | — | The evaluation framework (Trust Score QA, leak-free rebuild, entry-timing tests) is a headline output but has no panel | Medium |
| 5 | Title | "Real-time" overstates it. These are daily pre-session reports | Medium |
| 6 | 02/03 | Sentiment tilt feeds M5 direction scoring, which is not shown. Module version (v2.1) and the source-discipline add-ons are not named | Low |

---

## 1. Panel 01: Corpus and research problem

### What the repo shows

| Asset | Report files (`reports/md`) | Unique report dates | Range | QA (Trust Score v3.7) | Strategy test (6-step) |
|---|---:|---:|---|---|---|
| S&P 500 | 57 | 57 | 11 May–31 Jul | done | **done** (`results/sp500_v2`) |
| FTSE 100 | **58** | **57** | 11 May–31 Jul | done | **done** (`results/ftse_v1`) |
| Gold | 57 | 57 | 11 May–31 Jul | done | baseline only; rebuild pending |
| Bitcoin | not in repo | 39 **[CHECK]** | **[CHECK]** | pending | pending |
| WTI crude | not in repo | **[n]** | **[CHECK]** | pending | pending |
| Shanghai | not in repo | **[n]** | **[CHECK]** | on hold | on hold |

**The FTSE count.** 15 May has two FTSE reports: `FTSE_100_Daily_Report_15_May_2026` and
`FTSE_EuroStoxx_Report_15May2026`. So 58 documents but 57 dates. Every FTSE result in the repo uses 57.

**The date range.** S&P, FTSE and gold all run Monday 11 May to Friday 31 July. "10 May–2 Aug" (Sunday to
Sunday) is only right if the Bitcoin series has weekend reports that reach those days. Otherwise use
11 May–31 Jul.

**The total.** 57 + 57 + 39 + 58 = 211, so the sum is correct. With WTI and Shanghai added it becomes
211 + [n_WTI] + [n_SSE]. Counting FTSE as 57 dates takes 1 off.

### Before

> **211 report documents, 10 May-2 August 2026:**
> S&P500 (57), gold (57), Bitcoin (39), FTSE100 (58).

### After (option A: count dates, which is what the analysis uses)

> **[N] daily reports across six markets, 11 May–31 July 2026:**
> S&P 500 (57), FTSE 100 (57), gold (57), Bitcoin (39), WTI crude ([n]), Shanghai Composite ([n]).

### After (option B: keep a documents count, say why it differs)

> **[N] report documents ([N−1] report dates), 11 May–31 July 2026:**
> S&P 500 (57), FTSE 100 (58; two on 15 May), gold (57), Bitcoin (39), WTI ([n]), Shanghai ([n]).

Option A is the better choice: it matches every results table.

**If Shanghai stays out of scope for now,** write "five markets" and add a footnote: "Shanghai Composite
reports collected; evaluation in progress."

### Optional: a small status strip under the corpus line

This shows the reader how far evaluation has got:

> Evaluated end-to-end: S&P 500, FTSE 100 · QA complete: gold · In progress: Bitcoin, WTI, Shanghai

---

## 2. Panel 05: Findings and limitations (biggest gain)

The current text is accurate but has no numbers. A poster audience scans for one figure per claim. All
figures below come from the repo:

- `results/sp500_v2/REPORT.md` and `results/ftse_v1/REPORT.md`
- `qa/*/trust_scores.csv`
- `qa/gold_regen_qa1/STAGE1_SUMMARY.md`

### QA figures (57 reports each)

| | S&P 500 | FTSE 100 | Gold |
|---|---:|---:|---:|
| Mean Trust Score (0–100) | 60.1 | 52.9 | 71.5 |
| Mean accuracy & evidence (C3, 0–5) | 1.65 | 1.11 | 2.16 |
| Reports with a fabricated / unverifiable source | 13 | 21 | 2 |
| Reports with a restriction breach | 32 | 25 | 14 |

### Strategy figures (S&P and FTSE, baseline vs 3 independent QA-guided rebuilds, total R)

| | S&P baseline | S&P rebuilds | FTSE baseline | FTSE rebuilds |
|---|---:|---:|---:|---:|
| 07:00 UK entry | −6.2 | −7.5 / −4.5 / −8.5 | +9.4 | −3.0 / +2.2 / −0.8 |
| US cash open entry | −2.5 | +0.5 / +5.2 / +0.4 | −0.7 | +2.7 / +8.3 / +1.8 |

All bootstrap intervals on the gain from rebuilding include zero.

### Before

> Qualitative and sentiment synthesis offers potential efficiency gains. Time savings remain unquantified.
>
> Sentiment tilts are interpretive scores, not calibrated probabilities. Protocol adherence and source
> verification require review.
>
> Strategy results are mixed and sensitive to asset, timing and execution. Report quality does not
> establish predictive validity.

### After

> **Structure is strong; numbers are weak.** Reports score well on structure and reasoning but low on
> accuracy (C3 mean 1.1–2.2 of 5). The commonest errors are levels built from the wrong prior session
> and understated volatility (ATR).
>
> **Sources need checking.** A fabricated or unverifiable source was flagged in 21 of 57 FTSE reports and
> 13 of 57 S&P reports.
>
> **Quality ≠ profitability.** The QA score is uncorrelated with how the report's own trade rules performed
> (Spearman ρ ≈ 0.0 for both S&P 500 and FTSE 100).
>
> **Correcting the inputs did not detectably change outcomes.** Trade rules were rebuilt from QA feedback
> and real prior-day data, with no look-ahead. At the US open, all three rebuilds beat the original on both
> indices, but no interval excludes zero over 57 days.
>
> **Timing matters as much as content.** On the S&P, moving entry by a single session changes the baseline
> total from −7.0R to −15.9R.
>
> Time savings from the qualitative synthesis remain unquantified. Sentiment tilts are interpretive
> scores, not calibrated probabilities.

**If space is tight,** keep the first, third and fourth points. They carry the argument.

---

## 3. New mini-panel: the evaluation framework

"Evaluation framework and report archive" is listed as a research output in panel 06 but described
nowhere. The leak-free design is the most defensible methodological contribution, so give it space.

**Where.** Either merge panels 03 (sentiment) and 04 (macro context) into one "Evidence inputs" panel and
use the freed slot, or put a thin horizontal strip under panel 02.

### Suggested text

> **05 How reports are tested**
> 1. Score each report's trade rules against broker price data.
> 2. Re-score at alternative entry times (00:00 UK, 07:00 UK, US open).
> 3. Quality-assure each report (Trust Score v3.7: adherence, structure, accuracy, reasoning, transparency).
> 4. Rebuild the rules from QA feedback using only data available by 23:59 the night before (no look-ahead).
> 5. Re-test the rebuilds, three independent draws per report.
> 6. Compare with a daily-block bootstrap. A change counts only if a majority of draws beat the original.

A six-box flow (1 → 6) would mirror the M1–M5 strip visually.

**Panel numbering.** If you add this, renumber "Findings and limitations" to 06 and "Outputs" to 07, or
drop the 0x numbers.

---

## 4. Title

### Before

> Guiding real-time LLM market analytics for the UK financial industry

### After (pick one)

> Guiding **daily** LLM market analytics for the UK financial industry

> Modular LLM market reporting for the UK financial industry: traceability, accuracy and evaluation

**Why.** Each report is produced once per day for the next session. A reviewer may read "real-time" as
intraday or streaming, which the project does not test.

---

## 5. Panel 02: Modular response (small precision edits)

- **State the version.** The modules are v2.1 (`modules/*_v2_1.md`). Add "(v2.1)" after "Our modular
  response", or to the footer line: "M2–M5 change only through explicit versioned updates (current: v2.1)…"
- **Name the source-discipline add-ons.** These are `Agentic_Safe_Source_Module` (an approved source stack)
  and `Source_Discipline_NoSynthesis_Protocol` (no synthesised numbers). They are your main control
  against fabricated sources, which is a headline QA failure. One line under M2 is enough: *"+ approved
  source stack and no-synthesis rule"*.
- **M5 card text.** "Conditional trade rules, evaluated separately" is good. Optionally add "regime-dependent
  (trend / range / transition)".

### M2 card: before

> News, sentiment and macro research standards.

### M2 card: after

> News, sentiment and macro research standards; approved-source stack; no synthesised figures.

---

## 6. Panel 03: Sentiment assessment

The text matches M2 Step 9 (the quote of ≤15 words, the four labels, and the weighted tilt clipped to
[−1, +1]). Two additions make the panel connect to the rest of the poster.

### Before (last sentence)

> Source disagreement and sentiment-price divergence require explicit flags.

### After

> Source disagreement and sentiment-price divergence require explicit flags. The tilt is one of six
> inputs to the strategy module's direction score.

### Optional evidence line

From `results/sp500_v2/REPORT.md`:

> Rebuilding helped least where the report cited a fabricated source (S&P: −0.40R per date vs +0.34R where
> no override applied), consistent with unverified sentiment being carried into the rules.

This is suggestive, not significant. Use it only if you label it that way.

---

## 7. Panel 04: Macroeconomic context and use

This panel is fine, and it is the easiest to shorten if you need room for the evaluation panel. The second
paragraph ("Managers use the synthesis…") is a usage claim. If it comes from TT International feedback,
say so ("TT International analysts use…"). If not, soften it to "Intended for briefings…".

---

## 8. Panel 06: Outputs and contribution

### Research outputs: before

> Modular prompt library · Evaluation framework and report archive · Working paper on modular LLM market
> reporting

### Research outputs: after

> Modular prompt library (v2.1) · Leak-free evaluation pipeline: QA scoring, rule rebuilding and
> back-testing across entry times · Report archive ([N] reports, [k] markets) · **Working paper** on
> modular LLM market reporting

### Contribution line

This is fine as is. To tie it to the evidence, you could add: "…provisional principles, notably that
report quality checks and trading-rule validation must be assessed separately."

---

## 9. Numbers to confirm before printing

- [ ] Bitcoin report count (39) and date span. The range end-points 10 May / 2 Aug depend on this.
- [ ] WTI report count and date span.
- [ ] Shanghai: in or out of the poster, and its count if in.
- [ ] Whether any non-FTSE asset also has duplicate-date files. If so, count dates, not files.
- [ ] Whether gold strategy figures will be ready in time. If not, phrase findings as "S&P 500 and FTSE 100".
