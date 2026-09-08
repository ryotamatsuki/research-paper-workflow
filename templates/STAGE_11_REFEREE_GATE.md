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
- Stage-4A equilibrium-set / multiplicity evidence: `[EQUILIBRIUM_SET_CERTIFICATES]`
- Stage-7 welfare-selection robustness evidence: `[WELFARE_SELECTION_EVIDENCE]`
- Stage-7.5A claim-scope ledger: `[STAGE_7_5A_CERTIFICATES]`
- Closest papers: `[CLOSEST_PAPERS]`
- Target journal: `[TARGET_JOURNAL]`
- Repository/manuscript: `[SOURCE_REPOSITORY]`

## 2. Stage objective

Identify fatal conceptual, mathematical, novelty, robustness, institutional, welfare, journal-fit, equilibrium-selection, and claim-scope objections; require fixes only when they address a genuine vulnerability.

For sequential/game-theoretic papers, independently attack downstream continuation completeness rather than merely re-running the author's equilibrium solver.

For equilibrium papers generally, independently distinguish whether the manuscript has verified a proposed candidate against deviations or has actually characterized the equilibrium set.

For broad theorem/generalization claims, independently attack admissible function classes and quantifiers rather than merely rereading the production proof.

## 3. Canonical inputs

The current full draft, theory freeze, Stage-4A certificates, Stage-7 welfare-selection evidence, and Stage-7.5A claim-scope ledger are the objects under attack. Do not presume acceptance.

## 4. Allowed changes

You may recommend exposition fixes, additional verification, or an approved robustness exercise. Any substantive theory change must trigger formal theory-change control and reopening of affected stages.

## 5. Prohibited changes

Do not respond to every criticism by adding an extension. Do not bury fatal objections in minor comments.

Do not treat green CI, reproduction of the author's numbers, repeated execution of the same solver, a successful no-profitable-deviation test for one candidate, or agreement of the same derivation path as independent equilibrium/theorem validation.

## 6. Mandatory attack classes

Use `checklists/REFEREE_ATTACK_CHECKLIST.md` and explicitly test at least:

- classic-result attack;
- ad-hoc-assumption attack;
- result-built-into-assumption attack;
- no-new-mechanism attack;
- alternative-demand attack;
- alternative-contract/information attack;
- participation/corner/boundary/regime-switch attack;
- candidate-deviation-vs-alternative-equilibrium attack;
- payoff-indifference/zero-demand/zero-profit multiplicity attack;
- equilibrium-selection/refinement provenance and symmetry attack;
- welfare-selection robustness attack;
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

### Independent equilibrium-set regression attack

For every paper whose headline result uses an equilibrium characterization, uniqueness, equilibrium price/action, or selection-free allocation/welfare statement:

- choose at least one headline equilibrium candidate and independently repeat the **candidate-deviation audit** from primitives;
- separately search for at least one alternative equilibrium profile outside the preferred branch, emphasizing boundaries, ties, zero-demand/zero-output/zero-profit states, participation changes, and regime switches;
- verify that the manuscript does not infer uniqueness from the fact that the preferred candidate has no profitable unilateral deviation;
- when payoff indifference occurs, vary the indifferent player's action and recompute other players' best responses; test whether the action changes the equilibrium set or downstream conclusions despite leaving that player's own payoff unchanged;
- inspect every equilibrium-selection rule, tie-breaking assumption, no-loss restriction, dominance refinement, or auxiliary constraint and identify whether it originates in the model or was added later;
- apply every refinement symmetrically. If weak-dominance elimination is used to remove an inconvenient equilibrium, test whether it also removes a preferred payoff-equivalent or weakly dominated action;
- verify manuscript words such as `the equilibrium`, `unique`, `always`, and `regardless of equilibrium selection` against the Stage-4A equilibrium-set certificate.

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
- verify `for all`, `generic`, `unique`, `strict`, `global`, `for every equilibrium`, and similar words match the Stage-7.5A certificate;
- reconstruct planner choice sets for at least one high-stakes `first best`/`second best`/constrained benchmark comparison.

### Welfare-selection regression attack

When multiplicity exists anywhere relevant to a welfare or policy statement:

- choose at least one nonpreferred certified equilibrium and recompute the welfare comparison;
- if several markets, regions, subgames, or stages can select equilibria independently, test at least one admissible mixed selection profile rather than imposing the same preferred equilibrium everywhere;
- verify that a claim stated without selection qualifiers holds across the relevant equilibrium set;
- if not, require wording such as `under selection rule R`, `for the selected equilibrium`, or another exact scope statement.

For every serious attack state:

`Attack → Severity → Evidence → Can the paper answer now? → Required fix → Earliest affected stage → Certification regression?`

For every PASS state preserve:

`Claim → Attack actually performed → Proof/counterexample/code artifact → Surviving limitation`.

## 7. Evidence requirements

Referee attacks must cite exact model assumptions, manuscript passages, prior papers, theorem certificates, equilibrium-set artifacts, or verification failures. Avoid generic complaints.

For equilibrium attacks, reproducing the manuscript's reported equilibrium path is insufficient. Distinguish candidate verification from alternative-equilibrium search, and distinguish on-path numerical correctness from off-path/global validity.

For theorem-scope attacks, distinguish a false theorem from correct mathematics paired with inflated prose.

A material Stage-11 PASS must be evidence-bearing; `reviewed`, `checked`, or `looks correct` is not sufficient without an attack and artifact.

## 8. Verification protocol

Re-run key symbolic/numerical gates where attacks concern mathematics. Re-open closest papers where attacks concern novelty. Check primary sources where attacks concern institutions.

At least one high-stakes mathematical attack should use an implementation or direct-payoff reconstruction logically independent of the code path used to generate the headline result, where feasible.

At least one high-stakes equilibrium-set attack must search for an alternative equilibrium rather than only challenge deviations from the preferred candidate whenever the manuscript makes uniqueness, characterization, or selection-free claims.

At least one high-stakes generality attack should search outside the baseline functional form when the manuscript makes a broader claim.

## 9. Kill tests

Classify each attack as:

- `FATAL`
- `MAJOR BUT FIXABLE`
- `MINOR`

A `FATAL` attack blocks submission preparation. If the only fix changes the mechanism or theorem, reopen the appropriate earlier stage rather than patching prose.

For an SPNE/global claim, a material `UNRESOLVED` or `NUMERICAL_FAILURE` continuation is at least a major correctness blocker.

For a uniqueness/equilibrium-characterization claim, one additional admissible equilibrium is fatal to that statement until the claim is narrowed or the model/refinement is repaired.

For a selection-free welfare claim, one certified equilibrium or admissible cross-component selection profile reversing the result is fatal to that scope until qualified or repaired.

For a broad theorem claim, one admissible counterexample inside the claimed domain is fatal to that theorem statement until scope is corrected or the theory is repaired.

## 10. Certification-regression rule

If Stage 11 discovers a flaw that Stage 4A, Stage 7, or Stage 7.5A should have detected, label it `CERTIFICATION REGRESSION` and preserve it as workflow evidence.

Typical examples:

- profitable boundary/corner deviation missed at Stage 4A;
- preferred equilibrium passes deviation checks but another equilibrium was never searched for and contradicts uniqueness/selection-free claims;
- a zero-demand/zero-profit/payoff-indifferent action was dismissed because own payoff was unchanged even though it alters another player's best response;
- a weak-dominance or tie-breaking refinement was used only to remove an inconvenient equilibrium and would also remove the preferred action if applied symmetrically;
- off-path solver failure silently filtered after certification;
- welfare comparison stated selection-free although it changes across certified equilibria or independent component selections;
- broad `C^2`/convex/concave claim contradicted by an admissible function;
- strict comparative static stated beyond proved restrictions;
- constrained benchmark mislabeled `first best` despite Stage 7.5A;
- a prior `PASS` has no identifiable adversarial attack or evidence artifact.

The paper must roll back to the earliest invalidated stage. Do not treat late discovery as merely a Stage-11 patch.

The regression record should also state which earlier certification question or required artifact would have prevented the failure. The purpose is to improve the reusable workflow, not only the current paper.

## 11. Success criteria

No unresolved fatal attack on the main contribution; major fixes are bounded and do not require uncontrolled theory drift.

Candidate-deviation validity, equilibrium-set characterization at the claimed scope, continuation/globality, welfare-selection robustness, and theorem scope must independently survive the hostile audit where applicable.

## 12. Failure criteria

Return to the earliest stage if novelty, mechanism identification, mathematical validity, equilibrium multiplicity/selection, continuation completeness, welfare-selection robustness, theorem quantifiers, benchmark definitions, or institutional coherence remains fatally vulnerable.

## 13. Required final output

1. Executive referee-gate verdict
2. Referee A: novelty/mechanism report
3. Referee B: assumptions/math/globality report
4. Referee C: welfare/institution/benchmark report
5. Referee D: journal/exposition/claim-scope report
6. Candidate-deviation re-audit
7. Alternative-equilibrium / multiplicity re-audit
8. Indifference / zero-payoff re-audit
9. Selection/refinement provenance and symmetry audit
10. Independent equilibrium/continuation re-audit, where applicable
11. Welfare-selection regression audit, where applicable
12. Independent quantifier/function-class re-audit, where applicable
13. Solver-failure/unresolved-continuation ledger, where applicable
14. Evidence ledger for material PASS states
15. Certification-regression ledger
16. Consolidated severity table
17. Required fixes and earliest affected stage
18. Theory-change implications
19. Resolved vs unresolved attacks
20. Verdict and Stage-12 contract

## 14. Final verdict

Choose one:

- `GO TO JOURNAL POSITIONING`
- `CONDITIONAL GO` — bounded major fixes
- `REOPEN EARLIER STAGE / NO-GO`

## 15. Next-stage contract

Stage 12 selects a journal for the actual surviving certified contribution. It must not reshape the result, enlarge theorem scope, or suppress equilibrium-selection qualifications to fit a preferred journal.
