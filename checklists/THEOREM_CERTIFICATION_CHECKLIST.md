# Theorem Certification Checklist

Use this checklist for every headline equilibrium, theorem, proposition, welfare result, and broad robustness claim before theory freeze.

The checklist is designed to prevent two recurrent failure modes:

1. a locally valid/interior/regular-branch candidate being reported as a global equilibrium; and
2. a baseline or restricted theorem being reported with broader quantifiers, functional-form generality, or benchmark language than the proof supports.

A material item may be marked `NOT APPLICABLE` only with a written reason. `NOT TESTED` is not a passing state.

## A. Exact claim identity

- [ ] Give the claim a stable identifier.
- [ ] State the exact mathematical claim, not only prose.
- [ ] Record whether it is an equilibrium characterization, comparative static, threshold, welfare result, robustness result, existence/uniqueness result, or benchmark comparison.
- [ ] Record the manuscript sections in which the claim is used.

## B. Quantifier certificate

- [ ] Record every `for all`, `there exists`, `unique`, `generic`, `local`, `global`, `strict`, `weak`, and `almost everywhere` qualifier.
- [ ] Record the complete parameter domain.
- [ ] Record the complete strategy/choice domain.
- [ ] Record the admissible function class, if any.
- [ ] Confirm the proof establishes exactly those quantifiers.
- [ ] Confirm a sufficient condition is not described as necessary unless proved.
- [ ] Confirm an existence result is not described as uniqueness.
- [ ] Confirm a local or branch-specific result is not described as global.

## C. Assumption-dependence certificate

- [ ] List every assumption actually used in the proof.
- [ ] Separate economic assumptions from normalization/tractability assumptions.
- [ ] Separate shape restrictions from parameter restrictions.
- [ ] Identify which sign, concavity, uniqueness, or ordering conclusion uses which derivative/restriction.
- [ ] Identify any assumption that appears in prose but is not mathematically used.
- [ ] Identify any mathematically used assumption omitted from the theorem statement.

## D. Equilibrium/globality certificate

When applicable:

- [ ] Verify FOCs/KKT conditions.
- [ ] Verify SOCs/Hessian/principal-minor conditions.
- [ ] Verify feasibility and participation.
- [ ] Enumerate all relevant corners/boundaries.
- [ ] Enumerate active-set, entry/exit, zero-output, ordering, participation, and regime-switch cases.
- [ ] Search finite/global deviations over the actual strategy set.
- [ ] Distinguish a regular/interior candidate from a global best response.
- [ ] For sequential games, verify downstream continuation after material upstream deviations.
- [ ] Treat `None`, NaN, exception, invalid branch, or nonconvergence as `UNRESOLVED`, not as an unprofitable deviation.
- [ ] Record multiplicity/nonexistence where relevant.

## E. Independent reconstruction certificate

- [ ] Reconstruct at least one high-stakes payoff/allocation object directly from primitives where feasible.
- [ ] Use an independent derivation, evaluator, solver, or model/reviewer where feasible.
- [ ] Confirm the independent path does not merely call the production solver.
- [ ] Reconcile any discrepancy before `PASS`.

## F. Counterexample certificate

- [ ] Search analytically/symbolically for counterexamples where feasible.
- [ ] Search numerically only after analytic/symbolic characterization where feasible.
- [ ] Include boundary and near-boundary parameter values.
- [ ] Include near-singular or low-curvature/high-curvature cases when relevant.
- [ ] Include histories/strategies designed to exit the preferred branch.
- [ ] For broad function classes, construct admissible nonbaseline functions and try to reverse the claimed sign/concavity/ordering.
- [ ] Preserve every discovered counterexample as a regression test or permanent verification artifact.

## G. Functional-form/generality certificate

When a baseline functional form is used:

- [ ] Classify the result as baseline-only, restricted-class, sufficient-condition, numerical robustness, conjectured generality, or general theorem.
- [ ] Identify which parts depend on the baseline functional form.
- [ ] Verify that a quadratic/linear/CES/etc. result is not called generic without a separate proof.
- [ ] If the theorem ranges over `C^k`, monotone, convex, concave, supermodular, single-crossing, or another function class, verify the claimed result follows from exactly those restrictions.
- [ ] Record the strongest defensible generality statement.

## H. Benchmark-definition certificate

When welfare/planner benchmarks are used:

- [ ] Write the planner's objective explicitly.
- [ ] Write the planner's complete feasible choice set.
- [ ] Identify constraints inherited from technology/information/commitment/instruments.
- [ ] Verify the label `first best` is used only for the unrestricted relevant planner problem.
- [ ] Otherwise use the exact label: constrained first best, second best, fixed-allocation benchmark, restricted-instrument optimum, etc.
- [ ] Verify private/social comparisons use the same population, outside options, accounting, and feasibility conventions.

## I. Proof/evidence maturity

- [ ] Classify the claim as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`.
- [ ] Record proof location and verification artifact.
- [ ] Confirm numerical evidence is not presented as analytic proof.
- [ ] Confirm CI/reproduction of the same solver is not counted as independent certification.

## J. Manuscript-scope certificate

- [ ] Map the theorem to abstract wording.
- [ ] Map the theorem to introduction/contribution wording.
- [ ] Map the theorem to welfare/policy wording.
- [ ] Map the theorem to robustness wording.
- [ ] State the maximum defensible prose claim.
- [ ] State stronger wording that is prohibited.

## K. Final certificate state

Record one:

- `PASS` — exact scope verified; no material item remains untested.
- `CONDITIONAL` — one precise proof/scope blocker remains and the earliest affected stage is identified.
- `FAIL` — the claim is false, materially overstated, globally uncertified, or benchmark-misdefined.

A headline claim with `FAIL`, or with material `NOT TESTED`, blocks Stage 4A/7.5A `GO` and therefore blocks Stage 8 theory freeze.
