# Stage 8 — Canonical Theory Freeze

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as research director and configuration manager. Convert the approved and independently certified theory into a canonical, auditable specification before manuscript construction.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Working title: `[WORKING_TITLE]`
- Approved question: `[CORE_RESEARCH_QUESTION]`
- Approved mechanism: `[CORE_MECHANISM]`
- Approved model: `[CANONICAL_MODEL]`
- Stage 7.5 verdict: `[STAGE_7_5_RESULT]`
- Stage 4A certification: `[STAGE_4A_RESULT]`
- Stage 7.5A certification: `[STAGE_7_5A_RESULT]`
- Closest papers: `[CLOSEST_PAPERS]`

## 2. Stage objective

Freeze the theoretical object so that later writing cannot silently change the model, propositions, quantifiers, benchmark definitions, or contribution claims.

## 3. Entry hard gate

Stage 8 may begin only if both are present and `GO`:

1. `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` from Stage 4A; and
2. `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS` from Stage 7.5A.

A Stage-4 or Stage-7.5 `GO`, green CI, successful symbolic reproduction, or a working production solver is not a substitute for either certificate.

## 4. Canonical inputs

Only results explicitly approved by the prior gates may enter the freeze. The Stage-4A theorem certificates and Stage-7.5A claim-scope ledger are canonical freeze inputs.

## 5. Allowed changes

Notation cleanup and unambiguous restatement only.

## 6. Prohibited changes

No new extensions, assumptions, propositions, welfare claims, function-class generalizations, benchmark relabeling, or literature positioning.

## 7. Mandatory freeze record

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
10. admissible function classes and shape restrictions;
11. equilibrium concept;
12. baseline equilibrium objects;
13. main propositions with exact quantifiers and domains;
14. welfare propositions and exact benchmark definitions;
15. proof/verification status;
16. approved robustness scope;
17. empirical/institutional interpretation;
18. closest-paper distinction;
19. claims explicitly not made;
20. Stage-4A theorem-certificate register;
21. Stage-7.5A claim-scope/quantifier register;
22. benchmark-definition register;
23. counterexample and regression-test register.

For sequential/game-theoretic models, additionally freeze:

24. off-path history classes relevant to unilateral deviations;
25. continuation-equilibrium status for those classes;
26. active-set/corner/order/participation handling;
27. solver outcome taxonomy and unresolved/failure count;
28. multiplicity/nonexistence and continuation-selection assumptions, if any;
29. independent direct-payoff/allocation verification artifact used for high-stakes equilibrium claims.

For each proposition classify proof/evidence maturity as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`.

## 8. Evidence requirements

Freeze references to the verified literature record, Stage-4A certificates, Stage-7.5A claim-scope ledger, and verification artifacts. Do not freeze an unverified conjecture as a theorem.

For a sequential model claiming SPNE/subgame perfection, retain `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` output as freeze evidence.

For each headline theorem retain `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` evidence or an equivalent completed certificate.

## 9. Verification protocol

Cross-check the freeze against Stage 4/4A/6/7/7.5/7.5A outputs and symbolic/numerical verification. Confirm parameter restrictions, function classes, theorem quantifiers, and benchmark labels exactly match the certified model.

For sequential games, confirm that on-path calculations and off-path continuation certification are separately auditable and no material solver failure was discarded from deviation searches.

For generality claims, confirm the manuscript-allowed wording does not exceed the Stage-7.5A maximum defensible wording.

## 10. Kill tests

Do not freeze if:

- Stage 4A or Stage 7.5A is missing, conditional, or failed;
- the model description differs from verified equations;
- a main proposition remains only numerically supported while presented as analytic;
- theorem quantifiers exceed the proof/certificate;
- a parametric result is relabeled generic without certification;
- a constrained planner benchmark is mislabeled `first best`;
- a claimed SPNE/global equilibrium has a material `UNRESOLVED` or `NUMERICAL_FAILURE` continuation;
- FOCs/SOCs/interiority on a regular branch substitute for full-strategy verification where a global claim is made;
- solver failure, invalid active set, or branch violation has been interpreted as an unprofitable deviation;
- the stated consumer/agent choice set differs from the allocation routine;
- closest-paper positioning is unresolved;
- theory changed after certification without re-running affected gates.

## 11. Success criteria

The frozen record must be sufficient for an independent researcher to know exactly what may be written and proved, at what quantifier scope, under which assumptions, and against which planner/equilibrium benchmark.

## 12. Failure criteria

Return to the earliest affected stage if any substantive inconsistency is found. Equilibrium/globality problems normally reopen Stage 4 and Stage 4A. Generality/quantifier problems normally reopen Stage 7.5A and any earlier stage whose theorem is actually false. Benchmark-definition problems reopen Stage 7 or Stage 4 depending on whether the underlying optimization problem is wrong or only mislabeled.

## 13. Required final output

1. Canonical theory specification
2. Proposition register with exact quantifiers
3. Parameter/function-class restriction register
4. Welfare/benchmark register
5. Verification status table
6. Stage-4A theorem-certificate register
7. Stage-7.5A claim-scope ledger
8. Continuation-completeness register, where applicable
9. Solver-failure/unresolved-continuation ledger, where applicable
10. Counterexample/regression-test register
11. Approved robustness list
12. Contribution/closest-paper statement
13. Explicit exclusions/prohibited stronger claims
14. Freeze identifier/date/SHA if applicable
15. Theory change-control procedure

## 14. Final verdict

Choose one:

- `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`
- `FREEZE BLOCKED` — identify the exact earlier stage to reopen

## 15. Theory change control

Any post-freeze theoretical change must record:

- what changed;
- why;
- affected equations/propositions;
- affected theorem certificates/quantifiers;
- affected benchmark definitions;
- affected verification;
- affected literature claims;
- stages that must be re-run.

Any change affecting equilibrium correctness/globality requires Stage 4/4A re-certification. Any change affecting theorem scope/generality/benchmark language requires Stage 7.5A re-certification. No silent theory drift is permitted.
