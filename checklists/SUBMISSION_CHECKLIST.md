# Submission Checklist

Use immediately before Stage 15 freeze. Verify journal-specific items against current official instructions rather than memory. For figure/table-specific design, reproducibility, artwork, and accessibility checks, also use [`FIGURE_TABLE_CHECKLIST.md`](FIGURE_TABLE_CHECKLIST.md).

## Journal instructions

- [ ] Current journal instructions opened and dated
- [ ] Article type confirmed
- [ ] Manuscript format confirmed
- [ ] Page/word/figure/table limits checked
- [ ] File-format requirements checked
- [ ] Figure/table/artwork requirements checked
- [ ] Double-blind / single-blind requirements checked
- [ ] Supplement/code/data requirements checked
- [ ] Current AI/generative-AI disclosure policy checked

## Manuscript metadata

- [ ] Final title
- [ ] Author names/affiliations where appropriate
- [ ] Corresponding-author information
- [ ] Anonymous title page prepared if required
- [ ] Abstract within limit
- [ ] Keywords
- [ ] JEL codes where appropriate
- [ ] Highlights / graphical abstract if required

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

## Declarations

- [ ] Funding statement
- [ ] Conflict-of-interest declaration
- [ ] Data availability statement
- [ ] Code availability statement
- [ ] Ethics statement if applicable
- [ ] Author contribution statement if required
- [ ] Generative-AI disclosure if required
- [ ] Acknowledgments handled consistently with anonymity rules

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

## Visual QA

- [ ] Every PDF page inspected
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

## Provenance

- [ ] Final repository SHA recorded
- [ ] Final tag planned/created at Stage 15
- [ ] Final PDF corresponds to recorded SHA
- [ ] Final source archive corresponds to recorded SHA
- [ ] Final figure/table outputs correspond to recorded source/generators
- [ ] Hash/checksum recorded where useful
- [ ] Submission date/time recorded

## Final gate

- [ ] No substantive correction remains pending
- [ ] No unresolved fatal referee attack remains
- [ ] All journal-specific required files are present
- [ ] Figure/table/artwork QA passes under current journal rules
- [ ] Stage 14 QA status is `PASS` or resolved `CONDITIONAL PASS`

If any substantive item fails, do not freeze the submission. Reopen the relevant workflow stage.