# Referee Attack Checklist

Use this checklist to simulate serious external review. Every attack should target a concrete claim, assumption, equation, source, theorem certificate, or journal-fit issue.

For each item use:

```text
Attack:
Severity: FATAL / MAJOR BUT FIXABLE / MINOR
Evidence:
Current response:
Required fix:
Earliest affected stage:
Certification regression?: YES / NO
Does the fix reopen theory?: YES / NO
Resolved?: YES / NO
```

## Novelty attacks

- [ ] “This is classic result X in different notation.”
- [ ] “The closest paper already contains the same mechanism.”
- [ ] “The contribution is only a new application.”
- [ ] “The model combines known components but generates no new interaction.”
- [ ] “The same theorem exists in an appendix / working paper.”

## Mechanism attacks

- [ ] “The claimed mechanism is built directly into the payoff/demand.”
- [ ] “The result is a market-size effect, not strategic interaction.”
- [ ] “The threshold exists only because a fixed cost was added.”
- [ ] “The extra player/channel has no independent economic role.”
- [ ] “The dynamic result is trivial state dependence.”

## Assumption attacks

- [ ] Essential assumption identified and defended
- [ ] Ad hoc contract assumption challenged
- [ ] Information/contractibility assumption challenged
- [ ] Symmetry/asymmetry assumption challenged
- [ ] Functional-form dependence challenged
- [ ] Participation/outside option challenged
- [ ] Institutional primitive challenged
- [ ] Consumer/agent choice set is explicit rather than inferred from a local demand formula
- [ ] Proof assumptions match theorem-statement assumptions exactly
- [ ] Shape restrictions actually imply the claimed sign/curvature/ordering

## Mathematical attacks

- [ ] FOC solution vs actual equilibrium
- [ ] SOC/Hessian failure
- [ ] Feasibility/interiority failure
- [ ] Corner/KKT omitted
- [ ] Parameter restriction inconsistent with claimed theorem
- [ ] Limiting case produces contradiction
- [ ] Numerical pattern presented as proof
- [ ] Welfare identity/accounting error
- [ ] Large finite unilateral deviation outside the regular/local branch
- [ ] Upstream deviation followed by full re-solution of the downstream subgame
- [ ] Off-path active-set/order/participation/regime change
- [ ] Pure-strategy continuation nonexistence or multiplicity
- [ ] Solver `None`/NaN/nonconvergence/invalid branch is being discarded rather than classified `UNRESOLVED`
- [ ] Independent direct-payoff/allocation reconstruction disagrees with the candidate solver
- [ ] Claimed `whole-domain`/`global`/`SPNE` verification actually conditions on survival of an interior/regular branch

For sequential games, apply `EQUILIBRIUM_CONTINUATION_CHECKLIST.md`. At least one hostile referee should reconstruct a material payoff/allocation from primitives without relying on the paper's equilibrium solver.

## Theorem scope / quantifier attacks

Apply `THEOREM_CERTIFICATION_CHECKLIST.md` to at least one adversarially selected headline theorem when the paper makes a broad or high-stakes claim.

- [ ] `for all` claim actually proved over the stated domain
- [ ] existence not inflated into uniqueness
- [ ] local result not inflated into global
- [ ] weak result not inflated into strict
- [ ] sufficient condition not inflated into necessary-and-sufficient
- [ ] baseline functional-form result not relabeled generic
- [ ] numerical robustness not relabeled analytic robustness
- [ ] broad function class (`C^k`, convex, concave, monotone, etc.) actually implies the claimed sign/curvature/order
- [ ] admissible nonbaseline function searched for as a counterexample
- [ ] abstract/introduction wording does not exceed the theorem certificate
- [ ] robustness section does not exceed the Stage-7.5A claim-scope ledger

## Robustness attacks

- [ ] Alternative demand system
- [ ] Alternative contract/instrument set
- [ ] Alternative timing
- [ ] Alternative outside option
- [ ] Boundary cases
- [ ] Removal of nonessential asymmetry
- [ ] Simplified/nested model
- [ ] Nonquadratic/nonlinear functional form when baseline convenience may drive a theorem
- [ ] Near-boundary / low-curvature / high-curvature parameterizations when relevant

## Welfare/policy/benchmark attacks

- [ ] Welfare result is only transfer accounting
- [ ] Consumer surplus is computed inconsistently
- [ ] Planner objective is explicit
- [ ] Planner feasible choice set is explicit
- [ ] `first best` is genuinely unrestricted over the relevant choices
- [ ] constrained first best / second best / fixed-allocation benchmark are not conflated
- [ ] private/social comparison uses consistent population, outside options, and accounting
- [ ] policy recommendation uses an unmodeled instrument
- [ ] externality is asserted rather than derived

## Institutional / empirical attacks

- [ ] Motivating fact verified by primary evidence
- [ ] Model primitive actually corresponds to the institution
- [ ] Suggestive evidence is labeled as such
- [ ] Generality goes beyond renaming industries
- [ ] Empirical prediction is observable in principle

## Journal / exposition attacks

- [ ] Contribution is sufficient for target journal
- [ ] Paper belongs to the claimed field rather than adjacent operations/management domain
- [ ] Introduction does not overclaim
- [ ] Related Literature handles closest papers directly
- [ ] Results explain mechanism
- [ ] Discussion does not repeat or enlarge results
- [ ] Conclusion adds no new claims
- [ ] Headline figure/table does not hide domain restrictions, use an arbitrary normalization as the reported economic object, or visually imply a stronger theorem than is proved
- [ ] Every central result has an appropriate exposition vehicle; absence of a figure/table is justified when theorem/prose is more efficient

## Certification-regression attacks

A Stage-11 reviewer should explicitly ask whether the full manuscript reveals a failure that the pre-freeze red-team gates should have caught.

- [ ] Stage-4A global-equilibrium certificate contradicted by a new boundary/corner/regime deviation
- [ ] Stage-4A continuation certificate contradicted by a new off-path history or solver-failure path
- [ ] Stage-7.5A quantifier certificate contradicted by an admissible function/parameter counterexample
- [ ] Stage-7.5A benchmark-definition certificate contradicted by the actual planner choice set
- [ ] Manuscript wording drifted beyond the certified maximum defensible claim

If yes, mark `CERTIFICATION REGRESSION`, preserve the counterexample as workflow evidence, and route to the earliest invalidated stage.

## Gate rule

- [ ] No unresolved `FATAL` attack on the core contribution
- [ ] Every `MAJOR BUT FIXABLE` attack has a bounded fix
- [ ] Any fix that changes theory is routed back through theory-change control
- [ ] For SPNE/sequential claims, no material off-path continuation remains `UNRESOLVED` or `NUMERICAL_FAILURE`
- [ ] Solver failures have not been silently filtered from deviation searches
- [ ] Headline theorem quantifiers do not exceed Stage-7.5A certification
- [ ] Benchmark language matches the certified planner problem
- [ ] Any certification regression is explicitly recorded and rolled back
- [ ] Minor comments are not used to obscure fatal issues
