"""
Figure 1 — Signal Fidelity Decay in Linear Workflows
Exponential decay curve illustrating cumulative fidelity loss across
sequential agent handoffs in a linear pipeline vs. PCR parallel architecture.
Output: figure1_signal_decay.tiff — 600 dpi, LZW, BMC/Springer Nature spec.
"""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

stages = np.array([0, 1, 2, 3, 4, 5])
labels = ['Source\nText', 'Prompt\nConstruction', 'LLM\nGeneration',
          'Context\nSynthesis', 'Draft\nOutput', 'Inserted\nText']

decay_rate = 0.28
fidelity_linear = np.exp(-decay_rate * stages)

fidelity_pcr = np.array([1.00, 0.97, 0.94, 0.92, 0.91, 0.90])

tau = 0.70

C_LINEAR = '#922b21'
C_PCR    = '#1a5276'
C_TAU    = '#c0392b'

fig, ax = plt.subplots(figsize=(8.0, 5.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

ax.plot(stages, fidelity_linear, color=C_LINEAR, linewidth=2.2, marker='o',
        markersize=7, label='Linear Workflow (sequential handoff)', zorder=5)
ax.plot(stages, fidelity_pcr, color=C_PCR, linewidth=2.2, marker='s',
        markersize=7, linestyle='--', label='PCR Architecture (parallel verification)', zorder=5)

ax.axhline(y=tau, color=C_TAU, linewidth=1.4, linestyle=':', zorder=4)
ax.text(5.05, tau + 0.02, 'τ = .70', va='bottom', ha='left',
        fontsize=8.5, color=C_TAU, fontstyle='italic', fontweight='semibold')

ax.axhspan(0.0, tau, facecolor='#fadbd8', alpha=0.15, zorder=1)
ax.text(2.5, tau / 2, 'Hallucination Risk Zone', ha='center', va='center',
        fontsize=8.0, color='#c0392b', alpha=0.40, fontstyle='italic')

cross_stage = -np.log(tau) / decay_rate
ax.axvline(x=cross_stage, color=C_LINEAR, linewidth=0.9, linestyle=':', alpha=0.6)
ax.annotate(f'Fidelity drops\nbelow τ at\nstage ≈ {cross_stage:.1f}',
            xy=(cross_stage, tau), xytext=(cross_stage + 0.4, tau - 0.15),
            fontsize=7.5, color=C_LINEAR,
            arrowprops=dict(arrowstyle='->', color=C_LINEAR, lw=0.9))

ax.set_xticks(stages)
ax.set_xticklabels(labels, fontsize=8.5)
ax.set_yticks(np.arange(0.0, 1.1, 0.1))
ax.set_ylim(-0.02, 1.10)
ax.set_xlim(-0.3, 5.5)
ax.tick_params(axis='y', labelsize=9.0, colors='#2c3e50')
ax.set_ylabel('Signal Fidelity Index (Φ)', fontsize=10.5, color='#2c3e50',
              labelpad=8, fontweight='semibold')
ax.set_xlabel('Pipeline Stage', fontsize=10.5, color='#2c3e50', labelpad=8)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#bdc3c7')
ax.spines['bottom'].set_color('#bdc3c7')
ax.yaxis.grid(True, linestyle=':', color='#ecf0f1', linewidth=0.7, zorder=1)
ax.set_axisbelow(True)

ax.legend(loc='upper right', fontsize=8.5, framealpha=0.9, edgecolor='#bdc3c7')
fig.subplots_adjust(left=0.10, right=0.97, top=0.97, bottom=0.13)

output_dir = Path(__file__).resolve().parent.parent / '_02_Figures_TIFF'
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'figure1_signal_decay.tiff'
fig.savefig(output_path, dpi=600, format='tiff', bbox_inches='tight',
            facecolor='white', pil_kwargs={'compression': 'tiff_lzw'})
plt.close(fig)
print(f"Saved: {output_path}")
