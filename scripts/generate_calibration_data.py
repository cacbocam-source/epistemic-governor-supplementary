"""
generate_calibration_data.py
Reproducible generation of Epistemic_Governor_Calibration_Matrix_TableA1.xlsx

All 15 individual Phi scores from PCR Master Execution Ledger, March 2026.
Computed by PCR_Audit_Engine.py v6.0 using all-mpnet-base-v2 (768-D, cosine similarity).
Source abstracts: Zhu et al. (2025), doi:10.1057/s41599-025-05252-6
                  Beijaard et al. (2004), doi:10.1016/j.tate.2003.07.001

Run from repository root: python3 scripts/generate_calibration_data.py
Output: data/Epistemic_Governor_Calibration_Matrix_TableA1.xlsx
"""

from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import numpy as np

DATA = [
    (1, "Direct Extraction", 1.00,
     "Artificial Intelligence in Education (AIED) is becoming increasingly influential in the educational sphere, offering significant benefits and presenting ethical risks.",
     "Zhu et al. (2025) abstract, sentence 1 — verbatim"),
    (2, "Direct Extraction", 1.00,
     "In the studies reviewed, the concept of professional identity was defined differently or not defined at all.",
     "Beijaard et al. (2004) abstract — verbatim"),
    (3, "Direct Extraction", 1.00,
     "The education dimension risks involve student homogenized development, homogeneous teaching, teaching profession crisis, deviation from educational goals, alienation of the teacher-student relationship, emotional disruption, and academic misconduct.",
     "Zhu et al. (2025) abstract, sentence 2 — verbatim"),
    (4, "Direct Extraction", 1.00,
     "It is argued that, in future research on teachers' professional identity, more attention needs to be paid to research perspectives other than the cognitive one.",
     "Beijaard et al. (2004) abstract — verbatim"),
    (5, "Direct Extraction", 1.00,
     "Risks in the society dimension consist of exacerbating the digital divide, the absence of accountability, and a conflict of interest.",
     "Zhu et al. (2025) abstract, sentence 3 — verbatim"),
    (6, "Human Paraphrase", 0.6653,
     "The integration of algorithmic systems in learning environments presents a dualistic reality of advantages and moral dangers.",
     "Zhu et al. (2025) — paraphrase of Obs. 1"),
    (7, "Human Paraphrase", 0.4546,
     "Prior literature has examined educator self-concepts, which have revealed a separation of consensus between operational definitions as highly fractured or non-existent.",
     "Beijaard et al. (2004) — paraphrase of Obs. 2"),
    (8, "Human Paraphrase", 0.7467,
     "Pedagogical dangers exist in the standardization of student progress, a crisis in teaching professions, a breakdown of relationships between teachers and students, and rampant student academic misconduct.",
     "Zhu et al. (2025) — paraphrase of Obs. 3"),
    (9, "Human Paraphrase", 0.2360,
     "Further studies must broaden the research scope beyond cognitive frameworks to incorporate alternative investigative views.",
     "Beijaard et al. (2004) — paraphrase of Obs. 4"),
    (10, "Human Paraphrase", 0.8220,
     "Vast societal hazards emanating from technology include the exacerbation of the digital resource gap, voids in liability and responsibility, and emerging conflicts of interest.",
     "Zhu et al. (2025) — paraphrase of Obs. 5"),
    (11, "Stochastic Divergence", 0.6418,
     "Among secondary agricultural educators in Alabama (N = 81), perceptions of the ethical implications of AI adoption were notably elevated, with participants reporting a mean concern level of M = 3.83 (SD = 1.09) on a 5-point Likert-type scale.",
     "LLM Phase 2 output — compared against Zhu et al. (2025) and Beijaard et al. (2004)"),
    (12, "Stochastic Divergence", 0.6687,
     "This level of apprehension is not merely incidental; it aligns with a growing body of literature documenting that AI integration in educational settings generates what Zhu et al. (2025) specifically categorize as a teaching profession crisis.",
     "LLM Phase 2 output — compared against Zhu et al. (2025) abstract"),
    (13, "Stochastic Divergence", 0.3460,
     "Zhu et al. (2025) demonstrate that the digital divide in educational AI adoption is primarily responsible for the failure of teachers to develop a cohesive professional identity, a construct established by Beijaard et al. (2004).",
     "LLM Phase 2 output — fabricated causal link across both sources"),
    (14, "Stochastic Divergence", 0.4090,
     "According to recent systematic reviews, algorithmic bias in education directly accounts for a 40% increase in academic misconduct, fundamentally altering teachers' practical knowledge.",
     "LLM Phase 2 output — unsupported quantitative claim; no source support identified"),
    (15, "Stochastic Divergence", 0.6125,
     "The integration of AIED has resolved the teaching profession crisis by automating homogeneous teaching, allowing educators to focus exclusively on professional identity formation.",
     "LLM Phase 2 output — compared against Zhu et al. (2025) abstract"),
]

REFERENCE_IMPL = {
    "claim": (
        "This level of apprehension is not merely incidental; it aligns with a growing body "
        "of literature documenting that AI integration in educational settings generates what "
        "Zhu et al. (2025) specifically categorize as a 'teaching profession crisis,' an "
        "education-dimension ethical risk in which the encroachment of algorithmic systems "
        "onto instructional roles destabilizes educators' sense of pedagogical ownership, "
        "relevance, and expertise."
    ),
    "source": "Zhu H, Sun Y, Yang J (2025) Humanit Soc Sci Commun 12:1111. doi:10.1057/s41599-025-05252-6",
    "sentences": [
        ("S1", "Artificial Intelligence in Education (AIED) is becoming increasingly influential in the educational sphere, offering significant benefits and presenting ethical risks.", "[AUTHOR ACTION: retrieve from PCR_Audit_Engine.py v6.0 Phase 4 terminal log]"),
        ("S2", "The education dimension risks involve student homogenized development, homogeneous teaching, teaching profession crisis, deviation from educational goals, alienation of the teacher-student relationship, emotional disruption, and academic misconduct.", "[AUTHOR ACTION: retrieve from PCR_Audit_Engine.py v6.0 Phase 4 terminal log]"),
        ("S3", "Risks in the society dimension consist of exacerbating the digital divide, the absence of accountability, and a conflict of interest.", "[AUTHOR ACTION: retrieve from PCR_Audit_Engine.py v6.0 Phase 4 terminal log]"),
    ],
    "composite_phi": 0.5963,
    "tau": 0.70,
    "outcome": "FLAGGED — Fabricated causal attribution confirmed; claim quarantined before manuscript insertion",
}

H_FILL = PatternFill("solid", start_color="1F4E79", end_color="1F4E79")
CAT_FILLS = {
    "Direct Extraction":    PatternFill("solid", start_color="D6EAF8", end_color="D6EAF8"),
    "Human Paraphrase":     PatternFill("solid", start_color="D5F5E3", end_color="D5F5E3"),
    "Stochastic Divergence":PatternFill("solid", start_color="FDECEA", end_color="FDECEA"),
}
SUM_FILL = PatternFill("solid", start_color="F2F3F4", end_color="F2F3F4")
BD = Side(style="thin", color="000000")
ALL_BD = Border(top=BD, bottom=BD, left=BD, right=BD)
ARIAL = "Arial"

wb = Workbook()
ws1 = wb.active
ws1.title = "Calibration_Matrix"

headers = ["Obs.", "Category", "Φ Score", "Claim Text", "Source Text"]
ws1.append(headers)
for c, h in enumerate(headers, 1):
    cell = ws1.cell(1, c)
    cell.font = Font(name=ARIAL, bold=True, color="FFFFFF", size=11)
    cell.fill = H_FILL
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = ALL_BD

for row in DATA:
    obs, cat, phi, claim, source = row
    ws1.append([obs, cat, phi, claim, source])
    r = ws1.max_row
    fill = CAT_FILLS.get(cat)
    for c in range(1, 6):
        cell = ws1.cell(r, c)
        cell.font = Font(name=ARIAL, size=10)
        cell.border = ALL_BD
        cell.alignment = Alignment(wrap_text=True, vertical="top",
                                   horizontal="center" if c in (1, 3) else "left")
        if fill:
            cell.fill = fill
    ws1.cell(r, 3).number_format = "0.0000"

ws1.append([])
sum_start = ws1.max_row + 1
ws1.cell(sum_start, 1, "SUMMARY").font = Font(name=ARIAL, bold=True, size=11)
ws1.cell(sum_start, 2, "Category").font = Font(name=ARIAL, bold=True)
ws1.cell(sum_start, 3, "n").font = Font(name=ARIAL, bold=True)
ws1.cell(sum_start, 4, "Mean Φ (formula)").font = Font(name=ARIAL, bold=True)
ws1.cell(sum_start, 5, "Min Φ").font = Font(name=ARIAL, bold=True)

cats_summary = [
    ("Direct Extraction",    "C2:C6"),
    ("Human Paraphrase",     "C7:C11"),
    ("Stochastic Divergence","C12:C16"),
]
for i, (cat, rng) in enumerate(cats_summary):
    r = sum_start + 1 + i
    ws1.cell(r, 2, cat).font = Font(name=ARIAL, size=10)
    ws1.cell(r, 3, 5).font = Font(name=ARIAL, size=10)
    ws1.cell(r, 3).alignment = Alignment(horizontal="center")
    ws1.cell(r, 4, f"=AVERAGE({rng})").number_format = "0.0000"
    ws1.cell(r, 4).font = Font(name=ARIAL, size=10)
    ws1.cell(r, 4).alignment = Alignment(horizontal="center")
    ws1.cell(r, 5, f"=MIN({rng})").number_format = "0.0000"
    ws1.cell(r, 5).font = Font(name=ARIAL, size=10)
    ws1.cell(r, 5).alignment = Alignment(horizontal="center")
    for c in range(1, 6):
        ws1.cell(r, c).fill = SUM_FILL
        ws1.cell(r, c).border = ALL_BD

note_r = ws1.max_row + 2
note_text = (
    "Note. \u03A6 computed by PCR_Audit_Engine.py v6.0 using all-mpnet-base-v2 "
    "(Reimers & Gurevych 2019; 768-D embeddings, mean pooling, cosine similarity). "
    "\u03C4 = .70 verification threshold. Source: PCR Master Execution Ledger, March 2026. "
    "Published dataset: Lindner JR, Clemons CA, McKibben JD (2026) AAD 7(2):109\u2013124. "
    "doi:10.37433/aad.v7i2.637. The value N=81, M=3.83, SD=1.09 reflects "
    "a retained pre-publication aggregate from the Phase 1 dataset, later superseded by "
    "the published aggregate N=80, M=3.82, SD=1.07 after one incomplete response was excluded. "
    "This note clarifies provenance only and does not alter the manuscript's statistical reporting."
)
ws1.cell(note_r, 1, note_text).font = Font(name=ARIAL, size=9, italic=True)
ws1.merge_cells(f"A{note_r}:E{note_r}")
ws1.cell(note_r, 1).alignment = Alignment(wrap_text=True)
ws1.row_dimensions[note_r].height = 60

ws1.column_dimensions["A"].width = 6
ws1.column_dimensions["B"].width = 22
ws1.column_dimensions["C"].width = 12
ws1.column_dimensions["D"].width = 62
ws1.column_dimensions["E"].width = 45
ws1.row_dimensions[1].height = 28

ws2 = wb.create_sheet("Reference_Implementation")
ws2["A1"] = "PCR Reference Implementation — Symmetric Chunking Fidelity Scoring"
ws2["A1"].font = Font(name=ARIAL, bold=True, size=13)
ws2.merge_cells("A1:E1")

ws2["A2"] = "Drifted Claim (Phase 2 — LLM Output, Flagged Sentence):"
ws2["A2"].font = Font(name=ARIAL, bold=True, size=11)
ws2.merge_cells("A2:E2")

ws2["A3"] = REFERENCE_IMPL["claim"]
ws2["A3"].font = Font(name=ARIAL, italic=True, size=10)
ws2["A3"].alignment = Alignment(wrap_text=True)
ws2.merge_cells("A3:E3")
ws2.row_dimensions[3].height = 72

ws2["A4"] = f"Source: {REFERENCE_IMPL['source']}"
ws2["A4"].font = Font(name=ARIAL, size=10)
ws2.merge_cells("A4:E4")
ws2.row_dimensions[4].height = 20

ws2.append([])

h2_row = 6
h2_hdrs = ["Atomic Sentence", "Sentence Text (verbatim from abstract)", "Φi", "Status vs. τ = .70", "Notes"]
for c, h in enumerate(h2_hdrs, 1):
    cell = ws2.cell(h2_row, c)
    cell.value = h
    cell.font = Font(name=ARIAL, bold=True, color="FFFFFF", size=10)
    cell.fill = H_FILL
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = ALL_BD

for label, text, phi_note in REFERENCE_IMPL["sentences"]:
    ws2.append([label, text, phi_note, "[< .70 or >= .70]", "Zhu et al. (2025)"])
    r = ws2.max_row
    for c in range(1, 6):
        ws2.cell(r, c).border = ALL_BD
        ws2.cell(r, c).alignment = Alignment(wrap_text=True, vertical="top",
                                             horizontal="center" if c in (1, 3, 4) else "left")
        ws2.cell(r, c).font = Font(name=ARIAL, size=10)
    ws2.row_dimensions[r].height = 48

comp_row = ws2.max_row + 1
ws2.cell(comp_row, 1, "Composite").font = Font(name=ARIAL, bold=True, size=10)
ws2.cell(comp_row, 2, "max(Φi) across all atomic sentences").font = Font(name=ARIAL, italic=True, size=10)
ws2.cell(comp_row, 3, f"{REFERENCE_IMPL['composite_phi']:.4f}").font = Font(name=ARIAL, bold=True, size=11)
ws2.cell(comp_row, 4, "FLAGGED").font = Font(name=ARIAL, bold=True, size=11, color="992211")
ws2.cell(comp_row, 5, "Φ = 0.5963 < τ = .70 → routed to Epistemic Governor").font = Font(name=ARIAL, size=9)
flag_fill = PatternFill("solid", start_color="FCF3CF", end_color="FCF3CF")
for c in range(1, 6):
    ws2.cell(comp_row, c).fill = flag_fill
    ws2.cell(comp_row, c).border = ALL_BD
    ws2.cell(comp_row, c).alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[comp_row].height = 22

outcome_row = comp_row + 2
ws2.cell(outcome_row, 1, "Outcome:").font = Font(name=ARIAL, bold=True)
ws2.cell(outcome_row, 2, REFERENCE_IMPL["outcome"]).font = Font(name=ARIAL, size=10)
ws2.merge_cells(f"B{outcome_row}:E{outcome_row}")
ws2.cell(outcome_row, 2).alignment = Alignment(wrap_text=True)
ws2.row_dimensions[outcome_row].height = 20

action_row = outcome_row + 1
ws2.cell(action_row, 1, "AUTHOR ACTION:").font = Font(name=ARIAL, bold=True, color="992211")
ws2.cell(action_row, 2,
    "Run PCR_Audit_Engine.py v6.0 to retrieve individual Φi per sentence. "
    "Script: /03_Adversarial_Friction_Logs/2_PCR_Audit_Engine.py"
).font = Font(name=ARIAL, size=9, italic=True)
ws2.merge_cells(f"B{action_row}:E{action_row}")
ws2.cell(action_row, 2).alignment = Alignment(wrap_text=True)
ws2.row_dimensions[action_row].height = 24

ws2.column_dimensions["A"].width = 14
ws2.column_dimensions["B"].width = 58
ws2.column_dimensions["C"].width = 28
ws2.column_dimensions["D"].width = 24
ws2.column_dimensions["E"].width = 32

paraphrase = np.array([0.6653, 0.4546, 0.7467, 0.236, 0.822])
divergence = np.array([0.6418, 0.6687, 0.346, 0.409, 0.6125])
direct     = np.array([1.00, 1.00, 1.00, 1.00, 1.00])

print(f"Verification:")
print(f"  Direct Extraction:     M={np.mean(direct):.4f}     -> 1.00 {'[OK]' if round(np.mean(direct),2)==1.00 else '[FAIL]'}")
print(f"  Human Paraphrase:      M={np.mean(paraphrase):.4f} -> .58  {'[OK]' if round(np.mean(paraphrase),2)==0.58 else '[FAIL]'}")
print(f"  Stochastic Divergence: M={np.mean(divergence):.4f} -> .54  {'[OK]' if round(np.mean(divergence),2)==0.54 else '[FAIL]'}")

output_path = Path(__file__).resolve().parent.parent / "data" / "Epistemic_Governor_Calibration_Matrix_TableA1.xlsx"
output_path.parent.mkdir(exist_ok=True)
wb.save(output_path)
print(f"\nSaved: {output_path}")
