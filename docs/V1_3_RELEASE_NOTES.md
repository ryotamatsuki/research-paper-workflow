# research-paper-workflow v1.3

Release date: 2026-09-06

## Summary

v1.3 adds a backward-compatible **result-to-exposition and figure/table architecture lifecycle** to the existing Stage 0–15 theory workflow.

The change was prompted by a production-paper submission audit in which the mathematics, novelty, and submission package were already mature, but a central sign-reversal result was only recognized as needing a figure after Stage 14. That caused avoidable Stage-13 reintegration and Stage-14 re-QA. The subsequent re-QA also exposed a vector-font embedding defect that belonged in normal artwork QA.

v1.3 moves those decisions and checks earlier without adding or renumbering any Stage.

## What changes

### Stage 7 — identify

Every surviving headline result receives a result-to-exposition triage. Candidate vehicles are theorem/proposition, figure, table, numerical illustration, or concise prose.

There is no minimum figure quota.

### Stage 10 — design and implement

A mandatory Figure/Table Architecture Gate is completed before the Introduction is finalized. Every headline result gets one primary exposition vehicle, and every required quantitative figure/table must be reproducibly generated from verified model objects or authoritative source data.

### Stage 13 — integrate

The Stage-10 architecture is reconciled with the selected journal. Figure/table placement, captions, references, and journal-specific presentation are finalized. Bounded presentation of already verified results is allowed; new substantive computation requires rollback.

### Stage 14 — verify

Submission QA now explicitly checks:

- figure/table regeneration;
- numerical integrity against manuscript checkpoints;
- current journal artwork rules;
- vector-font embedding where required;
- raster resolution where applicable;
- grayscale/color/accessibility and final-size legibility;
- source/generator inclusion in the submission package;
- page-by-page visual QA.

A central missing exposition vehicle discovered at Stage 14 routes back to Stage 10/13 rather than being patched with an unverified last-minute visual.

## New checklist

- `checklists/FIGURE_TABLE_CHECKLIST.md`

The existing `SUBMISSION_CHECKLIST.md` is also expanded to incorporate artwork and figure/table package checks.

## Compatibility

This is a **MINOR** release under `docs/VERSIONING_POLICY.md`.

v1.3 does **not** change:

- Stage numbering or identity;
- canonical hierarchy;
- `GO / CONDITIONAL GO / NO-GO` semantics;
- normal Stage routing;
- one-diagnosed-fix discipline;
- rollback/stale-state behavior;
- theory-freeze or submission-freeze meaning.

Existing v1 projects remain interpretable under the same architecture. Active projects may optionally re-audit their exposition architecture under the stronger v1.3 checks.

## Historical releases

`v1.0`, `v1.1`, and `v1.2` remain immutable historical releases.
