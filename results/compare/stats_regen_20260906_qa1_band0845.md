# baseline vs regenerated
cards paired: 162  |  report dates: 54 (effective N)
total R  baseline: -9.49   regenerated: -20.17   diff: -10.68
mean per-card diff: -0.066  median: +0.000  cards better/worse/same: 39/34/89
Wilcoxon signed-rank (non-zero diffs, n=73): W=1270  p=0.6552
sign test: 39/73 positive  p=0.6400
daily-block bootstrap of total-R difference: -10.68  95% CI [-57.15, +22.31]  P(diff<=0)=0.655  (blocks=54)
fill rate: 43.8% -> 31.5%  z=-2.29 p=0.022
Mann-Whitney on filled-card R: U=1936 p=0.4943  | win rate 31.0% -> 25.5%

by family:
| family   |   baseline |   regenerated |   diff |
|:---------|-----------:|--------------:|-------:|
| Trade 1  |      -6.82 |        -12.96 |  -6.14 |
| Trade 2  |      -2.67 |         -6.61 |  -3.94 |
| Trade 3  |       0.48 |          0    |  -0.48 |
| Trade 3A |       0.71 |          0.23 |  -0.48 |
| Trade 3B |       0    |          0.17 |   0.17 |
| Trade 3C |      -1.18 |         -1    |   0.18 |

by month:
| m       |   baseline |   regenerated |   diff |
|:--------|-----------:|--------------:|-------:|
| 2026-05 |      19.28 |          0.84 | -18.44 |
| 2026-06 |     -16.52 |        -14.62 |   1.9  |
| 2026-07 |     -12.24 |         -6.38 |   5.86 |
