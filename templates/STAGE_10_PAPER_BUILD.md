# Stage 10 — Section-by-Section Paper Construction

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as research director, technical writer, and repository maintainer. Build the paper in dependency order without changing the frozen theory.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Working title: `[WORKING_TITLE]`
- Frozen theory: `[CANONICAL_MODEL]`
- Freeze record: `[CURRENT_STAGE_RESULT]`
- Repository: `[SOURCE_REPOSITORY]`
- Target journal: `[TARGET_JOURNAL]`

## 2. Stage objective

Construct a coherent, compilable full manuscript section by section, with every theorem, equation, figure, table, and citation traceable to frozen theory or verified evidence. Before the draft is declared complete, define and implement an explicit exposition architecture for every headline result.

## 3. Canonical inputs

Stage 8 theory freeze and Stage 9 repository are authoritative. The Stage-7 result-to-exposition triage is a planning input. Re-fetch latest remote state before every substantial implementation cycle.

## 4. Allowed changes

Exposition, notation presentation, ordering, proofs, figures/tables, literature synthesis, and journal-appropriate framing that do not alter the substantive theory.

## 5. Prohibited changes

- no new theorem or assumption introduced to improve prose;
- no silent change to timing, payoff, parameter restriction, welfare concept, or contribution claim;
- no writing the Introduction as a commitment device before results are stable;
- no manual figure/table values that differ from scripts or verified source material;
- no plotting an arbitrarily normalized polynomial or index and labeling it as an economic derivative, welfare object, equilibrium quantity, or other substantive result;
- no minimum-figure quota and no decorative visual added solely to make the manuscript look more complete.

## 6. Recommended construction order

Unless project dependencies justify another sequence, build:

1. Model
2. Equilibrium characterization
3. Main results
4. Welfare
5. Robustness/extensions approved at freeze
6. Institutional / empirical bridge
7. Related Literature
8. **Figure/Table Architecture Gate**
9. Introduction
10. Discussion
11. Conclusion

For each section:

1. inspect latest repository state;
2. identify frozen inputs used by the section;
3. draft in modular source files;
4. compile/build;
5. verify equations and proposition statements;
6. verify references/cross-references;
7. review for scope and overclaiming;
8. commit through a controlled branch/PR when repository policy requires it.

## 6A. Mandatory Figure/Table Architecture Gate

Before drafting or finalizing the Introduction, create a manuscript-level exposition map. For every headline theorem, comparative static, welfare result, benchmark contrast, robustness result, and scope condition, assign one primary presentation vehicle:

- theorem/proposition;
- figure;
- table;
- numerical illustration;
- concise prose.

The map must minimally record:

| Headline result | Economic object | Primary vehicle | Why this vehicle | Verified source / generator | Required in final paper? |
|---|---|---|---|---|---|

Use a figure when a reader materially benefits from seeing shape or structure — for example a threshold crossing, non-monotonicity, regime map, comparative-static path, benchmark separation, or network/strategic-response pattern. Use a table when exact values, multi-case comparisons, sensitivity results, welfare accounting, or classification are more informative than a continuous visual. Use prose/theorem only when a visual would be redundant.

Every proposed figure/table must earn its place by materially reducing the reader's cost of understanding a central mechanism, result, comparison, or scope condition.

### Implementation requirements for accepted figures/tables

- generate quantitative content from verified scripts or authoritative source data;
- preserve the economic scale and sign of the actual reported object;
- machine-check representative values, thresholds, or identities where feasible;
- keep source/generator files in the repository;
- ensure caption and surrounding prose state exactly what the visual establishes and what it does not;
- use labels and references in the manuscript rather than leaving orphan visuals;
- retain sufficient information for later journal-specific formatting in Stage 13.

A game-timing diagram, conceptual schematic, or mechanism flowchart is optional and should be included only when it reduces genuine cognitive load.

## 7. Evidence requirements

Literature claims must cite verified sources. Institutional claims must retain evidence-level qualifiers. Every quantitative number should be generated or sourced. Every figure/table must be traceable to a verified model object, script, or source.

## 8. Verification protocol

After each section, run relevant build/test gates. For mathematical sections, compare text claims directly with the proposition register. For literature sections, check bibliography resolution and claim-source alignment. For each figure/table, verify that the plotted/tabulated values reproduce the manuscript's stated checkpoints and do not silently extrapolate beyond the proven domain.

## 9. Kill tests

Stop and reopen earlier stages if writing reveals:

- a missing assumption required for a theorem;
- a proposition that cannot be stated under frozen restrictions;
- a new fatal prior-art issue;
- an institutional claim incompatible with the model;
- a robustness requirement that changes the mechanism.

Do not declare Stage 10 complete if:

- a headline result has no explicit exposition vehicle;
- a visual is necessary to make a central threshold/regime/benchmark result intelligible but remains unimplemented without a documented reason;
- a figure/table is based on hand-entered or unverified values;
- a visual communicates a stronger claim than the proposition/proof supports.

## 10. Success criteria

Each section must compile, be internally consistent, and add a distinct function to the paper rather than repeating earlier sections. Every headline result must have an explicit exposition vehicle, and every figure/table designated as required must be implemented reproducibly before the full draft is sent to Stage 11.

## 11. Failure criteria

Do not integrate a section that requires theory drift, contains unresolved citation/verification failures, or exists only to inflate length. Do not defer a known exposition-architecture gap to submission QA.

## 12. Required final output

For each section report:

1. files changed
2. frozen theory inputs used
3. key claims/equations
4. verification/build result
5. literature/reference checks
6. unresolved issues
7. PR/commit status

At Stage completion additionally provide:

8. full section map
9. Figure/Table Architecture map
10. figure/table generators and verification status
11. remaining manuscript gaps

## 13. Final verdict

Choose one:

- `FULL DRAFT READY FOR REFEREE GATE`
- `CONDITIONAL GO` — specific section or exposition-architecture blocker
- `REOPEN EARLIER STAGE`

## 14. Next-stage contract

Stage 11 attacks the completed manuscript and model; it does not add unmotivated extensions. Any required figure/table already identified at Stage 10 should travel with the draft into Stage 11 rather than be postponed to Stage 13 or 14.