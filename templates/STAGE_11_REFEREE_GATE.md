# Stage 11 — Robustness / Referee Attack Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as multiple hostile referees and an editor. Try to reject `[WORKING_TITLE]` before external review does.

Stage 11 is a late independent defense layer. It does not replace Stage 4A mathematical adversarial certification or Stage 7.5A generality/quantifier certification.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Frozen theory: `[CANONICAL_MODEL]`
- Core mechanism: `[CORE_MECHANISM]`
- Main propositions: `[CURRENT_STAGE_RESULT]`
- Stage-4A theorem certificates: `[STAGE_4A_CERTIFICATES]`
- Stage-7.5A claim-scope ledger: `[STAGE_7_5A_CERTIFICATES]`
- Closest papers: `[CLOSEST_PAPERS]`
- Target journal: `[TARGET_JOURNAL]`
- Repository/manuscript: `[SOURCE_REPOSITORY]`

## 2. Stage objective

Identify fatal conceptual, mathematical, novelty, robustness, institutional, welfare, journal-fit, and claim-scope objections; require fixes only when they address a genuine vulnerability.

For sequential/game-theoretic papers, independently attack downstream continuation completeness rather than merely re-running the author's equilibrium solver.

For broad theorem/generalization claims, independently attack admissible function classes and quantifiers rather than merely rereading the production proof.

## 3. Canonical inputs

The current full draft, theory freeze, Stage-4A certificates, and Stage-7.5A claim-scope ledger are the objects under attack. Do not presume acceptance.

## 4. Allowed changes

You may recommend exposition fixes, additional verification, or an approved robustness exercise. Any substantive theory change must trigger formal theory-change control and reopening of affected stages.

## 5. Prohibited changes

Do not respond to every criticism by adding an extension. Do not bury fatal objections in minor comments.

Do not treat green CI, reproduction of the author's numbers, repeated execution of the same solver, or agreement of the same derivation path as independent equilibrium/theorem validation.

## 6. Mandatory attack classes

Use `checklists/REFEREE_ATTACK_CHECKLIST.md` and explicitly test at least:

- classic-result attack;
- ad-hoc-assumption attack;
- result-built-into-assumption attack;
- no-new-mechanism attack;
- alternative-demand attack;
- alternative-contract/information attack;
- participation/corner/boundary/regime-switch attack;
- welfare-is-mechanical attack;
- institution-too-specific attack;
- external-validity/generality attack;
- numerical-not-proof attack;
- proof/notation inconsistency attack;
- wrong-journal / insufficient-contribution attack;
- exposition/claim-inflation attack;
- theorem-quantifier inflation relative to Stage 7.5A;
- functional-form generality inflation;
- planner/benchmark terminology drift;
- global/SPNE claim drift relative to Stage 4A.

### Independent mathematical regression attack

For sequential/game-theoretic models:

- apply `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md`;
- select at least one material upstream deviation/off-path history and reconstruct downstream allocation/payoff from primitives without calling the manuscript's candidate equilibrium solver;
- deliberately search for a large finite deviation that exits the regular/interior branch;
- inspect every `None`, NaN, invalid, exception, or nonconvergence outcome and verify none is treated as an unprofitable deviation;
- challenge pure-strategy continuation existence and multiplicity where active-set/order/participation changes permit them;
- verify labels such as `global`, `whole-domain`, or `SPNE` match the economic domain certified at Stage 4A.

For broad theorem/function-class claims:

- apply `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` to at least one headline claim chosen adversarially;
- attempt at least one admissible nonbaseline function or parameter configuration designed to reverse the claimed sign, curvature, ordering, uniqueness, or threshold result;
- verify `for all`, `generic`, `unique`, `strict`, `global`, and similar words match the Stage-7.5A certificate;
- reconstruct planner choice sets for at least one high-stakes `first best`/`second best`/constrained benchmark comparison.

For every serious attack state:

`Attack → Severity → Evidence → Can the paper answer now? → Required fix → Earliest affected stage → Certification regression?`

## 7. Evidence requirements

Referee attacks must cite exact model assumptions, manuscript passages, prior papers, theorem certificates, or verification failures. Avoid generic complaints.

For equilibrium attacks, reproducing the manuscript's reported equilibrium path is insufficient. Distinguish on-path numerical correctness from off-path/global validity.

For theorem-scope attacks, distinguish a false theorem from correct mathematics paired with inflated prose.

## 8. Verification protocol

Re-run key symbolic/numerical gates where attacks concern mathematics. Re-open closest papers where attacks concern novelty. Check primary sources where attacks concern institutions.

At least one high-stakes mathematical attack should use an implementation or direct-payoff reconstruction logically independent of the code path used to generate the headline result, where feasible.

At least one high-stakes generality attack should search outside the baseline functional form when the manuscript makes a broader claim.

## 9. Kill tests

Classify each attack as:

- `FATAL`
- `MAJOR BUT FIXABLE`
- `MINOR`

A `FATAL` attack blocks submission preparation. If the only fix changes the mechanism or theorem, reopen the appropriate earlier stage rather than patching prose.

For an SPNE/global claim, a material `UNRESOLVED` or `NUMERICAL_FAILURE` continuation is at least a major correctness blocker.

For a broad theorem claim, one admissible counterexample inside the claimed domain is fatal to that theorem statement until scope is corrected or the theory is repaired.

## 10. Certification-regression rule

If Stage 11 discovers a flaw that Stage 4A or Stage 7.5A should have detected, label it `CERTIFICATION REGRESSION` and preserve it as workflow evidence.

Typical examples:

- profitable boundary/corner deviation missed at Stage 4A;
- off-path solver failure silently filtered after certification;
- broad `C^2`/convex/concave claim contradicted by an admissible function;
- strict comparative static stated beyond proved restrictions;
- constrained benchmark mislabeled `first best` despite Stage 7.5A.

The paper must roll back to the earliest invalidated stage. Do not treat late discovery as merely a Stage-11 patch.

## 11. Success criteria

No unresolved fatal attack on the main contribution; major fixes are bounded and do not require uncontrolled theory drift.

Continuation/globality and theorem scope must independently survive the hostile audit.

## 12. Failure criteria

Return to the earliest stage if novelty, mechanism identification, mathematical validity, continuation completeness, theorem quantifiers, benchmark definitions, or institutional coherence remains fatally vulnerable.

## 13. Required final output

1. Executive referee-gate verdict
2. Referee A: novelty/mechanism report
3. Referee B: assumptions/math/globality report
4. Referee C: welfare/institution/benchmark report
5. Referee D: journal/exposition/claim-scope report
6. Independent equilibrium/continuation re-audit, where applicable
7. Independent quantifier/function-class re-audit, where applicable
8. Solver-failure/unresolved-continuation ledger, where applicable
9. Certification-regression ledger
10. Consolidated severity table
11. Required fixes and earliest affected stage
12. Theory-change implications
13. Resolved vs unresolved attacks
14. Verdict and Stage-12 contract

## 14. Final verdict

Choose one:

- `GO TO JOURNAL POSITIONING`
- `CONDITIONAL GO` — bounded major fixes
- `REOPEN EARLIER STAGE / NO-GO`

## 15. Next-stage contract

Stage 12 selects a journal for the actual surviving certified contribution. It must not reshape the result or enlarge theorem scope to fit a preferred journal.
