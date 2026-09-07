# Submission Checklist

Use immediately before Stage 15 freeze. Verify journal-specific items against current official instructions rather than memory.

This checklist must be used together with:

- [`JOURNAL_REQUIREMENTS_CHECKLIST.md`](JOURNAL_REQUIREMENTS_CHECKLIST.md) for current journal/portal rules and evidence hierarchy;
- [`FIGURE_TABLE_CHECKLIST.md`](FIGURE_TABLE_CHECKLIST.md) for figure/table design, reproducibility, artwork, and accessibility.

A material journal requirement is not closed merely because a box is checked. The production repository must preserve a current `JOURNAL_REQUIREMENTS_LEDGER.md` or equivalent with source, access date, interpretation, affected artifact/portal field, and verification status.

## Journal instructions

- [ ] Current journal-specific Guide for Authors / Instructions for Authors opened and dated
- [ ] Relevant journal-specific policy pages opened and dated
- [ ] Article type/category confirmed
- [ ] Actual submission system/portal confirmed
- [ ] Review/anonymity model confirmed from current official evidence
- [ ] Author information placement in main manuscript/title page confirmed
- [ ] Corresponding-author requirement confirmed
- [ ] Manuscript format confirmed
- [ ] Page/word/figure/table limits checked
- [ ] Abstract/keyword/JEL/classification limits checked
- [ ] File-format requirements checked
- [ ] Initial-submission editable-source requirement checked
- [ ] LaTeX/source-package rules checked when applicable
- [ ] Figure/table/artwork requirements checked
- [ ] Supplement/code/data requirements checked
- [ ] Current AI/generative-AI disclosure policy checked
- [ ] Funding/competing-interest/CRediT requirements checked
- [ ] Prior-publication/preprint/thesis rules checked when relevant
- [ ] Submission fee / mandatory charges / APC options distinguished when material
- [ ] Any portal-only requirements explicitly identified

## Journal Requirements Ledger

- [ ] `JOURNAL_REQUIREMENTS_LEDGER.md` or equivalent exists
- [ ] Each material item has a current official source or identifiable direct journal communication
- [ ] Access/receipt date recorded
- [ ] Evidence level recorded under `JOURNAL_REQUIREMENTS_CHECKLIST.md`
- [ ] Operative requirement stated precisely
- [ ] Affected file/metadata/portal field identified
- [ ] Verification method recorded
- [ ] No material item remains `UNVERIFIED`
- [ ] No material `CONFLICT` remains unresolved
- [ ] Any direct editorial-office or authenticated-portal instruction overriding a lower-level source is documented

## Manuscript metadata

- [ ] Final title
- [ ] Author names/order where appropriate
- [ ] Affiliations where appropriate
- [ ] Corresponding-author information
- [ ] Email/ORCID handling where required
- [ ] Separate title page prepared if required
- [ ] Anonymous manuscript prepared if required
- [ ] Identified main manuscript prepared if required
- [ ] Abstract within limit
- [ ] Keywords
- [ ] JEL codes/classifications where appropriate
- [ ] Highlights / graphical abstract if required
- [ ] Portal metadata matches manuscript/title page exactly

## Manuscript integrity

- [ ] Clean build passes
- [ ] No unresolved TODO/FIXME/placeholder text
- [ ] All equations and proposition numbering correct
- [ ] All labels/cross-references resolve
- [ ] Figures render correctly
- [ ] Tables render correctly
- [ ] Every figure/table is referenced in the text
- [ ] Figure/table captions and titles match the actual object and scope
- [ ] Appendix/supplement references match
- [ ] Abstract, introduction, results, discussion, conclusion claims agree
- [ ] No theory drift from frozen model

## Figures / tables / artwork

- [ ] Final figure/table set matches the Stage-13 integrated exposition architecture
- [ ] No central result is missing its required exposition vehicle
- [ ] No redundant/decorative visual remains without justification
- [ ] Quantitative figures/tables regenerate from verified scripts or authoritative source data
- [ ] Representative values, signs, thresholds, and benchmark identities match the manuscript
- [ ] No arbitrary normalization/proxy is presented as the underlying economic object
- [ ] Accepted journal file types confirmed
- [ ] Separate artwork files included if required
- [ ] Vector-font embedding checked if required
- [ ] Raster resolution/effective DPI checked if applicable
- [ ] Axis labels, legends, notes, and table text readable at final size
- [ ] Series remain distinguishable in grayscale where relevant
- [ ] Meaning does not rely on color alone
- [ ] No clipping, overlap, overflow, or broken glyph in figures/tables
- [ ] Figure/table source and generator files included in source package when appropriate

## References

- [ ] Every in-text citation resolves
- [ ] Every bibliography entry is cited or intentionally retained
- [ ] Author/title/year/journal metadata checked for closest papers
- [ ] DOI/stable identifiers included where style requires
- [ ] No duplicate working-paper/published-version references unless justified
- [ ] No unverifiable/fabricated citation

## Reproducibility

- [ ] Symbolic verification passes
- [ ] Numerical verification passes
- [ ] Figures/tables regenerate from scripts
- [ ] Dependency/environment instructions current
- [ ] Source archive complete
- [ ] Code/data statement accurate
- [ ] Verification logs preserved

## LaTeX / editable-source package

Complete when editable source is required or LaTeX is used:

- [ ] Current journal rule on PDF-only vs editable source confirmed
- [ ] `.tex` files included
- [ ] `.bib`/bibliography files included as required
- [ ] Figure files included in accepted formats
- [ ] Table-source files included where applicable
- [ ] Required `.sty`, `.cls`, `.bst`, or other non-standard dependencies included/handled
- [ ] Archive format confirmed
- [ ] Folder/subfolder restrictions confirmed
- [ ] Exact archive intended for upload extracted to a clean directory
- [ ] Clean extraction compiles without relying on hidden repository paths
- [ ] Generated PDF from the upload archive matches intended manuscript
- [ ] Archive contains no unnecessary private/internal files

## Declarations

- [ ] Funding statement
- [ ] Conflict-of-interest / competing-interest declaration
- [ ] Data availability statement
- [ ] Code availability statement
- [ ] Ethics statement if applicable
- [ ] CRediT / author contribution statement if required
- [ ] Generative-AI disclosure if required
- [ ] Acknowledgments handled consistently with anonymity rules
- [ ] Prior-publication/preprint disclosure handled where relevant
- [ ] Portal declaration fields match manuscript declarations

## Submission package

- [ ] Main manuscript PDF/source
- [ ] Title page if separate
- [ ] Cover letter
- [ ] Highlights if required
- [ ] Figures as separate files if required
- [ ] Tables as separate files if required
- [ ] Figure/table source or generator files included where appropriate
- [ ] Appendix/supplement
- [ ] Code/data/repository link if required
- [ ] Suggested/opposed reviewers if requested
- [ ] Classification/subject codes if requested
- [ ] Every file has the correct submission-portal designation

## Local visual QA

- [ ] Every locally generated PDF page inspected
- [ ] First page author identification/anonymity checked against current journal rule
- [ ] Every figure/table page inspected at readable resolution
- [ ] No clipped equations
- [ ] No overflow/underflow that affects readability
- [ ] Figure labels readable
- [ ] Legends/markers/line styles readable
- [ ] Table widths acceptable
- [ ] Table font size readable
- [ ] Footnotes readable
- [ ] Hyperlinks/cross-references behave as intended
- [ ] Anonymous version contains no identifying metadata where prohibited
- [ ] Identified version contains required author/affiliation/corresponding-author information where required

## Authenticated portal preflight

Before final submit when an authenticated portal is used:

- [ ] Actual submission record opened
- [ ] Current required fields inspected rather than remembered
- [ ] Current file-designation options inspected
- [ ] Article type confirmed in portal
- [ ] Author order/affiliations/corresponding author confirmed
- [ ] Manuscript anonymity/identification confirmed
- [ ] Title-page handling confirmed
- [ ] Source/figure/table/supplement designations confirmed
- [ ] Funding/conflict/CRediT/AI/data/code/prior-publication fields reconciled
- [ ] Portal warnings resolved
- [ ] Submission PDF built/generated when supported
- [ ] Portal-generated PDF inspected page by page
- [ ] First page checked specifically for author identification/anonymity
- [ ] Equations/citations/figures/tables/appendix/declarations render correctly
- [ ] No file missing, duplicated, stale, or misdesignated

If authenticated portal access is the only remaining unknown at Stage 14, record `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`; do not upgrade it to full `PASS` by assumption.

## Provenance

- [ ] Final repository SHA recorded
- [ ] Final tag planned/created at Stage 15
- [ ] Final PDF corresponds to recorded SHA
- [ ] Final source archive corresponds to recorded SHA
- [ ] Final figure/table outputs correspond to recorded source/generators
- [ ] Final Journal Requirements Ledger preserved
- [ ] Hash/checksum recorded where useful
- [ ] Submission date/time recorded
- [ ] Portal-generated PDF/confirmation preserved where appropriate

## Final gate

- [ ] No substantive correction remains pending
- [ ] No unresolved fatal referee attack remains
- [ ] All journal-specific required files are present
- [ ] All material journal requirements are verified from current evidence
- [ ] No unresolved evidence conflict remains
- [ ] Figure/table/artwork QA passes under current journal rules
- [ ] Stage 14 QA status is `PASS` or the only remaining item is an explicit authenticated-portal preflight
- [ ] Final submission is not clicked until authenticated portal reconciliation is complete

If any substantive item fails, do not freeze the submission. Reopen the relevant workflow stage.

If a technical return later reveals a missed requirement, preserve it as workflow evidence and add a regression check so the same failure mode cannot silently pass future Stage-14/15 QA.