# baseline vs regenerated
cards paired: 162  |  report dates: 54 (effective N)
total R  baseline: -14.48   regenerated: -16.13   diff: -1.65
mean per-card diff: -0.010  median: +0.000  cards better/worse/same: 50/37/75
Wilcoxon signed-rank (non-zero diffs, n=87): W=1596  p=0.1785
sign test: 50/87 positive  p=0.1980
daily-block bootstrap of total-R difference: -1.65  95% CI [-35.38, +22.70]  P(diff<=0)=0.499  (blocks=54)
fill rate: 48.1% -> 30.2%  z=-3.30 p=0.001
Mann-Whitney on filled-card R: U=2037 p=0.5295  | win rate 26.9% -> 30.6%

by family:
| family   |   baseline |   regenerated |   diff |
|:---------|-----------:|--------------:|-------:|
| Trade 1  |      -8.65 |        -10.52 |  -1.87 |
| Trade 2  |      -5.46 |         -5.34 |   0.12 |
| Trade 3  |      -1    |          0    |   1    |
| Trade 3A |       1.71 |          0.56 |  -1.15 |
| Trade 3B |       0    |          0.17 |   0.17 |
| Trade 3C |      -1.09 |         -1    |   0.09 |

by month:
| m       |   baseline |   regenerated |   diff |
|:--------|-----------:|--------------:|-------:|
| 2026-05 |      13.43 |          0.3  | -13.12 |
| 2026-06 |     -16.71 |         -8.87 |   7.84 |
| 2026-07 |     -11.2  |         -7.56 |   3.64 |
