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

## 3. Canonical inputs

Freeze players, timing, information, and all primitives not explicitly authorized for this stage.

## 4. Allowed changes

Only algebraically necessary normalization or notation cleanup. Any substantive model change requires stopping and returning to Stage 3/5.

## 5. Prohibited changes

- no feature accumulation after an inconvenient result;
- no ignoring corners or participation constraints;
- no treating FOCs as equilibrium without SOC/feasibility;
- no numerical example as proof;
- no adding a fixed cost or transfer solely to manufacture a threshold;
- no declaring a generalization valuable merely because it contains more players or parameters than a benchmark.

## 6. Mandatory tasks

1. Derive utility/demand from the stated microfoundation where applicable.
2. Solve by backward induction or the appropriate equilibrium method.
3. Derive best responses, FOCs, SOCs, Hessians, existence, uniqueness, feasibility, participation, and KKT/corners where applicable.
4. Produce the full equilibrium in the smallest interpretable notation.
5. Derive profits, consumer surplus, total welfare, and private/social benchmarks when they are part of the research question.
6. Compute comparative statics analytically where possible.
7. Test limiting and boundary cases.
8. Write each desired result as a `Candidate Proposition` and actively search for counterexamples.
9. Identify sign-switch or threshold conditions when a derivative is ambiguous.
10. Decompose the mechanism into economic channels rather than reporting only derivatives.

### Additional tasks for generalization / unification routes

11. Define the minimum nested benchmark games by fixing/removing one strategic component at a time.
12. Solve or recover enough of each benchmark equilibrium to verify the claimed nesting.
13. Show explicitly whether the full model changes the best-response/strategic-feedback network.
14. Compare the full model and benchmarks for the headline object: equilibrium ordering, strategic complement/substitute relation, threshold, sign reversal, market-creation/displacement composition, welfare wedge, or conditions-for-effectiveness region.
15. Identify at least one full-model result that is not available as an immediate corollary of any benchmark alone.
16. If the full model only reproduces the union of known benchmark results, downgrade or kill the claimed generalization contribution.

## 7. Evidence requirements

Every reported closed form must be reproducibly derived. Any institutional interpretation must remain consistent with the primitive actually modeled.

A claim that the full strategic architecture adds theoretical value must be supported by explicit benchmark comparison, not by the absence of an exact prior paper title.

## 8. Verification protocol

Use Python/SymPy or an equivalent symbolic system for all material algebra when applicable. Apply `checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md`. Only after symbolic/analytic work, use `checklists/NUMERICAL_VERIFICATION_CHECKLIST.md` when numerical counterexample search or positive-measure region mapping is relevant.

Recommended exact checks include `simplify(lhs-rhs)==0`, factorization, determinant/principal-minor checks, resultants, exact roots, and inequality reduction when feasible.

For generalization/unification routes, verify benchmark recovery symbolically whenever feasible: impose the restriction that removes a component and confirm that the full equilibrium collapses to the benchmark expression or equilibrium conditions.

If a verification item is genuinely not applicable, record `NOT APPLICABLE` and why; do not silently skip a substantive gate.

## 9. Kill tests

Kill or downgrade the mechanism if:

- the key equilibrium is infeasible or nonconcave in the economically relevant region;
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

For a generalization/unification contribution, `GO` additionally requires:

- correct recovery of important nested benchmarks; and
- at least one economically substantive result generated by the interaction of strategic components that is unavailable in each benchmark alone.

## 11. Failure criteria and routing

- If the minimal mechanism/generalization survives without substantive repair, record `GO` and route directly to Stage 6 Novelty Re-Kill.
- If exactly one diagnosed economic deficiency remains and one authorized modification can test it, record `CONDITIONAL GO` and route to Stage 5 Mechanism Hardening with everything else frozen.
- If the mechanism fails economically or only produces trivial/known results without one defensible targeted repair, record `NO-GO` and stop the branch. Return to Stage 3 only for a genuinely distinct mechanism/generalization architecture, or Stage 0 for a distinct research question.

A negative proof is a valid Stage 4 output. `NO-GO` does not itself authorize Stage 5.

## 12. Required final output

1. Executive verdict
2. Exact model
3. Demand/technology derivation
4. Backward-induction equilibrium
5. SOC/existence/uniqueness
6. Full equilibrium and feasibility region
7. Participation/corners
8. Comparative statics
9. Mechanism decomposition
10. Candidate-proposition kill table
11. Consumer surplus and welfare, where applicable
12. Private vs social decision, where applicable
13. Limiting cases
14. Nested-benchmark recovery and comparison, where applicable
15. Full-model-only result table, where applicable
16. Numerical counterexample audit, where applicable
17. Artefact audit
18. Exact diagnosed blocker, if any
19. Canonical stage verdict
20. Routing/status output and next-stage contract

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