# Referee Attack Checklist

Use this checklist to simulate serious external review. Every attack should target a concrete claim, assumption, equation, source, or journal-fit issue.

For each item use:

```text
Attack:
Severity: FATAL / MAJOR BUT FIXABLE / MINOR
Evidence:
Current response:
Required fix:
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

## Robustness attacks

- [ ] Alternative demand system
- [ ] Alternative contract/instrument set
- [ ] Alternative timing
- [ ] Alternative outside option
- [ ] Boundary cases
- [ ] Removal of nonessential asymmetry
- [ ] Simplified/nested model

## Welfare/policy attacks

- [ ] Welfare result is only transfer accounting
- [ ] Consumer surplus is computed inconsistently
- [ ] First-best and decentralized benchmarks are conflated
- [ ] Policy recommendation uses an unmodeled instrument
- [ ] Externality is asserted rather than derived

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
- [ ] Discussion does not repeat results
- [ ] Conclusion adds no new claims

## Gate rule

- [ ] No unresolved `FATAL` attack on the core contribution
- [ ] Every `MAJOR BUT FIXABLE` attack has a bounded fix
- [ ] Any fix that changes theory is routed back through theory-change control
- [ ] For SPNE/sequential claims, no material off-path continuation remains `UNRESOLVED` or `NUMERICAL_FAILURE`
- [ ] Solver failures have not been silently filtered from deviation searches
- [ ] Minor comments are not used to obscure fatal issues
