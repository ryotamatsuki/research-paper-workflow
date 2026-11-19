#!/usr/bin/env python3
"""Offline v3.2 regression and documentation-contract test.

Tests research DECISION RULES on stipulated evidence, not theorem correctness.
Green case E is a non-destructive post-hoc shadow assessment.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "tests" / "fixtures" / "research_design_cases.json"
ALLOWED_ROUTES = {"THEME-FIRST", "MODEL-FIRST", "HYBRID"}
ALLOWED_FEATURE = {"NECESSARY", "MATERIAL_CHANGE", "UNCHANGED", "NOT_RUN", "NOT_APPLICABLE"}

def classify(case: dict) -> str:
    assert case["route"] in ALLOWED_ROUTES
    assert case["feature_test"] in ALLOWED_FEATURE
    assert case["evidence"].strip() and case["strongest_objection"].strip()
    parent = case["prior"]
    feature = case["feature_test"]
    gain = case["economic_gain"]
    claim = case["claim"]

    if parent == "UNRESOLVED":
        return "PRIOR_ART_UNRESOLVED"
    if parent == "ABSORBED":
        return "APPLICATION_ONLY" if claim == "APPLICATION" and gain == "IMPORTANT_APPLICATION" else "NO_INDEPENDENT_THEORY"
    if claim == "THEMATIC_THEORY":
        if feature == "NOT_RUN":
            return "THEMATIC_RISK_UNRESOLVED"
        if feature in ("UNCHANGED", "NOT_APPLICABLE"):
            return "CLAIM_REFRAME_REQUIRED"
        if feature in ("NECESSARY", "MATERIAL_CHANGE") and gain == "SUBSTANTIVE":
            return "SUPPORTED_WITH_SCOPE"
        return "ECONOMIC_GAIN_UNRESOLVED"
    if claim == "GENERAL_THEORY":
        return "SUPPORT_GENERAL_THEORY" if gain == "SUBSTANTIVE" else "ECONOMIC_GAIN_UNRESOLVED"
    if claim == "APPLICATION":
        return "APPLICATION_ONLY" if gain == "IMPORTANT_APPLICATION" else "ECONOMIC_GAIN_UNRESOLVED"
    raise AssertionError("unknown claim type: " + claim)

def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def test_cases() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    assert data["snapshot"]["workflow_version"] == "v3.1"
    assert len(data["cases"]) == 6
    assert [case["id"] for case in data["cases"]] == list("ABCDEF")
    for case in data["cases"]:
        actual = classify(case)
        assert actual == case["expected"], (case["id"], actual, case["expected"])
        print("PASS case", case["id"], "->", actual)
    e = next(c for c in data["cases"] if c["id"] == "E")
    assert e["legacy_verdict_preserved"] is True
    assert e["feature_test"] == "NOT_RUN" and e["expected"] == "THEMATIC_RISK_UNRESOLVED"
    assert "matched" in e["unrun_counterfactual"]
    assert len(data["snapshot"]["evidence_files"]) >= 4
    for f in data["snapshot"]["evidence_files"]:
        assert len(f["blob_sha"]) == 40 and f["anchor"].strip()

def test_contract() -> None:
    targets = {
        "GOVERNANCE.md": ["research-question/model/contribution governance", "THEME-FIRST"],
        "THEORY_PAPER_RESEARCH_PIPELINE.md": ["v3.2 candidate", "five independent"],
        "templates/STAGE_00_IDEA_INTAKE.md": ["THEME-FIRST", "MODEL-FIRST", "HYBRID"],
        "templates/STAGE_02_NOVELTY_GATE.md": ["Research Question–Literature–Mechanism Mapping", "cheap falsifier"],
        "templates/STAGE_03_MECHANISM_SEARCH.md": ["pre-model Research Question–Mechanism Alignment", "eight questions"],
        "templates/STAGE_04_MINIMAL_MODEL.md": ["M0 =", "M1 =", "M2 =", "NON-COMPARABLE"],
        "templates/STAGE_06_NOVELTY_REKILL.md": ["Theorem Absorption", "Mechanism Contribution Identification", "Economic Learning Gain"],
        "templates/STAGE_075_FREEZE_DECISION.md": ["CONTRIBUTION_IDENTIFICATION_REPORT.md", "question–theorem alignment"],
        "templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md": ["portability is not", "scope"], # check phrase below by casefold
        "templates/STAGE_08_THEORY_FREEZE.md": ["CONTRIBUTION_IDENTIFICATION_REPORT"],
        "templates/STAGE_10A_EXEMPLARY_PAPER_BENCHMARKING.md": ["argument construction"],
        "templates/STAGE_10_PAPER_BUILD.md": ["question-to-model-to-claim"],
        "templates/STAGE_11_REFEREE_GATE.md": ["Generic Model in Disguise", "Alternative Model Challenge"],
        "templates/STAGE_12_JOURNAL_POSITIONING.md": ["five scientific axes", "publication fit"],
        "templates/STAGE_13_FULL_PAPER_INTEGRATION.md": ["alignment regression", "v3.1 independent"],
        "templates/STAGE_14_SUBMISSION_QA.md": ["PRE_SUBMISSION_SCIENTIFIC_RISK_BRIEF.md"],
        "templates/STAGE_15_SUBMISSION_FREEZE.md": ["author-review closure"],
        "templates/CONTRIBUTION_IDENTIFICATION_REPORT.md": ["Original research question", "Strongest hostile referee objection"],
        "templates/PRE_SUBMISSION_SCIENTIFIC_RISK_BRIEF.md": ["Mathematical Validity", "Prior-Art Distinctness", "Research Question Alignment", "Economic Significance", "Generality & Scope"],
        "docs/V3_2_GAP_METHODOLOGY_AUDIT.md": ["DESIGN GAP", "EXECUTION GAP", "EVIDENCE GAP", "ROUTING GAP"],
        "docs/V3_2_RESEARCH_DESIGN_PROTOCOL.md": ["Stage 0", "Stage 11", "Stage 7.5A"],
    }
    for path, words in targets.items():
        body = text(path).casefold()
        for word in words:
            assert word.casefold() in body, (path, word)
    readme = text("README.md")
    assert "**Current canonical version: v3.1" in readme
    assert "current official release remains v3.1" in readme
    print("PASS documentation contract", len(targets), "files")
    
def test_green_source_integrity() -> None:
    """Optional online integrity check of actual GREEN source records at a pinned SHA.

    Does NOT assert that unrun counterfactuals fail or mathematically solve them.
    """
    import hashlib
    import urllib.request
    data = json.loads(DATA.read_text(encoding="utf-8"))
    snapshot = data["snapshot"]
    repo = snapshot["green_repository"]
    sha = snapshot["green_main_sha"]
    for record in snapshot["evidence_files"]:
        path = record["path"]
        url = "https://raw.githubusercontent.com/" + repo + "/" + sha + "/" + path
        req = urllib.request.Request(url, headers={"User-Agent": "research-paper-workflow-v3.2-regression"})
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = response.read()
        raw_blob = b"blob " + str(len(payload)).encode() + b"\x00" + payload
        observed_sha = hashlib.sha1(raw_blob).hexdigest()
        assert observed_sha == record["blob_sha"], ("SHA drift", path, observed_sha, record["blob_sha"])
        content = payload.decode("utf-8")
        assert record["anchor"] in content, ("missing real source excerpt", path, record["anchor"])
        print("PASS pinned Green evidence", path, observed_sha)

if __name__ == "__main__":
    test_cases()
    test_contract()
    print("PASS v3.2 research-design contract: 6 cases and stage integration")
    import sys
    if "--verify-green-sources" in sys.argv:
        test_green_source_integrity()
