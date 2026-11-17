# TDF v5.1 — Calibrated Dual-Track Theory Discovery

**Status:** Official practical-use version of the optional discovery companion, adopted 2026-11-17.

Start with the [master prompt](TDF_Master_Prompt_v5.1.md), [loop protocol](TDF_Loop_Protocol_v5.1.md), and [prompt library](TDF_Research_Prompt_Library_v5.1.md). Use the [run ledger](templates/Run_Ledger.md) during exploration and the [handoff template](templates/Stage0_Handoff.md) after author selection.

STANDARD, the default, focuses on researchable contributions for specialist journals. EPOCH searches separately for conceptual breakthroughs. BOTH uses separate queues and budgets with a shared bibliography. The protocol describes how to generate, search, test, recycle, checkpoint and resume.

`dual_track.py` records budget allocations and source reuse from the run record. `gate.py` validates reported metadata and author-controlled routing. The researchers executing the protocol assess the evidence. The [canonical governance](../../GOVERNANCE.md) and [pipeline](../../THEORY_PAPER_RESEARCH_PIPELINE.md) govern formal decisions, proof and novelty certification.

From this directory, run:

```sh
python3 -m unittest discover -s tests -v
python3 validation/replay.py
```

The [calibration report](validation/Calibration_Report.md) describes the retrospective and synthetic validation cases. These cases test classification and routing. Prospective comparative evidence on discovery performance remains pending. Keep case-specific unpublished evidence in its project records.
