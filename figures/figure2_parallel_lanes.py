"""
Figure 2 — PCR Three-Lane Parallel Agent Architecture
Conceptual diagram showing the Parallel Cognitive Router's three simultaneous
processing lanes: Analyst Agent, Skeptic Agent, and Epistemic Governor.
Output: figure2_parallel_lanes.tiff — 600 dpi, LZW, BMC/Springer Nature spec.
"""

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9.0, 6.0))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

C_ANALYST  = '#1a5276'
C_SKEPTIC  = '#922b21'
C_GOVERNOR = '#7d6608'
C_INPUT    = '#2c3e50'
C_OUTPUT   = '#1e8449'
C_ARROW    = '#5d6d7e'
C_LANE_BG  = '#f8f9fa'

def draw_box(ax, x, y, w, h, label, sublabel, color, fontsize=9.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                         facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.88, zorder=4)
    ax.add_patch(box)
    ax.text(x + w/2, y + h*0.62, label, ha='center', va='center',
            fontsize=fontsize, color='white', fontweight='bold', zorder=5)
    if sublabel:
        ax.text(x + w/2, y + h*0.28, sublabel, ha='center', va='center',
                fontsize=7.2, color='white', alpha=0.88, zorder=5)

def arrow(ax, x1, y1, x2, y2, color='#5d6d7e'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.4, mutation_scale=14),
                zorder=6)

# Lane backgrounds
for lane_y, lane_color, lane_label, label_color in [
    (4.6, '#eaf2ff', 'Lane 1 — Analyst Agent', C_ANALYST),
    (2.8, '#fdf2f2', 'Lane 2 — Skeptic Agent', C_SKEPTIC),
    (1.0, '#fefde7', 'Lane 3 — Epistemic Governor', C_GOVERNOR),
]:
    rect = mpatches.FancyBboxPatch((1.2, lane_y), 6.2, 1.5,
                                    boxstyle="round,pad=0.05",
                                    facecolor=lane_color, edgecolor='#dde0e3',
                                    linewidth=0.8, zorder=2)
    ax.add_patch(rect)
    ax.text(1.35, lane_y + 1.25, lane_label, ha='left', va='top',
            fontsize=7.8, color=label_color, fontstyle='italic', zorder=3)

# Input node
draw_box(ax, 0.1, 2.8, 1.0, 1.5, 'Input\nText', 'Draft Prose', C_INPUT, fontsize=8.5)

# Analyst lane
draw_box(ax, 1.5, 4.75, 1.6, 1.1, 'Analyst', 'Syntax + Structure', C_ANALYST)
draw_box(ax, 3.4, 4.75, 1.6, 1.1, 'Source\nRetrieval', 'DOI Crossref', C_ANALYST)
draw_box(ax, 5.3, 4.75, 1.6, 1.1, 'Analyst\nReport', '', C_ANALYST)

# Skeptic lane
draw_box(ax, 1.5, 2.95, 1.6, 1.1, 'Skeptic', 'Adversarial\nTemp=.70', C_SKEPTIC)
draw_box(ax, 3.4, 2.95, 1.6, 1.1, 'Φ\nComputation', 'all-mpnet-base-v2', C_SKEPTIC)
draw_box(ax, 5.3, 2.95, 1.6, 1.1, 'Friction\nReport', 'Φ vs. τ=.70', C_SKEPTIC)

# Governor lane
draw_box(ax, 1.5, 1.15, 1.6, 1.1, 'Epistemic\nGovernor', 'Adjudication', C_GOVERNOR)
draw_box(ax, 3.4, 1.15, 1.6, 1.1, 'Constraint\nAudit', 'MED Detection', C_GOVERNOR)
draw_box(ax, 5.3, 1.15, 1.6, 1.1, 'Governance\nDecision', '', C_GOVERNOR)

# Arrows within lanes
for y_center in [5.30, 3.50, 1.70]:
    arrow(ax, 3.1, y_center, 3.4, y_center, C_ARROW)
    arrow(ax, 5.0, y_center, 5.3, y_center, C_ARROW)

# Fan out from input
for y_target in [5.30, 3.50, 1.70]:
    arrow(ax, 1.1, 3.55, 1.5, y_target, C_INPUT)

# Convergence arrows to orchestrator
for y_source in [5.30, 3.50, 1.70]:
    arrow(ax, 6.9, y_source, 7.3, 3.55, C_ARROW)

# Orchestrator / output
draw_box(ax, 7.3, 2.8, 1.5, 1.5, 'Human\nOrchestrator', 'Final Decision', C_OUTPUT, fontsize=8.5)
arrow(ax, 8.8, 3.55, 9.1, 3.55, C_OUTPUT)
draw_box(ax, 9.1, 2.95, 0.8, 1.1, 'Verified\nOutput', '', C_OUTPUT, fontsize=7.5)

# PCR label
ax.text(5.0, 6.75, 'Parallel Cognitive Router (PCR) — Three-Lane Architecture',
        ha='center', va='top', fontsize=11.5, color='#2c3e50', fontweight='bold')

output_dir = Path(__file__).resolve().parent.parent / '_02_Figures_TIFF'
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'figure2_parallel_lanes.tiff'
fig.savefig(output_path, dpi=600, format='tiff', bbox_inches='tight',
            facecolor='white', pil_kwargs={'compression': 'tiff_lzw'})
plt.close(fig)
print(f"Saved: {output_path}")
