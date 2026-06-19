# Appendix A — Procedural Logic Proxy

This document reproduces the Appendix A procedural logic proxy from the manuscript.
It provides a pseudocode representation of the PCR Audit Engine's adversarial
retrieval protocol sufficient for independent replication via standard LLM interfaces.

For the complete Appendix A including Table A1 (calibration data), Table A2
(reference implementation), and the Epistemic Governor adjudication walkthrough,
see the manuscript.

---

## Skeptic Agent: Procedural Logic Proxy
**Function:** Adversarial Retrieval Protocol

```
Input: Analyst_Syntax_Output, Draft_Prose

Constraint: Temperature = .70, Role = Adversarial
// Note: Temperature = .70 is the LLM stochasticity parameter;
// this value is independent of the Fidelity threshold τ = .70.

Initialize Vector Cross-Reference:
   FOR EACH claim IN Draft_Prose:
      Query external database (Crossref / Global DOI Index)
      Retrieve Source_Abstract

Execute Symmetric_Chunking (Partition Abstract into Atomic_Sentences)
// Symmetric chunking partitions the source abstract into individual sentences
// at punctuation boundaries, treating each sentence as an atomic comparison
// unit against the target claim.

Compute claim embedding and per-sentence source embeddings:
// Encode both the target claim and each atomic sentence using all-mpnet-base-v2
// (768-dimensional vectors, mean pooling of token-level embeddings).
// Φ = maximum cosine similarity across all atomic source sentence embeddings.

Calculate Fidelity Index (Φ) against Atomic Sentences:
   IF Φ < τ (.70):
      Flag = "Hallucination Risk: Semantic Drift Detected"
      Generate Epistemic_Friction_Report
   ELSE:
      Flag = "Provisionally Aligned: Human Review Still Required"

Output: Epistemic_Friction_Report → Human_Orchestrator
```

---

## Calibration Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Embedding model | all-mpnet-base-v2 | Reimers & Gurevych (2019) |
| Embedding dimensions | 768 | Sentence-transformers |
| Pooling method | Mean pooling of token-level embeddings | Default |
| Similarity metric | Cosine similarity | Standard |
| Verification threshold (τ) | .70 | PCR Calibration Log, March 2026 |
| Skeptic Agent temperature | .70 (LLM parameter) | Independent of τ |

---

*Source: Clemons, C. A., McKibben, J. D., & Lindner, J. R. (2026). The Epistemic
Governor. International Journal for Educational Integrity.*
