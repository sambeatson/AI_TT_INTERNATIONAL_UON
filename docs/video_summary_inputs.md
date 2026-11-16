# Inputs to the TT International x CANON video summary (for UKFin+)

These comments are on `TT_International_CANON_video_summary.md`. The funder wants to see three things:
the research conducted, its potential, and its outputs. This note is organised in that order. Section 1
is the most important part, because the summary's headline numbers come from a superseded scoring pass.

All figures here come from two places:
- this repository (`results/sp500_v2`, `results/ftse_v1`, `qa/*`);
- the per-asset notes on the `claude/gold-trading-equity-curve-l985jp` branch of `AI_Report_Analysis`.

> **Update 16 Nov 2026: the Edinburgh A0 poster is now canonical** (`docs/poster/`). The video should use
> its wording and level of detail.
> - **Keep R figures off screen.** The poster gives none and says "strategy results were mixed … no
>   clear improvement". Say the same in the video. The table in §1 is background, there to stop the old
>   first-pass numbers being used. It is not for display.
> - **Use the poster's six-section order as the video's backbone:** why we built this → what each
>   report contains → CANON → how we tested → what we found → what it means for practice.
> - **Reuse the poster's chart** (Layout / Calculations / Citations) as the one on-screen chart.
>   Everything you show then matches what the funder has seen on the poster.
> - **Spell out CANON once on screen,** as the poster does.

---

## 1. Fix before recording: the S&P numbers in section 6 are from the first pass

The summary's table comes from the **first scoring pass** (`docs/HANDOVER_METHOD.md`):

| Figure | Value |
|---|---|
| Sessions | 54 |
| Cards | 159 |
| Stated-level total | +2.31R |
| Tradable total | −11.92R |
| Best entry policy | −9.40R |

That pass had two timing problems, both found later:

1. **One day late.** It entered every card on the session *after* the report date. The reports state
   their own session ("Report dated for Monday 11 May 2026 session"), so the correct entry is the same
   day. On the S&P this alone moves the original cards' total from **−15.9R (one day late) to −7.0R
   (correct day)**.
2. **One hour late** on card-anchored entries in the very first pass, because of the mislabelled time
   column (`HANDOVER_METHOD.md` §0).

The sample also grew from 54 to **57 sessions (168 cards)** when three missing reports were added.

**Recommendation.** Keep the first-pass *finding*: the analysis had some value, and card construction
destroyed it. Say so as "our first pass found…". Do **not** put the first-pass table on screen as the
result. Use the corrected, leak-free results below.

### Before (section 6 heading and table)

> **S&P 500 back-test: 159 trade cards, 54 sessions** | Total at stated card levels +2.31R | Total as
> actually tradable −11.92R | … | Best of four entry policies tested −9.40R | …

### After

> **S&P 500 and FTSE 100: 57 sessions each, original cards vs three corrected rebuilds**
>
> | | Original cards | Rebuilt on actual prior-day data (3 runs) |
> |---|---:|---:|
> | S&P 500, enter 07:00 UK | −6.2R | −7.5 / −4.5 / −8.5R |
> | S&P 500, enter at US open | −2.5R | +0.5 / +5.2 / +0.4R |
> | FTSE 100, enter 07:00 UK | +9.4R | −3.0 / +2.2 / −0.8R |
> | FTSE 100, enter at US open | −0.7R | +2.7 / +8.3 / +1.8R |
>
> *R = one unit of risk per trade. No difference is statistically distinguishable from luck over
> 57 days.*

**On-screen version (simpler):** two small equity-curve panels, original against rebuilt, for the S&P and
FTSE. They already exist in `results/sp500_v2/equity/` and `results/ftse_v1/equity/`.

---

## 2. Answers to the open items in section 7

| Section 7 item | Answer |
|---|---|
| **Regeneration results** | Done for the **S&P 500 and FTSE 100**. QA-score each report → rebuild the cards from the QA feedback plus actual data up to 23:59 the night before → three independent rebuilds → test at midnight UK, 07:00 UK and US open. **Result: no detectable improvement.** The one consistent pattern is that at the US cash open all three rebuilds beat the original on both indices, but every interval includes zero. Gold has been QA-scored; its rebuild is not yet done. |
| **Other assets** | A **first-pass** back-test exists for gold, FTSE, WTI and Bitcoin, with a different, earlier entry rule (see 3c). It is *not* the leak-free six-step design, so treat it as exploratory. EUR/USD and USDX were used only as cross-asset inputs, not back-tested. |
| **TT quote** | Still needed. Suggested prompt for Thomas: "What does a governed, auditable AI workflow let a firm like TT do that ad-hoc use of AI tools doesn't?" **[CHECK the spelling "Sittekt"]** |
| **IP** | Agreed. The poster and this video should use plain names (the brief, evidence rules, calculations, layout, trade ideas), not module codes or indicator names. |

---

## 3. The research conducted: what to add

The summary describes the framework well but under-sells the evaluation. These are the strongest
research points for a funder.

### 3a. Scale of the corpus

The summary says only "54 consecutive S&P 500 sessions". Add:

> **324 daily reports across six markets, 10 May – 2 August 2026:** S&P 500 (57), FTSE 100 / Euro Stoxx
> (58), Shanghai Composite (55), gold (57), WTI crude (58), Bitcoin (39).

### 3b. The no-hindsight test design

This is the methodological contribution. Say it in one breath:

> We graded every report, rebuilt its trade ideas using only data the AI could have known by midnight
> the night before, and tested both versions against real prices, three times over, at three different
> entry times. The future data was physically absent from what the AI could open.

### 3c. What the quality grading found (171 reports: S&P, FTSE, gold)

| | Follows the layout | Calculations can be re-checked | Sources are genuine | Cited a source that does not exist |
|---|---:|---:|---:|---:|
| S&P 500 | 3.9 / 5 | 1.9 / 5 | 2.2 / 5 | 13 of 57 |
| FTSE 100 | 3.7 / 5 | 2.1 / 5 | 1.4 / 5 | 21 of 57 |
| Gold | 4.1 / 5 | 2.5 / 5 | 4.0 / 5 | 2 of 57 |

**Spoken version:**

> The AI reliably wrote a well-structured report. It was weaker at showing calculations we could
> reproduce. And on some markets it cited sources that did not exist. Gold showed the source rules can
> work.

### 3d. The partner-relevant result

TT would supply its own market data, so the AI's own price fetching does not matter to them. The rebuild
experiment answers exactly their question:

> When we replaced every price figure with actual data, which is what a firm supplying its own data
> gets, the trade ideas still did not improve. Better data did not make the trades better. That tells us
> where the next effort belongs: the trade-construction rules, not the data.

### 3e. First-pass results for the other assets (exploratory)

These come from the earlier engine on the `AI_Report_Analysis` branch: entry from 07:00 UK (08:00 for
FTSE), plus a "better-entry" rule.

| Asset | Cards | Realised | Main caveat |
|---|---:|---:|---|
| Gold | 150 | −5.4R | |
| WTI | 149 | −6.0R | Shorts lost; July −8.6R |
| FTSE 100 | 156 | +32.4R | All from longs in a rising market |
| Bitcoin | 94 | +10.4R | One card gave +7.8R; 59 % from positions still open when the data ended |

**Use on video only as:**

> Results varied by market and by entry rule. Where the market trended, trades that went with it did
> well. No asset showed a robust edge once we corrected the timing.

**Do not quote the +32R FTSE figure.** It conflicts with the corrected same-day FTSE result (§1) and
would invite questions you don't want in a two-minute video.

---

## 4. Potential: what the funder will want to hear

Frame potential as **what this enables for UK financial firms**, not as trading performance.

1. **A governance template for AI-assisted research.** Fixed instructions, a changeable brief, logged
   patches and versioned releases. A firm can show a compliance team exactly what the AI was told and
   what changed between versions. This is the transferable asset.
2. **An audit toolkit for AI outputs.** The quality grading, the trade-card checker and the
   no-hindsight test can be applied to any LLM research product, not just this one.
3. **Clear evidence on where AI helps and where it doesn't:**
   - *Helps:* gathering and structuring news, sentiment and the economic calendar consistently across
     six markets.
   - *Needs checks:* calculations and source citations.
   - *Not ready:* unsupervised trade ideas.

   That evidence is itself useful to firms deciding where to deploy AI.
4. **A data-supplied version (next step).** The firm supplies the prices and the AI does the synthesis.
   This removes the weakest link the study found.
5. **Measurable time savings (next step).** Run the reports alongside TT analysts and time both. The
   study has not yet quantified this, and it is the number a funder or firm will ask for.

---

## 5. Outputs: a fuller list for the closing beat

Replace section 6's "Outputs" bullet list with this list, grouped for the funder.

**Delivered**
- **CANON Framework v2.1:** five fixed modules, a Python calculation engine, source rules and a patch
  registry. It was packaged with a manifest and integrity checker (6 Sep 2026).
- **Report archive:** 324 daily reports across six markets.
- **Evaluation repository:**
  - no-hindsight protocol;
  - quality-grading protocol;
  - trade-card checker;
  - back-test engine;
  - 171 graded reports with written feedback;
  - 1,026 rebuilt trade cards;
  - full results with equity curves.
- **Dissemination:** UKFin+ poster (A0), web summary, board-level update and funder submission.

**In progress / next**
- Working paper on modular LLM market reporting.
- Data-supplied version (v2.2), in which the firm's own data replaces AI price fetching.
- Rebuild tests for gold, WTI, Bitcoin and Shanghai under the same no-hindsight design.
- Packaging the checked instructions as reusable "skills" for other firms.
- A time-saving study with TT analysts.

---

## 6. Revised script (about 2 min 30 s, about 390 words)

| Time | Say | Show |
|---|---|---|
| 0:00–0:20 | Can a general-purpose AI produce market research that a regulated firm could trust, audit and repeat? That was our question, with TT International, funded by UKFin+. | Title card, logos |
| 0:20–0:45 | TT's AI Lead already had a governed template: change the brief, fix everything else. We grew it into a five-part framework, with a code engine doing the maths so the AI never makes up a number. | Three boxes growing to five |
| 0:45–1:05 | Over twelve weeks it produced 324 daily reports across six markets: US, UK and Chinese equities, gold, oil and Bitcoin. Each covers news sentiment, the economic calendar, price levels and trade ideas. | Report pages scrolling; six market labels |
| 1:05–1:25 | Real use taught us a lot. Data sources were blocked, so we wrote strict rules: two sources for every price, nothing invented, and every failure logged and fixed by version. | Patch log; "flag, don't halt" |
| 1:25–1:55 | Then we tested it properly. We graded 171 reports. We rebuilt every trade idea using only what was known the night before, and tested both against real prices, three times over. The AI wrote well-structured reports, but calculations and sources needed checking, and on some markets it cited sources that didn't exist. | Scorecard chart |
| 1:55–2:15 | The key result: even with correct data, the trade ideas didn't improve, and a good quality grade didn't predict a good trade. So AI is ready to gather and structure research, but trade ideas still need human judgement. | Two equity curves overlapping |
| 2:15–2:30 | What we leave behind is a governance template, an audit toolkit and a public evidence base. Next, we are building a version that runs on a firm's own data. | Outputs list; closing card |

---

## 7. Smaller points on the summary text

- **§1 "gold, oil, equity indices, FX and crypto".** FX was a cross-asset input and occasional extra
  session, not one of the six evaluated markets. Use "gold, oil, equity indices and crypto" or name the
  six markets.
- **§1 headline lesson.** "The analysis was modestly useful" comes from the first pass. The corrected
  run does not show a positive edge for the S&P (−7.0R card anchor, same day). Suggested replacement:
  *"The reports were well structured and the process is auditable; the trade ideas were not reliable,
  and a high quality score did not predict a good trade."*
- **§6 "Three or four simple assertions would catch most defects".** Still true for construction
  defects. The trade-card checker found 0 defective cards in all three S&P rebuilds and in all three
  FTSE rebuilds, against 3 (S&P) and 6 (FTSE) in the originals. The cleaner cards still did not perform
  better, which is worth one line.
- **§6 "Blended win rate about 30%".** This is from the first pass. Drop it, or recompute it from
  `results/*/MASTER.csv`.
- **Units.** Say "R = one unit of risk" once on screen. Better still, show equity curves without R values
  in the video.
