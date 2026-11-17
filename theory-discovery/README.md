# Theory Discovery Framework (TDF)

## v5.1 — Official practical-use version (adopted 2026-11-17)

TDF v5.1 is the default optional method for discovering and screening research questions before [Stage 0](../templates/STAGE_00_IDEA_INTAKE.md).

- [Master prompt](v5.1/TDF_Master_Prompt_v5.1.md) sets inputs and output requirements.
- [Loop protocol](v5.1/TDF_Loop_Protocol_v5.1.md) defines search, evidence, budget, and handoff rules.
- [Prompt library](v5.1/TDF_Research_Prompt_Library_v5.1.md) provides prompts for individual research tasks.
- [Run ledger](v5.1/templates/Run_Ledger.md) and [Stage 0 handoff](v5.1/templates/Stage0_Handoff.md) record decisions and evidence.
- [Package guide](v5.1/README.md) covers the Python helpers and links to the [calibration report](v5.1/validation/Calibration_Report.md).

Use STANDARD by default. A STANDARD candidate marked `PROMISING` can be proposed for author selection with novelty still unresolved. Use EPOCH to search for a concept or general principle with testable implications in at least two settings. BOTH runs separate search queues with a shared source ledger. In any mode, keep a candidate on hold when a decisive prior-art question remains unresolved. The author selects any candidate that moves to Stage 0.

The calibration covers decision rules and retrospective examples. Prospective discovery performance remains unverified. The [canonical pipeline](../THEORY_PAPER_RESEARCH_PIPELINE.md) and [governance](../GOVERNANCE.md) govern formal stage decisions, mathematical verification, novelty review and theory freeze.

## Historical reference — v4.0 (default from 2026-11-16 to 2026-11-17)

The v4.0 instructions below document the earlier baseline. The v4.0 construction pattern catalog remains available as a reference for model construction.

**Original status:** The author adopted v4.0 as the optional discovery baseline on 2026-11-16.

### Start here

- [TDF v4.0 Master Prompt](v4/TDF_Master_Prompt_v4.md) — v4.0 operational entry point.
- [TDF v4.0 Prompt Library](v4/TDF_Prompt_Library_v4.md) — reusable discovery and challenge prompts.
- [TDF v4.0 Theory Construction Pattern Catalog](v4/Theory_Construction_Pattern_Catalog_v4.md) — the model-construction toolbox, distinct from creative problem discovery.

The full v4.0 source package, including the historical research database, case analysis, research report and validation records, is retained in the author's library. This public repository mirrors only the three operational source documents listed above; it is not a claim that the entire package has been publicly imported.

### Operational rule

1. Begin with a research theme and the author's observations.
2. Reconstruct existing explanations; apply creative questioning to identify an unexplained contrast. Do not start by mechanically applying a model-construction pattern.
3. Produce and critically challenge research questions, using early reduction/parent-theory checks and allowing HOLD when evidence is inadequate. Separate question quality, mathematical validity, novelty and economic significance.
4. Develop a minimal discriminating comparison or model only after choosing a question. Preserve the question when a particular model is absorbed, if a meaningful unexplained contrast remains.
5. Obtain the author's selection before handing off to [Stage 0](../templates/STAGE_00_IDEA_INTAKE.md).

TDF is optional: a clear research question may enter Stage 0 directly. The [canonical pipeline](../THEORY_PAPER_RESEARCH_PIPELINE.md) and [governance](../GOVERNANCE.md) take precedence. TDF v4.0 is independent of the pipeline's version and does not modify its stages, verdicts, routing, certification gates, release tags or theorem-freeze requirements.

### Evidence boundary and change control

Historical reconstruction, pilot evaluations and regression tests provide preliminary evidence only. Predictive ability to discover genuinely unknown or epoch-making theories has not been demonstrated. Do not treat a TDF output as a mathematical or novelty certificate. Maintain records of practical applications, failed hypotheses, absorption findings and useful questions. Preserve this baseline without silent changes; documented defects or evidence from actual use may justify an explicitly reviewed future revision. No routine further redesign is required. Keep unpublished project ideas and detailed validation material private.

---

## Historical reference — v3.0 (superseded for default use)

The following original v3.0 README text is retained as a historical record; its operational-authority statements refer to v3.0 at the time of import, not the current default.


Optional research-idea discovery/deepening companion before Stage 0.

**Status:** practical package imported from Google Drive, 2026-11-16. This is the user's reconstructed v3.0 package, not an exact recovery of the original six Deep Research artifacts.

## Start here

- [Master Prompt](Theory_Discovery_Master_Prompt_v3.md) — canonical entrypoint within this optional companion
- [Framework](Theory_Discovery_Framework_v3.md) — seven-phase discovery and falsification process
- [Pattern Catalog](Theory_Discovery_Pattern_Catalog_v3.md) — twelve discovery patterns
- [User Guide](Theory_Discovery_User_Guide_v3.md) — instructions and five illustrative acceptance-test themes
- [Database (CSV)](Economic_Theory_Discovery_Database_v3.csv) / [Database (JSON)](Economic_Theory_Discovery_Database_v3.json) — 32 research records, equivalent on field comparison
- [Final Research Report](TDF_v3_Final_Report.md) — historical Deep Research report as saved in Drive

The reconstructed companion files are authoritative for TDF operation. Historical report references to original artifacts, sandbox links, citations and original pattern numbers are preserved as historical text, not live repository links or evidence of completed import. P01–P10 and the rubric were reconstructed; use the imported catalog's numbering rather than assuming the old numbering. The database comprises 14 studies mentioned in the final report and 18 reconstruction-time selections according to the source provenance; the original 10+22 selection was not recovered. Primary-source/DOI and theory-novelty rechecks have not been performed.

## Use

Provide a topic, motivation and any known closest literature. Read the master prompt and the companion documents/database. Explore distinct candidate mechanisms with their benchmark, causal chain, closest parent theories and provisional falsification. Return options for the researcher to discuss and choose; do not automatically write a paper. After author selection, pass the topic and evidence to [Stage 0](../templates/STAGE_00_IDEA_INTAKE.md). The seven internal TDF phases are not canonical stages.

TDF is optional. If a research question is already clear, start the existing workflow normally. [GOVERNANCE.md](../GOVERNANCE.md) and the [canonical pipeline](../THEORY_PAPER_RESEARCH_PIPELINE.md) take precedence. No Stage number, verdict, route, rollback, freeze rule, certification obligation, workflow version or historical tag is changed. TDF output is a hypothesis, never a Stage GO, mathematical certificate or novelty certificate. Synthesize promising ideas with the author before formal model development; candidate sketches and conjectures are not proved results.

## Handoff and public/private separation

Record candidate ID, observed facts and sources/reading depth, conventional explanation, revised question, mechanism fingerprint, closest parent theory and absorption risk, conjecture and falsifier, alternatives, open issues, disposition and author decision. Continue AI provenance under canonical rules. Keep future unpublished candidate registers, project-specific source material and sensitive notes in appropriate private project repositories. This public repository contains the explicitly supplied methodological package and illustrative historical examples; do not automatically publish future project research.

## Scope and provenance

The seven Drive files are kept as supplied. The source notes state the six methodological deliverables are reconstructions, not original-file duplicates. Scientific effectiveness, original-paper verification, priority and theorem proof remain unverified. Import is not a new stable release of the paper workflow; TDF v3.0 is a separate methodology version. Further development is optional and should be driven by actual use.
