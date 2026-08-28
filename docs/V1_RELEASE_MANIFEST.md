# v1.0 Release Manifest

Prospective version: `v1.0`

Release status: **release-ready candidate; Git tag and GitHub Release not yet created**

Prospective tag target: **the PR #5 squash-merge commit on `main`**. The exact SHA must be recorded after merge and re-checked immediately before tag creation.

## 1. Authority classes

The prospective release contains several authority levels. They must not be treated as equivalent.

### Canonical research behavior

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Stable promises include:

- Stage 0–15 architecture, including Stage 7.5;
- `GO / CONDITIONAL GO / NO-GO` semantics;
- novelty-kill and result re-kill discipline;
- one-diagnosed-fix hardening rule;
- rollback and stale-state policy;
- evidence/provenance discipline;
- theory freeze and submission freeze.

### Operational surface

`templates/` contains 17 executable Stage templates:

1. `STAGE_00_IDEA_INTAKE.md`
2. `STAGE_01_AUDIT.md`
3. `STAGE_02_NOVELTY_GATE.md`
4. `STAGE_03_MECHANISM_SEARCH.md`
5. `STAGE_04_MINIMAL_MODEL.md`
6. `STAGE_05_HARDENING.md`
7. `STAGE_06_NOVELTY_REKILL.md`
8. `STAGE_07_WELFARE_GENERALITY.md`
9. `STAGE_075_FREEZE_DECISION.md`
10. `STAGE_08_THEORY_FREEZE.md`
11. `STAGE_09_REPRODUCIBILITY_SETUP.md`
12. `STAGE_10_PAPER_BUILD.md`
13. `STAGE_11_REFEREE_GATE.md`
14. `STAGE_12_JOURNAL_POSITIONING.md`
15. `STAGE_13_FULL_PAPER_INTEGRATION.md`
16. `STAGE_14_SUBMISSION_QA.md`
17. `STAGE_15_SUBMISSION_FREEZE.md`

`checklists/` contains 6 verification checklists:

1. `LITERATURE_AUDIT_CHECKLIST.md`
2. `NOVELTY_KILL_CHECKLIST.md`
3. `SYMBOLIC_VERIFICATION_CHECKLIST.md`
4. `NUMERICAL_VERIFICATION_CHECKLIST.md`
5. `REFEREE_ATTACK_CHECKLIST.md`
6. `SUBMISSION_CHECKLIST.md`

These paths are part of the stable v1 operational surface. Future incompatible renaming or semantic replacement requires version-impact assessment.

### Non-canonical reference material

- `examples/README.md`
- `examples/retail-service-infrastructure/`

Example count at v1.0: **1**.

The current example is a research-decision trail with rejected branches and a surviving `CONDITIONAL GO` before canonical Stage 7.5. It is not a canonical successful-paper template.

### Audit / historical records

- `docs/WORKFLOW_V1_INTEGRATION_AUDIT.md`
- `docs/WORKFLOW_V1_READINESS_CHECKLIST.md`
- `docs/WORKFLOW_V1_CHANGELOG.md`

These document the PR #4 integration state and remain historical records.

### Release documentation

- `docs/VERSIONING_POLICY.md`
- `docs/V1_RELEASE_MANIFEST.md`
- `docs/V1_RELEASE_PREPARATION.md`

## 2. Root release-facing files

- `README.md`
- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

## 3. Counts

- Canonical Stage templates: **17**
- Verification checklists: **6**
- Worked examples: **1**
- Canonical pipeline: Stage **0–15 including Stage 7.5**

## 4. Stable interface for v1

Users may rely on the following as stable within the v1 line unless a documented compatible extension applies:

- canonical hierarchy;
- Stage identities and numbering;
- canonical verdict semantics;
- Stage 4 `GO → Stage 6`, one-blocker `CONDITIONAL GO → Stage 5`, `NO-GO → stop/distinct pivot` routing;
- rollback to the earliest invalidated Stage and stale downstream outputs;
- evidence/provenance maturity discipline;
- one-diagnosed-fix principle;
- Stage 7.5 full-paper investment gate;
- Stage 8 theory freeze;
- Stage 15 paper-level submission freeze;
- the published `templates/` and `checklists/` paths listed above.

## 5. Recommended reuse mode

The recommended v1 use is **reference-repository mode**:

1. keep `research-paper-workflow` as the canonical workflow reference;
2. use/copy the relevant Stage prompt into the active research process;
3. preserve Stage reports, decision logs, verification artifacts, and frozen outputs in the individual research/paper repository;
4. create the production paper repository at canonical Stage 9 after Stage 7.5 approval and Stage 8 theory freeze.

The workflow repository itself is not the production LaTeX repository scaffold for each paper.

## 6. Explicit exclusions from the v1.0 promise

The prospective v1.0 release does **not** promise:

- a complete empirical-economics post-Stage-3 workflow;
- automated workflow execution;
- GitHub Actions or CI enforcement;
- machine-readable/YAML stage metadata;
- automatic prompt generation;
- guaranteed novelty;
- guaranteed journal acceptance;
- automated proof correctness;
- a production-paper LaTeX repository scaffold;
- a legal/open-source reuse license beyond whatever repository license state is separately present.

## 7. Known deferred capabilities

Post-v1 candidates include:

- empirical companion workflow;
- additional worked examples;
- optional automation/CI;
- machine-readable metadata;
- lightweight execution profile;
- separate production-paper repository/bootstrap template;
- explicit open-source licensing if third-party redistribution/derivative reuse is intended.

These are not blockers for release as a versioned reference workflow.

## 8. Release operation boundary

PR #5 prepares the reviewed contents only. It must not create `v1.0`.

A later explicit release operation must:

1. confirm the latest `main` SHA equals the reviewed PR #5 merge SHA;
2. confirm no intervening commit exists;
3. confirm `v1.0` does not already exist;
4. confirm release notes match this manifest;
5. create the tag/release only after those checks.
