# v1.1 Release Manifest

Prospective version: `v1.1`

Release status: **integration-audited and release-ready; tag/release pending audit-PR merge**

Stable predecessor: `v1.0` at `d5c5146098d97279ad3e90342fa757f0f31c8264`

Post-PR-#6 audited baseline: `51bd722633a79020294991737625e94ba10ccde6`

## 1. Release character

v1.1 is a **MINOR** release under `docs/VERSIONING_POLICY.md`.

It preserves:

- canonical Stage 0–15 architecture, including Stage 7.5;
- `GO / CONDITIONAL GO / NO-GO` semantics;
- Stage routing;
- one-diagnosed-fix hardening;
- rollback/stale-state discipline;
- theory and submission freeze semantics.

It refines novelty evaluation inside the existing architecture.

## 2. Main v1.1 changes

### Whole-game absorption

Strategic/game-theoretic novelty assessment now separates:

1. component overlap; and
2. whole-game/result absorption.

An exact/absorbed verdict requires game-level evidence or result-level redundancy rather than a list of separate precedents for separate ingredients.

### Generalization / unification

The workflow explicitly recognizes economically substantive generalization/unification as a possible theory contribution, but requires:

- transparent nesting of important prior models;
- correct benchmark recovery;
- a strategic interaction endogenous only in the full architecture;
- at least one full-model-only theorem, threshold, ranking, sign reversal, equilibrium region, conditions-for-effectiveness result, or welfare wedge;
- Stage 6 result-level novelty re-kill.

### Versioning rule

- PATCH — non-substantive correction;
- MINOR — backward-compatible refinement of criteria/checks/verification while preserving Stage/verdict/routing architecture;
- MAJOR — incompatible Stage/verdict/routing/workflow-architecture change.

## 3. Files defining the v1.1 refinement

Canonical / operational:

- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_02_NOVELTY_GATE.md`
- `templates/STAGE_03_MECHANISM_SEARCH.md`
- `templates/STAGE_04_MINIMAL_MODEL.md`
- `templates/STAGE_06_NOVELTY_REKILL.md`
- `checklists/LITERATURE_AUDIT_CHECKLIST.md`
- `checklists/NOVELTY_KILL_CHECKLIST.md`
- `docs/VERSIONING_POLICY.md`

Decision / audit record:

- `docs/NOVELTY_GATE_CORRECTION_2026-09-02.md`
- `docs/WORKFLOW_V1_1_INTEGRATION_AUDIT.md`
- `docs/WORKFLOW_V1_1_READINESS_CHECKLIST.md`
- `docs/V1_1_RELEASE_MANIFEST.md`
- `docs/V1_1_RELEASE_NOTES.md`

## 4. Stable operational surface

Counts remain:

- canonical Stage templates: **17**;
- verification checklists: **6**;
- worked examples: **1**;
- canonical pipeline: Stage **0–15 including Stage 7.5**.

No Stage filename is changed in v1.1.

## 5. Compatibility promise

Existing v1 projects may continue to use the same Stage identities, verdict vocabulary and routing.

Projects whose novelty verdict relied materially on “all components are separately known” may merit re-audit at the earliest affected novelty gate. Re-audit does not imply automatic GO.

## 6. Historical records

The following remain historical v1.0-era records and are not rewritten:

- `docs/WORKFLOW_V1_INTEGRATION_AUDIT.md`
- `docs/WORKFLOW_V1_READINESS_CHECKLIST.md`
- `docs/WORKFLOW_V1_CHANGELOG.md`
- `docs/V1_RELEASE_PREPARATION.md`
- `docs/V1_RELEASE_MANIFEST.md`

The `v1.0` tag remains immutable.

## 7. Release operation

After the v1.1 audit PR merges:

1. verify the audit-ready marker;
2. verify `v1.1` does not already exist;
3. publish a new `v1.1` tag on the reviewed post-audit release state;
4. publish GitHub Release `research-paper-workflow v1.1` using `docs/V1_1_RELEASE_NOTES.md`;
5. verify the tag and release resolve to the intended commit;
6. leave `v1.0` untouched.

The release automation included with the audit PR is release-only infrastructure and does not alter research-stage semantics.
