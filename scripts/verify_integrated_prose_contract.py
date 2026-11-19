#!/usr/bin/env python3
"""Structural contract check; not a real paper prose referee."""
from pathlib import Path
r = Path(__file__).resolve().parents[1]
def check(p, *terms):
    s = (r/p).read_text(encoding="utf-8").lower()
    for t in terms:
        assert t.lower() in s, (p, t)
check("GOVERNANCE.md", "2.23A Mandatory final-paper", "Stage-13 GO", "PDF SHA-256")
check("THEORY_PAPER_RESEARCH_PIPELINE.md", "Stage 11 publication-prose", "final-prose subgate within Stage 13", "second")
check("templates/STAGE_11_REFEREE_GATE.md", "Stage-11 independent publication-facing prose diagnostic")
check("templates/STAGE_13_FULL_PAPER_INTEGRATION.md", "Mandatory independent final-publication-prose subgate", "Phase A", "Phase B", "second")
check("templates/STAGE_13_FINAL_PROSE_SUBGATE.md", "Phase A:", "Phase B:", "second", "SHA-256", "NO-GO")
check("templates/STAGE_14_SUBMISSION_QA.md", "33b.", "33c.", "SHA-256")
check("templates/STAGE_15_SUBMISSION_FREEZE.md", "invalidates the affected Stage-13")
check("checklists/FINAL_PROSE_REVIEW_CHECKLIST.md", "Phase A", "Phase B", "second")
check("checklists/EDITORIAL_ARGUMENT_QUALITY_CHECKLIST.md", "Stage 13 completed-paper prose subgate")
check("checklists/SUBMISSION_CHECKLIST.md", "Stage 13 final-PDF")
check("README.md", "Prospective v3.1", "No Stage 13P")
check("docs/VERSIONING_POLICY.md", "Prospective v3.1", "MINOR-class")
fix = (r/"examples/FINAL_PROSE_REVIEW_REGRESSION.md").read_text(encoding="utf-8")
for n in range(1,16):
    assert f"| P{n:02d} |" in fix, n
pipeline=(r/"THEORY_PAPER_RESEARCH_PIPELINE.md").read_text(encoding="utf-8")
assert pipeline.index("# Stage 11 —") < pipeline.index("# Stage 13 —") < pipeline.index("# Stage 14 —")
assert "# Stage 13P" not in pipeline
print("PASS structural v3.1 Stage 11/13 prose contract; no manuscript reviewed by CI")
