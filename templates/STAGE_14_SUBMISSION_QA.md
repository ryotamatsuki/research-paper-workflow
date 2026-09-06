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

Catch any mathematical, bibliographic, build, formatting, disclosure, anonymity, artwork, or package inconsistency before submission freeze. Stage 14 verifies an already designed exposition architecture; it is not the normal place to discover that a central result still needs a figure or table.

## 3. Canonical inputs

Use the integrated manuscript from Stage 13, the theory freeze, reproducibility scripts, the final Figure/Table Architecture reconciliation, and current official journal instructions.

## 4. Allowed changes

Typographical fixes, formatting, metadata, verified citation corrections, build fixes, artwork/file-format fixes, and submission-package compliance changes that do not alter theory or substantive interpretation.

## 5. Prohibited changes

No silent theoretical edits, new propositions, new claims, substantive robustness results, or new numerical experiments. Do not invent a new central figure/table at Stage 14 to compensate for an exposition gap that should have been resolved at Stage 10/13. Any substantive need requires reopening the earliest affected stage.

## 6. Mandatory tasks

Use both `checklists/SUBMISSION_CHECKLIST.md` and `checklists/FIGURE_TABLE_CHECKLIST.md`. At minimum verify:

1. fresh clean build from documented environment;
2. all symbolic verification gates pass;
3. reported numerical results regenerate;
4. every quantitative figure/table regenerates from its verified source or generator;
5. representative plotted/tabulated values, thresholds, signs, and benchmark identities agree with the manuscript;
6. current journal artwork requirements are opened and dated, including figure/table count, placement, accepted file types, raster resolution, vector/font rules, color/grayscale, and separate-file requirements when applicable;
7. vector-graphic fonts are embedded when the journal requires embedding, and any raster output meets the applicable resolution requirement;
8. line styles, markers, labels, legends, captions, and table text remain intelligible at final manuscript size and do not depend on color alone unless the journal permits and accessibility remains adequate;
9. every figure/table is referenced in the text, numbered consistently, and accompanied by a caption/title that matches the actual object and scope;
10. all citations resolve and bibliographic metadata are verified;
11. cross-references, labels, footnotes, equations, appendices, and supplement are consistent;
12. no stale TODOs/placeholders/comments remain;
13. journal formatting, length, file-type, and anonymity requirements are current and satisfied;
14. title page, abstract, keywords/JEL, highlights, declarations, data/code statement, funding/conflicts are handled as required;
15. generative-AI/disclosure policy is checked against current official guidance;
16. cover letter and submission metadata agree with the manuscript;
17. source archive contains all required manuscript, figure/table source, generator, and output files and no unnecessary sensitive/internal files;
18. final PDF receives visual QA page by page, including every figure/table page at readable resolution.

## 7. Evidence requirements

Journal-specific requirements must come from current official sources. Do not rely on remembered submission rules. Record the exact figure/table/artwork requirements that were actually applicable to the submission package.

## 8. Verification protocol

Prefer a clean checkout/build or equivalent isolated verification. Record commands, environment, outputs, hashes where useful, and failures. Re-run failed gates after fixes. Where tooling permits, automate artwork kill tests such as missing files, stale regeneration, font embedding, raster dimensions/resolution, unresolved references, or source-archive omissions.

## 9. Kill tests

Submission freeze is blocked by:

- any failed mathematical/reproducibility gate affecting reported results;
- figure/table values that do not reproduce or disagree with manuscript claims;
- a vector/raster artwork defect that violates current journal requirements;
- unreadable labels, clipped visuals, overwide tables, or color-only distinctions that materially impair interpretation;
- missing figure/table source or required separate artwork file;
- orphan, duplicated, or misnumbered figure/table references;
- unresolved or fabricated citation;
- journal requirement violation;
- inconsistent appendix/supplement;
- anonymity/disclosure problem;
- theoretical change discovered during QA.

If Stage 14 discovers that a **central result lacks an appropriate exposition vehicle**, return to Stage 10 or Stage 13 depending on whether the missing work is architecture/design or bounded integration. Do not patch over that gap with an unverified last-minute visual.

## 10. Success criteria

All material checks pass, or any non-material warning is documented and accepted explicitly. The final package must be mathematically reproducible, visually legible, journal-compliant, and self-contained enough that figures/tables do not create a second, inconsistent statement of the results.

## 11. Failure criteria

Return to the relevant earlier stage when a problem is substantive rather than formatting/packaging. Bounded artwork-format defects may be repaired within Stage 14 if the underlying verified object and interpretation remain unchanged.

## 12. Required final output

1. Executive QA verdict
2. Clean-build result
3. Symbolic/numerical verification result
4. Figure/table regeneration and numerical-integrity result
5. Artwork-format/accessibility result
6. Bibliography/reference result
7. Journal-format/policy result
8. Anonymity/disclosure result
9. PDF visual QA result
10. Package inventory, including figure/table sources/generators
11. Remaining warnings
12. Verdict and Stage 15 contract

## 13. Final verdict

Choose one:

- `SUBMISSION QA PASS`
- `CONDITIONAL PASS` — non-substantive fixes only
- `FAIL — REOPEN EARLIER STAGE`

## 14. Next-stage contract

Stage 15 records an immutable submission state. No substantive change is allowed between QA pass and freeze. Final figure/table outputs and generators used for the submission must be part of the frozen provenance.