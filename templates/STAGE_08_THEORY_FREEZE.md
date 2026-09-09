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
- Formal-verification state: `[FORMAL_VERIFICATION_STATE]`
- Formal-verification certificate / N/A rationale: `[FORMAL_VERIFICATION_ARTIFACT]`
- Closest papers: `[CLOSEST_PAPERS]`

## 2. Stage objective

Freeze the theoretical object so that later writing cannot silently change the model, propositions, quantifiers, benchmark definitions, contribution claims, or the boundary of any proof-assistant certification.

## 3. Entry hard gate

Stage 8 may begin only if all are present:

1. `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` from Stage 4A;
2. `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS` from Stage 7.5A; and
3. the Stage-7.5A Formal Verification Gate is closed with exactly one of:
   - `FORMAL VERIFICATION PASS`; or
   - `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

A Stage-4 or Stage-7.5 `GO`, green CI, successful symbolic reproduction, a working production solver, or an unassessed proof-assistant repository is not a substitute for these certificates.

`NOT TESTED`, `PLANNED`, failed compilation, unresolved statement-fidelity mismatch, unexplained proof escape hatch, or a stale formal certificate blocks theory freeze when formal verification is applicable.

## 4. Canonical inputs

Only results explicitly approved by the prior gates may enter the freeze. The Stage-4A theorem certificates, Stage-7.5A claim-scope ledger, and Stage-7.5A formal-verification certificate or recorded `NOT APPLICABLE` rationale are canonical freeze inputs.

## 5. Allowed changes

Notation cleanup and unambiguous restatement only.

## 6. Prohibited changes

No new extensions, assumptions, propositions, welfare claims, function-class generalizations, benchmark relabeling, literature positioning, or silent expansion of what a formal proof is said to certify.

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
22. formal-verification applicability decision;
23. formal-verification certificate or `NOT APPLICABLE` rationale;
24. paper-claim ↔ formal-theorem mapping, where applicable;
25. assumptions encoded but not proved inside the assistant, where applicable;
26. components explicitly outside the formalization, where applicable;
27. proof-assistant/toolchain/library/build provenance, where applicable;
28. axiom/placeholder status, where applicable;
29. benchmark-definition register;
30. counterexample and regression-test register.

For sequential/game-theoretic models, additionally freeze:

31. off-path history classes relevant to unilateral deviations;
32. continuation-equilibrium status for those classes;
33. active-set/corner/order/participation handling;
34. solver outcome taxonomy and unresolved/failure count;
35. multiplicity/nonexistence and continuation-selection assumptions, if any;
36. independent direct-payoff/allocation verification artifact used for high-stakes equilibrium claims.

For each proposition classify proof/evidence maturity as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`.

Where formal verification is used, also classify the formal coverage as `FULL CLAIM`, `PROOF-CRITICAL CORE`, or another exact bounded scope. Do not collapse analytic proof maturity and formal-proof coverage into one label.

## 8. Evidence requirements

Freeze references to the verified literature record, Stage-4A certificates, Stage-7.5A claim-scope ledger, formal-verification certificate/N-A rationale, and verification artifacts. Do not freeze an unverified conjecture as a theorem.

For a sequential model claiming SPNE/subgame perfection, retain `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` output as freeze evidence.

For each headline theorem retain `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` evidence or an equivalent completed certificate.

Retain `checklists/FORMAL_VERIFICATION_CHECKLIST.md` output for every theorem-bearing project. If the outcome is `FORMAL VERIFICATION PASS`, preserve the formal source paths, exact toolchain/library versions where feasible, build evidence, theorem mapping, axiom/placeholder audit, and explicit non-formalized scope.

## 9. Verification protocol

Cross-check the freeze against Stage 4/4A/6/7/7.5/7.5A outputs and symbolic/numerical verification. Confirm parameter restrictions, function classes, theorem quantifiers, and benchmark labels exactly match the certified model.

For sequential games, confirm that on-path calculations and off-path continuation certification are separately auditable and no material solver failure was discarded from deviation searches.

For generality claims, confirm the manuscript-allowed wording does not exceed the Stage-7.5A maximum defensible wording.

For formalized claims, confirm that the current paper theorem matches the formal theorem/certificate that actually passed, that supplied hypotheses are not being described as formally derived, and that the proof assistant is not credited with certifying model components that remain outside the formalization.

## 10. Kill tests

Do not freeze if:

- Stage 4A or Stage 7.5A is missing, conditional, or failed;
- the formal-verification state is missing, `NOT TESTED`, `PLANNED`, failed, stale, or otherwise unresolved;
- `FORMALIZATION NOT APPLICABLE` is asserted without a recorded reason;
- an applicable formal artifact contains an unexplained `sorry`, `admit`, equivalent placeholder, conclusion-smuggling axiom/definition, failed build, or statement-fidelity mismatch;
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
- theory changed after certification without re-running affected gates;
- manuscript-allowed language says the assistant proves the complete model/equilibrium correspondence when only a bounded core is formalized.

## 11. Success criteria

The frozen record must be sufficient for an independent researcher to know exactly what may be written and proved, at what quantifier scope, under which assumptions, against which planner/equilibrium benchmark, and—where formal verification is used—exactly which components are kernel-checked versus supplied or left outside the formal model.

## 12. Failure criteria

Return to the earliest affected stage if any substantive inconsistency is found. Equilibrium/globality problems normally reopen Stage 4 and Stage 4A. Generality/quantifier problems normally reopen Stage 7.5A and any earlier stage whose theorem is actually false. Benchmark-definition problems reopen Stage 7 or Stage 4 depending on whether the underlying optimization problem is wrong or only mislabeled.

Formal-source/build defects that do not alter certified mathematics return to the Stage-7.5A Formal Verification Gate. A false theorem or missing economic assumption exposed by formalization returns to the earliest affected analytic stage.

## 13. Required final output

1. Canonical theory specification
2. Proposition register with exact quantifiers
3. Parameter/function-class restriction register
4. Welfare/benchmark register
5. Verification status table
6. Stage-4A theorem-certificate register
7. Stage-7.5A claim-scope ledger
8. Formal-verification state and certificate / `NOT APPLICABLE` rationale
9. Formal theorem mapping and explicit non-formalized scope, where applicable
10. Continuation-completeness register, where applicable
11. Solver-failure/unresolved-continuation ledger, where applicable
12. Counterexample/regression-test register
13. Approved robustness list
14. Contribution/closest-paper statement
15. Explicit exclusions/prohibited stronger claims
16. Freeze identifier/date/SHA if applicable
17. Theory change-control procedure

## 14. Final verdict

Choose one:

- `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`
- `FREEZE BLOCKED` — identify the exact earlier stage or Stage-7.5A formal-verification sub-gate to reopen

## 15. Theory change control

Any post-freeze theoretical change must record:

- what changed;
- why;
- affected equations/propositions;
- affected theorem certificates/quantifiers;
- affected benchmark definitions;
- affected formal theorem statements/certificates, where applicable;
- affected verification;
- affected literature claims;
- stages that must be re-run.

Any change affecting equilibrium correctness/globality requires Stage 4/4A re-certification. Any change affecting theorem scope/generality/benchmark language requires Stage 7.5A re-certification. Any material change to a formally certified theorem, encoded hypothesis, or proof-critical identity marks the formal certificate stale and requires a fresh Formal Verification Gate before refreeze. No silent theory drift is permitted.
