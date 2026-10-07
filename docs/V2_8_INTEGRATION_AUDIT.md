# v2.8 Integration Audit

Date: 2026-10-07  
Reviewed baseline: `91ecb3597183e4d420926cdc7b99744636e0690f` (stable v2.7)  
Candidate branch: `workflow/v2.8-bounded-research-search`

## Version classification and final judgment

**MINOR** under `docs/VERSIONING_POLICY.md`. Retain the existing architecture and strengthen search/selection evidence inside current Stages. The proposed wholesale Stage 0–8 replacement and mandatory mass-generation quotas are not adopted.

## Validation performed

- Read Governance, the full canonical pipeline, version policy, current release/audit records, and affected Stage/checklist controls from the pinned latest-main baseline.
- Manually reviewed the canonical/template diff for route compatibility, correction-route standards, early-versus-certified claim maturity, independent attack exposure, bounded expansion, and existing freeze protections.
- Deterministically compared all 19 canonical Stage headings and all 19 existing Stage-template identities; unchanged.
- Compared existing template final-verdict/next-stage-contract sections and Governance routing/rollback/freeze sections against baseline; unchanged.
- Confirmed formal-verification and paper-specific inheritance checklists, and all v2.7 release/audit records, remain unchanged.
- Checked changed-document relative links against the full baseline/new-file inventory, including directory links.
- Parsed the new release YAML and checked embedded shell syntax, main-only/explicit-publish trigger, baseline ancestry, and immutable-tag guard.
- Ran `git diff --check` with no whitespace errors.

These are integration/document/control checks, not an empirical demonstration that the research workflow produces better papers.

## Behavioral compatibility review

| Case | Required behavior |
|---|---|
| Many labels describe the same feedback structure | Merge duplicate candidate IDs; no novelty credit from volume |
| High-scoring candidate lacks closest-paper evidence | Retain uncertainty; score cannot authorize novelty PASS |
| Corrected known model changes a substantive equilibrium/welfare conclusion | Evaluate correction novelty and consequence; no forced unrelated mechanism; inherited certification still applies |
| Random search finds no counterexample | Numerical support only unless separate analytic/exact certification covers the claim |
| Family member changes strategic primitives or a headline claim | Existing rollback/change control and new applicable certification |
| New workflow version reaches an already frozen project | No automatic thaw or fabricated historical portfolio; new material defects use existing rollback |

## Findings repaired

The Stage-8 template's Stage-7.5A certificate label omitted `PORTABILITY`. Its name now matches the canonical pipeline; the underlying certificate requirement and route are unchanged.

## Routing regression

The core route remains:

`Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8`.

The Stage-5 one-diagnosed-fix repair still returns to Stage 4 then Stage 4A. Short memos and companion registers introduce no independent Stage verdicts or authorizations.

## Readiness verdict

**`WORKFLOW v2.8 READY`**

Readiness is distinct from GitHub publication; verify the merged commit, publishing run, immutable tag, and Release separately.
