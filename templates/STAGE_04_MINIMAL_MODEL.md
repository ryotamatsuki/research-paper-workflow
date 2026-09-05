# Stage 4 — Minimal Model Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a skeptical theorist and symbolic-verification engineer. The goal is not to prove the desired proposition but to determine what the smallest defensible model actually implies.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Core question: `[CORE_RESEARCH_QUESTION]`
- Preferred mechanism: `[CORE_MECHANISM]`
- Closest papers: `[CLOSEST_PAPERS]`
- Proposed canonical model skeleton: `[CANONICAL_MODEL]`
- Allowed changes: `[ALLOWED_CHANGES]`
- Prohibited changes: `[PROHIBITED_CHANGES]`
- Contribution route: `[NEW MECHANISM / GENERALIZATION / UNIFICATION / NEW RESULT IN KNOWN MODEL]`
- Nested benchmarks, if applicable: `[NESTED_BENCHMARKS]`

## 2. Stage objective

Solve the minimal model completely, identify the economically meaningful parameter region, test candidate propositions, derive welfare, and decide whether the mechanism or generalization survives.

For a generalization/unification route, the stage must also determine what the full strategic architecture changes relative to the nested benchmark games.

For sequential games, “solve completely” includes the off-path continuation subgames required to evaluate upstream deviations under the stated equilibrium concept.

## 3. Canonical inputs

Freeze players, timing, information, strategy sets, consumer/agent choice sets, and all primitives not explicitly authorized for this stage.

## 4. Allowed changes

Only algebraically necessary normalization or notation cleanup. Any substantive model change requires stopping and returning to Stage 3/5.

## 5. Prohibited changes

- no feature accumulation after an inconvenient result;
- no ignoring corners or participation constraints;
- no treating FOCs/SOCs as equilibrium without full-strategy best-response verification where required;
- no extending a regular/interior/on-path formula to off-path histories outside its validity domain;
- no treating `None`, NaN, nonconvergence, invalid active set, or branch failure as evidence that a deviation is unprofitable;
- no numerical example as proof;
- no adding a fixed cost or transfer solely to manufacture a threshold;
- no declaring a generalization valuable merely because it contains more players or parameters than a benchmark.

## 6. Mandatory tasks

1. Derive utility/demand/allocation from the stated microfoundation where applicable, including the complete consumer/agent choice set.
2. Solve by backward induction or the appropriate equilibrium method.
3. Derive best responses, FOCs, SOCs, Hessians, existence, uniqueness, feasibility, participation, and KKT/corners where applicable.
4. Produce the full equilibrium in the smallest interpretable notation.
5. For every material upstream unilateral deviation in a sequential game, re-solve the downstream subgame on the strategy/history domain actually stated in the model.
6. Distinguish local/regular-branch candidates from global Nash equilibria. Test finite/global deviations, active-set changes, corners, kinks, ordering changes, participation changes, and boundary outcomes where feasible.
7. If pure-strategy continuation equilibrium may not exist, test for and report nonexistence. Do not silently discard the history. If mixed continuation is required for the claimed equilibrium concept, characterize it or stop the SPNE claim.
8. Use explicit solver outcome semantics: `SOLVED_EQUILIBRIUM`, `SOLVED_NO_EQUILIBRIUM`, `MULTIPLE_EQUILIBRIA`, `UNRESOLVED`, `NUMERICAL_FAILURE`. Material `UNRESOLVED`/`NUMERICAL_FAILURE` continuations block `GO`.
9. Construct an independent direct-payoff/allocation evaluator for at least one high-stakes equilibrium claim when feasible, and use it for adversarial deviation tests without calling the candidate equilibrium solver.
10. Derive profits, consumer surplus, total welfare, and private/social benchmarks when they are part of the research question.
11. Compute comparative statics analytically where possible.
12. Test limiting and boundary cases.
13. Write each desired result as a `Candidate Proposition` and actively search for counterexamples, including histories designed to break maintained regular/interior branches.
14. Any discovered equilibrium counterexample must be retained as a permanent regression test or equivalent verification artifact.
15. Identify sign-switch or threshold conditions when a derivative is ambiguous.
16. Decompose the mechanism into economic channels rather than reporting only derivatives.

### Additional tasks for generalization / unification routes

17. Define the minimum nested benchmark games by fixing/removing one strategic component at a time.
18. Solve or recover enough of each benchmark equilibrium to verify the claimed nesting.
19. Show explicitly whether the full model changes the best-response/strategic-feedback network.
20. Compare the full model and benchmarks for the headline object: equilibrium ordering, strategic complement/substitute relation, threshold, sign reversal, market-creation/displacement composition, welfare wedge, or conditions-for-effectiveness region.
21. Identify at least one full-model result that is not available as an immediate corollary of any benchmark alone.
22. If the full model only reproduces the union of known benchmark results, downgrade or kill the claimed generalization contribution.

## 7. Evidence requirements

Every reported closed form must be reproducibly derived. Any institutional interpretation must remain consistent with the primitive actually modeled.

A claim that the full strategic architecture adds theoretical value must be supported by explicit benchmark comparison, not by the absence of an exact prior paper title.

For sequential games, the equilibrium evidence must separately document on-path calculations and off-path continuation completeness. A solver's inability to evaluate a history is evidence of incompleteness, not evidence against the deviation.

## 8. Verification protocol

Use Python/SymPy or an equivalent symbolic system for all material algebra when applicable. Apply `checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md`. Only after symbolic/analytic work, use `checklists/NUMERICAL_VERIFICATION_CHECKLIST.md` when numerical counterexample search or positive-measure region mapping is relevant.

For sequential/game-theoretic models where off-path histories matter, apply `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` in full.

Recommended exact checks include `simplify(lhs-rhs)==0`, factorization, determinant/principal-minor checks, resultants, exact roots, and inequality reduction when feasible.

For generalization/unification routes, verify benchmark recovery symbolically whenever feasible: impose the restriction that removes a component and confirm that the full equilibrium collapses to the benchmark expression or equilibrium conditions.

If a verification item is genuinely not applicable, record `NOT APPLICABLE` and why; do not silently skip a substantive gate.

## 9. Kill tests

Kill or downgrade the mechanism if:

- the key equilibrium is infeasible or nonconcave in the economically relevant region;
- a claimed SPNE/global equilibrium relies on an unresolved off-path continuation;
- a finite deviation defeats a candidate that was certified only by FOCs/SOCs/interiority;
- a material continuation is discarded because the preferred branch/solver returns `None`, invalid, or nonconvergent;
- pure-strategy continuation equilibrium fails to exist on histories required by the claimed equilibrium concept and no valid alternative continuation is supplied;
- the desired proposition is false or knife-edge;
- the result is a market-size/intercept effect;
- the result is just a fixed-cost threshold;
- the result is created mechanically by a contract assumption;
- removing a cosmetic asymmetry eliminates everything;
- welfare is only transfer accounting;
- the mechanism duplicates a known result revealed by the algebra;
- a claimed generalization yields no strategically new feedback relative to its benchmarks;
- every headline result of the full model is already obtainable independently from one of the nested benchmarks;
- the only novelty is that several known benchmark cases are written inside one notation.

Do not kill a model solely because each component has a known precedent. The relevant question is whether the full equilibrium problem and results are strategically equivalent to prior work.

## 10. Success criteria

`GO` requires more than a monotone comparative static. At least one clean strategic trade-off, threshold ordering, sign reversal, organizational wedge, welfare result, or conditions-for-effectiveness characterization must survive exact analysis.

For any sequential model claiming SPNE/subgame perfection, `GO` additionally requires `PASS` on continuation completeness for the histories relevant to unilateral deviations. No material continuation may remain `UNRESOLVED` or `NUMERICAL_FAILURE`.

For a generalization/unification contribution, `GO` additionally requires:

- correct recovery of important nested benchmarks; and
- at least one economically substantive result generated by the interaction of strategic components that is unavailable in each benchmark alone.

## 11. Failure criteria and routing

- If the minimal mechanism/generalization survives without substantive repair, record `GO` and route directly to Stage 6 Novelty Re-Kill.
- If exactly one diagnosed economic deficiency remains and one authorized modification can test it, record `CONDITIONAL GO` and route to Stage 5 Mechanism Hardening with everything else frozen.
- If the mechanism fails economically or only produces trivial/known results without one defensible targeted repair, record `NO-GO` and stop the branch. Return to Stage 3 only for a genuinely distinct mechanism/generalization architecture, or Stage 0 for a distinct research question.

An unresolved continuation needed for an SPNE claim cannot be relabeled as a passed robustness check. A negative proof is a valid Stage 4 output. `NO-GO` does not itself authorize Stage 5.

## 12. Required final output

1. Executive verdict
2. Exact model and complete strategy/choice sets
3. Demand/technology/allocation derivation
4. Backward-induction equilibrium
5. SOC/existence/uniqueness
6. Full equilibrium and feasibility region
7. Participation/corners/active sets
8. Off-path continuation completeness audit, where applicable
9. Solver outcome/failure ledger, where applicable
10. Independent direct-payoff deviation audit, where applicable
11. Comparative statics
12. Mechanism decomposition
13. Candidate-proposition kill table
14. Consumer surplus and welfare, where applicable
15. Private vs social decision, where applicable
16. Limiting cases
17. Nested-benchmark recovery and comparison, where applicable
18. Full-model-only result table, where applicable
19. Numerical counterexample audit, where applicable
20. Permanent regression tests generated by counterexamples, where applicable
21. Artefact audit
22. Exact diagnosed blocker, if any
23. Canonical stage verdict
24. Routing/status output and next-stage contract

## 13. Final verdict

Record exactly one canonical stage verdict:

- `GO`
- `CONDITIONAL GO` — name exactly one blocker
- `NO-GO`

Then record the route separately:

- `GO` → Stage 6 Novelty Re-Kill
- `CONDITIONAL GO` → Stage 5 Mechanism Hardening
- `NO-GO` → terminate this branch; a distinct pivot must re-enter Stage 3 or Stage 0

## 14. Next-stage contract

If `CONDITIONAL GO`, Stage 5 may change only the one primitive needed to address the diagnosed deficiency. Everything else is frozen. If `GO`, Stage 6 receives the actual derived propositions unchanged, together with the nested-benchmark map when the claimed contribution is a generalization/unification.
