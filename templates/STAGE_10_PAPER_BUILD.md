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

Construct a coherent, compilable full manuscript section by section, with every theorem, equation, table, and citation traceable to frozen theory or verified evidence.

## 3. Canonical inputs

Stage 8 theory freeze and Stage 9 repository are authoritative. Re-fetch latest remote state before every substantial implementation cycle.

## 4. Allowed changes

Exposition, notation presentation, ordering, proofs, figures/tables, literature synthesis, and journal-appropriate framing that do not alter the substantive theory.

## 5. Prohibited changes

- no new theorem or assumption introduced to improve prose;
- no silent change to timing, payoff, parameter restriction, welfare concept, or contribution claim;
- no writing the Introduction as a commitment device before results are stable;
- no manual figure/table values that differ from scripts.

## 6. Recommended construction order

Unless project dependencies justify another sequence, build:

1. Model
2. Equilibrium characterization
3. Main results
4. Welfare
5. Robustness/extensions approved at freeze
6. Institutional / empirical bridge
7. Related Literature
8. Introduction
9. Discussion
10. Conclusion

For each section:

1. inspect latest repository state;
2. identify frozen inputs used by the section;
3. draft in modular source files;
4. compile/build;
5. verify equations and proposition statements;
6. verify references/cross-references;
7. review for scope and overclaiming;
8. commit through a controlled branch/PR when repository policy requires it.

## 7. Evidence requirements

Literature claims must cite verified sources. Institutional claims must retain evidence-level qualifiers. Every quantitative number should be generated or sourced.

## 8. Verification protocol

After each section, run relevant build/test gates. For mathematical sections, compare text claims directly with the proposition register. For literature sections, check bibliography resolution and claim-source alignment.

## 9. Kill tests

Stop and reopen earlier stages if writing reveals:

- a missing assumption required for a theorem;
- a proposition that cannot be stated under frozen restrictions;
- a new fatal prior-art issue;
- an institutional claim incompatible with the model;
- a robustness requirement that changes the mechanism.

## 10. Success criteria

Each section must compile, be internally consistent, and add a distinct function to the paper rather than repeating earlier sections.

## 11. Failure criteria

Do not integrate a section that requires theory drift, contains unresolved citation/verification failures, or exists only to inflate length.

## 12. Required final output

For each section report:

1. files changed
2. frozen theory inputs used
3. key claims/equations
4. verification/build result
5. literature/reference checks
6. unresolved issues
7. PR/commit status

At Stage completion provide a full section map and remaining manuscript gaps.

## 13. Final verdict

Choose one:

- `FULL DRAFT READY FOR REFEREE GATE`
- `CONDITIONAL GO` — specific section blocker
- `REOPEN EARLIER STAGE`

## 14. Next-stage contract

Stage 11 attacks the completed manuscript and model; it does not add unmotivated extensions.