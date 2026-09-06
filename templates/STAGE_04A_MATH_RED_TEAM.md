# Stage 4A — Independent Mathematical Adversarial Certification Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as an independent hostile mathematical referee. Do not help the Stage-4 derivation succeed. Try to falsify it from primitives, with emphasis on global equilibrium, omitted regimes, boundary deviations, theorem scope, and benchmark definitions.

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

## 3. Frozen inputs

Players, timing, primitives, equilibrium concept, strategy sets, and candidate propositions are frozen. This stage may expose an error or scope restriction but may not repair the model silently.

## 4. Mandatory certification tasks

For every headline equilibrium/proposition:

1. Write the exact mathematical claim, including all quantifiers, parameter domains, strategy domains, regularity assumptions, and whether the claim is local, branch-specific, global, generic, or existential.
2. Reconstruct the relevant payoffs/allocation from primitives without relying solely on the Stage-4 solver or symbolic derivation.
3. Re-check identities, FOCs, SOCs/Hessians/KKT conditions, feasibility, participation, and existence/uniqueness as applicable.
4. Enumerate economically possible corners, boundaries, active-set changes, regime switches, ordering changes, zero-output/entry-exit states, discontinuities, kinks, and off-path histories relevant to the equilibrium concept.
5. Search for profitable finite/global deviations over the actual strategy set, not only infinitesimal deviations around the candidate solution.
6. For sequential games, re-solve material downstream continuation games after upstream deviations and fail closed on `UNRESOLVED`/`NUMERICAL_FAILURE` outcomes.
7. Deliberately construct stress histories/parameter values that invalidate maintained interiority or the preferred regular branch.
8. Run symbolic or analytic counterexample search first where feasible, followed by numerical/adversarial search over boundaries, near-singular cases, and regime transitions.
9. Verify at least one high-stakes claim with an independent direct-payoff/allocation evaluator or independently written solver where feasible.
10. Verify that welfare and benchmark labels correspond to the actual optimization problem and choice set. In particular, distinguish `first best`, `constrained first best`, `second best`, `fixed-allocation benchmark`, and other restricted planner problems.
11. Preserve every discovered counterexample as a permanent regression test or equivalent reproducible artifact.
12. Produce a theorem certificate for each headline claim using `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`.

## 5. Required theorem certificate fields

Each headline claim must record:

- exact claim;
- exact quantifiers;
- parameter and strategy domains;
- assumptions actually used in the proof;
- proof type and proof location;
- local/branch/global status;
- boundary/corner/regime audit status;
- continuation completeness status where applicable;
- independent reconstruction status;
- counterexample search design and result;
- benchmark-definition status where applicable;
- known limitations/exclusions;
- `PASS`, `CONDITIONAL`, or `FAIL`.

`NOT TESTED` on a material field blocks Stage-4A `GO` unless it is explicitly `NOT APPLICABLE` with a valid reason.

## 6. Kill tests

Stage 4A fails if any headline claim relies on:

- FOCs/SOCs/interiority as a substitute for global best-response verification;
- an omitted profitable boundary/corner/regime-switch deviation;
- an unresolved material continuation treated as unprofitable;
- a regular/on-path formula used outside its validity domain;
- solver failure or branch failure being filtered from deviation search;
- a theorem statement whose quantifiers exceed what the proof establishes;
- a benchmark label inconsistent with the planner's actual choice set;
- a numerical illustration presented as proof;
- an implementation-independent reconstruction that contradicts the production result.

## 7. Success criteria

`GO` requires all headline mathematical claims to have theorem certificates with no unresolved correctness blocker and no material `NOT TESTED` field.

For global/SPNE claims, all economically material deviation classes must be certified or proved irrelevant. For purely local/branch-specific claims, the manuscript-level scope must be explicitly restricted to that status.

## 8. Failure routing

- A derivation, equilibrium, domain, or proof error routes back to Stage 4.
- Exactly one diagnosed economic deficiency that requires one authorized model modification may route to Stage 5; after repair the project must repeat Stage 4 and Stage 4A.
- A false core mechanism without a bounded repair is `NO-GO` and terminates the branch or returns to Stage 3 for a genuinely distinct architecture.

## 9. Required final output

1. Executive adversarial verdict
2. Independent reconstruction summary
3. Headline theorem-certificate table
4. Global deviation/boundary/regime audit
5. Continuation audit where applicable
6. Counterexample search design and results
7. Benchmark-definition audit
8. Permanent regression tests created
9. Exact blocker and earliest affected stage, if any
10. Canonical stage verdict and routing

## 10. Final verdict

Choose exactly one:

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`
- `CONDITIONAL GO` — name exactly one correctness blocker and route to the earliest affected stage
- `NO-GO / REOPEN STAGE 4 OR EARLIER`

A `GO` routes to Stage 6 Novelty Re-Kill. No project may bypass Stage 4A merely because Stage 4, symbolic tests, CI, or the production solver are green.
