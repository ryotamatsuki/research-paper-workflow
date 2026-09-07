# research-paper-workflow v2.1

Release date: 2026-09-07

## Summary

v2.1 is the first stable tagged release in the v2 line. It includes the v2.0 mathematical-adversarial-certification architecture and adds fail-closed, evidence-bearing journal-compliance controls before submission.

The release was prompted by a real production-paper technical return: an IJIO submission passed internal QA but still required editable LaTeX/source material and author information in the main document. The prior workflow instructed authors to check current journal rules, but that instruction was too easy to satisfy without preserving evidence or resolving ambiguity.

v2.1 makes current journal compliance an auditable gate rather than a remembered convention.

## v2 architecture retained

The release includes the major v2.0 architecture:

- Stage 4A — Independent Mathematical Adversarial Certification;
- Stage 7.5A — Generality / Quantifier Red-Team;
- mandatory certification before Stage 8 theory freeze;
- fail-closed global/off-path equilibrium verification;
- theorem-scope and quantifier discipline;
- benchmark-definition discipline;
- Stage-11 certification-regression attack.

## New in v2.1 — Journal Requirements Ledger

For the selected primary journal, Stage 12 now establishes an auditable Journal Requirements Ledger. Material requirements record the current source, access/receipt date, operative rule, affected artifact/portal field, verification method, and status.

Stage 14 refreshes this ledger from current official evidence immediately before submission freeze.

## Evidence hierarchy

For an actual submission, the most specific current evidence controls:

1. direct editorial-office instruction for the submission;
2. authenticated submission-portal instruction/required field/file designation;
3. journal-specific Guide for Authors / policy page;
4. publisher-wide official guidance;
5. secondary source, prior submission, repository note, memory, or inference.

Lower-level evidence cannot override a more specific current instruction.

## Fail-closed journal compliance

A material requirement marked `UNVERIFIED` or unresolved `CONFLICT` cannot receive full Stage-14 `SUBMISSION QA PASS`.

If official journal/publisher guidance and the authenticated portal do not resolve a material rule, the workflow requires clarification from the editorial office or submission support before full PASS.

A portal accepting a file, allowing the workflow to continue, or producing no warning is not by itself proof that editorial-office technical requirements are satisfied.

## Source-package QA

For LaTeX submissions, v2.1 explicitly checks the actual upload package, including as applicable:

- `.tex` sources;
- `.bib`/bibliography files;
- figures and table sources;
- nonstandard `.sty`, `.cls`, `.bst`, and other dependencies;
- archive/folder-layout restrictions;
- clean extraction and compilation of the exact archive intended for upload;
- consistency between the generated PDF and intended manuscript.

## Author identification and declarations

The workflow explicitly verifies whether the journal requires an anonymous or identified main manuscript, separate title page, affiliations, author email, and corresponding-author designation.

It also reconciles Funding, Competing interests, CRediT/author contributions, AI disclosure, data/code statements, prior-publication questions, and related portal metadata.

## Authenticated portal preflight

Stage 15 now requires, when applicable:

- opening the actual submission record;
- checking current required fields and file designations;
- reconciling authors/affiliations/corresponding author;
- reconciling declarations and attestations;
- resolving portal warnings;
- generating the platform submission PDF when supported;
- inspecting that PDF page by page;
- confirming no file is missing, stale, duplicated, or misdesignated;
- preserving actual submission confirmation before declaring `SUBMITTED`.

## Compatibility

The v2.1 journal-compliance refinement is MINOR relative to the v2.0 architecture. It does not add/remove/renumber Stages, change `GO / CONDITIONAL GO / NO-GO` semantics, change normal research routing, weaken one-diagnosed-fix discipline, or change theory-freeze meaning.

## Release history note

The v2.0 architecture was merged and integration-audited on 2026-09-06 but was not separately published as a GitHub Release/tag. v2.1 is therefore the first stable tagged v2 release and includes all v2.0 functionality.

Historical v1.0, v1.1, v1.2, and v1.3 releases remain immutable.