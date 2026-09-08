# Theorem Certification Checklist

Use this checklist for every headline equilibrium, theorem, proposition, welfare result, and broad robustness claim before theory freeze.

The checklist is designed to prevent four recurrent failure modes:

1. a locally valid/interior/regular-branch candidate being reported as a global equilibrium;
2. a baseline or restricted theorem being reported with broader quantifiers, functional-form generality, or benchmark language than the proof supports;
3. verification that a proposed equilibrium has no profitable deviation being mistaken for a search showing that no other equilibrium exists; and
4. payoff-indifferent, zero-demand, zero-profit, or tie actions being treated as irrelevant even when changing them can alter another player's best response, equilibrium set, allocation, or welfare.

A material item may be marked `NOT APPLICABLE` only with a written reason. `NOT TESTED` is not a passing state.

For every material certificate, preserve an evidence link of the form:

`claim -> adversarial attack performed -> proof/counterexample/code artifact -> surviving limitation`.

A bare statement such as `checked`, `verified`, or `PASS` is not evidence.

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

When applicable, complete the following sub-audits separately. Passing one does not imply passing another.

### D1. Candidate-deviation audit

This asks: **given the proposed strategy profile, is there a profitable unilateral deviation?**

- [ ] Verify FOCs/KKT conditions.
- [ ] Verify SOCs/Hessian/principal-minor conditions.
- [ ] Verify feasibility and participation.
- [ ] Enumerate all relevant corners/boundaries.
- [ ] Enumerate active-set, entry/exit, zero-output, ordering, participation, and regime-switch cases.
- [ ] Search finite/global deviations over the actual strategy set.
- [ ] Distinguish a regular/interior candidate from a global best response.
- [ ] For sequential games, verify downstream continuation after material upstream deviations.
- [ ] Treat `None`, NaN, exception, invalid branch, or nonconvergence as `UNRESOLVED`, not as an unprofitable deviation.

### D2. Alternative-equilibrium / multiplicity audit

This asks: **does another strategy profile also satisfy the equilibrium conditions?**

- [ ] Search for alternative pure-strategy equilibrium profiles outside the presented candidate branch.
- [ ] Search boundaries, ties, zero-demand/zero-output states, participation changes, and regime switches as possible sources of additional equilibria.
- [ ] Where tractable, solve or enumerate the equilibrium correspondence rather than only checking the presented candidate.
- [ ] Record whether the equilibrium is `UNIQUE`, `MULTIPLE`, `EXISTENCE ONLY`, or `UNRESOLVED` on the claimed domain.
- [ ] If multiplicity exists, characterize whether equilibrium prices/actions, allocations, profits, welfare, or policy conclusions are invariant across equilibria.
- [ ] If only existence is claimed and multiplicity is immaterial to every downstream claim, explain why the alternative-equilibrium audit is not required beyond that scope.

**Certification rule:** a successful no-profitable-deviation test in D1 is not evidence of uniqueness and does not satisfy D2. Conversely, finding one additional equilibrium does not by itself invalidate a correctly stated existence claim; it invalidates uniqueness or any selection-independent conclusion that is not robust across the equilibrium set.

### D3. Indifference / zero-payoff trigger audit

Trigger this audit whenever two or more actions give the same payoff to a player, including zero-demand, zero-output, zero-profit, participation/nonparticipation ties, bidding ties, matching ties, or contract-choice indifference.

- [ ] Identify the complete set of payoff-equivalent actions that are economically admissible.
- [ ] Change the indifferent player's action within that set and recompute other players' best responses and the equilibrium conditions.
- [ ] Check whether the equilibrium set, prices/actions, allocation, participation, continuation play, or welfare changes.
- [ ] Do not dismiss an action as irrelevant merely because the acting player's own payoff is unchanged.
- [ ] Preserve any newly discovered equilibrium or counterexample as a regression artifact.

## E. Equilibrium selection / refinement certificate

Complete whenever multiplicity is resolved by an added restriction, selection rule, refinement, tie-breaking assumption, price floor, no-loss condition, dominance argument, or other auxiliary criterion.

- [ ] State whether the criterion belongs to the original model, is standard but previously unstated, or is newly imposed for this paper.
- [ ] Identify exactly which equilibria the criterion removes.
- [ ] Verify that the criterion does not also remove the candidate equilibrium needed for the paper's main result.
- [ ] State which claims remain valid without the criterion.
- [ ] State which claims are conditional on the selected/refined equilibrium.
- [ ] Test the refinement symmetrically; do not use a principle only against inconvenient equilibria.
- [ ] In particular, if weak-dominance reasoning is used, verify it does not also eliminate economically required weakly dominated or payoff-equivalent actions elsewhere in the model.

## F. Independent reconstruction certificate

- [ ] Reconstruct at least one high-stakes payoff/allocation object directly from primitives where feasible.
- [ ] Use an independent derivation, evaluator, solver, or model/reviewer where feasible.
- [ ] Confirm the independent path does not merely call the production solver.
- [ ] Reconcile any discrepancy before `PASS`.

## G. Counterexample certificate

- [ ] Search analytically/symbolically for counterexamples where feasible.
- [ ] Search numerically only after analytic/symbolic characterization where feasible.
- [ ] Include boundary and near-boundary parameter values.
- [ ] Include near-singular or low-curvature/high-curvature cases when relevant.
- [ ] Include histories/strategies designed to exit the preferred branch.
- [ ] For broad function classes, construct admissible nonbaseline functions and try to reverse the claimed sign/concavity/ordering.
- [ ] Preserve every discovered counterexample as a regression test or permanent verification artifact.

## H. Functional-form/generality certificate

When a baseline functional form is used:

- [ ] Classify the result as baseline-only, restricted-class, sufficient-condition, numerical robustness, conjectured generality, or general theorem.
- [ ] Identify which parts depend on the baseline functional form.
- [ ] Verify that a quadratic/linear/CES/etc. result is not called generic without a separate proof.
- [ ] If the theorem ranges over `C^k`, monotone, convex, concave, supermodular, single-crossing, or another function class, verify the claimed result follows from exactly those restrictions.
- [ ] Record the strongest defensible generality statement.

## I. Benchmark-definition and welfare-selection certificate

When welfare/planner benchmarks are used:

- [ ] Write the planner's objective explicitly.
- [ ] Write the planner's complete feasible choice set.
- [ ] Identify constraints inherited from technology/information/commitment/instruments.
- [ ] Verify the label `first best` is used only for the unrestricted relevant planner problem.
- [ ] Otherwise use the exact label: constrained first best, second best, fixed-allocation benchmark, restricted-instrument optimum, etc.
- [ ] Verify private/social comparisons use the same population, outside options, accounting, and feasibility conventions.
- [ ] State whether each welfare comparison concerns one selected equilibrium or every equilibrium in the relevant equilibrium set.
- [ ] If multiple markets, regions, subgames, or stages admit multiplicity, state whether equilibrium selections can vary independently across them.
- [ ] If the welfare ranking changes with equilibrium selection, downgrade any selection-free welfare claim accordingly.

## J. Proof/evidence maturity and evidence ledger

- [ ] Classify the claim as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`.
- [ ] Record proof location and verification artifact.
- [ ] Record the exact adversarial attack actually performed for each material certification field.
- [ ] Record the counterexample, code, derivation, enumeration, or proof artifact that supports the result of that attack.
- [ ] Record any surviving limitation or unresolved domain.
- [ ] Confirm numerical evidence is not presented as analytic proof.
- [ ] Confirm CI/reproduction of the same solver is not counted as independent certification.
- [ ] Confirm `PASS` is not awarded from narrative assurance alone.

Minimum evidence-ledger row:

`claim | attack performed | evidence/artifact path | result | surviving limitation | certificate state`.

## K. Manuscript-scope certificate

- [ ] Map the theorem to abstract wording.
- [ ] Map the theorem to introduction/contribution wording.
- [ ] Map the theorem to welfare/policy wording.
- [ ] Map the theorem to robustness wording.
- [ ] State the maximum defensible prose claim.
- [ ] State stronger wording that is prohibited.

## L. Final certificate state

Record one:

- `PASS` — exact scope verified; required deviation, multiplicity/selection, indifference-trigger, welfare-selection, and evidence-ledger audits are complete for the claim's scope; no material item remains untested.
- `CONDITIONAL` — one precise proof/scope blocker remains and the earliest affected stage is identified.
- `FAIL` — the claim is false, materially overstated, globally uncertified, selection-dependent without qualification, or benchmark-misdefined.

A headline claim with `FAIL`, with material `NOT TESTED`, or with an applicable audit lacking evidence-linked execution blocks Stage 4A/7.5A `GO` and therefore blocks Stage 8 theory freeze.
