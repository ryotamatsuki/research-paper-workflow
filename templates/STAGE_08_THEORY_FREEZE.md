# Stage 8 — Canonical Theory Freeze

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as research director and configuration manager. Convert the approved theory into a canonical, auditable specification before manuscript construction.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Working title: `[WORKING_TITLE]`
- Approved question: `[CORE_RESEARCH_QUESTION]`
- Approved mechanism: `[CORE_MECHANISM]`
- Approved model: `[CANONICAL_MODEL]`
- Stage 7.5 verdict: `[CURRENT_STAGE_RESULT]`
- Closest papers: `[CLOSEST_PAPERS]`

## 2. Stage objective

Freeze the theoretical object so that later writing cannot silently change the model, propositions, or contribution claims.

## 3. Canonical inputs

Only results explicitly approved by Stage 7.5 may enter the freeze.

## 4. Allowed changes

Notation cleanup and unambiguous restatement only.

## 5. Prohibited changes

No new extensions, assumptions, propositions, welfare claims, or literature positioning.

## 6. Mandatory freeze record

Record at minimum:

1. research question;
2. contribution statement;
3. players and objectives;
4. timing and information;
5. utility/demand;
6. technology/costs;
7. contracts/transfers;
8. parameter restrictions;
9. equilibrium concept;
10. baseline equilibrium objects;
11. main propositions and exact conditions;
12. welfare propositions;
13. proof/verification status;
14. approved robustness scope;
15. empirical/institutional interpretation;
16. closest-paper distinction;
17. claims that are explicitly not made.

For each proposition classify proof status as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, or `REJECTED`.

## 7. Evidence requirements

Freeze references to the verified literature record and verification artifacts. Do not freeze an unverified conjecture as a theorem.

## 8. Verification protocol

Cross-check the freeze against Stage 4–7 outputs and symbolic verification. Confirm parameter restrictions and proposition statements exactly match the verified model.

## 9. Kill tests

Do not freeze if:

- the model description differs from the verified equations;
- a main proposition remains only numerically supported while presented as analytic;
- closest-paper positioning is unresolved;
- the theory changed after Stage 7.5 without re-running the affected gate.

## 10. Success criteria

The frozen record must be sufficient for an independent researcher to know exactly what may be written and proved in the paper.

## 11. Failure criteria

Return to the affected earlier stage if any substantive inconsistency is found.

## 12. Required final output

1. Canonical theory specification
2. Proposition register
3. Parameter-restriction register
4. Welfare register
5. Verification status table
6. Approved robustness list
7. Contribution/closest-paper statement
8. Explicit exclusions
9. Freeze identifier/date/SHA if applicable
10. Theory change-control procedure

## 13. Final verdict

Choose one:

- `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`
- `FREEZE BLOCKED` — identify the exact earlier stage to reopen

## 14. Theory change control

Any post-freeze theoretical change must record:

- what changed;
- why;
- affected equations/propositions;
- affected verification;
- affected literature claims;
- stages that must be re-run.

No silent theory drift is permitted.