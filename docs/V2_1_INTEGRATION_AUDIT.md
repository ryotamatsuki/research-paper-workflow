# v2.1 Integration Audit

Date: 2026-09-07

Scope: current `main` after PR #12, incorporating the v2.0 mathematical-certification architecture and the v2.1 live journal-compliance refinement.

## Executive verdict

**`WORKFLOW v2.1 READY`**

The current workflow is internally consistent and suitable for formal release as v2.1.

## Why v2.1 exists

A production IJIO submission was technically returned even though the internal manuscript QA had passed. The missed issues were operational rather than theoretical: editable LaTeX/source material was required, and author information had to appear in the main document. The prior workflow already said to check current journal rules, but it did not make that check sufficiently evidence-bearing or fail-closed.

v2.1 converts journal compliance from a generic checklist item into an auditable submission gate.

## Architecture compatibility

PASS.

The v2.0 mandatory mathematical architecture remains unchanged:

- Stage 4 `GO` → Stage 4A;
- Stage 4A `GO` → Stage 6;
- Stage 7.5 `GO` → Stage 7.5A;
- Stage 7.5A `GO` is required before Stage 8 theory freeze.

v2.1 adds no Stage, removes no Stage, changes no canonical verdict meaning, and changes no normal research routing. It strengthens Stages 12–15 and related checklists only.

## Journal-compliance lifecycle

PASS.

The submission lifecycle is now:

1. Stage 12 creates an initial Journal Requirements Ledger from current evidence.
2. Stage 13 carries verified journal requirements into manuscript/package integration and preserves unknowns as `UNVERIFIED`.
3. Stage 14 re-opens and dates current official requirements, refreshes the ledger, audits the exact source package, and fails closed on material unknowns/conflicts.
4. Stage 15 performs authenticated portal reconciliation, inspects the portal-generated PDF when applicable, and permits `SUBMITTED` only after actual confirmation.

## Evidence hierarchy

PASS.

The workflow now gives controlling priority to the most specific current evidence:

1. direct editorial-office instruction for the actual submission;
2. authenticated submission-portal instruction/required field/file designation;
3. journal-specific Guide for Authors / policy;
4. publisher-wide official guidance;
5. secondary source, previous submission, repository note, memory, or inference.

A lower-level source cannot override a more specific current source.

## Fail-closed behavior

PASS.

A material requirement marked `UNVERIFIED` or unresolved `CONFLICT` cannot receive full Stage-14 `SUBMISSION QA PASS`. If journal/publisher/portal research cannot resolve a material rule, clarification from the editorial office or submission support is required before full PASS.

The portal merely accepting a file or producing no warning is explicitly not treated as proof of technical compliance.

## Regression coverage

PASS.

The revised workflow directly covers the failure classes exposed by the IJIO technical return:

- PDF-only upload when editable source is required;
- missing `.tex`, `.bib`, figure, table, `.sty`, `.cls`, or `.bst` dependencies;
- wrong source-archive structure;
- anonymous manuscript when an identified manuscript is required, or the reverse;
- wrong title-page handling;
- corresponding-author mismatch;
- declaration/metadata inconsistency;
- failure to inspect the portal-generated PDF;
- reliance on remembered rules or prior internal assumptions.

## Version classification

PASS.

Under `docs/VERSIONING_POLICY.md`, the PR #12 refinement is MINOR relative to the v2.0 architecture because Stage identities, verdict semantics, routing, rollback, and freeze meanings are preserved. The formal release is therefore v2.1.

The v2.0 architecture was merged and audited on 2026-09-06 but was not separately published as a GitHub Release/tag. v2.1 is the first stable tagged release in the v2 line and includes the full v2.0 architecture plus the v2.1 journal-compliance hardening. Historical v1.0–v1.3 releases remain immutable.

## Final release gate

PASS.

No material integration blocker remains. Formal publication of v2.1 may proceed from a reviewed `main` state after readiness checks and release metadata finalization.