**S&P 500 (CASH INDEX)**

Daily Technical & Strategy Report

**Report for session: Thursday 16 July 2026**

Data as of close Tuesday 14 July 2026 · Prepared 15 July 2026

  -----------------------------------------------------------------------
  **Field**             **Value**
  --------------------- -------------------------------------------------
  Primary asset         S&P 500 cash index (\^GSPC)

  Instance              M1 --- S&P 500 (Cash Index) v2.1

  Role                  Senior US Equity Strategist

  Counters              DX-Y.NYB (USDX) · \^VIX · \^GDAXI (DAX 40)

  Strategies module     ENABLED --- §21 produced

  Daily open anchor     00:00 UK \*\* OVERRIDDEN from 07:00 UK \*\*

  Output length         Standard (§1--§21)

  Last corroborated     7,543.59 (14-Jul-2026)
  close                 
  -----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| **DATA INTEGRITY SUMMARY --- READ FIRST**                             |
|                                                                       |
| CLOSE prices: fully two-source corroborated across all 20 sessions    |
| (Investing.com x FRED/S&P Dow Jones official). Maximum delta 0.0000   |
| pts against a ±0.10 pt tolerance.                                     |
|                                                                       |
| OPEN / HIGH / LOW: SINGLE-SOURCE (Investing.com only). No second      |
| source returned intraday H/L. Under the Source Discipline Protocol §4 |
| these are \'indicative only\' and MAY NOT be used for pivot           |
| calculations or stop-loss pricing.                                    |
|                                                                       |
| CONSEQUENCE: all pivot levels and the Trade 1 structural stop inherit |
| a SINGLE-SOURCE-INDICATIVE flag. Trade cards are produced per         |
| explicit user instruction to be lenient on corroboration; they are    |
| NOT protocol-clean and must not be executed as-is without verifying   |
| H/L against a second source.                                          |
|                                                                       |
| ANCHOR: 00:00 UK override is not an executable market entry on a cash |
| index that trades 14:30--21:00 UK. Treated as a pending order. See    |
| §21 and §20.                                                          |
+-----------------------------------------------------------------------+

Contents

1\. Executive Summary

The S&P 500 closed at 7,543.59 on 14 July 2026, up 28.25 points (+0.38%)
on the session and up 60.88 points over the trailing five sessions. The
index sits 11.46 points above its 5-day mean and 68.46 points above its
20-day mean, but is essentially unchanged over the full 25-session
window (-10.70 points), which is the central tension in this report: a
firm short-term tape inside a flat medium-term structure.

The Kaufman Efficiency Ratio reads +0.3252, comfortably above the 0.13
trending threshold, classifying the tape as Trending Up. Realised
volatility is compressing (VOLator slope -0.0395) and the VIX is near 16
--- well below the 20 level that the M1 instance defines as elevated
risk. RSI2 at 58.01 is mid-range, so the move carries no short-term
exhaustion signal in either direction.

The composite direction score is +0.2750 against a conviction threshold
of 0.25. Trade 1 therefore fires LONG, but by a margin of 0.025 --- this
is a marginal pass, not a conviction call, and the report treats it as
such throughout.

**The dominant caveat is not directional. It is that Open/High/Low data
could not be corroborated by a second source, which under the governing
protocol invalidates every pivot level and the structural stop that the
trade cards depend on. Direction is well-evidenced; the price levels
attached to it are not.**

2\. Instance Configuration & Overrides

Two deviations from the M1 S&P 500 v2.1 populated instance apply to this
run. Both are user-directed and are logged here and in §20.

  ---------------------------------------------------------------------------------------------
  **Item**                               **M1         **This run**  **Assessment**
                                         default**                  
  -------------------------------------- ------------ ------------- ---------------------------
  \[DAILY_OPEN_ANCHOR\]                  07:00 UK     00:00 UK      USER OVERRIDE ---
                                                                    materially affects Trade 1
                                                                    executability. See below.

  Corroboration discipline               Halt on      Lenient ---   USER OVERRIDE --- trade
                                         failure      proceed       cards produced on
                                                                    single-source O/H/L.

  \[W\_\*\] weights                      Locked 20    Unchanged     Compliant --- defaults
                                         sessions                   retained.

  \[PRODUCE_STRATEGY_RECOMMENDATIONS\]   YES          YES           Compliant.

  Session date                           n/a          16-Jul-2026   Report generated on 15-Jul
                                                                    for the 16-Jul session.
  ---------------------------------------------------------------------------------------------

2a. On the 00:00 UK anchor override

The override has been applied as instructed. It is worth being explicit
about what it means, because the project\'s own documentation addresses
this case directly.

The M1 instance sets 07:00 UK deliberately, on the reasoning that the
S&P 500 cash index trades 14:30--21:00 UK and 07:00 UK anchors the
European pre-NY-open window where futures-led re-pricing is most
informative. PATCHES_v1_2 §P6 goes further and states plainly that a
market trade at 00:00 UK on the cash S&P 500 is not executable,
prescribing an anchor adjustment as the remedy.

**At 00:00 UK on 16 July the cash index will not be trading and no cash
print will exist. The Trade 1 entry below is therefore specified as a
pending order referenced to the prior corroborated close, triggering at
the 14:30 UK cash open. It is not a market fill. The 7,543.59 entry
reference will not survive the overnight gap --- ES futures will
re-price through the Asia and European sessions --- so realised slippage
against this reference should be expected and is unquantifiable from
cash data alone.**

*If the intent of the override was to align this run with a 24-hour
instrument convention (as WTI and EUR/USD use), the cleaner expression
would be to run the analysis against ES futures rather than the cash
index. That is a change of instrument, not of anchor, and is outside
this instance.*

3\. Source Discipline & Corroboration

Sources were attempted in the rank order given by the Source Discipline
No-Synthesis Protocol. Outcomes:

  --------------------------------------------------------------------------------------
  **Rank**   **Source**      **Tier**   **Outcome**    **Detail**
  ---------- --------------- ---------- -------------- ---------------------------------
  3          Stooq           Tier 1     FAILED         robots.txt disallow on CSV
                                                       endpoint; container egress
                                                       blocked.

  ---        Investing.com   Tier 2     CORROBORATED   Full OHLC, 20 sessions. Source A.

  ---        Barchart        Tier 2     PARTIAL        Table JS-rendered; no OHLC rows.
                                                       Last price 7,553.68 + 52wk high
                                                       7,620.90 matched Source A ---
                                                       used as sanity check only.

  ---        Yahoo Finance   Tier 3     PARTIAL        Live quote only (7,560.95
                                                       intraday 15-Jul). Demoted per
                                                       protocol; no historical OHLC.

  49         FRED / S&P DJI  Tier 6     CORROBORATED   Official S&P Dow Jones daily
                                                       closes through 14-Jul. Source B.
                                                       CLOSE ONLY --- no intraday H/L.
  --------------------------------------------------------------------------------------

3a. Close corroboration --- Source A × Source B

Tolerance for equity indices: ±0.10 points. All 20 sessions corroborated
at zero delta --- Investing.com is evidently carrying the official S&P
DJI close unmodified.

  -----------------------------------------------------------------------------
  **Session**   **Investing.com**   **FRED / S&P     **Delta**   **Status**
                                    DJI**                        
  ------------- ------------------- ---------------- ----------- --------------
  15-Jun        7,554.29            7,554.29         0.00        PASS

  16-Jun        7,511.35            7,511.35         0.00        PASS

  17-Jun        7,420.10            7,420.10         0.00        PASS

  18-Jun        7,500.58            7,500.58         0.00        PASS

  22-Jun        7,472.79            7,472.79         0.00        PASS

  23-Jun        7,365.46            7,365.46         0.00        PASS

  24-Jun        7,358.22            7,358.22         0.00        PASS

  25-Jun        7,357.49            7,357.49         0.00        PASS

  26-Jun        7,354.02            7,354.02         0.00        PASS

  29-Jun        7,440.43            7,440.43         0.00        PASS

  30-Jun        7,499.36            7,499.36         0.00        PASS

  01-Jul        7,483.23            7,483.23         0.00        PASS

  02-Jul        7,483.24            7,483.24         0.00        PASS

  06-Jul        7,537.43            7,537.43         0.00        PASS

  07-Jul        7,503.85            7,503.85         0.00        PASS

  08-Jul        7,482.71            7,482.71         0.00        PASS

  09-Jul        7,543.64            7,543.64         0.00        PASS

  10-Jul        7,575.39            7,575.39         0.00        PASS

  13-Jul        7,515.34            7,515.34         0.00        PASS

  14-Jul        7,543.59            7,543.59         0.00        PASS
  -----------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| **SINGLE-SOURCE FIELDS --- Protocol §4 register**                     |
|                                                                       |
| Instrument: \^GSPC. Fields: OPEN, HIGH, LOW. Sessions: all 20         |
| (15-Jun-2026 through 14-Jul-2026).                                    |
|                                                                       |
| Reason: FRED/S&P DJI (the only corroborating source reached)          |
| publishes closing values only. Stooq --- the protocol\'s designated   |
| free OHLC alternative --- was unreachable. No second independent      |
| intraday H/L source was obtained.                                     |
|                                                                       |
| Permitted uses: directional context, chart visualisation (labelled),  |
| supplementary narrative.                                              |
|                                                                       |
| Prohibited uses: pivot prior-period calculations, settlement          |
| references, entry or stop-loss pricing, any value cited as definitive |
| in a consensus price build.                                           |
|                                                                       |
| Every pivot table and the Trade 1 structural stop in this report fall |
| within the prohibited category and are flagged accordingly at point   |
| of use.                                                               |
+-----------------------------------------------------------------------+

4\. Validated OHLC + RSI2 (5-Day)

**Close column: CORROBORATED. Open/High/Low columns: SINGLE-SOURCE ---
INDICATIVE ONLY.**

  --------------------------------------------------------------------------------
  **Session**   **Open †** **High †** **Low †**  **Close    **Change**   **Range
                                                 ✓**                     †**
  ------------- ---------- ---------- ---------- ---------- ------------ ---------
  08-Jul-2026   7,476.54   7,488.51   7,421.82   7,482.71   -21.14       66.69

  09-Jul-2026   7,491.60   7,546.89   7,481.73   7,543.64   +60.93       65.16

  10-Jul-2026   7,547.64   7,579.93   7,508.16   7,575.39   +31.75       71.77

  13-Jul-2026   7,547.53   7,565.37   7,506.41   7,515.34   -60.05       58.96

  14-Jul-2026   7,536.70   7,557.44   7,513.23   7,543.59   +28.25       44.21
  --------------------------------------------------------------------------------

*† single-source indicative ✓ two-source corroborated*

Trading-date validation: 5 of 5 sessions are Monday--Friday. The
03-Jul-2026 US market holiday (Independence Day observed) correctly
reduces the count in the wider window; no weekend rows, no unjustified
duplicates. RSI2 latest = 58.01.

5\. Technical Indicators --- M3 §11 Named Output Surface

  ------------------------------------------------------------------------------
  **Surface field**     **Value**    **Corroboration**   **Reading**
  --------------------- ------------ ------------------- -----------------------
  last_close            7,543.59     CORROBORATED        Reference price for all
                                                         cards

  atr_14                78.26        Derived (uses H/L)  Inherits single-source
                                                         flag

  rsi2_latest           58.01        From corroborated   Mid-range --- no
                                     closes              extreme

  ker_value (smoothed)  +0.3252      From corroborated   \> 0.13 → Trending Up
                                     closes              

  ker_class             Trending Up  Derived             Strongest single input

  volator_slope         -0.0395      Derived (uses H/L)  Volatility compressing

  swing_high_5d         7,579.93     SINGLE-SOURCE       Not usable for pricing

  swing_low_5d          7,421.82     SINGLE-SOURCE       Not usable for pricing

  swing_high_25d        7,579.93     SINGLE-SOURCE       Not usable for pricing

  swing_low_25d         7,294.18     SINGLE-SOURCE       Not usable for pricing

  regime_label          TRANSITION   Derived             See §6 --- gates
                                                         disagree

  cross_asset_confirm   MIXED        Derived             See §7

  sentiment_tilt (M2    +0.20        Narrative-derived   VIX calm, semis bid
  §13b)                                                  
  ------------------------------------------------------------------------------

*Note on ATR(14) and VOLator: both consume High/Low and therefore
inherit the single-source flag. They are used here for regime
classification (a permitted directional-context use) but the ATR-derived
stop distances in §21 sit closer to the prohibited boundary and are
flagged there.*

6\. Regime Classification

The M3 §11b mapping rule is deterministic and must return exactly one
label. Applying it:

  ------------------------------------------------------------------------
  **Gate**        **Requirement for        **Actual**          **Pass?**
                  TREND_UP**                                   
  --------------- ------------------------ ------------------- -----------
  Step 4          Trending Bullish         Bullish short /     PARTIAL
  synthesis                                flat medium         

  ker_class       Trending Up              Trending Up         PASS
                  (strong/moderate)        (+0.3252)           

  volator_slope   ≥ 0                      -0.0395             FAIL
  ------------------------------------------------------------------------

**regime_label = TRANSITION.**

The VOLator slope gate fails: TREND_UP requires a non-negative slope and
the reading is -0.0395. Under §11b the label falls through to TRANSITION
--- the default when gates disagree. This is not a technicality worth
waving through. A negative VOLator slope alongside a positive KER
describes a market grinding higher on shrinking range, which is a real
and recognisable late-trend signature rather than a healthy impulsive
advance.

The practical consequence is that Trade 3 forks to 3C (transition
breakout) rather than 3A (momentum-pullback). It also argues for reading
the +0.2750 direction score as the marginal figure it is.

7\. Cross-Asset Confirmation

  -------------------------------------------------------------------------------
  **Counter**    **Level**   **Session   **Implication for SPX**   **Verdict**
                             move**                                
  -------------- ----------- ----------- ------------------------- --------------
  DX-Y.NYB       100.597     -0.11%      Softer dollar --- mild    CONFIRM (weak)
  (USDX)                                 tailwind for              
                                         multinational earnings    
                                         translation               

  \^VIX          16.50       -3.85%      Well below the 20         CONFIRM
                                         elevated-risk line; risk  
                                         appetite intact           

  \^GDAXI (DAX   25,030.21   -0.46%      European equity diverging CONTRADICT
  40)                                    lower --- does not        
                                         confirm US strength       

  US 10Y         4.593%      +0.008      Marginally higher yields  NEUTRAL/DRAG
  (context)                              --- slight valuation drag 
  -------------------------------------------------------------------------------

**cross_asset_confirm = MIXED.**

Per the M3 hard rules, contradiction is flagged rather than suppressed:
the DAX declined 0.46% on the session while the S&P advanced 0.38%. The
mandatory USDX counter and the VIX both lean supportive, but neither
strongly. The aggregate does not confirm the long thesis --- it merely
fails to refute it, which is why the cross-asset component contributes
only +0.10 before weighting.

*VIX corroboration note: three independent readings were obtained ---
16.13 (FRED/CBOE official, 07-Jul), 16.26 (Yahoo, live 15-Jul), 16.50
(Investing.com, 14-Jul close). These are consistent in level and regime
but are not date-matched, so the VIX is used for directional context
only, as the protocol permits.*

8\. Floor Pivot Analysis

+-----------------------------------------------------------------------+
| **ALL PIVOT LEVELS BELOW ARE SINGLE-SOURCE-INDICATIVE**               |
|                                                                       |
| Pivots are computed from prior-period High/Low/Close. The H and L     |
| inputs are single-source. Source Discipline Protocol §4 explicitly    |
| prohibits single-source values from being used for pivot prior-period |
| calculations.                                                         |
|                                                                       |
| These levels are reproduced for chart visualisation and directional   |
| context only. They are NOT valid support/resistance for execution and |
| M5 §4a reads this flag through to every trade card that cites them.   |
+-----------------------------------------------------------------------+

8a. Daily pivots (from 14-Jul H/L/C)

  -----------------------------------------------------------------------
  **Level**               **Value**               **Distance from close**
  ----------------------- ----------------------- -----------------------
  **R3**                  7,607.15                +63.56

  **R2**                  7,582.30                +38.71

  **R1.5**                7,572.62                +29.03

  **R1**                  7,562.94                +19.35

  **P (pivot)**           7,538.09                -5.50

  **S1**                  7,518.73                -24.86

  **S1.5**                7,506.30                -37.29

  **S2**                  7,493.88                -49.71

  **S3**                  7,474.52                -69.07
  -----------------------------------------------------------------------

The close sits 5.50 points above the daily pivot --- effectively on it.
That is a neutral pivot position and offers no directional edge on its
own.

8b. Weekly pivots (prior week 06--10 Jul)

  -----------------------------------------------------------------------
  **Level**                           **Value**
  ----------------------------------- -----------------------------------
  **R2**                              7,683.82

  **R1**                              7,629.61

  **P (pivot)**                       7,525.71

  **S1**                              7,471.50

  **S2**                              7,367.60
  -----------------------------------------------------------------------

Price is holding above the weekly pivot at 7,525.71, which is the mildly
constructive read available from this timeframe --- subject to the same
corroboration caveat.

9\. Key Market Considerations

Semiconductor leadership is the visible driver in the 14-Jul tape: NVDA
+4.06%, MU +4.92%, SNDK +5.01%, AMD +2.57%. Breadth within the complex
is genuine rather than a single-name effect.

Against that, IBM fell 25.21% on volume of 67.44M --- a severe
single-name repricing. The index absorbed it and still closed higher,
which speaks to underlying bid, though a move of that magnitude warrants
confirmation of the cause before it is read as idiosyncratic. Healthcare
was notably weak (HCA -6.95%, ISRG -6.78%, SYK -6.15%, BIIB -8.17%),
suggesting sector rotation into technology rather than uniform risk-on.

**Per the M1 instance\'s \[ADDITIONAL_CONTEXT\], the four primary
catalysts are FOMC, NFP, CPI and mega-cap earnings. This report does not
have corroborated calendar data for the 16-Jul session; §13d
event-collision checks could not be completed. Position sizing should
account for an unverified event calendar.**

10\. Macro Context

  ------------------------------------------------------------------------
  **Factor**          **Reading**              **Direction of effect**
  ------------------- ------------------------ ---------------------------
  Dollar (USDX)       100.597, -0.11%          Mildly supportive

  US 10Y yield        4.593%, +0.008           Mild drag on valuations

  US 30Y yield        5.107%, +0.013           Long end firm --- duration
                                               pressure

  10-2 spread         31.32bp, +15.27%         Steepening --- curve
                                               normalising

  Implied vol (VIX)   16.50, -3.85%            Calm --- supportive

  Crude (WTI)         79.72, +0.48%            Neutral for index
  ------------------------------------------------------------------------

The macro backdrop is mildly supportive but not decisively so. A
steepening curve alongside a firm long end is the most notable feature:
it is consistent with growth expectations holding up, but it also raises
the discount rate applied to the long-duration technology names
currently leading the advance. That is an internal tension in the bull
case, not a confirmation of it.

11\. Bull / Bear Balance

  -----------------------------------------------------------------------
  **Upside risks**                    **Downside risks**
  ----------------------------------- -----------------------------------
  KER +0.3252 confirms an efficient   VOLator slope negative --- advance
  uptrend, the strongest single       is on shrinking range, a late-trend
  reading in the surface              signature

  VIX \~16 with no stress signal;     25-day net change is -10.70 pts ---
  risk appetite intact                no medium-term structure to the
                                      move

  Semiconductor breadth is real       DAX contradicts; global equity is
  (NVDA, MU, SNDK, AMD all firmly     not confirming
  bid)                                

  Close above both 5-day and 20-day   Direction score +0.2750 clears its
  means                               threshold by only 0.025

  Holding above the weekly pivot      IBM -25.21% unexplained; healthcare
  (indicative)                        broadly weak

  Softer dollar aids earnings         Long-end yields firm against a
  translation                         duration-heavy leadership group
  -----------------------------------------------------------------------

12\. Forward View

Expected direction over the next five trading days: mildly higher, with
low conviction.

Expected trading range: approximately 7,420 -- 7,620. The lower bound
references the 5-day swing low region and the upper bound the 52-week
high at 7,620.90 (corroborated across Investing.com and Barchart). Both
bounds are indicative --- the swing low is single-source.

Base case invalidation: a daily close below 7,421.82 (the 5-day swing
low) would break the short-term structure and flip the short-term
technical component negative. On the upside, a close above 7,620.90
would establish a new 52-week high and resolve the TRANSITION label
toward TREND_UP.

*The forward view respects the technical regime rather than overriding
it: TRANSITION with a positive but marginal direction score maps to
\'mildly higher, low conviction\', not to a directional call of
substance.*

13\. Forecast

+-----------------------------------------------------------------------+
| **FORECAST --- ONE SENTENCE**                                         |
|                                                                       |
| The S&P 500 grinds modestly higher toward 7,580--7,620 over the next  |
| five sessions on efficient-trend momentum and a calm volatility       |
| regime, but the advance is fragile --- compressing range, a           |
| contradicting DAX and a flat 25-day structure leave it vulnerable to  |
| a fast reversal below 7,421.82.                                       |
+-----------------------------------------------------------------------+

14\. Final Analyst Judgement

  -----------------------------------------------------------------------
  **Element**        **Judgement**
  ------------------ ----------------------------------------------------
  Consensus price    Mildly bullish --- 7,580 target over 5 sessions
  call               

  Confidence         LOW

  Reason 1           KER +0.3252 is a clean, corroborated-close-derived
                     trending signal --- the strongest evidence
                     available.

  Reason 2           Regime is TRANSITION, not TREND_UP: the VOLator gate
                     fails and cross-asset is MIXED. The trend lacks
                     confirmation.

  Reason 3           Direction score clears its threshold by 0.025. Small
                     changes to any component flip it to suppression.

  Single watch item  A daily close below 7,421.82 --- invalidates the
                     short-term structure and the entire long thesis.
  -----------------------------------------------------------------------

*Confidence is set to LOW rather than MEDIUM specifically because of the
data-quality position. The direction is reasonably evidenced from
corroborated closes; the levels needed to act on it are not corroborated
at all.*

15\. Source Discipline Note

Live vs indicative: closes are live and corroborated to 14-Jul-2026. All
Open/High/Low values are indicative, single-source.

Data gaps: (i) no second-source intraday H/L for \^GSPC; (ii) no
corroborated OHLC series obtained for DX-Y.NYB, \^VIX or \^GDAXI ---
counters are represented by single-source live quotes and used for
directional context only, which falls short of the M3 hard rule that
counters receive the same OHLC validation treatment as the primary;
(iii) no corroborated economic calendar for the 16-Jul session, so §13d
collision checks are incomplete.

Normalisation assumptions: none applied. No value in this report has
been synthesised, interpolated, or recalled from memory. Where a value
could not be corroborated it is labelled rather than estimated.

Corroboration status by instrument:

  ---------------------------------------------------------------------------
  **Instrument**   **Close**           **Open/High/Low**   **Usable for
                                                           pricing?**
  ---------------- ------------------- ------------------- ------------------
  \^GSPC           CORROBORATED        SINGLE-SOURCE       Close: yes.
                   (20/20)                                 Levels: no.

  DX-Y.NYB         SINGLE-SOURCE       NOT OBTAINED        No --- context
                                                           only

  \^VIX            SINGLE-SOURCE       NOT OBTAINED        No --- context
                                                           only

  \^GDAXI          SINGLE-SOURCE       NOT OBTAINED        No --- context
                                                           only
  ---------------------------------------------------------------------------

**Under an unmodified protocol run this report would have halted at §1
with a DataCorroborationError on the H/L fields. It proceeds solely
under the user\'s explicit instruction to be lenient on corroboration
and not to suppress the trading strategies.**

16\. Agent Log

Run timestamp: 15-Jul-2026, generated for the 16-Jul-2026 session.
Engine: manual execution of M1/M2/M3/M4/M5 v2.1 logic (container egress
restricted to package registries; agentic_technical_engine.py could not
fetch market data and was not invoked).

16a. Sources attempted

Stooq (rank 3) --- FAILED, robots disallow + egress block. Investing.com
--- CORROBORATED (Source A, full OHLC). Barchart --- PARTIAL,
JS-rendered table, used as sanity check (last 7,553.68; 52wk high
7,620.90 matched Source A). Yahoo Finance --- PARTIAL, live quote only,
Tier 3 per 2025 demotion. FRED/S&P DJI (rank 49) --- CORROBORATED
(Source B, closes only). Corroborating pair: Investing.com × FRED.
Sources attempted before corroboration: 5.

16b. Validation method

Close corroboration: pairwise delta vs ±0.10 pt equity-index tolerance
across 20 sessions. Max delta 0.0000. Date validation: Mon--Fri only;
03-Jul holiday verified; no duplicates.

16c. Direction-score weights basis

DEFAULT --- M1 §H.3 values unchanged (locked for the first 20
forward-test sessions). No tuning applied, so no §H.3 lock deviation to
report.

16d. Suppression reasons

Trade 1: NOT suppressed --- \|score\| 0.2750 ≥ 0.25 threshold. Trade 2:
produced (\[PRODUCE_PIVOT_TRADE\]=YES) but flagged --- every level it
cites is single-source-indicative. Trade 3: forked to 3C per TRANSITION
regime; 3A/3B not applicable. Fib swing anchor (§4b): the 4-session
lookback found no swing of magnitude ≥ 2 × ATR(14) (156.52 pts);
extending to the 10-session maximum, the largest qualifying move is the
25-day range of 285.75 pts, which qualifies --- but its endpoints are
single-source H/L, so the anchor is flagged.

16e. Backtest reconstruction notes

5 sessions replayed (08-Jul to 14-Jul). No-leakage discipline enforced:
at each session t the signal is computed strictly from closes up to t-1.
Sentiment frozen at the session-of-record value --- no forward sentiment
leaked into replayed sessions. Reconstruction uses corroborated closes
only, so the backtest is cleaner than the live trade cards.

16f. Anomalies

\(1\) FRED\'s HTML series page served a snapshot ending 13-May-2026
while its data endpoint returned data through 14-Jul-2026 --- the
endpoint was used and is the authoritative figure. (2) IBM -25.21% on
14-Jul is an extreme single-name move left unexplained by available
data. (3) 02-Jul close (7,483.24) sits 0.01 above the 01-Jul close
(7,483.23), reported as 0.00% change --- a legitimate near-zero session,
not a duplicate; both values are corroborated and it does not meet the
§1a rejection test (O=H=L=C identical to prior row). (4) Anchor override
conflicts with PATCHES §P6 --- logged in §2a.

17\. Strategy Recommendations (§21)

+-----------------------------------------------------------------------+
| **EXECUTION WARNING**                                                 |
|                                                                       |
| These cards are produced under the user\'s explicit instruction to be |
| lenient on corroboration and not suppress strategies. They are not    |
| protocol-clean.                                                       |
|                                                                       |
| Every stop-loss and every pivot level below derives from              |
| single-source High/Low data that Source Discipline Protocol §4        |
| prohibits from being used for exactly this purpose. Direction is      |
| defensible; the levels are not verified.                              |
|                                                                       |
| The 00:00 UK entry anchor is not executable on the cash index.        |
| Entries are pending orders referencing the prior close and will gap.  |
|                                                                       |
| Before risking capital: obtain a second independent source for 14-Jul |
| High/Low (7,557.44 / 7,513.23) and re-derive. If the second source    |
| disagrees beyond ±0.10 pts, every level below changes.                |
+-----------------------------------------------------------------------+

17a. Directional conviction summary

  ------------------------------------------------------------------------------------------
  **Component**     **Weight**   **Score**   **Contribution**   **Basis**
  ----------------- ------------ ----------- ------------------ ----------------------------
  W_SHORT_TECH      0.25         +0.50       +0.1250            Close \> SMA5; +60.88 over
                                                                5d; RSI2 58 (no extreme)

  W_MEDIUM_REGIME   0.20         -0.05       -0.0100            25d change -10.70 pts ---
                                                                structurally flat

  W_VOLATOR         0.10         +0.25       +0.0250            Slope -0.0395 --- vol
                                                                compressing

  W_KAUFMAN         0.15         +0.60       +0.0900            KER +0.3252, well above 0.13

  W_SENTIMENT       0.15         +0.20       +0.0300            M2 §13b: VIX calm, semis bid

  W_CROSS_ASSET     0.15         +0.10       +0.0150            MIXED --- DAX contradicts

  TOTAL             1.00         ---         +0.2750            Threshold 0.25 → Trade 1
                                                                FIRES LONG
  ------------------------------------------------------------------------------------------

**The score clears the conviction threshold by 0.025. Two-thirds of the
positive contribution comes from W_SHORT_TECH and W_KAUFMAN; the four
remaining components contribute +0.06 combined. This is a narrow,
concentrated signal.**

17b. Trade 1 --- Daily Directional

  -----------------------------------------------------------------------
  **Element**     **Value**          **Note**
  --------------- ------------------ ------------------------------------
  Direction       LONG               Score +0.2750 ≥ 0.25

  Entry           Pending order @    00:00 UK anchor NOT executable ---
                  7,543.59 ref       triggers 14:30 UK cash open. Will
                                     gap.

  Stop loss       7,402.26           swing_low_5d (7,421.82) − 0.25×ATR
                                     --- SINGLE-SOURCE, PROHIBITED BASIS

  R (risk)        141.34 pts         1.81 × ATR(14)

  TP1 (Unit 1)    7,684.93           +1R

  TP2 (Unit 2)    7,826.26           +2R --- above 52wk high; see caveats

  TP3 (Unit 3,    7,778.37           3 × ATR cap, or session close,
  runner)                            whichever first

  Tranche         3 equal units      U1→TP1; U2→TP2; on U2 fill, U3 stop
  management                         → entry + 0.2R (7,571.86)

  Thesis          7,402.26           Coincides with SL
  invalidation                       

  ATR-cap check   Cap at 7,269.68    Structural stop is tighter --- cap
                  not binding        does not apply
  -----------------------------------------------------------------------

**Mandatory §5.1 sanity flags:**

• WIDE STOP --- R = 141.34 pts exceeds 1 × ATR(14) = 78.26. Risk per
unit is 1.81 ATR.

• TP2 AMBITIOUS FOR A DAILY HORIZON --- 2R = 282.68 pts exceeds 3 × ATR
= 234.78. Per M5 §5.1 this is flagged, not suppressed. TP2 at 7,826.26
sits above the 52-week high of 7,620.90; reaching it in one session
would require a \~3.7% advance. Treat as aspirational.

• Note the internal inconsistency the rules produce here: TP3 (7,778.37)
sits below TP2 (7,826.26), because the runner is ATR-capped while TP2 is
R-multiple-derived and R is unusually wide. The runner will cap out
before TP2 is reached.

17c. Trade 2 --- Regime-Aware Pivot

  ----------------------------------------------------------------------------
  **Element**     **Value**                  **Note**
  --------------- -------------------------- ---------------------------------
  Status          PRODUCED --- ALL LEVELS    \[PRODUCE_PIVOT_TRADE\] = YES
                  UNVERIFIED                 

  Regime          TRANSITION                 Not RANGE --- mean-reversion at
                                             pivots is not the
                                             high-probability expression

  Bias            LONG toward R1             Aligns with Trade 1

  Entry zone      7,538.09 (daily P)         SINGLE-SOURCE-INDICATIVE

  Target          7,562.94 (R1) → 7,572.62   SINGLE-SOURCE-INDICATIVE
                  (R1.5)                     

  Stop            7,518.73 (S1)              SINGLE-SOURCE-INDICATIVE

  R:R             ≈ 1.28 : 1                 To R1

  Corroboration   SINGLE-SOURCE-INDICATIVE   M5 §4a inherits from parent
  flag                                       pivots dict
  ----------------------------------------------------------------------------

*Under the protocol as written this card should not exist --- its entry,
target and stop are all pivot-derived and pivots may not be computed
from single-source H/L. It is included per instruction and marked
accordingly.*

17d. Trade 3C --- Transition Breakout

Regime is TRANSITION, so the fork resolves to 3C. Per M5 §4d the anchor
is the 25-day range boundary rather than a fib swing.

  ------------------------------------------------------------------------
  **Element**        **Value**             **Note**
  ------------------ --------------------- -------------------------------
  Fork               3C (transition        3A/3B suppressed --- regime is
                     breakout)             not TREND\_\* or RANGE

  Range boundary     7,579.93              swing_high_25d ---
  (upper)                                  SINGLE-SOURCE

  Range boundary     7,294.18              swing_low_25d --- SINGLE-SOURCE
  (lower)                                  

  Confirmed break    Daily close \>        Boundary + 0.25 × ATR (19.57)
  (long)             7,599.50              

  Confirmed break    Daily close \<        Boundary − 0.25 × ATR
  (short)            7,274.61              

  Eligibility        NOT YET ELIGIBLE      14-Jul close 7,543.59 is inside
                                           the range --- no confirming
                                           close

  Fib swing anchor   25-day range, 285.75  Qualifies at 10-session
  (§4b)              pts = 3.65 × ATR      lookback (default 4 found none
                                           ≥ 2×ATR)
  ------------------------------------------------------------------------

Trade 3C does not trigger for the 16-Jul session. Price must first close
beyond 7,599.50 (long) or 7,274.61 (short). This is the correct outcome
--- a breakout strategy should not fire mid-range.

17e. Simultaneous long/short check

\[MAX_SIMULTANEOUS_LONG_SHORT\] = YES. Trades 1 and 2 are both LONG;
Trade 3C is inactive. No opposing cards, so no suppression is triggered
under this switch.

17f. Five-session no-leakage backtest

Signal at each session t computed strictly from closes up to t-1 (KER
sign + position vs SMA5). Corroborated closes only.

  -------------------------------------------------------------------------------
  **Session**   **Signal**   **KER(t-1)**   **vs       **Actual     **Result**
                                            SMA5**     move**       
  ------------- ------------ -------------- ---------- ------------ -------------
  08-Jul-2026   NONE         -0.0212        above      -21.14       no trade

  09-Jul-2026   NONE         +0.0523        below      +60.93       no trade

  10-Jul-2026   LONG         +0.0712        above      +31.75       WIN

  13-Jul-2026   LONG         +0.1421        above      -60.05       LOSS

  14-Jul-2026   NONE         +0.2435        below      +28.25       no trade
  -------------------------------------------------------------------------------

**Trades taken: 2. Wins: 1. Losses: 1. Hit rate: 50%. Net: -28.30 pts.**

*This result carries no statistical weight whatsoever. Two trades cannot
distinguish a working strategy from a coin flip; the sample exists
because \[BACKTEST_LOOKBACK_DAYS\] = 5, not because five sessions are
informative. It is reported because the module requires it. The §H.3
twenty-session weight-lock exists precisely so that weights are not
tuned on evidence this thin.*

17g. What is working

Across the replayed window the KER/SMA5 filter stayed flat on three of
five sessions, including 09-Jul (+60.93) and 14-Jul (+28.25) --- two up
sessions it missed by requiring price above the 5-day mean. It caught
10-Jul (+31.75) and was wrong on 13-Jul (-60.05), where the single loss
exceeded the single win. The pattern in this tiny sample is consistent
with the regime label: a filter built for trends is being whipsawed by a
market that is not trending cleanly, which is what TRANSITION describes.
Nothing here should be read as evidence for or against the weights.

18\. Forward-Test Session Log Entry

  -----------------------------------------------------------------------
  **Field**        **Entry**
  ---------------- ------------------------------------------------------
  Session \#       1 (of 20 minimum before any weight tuning)

  Date             16-Jul-2026

  Run timestamp    15-Jul-2026 (report prepared ahead of session)
  (UK)             

  Output dir       n/a --- manual run; engine not invoked (egress
                   restricted)

  §21 result       Trade 1 LONG @ 7,543.59 ref, SL 7,402.26, score
  summary          +0.2750. Trade 2 LONG pivot (unverified). Trade 3C not
                   eligible.

  Notes            Anchor overridden to 00:00 UK (non-executable on cash
                   --- pending order). O/H/L single-source; corroboration
                   leniency applied per user instruction. Weights at
                   default.
  -----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| **CLOSING NOTE**                                                      |
|                                                                       |
| Two aspects of this run depart from the framework\'s own safeguards,  |
| both at your explicit instruction, and both are recorded rather than  |
| quietly absorbed:                                                     |
|                                                                       |
| 1\. The corroboration leniency means the trade levels rest on         |
| unverified High/Low data. The direction (+0.2750 LONG) is derived     |
| from fully corroborated closes and stands on its own. The levels do   |
| not --- one second source for 14-Jul H/L would resolve this and       |
| re-validate every number in §17.                                      |
|                                                                       |
| 2\. The 00:00 UK anchor cannot fill on a cash index. The framework\'s |
| own PATCHES §P6 anticipates precisely this and prescribes the anchor  |
| be corrected. If the goal is a genuine 24-hour entry, ES futures      |
| rather than \^GSPC is the instrument that supports it.                |
|                                                                       |
| The report is complete and internally consistent. It should not be    |
| treated as protocol-clean.                                            |
+-----------------------------------------------------------------------+
