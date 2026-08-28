# Numerical Verification Checklist

Numerical work is normally diagnostic and should follow symbolic/analytic work unless the research design is explicitly computational.

## Preconditions

- [ ] Analytical model and parameter restrictions documented
- [ ] Symbolic derivation completed where feasible
- [ ] Feasible parameter region defined
- [ ] Numerical purpose stated: benchmark / counterexample search / region mapping / illustration

## Benchmark checks

- [ ] Normalization stated explicitly
- [ ] At least one economically interpretable benchmark
- [ ] Benchmark satisfies all SOC/feasibility/participation conditions
- [ ] Analytic and numerical equilibrium values agree
- [ ] Profit/CS/welfare identities agree numerically

## Parameter coverage

- [ ] Multiple values for each key parameter
- [ ] Low / medium / high cases
- [ ] Boundary-near cases where numerically stable
- [ ] Relevant interaction parameters varied jointly
- [ ] Fixed costs / participation thresholds sampled on both sides

## Random / grid audit

- [ ] Sampling distribution/range documented
- [ ] Random seed fixed and recorded
- [ ] Infeasible draws filtered using explicit conditions
- [ ] Number of raw and feasible draws reported
- [ ] Counterexamples to proposed global claims actively searched
- [ ] Sign reversals recorded rather than averaged away
- [ ] Mode/organizational regions checked for positive measure
- [ ] Knife-edge results identified

## Numerical stability

- [ ] Denominators and near-singular cases monitored
- [ ] Root selection verified economically
- [ ] Multiple starting values used if numerical optimization is nonconvex
- [ ] Solver convergence/failure rates reported
- [ ] Floating-point tolerance stated where material
- [ ] Results cross-checked with alternative formulation/solver when high stakes

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

## Final numerical audit record

- Purpose:
- Parameter ranges:
- Seed:
- Raw draws:
- Feasible draws:
- Counterexamples found?:
- Positive-measure regions found?:
- Analytic consistency result:
- Remaining numerical concerns: