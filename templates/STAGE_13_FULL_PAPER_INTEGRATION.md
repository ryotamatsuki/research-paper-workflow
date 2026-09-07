# Stage 13 — Full-Paper Integration

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a field-journal editor and manuscript integrator. Convert independently correct sections into one coherent argument without contribution inflation.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Working title: `[WORKING_TITLE]`
- Frozen theory: `[CANONICAL_MODEL]`
- Core mechanism: `[CORE_MECHANISM]`
- Primary journal: `[TARGET_JOURNAL]`
- Manuscript repository: `[SOURCE_REPOSITORY]`

## 2. Stage objective

Audit the complete manuscript for argument flow, section roles, claim consistency, notation, literature positioning, figure/table integration, and journal-appropriate exposition.

Carry the Stage-12 Journal Requirements Ledger into manuscript integration so known journal-specific requirements affect the package before final QA. Stage 14 must still refresh those requirements from current official sources.

## 3. Canonical inputs

Use the Stage 8 freeze, Stage 10 Figure/Table Architecture map, Stage 11 resolved attack log, Stage 12 journal positioning, and the Stage-12 Journal Requirements Ledger as authoritative inputs.

The ledger is an integration input, not a permanent truth: any `UNVERIFIED` or authenticated-portal-only item must remain visible for Stage 14 rather than being converted into an assumption.

## 4. Allowed changes

Exposition, ordering, compression, transitions, terminology, literature organization, abstract/introduction framing, figure/table placement and presentation, and journal-required formatting that do not alter substantive theory or verified results.

## 5. Prohibited changes

No new theory, unverified claim, extra robustness result, literature claim, or ad hoc numerical experiment introduced solely for narrative or visual convenience. A missing visual may be created here only when it directly represents an already verified result identified in the Stage-10 exposition architecture or when integration shows a bounded presentation gap that does not require new research.

Do not guess unresolved journal requirements. Preserve them explicitly for Stage 14.

## 6. Mandatory tasks

Audit the manuscript section by section:

### Introduction

- question is stated before machinery;
- mechanism and main results are precise;
- contribution claims map to verified results;
- no overclaiming of novelty or generality;
- motivation does not promise results the model cannot deliver;
- headline figures/tables are signposted when doing so materially improves navigation.

### Related Literature

- organized by conceptual relationship, not an author-by-author catalogue;
- distinguishes exact/structural/component overlap;
- avoids repetitive paragraph templates and repeated “paper X shows… our paper differs…” rhythm;
- positions the contribution rather than summarizing everything read.

### Model / Results / Welfare

- assumptions match freeze;
- proposition statements and restrictions match proofs;
- results explain mechanism rather than restating algebra;
- welfare accounting is consistent;
- figure/table interpretation matches the verified mathematical object and domain.

### Figures / Tables

- reconcile the final manuscript with the Stage-10 Figure/Table Architecture map;
- retain only visuals/tables that materially reduce reader effort;
- ensure every retained figure/table is referenced and interpreted in the surrounding text;
- ensure captions are self-contained enough to identify the object, sample/parameterization or benchmark when applicable, sign convention, and key scope limitation;
- ensure quantitative visuals/tables come from verified generators or authoritative source data rather than manual transcription;
- ensure the actual economic object is plotted/tabulated rather than an arbitrary normalization presented as if it were the object itself;
- check whether the target journal imposes figure/table count, placement, file-type, grayscale/color, accessibility, or caption requirements, and adapt presentation without changing results;
- preserve generator/source files for Stage 14 package QA.

There is no minimum figure count. If a headline result is best communicated by theorem/prose, document that decision rather than adding a decorative visual.

### Journal-specific manuscript/package integration

Using the Stage-12 Journal Requirements Ledger:

- align manuscript anonymity/identification only to requirements that are actually verified;
- align title page, author/affiliation/corresponding-author placement, abstract/keywords/JEL/highlights, declarations, acknowledgments, and ancillary-file structure where already known;
- identify whether an editable Word/LaTeX source package will be required and preserve all dependencies needed to construct it;
- preserve a separate identified and anonymous build only when the journal workflow genuinely requires both or when doing so is operationally useful without creating ambiguity;
- carry every unresolved portal-only or policy item into the Stage-14 contract explicitly.

Do not treat a generic publisher rule, previous submission, repository assumption, or remembered screen as controlling when a more specific current journal instruction exists.

### Discussion

- interprets mechanism, scope, empirical/institutional implications, and limitations;
- does not simply repeat the Results section.

### Conclusion

- short;
- answers the research question;
- does not introduce a new result, policy claim, literature claim, or new visual interpretation.

Cross-document audit:

- notation consistency;
- terminology consistency;
- abstract/introduction/conclusion claim alignment;
- theorem-to-claim mapping;
- citations and cross-references;
- figure/table references and numbering;
- appendix/supplement consistency;
- title-page/main-manuscript/declaration/metadata consistency for all requirements already verified at Stage 12.

## 7. Evidence requirements

Every substantive statement must map to a verified theorem, source, or clearly labeled interpretation. Every quantitative figure/table must map to a verified generator or authoritative source and preserve the proven/reportable domain.

Journal-specific integration decisions must map to the Stage-12 Journal Requirements Ledger. Unknown requirements remain `UNVERIFIED`; do not silently promote them to facts.

## 8. Verification protocol

Compile/build after integration. Search globally for notation variants, stale claims, placeholder text, unresolved TODOs, citations, and orphan/missing figure/table references. Compare contribution sentences directly with Stage 6/8 records. Re-run figure/table generators and representative numerical checkpoints where feasible.

Build any planned anonymous/identified/title-page variants and compare them for accidental content drift. Confirm known journal requirements have been implemented consistently while unresolved requirements remain visible for Stage 14.

## 9. Kill tests

Block submission QA if:

- sections make inconsistent contribution claims;
- the Introduction oversells a killed result;
- Discussion/Conclusion adds unmodeled policy claims;
- Related Literature misstates a closest paper;
- notation or parameter restrictions differ across sections;
- a headline result identified at Stage 10 still lacks its required exposition vehicle without a documented reason;
- a figure/table cannot be reproduced from its claimed source;
- a visual/tabular interpretation exceeds the theorem's scope or uses an arbitrary normalization as if it were the reported economic object;
- a known journal requirement is implemented inconsistently across manuscript/title page/declarations/package;
- an `UNVERIFIED` journal requirement has been silently converted into a definitive formatting/anonymity/source-package choice.

If integration reveals that a **new substantive computation or result** is needed to make a figure/table defensible, do not create it silently: return to the earliest affected stage. If the issue is bounded presentation of an already verified result, repair it in Stage 13 and document the scope.

## 10. Success criteria

A reader should encounter one research question, one coherent mechanism, verified results, and a disciplined contribution narrative from abstract through conclusion. The final figure/table set should make the paper easier to understand without becoming a parallel source of unverified claims.

The integrated package should also be structurally ready for Stage 14 to perform a fresh live journal-compliance audit rather than discovering preventable source/title-page/declaration inconsistencies for the first time.

## 11. Failure criteria

Return to the relevant section or earlier research stage if integration reveals substantive inconsistency rather than mere prose or presentation weakness.

Bounded journal-format/package issues may remain for Stage 14 only when they are explicitly identified and do not require substantive research changes.

## 12. Required final output

1. Executive integration verdict
2. Section-role audit
3. Contribution-claim audit
4. Related-literature structure audit
5. Results/Discussion separation audit
6. Abstract/intro/conclusion alignment
7. Figure/Table Architecture reconciliation and journal-specific integration audit
8. Journal Requirements Ledger integration status
9. Known manuscript/title-page/declaration/source-package requirements implemented
10. `UNVERIFIED` or authenticated-portal-only requirements carried forward
11. Notation/citation/cross-reference audit
12. Changes made
13. Remaining blockers
14. Verdict and Stage 14 contract

## 13. Final verdict

Choose one:

- `INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`
- `CONDITIONAL GO` — bounded integration fixes
- `REOPEN SECTION / EARLIER STAGE`

## 14. Next-stage contract

Stage 14 verifies the complete submission package and **refreshes all material journal requirements from current official sources**. It should not be the first stage at which the project decides whether a central result needs a figure or table, but it is the mandatory stage at which journal-compliance evidence is re-opened, dated, reconciled, and made fail-closed.

Stage 14 may repair formatting/package defects but should not materially rewrite the theory, contribution, or exposition architecture.