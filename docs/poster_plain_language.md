# Poster: plain-language redraft

## The problem with drafts 1–5

The poster is written in the project's internal vocabulary: M1–M5, C2, 3.3, Trust Score v3.7, ρ, bootstrap,
draws, R. A visitor has about 30 seconds and does not know any of it. Three things are missing:

1. **No storyline.** The panels are a list of components, not "we did X, to find out Y, and found Z".
2. **Codes instead of meanings.** "Calculations (3.3)" means nothing until you read a footnote.
   "Numbers can be re-checked" needs no footnote.
3. **No answer to "so what?"** Nothing says what this means for TT International or for a fund that
   wants to use LLM reports.

**The fix:** one storyline, plain words, and one picture per idea. The draft text below fits the
existing six-panel grid. It is about 600 words, a comfortable amount for A0.

---

## Storyline (top to bottom)

> **We built** a fixed set of instructions so an AI writes the same daily market report every day →
> **we checked** whether its reports are well-made, checkable and honestly sourced →
> **we tested** whether its trade ideas worked against real prices, before and after fixing the data →
> **so what:** what a fund can and cannot rely on.

---

## Title block

Keep the registered title, as the QR link uses it. Replace the subtitle.

> **Guiding real-time LLM market analytics for the UK financial industry**
> *Can an AI write a daily market briefing that a fund manager can trust? We tested 324 reports across
> six markets.*

## Research question (dark bar)

> Can a structured set of AI instructions produce daily market research that is consistent, checkable
> and honest about its sources, while leaving judgement to the professional?

---

## 01 What we built

> We wrote a **fixed recipe** of instructions for an AI model. One part changes each day (which market,
> which date). The rest never changes during a study: where to find evidence, how to calculate signals,
> how to lay out the report, and how to turn it into trade ideas.
>
> Because the recipe is fixed, every report can be compared like-for-like, and any mistake can be traced
> to a specific instruction.
>
> **324 daily reports, 10 May – 2 August 2026**
> S&P 500 · FTSE 100 · Shanghai Composite · Gold · WTI crude oil · Bitcoin

**Visual:** keep the five-box strip, but give the boxes plain names. No M-codes on the poster; put them
in the working paper.

| Changes each day | Fixed | Fixed | Fixed | Fixed |
|---|---|---|---|---|
| **The brief** (market, date) | **Evidence rules** (approved sources, no invented figures) | **Calculations** (price levels, momentum, volatility) | **Report layout** (same sections every day) | **Trade ideas** (if-then rules, tested separately) |

## 02 What each report contains

Merge the current panels 03 (sentiment) and 04 (macro context); together they describe what the report
delivers.

> - **News sentiment.** Each article is labelled bullish, bearish, neutral or mixed, with a short quote
>   as proof. These combine into one score from −1 (bearish) to +1 (bullish).
> - **Economic calendar.** Recent and upcoming releases (inflation, jobs, interest rates) with forecasts,
>   outcomes and the likely effect on this market.
> - **Price levels and signals.** Support and resistance, momentum and volatility.
> - **Trade ideas.** Up to three if-then trades, each with an entry, a stop-loss and targets.

## 03 How we tested it

**Visual:** a simple four-step flow diagram with icons.

```
 1. CHECK THE REPORT        2. TEST THE TRADES          3. FIX THE DATA            4. TEST AGAIN
 Reviewers graded 171       Each trade idea was run     Replaced the AI's own      Re-ran the corrected
 reports (S&P, FTSE, gold)  against actual prices at    price figures with actual  trades, three times
 on a 0–5 scale             several entry times         data from the night before over, and compared
```

> Strictly no hindsight: corrected trades used only data available by midnight before each trading day.

## 04 What we found: the reports

**Chart:** keep the grouped bars, but with plain labels. Or use a traffic-light table, which is faster to
read. Use the bars if you need numbers, the table if you need the message.

| | Follows the layout | Numbers can be re-checked | Sources are genuine |
|---|:---:|:---:|:---:|
| S&P 500 | ● good (3.9/5) | ◐ partly (1.9/5) | ◐ partly (2.2/5) |
| FTSE 100 | ● good (3.7/5) | ◐ partly (2.1/5) | ○ weak (1.4/5) |
| Gold | ● good (4.1/5) | ◐ partly (2.5/5) | ● good (4.0/5) |

> **The AI is a reliable writer but an unreliable analyst.** It almost always followed the layout. But
> reviewers could only partly reproduce its calculations, and it sometimes **cited sources that did not
> exist**: 1 in 4 S&P reports, more than 1 in 3 FTSE reports, rarely for gold.

## 05 What we found: the trade ideas

**Visual:** one small chart showing cumulative profit and loss over the 57 days for the original and the
corrected trades, S&P and FTSE side by side. The existing equity curves in `results/*/equity/` can be
restyled. The picture shows two wobbling, overlapping lines, which is the finding.

> **Correcting the data did not make the trade ideas better.** Fixing every price figure with actual
> data, which is what a fund supplying its own data would get, changed which trades were suggested
> but not how well they performed. Results were small, inconsistent and within the range of luck over
> 57 trading days.
>
> **Report quality did not predict trading results.** Better-graded reports did not produce better trades.

## 06 What this means and what comes next

> **For a fund using AI market reports:**
> - **Use it for:** gathering and summarising news, sentiment and the economic calendar in a consistent
>   format. This is likely to save time, though we have not yet measured how much.
> - **Supply your own price data.** Do not let the model fetch prices.
> - **Check:** the calculations and every cited source.
> - **Do not use the trade ideas** without independent testing.
>
> **Next:** a version that reads the fund's own data; packaging the checked instructions as reusable
> "skills"; extending the testing to oil, Bitcoin and Shanghai.
>
> **Outputs:** instruction library · testing toolkit and report archive · working paper.

Contribution line: keep it, but make it concrete:

> *First-stage principles for using AI market research in practice, to be tested with more institutions.*

---

## Jargon to remove (poster → plain)

| On the poster now | Say instead | Where the technical term goes |
|---|---|---|
| M1 … M5 | brief · evidence rules · calculations · layout · trade ideas | working paper |
| C2 / Structure | follows the layout | chart footnote, if anywhere |
| 3.3 / Calculations | numbers can be re-checked | – |
| 3.2 / Citations | sources are genuine | – |
| Trust Score v3.7 | reviewer grade (0–5) | small footnote: "Trust Score v3.7 rubric" |
| hallucinated source / override | cited a source that does not exist | – |
| Spearman ρ = 0.01 / 0.04 | better-graded reports did not produce better trades | working paper |
| 95% bootstrap intervals include zero | within the range of luck over 57 days | working paper |
| three draws | ran three times over | – |
| prior-data rebuild | fixed the data and re-tested | – |
| R, entry policies, band0845 | (leave out) | working paper |
| v2.1 | (leave out, or footnote) | – |

## Layout notes

- **Read order:** the storyline runs top to bottom, left then right: built → contains → tested →
  found (reports) → found (trades) → means. Number the panels in that order.
- **Bold the takeaway.** Each panel opens with one bold sentence. Someone who reads only the bold lines
  should get the whole story.
- **Pictures:** five-box recipe strip, four-step test flow, report scorecard, profit-and-loss lines.
  Four pictures for six panels is about right.
- **Footnotes:** one small line at the bottom of the poster can hold the technical references (rubric
  name, statistics used, sample sizes), so the panels stay clean.
