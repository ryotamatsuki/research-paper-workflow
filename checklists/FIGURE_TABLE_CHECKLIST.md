# Figure / Table Architecture and QA Checklist

Use across Stages 7, 10, 13, and 14. The purpose is not to maximize the number of visuals. It is to ensure that every central result is communicated by the most efficient verified exposition vehicle and that any retained figure/table is reproducible and submission-ready.

## Governing principle

> Every figure or table must earn its place by materially reducing the reader's cost of understanding a central mechanism, result, comparison, or scope condition.

There is **no minimum figure or table quota**. A theorem/proposition or concise prose may be the correct vehicle when a visual would be redundant.

---

## Stage 7 — Result-to-exposition triage

For every surviving headline result:

- [ ] Economic object identified precisely
- [ ] Candidate exposition vehicle assigned: theorem/proposition / figure / table / numerical illustration / prose
- [ ] Reason for that vehicle recorded
- [ ] Verified theoretical/source object identified
- [ ] Any future generator or verification need identified
- [ ] Vehicle does not imply a stronger claim than the theorem supports

Flag for explicit consideration when the result involves:

- [ ] threshold crossing
- [ ] sign reversal
- [ ] non-monotonicity
- [ ] regime or active-set changes
- [ ] benchmark separation
- [ ] welfare decomposition
- [ ] multi-case or multi-parameter sensitivity
- [ ] strategic-response/network structure

A flag means “consider a visual/table,” not “must create one.”

---

## Stage 10 — Figure/Table Architecture Gate

Before finalizing the Introduction:

- [ ] Every headline result has one primary exposition vehicle
- [ ] Required figures/tables are explicitly listed
- [ ] Redundant/decorative visuals are rejected
- [ ] Figure vs table choice is justified by reader information needs
- [ ] Every quantitative visual/table maps to a verified script or authoritative source
- [ ] No hand-entered quantitative content unless independently checked and documented
- [ ] No arbitrary normalized polynomial/index is labeled as the underlying economic object
- [ ] Proven domain/range is respected
- [ ] Representative values, thresholds, signs, or identities are regression-checked where feasible
- [ ] Source/generator files are stored in the production repository
- [ ] Labels/captions/reference hooks are planned

Suggested choice rule:

- **Figure**: shape, crossing, non-monotonicity, regime map, strategic path/network, benchmark separation
- **Table**: exact values, discrete comparisons, sensitivity matrix, welfare accounting, classifications
- **Theorem/prose**: compact result where visual representation adds little information

Exit condition:

- [ ] Every headline result has an explicit exposition vehicle
- [ ] Every figure/table classified as required is reproducibly implemented or has a documented blocker

---

## Stage 13 — Journal-specific integration

- [ ] Stage-10 architecture map reconciled with final manuscript
- [ ] Target-journal figure/table limits checked
- [ ] Placement rules checked
- [ ] Accepted artwork/file types checked
- [ ] Captions/titles are self-contained and scope-accurate
- [ ] Every retained figure/table is referenced in surrounding prose
- [ ] No orphan visual/table
- [ ] No duplicate visual/table conveying the same information without justification
- [ ] Headline visual is signposted in Introduction when useful
- [ ] Figure/table interpretation matches proposition/proof restrictions
- [ ] Actual economic object is plotted/tabulated, not a misleading proxy or arbitrary normalization
- [ ] Generator/source files retained for Stage 14

If a missing figure/table requires a new substantive computation, new result, or new robustness exercise:

- [ ] Reopen the earliest affected research stage rather than adding it silently

If it is only bounded presentation of an already verified result:

- [ ] Integrate it in Stage 13 and record that there is no theory/result change

---

## Stage 14 — Submission artwork QA

### Reproducibility and numerical integrity

- [ ] All quantitative figures/tables regenerate from source
- [ ] Regeneration uses the documented/pinned environment
- [ ] Representative plotted/tabulated values match manuscript values
- [ ] Thresholds, roots, signs, benchmark identities, and labels are consistent
- [ ] Generated outputs are not stale relative to source/generator files

### Vector graphics

When applicable under current journal guidance:

- [ ] Fonts embedded
- [ ] Font embedding/subsetting verified with an appropriate tool
- [ ] Text remains text/vector rather than unnecessarily rasterized
- [ ] Line widths and symbols survive final-size rendering

### Raster graphics

When applicable under current journal guidance:

- [ ] Pixel dimensions adequate
- [ ] Effective DPI/resolution adequate at final size
- [ ] Compression does not obscure labels/lines
- [ ] No unnecessary low-resolution screenshots

### Legibility/accessibility

- [ ] Axis labels readable at final manuscript size
- [ ] Legends readable
- [ ] Mathematical notation renders correctly
- [ ] Line styles/markers distinguish series in grayscale where needed
- [ ] Meaning does not depend on color alone
- [ ] Captions identify solid/dashed/marker meanings where relevant
- [ ] Table font size remains readable
- [ ] Tables do not overflow margins
- [ ] No clipped labels, equations, legends, or notes

### Manuscript/package integration

- [ ] Figure/table numbering sequential and stable
- [ ] All references resolve
- [ ] Every figure/table cited in text
- [ ] No obsolete/unreferenced figure/table remains in source package unless intentionally documented
- [ ] Required separate artwork files are included
- [ ] Figure/table source and generator files are included when appropriate
- [ ] Final PDF page containing each figure/table visually inspected
- [ ] Portal-generated PDF, if any, preserves figure/table legibility before final submit

---

## Kill tests

Do not pass the relevant stage if:

- [ ] A headline result has no defensible exposition vehicle
- [ ] A required figure/table is unreproducible
- [ ] A visual/table contradicts the manuscript or theorem
- [ ] A visual exaggerates scope or hides domain restrictions
- [ ] Manual data or arbitrary normalization is presented as a verified economic object
- [ ] Current journal artwork requirements are violated
- [ ] Figure/table legibility materially fails at final size
- [ ] A central missing visual is discovered at Stage 14 and would require substantive new work

## Required provenance

For each final quantitative figure/table, preserve where feasible:

- [ ] source/generator path
- [ ] environment/dependency version
- [ ] relevant input/model/freeze identifier
- [ ] representative numerical checks
- [ ] output path
- [ ] output hash/checksum when useful at submission freeze
- [ ] journal-specific artwork QA result
