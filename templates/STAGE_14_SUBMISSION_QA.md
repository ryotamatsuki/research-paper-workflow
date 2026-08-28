# Stage 14 — Submission QA

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a submission-quality auditor. Verify the complete package from a clean state against current journal requirements and the frozen research record.

## 1. Project context

- Working title: `[WORKING_TITLE]`
- Primary journal: `[TARGET_JOURNAL]`
- Repository: `[SOURCE_REPOSITORY]`
- Theory freeze: `[CANONICAL_MODEL]`
- Current date: `[CURRENT_DATE]`

## 2. Stage objective

Catch any mathematical, bibliographic, build, formatting, disclosure, anonymity, or package inconsistency before submission freeze.

## 3. Canonical inputs

Use the integrated manuscript from Stage 13, the theory freeze, reproducibility scripts, and current official journal instructions.

## 4. Allowed changes

Typographical fixes, formatting, metadata, verified citation corrections, build fixes, and submission-package compliance changes that do not alter theory.

## 5. Prohibited changes

No silent theoretical edits, new propositions, new claims, or substantive robustness results. Any such need requires reopening an earlier stage.

## 6. Mandatory tasks

Use `checklists/SUBMISSION_CHECKLIST.md`. At minimum verify:

1. fresh clean build from documented environment;
2. all symbolic verification gates pass;
3. reported numerical results regenerate;
4. figures/tables regenerate from source;
5. all citations resolve and bibliographic metadata are verified;
6. cross-references, labels, footnotes, equations, appendices, and supplement are consistent;
7. no stale TODOs/placeholders/comments remain;
8. journal formatting, length, file-type, and anonymity requirements are current and satisfied;
9. title page, abstract, keywords/JEL, highlights, declarations, data/code statement, funding/conflicts are handled as required;
10. generative-AI/disclosure policy is checked against current official guidance;
11. cover letter and submission metadata agree with the manuscript;
12. source archive contains all required files and no unnecessary sensitive/internal files;
13. final PDF receives visual QA page by page.

## 7. Evidence requirements

Journal-specific requirements must come from current official sources. Do not rely on remembered submission rules.

## 8. Verification protocol

Prefer a clean checkout/build or equivalent isolated verification. Record commands, environment, outputs, and failures. Re-run failed gates after fixes.

## 9. Kill tests

Submission freeze is blocked by:

- any failed mathematical/reproducibility gate affecting reported results;
- unresolved or fabricated citation;
- journal requirement violation;
- inconsistent appendix/supplement;
- anonymity/disclosure problem;
- theoretical change discovered during QA.

## 10. Success criteria

All material checks pass, or any non-material warning is documented and accepted explicitly.

## 11. Failure criteria

Return to the relevant earlier stage when a problem is substantive rather than formatting/packaging.

## 12. Required final output

1. Executive QA verdict
2. Clean-build result
3. Symbolic/numerical verification result
4. Figure/table regeneration result
5. Bibliography/reference result
6. Journal-format/policy result
7. Anonymity/disclosure result
8. PDF visual QA result
9. Package inventory
10. Remaining warnings
11. Verdict and Stage 15 contract

## 13. Final verdict

Choose one:

- `SUBMISSION QA PASS`
- `CONDITIONAL PASS` — non-substantive fixes only
- `FAIL — REOPEN EARLIER STAGE`

## 14. Next-stage contract

Stage 15 records an immutable submission state. No substantive change is allowed between QA pass and freeze.