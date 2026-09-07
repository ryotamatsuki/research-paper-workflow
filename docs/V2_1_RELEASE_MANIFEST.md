# v2.1 Release Manifest

Release family: `research-paper-workflow`

Release: `v2.1`

Date: 2026-09-07

## Canonical authority

The v2.1 release preserves the repository hierarchy:

1. `GOVERNANCE.md`
2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
3. `templates/*.md`
4. `checklists/*.md`
5. `examples/*`

## Core v2 architecture included

v2.1 includes the full v2.0 mathematical-safety architecture:

- mandatory Stage 4A — Independent Mathematical Adversarial Certification;
- mandatory Stage 7.5A — Generality / Quantifier Red-Team;
- Stage 8 freeze blocked without both certificates;
- fail-closed off-path/global-equilibrium verification;
- theorem quantifier/scope discipline;
- benchmark-definition discipline;
- late Stage-11 certification-regression attack.

## v2.1 submission-compliance additions

Canonical modified/added surfaces include:

- `templates/STAGE_12_JOURNAL_POSITIONING.md`
- `templates/STAGE_13_FULL_PAPER_INTEGRATION.md`
- `templates/STAGE_14_SUBMISSION_QA.md`
- `templates/STAGE_15_SUBMISSION_FREEZE.md`
- `checklists/JOURNAL_REQUIREMENTS_CHECKLIST.md`
- `checklists/SUBMISSION_CHECKLIST.md`

The release requires an evidence-bearing Journal Requirements Ledger, current-policy recheck, source-package QA, unresolved-rule escalation, authenticated portal preflight, and generated-PDF inspection where applicable.

## Release documents

- `docs/V2_1_INTEGRATION_AUDIT.md`
- `docs/V2_1_READINESS_CHECKLIST.md`
- `docs/V2_1_RELEASE_MANIFEST.md`
- `docs/V2_1_RELEASE_NOTES.md`

## Publication machinery

- `.github/workflows/publish-v2.1.yml`

The workflow must refuse to overwrite an existing `v2.1` tag, finalize release metadata on reviewed `main`, and create the GitHub Release from `docs/V2_1_RELEASE_NOTES.md`.

## Historical-release treatment

Stable v1.0–v1.3 tags/releases remain immutable.

The v2.0 architecture was merged and integration-audited on 2026-09-06 but was not separately published as a GitHub tag/release. v2.1 is therefore the first stable tagged v2 release and contains both the v2.0 architecture and v2.1 submission-compliance hardening.

## Release target rule

The `v2.1` tag must point to the release-finalization commit produced from the reviewed v2.1 release PR state. It must not be moved afterward.