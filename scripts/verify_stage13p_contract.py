#!/usr/bin/env python3
"""Structural smoke tests for the prospective mandatory v4.0 Stage 13P gate.

These tests do NOT read a paper, rank prose, certify genuine reviewer independence,
evaluate economic theories, or authorize a journal submission.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

NEEDED = [
    "GOVERNANCE.md",
    "README.md",
    "THEORY_PAPER_RESEARCH_PIPELINE.md",
    "docs/VERSIONING_POLICY.md",
    "docs/STAGE13P_PUBLICATION_PROSE_GATE_DESIGN_2026-11-19.md",
    "templates/STAGE_13P_INDEPENDENT_PROSE_REVIEW.md",
    "templates/STAGE_13_FULL_PAPER_INTEGRATION.md",
    "templates/STAGE_14_SUBMISSION_QA.md",
    "templates/STAGE_15_SUBMISSION_FREEZE.md",
    "templates/STAGE_10A_EXEMPLARY_PAPER_BENCHMARKING.md",
    "templates/STAGE_12_JOURNAL_POSITIONING.md",
    "checklists/PUBLICATION_PROSE_REVIEW_CHECKLIST.md",
    "checklists/SUBMISSION_CHECKLIST.md",
    "examples/PUBLICATION_PROSE_REVIEW_REGRESSION.md",
]

DELIVERABLES = [
    "PROSE_REFEREE_REPORT.md",
    "EXEMPLAR_PROSE_COMPARISON.md",
    "PROSE_ISSUE_REGISTER.md",
    "PROSE_REVISION_AUDIT.md",
    "STAGE13P_GATE_REPORT.md",
]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def main():
    for path in NEEDED:
        require((ROOT / path).is_file(), f"missing required v4 candidate artifact: {path}")

    gov, pipe = read("GOVERNANCE.md"), read("THEORY_PAPER_RESEARCH_PIPELINE.md")
    template = read("templates/STAGE_13P_INDEPENDENT_PROSE_REVIEW.md")
    sub = read("checklists/SUBMISSION_CHECKLIST.md")
    qa = read("templates/STAGE_14_SUBMISSION_QA.md")
    freeze = read("templates/STAGE_15_SUBMISSION_FREEZE.md")
    design = read("docs/STAGE13P_PUBLICATION_PROSE_GATE_DESIGN_2026-11-19.md")
    regress = read("examples/PUBLICATION_PROSE_REVIEW_REGRESSION.md")
    ver = read("docs/VERSIONING_POLICY.md")
    readme = read("README.md")

    require(pipe.index("# Stage 13 — Full-Paper Integration") <
            pipe.index("# Stage 13P — Independent Publication Prose Review") <
            pipe.index("# Stage 14 — Submission QA"),
            "Stage 13P must be between Stage 13 and Stage 14")
    require("Stage 13 GO → Stage 13P GO → Stage 14" in pipe,
            "proposed canonical routing not explicitly declared")
    require("Stage 13P GO is required to enter Stage 14" in gov,
            "governance bypass: prose gate not mandatory")
    require("CONDITIONAL GO" in pipe and "does not authorize Stage 14" in template,
            "conditional should not bypass new gate")

    phase_a = template.index("## 2. Phase A")
    phase_b = template.index("## 3. Phase B")
    require(phase_a < phase_b, "blind Phase A must precede exemplar access in Phase B")
    require("before" in template.lower() and "blind" in template.lower()
            and "full" in template.lower() and "source" in template.lower(),
            "must specify genuinely independent full-text exposure")
    require("second cold read" in template and "exact" in template.lower(),
            "independent post-repair full-text retest missing")
    require("source SHA" in template and "PDF hash" in template,
            "accepted manuscript source/PDF provenance missing")
    require("STRONG / ADEQUATE / WEAK" in template,
            "qualitative text-grounded exemplar comparison missing")

    for item in DELIVERABLES:
        require(item in template, f"Stage13P deliverable missing: {item}")
    require("Stage 13P" in qa and "Stage 13P" in freeze and "Stage 13P" in sub,
            "downstream QA/freeze route missing")
    require("post-GO" in qa or "subsequent wording change" in qa,
            "Stage14 must invalidate stale material prose review")
    require("v4.0" in ver and "MAJOR" in ver and "v3.0" in ver and "v3.0" in readme,
            "versioning must state prospective v4 and preserve existing v3")
    require("NOT" in design and "v3.0" in design and "v4.0" in design,
            "release status must be explicitly unreleased")
    ids = sorted(set(re.findall(r"\bP(?:0[1-9]|1[0-9])\b", regress)))
    require(len(ids) >= 12, "insufficient regression fixtures")
    require("Stage-4A" in regress and "hostile-audit" in regress
            and "Stage 1" in regress and "quantifier" in regress,
            "case fixtures must include workflow leakage, valid game stage and scientific safety")

    print("STAGE13P STRUCTURAL ROUTE/EXEMPLAR/SNAPSHOT REGRESSION PASS")
    print("NOTE: this does not perform independent manuscript reading or prose peer review.")

if __name__ == "__main__":
    main()
