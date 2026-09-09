# baseline vs regenerated
cards paired: 162  |  report dates: 54 (effective N)
total R  baseline: -5.03   regenerated: -17.88   diff: -12.85
mean per-card diff: -0.079  median: +0.000  cards better/worse/same: 36/37/89
Wilcoxon signed-rank (non-zero diffs, n=73): W=1332  p=0.9187
sign test: 36/73 positive  p=1.0000
daily-block bootstrap of total-R difference: -12.85  95% CI [-59.43, +20.29]  P(diff<=0)=0.697  (blocks=54)
fill rate: 43.8% -> 31.5%  z=-2.29 p=0.022
Mann-Whitney on filled-card R: U=1936 p=0.4943  | win rate 36.6% -> 31.4%

by family:
| family   |   baseline |   regenerated |   diff |
|:---------|-----------:|--------------:|-------:|
| Trade 1  |      -6.1  |        -12.29 |  -6.19 |
| Trade 2  |      -1.07 |         -6.26 |  -5.19 |
| Trade 3  |       0.41 |          0    |  -0.41 |
| Trade 3A |       2.91 |          0.83 |  -2.08 |
| Trade 3B |       0    |          0.84 |   0.84 |
| Trade 3C |      -1.18 |         -1    |   0.18 |

by month:
| m       |   baseline |   regenerated |   diff |
|:--------|-----------:|--------------:|-------:|
| 2026-05 |      20.28 |          0.84 | -19.44 |
| 2026-06 |     -13.87 |        -13.61 |   0.26 |
| 2026-07 |     -11.44 |         -5.12 |   6.33 |
