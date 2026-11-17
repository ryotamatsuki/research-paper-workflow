# TDF v5.1 — Calibrated Dual-Track Theory Discovery

**Status:** Official practical-use version of the optional discovery companion, adopted 2026-11-17.

Start with the [master prompt](TDF_Master_Prompt_v5.1.md), [loop protocol](TDF_Loop_Protocol_v5.1.md), and [prompt library](TDF_Research_Prompt_Library_v5.1.md). Use the [run ledger](templates/Run_Ledger.md) during exploration and the [handoff template](templates/Stage0_Handoff.md) after author selection.

BOTH is the default. It runs STANDARD for researchable contributions and EPOCH for conceptual breakthroughs, using separate queues, budgets and verdicts with a shared bibliography. A single-track run can be requested explicitly. STANDARD is suited to a narrow question or a short exploration. The protocol describes how to generate, search, test, recycle, checkpoint and resume.

`dual_track.py` records budget allocations and source reuse from the run record. `gate.py` validates reported metadata and author-controlled routing. The researchers executing the protocol assess the evidence. The [canonical governance](../../GOVERNANCE.md) and [pipeline](../../THEORY_PAPER_RESEARCH_PIPELINE.md) govern formal decisions, proof and novelty certification.

From this directory, run:

```sh
python3 -m unittest discover -s tests -v
python3 validation/replay.py
```

The [calibration report](validation/Calibration_Report.md) describes the retrospective and synthetic validation cases. These cases test classification and routing. Prospective comparative evidence on discovery performance remains pending. Keep case-specific unpublished evidence in its project records.
