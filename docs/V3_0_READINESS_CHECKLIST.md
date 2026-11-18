# v3.0 Release Readiness

Date: 2026-11-19 JST.
Baseline: `v2.9` released 2026-10-12.
Status: **WORKFLOW v3.0 RELEASE READY** — publication job must independently verify tag and ancestry; checklist is not evidence that the GitHub release already exists.

## Architecture
- [x] Documented **MAJOR** classification for mandatory new Stage 10A / Stage 10B route.
- [x] Canonical Stage 9 → 10A → 10B → 11/12/13/14/15 route present.
- [x] Stage 10A `GO` is mandatory before manuscript rewriting; `CONDITIONAL GO` blocks 10B.
- [x] Stage 10B keeps the historical Stage 10 manuscript template file path.
- [x] Stage 4A and Stage 7.5A mathematical certification, author approval, theory-change rollback and Stage 15 portal gates remain controlling.
- [x] Prior `v2.9` tag and v2.9 readiness/notes remain unchanged.

## Source / writing tests
- [x] Lawful full text and material appendix **acquisition-before-scoring** enforced.
- [x] Actual complete reading and source-located writing techniques mandatory.
- [x] Default 3–5 role-based exemplars, justified smaller option and no mandatory anchor.
- [x] Introduction, proof, intuition, exhibits, limitations and journal fit role selection with coherence audit.
- [x] Source and reading provenance plus blueprint required before any 10B writing.
- [x] No exemplar prose copying, hidden theorem scope changes, or unsupported policy extensions.
- [x] Stage 11 independent cold-reader/editor attack; Stage 12 journal refresh; Stage 13 repair/retest; Stage 14 PDF validation.

## Release and boundary
- [x] Version headers in Governance/pipeline align with v3.0.
- [x] Release notes, manifest, integration audit and readiness file prepared.
- [x] One-off release workflow uses `contents: write`, exact commit-message trigger and tag-exists guard.
- [x] README transparently records v3.0 path, baseline and prior-draft migration.
- [ ] GitHub `v3.0` tag and published Release exist (verify **after** workflow run).
- [ ] Release job succeeded against the exact reviewed SHA (verify **after** workflow run).

Decision: **WORKFLOW v3.0 READY FOR TAG PUBLICATION**, conditional on GitHub Actions publishing and verifying the actual immutable tag.
