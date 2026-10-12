# v2.9 Release Manifest

Date: 2026-10-12 JST
Release class: **MINOR**
Baseline: stable v2.8 tag `aa80ffcd11615ce6da71807ee3dffde503c840e4`.
Release authorization: reviewed main and explicit main-branch publishing commit `Publish research-paper-workflow v2.9`.

## Canonical scope

- `GOVERNANCE.md` — §2.20 economic-contribution/editorial standards and §2.21 limitations/frontier.
- `THEORY_PAPER_RESEARCH_PIPELINE.md` — Stage 2, Stage 3, Stage 6, Stage 7.5, plus Stage 7/8/11/12 as relevant.
- `README.md`, `docs/VERSIONING_POLICY.md`.
- `templates/STAGE_02_NOVELTY_GATE.md`, `templates/STAGE_03_MECHANISM_SEARCH.md`, `templates/STAGE_06_NOVELTY_REKILL.md`, `templates/STAGE_075_FREEZE_DECISION.md`.
- `templates/STAGE_07_WELFARE_GENERALITY.md`, `templates/STAGE_08_THEORY_FREEZE.md`, `templates/STAGE_11_REFEREE_GATE.md`, `templates/STAGE_12_JOURNAL_POSITIONING.md`.
- `checklists/ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md`, `checklists/LITERATURE_AUDIT_CHECKLIST.md`, `checklists/NOVELTY_KILL_CHECKLIST.md`, `checklists/REFEREE_ATTACK_CHECKLIST.md`.
- `checklists/FRONTIER_OPPORTUNITY_CHECKLIST.md`, `templates/FRONTIER_OPPORTUNITY_REGISTER.md`, `templates/RESEARCH_SEARCH_REGISTER.md`.

## Evidence, checks, controls

- `docs/ECONOMIC_CONTRIBUTION_COMPLETENESS_REFINEMENT_2026-10-10.md`.
- `docs/FRONTIER_OPPORTUNITY_REFINEMENT_2026-10-12.md`.
- `docs/V2_9_INTEGRATION_AUDIT.md`.
- `docs/V2_9_READINESS_CHECKLIST.md`.
- `docs/V2_9_RELEASE_NOTES.md`.
- `.github/workflows/publish-v2.9.yml`.

## Publication contract

A GitHub Release named `research-paper-workflow v2.9` and its immutable `refs/tags/v2.9` must point to the reviewed `main` head after the explicit publishing commit and passing checks. In the absence of observed GitHub release metadata, this manifest claims release **readiness only**, not actual publication. Prior stable tags are never moved.
