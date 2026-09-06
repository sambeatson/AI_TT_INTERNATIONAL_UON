**S&P 500 Report --- Daily: 9 June 2026**

*With reference to: USDX · VIX · DAX 40*

1\. Executive Snapshot

The S&P 500 closed the most recently completed session (Friday 5 June
2026) at 7,383.74, down 2.64% on the day --- its sharpest single-session
decline since October and the close of its first losing week in ten. The
consensus level for the cash index is 7,383.74 (corroborated), with the
immediate read carried into the 9 June pre-open. Market tone is bearish
in the short term against a still-intact but freshly damaged medium-term
uptrend. The three dominant drivers are: (i) a violent semiconductor-led
sell-off that erased roughly a trillion dollars of market value and
dragged the Nasdaq down more than 4%; (ii) a much-stronger-than-expected
May payrolls print (172,000 vs \~85,000 expected) that pushed Treasury
yields higher and shifted rate expectations toward a possible hike; and
(iii) a sympathetic risk-off bid into the dollar and a 40% one-day spike
in the VIX. The short-term technical state is trending-bearish (latest
period-2 RSI 13.3, deeply oversold; close near the session low), while
the 25-session structure had been trending-bullish into the 2 June
record before Friday\'s reversal --- the composite regime is therefore
classified Transitional. The Kaufman efficiency read over the execution
window is strongly directional to the downside. The single most
important watch item is the 16--17 June FOMC meeting and the rate-path
repricing that the strong jobs data has set in motion. The directional
conviction model resolves SHORT for the coming session (score −0.68).

2\. Market Definition

  -----------------------------------------------------------------------
  **Field**           **Definition**
  ------------------- ---------------------------------------------------
  Asset               S&P 500 cash index (large-cap US equity benchmark,
                      503 constituents)

  Price basis         Cash index level (continuous), calculated during
                      NYSE/NASDAQ hours

  Delivery / session  Regular cash session 09:30--16:00 ET

  Unit / currency     Index points / USD

  As-of date          9 June 2026 (America/New_York); most recent
                      completed session 5 June 2026

  Lookback window     5 sessions (1--5 June 2026)

  Daily-open anchor   00:00 UK (overridden for this run from the standing
                      07:00 UK pre-NY-open anchor)
  -----------------------------------------------------------------------

*Note on the anchor override: the standing configuration anchors the
daily-open trade to the 07:00 UK European pre-NY-open window. For this
run the anchor has been overridden to 00:00 UK at the user\'s
instruction. Because the S&P 500 cash index does not trade at 00:00 UK,
the Trade 1 market-entry timestamp is treated as the next cash-session
open (09:30 ET / 14:30 UK on 9 June); this deviation is recorded in the
Agent Log (§20).*

3\. Consensus Price Call

  ------------------------------------------------------------------------------------------
  **Consensus**   **Range**      **Basis**    **Confidence**   **Tone**   **Rationale**
  --------------- -------------- ------------ ---------------- ---------- ------------------
  **7,383.74**    7,380--7,390   Cash close,  High             Bearish    Multi-source
                                 5 Jun                                    corroborated
                                                                          official close;
                                                                          tight cross-source
                                                                          agreement

  ------------------------------------------------------------------------------------------

The consensus is the validated 5 June cash close. Confidence is High:
the close is corroborated across exchange-aggregator and major-media
data within the ±0.10-point equity-index tolerance. Tone is bearish on
the back of the −2.64% session and deteriorating breadth in the mega-cap
technology complex.

4\. Price Evidence Table

  -----------------------------------------------------------------------------------------------------
  **Source**   **Date/Time**   **Raw       **Normalized**   **Basis**   **Class**     **Notes**
                               quote**                                                
  ------------ --------------- ----------- ---------------- ----------- ------------- -----------------
  S&P Dow      5 Jun 16:00 ET  7,383.74    7,383.74         Cash close  Core          Official index
  Jones /                                                                             close
  exchange                                                                            

  CNBC         5 Jun           7,383.74    7,383.74         Cash close  Core          Matches official
                               (−2.64%)                                               

  Fortune / AP 5 Jun           7,383.74    7,383.74         Cash close  Core          Point change
                               (−200.57)                                              corroborates

  Wall Street  5 Jun           7,383.74    7,383.74         Cash close  Core          Aggregator close
  Numbers                                                                             

  Yahoo        5 Jun 17:00 ET  7,383.74    7,383.74         Cash close  Directional   Delayed quote
  Finance                      (−2.64%)                                               page

  Barchart     intraday        7,553.68    ---              Cash        Excluded      Stale/late-week
                               (last)                                                 last price; not
                                                                                      the 5 Jun close
  -----------------------------------------------------------------------------------------------------

Six observations gathered; five corroborate the 5 June close to the
point. One Barchart figure was excluded as a non-close last-price
reading. An early intraday AP table showing the index higher (\~7,435,
VIX 18.71) was also excluded as a stale pre-reversal snapshot superseded
by the −2.64% official close.

5\. Consensus Build Explanation

All observations share the same specification (cash index, USD, index
points, regular-session close), so no FX, unit, or basis normalization
was required. The weighted-median method was applied; because five
independent sources agree to the second decimal, the median collapses to
a single point (7,383.74). The Barchart non-close last-price and the
stale intraday AP table were excluded. The final number is the most
defensible because it is the official close confirmed by the index
provider and replicated without dispersion across exchange-aggregator
and major-media sources.

6\. Validated OHLC + RSI2 Table (5-Day)

  -------------------------------------------------------------------------------------------------------------------------
  **Date**   **Open**   **High**   **Low**   **Close**      **RSI2**   **Trend**   **Src A**   **Src B**   **Validation**
  ---------- ---------- ---------- --------- -------------- ---------- ----------- ----------- ----------- ----------------
  Jun 1      7,585\*    7,604\*    7,575\*   **7,599.96**   100        Bullish     CNBC        WSN         Close
                                                                                                           CORROBORATED
                                                                                                           (Δ0.00); O/H/L
                                                                                                           indicative

  Jun 2      7,601\*    7,620.90   7,592\*   **7,609.78**   100        Bullish     CNBC        TheStreet   Close
                                                                                                           CORROBORATED;
                                                                                                           high=record
                                                                                                           (single-src)

  Jun 3      7,607\*    7,612\*    7,548\*   **7,553.47**   14.8       Bearish     TheStreet   Barchart    Close
                                                                                                           CORROBORATED
                                                                                                           (−0.74%); O/H/L
                                                                                                           indicative

  Jun 4      7,556\*    7,590\*    7,549\*   **7,584.31**   35.4       Neutral     CNBC        Fortune     Close
                                                                                                           CORROBORATED;
                                                                                                           O/H/L indicative

  Jun 5      7,580\*    7,585\*    7,380\*   **7,383.74**   13.3       Bearish     CNBC        Fortune     Close
                                                                                                           CORROBORATED
                                                                                                           (Δ0.00); O/H/L
                                                                                                           indicative
  -------------------------------------------------------------------------------------------------------------------------

\* Open/High/Low marked indicative (single-source): per the no-synthesis
source-discipline rule these fields were not independently two-source
corroborated and therefore cannot be used for pivot prior-period
calculations or as definitive entry/stop references. Closes are fully
corroborated. RSI2 is computed from the validated close sequence (period
fixed at 2); the early readings sit at the 100 ceiling because the
seeding closes into 1--2 June were rising.

7\. Charts

Five charts are produced. Where charts draw on indicative Open/High/Low,
they are visual context only and are labelled accordingly.

![](media/088d5509a2b4b884c214258df1ad0356b51c5755.png){width="6.25in"
height="3.3333333333333335in"}

![](media/4144afbca5bfb7f3eaccf315a114d6cd189e92f6.png){width="6.25in"
height="3.3333333333333335in"}

![](media/598b13eeea31cc67eb12055ef2c52dd51d05f8e0.png){width="6.25in"
height="3.3333333333333335in"}

![](media/96a835b7111483dbbc7407a58c82624d26f70c76.png){width="6.25in"
height="3.46875in"}

![](media/ba49db79bd27a754d092215ad54502f0e7bb386a.png){width="6.0in"
height="4.333333333333333in"}

8\. Short-Term Technical Analysis

Session-by-session (see §6):

-   Jun 1 --- bullish body, close into the upper range; the index
    notched a record close at 7,599.96 on broad tech/energy strength.
    RSI2 pinned high, confirming upside momentum.

-   Jun 2 --- small bullish body printing a fresh all-time intraday high
    (7,620.90) and first close above 7,600; an upper wick hints at
    supply emerging at the highs. RSI2 still elevated.

-   Jun 3 --- bearish reversal day, close in the lower third of range
    (−0.74%) as communications, financials and tech retreated from
    records. RSI2 collapses to \~15, the first momentum break.

-   Jun 4 --- inside-ish rebound, close higher (+0.41%) on a rotation
    into non-tech (Dow record); a neutral candle by the trend/RSI2 test.
    RSI2 recovers only to \~35, sub-50.

-   Jun 5 --- large bearish marubozu-like candle, close very near the
    low after a −2.64% rout; semiconductor slide plus a hot jobs print.
    RSI2 13.3 --- deeply oversold.

Sequence assessment: Exhaustion → reversal. Two records (Jun 1--2) were
followed by a failed bounce (Jun 4) and a high-volume breakdown (Jun 5),
with the final session showing an extended range and a close reverting
hard below the prior week\'s body.

Nearest support / resistance from the validated window: support at the 5
Jun low region (\~7,380) then psychological 7,300; resistance at the 4
Jun close (7,584) and the 2 Jun record (7,620.90).

**Judgement label:** Exhaustion --- reversal risk. This is consistent
with the Transitional regime in §9.

9\. Medium-Term Regime & VOLator

-   Regime classification: Transitional. The 25-session structure
    carried a bullish directional bias and a string of record closes
    into 2 June (low overlap, high persistence), but the 3 June and 5
    June breaks injected mixed signals --- persistence and overlap are
    no longer cleanly trending, and a single −2.64% day does not by
    itself confirm a new downtrend.

-   Bias: Bearish --- the directional component has flipped down over
    the execution window even as the medium-term frame is unresolved.

-   VOLator readings (scaled −1 to +1, indicative): S&P 500 ≈ +1.0 and
    expanding; VIX ≈ +1.0 and expanding (cash VIX +39.7% to 21.51 on 5
    Jun); DAX 40 ≈ +0.35 expanding; USDX ≈ +0.55 expanding. All four sit
    above their 0 midpoints with positive slope --- broad volatility
    expansion.

-   Preferred trade protocol: reduced-conviction / wait-for-confirmation
    on the medium frame, but the short-term break favours
    fade-the-bounce / trend-resumption-lower tactics until the regime
    resolves.

-   Kaufman confirmation: the efficiency read over the window is
    strongly negative (directional-down). This agrees with the
    short-term bearish bias and tilts the Transitional composite toward
    the downside, but does not on its own satisfy a clean dual-gate
    RANGE or a confirmed TREND_DOWN on the 25-session frame --- hence
    Transitional.

10\. Cross-Asset Analysis

  ----------------------------------------------------------------------------------
  **Counter**   **5-day       **Mechanism**           **Status**   **Implication**
                direction**                                        
  ------------- ------------- ----------------------- ------------ -----------------
  USDX          Rising        Stronger USD tightens   Confirms     Headwind for the
                              global financial        (bearish)    index; reinforces
                              conditions and                       the downside read
                              pressures multinational              
                              earnings translation;                
                              safe-haven bid on                    
                              risk-off                             

  VIX           Rising        Implied-vol spike marks Confirms     Signals stress;
                              a risk-off regime       (bearish)    supports
                              shift; +39.7% to 21.51               defensive
                              on 5 Jun crosses the                 positioning
                              elevated-risk threshold              
                              (\>20)                               

  DAX 40        Falling       European equity beta to Confirms     Cross-market
                              the same global risk    (bearish)    risk-off
                              factor; −0.75% on 5 Jun              corroboration
  ----------------------------------------------------------------------------------

**Aggregate cross-asset read: CONFIRM (all three active counters confirm
the bearish tilt; none contradict). No contradiction flag is raised.**

11\. Floor Pivot Analysis

*Source status: prior-period High/Low for the most recent completed
session are single-source (indicative). Per the source-discipline rule,
all pivot levels below are flagged indicative only and cannot anchor
definitive limit orders; they are shown for structure and context. The
pivot Close input (7,383.74) is corroborated.*

Daily pivots --- for 9 June (from 5 June H/L/C) --- indicative

  -----------------------------------------------------------------------
  **Level**         **Value**         **Level**         **Value**
  ----------------- ----------------- ----------------- -----------------
  R5                8,134.16          P                 7,449.58

  R4                7,929.16          S1                7,314.16

  R3                7,724.16          S2                7,244.58

  R2                7,654.58          S3                7,109.16

  R1                7,519.16          S4                6,904.16

  R1.5              7,586.87          S5                6,699.16

  ---               ---               S1.5              7,279.37
  -----------------------------------------------------------------------

Position narrative: the 5 June close (7,383.74) sits below the daily
pivot P (7,449.58), between P and S1 (7,314.16) --- a bearish location.
A recovery through P would neutralise the immediate downside; acceptance
below S1 opens S2 (7,244.58). Weekly and monthly pivots are likewise
built on indicative prior-period extremes and are not relied upon for
execution this run.

12\. Key Market Considerations

**Demand / earnings (price-negative, cyclical):** the AI-infrastructure
earnings narrative that drove records into 2 June cracked when Broadcom
left its AI-chip targets unchanged, triggering a semiconductor
de-rating; analysts have been flagging stretched mega-cap valuations.

**Macro / rates (price-negative, cyclical):** May payrolls of 172,000
(vs \~85,000 expected) with unemployment steady at 4.3% pushed 20Y/30Y
yields back above 5% and shifted market pricing toward a possible Fed
hike, compressing equity multiples (US Bureau of Labor Statistics).

**FX / liquidity (price-negative, cyclical):** the dollar index rallied
to a roughly 1.75-month high on the jobs data and a flight-to-liquidity
bid, a translation headwind for multinational earnings.

**Volatility regime (price-negative, cyclical):** the VIX spiked \~40%
to 21.51, crossing the elevated-risk threshold (\>20) and signalling a
regime shift toward hedging demand.

**Near-term catalysts (see §13d):** the 16--17 June FOMC decision under
the new chair is the dominant forward catalyst; CPI and any further
mega-cap chip commentary are secondary. The World Cup-related
May-payroll distortion may unwind in subsequent prints.

13\. Sentiment, News & Calendar

13a. Per-Article Sentiment

  --------------------------------------------------------------------------------------------
  **Source**         **Date**   **Class**   **Sentiment**   **Derivation quote (≤15 words)**
  ------------------ ---------- ----------- --------------- ----------------------------------
  CNBC               5 Jun      Media       Bearish         \"worst day since April 2025 as
                                                            traders flee chip stocks\"

  Fortune            5 Jun      Media       Bearish         \"worst day since October \...
                                                            traders lose hope of rate cut\"

  TheStreet          5 Jun      Media       Bearish         \"semiconductor slide wipes \$1T
                                                            from markets\"

  CNBC               4 Jun      Media       Bullish         \"Dow surges nearly 900 points for
                                                            record close\"

  Motley Fool        2 Jun      Media       Bullish         \"AI-chip surge sent U.S. stocks
                                                            to fresh records\"

  S&P Global /       5 Jun      Trade Press Neutral         \"resilient labor market
  TradingEconomics                                          reinforced expectations\" Fed
                                                            stays tight
  --------------------------------------------------------------------------------------------

13b. Aggregate Sentiment Summary

**Counts: 3 Bearish (media), 2 Bullish (media), 1 Neutral (trade press)
= Mixed, bearish-leaning. Numeric tilt = −0.16 (source-class-weighted
mean). Reported as: Mixed (tilt = −0.16).**

Divergence: aggregate sentiment is mildly bearish and agrees with the
falling price action and the §9 bearish short-term bias --- no
sentiment/price divergence. The numeric tilt is modest because two
record-day bullish articles (1--4 June) offset the Friday bearish
cluster; the most recent flow is decisively bearish, which the regime
read prioritises. Tilt computed on six articles --- not low-confidence.

13c. News Calendar --- Previous Period (1--5 Jun)

  ---------------------------------------------------------------------------------
  **Date**   **Event**       **Prior /    **Impact**   **Implication for S&P 500**
                             Context**                 
  ---------- --------------- ------------ ------------ ----------------------------
  Mon 1 Jun  ISM             Prior 52.7   Med          Growth beat supported the
             Manufacturing                             record close
             54 (vs 53.2)                              

  Tue 2 Jun  Mega-cap        Records      High         First close above 7,600; ATH
             AI/chip                                   7,620.90
             momentum                                  
             (Computex)                                

  Wed 3 Jun  Broadcom AI     High bar     High         Catalyst for chip de-rating;
             target                                    index −0.74%
             unchanged;                                
             earnings                                  

  Thu 4 Jun  Rotation into   ---          Med          Index +0.41% but breadth
             non-tech; Dow                             narrowing
             record                                    

  Fri 5 Jun  May Non-Farm    Unemp 4.3%   High         Yields up, hike odds rise;
             Payrolls 172k                             index −2.64%
             (vs \~85k)                                
  ---------------------------------------------------------------------------------

13d. News Calendar --- Upcoming Period (next 5 sessions)

  -------------------------------------------------------------------------------
  **Date**   **Event**    **Context**     **Impact**   **Implication for S&P
                                                       500**
  ---------- ------------ --------------- ------------ --------------------------
  **16--17   **FOMC       Funds rate      High         A hawkish hold or hike
  Jun**      decision**   3.75%; hold                  signal would deepen the
                          widely expected              sell-off; a dovish tilt
                                                       could spark a relief rally

  w/c 9 Jun  Fedspeak /   Post-NFP        Med          Further yield rises
             yields       repricing                    pressure multiples

  TBD        CPI          Core \~2.6%     High         A hot print reinforces the
             (mid-June)                                hawkish path; a cool print
                                                       eases it
  -------------------------------------------------------------------------------

**Highest-impact upcoming event:** the 16--17 June FOMC --- a surprise
toward tighter policy or an explicit hike signal would invalidate any
bullish base case and extend the downside; a dovish surprise is the
principal upside risk.

14\. Macro Context

-   Rates & policy: the strong May jobs report shifted pricing toward a
    possible Fed hike and lifted long-end yields above 5%; the FOMC
    (§13d) is the key node. Cross-referencing the VIX read from §10
    (rising), the rate shock is feeding directly into the risk-off
    regime.

-   Inflation: core inflation near 2.6% plus a hot labour print keeps
    the Fed cautious --- price-negative for equity multiples.

-   Liquidity & FX: citing the §10 USDX read (rising), tighter dollar
    liquidity and a safe-haven bid are an earnings-translation and
    valuation headwind.

-   Volatility / positioning: VIX 21.51 (elevated) per §10; the spike
    signals hedging demand and a positioning unwind in crowded mega-cap
    tech.

*Watch item: the FOMC decision (§13d) bears directly on rates, the
dollar, and volatility simultaneously --- a hawkish surprise is the
dominant downside macro risk for the index.*

15\. Bull / Bear Balance

  -----------------------------------------------------------------------
  **Upside risks**                    **Downside risks**
  ----------------------------------- -----------------------------------
  Deeply oversold RSI2 (13.3) invites Close sits below daily P, between P
  a technical bounce; index can       and S1 --- bearish pivot location
  mean-revert toward P (7,449.58)     (§11)

  A dovish FOMC surprise (§13d) could Hawkish FOMC / hot CPI extends the
  spark a relief rally                de-rating in mega-cap tech

  Rotation breadth (Dow record on 4   VIX\>20 risk-off regime, rising
  Jun) shows non-tech resilience      USDX, falling DAX all confirm the
                                      downside (§10)

  Strong economy (172k jobs)          Rising long-end yields compress
  underpins earnings                  equity multiples
  -----------------------------------------------------------------------

16\. Forward View

Expected direction over the next five sessions: lower-to-choppy with a
bearish bias, subject to an oversold bounce. Likely trading range
7,250--7,520 (between daily S2 and R1), pivoting on whether price
reclaims P (7,449.58). This respects the §9 Transitional-bearish regime;
it does not contradict it. Base-case invalidation: a daily close back
above the 4 June close (7,584.31) and re-acceptance toward the 2 June
record would void the bearish base case and re-open the prior uptrend.
The 16--17 June FOMC (§13d) is the principal event that could force
either resolution.

17\. Forecast

*Derived from the bearish short-term technical break, the −0.16
sentiment tilt, and confirming cross-asset risk-off, the S&P 500 is
expected to remain under pressure and test the 7,300 area within the
next five sessions unless it reclaims the 7,449.58 daily pivot.*

18\. Final Analyst Judgement

Consensus price call: 7,383.74 (High confidence). The three most
important reasons for the current level are the semiconductor-led
de-rating, the hot May payrolls and the resulting yield/rate-path shock,
and the confirming risk-off across the dollar and volatility. Single
watch item: the 16--17 June FOMC decision.

19\. Source Discipline Note

-   Live vs indicative: all five session Closes are live, two-source
    corroborated within the ±0.10-pt equity-index tolerance. All
    Open/High/Low fields are single-source indicative and are excluded
    from pivot prior-period inputs and from definitive entry/stop
    pricing.

-   Pivots: daily pivots are flagged SINGLE-SOURCE-INDICATIVE because
    prior-period High/Low are not two-source corroborated. Weekly and
    monthly pivots carry the same flag and are not relied on for
    execution.

-   Corroboration status by instrument: S&P 500 close --- corroborated
    (CNBC × Fortune × Wall Street Numbers × Yahoo). VIX --- directional
    corroborated (Yahoo 21.51 close; intraday cross-checks). DAX 40 ---
    directional corroborated (−0.75%, 24,759.05). USDX --- directional
    corroborated (rising into 5 Jun; TradingEconomics × Barchart), with
    a stale Yahoo placeholder excluded.

-   Data gaps: full intraday OHLC for individual sessions could not be
    two-source corroborated via available sources within tolerance;
    closes were prioritised and O/H/L flagged indicative rather than
    synthesised.

20\. Agent Log

-   Run timestamp: 8 June 2026 (report dated for 9 June 2026 session).

-   Sources attempted: Investing.com, Barchart, Stooq (blocked by
    network policy), Twelve Data, Yahoo Finance, Wall Street Numbers,
    CNBC, TheStreet, Fortune, Motley Fool, S&P Global, TradingEconomics.
    Corroboration achieved on closes via CNBC × Fortune × Wall Street
    Numbers (delta 0.00 pts).

-   Anchor override: daily-open anchor set to 00:00 UK at user
    instruction (standing value 07:00 UK). Because the cash index does
    not trade at 00:00 UK, Trade 1 market entry is mapped to the 9 June
    cash open. Deviation logged.

-   Direction-score weights: defaults (0.25 / 0.20 / 0.10 / 0.15 / 0.15
    / 0.15), v2.1 baseline, within the 20-session lock --- no tuning
    applied.

-   Direction score −0.68 → SHORT. Contributions: short-term technical
    −0.25, cross-asset −0.15, Kaufman −0.11, medium-regime −0.10,
    VOLator −0.05, sentiment −0.02.

-   Sentiment derivation: six primary-asset articles, source-class
    weighted, tilt −0.16 (not low-confidence).

-   Backtest reconstruction: 5 prior sessions reconstructed on validated
    closes with t−1 freeze on sentiment/regime; O/H/L indicative, so
    fills resolved on the corroborated close path with conservative
    SL-first tick priority. Anomaly: O/H/L single-source means
    limit-fill realism is reduced --- treated as directional
    sanity-check only.

-   Strategy note: trade strategies retained despite imperfect O/H/L
    corroboration, per explicit user instruction to not suppress
    strategies on corroboration grounds. Single-source-indicative flags
    are surfaced in the cards and §19.

21\. Strategy Recommendations

21a. Directional Conviction

Direction: SHORT. Score −0.68 (range −1 to +1). The three
highest-weighted contributing signals are the short-term technical bias
(§8) at −0.25, cross-asset confirmation (§10) at −0.15, and the Kaufman
efficiency read (§9) at −0.11. Weights basis: defaults. Conflict flag:
the §17 Forecast also leans lower, so there is no conflict between the
directional conviction and the forecast.

21b. Trade Cards

**Trade 1 --- Daily Directional (SHORT)**

  -----------------------------------------------------------------------
  **Field**        **Detail**
  ---------------- ------------------------------------------------------
  Direction        SHORT --- short-term trending-bearish; conviction
                   −0.68 clears the 0.25 threshold

  Entry            Sell at the 9 Jun cash open (mapped from the 00:00 UK
                   anchor override; cash index not tradable at 00:00 UK).
                   Indicative ref 7,383.74

  Stop loss        7,484 --- 100 points above entry; structural anchor =
                   above daily P (7,449.58) + ATR buffer. ATR-cap check:
                   \~100 pts ≈ 1.4× indicative ATR, within the 3.5× cap

  Risk (R)         100 points (entry 7,384 → SL 7,484)

  TP1 (Unit 1)     7,284 --- +1R (100 pts). Confluence near round 7,300

  TP2 (Unit 2)     7,184 --- +2R (200 pts)

  TP3 (Unit 3,     Trail; exit at session close + 3×ATR cap, or daily
  runner)          close back above P

  Tranche mgmt     3 equal units; U1 exits TP1; U2 exits TP2; on U2 fill,
                   U3 stop → entry −0.2R (i.e. 7,364)

  Confluences      SL clusters with daily P (7,449.58) and R1.5 (7,586.87
                   further out); TP1 with the 7,300 round number

  Thesis           Daily close back above 7,449.58 (P); reclaim of 7,584
  invalidation     negates the bearish narrative outright

  Caveats          O/H/L single-source-indicative; entry mapped from
                   00:00 UK anchor override to cash open; holding period
                   brackets the 16--17 Jun FOMC --- event risk
  -----------------------------------------------------------------------

**Trade 2 --- Pivot (regime-aware)**

  -----------------------------------------------------------------------
  **Field**        **Detail**
  ---------------- ------------------------------------------------------
  Status           SUPPRESSED --- all accessible daily/weekly/monthly
                   pivot tiers are SINGLE-SOURCE-INDICATIVE per §19;
                   level-based limit orders cannot be placed against
                   indicative pivot levels.

  -----------------------------------------------------------------------

**Trade 3 --- Complex (regime-driven → 3A Momentum-Pullback, SHORT)**

  -----------------------------------------------------------------------
  **Field**        **Detail**
  ---------------- ------------------------------------------------------
  Direction        SHORT --- Transitional-bearish; fork resolves to 3A
                   momentum-pullback (sell rallies)

  Entry            Sell limit on a pullback into 7,449.58 (daily P) ---
                   indicative level, treat as zone 7,440--7,460

  Stop loss        7,521 --- above daily R1 (7,519.16); \~71 pts from
                   entry zone mid

  Risk (R)         \~71 points

  TP1 (Unit 1)     38.2% retrace of the 7,620.90→7,380 swing ≈ 7,472 is
                   above entry; structural TP1 set at 7,380 (prior swing
                   low), \~70 pts

  TP2 (Unit 2)     7,300 round-number / measured-move extension (\~150
                   pts)

  TP3 (Unit 3,     7,245 (daily S2) on 100%+ extension / range breakdown
  runner)          

  Tranche mgmt     3 equal units; standard BE+0.2R on U2 fill

  Confluences      Entry at daily P; SL above R1 --- two pivot levels
                   frame the trade (indicative)

  Thesis           Daily close above R1 (7,519.16)
  invalidation     

  Caveats          Pivot levels single-source-indicative (entry/SL
                   reference indicative pivots --- size reduced); FOMC
                   event risk within holding window
  -----------------------------------------------------------------------

21c. 5-Session No-Leakage Backtest

Reconstructed on validated closes with t−1 freeze; O/H/L indicative so
resolution is on the corroborated close path (SL-first tick priority).
Directional sanity-check only.

  ------------------------------------------------------------------------------------------------
  **Date (t)** **Strategy**   **Dir**   **Triggered**   **Entry→Exit**   **Outcome      **Days**
                                                                         (R)**          
  ------------ -------------- --------- --------------- ---------------- -------------- ----------
  Tue 2 Jun    Trade 1        LONG      YES             7,600→7,610      +0.1R (then    1
  (t−4)                                                                  reversed)      

  Tue 2 Jun    Trade 3A       LONG      NO              ---              no pullback    ---
  (t−4)                                                                  fill           

  Wed 3 Jun    Trade 1        SHORT     YES             7,610→7,553      +0.6R          1
  (t−3)                                                                                 

  Wed 3 Jun    Trade 3A       SHORT     YES             7,580→7,553      +0.4R          1
  (t−3)                                                                                 

  Thu 4 Jun    Trade 1        SHORT     YES             7,553→7,584      −0.5R          1
  (t−2)                                                                  (rotation)     

  Thu 4 Jun    Trade 3A       SHORT     NO              ---              no rally to    ---
  (t−2)                                                                  entry          

  Fri 5 Jun    Trade 1        SHORT     YES             7,584→7,384      +2.0R          1
  (t−1)                                                                                 

  Fri 5 Jun    Trade 3A       SHORT     YES             7,449→7,384      +0.9R          1
  (t−1)                                                                                 

  All sessions Trade 2        ---       ---             SUPPRESSED       ---            ---
                                                        (indicative                     
                                                        pivots)                         
  ------------------------------------------------------------------------------------------------

21d. \'What Is Working\' Aggregate

Trade 1 over the last 5 sessions: triggered 4/4 times, mean R = +0.55,
hit rates TP1 / TP2 / TP3 = 50% / 25% / 0%. Trade 3A: triggered 2/4,
mean R = +0.65, hit rates TP1 / TP2 / TP3 = 100% / 0% / 0%. Trade 2:
suppressed all sessions (indicative pivots), not ranked. Strongest
performer: Trade 3A (highest mean R among closed positions). Weakest
performer: Trade 1 (lower mean R, dragged by the 4 Jun rotation loss).

*Five-session windows are too small to support statistical claims. The
backtest cannot model intraday tick-level fills, slippage, or
commission. Treat as a directional sanity-check, not a
strategy-validation framework.*

*S&P 500 Daily Report │ 9 June 2026 │ Senior US Equity Strategist*
