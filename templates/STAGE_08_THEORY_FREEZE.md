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
5. complete strategy sets and consumer/agent choice sets;
6. utility/demand;
7. technology/costs;
8. contracts/transfers;
9. parameter restrictions;
10. equilibrium concept;
11. baseline equilibrium objects;
12. main propositions and exact conditions;
13. welfare propositions;
14. proof/verification status;
15. approved robustness scope;
16. empirical/institutional interpretation;
17. closest-paper distinction;
18. claims that are explicitly not made.

For sequential/game-theoretic models, additionally freeze:

19. off-path history classes relevant to unilateral deviations;
20. continuation-equilibrium status for those classes;
21. active-set/corner/order/participation handling;
22. solver outcome taxonomy and unresolved/failure count;
23. multiplicity/nonexistence and continuation-selection assumptions, if any;
24. independent direct-payoff/allocation verification artifact used for high-stakes equilibrium claims.

For each proposition classify proof status as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, or `REJECTED`.

## 7. Evidence requirements

Freeze references to the verified literature record and verification artifacts. Do not freeze an unverified conjecture as a theorem.

For a sequential model claiming SPNE/subgame perfection, apply `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` and retain its audit record as freeze evidence.

## 8. Verification protocol

Cross-check the freeze against Stage 4–7 outputs and symbolic verification. Confirm parameter restrictions and proposition statements exactly match the verified model.

For sequential games, confirm that on-path calculations and off-path continuation certification are separate artifacts or separately auditable sections, and that no material solver failure was discarded from deviation searches.

## 9. Kill tests

Do not freeze if:

- the model description differs from the verified equations;
- a main proposition remains only numerically supported while presented as analytic;
- a claimed SPNE/global equilibrium has a material `UNRESOLVED` or `NUMERICAL_FAILURE` off-path continuation;
- FOCs/SOCs/interiority on a regular branch are being used as a substitute for full-strategy Nash verification;
- solver failure, invalid active set, or branch violation has been interpreted as an unprofitable deviation;
- the stated consumer/agent choice set is incomplete or differs from the allocation routine;
- closest-paper positioning is unresolved;
- the theory changed after Stage 7.5 without re-running the affected gate.

## 10. Success criteria

The frozen record must be sufficient for an independent researcher to know exactly what may be written and proved in the paper.

For sequential games, it must also be sufficient to reconstruct how every material class of upstream deviation receives a valid downstream continuation under the claimed equilibrium concept.

## 11. Failure criteria

Return to the affected earlier stage if any substantive inconsistency is found. Continuation incompleteness normally reopens Stage 4.

## 12. Required final output

1. Canonical theory specification
2. Proposition register
3. Parameter-restriction register
4. Welfare register
5. Verification status table
6. Continuation-completeness register, where applicable
7. Solver-failure/unresolved-continuation ledger, where applicable
8. Approved robustness list
9. Contribution/closest-paper statement
10. Explicit exclusions
11. Freeze identifier/date/SHA if applicable
12. Theory change-control procedure

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
