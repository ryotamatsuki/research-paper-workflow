# v1.3 Release Manifest

Prospective release: `v1.3`

Status before publication: **release-ready candidate**

Stable baseline: `v1.2` at `944e6bace951e13645b02200a63bf25363dc7242`.

Release PR: #10 — `v1.3: result-to-exposition and figure/table architecture`.

## Canonical files changed

- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_07_WELFARE_GENERALITY.md`
- `templates/STAGE_10_PAPER_BUILD.md`
- `templates/STAGE_13_FULL_PAPER_INTEGRATION.md`
- `templates/STAGE_14_SUBMISSION_QA.md`

## Canonical/supporting checklist changes

- new `checklists/FIGURE_TABLE_CHECKLIST.md`
- updated `checklists/SUBMISSION_CHECKLIST.md`
- updated `checklists/REFEREE_ATTACK_CHECKLIST.md`

## Release and version documentation

- `README.md`
- `docs/VERSIONING_POLICY.md`
- `docs/WORKFLOW_V1_3_INTEGRATION_AUDIT.md`
- `docs/WORKFLOW_V1_3_READINESS_CHECKLIST.md`
- `docs/V1_3_RELEASE_NOTES.md`
- `docs/V1_3_RELEASE_MANIFEST.md`
- `.github/workflows/publish-v1.3.yml`

## Compatibility contract

v1.3 preserves:

- Stage numbering and identity;
- canonical hierarchy;
- `GO / CONDITIONAL GO / NO-GO` semantics;
- normal routing;
- one-diagnosed-fix discipline;
- rollback/stale-state policy;
- theory-freeze semantics;
- submission-freeze semantics.

The release is therefore classified as **MINOR**.

## Functional contract

The v1.3 exposition lifecycle is:

1. Stage 7 — identify candidate exposition vehicles;
2. Stage 10 — decide and reproducibly implement the figure/table architecture;
3. Stage 13 — integrate the architecture for the selected journal;
4. Stage 14 — verify regeneration, numerical integrity, artwork compliance, package completeness, and visual legibility.

There is no minimum figure/table quota.

## Release gate

Release only if:

- `docs/WORKFLOW_V1_3_INTEGRATION_AUDIT.md` contains **`WORKFLOW v1.3 READY`**;
- `docs/WORKFLOW_V1_3_READINESS_CHECKLIST.md` is fully checked and contains **`WORKFLOW v1.3 READY`**;
- PR #10 contains no incompatible Stage/verdict/routing change;
- `v1.3` tag is absent before publication;
- the release automation successfully finalizes metadata and creates tag/release `v1.3` without modifying historical tags.

## Final release SHA

The definitive release SHA is intentionally not predeclared in this candidate manifest. `.github/workflows/publish-v1.3.yml` creates a final metadata commit after the reviewed PR lands on `main`, then tags that finalized commit as `v1.3`. The tag target is the authoritative release SHA.
