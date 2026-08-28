# Workflow v1 Integration Changelog

This file records only the minimal harmonizations made during PR #4 after the integration audit. It is not a general release changelog.

## V1-001 — Canonical verdict versus routing/status

Affected:

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Change:

- canonical stage verdict is always `GO / CONDITIONAL GO / NO-GO`;
- subtests may use `PASS / CONDITIONAL / FAIL`;
- operational labels such as `GO TO STAGE 6`, `THEORY FROZEN`, or `SUBMISSION QA PASS` are secondary route/status outputs.

Reason: prevent route labels from weakening or obscuring stage decisions.

## V1-002 — Rollback and stale-state policy

Affected:

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Change:

A later substantive error now returns the project to the earliest stage whose output was invalidated. Dependent downstream artifacts are stale until necessary stages are re-run.

Reason: prevent Stage 11/13/14 findings from being silently patched only in prose or packaging.

## V1-003 — Stage 4 routing

Affected:

- `templates/STAGE_04_MINIMAL_MODEL.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Change:

- `GO` → Stage 6 Novelty Re-Kill;
- `CONDITIONAL GO` with one diagnosed repair → Stage 5 Mechanism Hardening;
- `NO-GO` → stop; only a genuinely distinct Stage 3/0 pivot may restart research.

Reason: close a complexity-rescue loophole.

## V1-004 — Theory-method scope

Affected:

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- root `README.md`

Change:

v1 is explicitly a theory-oriented economics pipeline. Stages 0–3 may recommend another method, but non-theory projects should leave the canonical theory path instead of pretending to pass Stage 4. Verification items may be `NOT APPLICABLE` only with justification.

Reason: prevent systematic misrouting of policy/institutional or empirical-first projects.

## V1-005 — Evidence maturity / AI provenance

Affected:

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Change:

Distinguish conversation/scratch-reported outputs, repository-reproduced results, source-verified facts/literature, submission-level verification, conjectures/model assumptions, and rejected claims.

Reason: PR #3 showed that provenance maturity is essential in AI-assisted research.

## V1-006 — Literature continuity

Affected:

- `THEORY_PAPER_RESEARCH_PIPELINE.md`

Change:

Stage 2 establishes the baseline literature ledger. Stages 3/5/6/7/12 perform targeted updates for their distinct purposes rather than automatically repeating the full search from zero.

Reason: reduce unnecessary research cost without weakening novelty verification.

## No structural additions

PR #4 deliberately does **not** add:

- a new stage;
- a new worked case;
- an empirical pipeline;
- CI/automation;
- YAML/machine-readable metadata;
- a v1.0 tag or release;
- a paper/model extension.
