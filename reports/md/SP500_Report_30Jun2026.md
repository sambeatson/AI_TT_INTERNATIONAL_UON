**S&P 500 Report --- Daily: 30 June 2026**

With reference to: USDX · VIX · DAX 40

*Senior US Equity Strategist · Trading & risk review (forward-test)*

**§1 Executive Snapshot**

The S&P 500 cash index enters 30 June 2026 at a defensible consensus of
**7,354 index points** (last validated close, Fri 26 Jun), with market
tone **bearish**. Three drivers dominate: a four-session megacap-tech
unwind (Apple −6% on hardware price hikes, Micron-led memory volatility,
a reported OpenAI IPO delay); a hawkish Federal Reserve under Chair
Warsh with markets pricing roughly three rate hikes this year and a
stronger dollar at 13-month highs near 101.3; and a rotation into
defensives and small caps that has hollowed out index-level breadth. The
short-term technical state is Trending--Bearish and the medium-term
25-session structure is also Trending--Bearish, with the close pinned in
the bottom decile of the five-week range. The Kaufman efficiency read is
Trending Down --- Strong (−0.52), confirming the down-regime rather than
contradicting it. Directional conviction from the strategy engine is
SHORT (score −0.77). The single most important watch item is **Thursday
2 July US non-farm payrolls** --- a hot print hardens the
hawkish-Fed/strong-dollar headwind, a soft print is the most credible
near-term catalyst for the oversold bounce already visible intraday on
30 June.

**§2 Market Definition**

  -----------------------------------------------------------------------
  **Field**              **Definition**
  ---------------------- ------------------------------------------------
  Asset                  S&P 500 cash index (large-cap US equity
                         benchmark, 503 constituents)

  Price basis            Cash index level (continuous), calculated during
                         NYSE/NASDAQ hours

  Delivery basis         Regular cash session 09:30--16:00 ET;
                         pre/after-market excluded from OHLC

  Unit / Currency        Index points · USD

  As-of date             30 June 2026 (America/New_York). Report date
                         overrides the populated instance date.

  Daily-open anchor      Overridden for this run to 00:00 UK (per
                         request). Standard cash anchor is the 07:00 UK
                         pre-NY-open window; the override is recorded in
                         the Agent Log (§20).

  Lookback window        5 sessions (execution block); 25 sessions
                         (regime block)
  -----------------------------------------------------------------------

*Note: 30 June is an in-progress session at run time. The validated
completed-session block ends Friday 26 June 2026; all OHLC, pivot, and
regime mathematics are computed on completed sessions only, per the
no-synthesis rule.*

**§3 Consensus Price Call**

  ---------------------------------------------------------------------------
  **Consensus**   **Range**       **Basis**    **Confidence**   **Tone**
  --------------- --------------- ------------ ---------------- -------------
  **7,354 pts**   7,331 -- 7,372  Cash close   High             **Bearish**
                                  26 Jun                        

  ---------------------------------------------------------------------------

Rationale: the 26 June official close of 7,354.02 is corroborated across
multiple independent feeds with zero material delta and sits inside a
tight 41-point final-session range, making it the most defensible
anchor. The wider 7,331--7,372 band reflects the 26 June intraday
high/low. The in-progress 30 June rally (index quoted near 7,436, +1.1%)
is a counter-trend bounce off oversold and is treated as live, not
validated, data.

**§4 Price Evidence Table**

  ----------------------------------------------------------------------------------------
  **Source**   **Date/Time**   **Raw          **Normalized**   **Basis**   **Relevance**
                               (close)**                                   
  ------------ --------------- -------------- ---------------- ----------- ---------------
  S&P Dow      26 Jun 17:02 CT 7,354.02       7,354.02         Cash close  Core
  Jones / FRED                                                             

  CNBC market  26 Jun close    7,354.02       7,354.02         Cash close  Core
  wrap                                                                     

  TheStreet    26 Jun close    7,354.02       7,354.02         Cash close  Core
  live blog                                                                

  Bloomberg TV 26 Jun close    ≈7,354         7,354.02         Cash close  Directional
  (The Close)                                                              

  CME ES       26 Jun          basis-linked   ---              Futures     Confirmation
  futures                                                                  only
  (ESM26)                                                                  

  Yahoo        26 Jun delayed  7,354.02       7,354.02         Cash close  Directional
  Finance                                                                  
  (web)                                                                    
  ----------------------------------------------------------------------------------------

*Six independent observations. Closes corroborate to the cent; intraday
high/low for the prior five sessions are reconstructed from session
reporting and carry a single-source-indicative flag where a second
independent intraday feed could not be confirmed (see §19).*

**§5 Consensus Build Explanation**

All observations are already on the same specification (cash index, USD,
index points, regular-session close), so no FX, freight, or grade
normalization is required. The weighted-median method down-weights the
delayed Yahoo web quote and the basis-linked futures print, both flagged
confirmation-only. The official S&P DJI / FRED value and the two
real-time market desks (CNBC, TheStreet) agree to the cent and carry the
highest weight. The 26 June close of 7,354.02 is therefore adopted as
the consensus; the range is set by that session\'s own high/low rather
than cross-source dispersion, which is immaterial here.

**§6 Validated OHLC + RSI2 Table (5-Day)**

  ---------------------------------------------------------------------------------------------------------------
  **Date**   **Open**   **High**   **Low**   **Close**      **RSI2**   **Trend**   **Sources**   **Validation**
  ---------- ---------- ---------- --------- -------------- ---------- ----------- ------------- ----------------
  22 Jun     7,474      7,486      7,420     **7,448.30**   0          Bearish     S&P DJI ×     CORROBORATED
                                                                                   CNBC          (close Δ0.00)

  23 Jun     7,447      7,458      7,350     **7,365.46**   0          Bearish     S&P DJI ×     CORROBORATED
                                                                                   CNBC          (close Δ0.00)

  24 Jun     7,370      7,405      7,352     **7,358.22**   0          Bearish     S&P DJI ×     CORROBORATED
                                                                                   TheStreet     (close Δ0.00)

  25 Jun     7,361      7,411      7,351     **7,357.49**   0          Bearish     S&P DJI ×     CORROBORATED
                                                                                   CNBC          (close Δ0.00)

  26 Jun     7,355      7,372      7,331     **7,354.02**   0          Neutral     S&P DJI ×     CORROBORATED
                                                                                   FRED          (close Δ0.00)
  ---------------------------------------------------------------------------------------------------------------

*RSI2 fixed at period 2, computed from the validated close sequence.
With closes declining monotonically across the block, mean gain is zero
and RSI2 prints 0 (deeply oversold) --- a legitimate, not a missing,
value. Intraday High/Low are single-source-indicative; they are used for
chart context and regime mathematics but the §11 pivot inputs are
flagged accordingly (see §19). 26 Jun is Neutral by rule: Close \< Open
is marginal and RSI2 is not \> 50.*

**§7 Charts**

Chart 1 --- 5-Day Candlestick

![](media/05644053d0392d2eba9f5ed7a957f866e3023049.png){width="6.25in"
height="3.3333333333333335in"}

Chart 2 --- Distance from Open

![](media/612af8e497251b936d57e00b70f4ae86fd60df3e.png){width="6.25in"
height="3.3333333333333335in"}

Chart 3 --- 25-Session Structure

![](media/bbb9db02561c1caed131a80719b17d5ed078c4c8.png){width="6.25in"
height="3.3333333333333335in"}

Chart 4 --- Comparative Volatility (VOLator)

![](media/5c1a4d735e83c9efe606b9cea6701382c52b16e4.png){width="6.25in"
height="3.46875in"}

*Counter volatility series (VIX, USDX, DAX) are scaled illustratively to
show co-movement of the risk regime; the S&P 500 series is computed from
validated OHLC. VIX tracks the index vol expansion; USDX runs inverse
(risk-off dollar bid).*

Chart 5 --- Pivot Structure (Weekly Candles)

![](media/404cdebcc35fec887d45c83a111ceda9bf0f65c3.png){width="6.0in"
height="4.333333333333333in"}

**§8 Short-Term Technical Analysis**

**22 Jun** A bearish marubozu-like body (close near the lows, close
location ≈ 43% of range), RSI2 at 0. Semiconductor weakness on a BofA
rate-hike note set a one-way tone (see §6).

**23 Jun** The decisive session: a wide-range bearish candle, close
location ≈ 14%, −1.44%. The Asian memory-chip rout carried into NY; this
is the impulse leg of the down-move.

**24 Jun** Inside-ish range with a long upper wick rejected from 7,405;
close ≈ 12% of range. Intraday volatility surged ahead of Micron
earnings --- supply pressure persists despite the small headline change.

**25 Jun** Doji-adjacent body, close ≈ 11% of range, RSI2 0. Micron\'s
beat could not lift the index as Apple (−6%) and Microsoft (−3%) dragged
the megacaps.

**26 Jun** Compression: a narrow 41-point range, near-flat close
(−0.05%), close location ≈ 66%. The down-impulse has flattened into a
doji --- the first sign of seller exhaustion at the lows.

**Sequence assessment:** Continuation flattening to Compression.
Sessions 22--24 Jun are a clean directional progression (low overlap,
closes traveling one way); 25--26 Jun show range contraction and a doji
at the lows. Evidence: overlap ratio rose into the final two sessions
while the range collapsed from 108 points (23 Jun) to 41 points (26
Jun).

**Nearest support / resistance:** support 7,331 (26 Jun low, also the
5-day swing low); resistance 7,411--7,486 (25 Jun high up to the 5-day
swing high).

**Judgement label: Bearish continuation** --- with explicit
reversal-risk noted from the 26 Jun compression doji. Consistent with
the §9 Trending--Bearish regime.

**§9 Medium-Term Regime & VOLator**

**Regime classification: Trending --- Bearish.** Supporting metrics:
overlap ratio 0.63, directional persistence 0.79, range-position bias
0.10 (bottom decile of the 25-session range), VOLator slope positive
(+0.24, volatility expanding), median RSI2 across the block in the 0--40
band. The high overlap reflects the late-block compression, but
persistence and range position confirm a decisive directional down-leg
from the 17 June peak (7,570) into the 7,331--7,354 zone.

**Bias:** Bearish.

**VOLator current readings:** S&P 500 scaled volatility ≈ +1.0 (top of
its own range, expanding). VIX elevated near 18.4 (above the
\'elevated\' 20 watch line is not yet breached but it is rising); USDX
volatility moderate and inverse; DAX volatility expanding in sympathy.
Every active counter sits above or at its midpoint.

**Preferred trade protocol:** High-conviction trend continuation ---
pullback entries in the trend (short) direction. Short-term (§8) and
medium-term reads agree, so no conflict flag.

**Kaufman confirmation:** KER −0.52, Trending Down --- Strong. Agrees
with the regime synthesis and raises confidence. No contradiction to
resolve.

**§10 Cross-Asset Analysis**

  ---------------------------------------------------------------------------------
  **Counter**   **5-day dir**  **Mechanism**        **Status**   **Implication**
  ------------- -------------- -------------------- ------------ ------------------
  USDX          Rising         A stronger dollar    Confirms     Headwind;
                               (13-mo highs                      consistent with
                               \~101.3) tightens                 bearish bias
                               global financial                  
                               conditions and                    
                               translates                        
                               multinational                     
                               earnings lower.                   

  VIX           Rising         Implied-vol          Confirms     Risk regime
                               expansion signals                 negative for the
                               demand for downside               index
                               protection /                      
                               risk-off                          
                               positioning.                      

  DAX 40        Falling/Flat   Common global-risk   Confirms     Broad risk-off,
                               factor; European                  not
                               equity confirms or                US-idiosyncratic
                               contradicts the US                
                               risk read.                        
  ---------------------------------------------------------------------------------

**Aggregate cross-asset confirmation: CONFIRM** --- all three active
counters align with the Trending--Bearish synthesis; none contradicts.
No contradiction flag is raised.

**§11 Floor Pivot Analysis**

Daily (from 26 Jun H/L/C)

  -----------------------------------------------------------------------
  **Level**               **Price**               **Level / Price**
  ----------------------- ----------------------- -----------------------
  R5                      7,496.7                 S1 7,332.7

  R4                      7,455.7                 S2 7,311.3

  R3                      7,414.7                 S3 7,291.7

  R2                      7,393.3                 S4 7,250.7

  R1                      7,373.7                 S5 7,209.7

  **P**                   **7,352.3**             ---
  -----------------------------------------------------------------------

Weekly (from W/E 26 Jun H/L/C)

  -----------------------------------------------------------------------
  **Level**               **Price**               **Level / Price**
  ----------------------- ----------------------- -----------------------
  R3                      7,604.7                 S1 7,294.7

  R2                      7,545.3                 S2 7,235.3

  R1                      7,449.7                 S3 7,139.7

  **P**                   **7,390.3**             ---
  -----------------------------------------------------------------------

Monthly (June block H/L/C proxy)

  -----------------------------------------------------------------------
  **Level**               **Price**               **Level / Price**
  ----------------------- ----------------------- -----------------------
  R2                      7,657.3                 S1 7,266.7

  R1                      7,505.7                 S2 7,179.3

  **P**                   **7,418.3**             S3 7,027.7
  -----------------------------------------------------------------------

**Source status:** prior-period H/L/C closes are corroborated; intraday
H/L feeding the pivots are single-source-indicative (see §19). All pivot
levels therefore carry the indicative qualifier and are propagated to
the §21 strategy suppression logic.

**Position narrative:** the 26 June close (7,354.02) sits almost exactly
on the daily pivot P (7,352.3) and just below the weekly P (7,390.3) and
monthly P (7,418.3) --- a clean stack of pivots overhead, all
bearish-confirming. First support is daily S1 7,332.7 (≈ the 5-day swing
low 7,331); first resistance is daily R1 7,373.7. No sub-0.05%
three-timeframe confluence zone is present.

**§12 Key Market Considerations**

**Demand / Earnings:** Q2 2026 S&P earnings growth tracking \~23% with a
bottom-up target well above spot, but megacap leadership is fracturing
(Apple, Microsoft hardware price hikes; OpenAI IPO-delay chatter).
Structural support, cyclical drag.

*Direction: Neutral-to-negative (cyclical)*

**Supply / Positioning:** Quarter-end rebalancing by pensions and
sovereign funds amplified the tech selloff; breadth narrowed as
defensives and small caps absorbed flows.

*Direction: Price-negative (cyclical)*

**Substitution / Spreads:** Rotation away from the S&P\'s tech-heavy
weighting toward the Dow (industrials, healthcare) and Russell 2000; the
index underperformed its peers on the week (−2%).

*Direction: Price-negative for the cap-weighted index (cyclical)*

**Policy / Rates:** Hawkish Fed under Chair Warsh; markets price \~three
hikes in 2026, first move odds \~60% by September; PCE 4.1% sticky.
Higher-for-longer compresses equity multiples.

*Direction: Price-negative (structural)*

**Macro / FX:** Dollar at 13-month highs (\~101.3) is a translation
headwind for the index\'s 28% foreign revenue base; 10-year yield easing
toward 4.4% on the oil drop is a modest offset.

*Direction: Net price-negative (cyclical)*

**Near-term catalysts:** Thursday 2 July non-farm payrolls is the
dominant event within the horizon; Nike earnings; ongoing US-Iran /
Strait of Hormuz headlines driving oil and risk sentiment.

*Direction: Two-way risk (cyclical)*

**§13 Sentiment, News & Calendar**

§13a Per-Article Sentiment

  ----------------------------------------------------------------------------------------
  **Source**   **Date**   **Headline      **Class.**      **Sentiment**   **Derivation
                          (abridged)**                                    quote (≤15w)**
  ------------ ---------- --------------- --------------- --------------- ----------------
  CNBC         26 Jun     Nasdaq posts    Media           Bearish         "rotated out of
                          fifth losing                                    key technology
                          session as chip                                 stocks into more
                          stocks tumble                                   defensive areas"

  TheStreet    26 Jun     Nasdaq, S&P     Media           Bearish         "stocks were
                          tread water                                     lower amid a
                          amid tech                                       global tech
                          sell-off,                                       sell-off"
                          OpenAI IPO                                      
                          delay                                           

  Schwab       26 Jun     Stocks rebound  Media           Mixed           "S&P 500 is just
                          early, awaiting                                 3% off all-time
                          fresh jobs data                                 highs"

  Goldman (via 26 Jun     'Still in       Institutional   Bullish         "general trend
  CNBC)                   buy-dip mode'                                   for this market
                          --- Flood                                       is higher, dips
                                                                          present
                                                                          opportunities"

  BofA Global  25 Jun     Constructive on Institutional   Bullish         "reinforcing our
  Research                memory\'s role                                  constructive
                          in AI (Micron)                                  view on
                                                                          memory\'s role
                                                                          in AI"

  Bloomberg    26 Jun     S&P halts       Media           Mixed           "halts four-day
                          four-day drop                                   drop ... jittery
                          to end jittery                                  week"
                          week                                            
  ----------------------------------------------------------------------------------------

§13b Aggregate Sentiment Summary

Counts: 2 Bullish (institutional), 2 Bearish (media), 2 Mixed (media).
Categorical label: **Mixed-to-Bearish.** Numeric tilt
(source-class-weighted): **−0.30**. The two institutional
\'buy-the-dip\' notes carry full weight but are outweighed by the
media-level bearish tape plus the structural hawkish-Fed read; the mixed
articles net to zero.

**Divergence flag:** price action (falling) agrees with the aggregate
bearish media tilt; the institutional buy-the-dip view diverges from
price. Given the Trending--Bearish regime (§9), price/tape is the more
reliable near-term signal --- the institutional view is a swing-horizon
call. Categorical label and tilt agree in sign.

§13c News Calendar --- Previous Period (22--26 Jun)

  ------------------------------------------------------------------------------
  **Date**   **Event**        **Prior /         **Impact**   **Implication for
                              Context**                      S&P 500**
  ---------- ---------------- ----------------- ------------ -------------------
  Tue 23 Jun Asian            Semis lead;       High         Index −1.44%;
             memory-chip rout Micron −13%                    impulse leg of the
             / BofA rate-hike                                down-move
             note                                            

  Wed 24 Jun Micron earnings  Rev \$41.5bn, EPS High         Intraday vol surge;
             (after close)    \$25.11 beat                   failed to lift
                                                             index next day

  Thu 25 Jun May PCE          PCE 4.1% headline High         Megacaps dragged;
             (in-line);                                      S&P −0.01%, Dow to
             Apple/MSFT price                                record
             hikes                                           

  Fri 26 Jun OpenAI IPO-delay NYT sourcing      Medium       Global tech
             report;                                         selloff; S&P
             quarter-end                                     −0.05%, −2% on week
             rebalance                                       
  ------------------------------------------------------------------------------

§13d News Calendar --- Upcoming Period (next 5 sessions)

  ------------------------------------------------------------------------------
  **Date**   **Event**        **Context**       **Impact**   **Implication (beat
                                                             / miss)**
  ---------- ---------------- ----------------- ------------ -------------------
  Tue 30 Jun Quarter /        S&P −2% for June  Medium       Rebalancing flows
             month-end close                                 two-way; oversold
                                                             bounce live
                                                             intraday

  Tue 30 Jun Nike earnings    Consumer          Medium       Read on
                              bellwether                     discretionary
                                                             demand

  Thu 2 Jul  US Non-Farm      Hawkish-Fed       High         Beat → harder
             Payrolls         backdrop                       dollar/rates,
                                                             bearish; miss →
                                                             rate-hike
                                                             repricing, bullish
                                                             bounce

  Thu 2 Jul  ISM / jobless    Pre-holiday       Medium       Confirms or offsets
             claims                                          the NFP read
  ------------------------------------------------------------------------------

**Highest-impact upcoming event: Thursday 2 July Non-Farm Payrolls** ---
a hot print reinforces the hawkish-Fed/strong-dollar headwind and
extends the down-regime, while a soft print is the single most credible
trigger to convert the 30 June oversold bounce into a genuine reversal.

**§14 Macro Context**

-   **Rates & policy:** hawkish Fed (Chair Warsh); \~three 2026 hikes
    priced, first-move odds \~60% by September. Cross-references the
    rising VIX read in §10 --- both risk-negative for the index.

-   **Inflation:** May PCE 4.1% headline, sticky and above target.
    Price-negative (multiple compression).

-   **Safe-haven / real yields:** 10-year yield easing toward 4.4% as
    oil fell is a modest offset, but real yields remain elevated under
    the hawkish stance --- net neutral-to-negative.

-   **Liquidity & FX:** USDX rising to 13-month highs (§10) tightens
    conditions and translates the index\'s 28% foreign revenue lower.
    Price-negative.

-   **Energy:** WTI/Brent fell sharply (Brent −4.3% on 24 Jun) on
    US-Iran de-escalation hopes; lower oil eases the inflation impulse
    but signals demand concern --- mixed for equities.

-   **Positioning:** quarter-end rebalancing, narrow breadth, VIX \~18.4
    and rising. Watch item from §13d: a hot NFP would push the dollar
    and yields higher and pressure the index further.

**§15 Bull / Bear Balance**

+-----------------------------------+-----------------------------------+
| **Upside risks**                  | **Downside risks**                |
+===================================+===================================+
| Oversold mean-reversion: RSI2     | Trend continuation from a         |
| pinned at 0, 26 Jun compression   | confirmed Trending--Bearish       |
| doji at the 5-day swing low       | regime (KER −0.52); close pinned  |
| (7,331) --- the 30 Jun intraday   | in the bottom decile of the       |
| rally (+1.1%) is already          | 25-day range.                     |
| expressing this.                  |                                   |
|                                   | Hawkish Fed + 13-month-high       |
| Soft 2 Jul NFP repricing Fed-hike | dollar (§14) as a persistent      |
| odds lower (the §13d              | multiple-compression headwind.    |
| highest-impact event).            |                                   |
|                                   | Narrow breadth / megacap          |
| Institutional \'buy-the-dip\'     | leadership fracturing (Apple,     |
| flows (Goldman, BofA) plus index  | Microsoft, OpenAI-IPO overhang).  |
| only \~3% off all-time highs.     |                                   |
|                                   | A break of 7,331 swing-low/S1     |
| Pivot reclaim: a daily close back | opens daily S2 7,311 then weekly  |
| above weekly P 7,390 would        | S1 7,295.                         |
| neutralise the bearish stack.     |                                   |
+-----------------------------------+-----------------------------------+

**§16 Forward View**

Expected direction over the next five sessions: **lower-to-sideways with
elevated two-way risk.** The dominant Trending--Bearish regime favours
rallies being sold toward the 7,373 (daily R1) -- 7,390 (weekly P) band.
Expected trading range 7,295--7,420. Base case is a retest of 7,331
swing-low support; a daily close below 7,311 (daily S2) confirms
continuation toward weekly S1 7,295.

*This view respects the §9 technical regime.* It is flagged, however,
that the in-progress 30 June session is rallying hard intraday (\~+1.1%)
--- a counter-trend oversold bounce. The base case is invalidated to the
upside on a daily close back above weekly P 7,390, which would turn the
bearish pivot stack and argue for a swing back toward 7,449 (weekly R1).
The 2 July payrolls print is the most likely arbiter.

**§17 Forecast**

**Forecast:** *The S&P 500 is biased lower toward 7,331 then 7,311 over
the coming sessions as the Trending--Bearish regime, hawkish-Fed dollar
strength, and bearish cross-asset confirmation outweigh an oversold
bounce that requires a soft payrolls print to sustain.*

**§18 Final Analyst Judgement**

**Consensus price call:** 7,354 index points, bearish tone, High
confidence.

**Three most important reasons:** (1) a confirmed Trending--Bearish
regime across both the 5-day and 25-session windows with KER −0.52
corroboration; (2) a hawkish Fed and 13-month-high dollar imposing a
structural multiple-compression headwind; (3) unanimous bearish
cross-asset confirmation (USDX up, VIX up, DAX soft).

**Single watch item:** Thursday 2 July US Non-Farm Payrolls.

**§19 Source Discipline Note**

-   Live vs indicative: session closes for 22--26 Jun are CORROBORATED
    (two independent sources, zero delta). Intraday High/Low for those
    sessions are SINGLE-SOURCE --- indicative only; they are used for
    chart context and regime mathematics but not as definitive
    settlement references.

-   Pivot inputs: because the prior-period intraday H/L are
    single-source-indicative, all daily/weekly/monthly pivot levels
    carry the indicative qualifier and are flagged to the §21 strategy
    logic.

-   Per the run instruction, strategy recommendations are NOT suppressed
    on corroboration grounds; the indicative status is disclosed on
    every affected trade card instead (corroboration leniency applied
    --- see §20).

-   The 30 June in-progress quote (\~7,436) is live, not validated, and
    is excluded from all OHLC, pivot, and regime calculations.

-   Corroboration status by instrument: S&P 500 close CORROBORATED;
    USDX, VIX, DAX directional reads sourced from market data feeds for
    cross-asset context only.

**§20 Agent Log**

-   Run configuration overrides: as-of/report date set to 30 June 2026
    (instance default 29 April 2026 overridden per request); daily-open
    anchor overridden to 00:00 UK (instance default 07:00 UK) per
    request --- recorded here as required.

-   Sources attempted for S&P 500 close: S&P DJI/FRED, CNBC, TheStreet,
    Bloomberg, Yahoo (web), CME ES (confirmation). Corroborated pair:
    S&P DJI × CNBC, delta 0.00 pts, tolerance ±0.10 pts. Intraday H/L:
    single-source for the five-session block --- logged by session date
    in §19.

-   Direction-score weights basis: DEFAULTS (0.25 / 0.20 / 0.10 / 0.15 /
    0.15 / 0.15), unchanged; within the 20-session weight-lock window.
    No tuning applied.

-   Direction score −0.77 → SHORT. Contributing signals: short-term
    technical bias −1×0.25, medium-term regime −1×0.20, cross-asset
    CONFIRM −1×0.15, sentiment tilt −0.30×0.15, Kaufman −0.52×0.15,
    VOLator −0.5×0.10.

-   Sentiment tilt provenance: M-stage §13b primary-asset value −0.30,
    computed on six articles (above the three-article low-confidence
    threshold). Source-class weighting applied (institutional 1.0, media
    0.5).

-   Regime label TREND_DOWN: Step-4 synthesis Trending Bearish /
    Trending Bearish, KER Trending Down --- Strong, VOLator slope
    positive --- mapped to TREND_DOWN (not RANGE; dual-gate not
    engaged).

-   Backtest reconstruction: 5 sessions replayed at each t−1 close;
    sentiment frozen at t−1; no forward leakage. Notes in §21c.

-   Corroboration-leniency directive applied: strategy cards produced
    despite single-source-indicative pivots; indicative caveat surfaced
    on each card rather than suppressing Trade 2.

**§21 Strategy Recommendations**

§21a Directional Conviction

Direction: **SHORT** · Score: **−0.77**. The three highest-weighted
contributing signals are short-term technical bias (§8) −0.25,
medium-term regime (§9) −0.20, and cross-asset confirmation (§10) −0.15,
with sentiment tilt (§13b) and Kaufman/VOLator reinforcing. Weights
basis: defaults. No conflict with the §17 forecast --- both are bearish.
The only caveat is the live 30 June oversold bounce, surfaced on each
card.

§21b Trade Cards

**Trade 1 --- Daily Directional**

  -----------------------------------------------------------------------
  **Field**           **Detail**
  ------------------- ---------------------------------------------------
  **Type /            Trade 1 --- Daily Directional · SHORT ---
  Direction**         TREND_DOWN regime

  **Entry**           Market at 00:00 UK anchor (overridden), reference
                      7,354 pts

  **Stop loss**       7,500 pts --- 146 pts above entry. Anchor: 5-day
                      swing high 7,486 + 0.25×ATR. (Structural stop is
                      tighter than the 3.5×ATR cap of 196 pts, so the
                      structural anchor applies.)

  **Risk (R)**        146 pts (146 points)

  **TP1 (Unit 1)**    7,208 pts --- +1R

  **TP2 (Unit 2)**    7,062 pts --- +2R. On fill, Unit 3 SL → entry +0.2R
                      (7,325).

  **TP3 (Unit 3       Time-stop at session close, or 3×ATR (7,186 pts),
  runner)**           whichever first

  **Tranche mgmt**    3 equal units; U1→TP1, U2→TP2; on U2 fill U3
                      SL→entry−0.2R

  **Confluences**     SL at 5-day swing high (swing); entry at daily P
                      7,352 (pivot) --- entry sits on P

  **Thesis            Daily close back above weekly P 7,390
  invalidation**      

  **Caveats**         Wide stop (1R \> 1×ATR); TP2 ambitious for a daily
                      horizon; single-source-indicative pivots; holding
                      period collides with 2 Jul NFP; live
                      oversold-bounce risk
  -----------------------------------------------------------------------

**Trade 2 --- Pivot (regime-aware, TREND_DOWN)**

  -----------------------------------------------------------------------
  **Field**           **Detail**
  ------------------- ---------------------------------------------------
  **Type /            Trade 2 --- Pivot breakout (TREND) · SHORT below
  Direction**         pivot

  **Entry**           Sell stop/limit at 7,350 pts --- P − 10% of (P −
                      S1), on the downside

  **Stop loss**       7,369 pts --- P + 0.8×(R1 − P); 19 pts above entry

  **Risk (R)**        19 pts (19 points)

  **TP1 / TP2 / TP3** S1 7,333 / S1.5 7,322 / S2 7,311 (runner toward
                      weekly S1 7,295)

  **Tranche mgmt**    3 equal units; U1→S1, U2→S1.5; on U2 fill U3
                      SL→entry−0.2R

  **Confluences**     S1 7,333 ≈ 5-day swing low 7,331 (swing + pivot) →
                      strong confluence at TP1

  **Thesis            Daily close back through daily P 7,352
  invalidation**      

  **Caveats**         Single-source-indicative pivots (corroboration
                      leniency applied --- not suppressed); tight stop; 2
                      Jul NFP collision
  -----------------------------------------------------------------------

**Trade 3A --- Momentum-Pullback (TREND_DOWN)**

  -----------------------------------------------------------------------
  **Field**           **Detail**
  ------------------- ---------------------------------------------------
  **Type /            Trade 3 --- Momentum-Pullback (3A) · SHORT
  Direction**         

  **Fib anchor**      Down-swing 7,486 → 7,331 (width 155 pts), most
                      recent qualifying swing (≥2×ATR)

  **Entry**           7,420 pts --- 57.5% retracement of the down-swing
                      (sell the pullback)

  **Stop loss**       7,500 pts --- beyond the 0% anchor (swing high)
                      +0.25×ATR; 80 pts (within 3.5×ATR cap)

  **Risk (R)**        80 pts (80 points)

  **TP1 (Unit 1)**    7,390 pts --- 38.2% retracement (shallow target)

  **TP2 (Unit 2)**    7,331 pts --- 0% / swing low. On fill, U3 SL →
                      entry +0.2R

  **TP3 (Unit 3       100%+ extension (7,176 = swing low − 1×width);
  runner)**           structural runner-stop pull to the 50% mark on a
                      100%-extension print

  **Tranche mgmt**    3 equal units; structural runner override on
                      100%-extension break

  **Confluences**     TP1 7,390 ≈ weekly P (pivot); entry 7,420 near
                      monthly P 7,418 (pivot) → strong confluence at
                      entry

  **Thesis            Daily close above the swing-high anchor 7,486
  invalidation**      

  **Caveats**         Entry requires a pullback that may not arrive if
                      7,331 breaks first; single-source-indicative
                      pivots; 2 Jul NFP collision
  -----------------------------------------------------------------------

§21c 5-Session No-Leakage Backtest

  -----------------------------------------------------------------------------------------------
  **Date     **Strategy**   **Direction**   **Triggered**   **Entry /      **Outcome   **Days**
  (t−N)**                                                   Exit**         (R)**       
  ---------- -------------- --------------- --------------- -------------- ----------- ----------
  Mon 22 Jun Trade 1        SHORT           YES             7,474 / 7,448  +0.18R      1
  (t−5)                                                                                

  Mon 22 Jun Trade 3A       SHORT           NO              limit 7,460    ---         ---
  (t−5)                                                     not hit                    

  Tue 23 Jun Trade 1        SHORT           YES             7,447 / 7,365  +0.56R      1
  (t−4)                                                                                

  Tue 23 Jun Trade 2        SHORT           YES             pivot / S2     +1.0R       1
  (t−4)                                                                                

  Wed 24 Jun Trade 1        SHORT           YES             7,370 / 7,358  +0.21R      1
  (t−3)                                                                                

  Thu 25 Jun Trade 1        SHORT           YES             7,361 / 7,357  +0.07R      1
  (t−2)                                                                                

  Thu 25 Jun Trade 3A       SHORT           NO              pullback not   ---         ---
  (t−2)                                                     reached                    

  Fri 26 Jun Trade 1        SHORT           YES             7,355 / 7,354  +0.02R      1
  (t−1)                                                                                

  Fri 26 Jun Trade 2        SHORT           NO              S-tier limits  ---         ---
  (t−1)                                                     not hit                    
  -----------------------------------------------------------------------------------------------

*Reconstructed at each t−1 close with sentiment, ATR, swings, pivots and
regime frozen at t−1; no forward leakage. SL-first tick-priority applied
where both could fill. Slippage = 0.*

§21d What Is Working

Trade 1 (Daily Directional) over the last 5 sessions: triggered 5/5
times, mean R = +0.21, with the 23 Jun impulse session the standout
(+0.56R). Trade 2 (Pivot) triggered 1/2, mean R = +1.0 on its single
fill. Trade 3A (Momentum-Pullback) triggered 0/2 --- the trend ran
without offering the 57.5% pullback. **Strongest performer: Trade 2
(pivot short) by mean R;** weakest: Trade 3A (insufficient triggers to
rank). The short bias has been consistently rewarded as the down-regime
persisted.

***Limitations:** Five-session windows are too small to support
statistical claims. The backtest cannot model intraday tick-level fills,
slippage, or commission. Treat as a directional sanity-check, not a
strategy-validation framework.*
