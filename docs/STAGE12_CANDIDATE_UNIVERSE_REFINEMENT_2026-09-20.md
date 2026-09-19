# Stage-12 Journal Candidate-Universe Refinement — 2026-09-20

## Problem

A journal-positioning stage can perform careful current-scope and submission-rule research yet still produce an unreliable ranking if the initial candidate set is incomplete. The failure mode is **candidate-set omission**, not necessarily bad comparison logic.

The triggering regression was a correction-paper case in which a natural field journal represented repeatedly in the closest literature was not evaluated before the primary outlet was selected. The workflow already required examination of serious candidates but did not make candidate-universe construction and completeness explicit enough.

## General solution

The refinement is intentionally paper-type agnostic.

1. Build the broad candidate universe from the Stage-11-surviving paper: field/audience, contribution/article type, methodological level, manuscript scale, and materially relevant audience constraints.
2. Use venues from the closest literature as a completeness cross-check only. A close paper's venue is neither automatically included nor silently ignorable.
3. Require an explicit exclusion reason for obvious field journals or repeatedly represented relevant venues that are not serious candidates.
4. Only for correction, comment, replication, re-examination, or closely related source-audit papers, explicitly evaluate the target/source paper's journal unless there is a documented exclusion reason.
5. Preserve a Candidate-Universe Ledger before ranking.
6. If a material omitted venue is discovered later, reopen Stage 12 rather than changing theory or pretending the earlier ranking covered it.

## Why this is not correction-paper-specific

The generic rule is contribution-first candidate generation plus completeness auditing. The source-journal rule is explicitly conditional. Ordinary original research is not forced toward the journals of its closest papers.

This avoids two opposite errors:

- **omission error:** a natural field outlet is never evaluated;
- **lineage lock-in:** a paper is mechanically routed to the journals that published its closest predecessors.

## Compatibility

No Stage is added, removed, renamed, or rerouted. Canonical verdict meanings are unchanged. The change strengthens an existing Stage-12 decision gate and is therefore minor-version compatible under `docs/VERSIONING_POLICY.md`.

Prospective version: **v2.3**.
