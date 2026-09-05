# Numerical Verification Checklist

Numerical work is normally diagnostic and should follow symbolic/analytic work unless the research design is explicitly computational.

## Preconditions

- [ ] Analytical model and parameter restrictions documented
- [ ] Symbolic derivation completed where feasible
- [ ] Feasible parameter region defined
- [ ] Numerical purpose stated: benchmark / counterexample search / region mapping / illustration / continuation audit
- [ ] Complete economic strategy/history domain distinguished from the domain on which a particular closed-form/regular branch is valid

## Benchmark checks

- [ ] Normalization stated explicitly
- [ ] At least one economically interpretable benchmark
- [ ] Benchmark satisfies all SOC/feasibility/participation conditions
- [ ] Analytic and numerical equilibrium values agree
- [ ] Profit/CS/welfare identities agree numerically
- [ ] At least one high-stakes payoff/allocation is independently reconstructed from primitives when feasible

## Parameter and strategy coverage

- [ ] Multiple values for each key parameter
- [ ] Low / medium / high cases
- [ ] Boundary-near cases where numerically stable
- [ ] Relevant interaction parameters varied jointly
- [ ] Fixed costs / participation thresholds sampled on both sides
- [ ] Finite/global unilateral deviations sampled, not only local perturbations
- [ ] Adversarial actions designed to trigger active-set, ordering, participation, market-coverage, or regime changes where relevant

## Random / grid audit

- [ ] Sampling distribution/range documented
- [ ] Random seed fixed and recorded
- [ ] Infeasible draws filtered only using primitive/model conditions, not because the preferred equilibrium branch failed
- [ ] Number of raw and economically infeasible draws reported separately
- [ ] Counterexamples to proposed global claims actively searched
- [ ] Sign reversals recorded rather than averaged away
- [ ] Mode/organizational regions checked for positive measure
- [ ] Knife-edge results identified

## Solver-failure semantics

Classify every solver call relevant to an equilibrium claim as one of:

- `SOLVED_EQUILIBRIUM`
- `SOLVED_NO_EQUILIBRIUM` when nonexistence is actually established
- `MULTIPLE_EQUILIBRIA`
- `UNRESOLVED`
- `NUMERICAL_FAILURE`

- [ ] `None`, NaN, exception, invalid active set, branch/interiority failure, or nonconvergence is never counted as an unprofitable deviation
- [ ] Failed/unresolved continuations are retained in the audit ledger
- [ ] Solver convergence/failure/unresolved counts are reported
- [ ] For sequential games, a material `UNRESOLVED`/`NUMERICAL_FAILURE` downstream continuation blocks certification of the upstream equilibrium
- [ ] If pure equilibrium may not exist, nonexistence is tested rather than assumed from solver failure
- [ ] Multiplicity and continuation-selection sensitivity are reported where relevant

## Numerical stability

- [ ] Denominators and near-singular cases monitored
- [ ] Root selection verified economically
- [ ] Multiple starting values used if numerical optimization is nonconvex
- [ ] Floating-point tolerance stated where material
- [ ] Results cross-checked with alternative formulation/solver when high stakes
- [ ] Regular/interior formulas are not extrapolated outside their verified validity region

## Comparative statics

- [ ] Finite differences use appropriate step sizes
- [ ] Finite-difference signs compared with analytic derivatives
- [ ] Threshold crossings checked directly
- [ ] No finite-difference pattern is presented as a theorem

## Figures and tables

- [ ] Generated from source code
- [ ] Axes/units/normalizations documented
- [ ] No selective range chosen to hide counterexamples
- [ ] Figure is used only when it adds information beyond a table/equation
- [ ] Underlying data can be regenerated

## Reporting discipline

- [ ] Numerical example labeled as example
- [ ] Parameter-grid evidence labeled as diagnostic/supportive
- [ ] Analytical proof and numerical evidence clearly separated
- [ ] Negative/counterexample results retained
- [ ] Any counterexample to an equilibrium/proposition is converted into a permanent regression test where practical
- [ ] Terms such as `global`, `whole-domain`, `whole-circle`, or `complete` are used only if the audit actually covers the economic domain, not merely the solver's regular branch

## Final numerical audit record

- Purpose:
- Parameter ranges:
- Strategy/history ranges:
- Seed:
- Raw draws:
- Economically infeasible draws:
- Solved equilibrium calls:
- Solved nonexistence calls:
- Multiple-equilibrium calls:
- Unresolved calls:
- Numerical failures:
- Counterexamples found?:
- Positive-measure regions found?:
- Independent payoff/allocation cross-check:
- Analytic consistency result:
- Remaining numerical concerns:
