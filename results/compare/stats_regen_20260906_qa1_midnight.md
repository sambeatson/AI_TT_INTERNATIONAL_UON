# baseline vs regenerated
cards paired: 162  |  report dates: 54 (effective N)
total R  baseline: -17.73   regenerated: -8.56   diff: +9.17
mean per-card diff: +0.057  median: +0.000  cards better/worse/same: 55/32/75
Wilcoxon signed-rank (non-zero diffs, n=87): W=1400  p=0.0294
sign test: 55/87 positive  p=0.0178
daily-block bootstrap of total-R difference: +9.17  95% CI [-8.54, +24.97]  P(diff<=0)=0.138  (blocks=54)
fill rate: 48.8% -> 30.9%  z=-3.29 p=0.001
Mann-Whitney on filled-card R: U=1920 p=0.7886  | win rate 29.1% -> 38.0%

by family:
| family   |   baseline |   regenerated |   diff |
|:---------|-----------:|--------------:|-------:|
| Trade 1  |      -6.31 |         -6.78 |  -0.48 |
| Trade 2  |      -8.39 |         -1.06 |   7.33 |
| Trade 3  |       0.48 |          0    |  -0.48 |
| Trade 3A |      -3.06 |          0.11 |   3.17 |
| Trade 3B |       0    |          0.17 |   0.17 |
| Trade 3C |      -0.46 |         -1    |  -0.54 |

by month:
| m       |   baseline |   regenerated |   diff |
|:--------|-----------:|--------------:|-------:|
| 2026-05 |       5.03 |          1.71 |  -3.32 |
| 2026-06 |     -12.05 |         -6.63 |   5.42 |
| 2026-07 |     -10.72 |         -3.64 |   7.08 |
