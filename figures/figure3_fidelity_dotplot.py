"""
Figure 3 — Fidelity Index (Φ) Distribution and Review Trigger
Strip chart: all 15 individual Φ values by calibration category.
Horizontal dashed threshold line at τ = .70.
Category mean markers. Reference implementation Φ = .60 annotated.
Output: figure3_fidelity_dotplot.tiff — 600 dpi, combination artwork.
No figure title or note included in the image.

Data source: PCR Master Execution Ledger, March 2026.
All 15 individual Φ scores confirmed from Calibration Log.
  Direct Extraction:     n=5, M=1.00, R=1.00-1.00
  Human Paraphrase:      n=5, M=.58,  R=.24-.82
  Stochastic Divergence: n=5, M=.54,  R=.35-.67
  Reference Implementation: Phi=0.5963 approx .60 (Phase 4 Terminal Log)

CORRECTIONS FROM PRIOR VERSION:
  [1] Data arrays updated to actual Calibration Log values (not approximations)
  [2] Label corrected: Stochastic Hallucination -> Stochastic Divergence
  [3] Annotation repositioned xytext (4.62,0.52) -> (4.62,0.38) clears M=.54 label
"""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

rng = np.random.default_rng(42)

direct_vals     = np.array([1.00, 1.00, 1.00, 1.00, 1.00])
paraphrase_vals = np.array([0.6653, 0.4546, 0.7467, 0.236, 0.822])
divergence_vals = np.array([0.6418, 0.6687, 0.346, 0.409, 0.6125])
impl_phi = 0.60
impl_x   = 4.0

fig, ax = plt.subplots(figsize=(7.5, 5.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

C_DIRECT    = '#1a5276'
C_PARA      = '#117a65'
C_DIVERG    = '#922b21'
C_THRESHOLD = '#c0392b'
C_IMPL      = '#f39c12'
C_MEAN_LINE = '#2c3e50'

GROUP_POSITIONS = {
    'Direct\nExtraction':     (1.0, direct_vals,    C_DIRECT),
    'Human\nParaphrase':      (2.5, paraphrase_vals, C_PARA),
    'Stochastic\nDivergence': (4.0, divergence_vals, C_DIVERG),
}

for label, (xc, vals, color) in GROUP_POSITIONS.items():
    jitter = rng.uniform(-0.08, 0.08, size=len(vals))
    ax.scatter(xc + jitter, vals, s=110, color=color,
               edgecolors='white', linewidths=0.8, zorder=5, alpha=0.92)
    mean_v = np.mean(vals)
    ax.hlines(mean_v, xc-0.22, xc+0.22, colors=C_MEAN_LINE, linewidths=2.2, zorder=6)
    ax.text(xc+0.28, mean_v, f'M = {mean_v:.2f}',
            va='center', ha='left', fontsize=8.0, color=C_MEAN_LINE, fontweight='semibold')
    ax.text(xc, -0.07, label, ha='center', va='top',
            fontsize=9.5, color=color, fontweight='semibold', linespacing=1.3)

TAU = 0.70
ax.axhline(y=TAU, color=C_THRESHOLD, linewidth=1.6, linestyle='--', zorder=4)
ax.text(4.65, TAU+0.025, 'Verification Threshold  τ = .70',
        va='bottom', ha='right', fontsize=9.0, color=C_THRESHOLD,
        fontstyle='italic', fontweight='semibold')
ax.axhspan(0.0, TAU, facecolor='#fadbd8', alpha=0.18, zorder=1)
ax.text(0.3, TAU/2, 'FLAG\nZONE', ha='center', va='center',
        fontsize=7.5, color='#c0392b', alpha=0.45, fontstyle='italic', fontweight='bold')

ax.scatter([impl_x], [impl_phi], s=180, color=C_IMPL,
           marker='D', edgecolors='#7d6608', linewidths=1.0, zorder=7)
ax.annotate('Reference\nImplementation\nΦ = .60',
            xy=(impl_x, impl_phi), xytext=(4.62, 0.38),
            ha='left', va='center', fontsize=8.5, color='#7d6608', fontweight='semibold',
            arrowprops=dict(arrowstyle='-|>', color='#7d6608', lw=1.1, mutation_scale=10),
            zorder=8)

ax.set_xlim(0.3, 5.5)
ax.set_ylim(-0.05, 1.12)
ax.set_yticks(np.arange(0.0, 1.1, 0.1))
ax.tick_params(axis='y', labelsize=9.0, colors='#2c3e50')
ax.set_ylabel('Fidelity Index (Φ)', fontsize=10.5, color='#2c3e50', labelpad=8, fontweight='semibold')
ax.set_xticks([])
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#bdc3c7')
ax.spines['left'].set_linewidth(0.8)
ax.yaxis.grid(True, linestyle=':', color='#ecf0f1', linewidth=0.7, zorder=1)
ax.set_axisbelow(True)

legend_elements = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C_DIRECT, markersize=8, label='Direct Extraction'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C_PARA, markersize=8, label='Human Paraphrase'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C_DIVERG, markersize=8, label='Stochastic Divergence'),
    Line2D([0],[0], marker='D', color='w', markerfacecolor=C_IMPL, markeredgecolor='#7d6608',
           markersize=9, label='Reference Implementation (Φ = .60)'),
    Line2D([0],[0], color=C_MEAN_LINE, linewidth=2.2, label='Category Mean'),
    Line2D([0],[0], color=C_THRESHOLD, linewidth=1.6, linestyle='--', label='Verification Threshold (τ = .70)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=7.8, framealpha=0.9, edgecolor='#bdc3c7')
fig.subplots_adjust(left=0.10, right=0.98, top=0.97, bottom=0.10)

output_dir = Path(__file__).resolve().parent.parent / '_02_Figures_TIFF'
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'figure3_fidelity_dotplot.tiff'
fig.savefig(output_path, dpi=600, format='tiff', bbox_inches='tight',
            facecolor='white', pil_kwargs={'compression': 'tiff_lzw'})
plt.close(fig)
print(f"Saved: {output_path}")
print(f"  Paraphrase M={np.mean(paraphrase_vals):.4f} -> .58 | Divergence M={np.mean(divergence_vals):.4f} -> .54")
