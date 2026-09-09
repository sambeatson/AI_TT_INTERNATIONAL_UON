*M5 — Strategies Module  │  Modular Prompt Architecture v2.1  │  DO NOT EDIT*

| **M5   ****MODULE 5 — FIXED STRATEGIES MODULE** *DO NOT EDIT  ·  This module is fixed. Variable placeholders are consumed from M1 at run time. Inputs are consumed from the M3 §11 Named Output Surface only.* *Modular Prompt Architecture v2.1  │  April 2026  │  Refreshed to single-source on M3 §11* |
| --- |

| **M1  VARIABLES** *Provides inputs* | **M2  RESEARCH STD** *Governs evidence* | **M3  TECHNICAL** *Governs technicals* | **M4  OUTPUT** *Formats results* | **M5  STRATEGIES** *← You are here* |
| --- | --- | --- | --- | --- |

You are acting as a **[ROLE_TITLE]** producing a regime-aware, three-tier set of trade recommendations for **[PRIMARY_ASSET]** as of **[AS_OF_DATE]** (**[AS_OF_TIMEZONE]**). This module is the executable expression of the analysis already established in M2 and M3. It does not fetch new data, does not infer new signals, and does not override the §17 Forecast.  It consumes one and only one upstream contract: the **M3 §11 Named Output Surface**.  All technical inputs reach M5 through that surface.

This module runs **after** M3 has produced its Named Output Surface, and **before** M4 begins formatting §21. Outputs from this module feed exclusively into M4 §21. Trade cards are produced for **[PRIMARY_ASSET] only**.

## **VARIABLES CONSUMED FROM M1**

| **M1 Variable** | **How M5 uses it** |
| --- | --- |
| [PRIMARY_ASSET] | Sole instrument for which trade cards are produced. |
| [TICK_SIZE] / [TICK_NAME] | Drives the dual price-and-native-unit reporting convention in §21b. Required when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. |
| [UNIT_OF_MEASURE] / [CURRENCY] | Price-display convention. |
| [AS_OF_DATE] / [AS_OF_TIMEZONE] | Snapshot date for the trade cards and t−1 close anchor for the §7 backtest. |
| [PRODUCE_STRATEGY_RECOMMENDATIONS] | Master switch. NO → entire module skipped, M4 §21 omitted. |
| [DAILY_OPEN_ANCHOR] | 00:00 UK / 07:00 UK — Trade 1 entry timestamp. |
| [PRODUCE_PIVOT_TRADE] | Trade 2 gate. |
| [PRODUCE_COMPLEX_TRADE] | Trade 3 gate. Single switch — regime determines 3A / 3B / 3C. |
| [MAX_SIMULTANEOUS_LONG_SHORT] | Allows opposing trade cards across the three strategies when YES. |
| [FIB_RANGE_DAYS] | Default minimum lookback for fib swing anchor (3–10 sessions, adaptive). Default 4. |
| [BACKTEST_LOOKBACK_DAYS] | Number of prior sessions replayed in §7 backtest. Default 5. |
| [ATR_STOP_CAP] | ATR multiple cap for structural stops. Default 3.5. |
| [BE_TRAIL_R] | Runner stop offset in R-multiples on Unit 2 fill. Default 0.2. |
| [CONVICTION_THRESHOLD] | Absolute conviction score below which Trade 1 is suppressed. Default 0.25. |
| [W_SHORT_TECH] / [W_MEDIUM_REGIME] / [W_VOLATOR] / [W_KAUFMAN] / [W_SENTIMENT] / [W_CROSS_ASSET] | Direction-scoring weights consumed in §2. Defaults sum to 1.00. Locked for a minimum of 20 sessions before any tuning. |

| **ABSOLUTE RULES — strategies are deterministic, structural, and traceable** 1. SINGLE INPUT CONTRACT.  M5 reads from one upstream surface only: the M3 §11 Named Output Surface. M5 may not reach into M3 sub-steps directly, may not re-derive any value already on the surface, and may not call M2 or M1 except for the variables explicitly listed above. If a required surface value is absent, suppress the affected trade card and log the reason — never substitute or estimate. 2. NO NEW DATA.  M5 fetches nothing. Every value used must already exist in M1 variables or on the M3 §11 surface. 3. NO SYNTHESIS OF LEVELS.  Pivots, swings, ATR, regime, and sentiment tilt come from the surface only. M5 may compute the fib swing anchor and floor-pivot midpoints (R1.5 / S1.5), but never invents an OHLC, pivot, or sentiment value. 4. SINGLE-SOURCE INDICATIVE PROPAGATION.  Any trade card whose entry or stop references a SINGLE-SOURCE-INDICATIVE level (per the corroboration flag on the surface) must carry the indicative qualifier in §21b and the same flag in M4 §19. Trade 2 is suppressed entirely if all accessible pivot tiers are SINGLE-SOURCE-INDICATIVE. 5. PRIMARY ASSET ONLY.  No trade card may reference a price, level, or invalidation in a secondary or counter asset. Cross-asset signals contribute to direction scoring (via the surface’s cross_asset_confirm field) only. 6. NO OVERRIDE OF §17.  M5 does not modify, soften, or contradict the §17 Forecast. Conflicts between the §21a directional conviction and the §17 forecast are flagged in §21a but never resolved by editing either output. 7. THREE TRANCHES, ALWAYS.  Every triggered trade is composed of three equal units. Tranching, BE+[BE_TRAIL_R]·R management, and runner exit rules are universal across all trade types except where a structural runner rule explicitly supersedes them (Trade 3A 100%-extension stop pull is the only such case). 8. GATES ARE NON-OVERRIDABLE.  The suppression triggers in §10, the order-side and anchor rules in §5.0, and the pre-emit checklist in §9a are part of the fixed module. No run-time direction, user instruction, operator note, standing preference, or convenience argument may relax, defer, or reverse them, and no such instruction may be cited in the report as authority for doing so. If a gate fires, the only compliant outputs are the SUPPRESSED row or a rebuild that clears the gate on its merits. A card emitted against a fired gate is a P-level QA failure regardless of how well formed it is. |
| --- |

# **§1  Inputs Consumed (Single-source contract)**

M5 reads from three places: M1 variables (Section H + tick spec from B), the M2 sentiment derivation (passed through M3 §11 — never read directly), and the M3 §11 Named Output Surface. There is no other input path.

### **§1a  From M1**

| **Input** | **Purpose** |
| --- | --- |
| Strategy switches (Section H.1) | Master gate, daily-open anchor, per-trade gates, simultaneous long/short policy. |
| Strategy parameters (Section H.2 + H.4) | ATR_STOP_CAP, BE_TRAIL_R, CONVICTION_THRESHOLD, FIB_RANGE_DAYS, BACKTEST_LOOKBACK_DAYS. |
| Direction weights (Section H.3) | Six [W_*] weights for §2 direction scoring. |
| Tick spec (Section B) | [TICK_SIZE], [TICK_NAME] for native-unit conversion of stops and targets. |

### **§1b  From the M3 §11 Named Output Surface**

Every M3-derived input is read by name from the surface. M5 makes no direct reference to M3 sub-steps. This is the entire technical-input contract:

| **Surface field** | **How M5 uses it** |
| --- | --- |
| atr_14 | Trade 1 SL cap (§4c); Trade 2 RANGE ATR-tier selection (§5.2a); fib swing magnitude qualifier (§4b); Trade 1 TP3 runner cap. |
| rsi2_latest | Direction signal — short-term technical bias contribution (§2 W_SHORT_TECH). |
| swing_high_5d / swing_low_5d | Trade 1 SL anchor (§4c). |
| swing_high_25d / swing_low_25d | Range definition for Trade 3B / 3C; secondary SL anchor for trend-following Trade 2. |
| fractal_swings | Adaptive fib swing anchor selection (§4b). Empty list → suppress Trade 3A and 3B. |
| pivots_daily / pivots_weekly / pivots_monthly | Trade 2 entry levels (S1/S1.5/S2 or R1/R1.5/R2). Each pivot dict carries a corroboration flag (CORROBORATED / SINGLE-SOURCE-INDICATIVE) which propagates to the §21b trade card and §10 suppression rules. |
| nearest_support / nearest_resistance | Trade 1 SL alternative anchor (tighter of swing or S/R + 0.25 × ATR buffer). |
| ker_value, ker_class | Direction signal (§2 W_KAUFMAN). RANGE-regime confirmation gate (§3a). |
| volator_slope | Direction signal (§2 W_VOLATOR). RANGE-regime confirmation gate (§3a). |
| cross_asset_confirm | Direction signal (§2 W_CROSS_ASSET) — one of {CONFIRM, CONTRADICT, MIXED, NEUTRAL}. |
| regime_label | Single source of truth for the regime fork in §3 — one of {TREND_UP, TREND_DOWN, RANGE, TRANSITION}. M5 does not re-derive the label. |
| sentiment_tilt | Pass-through of the M2 §13b numeric tilt. Direction signal (§2 W_SENTIMENT). |
| seven_line_judgement | Conflict detection vs §17 Forecast (Integration note line). |

### **§1c  From M2 (indirect — via M3 §11)**

M5 does not read M2 directly. The M2 §13b numeric tilt is exposed on the M3 §11 surface as sentiment_tilt and is consumed from there. The M2 §13d news calendar is consumed by M4 §21b for trade-card holding-period collision flagging — M5 itself does not need the calendar to construct trade cards.

# **§2  Direction Derivation (shared by all three trades)**

Direction is computed once per session as a weighted, signed score in [−1, +1]. The same direction is used by all three trade types unless overridden by a structural rule (Trade 2 RANGE limits face the level, not the directional score; Trade 3C breakout direction follows the broken side).

### **§2a  Signal vector**

| **Signal** | **Source field on the surface** | **Value mapping → [−1, +1]** | **Default Weight** |
| --- | --- | --- | --- |
| Short-term technical bias | rsi2_latest + 5-day trend in seven_line_judgement | Bullish = +1, Bearish = −1, Neutral = 0 | [W_SHORT_TECH] = 0.25 |
| Medium-term regime | 5-week regime line in seven_line_judgement | Trend up = +1, Trend down = −1, Range = 0, Transition = sign of last completed swing × 0.5 | [W_MEDIUM_REGIME] = 0.20 |
| VOLator regime | volator_slope (signed) | Expansion-up = +0.5, Expansion-down = −0.5, Compression = 0, sign aligned with most recent breakout | [W_VOLATOR] = 0.10 |
| Kaufman KER | ker_value, ker_class | Linear in ker_value × sign of medium-term move; capped at ±1 | [W_KAUFMAN] = 0.15 |
| Sentiment tilt | sentiment_tilt | Use as-is — already in [−1, +1] | [W_SENTIMENT] = 0.15 |
| Cross-asset confirmation | cross_asset_confirm + medium-term direction | CONFIRM = sign × 1, MIXED = sign × 0.3, CONTRADICT = sign × −0.5, NEUTRAL = 0 | [W_CROSS_ASSET] = 0.15 |

### **§2b  Aggregation**

**score = Σ ( signalᵢ × weightᵢ )**

direction =  **LONG** if score ≥ +[CONVICTION_THRESHOLD],  **SHORT** if score ≤ −[CONVICTION_THRESHOLD],  otherwise **NEUTRAL**.

If direction = NEUTRAL, Trade 1 is suppressed. Trade 2 proceeds — its direction is regime-driven (regime_label), not score-driven. Trade 3 proceeds — its direction follows regime_label (3A / 3B trend or range bias) or the broken side (3C).

### **§2c  Twenty-session lock**

**Direction-weight defaults are locked for a minimum of 20 sessions.**  No weight value may be changed in a live forward-test session before 20 baseline sessions have completed under the default vector. After session 20, weight changes are permitted but must be logged in M4 §20 with the prior values, the new values, and the rationale.

# **§3  Regime Gate (drives Trade 3 fork and Trade 2 logic)**

M5 reads regime_label from the M3 §11 surface — never re-derives it. The mapping below is informational; the surface is authoritative.

| **regime_label (from surface)** | **Trade 2 logic** | **Trade 3 variant** |
| --- | --- | --- |
| TREND_UP | Trend-following: long entry above pivot | 3A Momentum-Pullback — long |
| TREND_DOWN | Trend-following: short entry below pivot | 3A Momentum-Pullback — short |
| RANGE | Mean-reversion at S1/S1.5/S2 and R1/R1.5/R2 | 3B Mean-Reversion |
| TRANSITION | Breakout-side limit only (aligned with 3C direction) | 3C Momentum-Breakout |

### **§3a  RANGE confirmation (cross-check the surface)**

RANGE is permitted only when the M3 §11b dual-gate rule is satisfied: ker_value < [KAUFMAN_TREND_THRESHOLD] in absolute terms AND volator_slope ≤ 0. The surface enforces this. M5 reads regime_label = RANGE as confirmation. If the surface emits RANGE without satisfying the dual gate, raise a SurfaceContractError and halt the module — this is a M3-level protocol failure that must be fixed upstream.

### **§3b  TRANSITION rationale**

TRANSITION is treated as a directional regime, not a hold. The thesis is that the prior range has already been tested and faked out sufficiently that the next confirmed break has elevated probability of follow-through. Trade 3C is therefore a momentum trade in the direction of the break, with a generous structural stop reflecting the post-fakeout context. Trade 2 in TRANSITION is restricted to the breakout side only — placing a limit on the opposite side would front-run Trade 3C and is suppressed.

# **§4  Level Derivation**

All structural levels come from the M3 §11 surface. M5 derives only the fib swing anchor (using fractal_swings) and the floor-pivot midpoints (R1.5, S1.5). No other levels are computed by this module.

### **§4a  Floor-pivot midpoints**

R1.5 = (R1 + R2) / 2        S1.5 = (S1 + S2) / 2

Computed at all three pivot timeframes (daily, weekly, monthly) when the corresponding pivots dict is present on the surface (i.e. the M1 toggle was YES). Carries forward the corroboration flag of the parent pivots dict — if R1 / R2 are SINGLE-SOURCE-INDICATIVE, R1.5 inherits the flag.

### **§4b  Fib swing anchor (adaptive)**

Read fractal_swings from the M3 §11 surface. Algorithm:

- Start with a [FIB_RANGE_DAYS]-session lookback (default 4). Find the most recent qualifying swing in fractal_swings whose magnitude ≥ 2 × atr_14.

- If no qualifying swing exists at the default lookback, extend to a maximum 10 sessions in 1-session increments. Use the surface’s fractal_swings list — do not detect fractals from raw OHLC.

- If after 10 sessions no swing of magnitude ≥ 2 × atr_14 is found, log ‘NO QUALIFYING SWING’ and suppress Trade 3A and 3B. Trade 3C remains available — its anchor is the 25-day range boundary, not the swing.

- Direction of the swing: if the latest local high is more recent than the latest local low, the active swing is up (retracements measured from low → high); inverse for down.

- The selected swing endpoints, the lookback that was actually used, and the swing magnitude in ATR units must be logged on every Trade 3 card.

### **§4c  Trade 1 SL anchor**

Tighter of (a) the relevant swing extreme from the surface (swing_high_5d for shorts, swing_low_5d for longs), or (b) nearest_support / nearest_resistance from the surface, with a 0.25 × atr_14 buffer added beyond the chosen anchor. The whole stop distance is then capped at [ATR_STOP_CAP] × atr_14 — if the structural stop is wider than the cap, the cap applies and the trade size is reduced commensurately rather than the stop being moved tighter.

### **§4d  Trade 3C breakout anchor**

The prior range is bounded by swing_high_25d and swing_low_25d on the surface. ‘Confirmed break’ requires a daily close beyond the boundary by at least 0.25 × atr_14. Without the confirming close, the trade is not eligible.

# **§5  Trade Construction**

## **§5.0  Order-side, anchor, and reference-close rules (apply to every card)**

These four rules bind every card built in §5.1–§5.3 and are checked again at §9a. They add no strategy logic — they state the conditions a card must already satisfy.

| **Rule** | **Condition** |
| --- | --- |
| Reference close | Every card is built against one reference close: the settled close of the last completed primary-asset session strictly before the report date (D-1). Print that close, as a number and with its session date, on every card. A card built on a D-2 close, an intraday mark, or a proxy-instrument close is non-compliant. |
| MARKET entry | A MARKET card enters at the D-1 reference close. State the level as a number; do not substitute a prior session’s close, a synthetic open, or a rounded figure. |
| Order side | A BUY LIMIT and a SELL STOP must sit at or below the D-1 reference close. A SELL LIMIT and a BUY STOP must sit at or above it. A card whose entry sits on the wrong side of that close is non-compliant and must be rebuilt or suppressed — it is never shipped with a note. State the entry, the reference close, and the signed gap between them on the card. |
| Anchor | Entry timing is [DAILY_OPEN_ANCHOR] as populated in the M1 instance in force for this run. That value governs; it is not re-selected per run, per session, or per convenience. One anchor is stated on the card, in the handoff record, and in the report body, and the three must read the same converted time. |

## **§5.1  Trade 1 — Daily Directional**

Direction-of-the-day expression. Always entered at [DAILY_OPEN_ANCHOR]. Suppressed if §2 score is NEUTRAL.

| **Element** | **Rule** |
| --- | --- |
| Direction | From §2 (LONG / SHORT). Suppressed if NEUTRAL. |
| Entry | Market or just-fillable order at [DAILY_OPEN_ANCHOR] as populated in the M1 instance — the parenthetical options in the M1 variables contract are the menu the instance chooses from, not a choice left open at run time. The fill level is the D-1 reference close per §5.0. |
| Stop loss | Per §4c. Tighter of (5-day swing extreme + 0.25 × atr_14) or (nearest_support/resistance + 0.25 × atr_14), capped at [ATR_STOP_CAP] × atr_14. |
| Position structure | 3 equal units. |
| TP1 (Unit 1) | Entry ± 1 × R, where R = entry-to-SL distance. |
| TP2 (Unit 2) | Entry ± 2 × R. On fill, Unit 3 SL moves to entry ± [BE_TRAIL_R] × R. |
| TP3 (Unit 3 — runner) | Time-stopped at session close, OR price-stopped at 3 × atr_14 from entry, whichever triggers first. |
| Sanity check | Mandatory on every card in §5, not Trade 1 alone. Print R in points and as a multiple of atr_14 (R ÷ atr_14, two decimals). If R > 1 × atr_14, the card carries the ‘wide stop’ flag — the flag is set by the arithmetic, not by judgement, and omitting it is a construction defect even where the stop is otherwise correct. If 2 × R > 3 × atr_14, flag ‘TP2 ambitious for a daily horizon’ — do not suppress. Both tests use the stated atr_14 from the surface; a proxy or implied volatility figure may not be substituted. |
| Thesis invalidation | The next structural level beyond SL, and a different price from the SL. It may not be set equal to the stop, nor placed so close to it that it carries no information the stop does not already carry. State it as a close-through condition on a named level. |

## **§5.2  Trade 2 — Pivot, regime-aware**

Trade 2 is fully regime-driven. Direction does NOT inherit from §2. In RANGE, Trade 2 fades pivots; in TREND, Trade 2 follows the trend across the pivot; in TRANSITION, Trade 2 plays the breakout side only.

The branch is selected by regime_label on the surface and by nothing else. One regime label governs the whole run: the label used to pick this branch must be the same label reported in the technical sections and the same label used to fork Trade 3. Name the branch on the card (RANGE / TREND / TRANSITION) and build every element from that branch’s row only. Borrowing geometry across branches — a mean-reversion limit under TREND or TRANSITION, a pivot-fade ladder where the breakout rule applies — is a construction defect even when the resulting levels are internally consistent. If the regime is TRANSITION, the only permitted Trade 2 is a breakout-side entry beyond the boundary; a limit on the counter side is suppressed, not re-labelled.

### **§5.2a  RANGE regime — mean-reversion at pivots**

| **Element** | **Rule** |
| --- | --- |
| Direction (long) | Buy limit at S1, S1.5, or S2. |
| Direction (short) | Sell limit at R1, R1.5, or R2. |
| Tier selection | ATR-tiered using atr_14. Distance from current price to the pivot:  < 1 × atr_14 → tier 1.  1–2 × atr_14 → tier 1.5.  > 2 × atr_14 → tier 2. |
| Fib confluence override | Any pivot tier within 0.15 × atr_14 of an active fib retracement (38.2%, 50%, 61.8%, 78.6%) is promoted to first-pick. Confluence logged on the trade card. |
| Stop loss | [ATR_STOP_CAP] × atr_14 from entry, beyond the pivot. If a structural level (next pivot tier, swing extreme) sits closer than the ATR cap, the structural level + 0.25 × atr_14 buffer is used instead. |
| Position structure | 3 equal units. |
| TP1 / TP2 / TP3 | Entry ± 1 × R / Entry ± 2 × R / runner toward P (the pivot). |
| Suppression | Suppressed entirely if all accessible pivot tiers carry the SINGLE-SOURCE-INDICATIVE flag on the surface (i.e. corroboration field of pivots_daily / pivots_weekly is SINGLE-SOURCE-INDICATIVE for every active timeframe). ‘Accessible’ means every pivot timeframe toggled YES in M1 that this card could draw a level from — not merely the tier the card happened to choose. The test is symmetric: if the report states anywhere that every pivot tier is indicative, the card is suppressed; if a card is produced, the report must show which tier is corroborated and by which second source. Stating the flag and shipping the card anyway is the failure this rule exists to prevent. A tier that is absent or uncomputed is not the same as one that is indicative — pivots that can be computed from corroborated prior-period H/L/C must be computed before this test is run. **The flag describes the provenance of the H/L/C actually used to compute the tier, not the provenance of any figure quoted elsewhere in the report.** A tier computed from the execution price series — the broker series the resulting order is filled and settled against — is CORROBORATED by construction: that series is the settlement source, not a secondary quote about it, and there is nothing for a second source to corroborate it against. This gate exists for tiers struck from narrative or aggregator quotes whose true prior-period H/L cannot be established. Where the execution series is in hand, recompute the tier from it and record the flag as CORROBORATED with the series and session named; do not inherit an indicative flag that described a different and weaker input. |

### **§5.2b  TREND regime — pivot breakout**

| **Element** | **Rule (long; mirror for short)** |
| --- | --- |
| Direction | Long in TREND_UP; short in TREND_DOWN. |
| Entry (long) | Stop or limit at  P + 0.10 × (R1 − P)  — 10% of the way from P to R1, on the upside. |
| Stop loss (long) | P − 0.8 × (P − S1). If a confluence (5-day swing low, weekly S1, prior-day low) sits just below S1, use ‘just below S1 minus 0.25 × atr_14’ instead — whichever is tighter. |
| Position structure | 3 equal units. |
| TP1 / TP2 / TP3 | R1 / R1.5 / R2. |
| Thesis invalidation | Daily close back through P. Documented even when SL is tighter. |

### **§5.2c  TRANSITION regime — breakout side only**

In TRANSITION, Trade 2 is allowed only on the breakout side as identified by Trade 3C. Configuration mirrors §5.2b TREND breakout, with R1/R1.5/R2 for an upside breakout and S1/S1.5/S2 for a downside breakout. A counter-side limit (e.g., a sell limit at R1 when 3C is long) is suppressed — placing one would front-run 3C and contradict the regime read.

## **§5.3  Trade 3 — Regime-driven, structural TPs preserved**

Single switch [PRODUCE_COMPLEX_TRADE]. regime_label determines which variant is built, on a fixed mapping with no discretion: TREND_UP / TREND_DOWN → 3A, RANGE → 3B, TRANSITION → 3C. Name the fork and the label that selected it on the card. A card headed with one variant and built with another variant’s geometry is non-compliant; so is a variant chosen because its levels look more tradeable. If the selected variant’s own eligibility test fails (§4b for 3A/3B, §4d for 3C), the outcome is the SUPPRESSED row for that variant — never a substitution of a different variant, and never pivot levels standing in for swing or range levels.

### **§5.3a  Trade 3A — Momentum-Pullback (regime_label ∈ {TREND_UP, TREND_DOWN})**

| **Element** | **Rule (long; mirror for short)** |
| --- | --- |
| Direction | Long in TREND_UP; short in TREND_DOWN. |
| Fib anchor | Most recent qualifying swing per §4b — swing low → swing high for longs. |
| Entry | 57.5% retracement of the swing  (= midpoint of the 50% and 61.8% retracements). |
| Stop loss | Beyond the 0% anchor (swing low) by 0.25 × atr_14, capped at [ATR_STOP_CAP] × atr_14. |
| Position structure | 3 equal units. |
| TP1 (Unit 1) | 38.2% retracement — shallow-pullback target. |
| TP2 (Unit 2) | 0% — full retrace, swing origin (high for longs). On fill, Unit 3 SL moves to entry + [BE_TRAIL_R] × R. |
| TP3 (Unit 3 — runner) | 100%+ extension of the swing. |
| Runner stop pull (structural override) | When price prints above the 100% extension, Unit 3 SL moves to the 50% mark of the original 1:1 leg — halfway between entry (57.5%) and TP2 (0%). Locks in more than the universal BE+[BE_TRAIL_R]·R rule. Only documented case where a structural rule supersedes the universal trail. |
| Thesis invalidation | Daily close beyond the swing-low anchor. |

### **§5.3b  Trade 3B — Mean-Reversion (regime_label = RANGE)**

| **Element** | **Rule** |
| --- | --- |
| Range definition | swing_high_25d and swing_low_25d from the M3 §11 surface. |
| Direction (short) | Sell limit at 78.6%–88.6% of the range (measured from low = 0% to high = 100%). |
| Direction (long) | Buy limit at 11.4%–21.4% of the range. |
| Stop loss (short) | Inside the upper boundary by 10% of range width: high − 0.10 × width.  Worked example: range 100.00 / 110.00 (width 10), short filled at 108.50, stop at 109.00. |
| Stop loss (long) | Inside the lower boundary by 10% of range width: low + 0.10 × width. |
| Position structure | 3 equal units. |
| TP1 (Unit 1) | Range midpoint:  low + 0.50 × width. |
| TP2 (Unit 2) | Opposite side − 10% of range width (for shorts: low + 0.10 × width;  for longs: high − 0.10 × width). On fill, Unit 3 SL moves to entry ∓ [BE_TRAIL_R] × R. |
| TP3 (Unit 3 — runner) | Breakout runner. When TP2 fills, runner SL moves to just past midpoint (mid + 0.05 × width for shorts, mid − 0.05 × width for longs). |
| Thesis invalidation | Daily close outside the range (in the direction the trade is fading). |

### **§5.3c  Trade 3C — Momentum-Breakout (regime_label = TRANSITION)**

The post-fakeout breakout play. Generous structural stop reflecting the prior chop.

| **Element** | **Rule (upside breakout; mirror for downside)** |
| --- | --- |
| Range definition | Same as 3B — swing_high_25d / swing_low_25d from the surface. |
| Direction trigger | Side of the most recent failed retest of the boundary, confirmed by volator_slope sign and cross_asset_confirm. Long if recent retests have failed at the upper boundary. |
| Confirmed break | Daily close beyond the boundary by ≥ 0.25 × atr_14. Without this, trade is not eligible. |
| Entry | On confirmed breakout, at breakout candle close (or following session open if breakout is identified after close). |
| Stop loss | Inside range, at far side of midpoint:  range_low + 0.40 × width  for upside breakouts (just below midpoint). Generous post-fakeout stop. |
| Position structure | 3 equal units. |
| TP1 (Unit 1) | Measured move: high (broken) + 1.0 × width. |
| TP2 (Unit 2) | 1.5 × measured move. On fill, Unit 3 SL moves to the broken boundary (tighter than [BE_TRAIL_R] dictates). |
| TP3 (Unit 3 — runner) | Discretionary trail beyond 1.5 × MM, anchored to subsequent swing structure. |
| Thesis invalidation | Daily close back inside range past midpoint. |

# **§6  Invalidation Prices and Confluence Logging**

### **§6a  Invalidation**

Every trade card carries an explicit ‘thesis invalidation’ value separate from the stop loss. The invalidation is the first level whose close-through breaks the directional narrative. It must be a named structural level and a different price from the stop: it may sit beyond the stop or — for tightly stopped pivot trades — inside it, but an invalidation set equal to the stop, or within 0.15 × atr_14 of it, is not an invalidation and the card is non-compliant. The stop is an intraday price; the invalidation is a close-through condition. When invalidation is wider than stop, the card notes ‘stop ahead of invalidation’.

### **§6b  Confluences**

Each trade card lists every confluence detected at its entry, stop, and TP levels. Standardised taxonomy:

- ‘Pivot’ — daily / weekly / monthly P, R1–R3, S1–S3, R1.5, S1.5.

- ‘Swing’ — swing_high_5d / swing_low_5d / swing_high_25d / swing_low_25d (all from the surface).

- ‘Fib’ — 38.2%, 50%, 57.5%, 61.8%, 78.6%, 88.6% retracement levels of the active swing.

- ‘Round number’ — major round-number levels in the asset’s native unit.

- ‘Cross-asset’ — e.g., USDX rejection at a structural level coinciding with EUR/USD support.

Two or more confluences within 0.15 × atr_14 are aggregated and logged as ‘strong confluence’.

# **§7  Backtest Synthesis (no leakage)**

The backtest reconstructs the prior [BACKTEST_LOOKBACK_DAYS] sessions (default 5) as if M5 had run at each prior t−1 close, then resolves each trade on the actual t-session OHLC.

### **§7a  No-leakage rules**

| **Information channel** | **Reconstruction rule** |
| --- | --- |
| M3 §11 surface fields (atr_14, swings, pivots, KER, VOLator slope, cross_asset_confirm, regime_label, fractal_swings) | Reconstruct each as it would have been at t−1 close. The surface contract is replayable: every named field is a function of OHLC and counter data ending at t−1, with no forward dependence. |
| sentiment_tilt | Frozen at t−1. Only articles published at or before t−1 contribute. Today’s sentiment is not propagated backwards. |
| regime_label | Recomputed at t−1 from the rolling 25-session block ending at t−1. No use of the current label. |
| News calendar | Only events whose dated impact is at or before t−1 contribute. |

### **§7b  Trade resolution**

- If entry was a market order at [DAILY_OPEN_ANCHOR], entry price = the t-session open.

- If entry was a limit, the trade triggers only if price reached the limit price within the t-session’s actual high/low range; entry price = the limit (slippage = 0).

- If both SL and a TP could fill within the same bar, SL is assumed first unless OHLC sequence rules out the stop. Conservative tick-priority rule.

- Multi-day resolution: positions carry forward up to 5 sessions; unresolved at t+5 recorded as OPEN with mark-to-market R.

### **§7c  Aggregate output (§21d ‘What is working’)**

- Trigger rate per strategy type (count triggered / count issued).

- Mean R outcome across triggered trades (closed positions only).

- TP1 / TP2 / TP3 hit rates (independent — a trade can hit TP1 then SL on the runner).

### **§7d  Limitations**

Five-session windows are too small for statistical claims. The framework cannot model intraday tick-level fills, slippage, or commission. The §21d output must state these limitations verbatim.

# **§8  Output Handoff to M4 §21**

| **§21 sub-section** | **Content from M5** |
| --- | --- |
| §21a Directional Conviction | One paragraph: §2 direction, score, three highest-weighted contributing signals, and any conflict with §17 forecast. |
| §21b Trade Cards (1, 2, 3) | Three structured tables. Each card per the M4 §21b standard structure. Suppressed trades produce a SUPPRESSED row, not an omission. |
| §21c 5-session backtest table | Per-session rows: date, strategy, direction, triggered, entry, exit, R outcome, days-to-resolution. |
| §21d ‘What is working’ summary | Per §7c plus one-line limitations boilerplate from §7d. |

The surface field names, trigger names, weight names and module or step codes used throughout M5 are internal addresses for building the handoff object. They are not report language. What crosses into M4 is the value, the plain-English description of how it was derived, and the report’s own section numbers — never the identifier. This applies to the Agent Log feed as much as to the card body.

# **§9  Procedure (run order)**

- Read M1. Confirm [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. If NO, halt M5 and signal M4 to omit §21. If YES, read all M1 strategy variables and tick spec; record for the Agent Log.

- Read the M3 §11 Named Output Surface. Verify presence of every field listed in §1b. If any required field is absent, log and proceed with the affected trade card suppressed. Do not attempt to fetch underlying values from M3 sub-steps — that would breach the single-source contract.

- Cross-check §3a dual-gate rule on regime_label = RANGE (M3 should already enforce; M5 verifies as defence-in-depth).

- Compute §2 direction score and label. Log per-signal contributions, weights, and total. Apply [CONVICTION_THRESHOLD].

- Apply §3 regime gate. Determine which Trade 3 variant (3A / 3B / 3C) is active.

- Compute §4 levels. Floor-pivot midpoints (R1.5, S1.5). Fib swing anchor with adaptive lookback per §4b using fractal_swings.

- Construct Trade 1 per §5.1. Apply suppression rules. Generate the trade card object.

- Construct Trade 2 per §5.2 (regime branch). Apply suppression rules. Generate the trade card object.

- Construct Trade 3 per §5.3 (variant per §3). Apply suppression rules. Generate the trade card object.

- Annotate every trade card with confluences (§6b) and explicit thesis invalidation (§6a). Propagate any SINGLE-SOURCE-INDICATIVE flag from the surface into the card caveats.

- Run §7 backtest. Reconstruct prior [BACKTEST_LOOKBACK_DAYS] sessions. Resolve on actual OHLC. Aggregate per §7c.

- Run the §9a pre-emit checklist. Do not emit any card until every row passes.

- Emit the §8 handoff object to M4 §21. Write the full M5 trace to the Agent Log section that M4 §20 will consume.

### **§9a  Pre-emit checklist (mandatory, per card)**

Run this before any card leaves M5. Each row is a test on a number already computed — none of it is new analysis. Record the row, the value tested and PASS or FAIL in the trace. **A FAIL is not a caveat.** The card is rebuilt until the row passes, or it is emitted as a SUPPRESSED row. A card shipped with a known FAIL, however well annotated, is a P-level QA failure.

| # | Check | Passes when |
| --- | --- | --- |
| 1 | Reference close | The D-1 reference close is printed as a number with its session date, and it is the settled close of the last completed session strictly before the report date. |
| 2 | Suppression gates | Every §10 trigger has been tested and its outcome logged. No fired trigger has been overridden. No suppressed row carries a stop, R or TP ladder. |
| 3 | Order side | MARKET entry equals the reference close; every LIMIT / STOP entry sits on the side of that close required by §5.0, with the signed gap printed. |
| 4 | Anchor | One anchor value, matching the M1 instance, stated identically on the card, in the handoff record and in the report body. |
| 5 | atr_14 stated | atr_14 appears on the card as a number, with its window and bar basis named. No proxy, no ‘implied’ or ‘approximate’ figure, no value inferred backwards from a buffer. |
| 6 | R and the wide-stop flag | R is printed in points and as R ÷ atr_14. Where that ratio exceeds 1.00 the ‘wide stop’ flag is present. Where it falls outside 0.3–3.0 the card is rebuilt, not warned. |
| 7 | Ladder order | For a long: stop < entry < TP1 < TP2 < TP3 (or TP3 null). Mirrored for a short. An inversion is resolved before emission, never narrated. |
| 8 | Branch and fork | The regime label is stated once, is the same label used in the technical sections, and the Trade 2 branch and Trade 3 fork named on the cards are the ones that label selects. |
| 9 | Derivation session | Every pivot level cited is from the prior period defined in M3 Step 8, and every swing endpoint is dated and inside the stated lookback. |
| 10 | Invalidation | Present, a named structural level, and a different price from the stop by more than 0.15 × atr_14. |
| 11 | Units | Every stop and target appears in both price and the native execution unit. |
| 12 | Naming | No surface field name, trigger name, weight name, module or step code, bracketed variable token or framework identifier appears anywhere in the emitted card or its caveats. |

# **§10  Suppression and Anomaly Rules**

Trade cards are suppressed — not faked, softened, or interpolated — when their construction inputs fail. Suppression is itself an output: §21b carries a one-line ‘SUPPRESSED — [reason]’ entry rather than being silently omitted.

Three points make this checkable rather than advisory.

- **The triggers below are not discretionary.** Each is a test on a stated value. When a trigger fires the card is suppressed, and no run-time instruction, user direction, operator preference or leniency note may reverse it. An emitted card that cites such an instruction as its authority is a P-level QA failure, and the instruction itself must not appear in the report.

- **A suppressed card is a row, not a card.** The SUPPRESSED row carries the trade name, the trigger that fired, and the value that fired it. It does not carry an entry, stop, R, or TP ladder. Where a contingent arming level is genuinely useful it may be given as a single trigger condition, outside §21b and labelled as commentary.

- **The suppression decision is recorded even when it does not fire.** For every trade, log the trigger tested, the value tested, and the outcome, so that a produced card is as auditable as a suppressed one.

| **Trigger** | **Action** |
| --- | --- |
| §2 score = NEUTRAL (│score│ < [CONVICTION_THRESHOLD]) | Suppress Trade 1. Trades 2 and 3 proceed. |
| All accessible pivot tiers SINGLE-SOURCE-INDICATIVE on the surface, after any tier computable from the execution price series has been recomputed from it (§5.2a) | Suppress Trade 2. |
| fractal_swings empty / no qualifying swing within 10 sessions | Suppress Trade 3A and 3B (Trade 3C remains available — its anchor is the 25-day range boundary, not the swing). |
| No confirmed break per §4d in TRANSITION regime | Suppress Trade 3C. |
| regime_label = RANGE without dual gate (M3-level failure) | Raise SurfaceContractError; halt M5; do not produce any trade card. Log as a P-level QA failure. |
| atr_14 absent, zero, or negative on the surface | Suppress every M5 output and signal a hard halt — log as a P-level QA failure (PATCHES.md S2 should catch this upstream). |
| [PRODUCE_STRATEGY_RECOMMENDATIONS] = NO | Skip module entirely. M4 §21 omitted. |

# **§11  Glossary**

| **Term** | **Definition** |
| --- | --- |
| R | R-multiple. R = entry-to-SL distance in the asset’s native unit. TP1 = 1 × R from entry, TP2 = 2 × R, etc. |
| Tranche / Unit | One-third of total position size. All M5 trades open as 3 equal units. |
| BE+0.2R | Break-even plus [BE_TRAIL_R] × R (default 0.2). Trigger: Unit 2 fills. |
| Surface | Shorthand for the M3 §11 Named Output Surface — the single contract M5 reads from. |
| Fib swing | Most recent significant swing identified by the §4b adaptive lookback. Magnitude ≥ 2 × atr_14. |
| Floor pivots | Standard floor-trader formula: P, R1..R5, S1..S5. R1.5 / S1.5 are M5 derivatives. |
| Measured move (MM) | Width of the 25-session range. Used for Trade 3C TP placement. |
| regime_label | M3 §11 consolidated label. One of {TREND_UP, TREND_DOWN, RANGE, TRANSITION}. |
| Conviction score | Signed scalar in [−1, +1] computed in §2. │score│ ≥ [CONVICTION_THRESHOLD] required for Trade 1. |
| Thesis invalidation | First level whose close-through breaks the trade’s directional narrative. Distinct from SL. |
| No-leakage | Backtest reconstruction constraint: no input value with date > t−1 may contribute to a t−1 trade-card reconstruction. |
| SurfaceContractError | Raised when the M3 §11 surface emits a value that violates its own contract (e.g., regime_label = RANGE without dual-gate confirmation). Halts M5. |

*End of M5. Single input contract — the M3 §11 Named Output Surface. Single output contract — the M4 §21 handoff object.*

*Modular Prompt Architecture v2.1  │  M5 Strategies Module  │  April 2026*

M5 │ April 2026 │ page  of