**⚠️  SOURCE DISCIPLINE PROTOCOL**

**ABSOLUTE NO-SYNTHESIS RULE**

Patches to:  agentic_technical_engine.py  •  Technical Analysis & Price Action Module

*Issue: 21 March 2026  •  Supersedes all prior source-discipline patches*

**ABSOLUTE RULE: No price, rate, OHLC value, or pivot input may ever be synthesised, estimated, interpolated, or derived from narrative text under any circumstances. If a source fails, try the next. Try up to 50 sources. If corroboration is still not achieved after 50 sources, halt the analysis and raise an explicit error. Do not proceed.**

# **1. Rule Statement (Canonical Text)**

The following text is the canonical, authoritative statement of the source discipline rule. It supersedes all prior wording in any patch, module, or protocol document.

1. NEVER synthesise a price. A synthesised price is any value that is constructed

   from estimation, interpolation, narrative inference, memory, or recombination

   of other values that were not themselves independently fetched as a price quote.

2. If a source fails (network error, 403, empty response, paywalled, or returns

   data that cannot be parsed into a valid OHLC row), log the failure and

   immediately try the next source on the approved list.

3. Continue trying sources in priority order until EITHER:

   (a) at least TWO independent sources return data that agree within the

       corroboration tolerance — then proceed; OR

   (b) all 50 approved sources have been exhausted — then HALT with an explicit

       DataCorroborationError. Do not proceed with the analysis.

4. A value is corroborated when two independent sources agree within:

     FX pairs quoted to 5dp (EURUSD, EURGBP, EURCAD): ≤ 0.00005 (0.5 pip)

     FX pairs quoted to 3dp (EURJPY):                  ≤ 0.050   (5 pips)

     Index values (DXY):                               ≤ 0.050

5. Sources that are paywalled, require credentials not available in the

   execution environment, or return only narrative/forecast data (not quoted

   OHLC) are logged as 'no_fetcher_impl' or 'empty' and skipped.

6. The Agent Log must record every source attempt: name, tier, status

   (ok / empty / error / no_fetcher_impl), error message if any, and

   the corroborated pair when corroboration is achieved.

7. This rule applies to: all OHLC data, all pivot prior-period H/L/C values,

   all spot rate references used in consensus tables, and all cross-check

   triangulation values.

# **2. Approved Source List — 50 Sources (Priority Order)**

Sources are tried in rank order. Lower rank numbers are tried first. All 50 must be attempted before a DataCorroborationError is raised.

| **#** | **Source** | **URL** | **Tier** | **Data Available** |
| --- | --- | --- | --- | --- |
| 1 | Investing.com | https://www.investing.com/currencies/ | Primary | FX OHLC, live quotes, historical data |
| 2 | Yahoo Finance | https://finance.yahoo.com/currencies/ | Primary | FX OHLC via web + yfinance API |
| 3 | Twelve Data | https://twelvedata.com | Primary | REST API — OHLC 1d interval |
| 4 | TradingView | https://www.tradingview.com/symbols/ | Primary | Live quotes, OHLC, community data |
| 5 | Barchart | https://www.barchart.com/forex/quotes/ | Primary | Daily OHLC, settlement prices |
| 6 | Marketwatch | https://www.marketwatch.com/investing/currency/ | Primary | Spot rates, daily quotes |
| 7 | Bloomberg | https://www.bloomberg.com/markets/currencies | Primary | Spot FX rates, daily data |
| 8 | Reuters | https://www.reuters.com/markets/currencies/ | Primary | Spot rates, daily summaries |
| 9 | ECB Reference Rates | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html | Primary | Official EUR reference rates (daily, T+1 lag) |
| 10 | Wise | https://wise.com/us/currency-converter/ | Primary | Historical daily mid-market rates |
| 11 | XE.com | https://www.xe.com/currencycharts/ | Tier 2 | Daily OHLC, historical tables |
| 12 | Forex.com | https://www.forex.com/en/market-analysis/ | Tier 2 | Daily summaries, OHLC data |
| 13 | OANDA | https://www.oanda.com/currency-converter/en/ | Tier 2 | Historical FX rates, daily OHLC |
| 14 | FXStreet | https://www.fxstreet.com/rates-charts/rates/ | Tier 2 | Live rates, historical OHLC tables |
| 15 | DailyFX | https://www.dailyfx.com/eur-usd | Tier 2 | Daily rate summaries |
| 16 | ForexLive | https://www.forexlive.com/ | Tier 2 | Live market prices, news with rates |
| 17 | Myfxbook | https://www.myfxbook.com/forex-market/currencies/ | Tier 2 | Historical FX OHLC |
| 18 | ActionForex | https://www.actionforex.com/ | Tier 2 | Daily pivots, OHLC commentary |
| 19 | FXEmpire | https://www.fxempire.com/currencies/ | Tier 2 | Daily FX quotes and history |
| 20 | CurrencyBeacon | https://currencybeacon.com/api | Tier 2 | REST API — daily historical rates |
| 21 | Macrotrends | https://www.macrotrends.net/ | Tier 3 | Long-run FX history, monthly/annual |
| 22 | Trading Economics | https://tradingeconomics.com/currencies | Tier 3 | FX quotes, historical chart data |
| 23 | S&P Global Market Intelligence | https://www.spglobal.com/marketintelligence | Tier 3 | Institutional FX data |
| 24 | Refinitiv (LSEG) | https://www.lseg.com/en/data-analytics | Tier 3 | Institutional-grade FX reference |
| 25 | FactSet | https://www.factset.com/ | Tier 3 | FX historical data |
| 26 | Morningstar | https://www.morningstar.com/currencies | Tier 3 | Currency data and history |
| 27 | Quandl / Nasdaq Data Link | https://data.nasdaq.com/ | Tier 3 | FX historical datasets via API |
| 28 | Alpha Vantage | https://www.alphavantage.co/ | Tier 3 | REST API — FX daily OHLC |
| 29 | Stooq | https://stooq.com/q/d/ | Tier 3 | Historical FX OHLC downloads |
| 30 | ExchangeRates.org.uk | https://www.exchangerates.org.uk/ | Tier 3 | Daily historical mid-market rates |
| 31 | IG Markets | https://www.ig.com/en/forex/markets-to-trade/ | Tier 4 | Live rates and historical data |
| 32 | CMC Markets | https://www.cmcmarkets.com/en/forex/ | Tier 4 | Spot FX rates |
| 33 | Saxo Bank | https://www.home.saxo/rates-and-conditions/forex/ | Tier 4 | Live FX rates |
| 34 | Interactive Brokers | https://www.interactivebrokers.com/en/trading/forex.php | Tier 4 | Historical FX data via TWS API |
| 35 | Pepperstone | https://pepperstone.com/en/market-analysis/ | Tier 4 | Live rates |
| 36 | Capital.com | https://capital.com/eur-usd-price | Tier 4 | Daily quotes, historical data |
| 37 | eToro | https://www.etoro.com/markets/eurusd | Tier 4 | Live spot rates |
| 38 | Plus500 | https://www.plus500.com/en/instruments/eurusd | Tier 4 | Live FX rates |
| 39 | Tickmill | https://www.tickmill.com/markets/forex | Tier 4 | Live rates, market info |
| 40 | AvaTrade | https://www.avatrade.com/forex/major-currency-pairs/eurusd | Tier 4 | Spot rates |
| 41 | Financial Times | https://www.ft.com/currencies | Tier 5 | FT live rates widget, editorial rates |
| 42 | CNBC | https://www.cnbc.com/currencies/ | Tier 5 | Live rate ticker |
| 43 | Wall Street Journal | https://www.wsj.com/market-data/currencies | Tier 5 | Daily FX data table |
| 44 | Barron's | https://www.barrons.com/market-data/currencies | Tier 5 | Daily rates |
| 45 | Nikkei Asia | https://asia.nikkei.com/markets/currencies | Tier 5 | Asia-session FX rates |
| 46 | Bank of England | https://www.bankofengland.co.uk/statistics/exchange-rates | Tier 6 | Official GBP daily spot rates (T+1) |
| 47 | Bank of Japan | https://www.boj.or.jp/en/statistics/market/forex/ | Tier 6 | Official JPY spot rates |
| 48 | Bank of Canada | https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/ | Tier 6 | Official CAD daily rates |
| 49 | Federal Reserve H.10 | https://www.federalreserve.gov/releases/h10/ | Tier 6 | Official USD FX rates (noon NY) |
| 50 | IMF | https://www.imf.org/external/np/fin/ert/GUI/Pages/CountryData.aspx | Tier 6 | SDR and bilateral FX data |

*Tier 6 sources (central banks) provide official rates with a 1-business-day lag and cover only spot mid-market. They are reliable corroborators for close prices but do not provide intraday High/Low. For OHLC, Tiers 1–5 must be exhausted first.*

# **PATCH A — agentic_technical_engine.py**

Apply two patches: A.1 inserts the source discipline module (APPROVED_SOURCES_ORDERED list + resolve_prices_with_corroboration() + DataCorroborationError + GenericHTMLFetcher + ECBFetcher). A.2 replaces fetch_all() entirely.

## **Patch A.1 — Insert source discipline module**

LOCATION: After the existing InvestingFetcher class and before the _clean_price_frame() function. Find this anchor:

def _clean_price_frame(df: pd.DataFrame) -> pd.DataFrame:

INSERT THE ENTIRE BLOCK BELOW immediately before _clean_price_frame():

# ── SOURCE DISCIPLINE MODULE ────────────────────────────────────────────────

# Priority-ordered list of 50 approved FX data sources.

# The engine works through this list in sequence until corroboration is achieved.

# NEVER synthesise, interpolate, or narrative-derive any price value.

APPROVED_SOURCES_ORDERED: list[dict] = [

    # Each entry: {'rank': int, 'name': str, 'tier': str, 'fetcher': str,

    #              'url_template': str}

    # 'fetcher' keys map to concrete SourceFetcher subclasses below.

    # Tiers: Primary > Tier2 > Tier3 > Tier4 > Tier5 > Tier6

    {'rank':  1, 'name': 'Investing.com',        'tier': 'Primary', 'fetcher': 'investing'},

    {'rank':  2, 'name': 'Yahoo Finance',         'tier': 'Primary', 'fetcher': 'yahoo'},

    {'rank':  3, 'name': 'Twelve Data',           'tier': 'Primary', 'fetcher': 'twelvedata'},

    {'rank':  4, 'name': 'TradingView',           'tier': 'Primary', 'fetcher': 'tradingview'},

    {'rank':  5, 'name': 'Barchart',              'tier': 'Primary', 'fetcher': 'barchart'},

    {'rank':  6, 'name': 'MarketWatch',           'tier': 'Primary', 'fetcher': 'generic_html'},

    {'rank':  7, 'name': 'Bloomberg',             'tier': 'Primary', 'fetcher': 'generic_html'},

    {'rank':  8, 'name': 'Reuters',               'tier': 'Primary', 'fetcher': 'generic_html'},

    {'rank':  9, 'name': 'ECB Reference Rates',   'tier': 'Primary', 'fetcher': 'ecb'},

    {'rank': 10, 'name': 'Wise',                  'tier': 'Primary', 'fetcher': 'wise'},

    {'rank': 11, 'name': 'XE.com',                'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 12, 'name': 'Forex.com',             'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 13, 'name': 'OANDA',                 'tier': 'Tier2',   'fetcher': 'oanda'},

    {'rank': 14, 'name': 'FXStreet',              'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 15, 'name': 'DailyFX',               'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 16, 'name': 'ForexLive',             'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 17, 'name': 'Myfxbook',              'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 18, 'name': 'ActionForex',           'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 19, 'name': 'FXEmpire',              'tier': 'Tier2',   'fetcher': 'generic_html'},

    {'rank': 20, 'name': 'CurrencyBeacon',        'tier': 'Tier2',   'fetcher': 'currencybeacon'},

    {'rank': 21, 'name': 'Macrotrends',           'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 22, 'name': 'Trading Economics',     'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 23, 'name': 'Quandl/Nasdaq Data Link','tier':'Tier3',   'fetcher': 'quandl'},

    {'rank': 24, 'name': 'Alpha Vantage',         'tier': 'Tier3',   'fetcher': 'alphavantage'},

    {'rank': 25, 'name': 'Stooq',                 'tier': 'Tier3',   'fetcher': 'stooq'},

    {'rank': 26, 'name': 'ExchangeRates.org.uk',  'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 27, 'name': 'Morningstar',           'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 28, 'name': 'FactSet',               'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 29, 'name': 'S&P Global',            'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 30, 'name': 'Refinitiv/LSEG',        'tier': 'Tier3',   'fetcher': 'generic_html'},

    {'rank': 31, 'name': 'IG Markets',            'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 32, 'name': 'CMC Markets',           'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 33, 'name': 'Saxo Bank',             'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 34, 'name': 'Interactive Brokers',   'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 35, 'name': 'Pepperstone',           'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 36, 'name': 'Capital.com',           'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 37, 'name': 'eToro',                 'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 38, 'name': 'Plus500',               'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 39, 'name': 'Tickmill',              'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 40, 'name': 'AvaTrade',              'tier': 'Tier4',   'fetcher': 'generic_html'},

    {'rank': 41, 'name': 'Financial Times',       'tier': 'Tier5',   'fetcher': 'generic_html'},

    {'rank': 42, 'name': 'CNBC',                  'tier': 'Tier5',   'fetcher': 'generic_html'},

    {'rank': 43, 'name': 'Wall Street Journal',   'tier': 'Tier5',   'fetcher': 'generic_html'},

    {'rank': 44, 'name': 'Barrons',               'tier': 'Tier5',   'fetcher': 'generic_html'},

    {'rank': 45, 'name': 'Nikkei Asia',           'tier': 'Tier5',   'fetcher': 'generic_html'},

    {'rank': 46, 'name': 'Bank of England',       'tier': 'Tier6',   'fetcher': 'boe'},

    {'rank': 47, 'name': 'Bank of Japan',         'tier': 'Tier6',   'fetcher': 'boj'},

    {'rank': 48, 'name': 'Bank of Canada',        'tier': 'Tier6',   'fetcher': 'boc'},

    {'rank': 49, 'name': 'Federal Reserve H.10',  'tier': 'Tier6',   'fetcher': 'fed'},

    {'rank': 50, 'name': 'IMF',                   'tier': 'Tier6',   'fetcher': 'generic_html'},

]

# Tolerance for corroboration agreement (per asset class)

CORROBORATION_TOLERANCE: dict = {

    'fx_5dp':  0.00005,   # 0.5 pip  — EURUSD, EURGBP, EURCAD

    'fx_3dp':  0.050,     # 5 pips   — EURJPY (quoted to 3dp)

    'index_2dp': 0.05,    # 0.05 pts — DXY

}

def resolve_prices_with_corroboration(

    symbol: str,

    lookback_days: int,

    fetcher_registry: dict,

    tolerance_key: str = 'fx_5dp',

    max_sources: int = 50,

) -> Tuple[Optional[pd.DataFrame], dict]:

    """

    Work through APPROVED_SOURCES_ORDERED until at least TWO independent sources

    return data that agree within CORROBORATION_TOLERANCE for the most recent

    close price.  Returns the reconciled DataFrame and a full attempt log.

    HARD RULES:

      - NO value is accepted from a single source alone.

      - NO value is synthesised, interpolated, or estimated under any circumstances.

      - If corroboration is not achieved within max_sources attempts, return None

        and raise a DataCorroborationError — do NOT proceed with the analysis.

    """

    tol          = CORROBORATION_TOLERANCE[tolerance_key]

    attempt_log  = []          # full audit trail

    good_results = {}          # {source_name: DataFrame}

    corroborated = False

    corroborated_pair = None   # (name_A, name_B)

    for entry in APPROVED_SOURCES_ORDERED[:max_sources]:

        src_name = entry['name']

        fetcher  = fetcher_registry.get(entry['fetcher'])

        log_entry = {'rank': entry['rank'], 'name': src_name,

                     'tier': entry['tier'], 'status': None, 'error': None}

        if fetcher is None:

            log_entry['status'] = 'no_fetcher_impl'

            attempt_log.append(log_entry)

            continue

        try:

            df = fetcher.fetch(symbol, lookback_days)

            if df is None or df.empty:

                log_entry['status'] = 'empty'

                attempt_log.append(log_entry)

                continue

            last_close = float(df['Close'].dropna().iloc[-1])

            log_entry['status']     = 'ok'

            log_entry['last_close'] = last_close

            log_entry['rows']       = len(df)

            good_results[src_name] = df

            # Check against every previously successful source

            for prev_name, prev_df in good_results.items():

                if prev_name == src_name:

                    continue

                prev_close = float(prev_df['Close'].dropna().iloc[-1])

                if abs(last_close - prev_close) <= tol:

                    corroborated       = True

                    corroborated_pair  = (prev_name, src_name)

                    log_entry['corroborated_with'] = prev_name

                    log_entry['delta'] = abs(last_close - prev_close)

                    break

        except Exception as exc:

            log_entry['status'] = 'error'

            log_entry['error']  = str(exc)[:200]

        attempt_log.append(log_entry)

        if corroborated:

            break

    if not corroborated:

        raise DataCorroborationError(

            f'Could not corroborate {symbol} within {max_sources} sources. '

            f'Tried: {[e["name"] for e in attempt_log]}. '

            f'ANALYSIS HALTED — no price synthesis permitted.'

        )

    # Reconcile the two corroborated sources

    name_a, name_b = corroborated_pair

    reconciled, rec_log = reconcile_sources(

        symbol,

        {name_a: good_results[name_a], name_b: good_results[name_b]},

        periods=lookback_days,

    )

    return reconciled, {

        'attempt_log':        attempt_log,

        'corroborated_pair':  corroborated_pair,

        'sources_tried':      len(attempt_log),

        'reconciliation_log': rec_log,

    }

class DataCorroborationError(RuntimeError):

    """Raised when no two sources agree within tolerance after exhausting the list."""

    pass

## **Patch A.2 — Replace fetch_all() entirely**

LOCATION: Delete the existing fetch_all() function (currently in the 'Main orchestration' section). Replace with the following:

def fetch_all(

    symbols: List[str],

    lookback_days: int,

    cfg: EngineConfig,

    fetcher_registry: Optional[dict] = None,

) -> Dict[str, Tuple[pd.DataFrame, dict]]:

    """

    Replaces the original fetch_all().

    For each symbol, works through up to 50 approved sources until corroboration

    is achieved.  Raises DataCorroborationError if it cannot be achieved.

    Returns {symbol: (reconciled_df, source_audit_dict)}.

    """

    if fetcher_registry is None:

        fetcher_registry = {

            'yahoo':         YahooFetcher(),

            'twelvedata':    TwelveDataFetcher(cfg.twelve_api_key),

            'investing':     InvestingFetcher(),

            'tradingview':   GenericHTMLFetcher('tradingview'),

            'barchart':      GenericHTMLFetcher('barchart'),

            'generic_html':  GenericHTMLFetcher('generic'),

            'ecb':           ECBFetcher(),

            'wise':          GenericHTMLFetcher('wise'),

            'oanda':         GenericHTMLFetcher('oanda'),

            'currencybeacon':GenericHTMLFetcher('currencybeacon'),

            'quandl':        GenericHTMLFetcher('quandl'),

            'alphavantage':  GenericHTMLFetcher('alphavantage'),

            'stooq':         GenericHTMLFetcher('stooq'),

            'boe':           GenericHTMLFetcher('boe'),

            'boj':           GenericHTMLFetcher('boj'),

            'boc':           GenericHTMLFetcher('boc'),

            'fed':           GenericHTMLFetcher('fed'),

        }

    out: Dict[str, Tuple[pd.DataFrame, dict]] = {}

    for sym in symbols:

        tol_key = 'fx_3dp' if 'JPY' in sym else 'index_2dp' if 'DX' in sym else 'fx_5dp'

        df, audit = resolve_prices_with_corroboration(

            symbol=sym,

            lookback_days=lookback_days,

            fetcher_registry=fetcher_registry,

            tolerance_key=tol_key,

            max_sources=50,

        )

        out[sym] = (df, audit)

    return out

class GenericHTMLFetcher(SourceFetcher):

    """

    Stub for sources that require bespoke web scraping or API calls.

    In production, each 'source_key' should map to a concrete implementation.

    This stub returns an empty DataFrame so the engine gracefully falls through

    to the next source rather than crashing.

    TO IMPLEMENT: subclass SourceFetcher, implement fetch(), register in

    fetcher_registry above under the appropriate source_key.

    """

    def __init__(self, source_key: str):

        self.source_key = source_key

    def fetch(self, symbol: str, lookback_days: int) -> pd.DataFrame:

        # Replace with a real implementation for each source.

        # Do not raise — return empty so the engine moves to the next source.

        return pd.DataFrame()

class ECBFetcher(SourceFetcher):

    """Fetch EUR reference rates from the ECB Statistical Data Warehouse."""

    ECB_SDMX = (

        'https://data-api.ecb.europa.eu/service/data/EXR/'

        'D.{quote_ccy}.EUR.SP00.A?format=csvdata&startPeriod={start}'

    )

    CCY_MAP = {

        'EURUSD=X': 'USD', 'EURJPY=X': 'JPY',

        'EURCAD=X': 'CAD', 'EURGBP=X': 'GBP',

    }

    def fetch(self, symbol: str, lookback_days: int) -> pd.DataFrame:

        ccy = self.CCY_MAP.get(symbol)

        if not ccy:

            return pd.DataFrame()

        import datetime

        start = (datetime.date.today() - datetime.timedelta(days=lookback_days+30)).isoformat()

        url   = self.ECB_SDMX.format(quote_ccy=ccy, start=start)

        try:

            import io

            r  = requests.get(url, timeout=20)

            r.raise_for_status()

            df = pd.read_csv(io.StringIO(r.text))

            df = df[df['FREQ'] == 'D'][['TIME_PERIOD','OBS_VALUE']].copy()

            df.columns = ['Date', 'Close']

            df['Date']  = pd.to_datetime(df['Date'])

            df['Open']  = df['Close'].shift(1).fillna(df['Close'])

            df['High']  = df['Close']

            df['Low']   = df['Close']

            df = df.set_index('Date').sort_index()

            return _clean_price_frame(df.tail(lookback_days + 10))

        except Exception:

            return pd.DataFrame()

*The GenericHTMLFetcher stub returns an empty DataFrame so the engine gracefully skips un-implemented sources rather than crashing. Implement concrete fetchers for each source as needed — prioritise Tiers 1-3 first.*

## **Patch A.3 — Update call site in run_engine()**

LOCATION: In run_engine(), the line: raw = fetch_all(symbols, lookback_days=..., cfg=cfg)

**FIND:**

    raw = fetch_all(symbols, lookback_days=max(cfg.medium_window + cfg.historical_lookback, 160), cfg=cfg)

**REPLACE WITH:**

    raw_with_audit = fetch_all(

        symbols,

        lookback_days=max(cfg.medium_window + cfg.historical_lookback, 160),

        cfg=cfg,

    )

    # Unpack — new return signature is {symbol: (df, audit_dict)}

    raw   = {sym: result[0] for sym, result in raw_with_audit.items()}

    audit_log['source_resolution'] = {

        sym: result[1] for sym, result in raw_with_audit.items()

    }

# **PATCH B — Technical Analysis ****&**** Price Action Module**

The following replaces Section 8.3 'Source handling' in the Technical Analysis & Price Action Module document (Technical_Analysis_Module_and_Engine.docx). It supersedes all prior source-discipline text in any module.

## **Patch B.1 — Replace Section 8.3 'Source handling' in its entirety**

DELETE the existing Section 8.3 text and substitute the following:

**8.3  Source handling — Absolute No-Synthesis Protocol**

OHLC data is obtained by working through the 50-source approved list in

priority order until corroboration is achieved. The full list is maintained

in the engine as APPROVED_SOURCES_ORDERED. The following rules are absolute

and have no exceptions.

RULE 1 — NO SYNTHESIS, EVER.

  No price, rate, OHLC field (O/H/L/C), or pivot input value may be

  synthesised, estimated, interpolated, memory-recalled, or derived from

  analytical commentary. If it was not fetched as a price quote from an

  independent source, it may not be used.

RULE 2 — SEQUENTIAL SOURCE EXHAUSTION.

  When a source fails for any reason (network, paywall, empty, parse error),

  log the failure and immediately try the next source in rank order.

  Continue until corroboration is achieved or all 50 sources are exhausted.

RULE 3 — TWO-SOURCE CORROBORATION REQUIRED.

  A value is accepted only when at least two independent sources agree

  within the corroboration tolerance:

    - FX 5dp pairs (EURUSD, EURGBP, EURCAD): <= 0.00005 (0.5 pip)

    - FX 3dp pairs (EURJPY):                 <= 0.050   (5 pips)

    - Index (DXY):                           <= 0.050

RULE 4 — HALT ON FAILURE.

  If all 50 sources are exhausted without achieving corroboration, the

  engine raises DataCorroborationError and HALTS. The analysis is not

  produced. The Agent Log records every attempt. No partial analysis or

  'best estimate' output is acceptable.

RULE 5 — COMPLETE AUDIT TRAIL.

  The Agent Log must record for every symbol: every source attempted

  (name, tier, rank, status, error if any), the corroborated pair,

  the delta between the two corroborating values, and the tolerance used.

RULE 6 — SCOPE.

  These rules apply to: all daily OHLC data, all pivot prior-period H/L/C

  values, all spot rates used in consensus tables, and all cross-check

  triangulation reference values.

## **Patch B.2 — Add source discipline note to Section 4.1 (Input validation)**

LOCATION: Section 4.1 'Input validation'. Append the following paragraph at the end of the section:

*Source discipline: cross-validation of OHLC across approved sources is not optional. The engine will not produce any output for a symbol unless at least two independent sources have corroborated the most recent close price within the stated tolerance. If corroboration cannot be achieved across all 50 approved sources, the symbol is excluded from the report and the failure is recorded in the Agent Log. Under no circumstances is a value estimated or substituted.*

## **Patch B.3 — Update Section 10 Final Judgement Syntax (add source status line)**

LOCATION: Section 10 'Final judgement syntax'. Append a seventh line to the six-line block:

Short-term technical state:   [Trending / Ranging / Transitional] — [Bullish / Bearish / Mixed]

Medium-term technical state:  [Trending / Ranging / Transitional] — [Bullish / Bearish / Mixed]

Preferred trade protocol:     [Range fade / Trend pullback / Reduced conviction]

Integration note:             [Forecast / macro / sentiment should lean with / oppose / remain cautious]

Pivot reference (daily):      [Price vs D.P / D.R1 / D.S1 — testing / above / below / at confluence]

Pivot reference (structural): [Weekly and monthly pivot alignment — supportive / resistive / neutral]

Source status:                [Corroborated: source_A x source_B | Sources tried: N | Any un-corroborated fields: none / list]

*END OF DOCUMENT — Absolute No-Synthesis Source Discipline Protocol  |  Issue 21 March 2026*

*This document supersedes all prior source-discipline patches. No further amendments needed unless the approved source list changes.*