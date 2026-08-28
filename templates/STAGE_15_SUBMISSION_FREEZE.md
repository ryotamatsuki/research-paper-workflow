# Stage 15 — Submission Freeze

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as release manager for the research submission. Create an immutable, auditable record of exactly what is being submitted.

## 1. Project context

- Working title: `[WORKING_TITLE]`
- Target journal: `[TARGET_JOURNAL]`
- Repository: `[SOURCE_REPOSITORY]`
- Stage 14 result: `[CURRENT_STAGE_RESULT]`
- Current date: `[CURRENT_DATE]`

## 2. Stage objective

Freeze the validated manuscript, code, supplement, metadata, and disclosures at a canonical commit/tag so the submitted state can be reproduced later.

## 3. Canonical inputs

Only a Stage 14 `SUBMISSION QA PASS` or fully resolved `CONDITIONAL PASS` may enter this stage.

## 4. Allowed changes

None substantive. Administrative naming or packaging changes must not alter content.

## 5. Prohibited changes

No silent edits to theory, prose claims, equations, references, figures, tables, appendix, or disclosure after the frozen identifier is recorded.

## 6. Mandatory tasks

Record and preserve:

1. canonical commit SHA and, where useful, submission tag;
2. final manuscript PDF;
3. source archive;
4. appendix/supplement;
5. symbolic and numerical verification logs/outputs;
6. generated figures/tables and source scripts;
7. bibliography database;
8. cover letter and journal-required ancillary files;
9. disclosure/declaration statements;
10. journal submission metadata;
11. final file inventory and checksums/hashes where practical;
12. date/time and journal version of the submission package.

Confirm the repository working state corresponds to the recorded SHA and that all final files derive from it.

## 7. Evidence requirements

The freeze record itself is provenance evidence. It must not claim successful submission unless the platform submission is actually completed.

## 8. Verification protocol

Compare frozen artifacts against the Stage 14 QA inventory. Recompute hashes or inspect metadata where useful. Confirm no uncommitted/subsequent edit is being substituted for the frozen output.

## 9. Kill tests

Do not declare a freeze if:

- the canonical SHA is unclear;
- final PDF/source differ from the validated state;
- required disclosure or journal file is missing;
- a substantive correction is still pending.

## 10. Success criteria

The exact submitted package can be reconstructed and identified unambiguously months later.

## 11. Failure criteria

If any substantive issue emerges, reopen the affected stage, re-run QA, and create a new freeze. Never patch the frozen package silently.

## 12. Required final output

1. Submission-freeze verdict
2. Canonical SHA/tag
3. Final artifact inventory
4. Verification artifact inventory
5. Journal-specific files
6. Disclosure/declaration record
7. Hash/provenance record
8. Submission status (`FROZEN`, `UPLOADED`, `SUBMITTED`) with evidence
9. Any post-submission follow-up protocol

## 13. Final verdict

Choose one:

- `SUBMISSION FROZEN`
- `SUBMITTED` — only with actual submission confirmation
- `FREEZE BLOCKED`

## 14. Revision rule

Any later theoretical or substantive manuscript change reopens the relevant workflow stages and results in a new freeze identifier. The old submission state remains preserved for provenance.