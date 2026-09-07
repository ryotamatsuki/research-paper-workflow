# v2.1 Readiness Checklist

Use before publishing the stable v2.1 tag/release.

## Canonical v2 architecture

- [x] Stage 4 `GO` routes to Stage 4A.
- [x] Stage 5 repair returns to Stage 4 then Stage 4A.
- [x] Stage 4A `GO` routes to Stage 6.
- [x] Stage 7.5 `GO` routes to Stage 7.5A.
- [x] Stage 7.5A `GO` is required before Stage 8.
- [x] Stage 8 blocks theory freeze without both independent certifications.
- [x] Stage 11 remains the late hostile regression layer.

## Journal-compliance gate

- [x] Stage 12 creates a Journal Requirements Ledger.
- [x] Stage 13 carries verified requirements into manuscript/package integration.
- [x] Stage 14 refreshes current official journal requirements immediately before submission freeze.
- [x] Stage 14 uses `JOURNAL_REQUIREMENTS_CHECKLIST.md`.
- [x] Material `UNVERIFIED` or unresolved `CONFLICT` blocks full Stage-14 PASS.
- [x] Material unresolved rules require editorial-office/submission-support clarification.
- [x] Portal acceptance or absence of a warning is not treated as proof of compliance.
- [x] Exact LaTeX/source archive is clean-extracted and compiled when applicable.
- [x] Anonymous/identified manuscript and title-page rules are checked explicitly.
- [x] Funding, competing interests, CRediT, AI, data/code, prior-publication and related declarations are reconciled.
- [x] Stage 15 requires authenticated portal preflight when applicable.
- [x] Portal-generated submission PDF is inspected when author approval is part of the workflow.
- [x] `SUBMITTED` requires actual journal/platform confirmation.

## Evidence discipline

- [x] Direct current editorial-office instructions outrank lower-level generic guidance for the actual submission.
- [x] Authenticated portal instructions outrank journal/publisher generic rules when they explicitly govern the submission.
- [x] Journal-specific official guidance outranks publisher-wide guidance.
- [x] Memory, prior submissions, and internal notes cannot close a material requirement by themselves.

## Release/version discipline

- [x] PR #12 preserves Stage structure, verdict semantics, routing, rollback and freeze meanings.
- [x] v2.1 is correctly classified as MINOR relative to the v2.0 architecture.
- [x] Historical v1.0–v1.3 tags/releases remain immutable.
- [x] v2.0 was merged/audited but not separately tagged; v2.1 will be the first stable tagged v2 release.
- [x] `docs/V2_1_INTEGRATION_AUDIT.md` reports **`WORKFLOW v2.1 READY`**.
- [x] Release notes and manifest are present.
- [x] Stable `v2.1` tag does not already exist before publication.

## Final verdict

[x] **`WORKFLOW v2.1 READY`**

Publication may proceed only if the release workflow re-verifies these markers and refuses to overwrite an existing v2.1 tag.