# research-paper-workflow v3.1 — Integrated Independent Publication Prose Gates

Release date: 2026-11-19. Minor release on the **unchanged v3.0 stage architecture**.

## Change

- **Stage 11, draft:** separate source-located communication-only referee tests scholarly English, defensive novelty prose, internal workflow contamination, repeated qualifications, and economic intuition around theorems. The first reading precedes actual fully read exemplar comparisons. This review applies to the *draft* only.
- **Stage 13, final:** after all integration and journal calibration, require a different reader's genuinely independent full-PDF initial prose review, saved before full-text published exemplars are revealed; evidence-backed comparisons by writing role; bounded repairs with theorem/counterexample/AI-claim protections; an independent second full cold reading; accepted source commit SHA and PDF SHA-256. Missing evidence, unresolved major issues or stale text block Stage-13 GO.
- **Stages 14–15, package:** reconcile the submission-facing source/PDF with the Stage-13 prose-accepted snapshot and independently retest later manuscript changes, including captions, appendices and declarations.
- Adds the complete-paper Stage-13 template/checklist, fifteen synthetic regression cases, version-impact and integration design documents, and structural CI contract.

## Compatibility

This is a **MINOR** release. No numbered Stage 13P exists, no Stage is added/removed/renamed, normal `GO / CONDITIONAL GO / NO-GO` meanings and stage routing remain unchanged, and frozen scientific conclusions remain subject to existing upstream rollback rules. v3.0 remains an immutable historical tag. The superseded v4.0 Stage-13P draft was **not** released.

## Validation and limitations

Draft PR #35's integrated structural CI succeeded (run [44484752077](https://github.com/ryotamatsuki/research-paper-workflow/actions/runs/44484752077)); release workflow reruns the structural check. Automated tests verify contract presence, not true reviewer independence, whole-paper comprehension, exemplar access or journal acceptance.

Retrospective Green Subsidies prose review found author-workflow residue and excessive defensive narration under a manuscript originally cleared using *v1.1*. This is an informative diagnostic **not** a valid v3.1 Stage-13 GO: the exact final PDF needs genuine initial full-paper blind reading and an independent post-repair complete re-read.

Release contract validation: the README describes v3.1 as adopted after merge; the structural checker accepts that completed state rather than requiring the historical proposal label.
