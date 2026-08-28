# v1 Release Preparation

Preparation date: 2026-08-28

Starting reviewed `main`: `b5427833c130a5f28a4812be1cfbf537883ec41e`

Working branch: `release/v1-preparation`

## 1. Executive verdict

**Post-fix verdict: `v1.0 RELEASE READY`.**

PR #4 established `WORKFLOW v1 READY` for repeated use as a theory-oriented economics research workflow. This release-preparation review found no blocker requiring changes to the research architecture. It found three pre-release documentation/interface issues that should be fixed before a stable tag:

1. canonical documents still identified themselves as `v1-rc1`, which would be stale inside a future `v1.0` tag;
2. release/version compatibility rules were listed as a future governance item rather than defined;
3. the README still described PR #5 as the next step and did not clearly state the recommended reference-repository reuse mode versus a production paper template.

The fixes are release-surface changes only. No Stage, gate, template semantics, checklist, worked case, CI, empirical workflow, tag, or GitHub Release is added.

## 2. Repository state reviewed

At audit start:

- default branch: `main`;
- `main` SHA: `b5427833c130a5f28a4812be1cfbf537883ec41e`;
- open PRs: none;
- Git tags: none;
- GitHub Releases: none;
- canonical Stage templates: 17;
- verification checklists: 6;
- worked examples: 1;
- PR #4 had already merged the v1 integration audit.

Branches observed at start:

| Branch | State for release prep |
|---|---|
| `main` | ACTIVE canonical branch |
| `audit/workflow-v1-integration` | MERGED / STALE; safe to delete later after release if desired |
| `bootstrap/workflow-v1` | MERGED / STALE historical bootstrap branch; safe to delete later |
| `examples/retail-service-case-study` | MERGED / STALE; safe to delete later |
| `templates/stage-templates-v1` | MERGED / STALE; safe to delete later |
| `release/v1-preparation` | ACTIVE PR #5 branch |

No branch is deleted in PR #5.

## 3. PR #4 readiness baseline

PR #4 concluded:

`WORKFLOW v1 READY`

The release review treats the following as already integration-audited and does not reopen them without evidence of a release defect:

- canonical Stage 0–15 + Stage 7.5 architecture;
- verdict/routing semantics;
- Stage 4 hardening route;
- rollback/stale-state rule;
- evidence maturity and AI provenance;
- literature-ledger continuity;
- theory-oriented v1 method scope.

## 4. Release scope

PR #5 freezes and documents the release interface. It does not develop new research functionality.

Release-facing stable areas are:

- canonical authority hierarchy;
- canonical Stage numbering and gate semantics;
- operational template/checklist paths;
- evidence/rollback/freeze behavior;
- version compatibility rules;
- public navigation and reuse mode.

Explicitly out of scope:

- new Stage/gate;
- empirical pipeline;
- new worked example/checklist;
- CI/automation/YAML;
- GitHub Template Repository setting;
- production paper scaffold;
- branch deletion;
- `v1.0` tag or GitHub Release.

## 5. Version-state audit

| Version/state phrase | Classification | Treatment |
|---|---|---|
| `Version: v1-rc1` in canonical governance/pipeline | STALE FOR PROSPECTIVE v1.0 | update to `v1.0` before tag |
| `WORKFLOW v1 READY` in PR #4 audit docs | HISTORICAL / CURRENT AUDIT RESULT | preserve |
| `release candidate` / `release-ready` | CURRENT PRE-RELEASE | preserve/use explicitly |
| PR #4 references recommending PR #5 | HISTORICAL | preserve in audit records |
| README saying PR #5 is next | STALE AFTER PR #5 | update |
| `v1.0 released` | NOT PRESENT / PROHIBITED BEFORE TAG | do not introduce |
| `bootstrap-v1` canonical version label | NOT PRESENT in current canonical docs | no action |

Historical audit documents are not rewritten to make them appear to have been authored after release preparation.

## 6. Canonical release surface

The authority order remains unchanged:

1. `GOVERNANCE.md`
2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
3. `templates/*.md`
4. `checklists/*.md`
5. `examples/*`

`docs/` contains audit, versioning, and release records. It does not outrank the canonical hierarchy.

The stable v1 interface includes Stage numbering, verdict semantics, one-diagnosed-fix discipline, rollback/stale-state behavior, evidence/provenance discipline, theory freeze, submission freeze, and the published Stage/checklist paths.

## 7. Navigation audit

The root README already provides direct links to:

- canonical pipeline;
- governance;
- all 6 checklists;
- examples;
- PR #4 audit documents.

Release preparation adds links to the version policy, manifest, and release-preparation record and makes the recommended reuse mode explicit.

**Verdict: PASS after minimal README update.**

## 8. Template reuse audit

Three possible reuse modes were evaluated.

### A — Copy/fork the entire workflow repository for every paper

Not recommended. Audit/history/example materials and workflow governance would be duplicated into each production paper repository and confuse workflow development with paper development.

### B — Copy only the Stage prompt needed at each step

Usable, but the authoritative Stage history and project evidence still need to be preserved in the active research repository.

### C — Keep this repository as the stable reference; store project-specific Stage reports/artifacts in the individual research repository

**Recommended v1 mode.**

This aligns with canonical Stage 9, where a production research/paper repository is created only after Stage 7.5 approval and Stage 8 theory freeze.

## 9. Repository-template suitability

### Reference repository

**`SUITABLE AS REFERENCE REPOSITORY`**.

The root cleanly separates canonical policy, operational templates/checklists, examples, and release/audit documentation.

### GitHub Template Repository for production papers

**`NOT YET SUITABLE AS TEMPLATE`** for production paper repositories.

Reasons:

- workflow audit/history files are reference material, not paper-project files;
- the worked example should not be copied as project state;
- Stage 9 expects a separate production repository/scaffold;
- no production LaTeX/project bootstrap surface is promised by v1.

This is not a v1 release blocker because v1 is explicitly a decision-workflow release, not a paper-repository-template release.

## 10. Branch hygiene

The four pre-v1 feature/audit branches are merged/stale and can be deleted later. PR #5 intentionally does not delete them.

The default `main` branch is currently reported as unprotected by the branch listing. Branch protection/ruleset hardening may be useful repository administration after release but is not part of the v1 content promise and is therefore deferred rather than silently configured here.

**Verdict: acceptable for v1 content release; cleanup deferred.**

## 11. Tag / release audit

At release-preparation start:

- existing Git tag refs: **0**;
- existing GitHub Releases: **0**;
- `v1.0` conflict: **none**.

PR #5 creates neither a tag nor a GitHub Release.

## 12. Stable-link audit

The release-facing relative links referenced from the root README resolve to paths present in the reviewed repository tree. The Stage template/checklist paths listed in the v1 manifest correspond to files present in the same tree.

No release-blocking broken relative link was identified.

**Verdict: PASS.**

## 13. File-name stability

The Stage file names are consistent and usable as stable v1 paths.

`STAGE_075_FREEZE_DECISION.md` is retained. Although `075` is a filename encoding rather than the display label `7.5`, renaming immediately before release would create unnecessary path churn without changing research behavior.

**Verdict: retain all current Stage/checklist filenames for v1.0.**

## 14. Historical-document handling

`docs/WORKFLOW_V1_*` files remain records of PR #4. Their references to `v1-rc1`, PR #5 as a future step, or the audited pre-release state are historical facts where they occur and should not be rewritten merely to match the later release surface.

New release documentation records the new state instead.

## 15. Compatibility policy

`docs/VERSIONING_POLICY.md` defines workflow-aware versioning:

- **MAJOR** for incompatible canonical research-decision behavior;
- **MINOR** for backward-compatible capability;
- **PATCH** for non-behavioral correction.

Backward compatibility is judged by whether existing v1 projects can retain the same Stage numbering, gate meanings, material evidence requirements, handoffs, rollback, and freeze semantics.

Stable tags are immutable; defects are corrected with later versions rather than moving an existing stable tag.

**Verdict: PASS after policy addition.**

## 16. Stress tests

### A — New theory-paper idea

README → governance → Stage 0 → placeholders → report/verdict path is clear.

**PASS.**

### B — Old thesis/model revival

Stage 0 can recover the question and Stage 1 can audit inherited source/model material. The worked example illustrates decision logic without being canonical.

**PASS.**

### C — Policy idea intended for empirical research

README and pipeline state that Stages 0–3 may identify an empirical/mixed route but non-theory projects should not be forced through Stage 4.

**PASS within declared v1 scope.**

### D — Stage 11 FATAL six months later

Governance requires rollback to the earliest invalidated Stage and marks dependent downstream outputs stale.

**PASS.**

### E — Future contributor proposes a new mandatory Stage 5 robustness gate

The version policy requires assessment of whether the new mandatory requirement changes canonical research-decision behavior. If it can alter existing v1 project verdicts/routes, it is breaking rather than a patch; a purely optional backward-compatible addition may be minor.

**PASS.**

## 17. Findings register

| ID | Area | Severity | Finding | Evidence | Fix now? | Resolution |
|---|---|---|---|---|---|---|
| R1-001 | version state | MAJOR PRE-RELEASE | canonical docs still say `v1-rc1` | Governance/pipeline headers | yes | prospective canonical version set to `v1.0`; README still states tag pending |
| R1-002 | version governance | MAJOR PRE-RELEASE | compatibility/tag immutability not yet defined and listed as future work | Governance future-extension section | yes | add `VERSIONING_POLICY.md` and small governance release-policy bridge |
| R1-003 | navigation/reuse | MAJOR PRE-RELEASE | README still points to PR #5 as future and does not explicitly distinguish reference workflow from production paper template | README status/use sections | yes | update release-facing README minimally |
| R1-004 | branch hygiene | MINOR PRE-RELEASE | four merged/stale feature/audit branches remain | branch listing | no destructive action | classify for later cleanup |
| R1-005 | tags/releases | NO ISSUE | no prior tag/release conflicts | Git refs/releases | no | safe future `v1.0` namespace |
| R1-006 | file paths | NO ISSUE | current 17 Stage filenames and 6 checklist filenames are stable enough | repository tree | no | freeze paths for v1 |
| R1-007 | repository template | POST-v1 ENHANCEMENT | workflow reference repo is not a production paper scaffold/template | architecture + Stage 9 | no | release as reference workflow; separate future bootstrap if useful |
| R1-008 | branch protection | POST-v1 ENHANCEMENT | `main` is not reported as protected | branch listing | no | optional repository-admin hardening later |
| R1-009 | licensing | POST-v1 ENHANCEMENT | no explicit LICENSE file is part of current release surface | repository tree | no | do not promise open-source redistribution; choose license explicitly later if intended |

No `BLOCKER FOR v1.0` finding remains after the planned release-surface fixes.

## 18. Changes made

PR #5 is limited to:

- add `docs/VERSIONING_POLICY.md`;
- add `docs/V1_RELEASE_MANIFEST.md`;
- add this `docs/V1_RELEASE_PREPARATION.md`;
- update root README for release-ready status, release-doc navigation, and reuse mode;
- update `GOVERNANCE.md` only to connect canonical change governance to version/tag immutability policy;
- change canonical document version headers from `v1-rc1` to prospective `v1.0` without changing research behavior.

No Stage/template/checklist/example research semantics are changed.

## 19. Deferred items

Post-v1 candidates:

- stale merged-branch deletion;
- branch protection/ruleset hardening;
- explicit repository license if open-source redistribution/derivative reuse is intended;
- dedicated empirical workflow;
- production-paper bootstrap/template repository;
- CI/automation/YAML;
- additional examples;
- lightweight workflow profile if real repeated use justifies it.

## 20. Prospective v1.0 release contents

The exact prospective contents are defined in `V1_RELEASE_MANIFEST.md`.

Counts remain:

- 17 Stage templates;
- 6 verification checklists;
- 1 worked example;
- Stage 0–15 including Stage 7.5.

Prospective `v1.0` tag target: **PR #5 squash-merge commit on `main`**, to be recorded and re-verified after merge.

## 21. Final release-readiness verdict

After the pre-release fixes described above:

- PR #4 workflow readiness is unchanged;
- no release blocker remains;
- canonical v1 promises are identified;
- version compatibility is defined;
- navigation and reuse mode are explicit;
- stable operational paths are known;
- tags/releases have no existing conflict;
- deferred template/empirical/automation work is not falsely included in the v1 promise.

Therefore:

**`v1.0 RELEASE READY`**

This means the merged PR #5 `main` may become the target of a later explicit `v1.0` tag/release operation. It does **not** mean that `v1.0` has already been released.

## 22. Exact next action

After PR #5 is merged:

1. retrieve the latest `main` SHA;
2. verify it is the PR #5 squash-merge SHA and that no intervening commit exists;
3. verify `v1.0` tag and GitHub Release are still absent;
4. prepare release notes from `V1_RELEASE_MANIFEST.md` and PR #1–#5 history;
5. only then, in a separate explicitly authorized operation, create immutable `v1.0` tag and GitHub Release.
