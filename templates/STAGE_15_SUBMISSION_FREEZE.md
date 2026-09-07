# Stage 15 — Submission Freeze

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as release manager for the research submission. Create an immutable, auditable record of exactly what is being submitted and complete the final authenticated portal reconciliation when required.

## 1. Project context

- Working title: `[WORKING_TITLE]`
- Target journal: `[TARGET_JOURNAL]`
- Repository: `[SOURCE_REPOSITORY]`
- Stage 14 result: `[CURRENT_STAGE_RESULT]`
- Current date: `[CURRENT_DATE]`

## 2. Stage objective

Freeze the validated manuscript, code, supplement, metadata, disclosures, Journal Requirements Ledger, and portal-ready source package at a canonical commit/tag so the submitted state can be reproduced later.

Where the journal uses an authenticated submission portal, complete the live portal preflight before the final submit action and verify the portal-generated submission PDF when available.

## 3. Canonical inputs

A Stage 14 `SUBMISSION QA PASS`, fully resolved `CONDITIONAL PASS`, or `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED` may enter this stage.

The special authenticated-portal conditional status permits entry only for the purpose of resolving the explicitly listed portal-only items. It does not permit submission with unresolved material requirements.

## 4. Allowed changes

None substantive. Administrative naming, file designation, or packaging changes must not alter content.

If the live portal reveals a previously unknown journal requirement, make only the bounded compliance change required, record the source and conflict, rerun affected Stage-14 checks, and create a new freeze identifier if any frozen artifact changes.

## 5. Prohibited changes

No silent edits to theory, prose claims, equations, references, figures, tables, appendix, author information, or disclosure after the frozen identifier is recorded.

Do not click final submit while a material portal requirement, generated-PDF defect, author/corresponding-author mismatch, anonymity mismatch, or file-designation uncertainty remains unresolved.

## 6. Mandatory tasks

Record and preserve:

1. canonical commit SHA and, where useful, submission tag;
2. final manuscript PDF;
3. exact source archive intended for upload;
4. appendix/supplement;
5. symbolic and numerical verification logs/outputs;
6. generated figures/tables and source scripts;
7. bibliography database and required LaTeX/style/class dependencies;
8. cover letter and journal-required ancillary files;
9. disclosure/declaration statements;
10. journal submission metadata;
11. final refreshed `JOURNAL_REQUIREMENTS_LEDGER.md` or equivalent;
12. final file inventory and checksums/hashes where practical;
13. date/time and journal version of the submission package.

Confirm the repository working state corresponds to the recorded SHA and that all final files derive from it.

### Authenticated portal preflight

Before the final submit action, when an authenticated portal is used:

1. open the actual submission record rather than a generic journal page;
2. inspect current required fields, file designations, warnings, and declarations;
3. reconcile every portal requirement with the Journal Requirements Ledger;
4. confirm article type, title, abstract, keywords/JEL/classifications, and editor/topic selections;
5. confirm author names/order, affiliations, emails/ORCID, and corresponding-author designation exactly match the intended manuscript/title page;
6. confirm whether the main document must be identified or anonymous and verify the uploaded file accordingly;
7. confirm title-page handling and any separate author-information file requirement;
8. confirm each uploaded manuscript/source/figure/table/supplement/cover-letter/highlight file has the correct portal designation;
9. for LaTeX, confirm the actual editable source/archive and required figure/bibliography/style/class files are included in the form the portal accepts;
10. confirm funding, competing interests, CRediT/author contribution, AI, data/code, ethics, prior-publication/preprint, and author-attestation fields agree with the frozen declarations;
11. resolve all portal warnings or record why a warning is non-material and accepted;
12. build/generate the portal submission PDF when supported;
13. inspect the portal-generated PDF page by page, including the first page, equations, references, figures, tables, appendix, declarations, and identifying/anonymity information;
14. verify no file is missing, duplicated, stale, or misdesignated;
15. only then perform the final submission action.

If a direct editorial-office instruction or authenticated portal requirement conflicts with a lower-level Guide/publisher/internal source, the current more-specific instruction controls the actual submission. Record the conflict and rerun affected Stage-14 checks before proceeding.

## 7. Evidence requirements

The freeze record itself is provenance evidence. It must not claim successful submission unless the platform submission is actually completed.

For journal compliance, retain enough evidence to show which current source controlled each material decision. Do not preserve passwords, private tokens, or other authentication secrets.

## 8. Verification protocol

Compare frozen artifacts against the Stage 14 QA inventory and refreshed Journal Requirements Ledger. Recompute hashes or inspect metadata where useful. Confirm no uncommitted/subsequent edit is being substituted for the frozen output.

Compare the portal-generated PDF with the locally validated manuscript and inspect any conversion difference that could affect author identification, equations, citations, figures/tables, pagination, appendices, or declarations.

## 9. Kill tests

Do not declare a freeze or submission if:

- the canonical SHA is unclear;
- final PDF/source differ from the validated state;
- required disclosure or journal file is missing;
- a substantive correction is still pending;
- any material Journal Requirements Ledger item remains `UNVERIFIED` or unresolved `CONFLICT`;
- the authenticated portal exposes an unresolved required field or file designation;
- author/affiliation/corresponding-author information differs across manuscript, title page, source, and portal;
- anonymity/identification behavior differs from the current operative rule;
- the portal-generated PDF has not been inspected when the system requires author approval of that PDF;
- the portal-generated PDF contains a material rendering/conversion defect;
- the final confirmation action has not actually completed.

## 10. Success criteria

The exact submitted package can be reconstructed and identified unambiguously months later, and the live submission record is consistent with the current journal requirements that governed the upload.

## 11. Failure criteria

If any substantive issue emerges, reopen the affected stage, re-run QA, and create a new freeze. Never patch the frozen package silently.

If the issue is a bounded journal-compliance defect, repair it under Stage 14, rerun the affected checks, and replace the freeze identifier before final submission.

## 12. Required final output

1. Submission-freeze verdict
2. Canonical SHA/tag
3. Final artifact inventory
4. Verification artifact inventory
5. Journal-specific files
6. Journal Requirements Ledger status
7. Disclosure/declaration record
8. Hash/provenance record
9. Authenticated portal preflight result
10. Portal-generated PDF inspection result when applicable
11. Submission status (`FROZEN`, `UPLOADED`, `SUBMITTED`) with evidence
12. Any post-submission follow-up protocol

## 13. Final verdict

Choose one:

- `SUBMISSION FROZEN` — validated package frozen, but final portal submission not yet completed;
- `UPLOADED — PORTAL PREFLIGHT PENDING/IN PROGRESS` — files are in the portal but final reconciliation is incomplete;
- `SUBMITTED` — only after authenticated portal reconciliation, generated-PDF approval where applicable, final submit action, and actual journal/platform confirmation;
- `FREEZE BLOCKED`.

## 14. Revision rule

Any later theoretical or substantive manuscript change reopens the relevant workflow stages and results in a new freeze identifier. The old submission state remains preserved for provenance.

Any later journal-specific technical return is treated as workflow evidence: record which requirement was missed, why the preflight failed to detect it, and convert that failure mode into a reusable Stage-14/15 regression check where appropriate.