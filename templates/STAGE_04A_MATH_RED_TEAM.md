# Stage 4A — Independent Mathematical Adversarial Certification Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as an independent hostile mathematical referee. Do not help the Stage-4 derivation succeed. Try to falsify it from primitives, with emphasis on global equilibrium, omitted regimes, alternative equilibria, payoff-indifferent actions, boundary deviations, theorem scope, equilibrium selection, and benchmark definitions.

The preferred reviewer/implementation should be independent of the one that constructed the Stage-4 solution. Independence can be provided by a different model, a clean-room derivation, a separately written evaluator/solver, or an equivalent method that does not inherit the production derivation's branch assumptions.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Canonical Stage-4 model: `[CANONICAL_MODEL]`
- Stage-4 propositions: `[CURRENT_STAGE_RESULT]`
- Equilibrium concept: `[EQUILIBRIUM_CONCEPT]`
- Strategy/choice domains: `[STRATEGY_DOMAINS]`
- Verification artifacts: `[VERIFICATION_ARTIFACTS]`
- Known branch/domain restrictions: `[KNOWN_BLOCKERS]`

## 2. Stage objective

Certify that the Stage-4 mathematical object survives an implementation-independent attempt to break it before novelty, welfare, manuscript, or journal work proceeds.

A Stage-4 `GO` is necessary but not sufficient. No theory project may route from Stage 4 directly to Stage 6.

The audit must distinguish two logically different questions:

1. **Candidate-deviation question:** holding the proposed equilibrium profile fixed, can any player profitably deviate?
2. **Alternative-equilibrium question:** does another strategy profile also satisfy equilibrium conditions?

A PASS on question 1 is not evidence of uniqueness and does not answer question 2. If the paper claims only existence and no downstream conclusion depends on equilibrium selection, the alternative-equilibrium search may be scoped accordingly, but that limitation must be explicit.

## 3. Frozen inputs

Players, timing, primitives, equilibrium concept, strategy sets, and candidate propositions are frozen. This stage may expose an error or scope restriction but may not repair the model silently.

## 4. Mandatory certification tasks

For every headline equilibrium/proposition:

1. Write the exact mathematical claim, including all quantifiers, parameter domains, strategy domains, regularity assumptions, and whether the claim is local, branch-specific, global, generic, existential, unique, or selection-dependent.
2. Reconstruct the relevant payoffs/allocation from primitives without relying solely on the Stage-4 solver or symbolic derivation.
3. Re-check identities, FOCs, SOCs/Hessians/KKT conditions, feasibility, participation, and existence/uniqueness as applicable.
4. Enumerate economically possible corners, boundaries, active-set changes, regime switches, ordering changes, zero-output/entry-exit states, discontinuities, kinks, ties, payoff-indifferent actions, and off-path histories relevant to the equilibrium concept.
5. Conduct the **candidate-deviation audit**: search for profitable finite/global unilateral deviations over the actual strategy set, not only infinitesimal deviations around the candidate solution.
6. Conduct the **alternative-equilibrium audit** separately whenever uniqueness, equilibrium characterization, equilibrium-invariant outcomes, or selection-free welfare claims are made. Search for other profiles satisfying the equilibrium conditions, especially on boundaries, tie sets, zero-demand/zero-profit states, participation changes, and regime switches.
7. Record the equilibrium-set status as `UNIQUE`, `MULTIPLE`, `EXISTENCE ONLY`, or `UNRESOLVED` on the claimed domain. If multiple equilibria exist, determine which prices/actions, allocations, profits, welfare results, and comparative statics are invariant across them.
8. Trigger an **indifference audit** whenever a player has two or more payoff-equivalent actions, including zero demand, zero output, zero profit, participation ties, bidding ties, matching ties, or contract-choice ties. Change that player's action within the indifference set and recompute other players' best responses and equilibrium conditions. Never infer irrelevance from unchanged own payoff alone.
9. For sequential games, re-solve material downstream continuation games after upstream deviations and fail closed on `UNRESOLVED`/`NUMERICAL_FAILURE` outcomes.
10. Deliberately construct stress histories/parameter values that invalidate maintained interiority or the preferred regular branch.
11. Run symbolic or analytic counterexample search first where feasible, followed by numerical/adversarial search over boundaries, near-singular cases, regime transitions, and candidate multiplicity regions.
12. Verify at least one high-stakes claim with an independent direct-payoff/allocation evaluator or independently written solver where feasible.
13. Audit every equilibrium-selection rule, refinement, tie-breaking condition, no-loss restriction, dominance argument, or auxiliary constraint used to eliminate multiplicity. State whether it is part of the original model or newly added, which equilibria it removes, whether it also removes the preferred candidate, and which claims survive without it. Apply refinements symmetrically.
14. In particular, if weak-dominance reasoning is invoked, test whether the same criterion would also eliminate payoff-equivalent or weakly dominated actions required by the paper's preferred equilibrium.
15. Verify that welfare and benchmark labels correspond to the actual optimization problem and choice set. For every welfare comparison under multiplicity, state whether it holds for one selected equilibrium or all relevant equilibria.
16. If several markets, regions, subgames, or stages admit multiplicity, determine whether their equilibrium selections can vary independently and whether that changes aggregate or welfare conclusions.
17. Preserve every discovered counterexample, additional equilibrium, and certification failure as a permanent regression test or equivalent reproducible artifact.
18. Produce a theorem certificate for each headline claim using `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`.
19. For every material PASS item, record an evidence row: `claim -> attack performed -> proof/counterexample/code artifact -> surviving limitation`. Narrative assertions such as `checked` or `verified` are insufficient.

## 5. Required theorem certificate fields

Each headline claim must record:

- exact claim;
- exact quantifiers;
- parameter and strategy domains;
- assumptions actually used in the proof;
- proof type and proof location;
- local/branch/global status;
- candidate-deviation audit status;
- alternative-equilibrium/multiplicity audit status;
- indifference-trigger audit status where applicable;
- equilibrium-selection/refinement status where applicable;
- boundary/corner/regime audit status;
- continuation completeness status where applicable;
- independent reconstruction status;
- counterexample search design and result;
- welfare-selection robustness status where applicable;
- benchmark-definition status where applicable;
- evidence/artifact path for each material PASS;
- known limitations/exclusions;
- `PASS`, `CONDITIONAL`, or `FAIL`.

`NOT TESTED` on a material field blocks Stage-4A `GO` unless it is explicitly `NOT APPLICABLE` with a valid reason.

## 6. Kill tests

Stage 4A fails if any headline claim relies on:

- FOCs/SOCs/interiority as a substitute for global best-response verification;
- a no-profitable-deviation check as evidence of uniqueness without an alternative-equilibrium search;
- an omitted profitable boundary/corner/regime-switch deviation;
- an omitted additional equilibrium that invalidates uniqueness, equilibrium characterization, or a selection-free downstream conclusion;
- payoff indifference, zero demand, zero output, or zero profit being treated as irrelevant without testing effects on other players' best responses;
- an equilibrium-selection/refinement condition introduced ad hoc without identifying which equilibria it removes and whether it also removes the preferred candidate;
- an unresolved material continuation treated as unprofitable;
- a regular/on-path formula used outside its validity domain;
- solver failure or branch failure being filtered from deviation search;
- a theorem statement whose quantifiers exceed what the proof establishes;
- a welfare claim that is valid only under one equilibrium selection but is stated selection-free;
- a benchmark label inconsistent with the planner's actual choice set;
- a numerical illustration presented as proof;
- an implementation-independent reconstruction that contradicts the production result;
- a material PASS with no identifiable attack/evidence artifact.

## 7. Success criteria

`GO` requires all headline mathematical claims to have theorem certificates with no unresolved correctness blocker and no material `NOT TESTED` field.

For global/SPNE claims, all economically material deviation classes must be certified or proved irrelevant. For uniqueness/equilibrium-characterization claims, alternative equilibria must have been actively searched for rather than inferred away from candidate verification. For purely local, branch-specific, or existence-only claims, the manuscript-level scope must be explicitly restricted to that status.

Whenever indifference or zero-payoff conditions are present, `GO` additionally requires evidence that alternative payoff-equivalent actions do not create unaccounted equilibria or alter conclusions, or else an explicit multiplicity/selection characterization.

## 8. Failure routing

- A derivation, equilibrium, domain, multiplicity, selection, or proof error routes back to Stage 4.
- Exactly one diagnosed economic deficiency that requires one authorized model modification may route to Stage 5; after repair the project must repeat Stage 4 and Stage 4A.
- A false core mechanism without a bounded repair is `NO-GO` and terminates the branch or returns to Stage 3 for a genuinely distinct architecture.

## 9. Required final output

1. Executive adversarial verdict
2. Independent reconstruction summary
3. Headline theorem-certificate table
4. Candidate-deviation audit
5. Alternative-equilibrium / multiplicity audit
6. Indifference / zero-payoff trigger audit
7. Equilibrium-selection / refinement audit
8. Global boundary/regime audit
9. Continuation audit where applicable
10. Counterexample search design and results
11. Welfare-selection and benchmark-definition audit
12. Evidence ledger: `claim | attack | artifact | result | surviving limitation`
13. Permanent regression tests created
14. Exact blocker and earliest affected stage, if any
15. Canonical stage verdict and routing

## 10. Final verdict

Choose exactly one:

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`
- `CONDITIONAL GO` — name exactly one correctness blocker and route to the earliest affected stage
- `NO-GO / REOPEN STAGE 4 OR EARLIER`

A `GO` routes to Stage 6 Novelty Re-Kill. No project may bypass Stage 4A merely because Stage 4, symbolic tests, CI, a no-profitable-deviation test, or the production solver are green.
