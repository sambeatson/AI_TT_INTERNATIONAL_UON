"""equity.py - equity curve(s) from one or more summary.csv files.

  python engine/equity.py --runs results/baseline_band0845/summary.csv results/regen_r1_band0845/summary.csv \
        --labels "baseline" "regenerated" --risk 2500 --account 1000000 --out results/compare/equity.png

Fixed-dollar risk per card, not compounded. Cards ordered by report_date then strategy.
Non-filled cards contribute 0R. Dark theme, 150 DPI. Never put '$' in matplotlib titles (mathtext).
"""
import argparse, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd
from matplotlib.ticker import FuncFormatter

PALETTE = ['#9ece6a', '#7aa2f7', '#e0af68', '#f7768e', '#bb9af7', '#7dcfff']

def curve(path, account, risk):
    d = pd.read_csv(path); d['blended_R'] = pd.to_numeric(d.blended_R, errors='coerce').fillna(0)
    d = d.sort_values(['report_date', 'strategy']).reset_index(drop=True)
    d['eq'] = account + (d.blended_R * risk).cumsum()
    d['dd'] = (d['eq'] - d['eq'].cummax()) / d['eq'].cummax() * 100
    return d

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs', nargs='+', required=True); ap.add_argument('--labels', nargs='+', default=None)
    ap.add_argument('--risk', type=float, default=2500); ap.add_argument('--account', type=float, default=1_000_000)
    ap.add_argument('--out', required=True); ap.add_argument('--title', default='Strategy-card forward test')
    a = ap.parse_args()
    labels = a.labels or [p.split('/')[-2] for p in a.runs]
    plt.rcParams.update({'figure.facecolor': '#11131a', 'axes.facecolor': '#11131a', 'savefig.facecolor': '#11131a',
        'text.color': '#c8d0e0', 'axes.labelcolor': '#c8d0e0', 'xtick.color': '#8b93a7', 'ytick.color': '#8b93a7',
        'axes.edgecolor': '#2a2f3d', 'grid.color': '#1c2029', 'font.size': 10, 'mathtext.default': 'regular'})
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(13, 9), height_ratios=[2.6, 1], sharex=True)
    stats = []
    for i, (p, lab) in enumerate(zip(a.runs, labels)):
        d = curve(p, a.account, a.risk); col = PALETTE[i % len(PALETTE)]
        x = pd.to_datetime(d.report_date)
        ax.plot(x, d['eq'], color=col, lw=2.2 if i == 0 else 1.5, label=f'{lab}   ({d.blended_R.sum():+.1f}R)')
        ax.annotate(f'{d["eq"].iloc[-1]/1000:.0f}k', xy=(x.iloc[-1], d["eq"].iloc[-1]), xytext=(6, 0), textcoords='offset points', color=col, fontsize=9, va='center')
        ax2.plot(x, d.dd, color=col, lw=1.2); ax2.fill_between(x, d.dd, 0, color=col, alpha=.15)
        stats.append(dict(run=lab, totR=round(d.blended_R.sum(), 2), final=round(d['eq'].iloc[-1]), maxdd=round(d.dd.min(), 1),
                          peak=round(d['eq'].max()), n=int((d.blended_R != 0).sum())))
    ax.axhline(a.account, color='#4a5163', lw=1, ls='--'); ax.grid(True, alpha=.5, lw=.6); ax2.grid(True, alpha=.5, lw=.6)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v/1e6:.2f}M')); ax2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:.0f}%'))
    ax.set_ylabel('Account equity'); ax2.set_ylabel('Drawdown'); ax2.set_xlabel('Report date')
    ax.set_title(f'{a.title}\nUSD {a.account:,.0f} account  ·  fixed {a.risk:,.0f} risk per card ({a.risk/a.account*100:.2f}%)  ·  R blended across 3 units',
                 color='#e6ebf5', fontsize=13, pad=14, loc='left')
    ax.legend(frameon=False, loc='lower left', fontsize=9)
    for a_ in (ax, ax2):
        for sp in ('top', 'right'): a_.spines[sp].set_visible(False)
    plt.tight_layout(); plt.savefig(a.out, dpi=150)
    S = pd.DataFrame(stats); S.to_csv(a.out.replace('.png', '_stats.csv'), index=False); print(S.to_string(index=False))

if __name__ == '__main__':
    main()
