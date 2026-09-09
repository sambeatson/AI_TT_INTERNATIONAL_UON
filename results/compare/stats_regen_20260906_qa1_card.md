# baseline vs regenerated
cards paired: 162  |  report dates: 54 (effective N)
total R  baseline: -13.87   regenerated: -11.90   diff: +1.97
mean per-card diff: +0.012  median: +0.000  cards better/worse/same: 50/36/76
Wilcoxon signed-rank (non-zero diffs, n=86): W=1522  p=0.1338
sign test: 50/86 positive  p=0.1606
daily-block bootstrap of total-R difference: +1.97  95% CI [-28.02, +24.49]  P(diff<=0)=0.405  (blocks=54)
fill rate: 48.8% -> 30.9%  z=-3.29 p=0.001
Mann-Whitney on filled-card R: U=2022 p=0.8223  | win rate 30.4% -> 34.0%

by family:
| family   |   baseline |   regenerated |   diff |
|:---------|-----------:|--------------:|-------:|
| Trade 1  |      -5.7  |         -9.84 |  -4.14 |
| Trade 2  |      -2.88 |         -2.71 |   0.17 |
| Trade 3  |       0.35 |          0    |  -0.35 |
| Trade 3A |      -4.72 |          1.48 |   6.2  |
| Trade 3B |       0    |          0.17 |   0.17 |
| Trade 3C |      -0.93 |         -1    |  -0.07 |

by month:
| m       |   baseline |   regenerated |   diff |
|:--------|-----------:|--------------:|-------:|
| 2026-05 |      11.07 |          1.79 |  -9.29 |
| 2026-06 |     -15.76 |         -8.5  |   7.27 |
| 2026-07 |      -9.18 |         -5.19 |   3.99 |
