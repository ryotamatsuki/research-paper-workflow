# Paper-Specific Certification Inheritance Checklist

Use this checklist whenever a project uses a paper-specific route instead of the canonical Stage labels, including correction-paper routes such as `C0–C6`, replication/audit routes, fast-track note routes, or other bespoke checkpoint systems.

A paper-specific route may change labels and sequencing for project management. It may not silently weaken the mathematical or scope certification required by the canonical workflow for the claims it intends to make.

## 1. Inheritance rule

For each paper-specific checkpoint, map the claims being certified to the corresponding canonical obligations.

At minimum, ask whether the checkpoint certifies any of the following:

- equilibrium existence;
- equilibrium uniqueness or complete characterization;
- global/Nash/SPNE validity;
- comparative statics or threshold results;
- welfare or policy comparisons;
- robustness/generality;
- planner/benchmark labels;
- manuscript-level quantifiers or contribution wording.

If it does, the corresponding Stage-4A / Stage-7 / Stage-7.5A certification questions and evidence requirements inherit into the paper-specific route even if the Stage number is not used.

## 2. Required mapping table

Create a route-certification table with at least:

`paper-specific checkpoint | claim ID | canonical obligation inherited | attack required | artifact path | result | surviving limitation | status`.

A checkpoint cannot be declared mathematically complete merely because a bespoke protocol did not explicitly name the canonical test.

## 3. Equilibrium claims

Whenever a checkpoint certifies equilibrium claims, separate:

1. **candidate-deviation audit** — whether the proposed profile admits a profitable unilateral deviation; and
2. **alternative-equilibrium audit** — whether another strategy profile also satisfies equilibrium conditions.

A PASS on (1) is not a PASS on (2).

If the project claims only existence and no later claim depends on uniqueness, selection, or equilibrium-invariant outcomes, the alternative-equilibrium audit may be scoped out with a written justification. If the project claims uniqueness, complete characterization, `the equilibrium`, or selection-free outcomes, active alternative-equilibrium search is mandatory.

## 4. Indifference / zero-payoff trigger

Whenever a player has payoff-equivalent actions — including zero demand, zero output, zero profit, participation ties, bidding ties, matching ties, or contract-choice ties — trigger a dedicated audit.

Required attack:

- vary the indifferent player's action within the admissible indifference set;
- recompute other players' best responses/equilibrium conditions;
- record whether the equilibrium set, allocation, prices/actions, continuation play, or welfare changes.

Do not infer irrelevance from unchanged own payoff.

## 5. Selection / refinement provenance

Whenever a paper-specific route adds or relies on a selection rule, refinement, tie-break, no-loss condition, dominance restriction, price floor, or other auxiliary constraint, record:

- whether it is in the original model or newly imposed;
- which equilibria it removes;
- whether it also removes the preferred candidate;
- which claims survive without it;
- which claims become selection/refinement-conditional;
- whether the criterion has been applied symmetrically.

Weak-dominance reasoning must be tested against both inconvenient and preferred payoff-equivalent actions.

## 6. Welfare under multiplicity

For every material welfare/policy claim, state whether it holds for:

- all relevant equilibria;
- one selected equilibrium only;
- a refinement-defined subset; or
- an equilibrium-invariant allocation/welfare object.

If multiple markets, regions, subgames, or stages admit multiplicity, state whether their equilibrium selections may vary independently. Test admissible combinations whenever the paper makes a selection-free aggregate or welfare claim.

## 7. Evidence-bearing PASS

Every material PASS must link:

`claim -> attack actually performed -> proof/counterexample/code artifact -> surviving limitation`.

The following are not sufficient by themselves:

- `checked`;
- `verified`;
- `reviewed`;
- green CI;
- reproduction of the same production solver;
- a numerical grid that never searched the relevant equilibrium class;
- a no-profitable-deviation result offered as uniqueness evidence.

Material `NOT TESTED` blocks the corresponding strong claim. `NOT APPLICABLE` requires a written reason tied to the claim's exact scope.

## 8. Required inherited artifacts

A bespoke route should preserve equivalents of the following where applicable:

- theorem certificate;
- candidate-deviation audit;
- alternative-equilibrium / multiplicity audit;
- indifference-trigger audit;
- selection/refinement provenance audit;
- counterexample/regression-test register;
- welfare-selection robustness table;
- claim-scope / quantifier ledger;
- evidence ledger;
- certification-regression record when a later checkpoint discovers an earlier missed defect.

Artifact names and directories may be project-specific. The evidentiary content may not be omitted merely because the canonical Stage label is absent.

## 9. Certification regression

If a later paper-specific checkpoint discovers a defect that an earlier checkpoint should have detected, record:

`missed defect | earlier checkpoint | canonical obligation that should have caught it | missing attack/artifact | repair | earliest rollback point | permanent regression test`.

Do not repair only the current manuscript. Update the project route or reusable workflow so the same class of failure becomes mechanically harder to repeat.

## 10. Final route-level state

A paper-specific route may declare its mathematical/scope certification complete only when:

- every strong claim has been mapped to the relevant canonical obligation;
- applicable attacks were actually executed;
- evidence artifacts are identifiable;
- multiplicity/selection limitations are explicit;
- no material `NOT TESTED` item remains behind a strong claim; and
- any discovered certification regression has an explicit rollback and regression artifact.
