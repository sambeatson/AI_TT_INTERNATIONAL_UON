# Gold baseline — P0 fixture and regression numbers

Registry: `cards/baseline/gold/cards_baseline_gold.csv` — **171 cards over 57 dates**
(2026-05-11 → 2026-07-31), 20 suppressed. Families: Trade 1 ×57, Trade 2 ×57, Trade 3A ×30,
Trade 3C ×20, Trade 3B ×7.

Built by 57 isolated transcription sessions (one per report, no market data, no other report),
schema-validated centrally by `engine/assemble_cards.py --baseline`.

## Timezone (P0 step 2)
`python engine/tz_check.py data/raw/XAUUSD_p_M15.csv --expect 16:30` → **peak 16:30 broker, OK**.
10,173 bars, 111 sessions, 2026-04-01 → 2026-09-03. Broker = UTC+3; `DateTime_UTC` is mislabelled
(offset 02:00) — index by `DateTime_Broker` only. OPEN/CUTOFF for metals: **09:00 / 23:00**.

## Regression fixture — reproduce before trusting any later stage

```
python engine/resolver.py --cards cards/baseline/gold/cards_baseline_gold.csv \
    --data data/raw/XAUUSD_p_M15.csv --policy <P> --open 09:00 --cutoff 23:00 --out results/gold_baseline_<P>
```

| policy | filled | W/L | **TOTAL R** |
|---|---:|---|---:|
| `card` | 79 | 32/47 | **−10.38** |
| `midnight` | 81 | 34/47 | **−1.87** |
| `usopen` | 73 | 28/45 | **−5.17** |
| `band0845` | 69 | 24/45 | **−0.59** |
| `band0845 --be tp1` | 69 | 26/43 | **−0.61** |

## Baseline lint (`--stale-atr 0.17`, the ATR-relative equivalent of the shipped US500 15-point tolerance)

151 live cards · **CLEAN 70 = 46.4%** · **10 dud cards**

| flag | n |
|---|---:|
| STALE_ANCHOR | 22 |
| MISPLACED_STOP | 17 |
| WARN_R_TINY | 14 |
| WARN_TP3_ORDER | 11 |
| MISPLACED_LIMIT | 9 |
| UNPRICED | 7 |
| WARN_TARGET_FAR | 5 |
| DUD_TP1_SIDE | 3 |
| WARN_R_HUGE | 2 |
| MALFORMED_FILL | 1 |

## The 14 cards the reports left incomplete

These are **report defects carried into the registry deliberately**, not extraction failures. The
baseline arm has to record what each report actually published, omissions included; the linter then
scores them (a card with no entry lints as `UNPRICED`, a dud).

| card | what the report does not state |
|---|---|
| `2026-05-13_Trade_3B` | card_R_points |
| `2026-05-14_Trade_3C` | tp2 |
| `2026-06-08_Trade_1` | entry (a MARKET card with no price) |
| `2026-06-24_Trade_2`, `2026-06-24_Trade_3A`, `2026-06-25_Trade_3A` | card_R_points |
| **`2026-07-07_Trade_1/2/3C`** | **entry, stop, tp1, tp2, card_R_points — all three cards** |
| `2026-07-14_Trade_2` | entry, card_R_points (a band, not a level) |
| `2026-07-20_Trade_3C`, `2026-07-30_Trade_3C` | entry |
| `2026-07-29_Trade_3C`, `2026-07-31_Trade_3C` | card_R_points |

**2026-07-07 is a corrupt report, not a transcription problem.** All three §21b card tables render
every cell as the literal string `[object Object]`, and the same strings are present in
`reports/docx/Gold_Report_07Jul2026.docx` (`word/document.xml`) — the damage predates the markdown
conversion. Nothing was inferred to fill the gap; the three cards carry only what the surrounding
prose states, and lint as UNPRICED.

## Note on the daily-open anchor

`M1_Variables_v2_1.md` fixes `[DAILY_OPEN_ANCHOR]` to one of 00:00 UK or 07:00 UK, chosen once per
populated instance and "not re-selected at run time, per session, or to suit when an analysis
happened to finish"; a departure is "a logged non-conformance, not an anchor". **21 of the 57 gold
reports reference a 07:00 UK anchor and the rest a 00:00 UK reset.** No gold M1 instance ships with
the package, so the populated value cannot be read off. This is flagged here for Stage 1 to assess
per report, not pre-judged — whether each report handled its own anchor as a logged non-conformance
or presented it as the instance value is a Category 1 / 5.2 question for the reviewer.
