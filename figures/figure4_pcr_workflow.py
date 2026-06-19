"""
Figure 4 — PCR Operational Swimlane Workflow
Four-swimlane diagram: Human Orchestrator, Analyst Agent, Skeptic Agent,
Epistemic Governor. Shows operational sequence and decision points.
Output: figure4_pcr_workflow.tiff — 600 dpi, LZW, BMC/Springer Nature spec.
"""

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10.0, 7.0))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

C_ORCH     = '#2c3e50'
C_ANALYST  = '#1a5276'
C_SKEPTIC  = '#922b21'
C_GOVERNOR = '#7d6608'
C_DECISION = '#1e8449'
C_ARROW    = '#7f8c8d'

LANES = [
    (6.0, 7.2, C_ORCH,     'Human Orchestrator'),
    (4.5, 5.7, C_ANALYST,  'Analyst Agent'),
    (3.0, 4.2, C_SKEPTIC,  'Skeptic Agent'),
    (1.5, 2.7, C_GOVERNOR, 'Epistemic Governor'),
]

for y_bot, y_top, color, label in LANES:
    rect = mpatches.FancyBboxPatch((0.5, y_bot), 11.0, y_top - y_bot,
                                    boxstyle="square,pad=0",
                                    facecolor=color, edgecolor='white',
                                    linewidth=1.5, alpha=0.10, zorder=1)
    ax.add_patch(rect)
    ax.text(0.62, (y_bot + y_top) / 2, label, ha='left', va='center',
            fontsize=8.5, color=color, fontweight='bold', rotation=0, zorder=3)

def box(ax, x, y, w, h, text, color, fontsize=8.0):
    b = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                 boxstyle="round,pad=0.06",
                                 facecolor=color, edgecolor='white',
                                 linewidth=1.2, alpha=0.85, zorder=4)
    ax.add_patch(b)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=fontsize, color='white', fontweight='semibold', zorder=5)

def diamond(ax, x, y, size, text, color):
    d = mpatches.FancyBboxPatch((x - size, y - size*0.6), size*2, size*1.2,
                                 boxstyle="round,pad=0.04",
                                 facecolor=color, edgecolor='white',
                                 linewidth=1.0, alpha=0.80, zorder=4)
    ax.add_patch(d)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=7.2, color='white', fontweight='bold', zorder=5)

def arr(ax, x1, y1, x2, y2, label='', color=C_ARROW):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2, mutation_scale=12), zorder=6)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.08, my, label, fontsize=7.0, color=color, va='center')

# Phase labels
for px, label in [(2.2,'Phase 1'), (4.5,'Phase 2'), (6.8,'Phase 3'), (9.2,'Phase 4'), (11.0,'Phase 5')]:
    ax.text(px, 7.55, label, ha='center', va='center', fontsize=7.5,
            color='#95a5a6', fontstyle='italic')

# Orchestrator lane
box(ax, 2.2, 6.6, 1.5, 0.70, 'Assign\nManuscript', C_ORCH)
box(ax, 4.5, 6.6, 1.5, 0.70, 'Route to\nPCR Agents', C_ORCH)
box(ax, 9.2, 6.6, 1.5, 0.70, 'Review\nFriction Report', C_ORCH)
box(ax, 11.0, 6.6, 1.2, 0.70, 'Approve /\nRevise', C_DECISION)

# Analyst lane
box(ax, 4.5, 5.1, 1.5, 0.70, 'Parse Syntax\n& Claims', C_ANALYST)
box(ax, 6.8, 5.1, 1.5, 0.70, 'Retrieve\nSource DOIs', C_ANALYST)
box(ax, 8.2, 5.1, 1.5, 0.70, 'Analyst\nReport', C_ANALYST)

# Skeptic lane
box(ax, 6.8, 3.6, 1.5, 0.70, 'Adversarial\nRetrieval', C_SKEPTIC)
box(ax, 8.2, 3.6, 1.5, 0.70, 'Compute Φ\n(cosine sim)', C_SKEPTIC)
diamond(ax, 9.6, 3.6, 0.80, 'Φ ≥ τ\n(.70)?', C_SKEPTIC)

# Governor lane
box(ax, 9.6, 2.1, 1.5, 0.70, 'Adjudicate\nDrifted Claim', C_GOVERNOR)
box(ax, 11.0, 2.1, 1.2, 0.70, 'Quarantine\nClaim', C_GOVERNOR)

# Arrows
arr(ax, 2.95, 6.6, 3.72, 6.6)
arr(ax, 5.25, 6.6, 10.25, 6.6)
arr(ax, 9.95, 6.6, 10.35, 6.6)
arr(ax, 4.5, 6.25, 4.5, 5.45)
arr(ax, 5.25, 5.1, 6.05, 5.1)
arr(ax, 7.55, 5.1, 7.45, 5.1)
arr(ax, 8.95, 5.1, 9.2, 6.25)
arr(ax, 6.8, 5.75, 6.8, 5.45)   # orch to analyst
arr(ax, 6.8, 4.75, 6.8, 3.95)
arr(ax, 7.55, 3.6, 7.45, 3.6)
arr(ax, 8.95, 3.6, 8.8, 3.6)
arr(ax, 9.6, 3.25, 9.6, 2.45)   # fail path
arr(ax, 10.35, 2.1, 10.35, 2.1)
arr(ax, 10.4, 2.1, 10.4, 2.1)

ax.text(9.75, 2.92, 'Φ < τ\n(FLAG)', fontsize=7.0, color=C_GOVERNOR, va='center')
ax.text(10.2, 3.72, 'Φ ≥ τ\n(PASS)', fontsize=7.0, color=C_DECISION, va='center')
arr(ax, 10.4, 3.6, 11.0, 6.25, color=C_DECISION)

ax.text(6.0, 7.82, 'PCR Operational Workflow — Swimlane View',
        ha='center', va='top', fontsize=11.5, color='#2c3e50', fontweight='bold')

output_dir = Path(__file__).resolve().parent.parent / '_02_Figures_TIFF'
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'figure4_pcr_workflow.tiff'
fig.savefig(output_path, dpi=600, format='tiff', bbox_inches='tight',
            facecolor='white', pil_kwargs={'compression': 'tiff_lzw'})
plt.close(fig)
print(f"Saved: {output_path}")
