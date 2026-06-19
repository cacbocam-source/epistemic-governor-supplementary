"""
Figure 5 — Reference Implementation Phase Map with Audit Trail
Horizontal phase map showing PCR execution phases for the Zhu et al. (2025)
reference implementation. Annotates flagged claim and Epistemic Governor outcome.
Output: figure5_phase_map.tiff — 600 dpi, LZW, BMC/Springer Nature spec.
"""

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10.0, 5.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

C_PHASE   = ['#1a5276', '#117a65', '#7d6608', '#922b21', '#6c3483']
C_FLAG    = '#c0392b'
C_PASS    = '#1e8449'
C_ARROW   = '#5d6d7e'
C_NOTE    = '#2c3e50'

PHASES = [
    (1,  'Phase 1\nPrompt\nConstruction',    'Human Orchestrator\nassigns claims'),
    (3,  'Phase 2\nLLM\nGeneration',         'Draft prose output\n(Analyst Agent)'),
    (5,  'Phase 3\nAdversarial\nRetrieval',  'Skeptic Agent\nTemp=.70'),
    (7,  'Phase 4\nΦ\nComputation',          'all-mpnet-base-v2\n768-D cosine sim'),
    (9,  'Phase 5\nEpistemic\nGovernor',     'Adjudication\nΦ = 0.5963 < τ = .70'),
    (11, 'Phase 6\nVerified\nOutput',        'Claim quarantined\nor approved'),
]

for i, (x, phase_label, sub_label) in enumerate(PHASES):
    color = C_PHASE[i % len(C_PHASE)]
    if i == 4:
        color = C_FLAG
    elif i == 5:
        color = C_PASS

    box = mpatches.FancyBboxPatch((x - 0.85, 2.8), 1.7, 1.8,
                                   boxstyle="round,pad=0.10",
                                   facecolor=color, edgecolor='white',
                                   linewidth=1.5, alpha=0.88, zorder=4)
    ax.add_patch(box)
    ax.text(x, 3.95, phase_label, ha='center', va='center',
            fontsize=8.0, color='white', fontweight='bold', linespacing=1.3, zorder=5)
    ax.text(x, 3.05, sub_label, ha='center', va='center',
            fontsize=6.8, color='white', alpha=0.90, linespacing=1.25, zorder=5)

    if i < len(PHASES) - 1:
        ax.annotate('', xy=(x + 0.95, 3.7), xytext=(x + 0.85, 3.7),
                    arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.3, mutation_scale=12),
                    zorder=6)

# Φ gauge bar below
ax.text(1.0, 2.5, 'Fidelity Index (Φ):', ha='left', va='top',
        fontsize=8.5, color=C_NOTE, fontweight='semibold')
bar_y = 2.0
bar_bg = mpatches.FancyBboxPatch((1.0, bar_y), 10.0, 0.35,
                                  boxstyle="round,pad=0.04",
                                  facecolor='#ecf0f1', edgecolor='#bdc3c7',
                                  linewidth=0.8, zorder=3)
ax.add_patch(bar_bg)
# Fill to Phi=0.5963 position (out of 1.0 across 10 units width)
phi_width = 10.0 * 0.5963
bar_fill = mpatches.FancyBboxPatch((1.0, bar_y), phi_width, 0.35,
                                    boxstyle="round,pad=0.04",
                                    facecolor=C_FLAG, edgecolor='none',
                                    linewidth=0, alpha=0.75, zorder=4)
ax.add_patch(bar_fill)
tau_x = 1.0 + 10.0 * 0.70
ax.axvline(x=tau_x, ymin=(bar_y)/6, ymax=(bar_y+0.35)/6,
           color=C_FLAG, linewidth=2.0, linestyle='--', zorder=5)
ax.text(tau_x + 0.05, bar_y + 0.40, 'τ = .70', fontsize=7.5, color=C_FLAG,
        fontstyle='italic', fontweight='semibold')
ax.text(1.0 + phi_width/2, bar_y + 0.175, 'Φ = 0.5963',
        ha='center', va='center', fontsize=7.5, color='white', fontweight='bold', zorder=6)

for tick_v in [0.0, 0.25, 0.50, 0.75, 1.00]:
    tx = 1.0 + 10.0 * tick_v
    ax.text(tx, bar_y - 0.12, f'{tick_v:.2f}', ha='center', va='top', fontsize=6.8, color='#7f8c8d')

# Outcome annotation
ax.text(6.0, 1.45, '→  Φ = 0.5963 < τ = .70  |  Fabricated attribution flagged  |  Claim quarantined before manuscript insertion',
        ha='center', va='center', fontsize=8.0, color=C_FLAG, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fdf2f2', edgecolor=C_FLAG, linewidth=0.8))

# Source note
ax.text(6.0, 0.75, 'Reference claim: "...AI integration generates what Zhu et al. (2025) specifically categorize as a teaching profession crisis..."',
        ha='center', va='center', fontsize=7.2, color='#7f8c8d', fontstyle='italic')
ax.text(6.0, 0.35, 'Source: Zhu H, Sun Y, Yang J (2025) Humanit Soc Sci Commun 12:1111 | PCR Master Execution Ledger, March 2026',
        ha='center', va='center', fontsize=6.8, color='#95a5a6')

ax.text(6.0, 5.7, 'PCR Reference Implementation — Phase Map with Audit Trail',
        ha='center', va='top', fontsize=11.5, color='#2c3e50', fontweight='bold')

output_dir = Path(__file__).resolve().parent.parent / '_02_Figures_TIFF'
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'figure5_phase_map.tiff'
fig.savefig(output_path, dpi=600, format='tiff', bbox_inches='tight',
            facecolor='white', pil_kwargs={'compression': 'tiff_lzw'})
plt.close(fig)
print(f"Saved: {output_path}")
