# The Epistemic Governor — Supplementary Materials

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20761026.svg)](https://doi.org/10.5281/zenodo.20761026)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**Figure generation scripts and calibration data for:**

> Clemons, C. A., McKibben, J. D., & Lindner, J. R. (2026). The Epistemic Governor: Reconceiving professional identity and methodological accountability in AI-assisted scholarship. *International Journal for Educational Integrity*, AI-Ethics Collection. https://doi.org/[JOURNAL_DOI]

---

## Overview

This repository provides fully reproducible supplementary materials for the Epistemic Governor manuscript. The paper introduces three theoretical constructs — the **Epistemic Governor**, **Micro Epistemic Drift (MED)**, and **Constraint Amnesia** — operationalized through a **Parallel Cognitive Router (PCR)** multi-agent architecture governed by a **Fidelity Index (Φ)** and **Verification Threshold (τ = .70)**.

### What is included

| Path | Contents |
|------|----------|
| `figures/figure1_signal_decay.py` | Exponential signal fidelity decay in linear workflows |
| `figures/figure2_parallel_lanes.py` | PCR three-lane parallel agent architecture |
| `figures/figure3_fidelity_dotplot.py` | **Primary empirical figure** — Φ distribution, all 15 calibration scores |
| `figures/figure4_pcr_workflow.py` | PCR operational swimlane workflow |
| `figures/figure5_phase_map.py` | Reference implementation phase map with audit trail |
| `data/Epistemic_Governor_Calibration_Matrix_TableA1.xlsx` | Complete calibration matrix — 15 individual Φ scores + Reference Implementation |
| `scripts/generate_calibration_data.py` | Reproducible XLSX generation script |

### What is NOT included

`PCR_Audit_Engine.py v6.0` (the Fidelity Index computation engine) is not publicly available pending intellectual property review. The complete procedural logic is documented in **Appendix A** of the manuscript as a pseudocode proxy enabling independent replication via standard LLM interfaces.

---

## Calibration Data Summary

All 15 Φ scores confirmed from PCR Master Execution Ledger, March 2026. Computed using `all-mpnet-base-v2` (Reimers & Gurevych, 2019), 768-dimensional sentence embeddings, cosine similarity. Source abstracts: Zhu et al. (2025) and Beijaard et al. (2004).

| Category | n | Mean Φ | Min Φ | Max Φ | Interpretation |
|---|:---:|:---:|:---:|:---:|---|
| Direct Extraction | 5 | 1.00 | 1.00 | 1.00 | Lexical alignment ceiling |
| Human Paraphrase | 5 | .58 | .24 | .82 | Acceptable syntactic variance |
| Stochastic Divergence | 5 | .54 | .35 | .67 | Maximum observed context drift |

**Verification Threshold:** τ = .70  
**Reference Implementation:** Φ = 0.5963 (≈ .60) — below τ, routed to Epistemic Governor  
**Drifted claim flagged:** LLM-generated "teaching profession crisis" attribution to Zhu et al. (2025)

---

## Quick Start

### Option 1 — pip

```bash
git clone https://github.com/cacbocam-source/epistemic-governor-supplementary.git
cd epistemic-governor-supplementary
pip install -r requirements.txt
python scripts/generate_calibration_data.py
python figures/figure3_fidelity_dotplot.py
```

### Option 2 — conda

```bash
git clone https://github.com/cacbocam-source/epistemic-governor-supplementary.git
cd epistemic-governor-supplementary
conda env create -f environment.yml
conda activate epistemic-governor
python scripts/generate_calibration_data.py
python figures/figure3_fidelity_dotplot.py
```

All figures save to `_02_Figures_TIFF/` as 600 dpi TIFF (LZW compression), BMC/Springer Nature combination artwork specification.

---

## Reproducing All Figures

Run from the repository root:

```bash
for fig in figures/figure*.py; do
    echo "Generating: $fig"
    python3 "$fig"
done
```

Expected output: five `.tiff` files in `_02_Figures_TIFF/`. File sizes: 0.8–5.0 MB each. DPI: 600 for all.

### Figure 3 — Empirical Verification

Figure 3 is the primary empirical figure. To verify that the generated figure matches the manuscript's reported values:

```bash
python3 - << 'EOF'
import numpy as np
paraphrase = np.array([0.6653, 0.4546, 0.7467, 0.236, 0.822])
divergence = np.array([0.6418, 0.6687, 0.346, 0.409, 0.6125])
print(f"Human Paraphrase:      M={np.mean(paraphrase):.4f} → .58 ✓")
print(f"Stochastic Divergence: M={np.mean(divergence):.4f} → .54 ✓")
print(f"Reference Implementation: Φ = 0.60 (Execution Ledger: 0.5963)")
print(f"Verification Threshold:   τ = .70")
EOF
```

---

## Reproducing the Calibration Matrix

```bash
python3 scripts/generate_calibration_data.py
```

Generates `data/Epistemic_Governor_Calibration_Matrix_TableA1.xlsx` with:
- **Sheet 1 — Calibration_Matrix:** 15 individual Φ scores with claim text and source text
- **Sheet 2 — Reference_Implementation:** Zhu et al. (2025) symmetric chunking comparison, composite Φ = 0.5963

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `matplotlib` | ≥3.7.0 | Figure rendering |
| `numpy` | ≥1.24.0 | Numerical computation |
| `Pillow` | ≥10.0.0 | TIFF export |
| `openpyxl` | ≥3.1.0 | Calibration matrix XLSX |

Python 3.10 or higher required.

---

## Citing This Work

### APA (7th edition)

```
Clemons, C. A., McKibben, J. D., & Lindner, J. R. (2026). The Epistemic Governor: 
Supplementary figure scripts and calibration data [Dataset]. Zenodo. 
https://doi.org/10.5281/zenodo.20761026
```

### BibTeX

```bibtex
@dataset{clemons2026epistemic_supplementary,
  author    = {Clemons, Christopher A. and McKibben, Jason D. and Lindner, James R.},
  title     = {The Epistemic Governor: Supplementary Figure Scripts and Calibration Data},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20761026},
  url       = {https://doi.org/10.5281/zenodo.20761026},
  note      = {Supplementary materials for manuscript submitted to International 
               Journal for Educational Integrity, AI-Ethics Collection}
}
```

### Cite the Manuscript

```bibtex
@article{clemons2026epistemic_governor,
  author  = {Clemons, Christopher A. and McKibben, Jason D. and Lindner, James R.},
  title   = {The Epistemic Governor: Reconceiving Professional Identity and 
             Methodological Accountability in {AI}-Assisted Scholarship},
  journal = {International Journal for Educational Integrity},
  year    = {2026},
  doi     = {PLACEHOLDER_JOURNAL_DOI}
}
```

---

## Key References

- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *EMNLP-IJCNLP*. https://arxiv.org/abs/1908.10084
- Zhu, H., Sun, Y., & Yang, J. (2025). Towards responsible artificial intelligence in education. *Humanities and Social Sciences Communications*, 12, Article 1111. https://doi.org/10.1057/s41599-025-05252-6
- Beijaard, D., Meijer, P. C., & Verloop, N. (2004). Reconsidering research on teachers' professional identity. *Teaching and Teacher Education*, 20(2), 107–128.
- Lindner, J. R., Clemons, C. A., & McKibben, J. D. (2026). Artificial intelligence in education: Perspectives of secondary teachers. *Advancements in Agricultural Development*, 7(2), 109–124. https://doi.org/10.37433/aad.v7i2.637
- Eaton, S. E. (2023). Postplagiarism. *International Journal for Educational Integrity*, 19(1), 23. https://doi.org/10.1007/s40979-023-00144-1

---

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this material for any purpose, provided appropriate credit is given.

---

## Acknowledgments

IRB Protocol: STUDY00000322. Auburn University covers the APC upon acceptance. The PCR reference implementation was executed March 2026. Source dataset: Lindner et al. (2026), *Advancements in Agricultural Development*, 7(2).
