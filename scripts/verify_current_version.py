#!/usr/bin/env python3
"""Fail-closed check for *active* version markers, without rewriting historical provenance.

Workflow v3.x is independent of TDF v5.x. Historical release notes, tag-specific
publication workflows, archived proposal text, and pinned v3.1 regressions are
intentionally out of scope for active-version equality checks.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def one_version(path: str, pattern: str) -> str:
    matches = re.findall(pattern, read(path), flags=re.MULTILINE)
    if len(matches) != 1:
        raise AssertionError(f"{path}: expected exactly one active-version declaration; got {matches}")
    return matches[0]


def validate() -> None:
    expected = read("WORKFLOW_VERSION").strip()
    if not re.fullmatch(r"v\d+\.\d+(?:\.\d+)?", expected):
        raise AssertionError(f"WORKFLOW_VERSION has invalid format: {expected!r}")

    markers = {
        "README.md": r"^\*\*Current canonical version: (v\d+\.\d+(?:\.\d+)?)\b",
        "GOVERNANCE.md": r"^Version: (v\d+\.\d+(?:\.\d+)?)$",
        "THEORY_PAPER_RESEARCH_PIPELINE.md": r"^Version: (v\d+\.\d+(?:\.\d+)?)$",
        "docs/VERSIONING_POLICY.md": r"^Current canonical workflow: (v\d+\.\d+(?:\.\d+)?)\b",
        ".github/workflows/research-design-contract.yml": r"^name: Research design contract \((v\d+\.\d+(?:\.\d+)?)\)$",
    }
    for path, pattern in markers.items():
        got = one_version(path, pattern)
        if got != expected:
            raise AssertionError(f"{path}: current={got}, WORKFLOW_VERSION={expected}")

    if f"Canonical workflow: **{expected}**" not in read("README.md"):
        raise AssertionError("README status section has a stale canonical version")
    if f"Stable release reference: [\x60{expected}\x60]" not in read("README.md"):
        raise AssertionError("README stable release link points at a different version")

    stem = expected.upper().replace(".", "_")
    release_notes = f"docs/{stem}_RELEASE_NOTES.md"
    protocol = f"docs/{stem}_RESEARCH_DESIGN_PROTOCOL.md"
    if not (ROOT / release_notes).is_file() or not (ROOT / protocol).is_file():
        raise AssertionError(f"active release/protocol missing: {release_notes}, {protocol}")
    if "Status: ACTIVE after author approval" not in read(protocol):
        raise AssertionError("active research-design protocol has no adopted status")

    # Detect accidental stale current-version headers in active operational text.
    for directory in ("templates", "checklists"):
        for path in (ROOT / directory).glob("*.md"):
            first_lines = "\n".join(path.read_text(encoding="utf-8").splitlines()[:12])
            for pattern in (
                r"(?m)^Version:\s*(v\d+\.\d+(?:\.\d+)?)\s*$",
                r"(?m)^Current canonical workflow:\s*(v\d+\.\d+(?:\.\d+)?)\b",
                r"(?m)^\*\*Current canonical version:\s*(v\d+\.\d+(?:\.\d+)?)\b",
            ):
                for found in re.findall(pattern, first_lines):
                    if found != expected:
                        raise AssertionError(f"{path.relative_to(ROOT)}: stale operational version {found}")

    # TDF's version is separate: never force optional discovery v5.1 to v3.2.
    tdf = read("theory-discovery/README.md")
    if "## v5.1 — Official practical-use version" not in tdf:
        raise AssertionError("TDF default is no longer demonstrably v5.1; review deliberately")
    if "TDF v5.1" not in read("theory-discovery/AGENTS.md") and "v5.1" not in read("theory-discovery/AGENTS.md"):
        raise AssertionError("TDF agent guidance has no v5.1 reference")
    if "Official practical-use version" not in read("theory-discovery/v5.1/README.md"):
        raise AssertionError("TDF v5.1 package status is missing")

    print(f"PASS active workflow version consistency: {expected} (TDF v5.1 independently retained)")
    print("PASS historical source exclusions: release tags, dated proposals, pinned v3.1 test cases unchanged")


if __name__ == "__main__":
    validate()
