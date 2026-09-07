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

Catch any mathematical, bibliographic, build, formatting, disclosure, anonymity, artwork, source-package, metadata, or portal inconsistency before submission freeze.

Stage 14 verifies an already designed exposition architecture; it is not the normal place to discover that a central result still needs a figure or table.

Stage 14 is also the mandatory **live journal-compliance gate**. A project may not pass this stage merely because an internal checklist, old repository note, previous submission, or remembered rule says the package is compliant.

## 3. Canonical inputs

Use the integrated manuscript from Stage 13, the theory freeze, reproducibility scripts, the final Figure/Table Architecture reconciliation, the Stage-12 Journal Requirements Ledger, and current official journal instructions.

The Stage-12 requirements snapshot is not presumed current. Re-open and date the operative official sources at Stage 14.

## 4. Allowed changes

Typographical fixes, formatting, metadata, verified citation corrections, build fixes, artwork/file-format fixes, source-package fixes, and submission-package compliance changes that do not alter theory or substantive interpretation.

## 5. Prohibited changes

No silent theoretical edits, new propositions, new claims, substantive robustness results, or new numerical experiments. Do not invent a new central figure/table at Stage 14 to compensate for an exposition gap that should have been resolved at Stage 10/13. Any substantive need requires reopening the earliest affected stage.

Do not guess a journal requirement in order to close QA. Material unknowns remain `UNVERIFIED` and fail closed.

## 6. Mandatory tasks

Use all three:

- `checklists/SUBMISSION_CHECKLIST.md`;
- `checklists/JOURNAL_REQUIREMENTS_CHECKLIST.md`;
- `checklists/FIGURE_TABLE_CHECKLIST.md`.

At minimum verify:

1. fresh clean build from documented environment;
2. all symbolic verification gates pass;
3. reported numerical results regenerate;
4. every quantitative figure/table regenerates from its verified source or generator;
5. representative plotted/tabulated values, thresholds, signs, and benchmark identities agree with the manuscript;
6. the selected journal's current Guide for Authors / Instructions for Authors and relevant journal-specific policy pages are opened and dated;
7. the Journal Requirements Ledger is refreshed item by item from current official evidence;
8. article type/category and submission system are confirmed;
9. review/anonymity model is confirmed, including whether author names, affiliations, email, acknowledgments, funding, and other identifying information belong in the main manuscript, a separate title page, both, or neither;
10. title-page, author-order, affiliation, email, ORCID, and corresponding-author rules are confirmed and mapped to actual files/portal metadata;
11. accepted initial-submission file types are confirmed, including whether PDF-only submission is permitted or editable Word/LaTeX source is required at initial submission;
12. for LaTeX, source-package requirements are confirmed explicitly: `.tex`, `.bib`/bibliography, figure files, table/source files, custom style/class/bibliography files when needed, archive type, and any flat-folder/subfolder restriction;
13. the actual LaTeX/source archive is extracted to a clean location and compiles using the structure that will be submitted;
14. current journal artwork requirements are opened and dated, including figure/table count, placement, accepted file types, raster resolution, vector/font rules, color/grayscale, accessibility, and separate-file requirements when applicable;
15. vector-graphic fonts are embedded when required, and any raster output meets the applicable resolution requirement;
16. line styles, markers, labels, legends, captions, and table text remain intelligible at final manuscript size and do not depend on color alone unless the journal permits and accessibility remains adequate;
17. every figure/table is referenced in the text, numbered consistently, and accompanied by a caption/title that matches the actual object and scope;
18. all citations resolve and bibliographic metadata are verified;
19. cross-references, labels, footnotes, equations, appendices, and supplement are consistent;
20. no stale TODOs/placeholders/comments remain;
21. manuscript-format, length, abstract, keyword, JEL/classification, highlight, graphical-abstract, line-numbering, spacing, reference-style, and supplement requirements are current and satisfied where applicable;
22. declarations are checked against current journal/publisher policy and the actual paper: funding, competing interests, CRediT/author contribution, data availability, code availability, ethics/consent, acknowledgments, and generative-AI/AI-assisted technologies;
23. prior-publication/preprint/thesis/conference-paper questions are checked where relevant;
24. cover letter, submission metadata, manuscript, title page, source archive, supplement, and declarations agree exactly;
25. suggested/opposed reviewers, editor/section/topic classifications, author attestations, and other mandatory portal metadata are identified where applicable;
26. current submission fees, mandatory publication/page/color charges, APC/open-access options, and licensing choices are distinguished and checked when material;
27. the source archive contains all required manuscript and figure/table source files and no unnecessary sensitive/internal files;
28. final locally generated PDF receives visual QA page by page, including every figure/table page at readable resolution;
29. authenticated portal-only requirements are either checked directly or explicitly isolated as the sole remaining `CONDITIONAL PASS` item for Stage 15 preflight.

## 7. Journal-requirement evidence hierarchy

When requirements conflict, use and record the most specific current authority:

1. direct current instruction from the journal/editorial office applying to the actual submission;
2. current authenticated submission-portal instruction, required field, file designation, warning, or generated-PDF behavior;
3. current journal-specific Guide for Authors / Instructions for Authors / journal policy page;
4. current publisher-wide official guidance;
5. secondary source, previous submission, internal repository note, memory, or inference.

A lower-level source may fill a gap provisionally but may not override a more specific current source. A prior workflow assumption does not survive a contradictory current journal instruction.

## 8. Evidence requirements

Journal-specific requirements must come from current official sources. Do not rely on remembered submission rules.

Maintain `JOURNAL_REQUIREMENTS_LEDGER.md` or an equivalent auditable artifact in the production repository. For every material requirement record:

- requirement/topic;
- source URL or identifiable direct journal communication;
- source level from the hierarchy above;
- access/receipt date;
- operative rule;
- affected file/metadata/portal field;
- verification method;
- status: `PASS`, `NOT APPLICABLE`, `UNVERIFIED`, or `CONFLICT`;
- conflict-resolution note where needed.

A checked box without supporting evidence does not close a material requirement.

## 9. Verification protocol

Prefer a clean checkout/build or equivalent isolated verification. Record commands, environment, outputs, hashes where useful, and failures. Re-run failed gates after fixes.

Where tooling permits, automate kill tests such as missing source files, stale regeneration, font embedding, raster dimensions/resolution, unresolved references, source-archive omissions, anonymous/identified manuscript mismatch, and required declaration text.

For LaTeX, test the exact archive layout that will be uploaded, not merely the repository build tree.

If authenticated portal access is available, perform the portal preflight in Stage 14. If it is not yet available or must occur only at the final submission step, Stage 14 may return only `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`, provided every non-portal item passes and the remaining uncertainty genuinely depends on authenticated access.

## 10. Kill tests

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
- anonymity/author-identification mismatch;
- title-page/corresponding-author mismatch;
- missing required editable source, bibliography, figure file, style/class file, or other source-package component;
- source archive that fails clean extraction/compilation under the submitted layout;
- disclosure/declaration inconsistency;
- any material Journal Requirements Ledger item marked `UNVERIFIED`;
- any unresolved material `CONFLICT` between official sources;
- reliance on memory/inference where a current official requirement should be verified;
- theoretical change discovered during QA.

If Stage 14 discovers that a **central result lacks an appropriate exposition vehicle**, return to Stage 10 or Stage 13 depending on whether the missing work is architecture/design or bounded integration. Do not patch over that gap with an unverified last-minute visual.

## 11. Success criteria

All material checks pass, and the Journal Requirements Ledger contains no material `UNVERIFIED` or unresolved `CONFLICT` items.

The final package must be mathematically reproducible, visually legible, journal-compliant, source-complete, internally consistent, and mapped explicitly to current official submission requirements.

The only allowed exception is a documented `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED` when every non-portal requirement passes and the remaining items can only be resolved inside the authenticated submission system.

## 12. Failure criteria

Return to the relevant earlier stage when a problem is substantive rather than formatting/packaging. Bounded artwork/source-package/metadata defects may be repaired within Stage 14 if the underlying verified object and interpretation remain unchanged.

If a live journal requirement contradicts an internal workflow assumption, the current journal requirement controls the submission package and the contradiction must be documented rather than rationalized away.

## 13. Required final output

1. Executive QA verdict
2. Clean-build result
3. Symbolic/numerical verification result
4. Figure/table regeneration and numerical-integrity result
5. Artwork-format/accessibility result
6. Bibliography/reference result
7. Refreshed Journal Requirements Ledger with URLs/access dates/statuses
8. Review-model/anonymity/author-identification result
9. Initial-submission file/source-package result
10. Declarations/AI/data/code/prior-publication result
11. Metadata/portal-field result
12. Fees/access/licensing result when material
13. Local PDF visual QA result
14. Authenticated portal preflight status
15. Package inventory, including figure/table and LaTeX/source dependencies
16. Remaining warnings
17. Verdict and Stage 15 contract

## 14. Final verdict

Choose one:

- `SUBMISSION QA PASS`
- `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`
- `CONDITIONAL PASS` — other non-substantive fix only
- `FAIL — REOPEN EARLIER STAGE`

A material `UNVERIFIED` journal requirement is never a full `PASS`.

## 15. Next-stage contract

Stage 15 records an immutable submission state and, where necessary, completes the authenticated portal preflight before the final submit action.

No substantive change is allowed between QA pass and freeze. Final figure/table outputs and generators used for the submission must be part of the frozen provenance.

If the authenticated portal reveals a new or conflicting operative requirement, update the package under the evidence hierarchy above, rerun the affected Stage-14 checks, and create a new validated freeze rather than silently altering the already audited package.