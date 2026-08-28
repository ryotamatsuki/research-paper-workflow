# Symbolic Verification Checklist

Use for analytical models when symbolic computation is applicable. Software assists verification; it does not replace economic proof.

## Symbol setup

- [ ] Symbols and domains declared
- [ ] Positivity/nonnegativity assumptions recorded
- [ ] Parameter restrictions separated from assumptions introduced later
- [ ] Composite notation defined and reversible

## Primitive consistency

- [ ] Utility/technology/profit functions entered exactly
- [ ] Direct demand derived from utility where applicable
- [ ] Inverse/direct demand consistency verified
- [ ] Costs and transfers entered with correct signs
- [ ] Timing-specific objective functions checked

## Equilibrium derivation

- [ ] FOCs derived symbolically
- [ ] Best responses solved
- [ ] Candidate equilibrium solved
- [ ] Candidate substituted back into FOCs
- [ ] Identity checks simplify exactly to zero
- [ ] Denominators/factor conditions recorded

Example diagnostic:

```python
sp.simplify(lhs - rhs) == 0
```

## Second-order / existence checks

- [ ] Own second derivatives checked
- [ ] Hessian computed where multidimensional
- [ ] Determinant / principal minors checked
- [ ] Concavity/convexity region derived
- [ ] Existence conditions stated
- [ ] Uniqueness conditions stated

## Constraints and corners

- [ ] Quantity/service/effort nonnegativity checked
- [ ] Price/wholesale constraints checked when economically required
- [ ] Participation constraints derived
- [ ] Individual-rationality constraints derived
- [ ] KKT conditions used for binding constraints
- [ ] Boundary/corner regimes solved when they can be optimal

## Equilibrium identities

- [ ] Profits recomputed from primitive definitions
- [ ] Consumer surplus derived consistently from utility
- [ ] Welfare computed independently
- [ ] `CS + profits` identity checked where applicable
- [ ] Transfers cancel correctly in welfare
- [ ] Threshold equations verified

## Comparative statics

- [ ] Key derivatives computed symbolically
- [ ] Signs proved under stated restrictions where possible
- [ ] Ambiguous signs reduced to exact threshold conditions
- [ ] Mixed partials checked only when economically interpretable
- [ ] Global claims stress-tested for counterexamples

## Limiting cases

- [ ] Zero-effect parameter limit
- [ ] Symmetry/independence limit
- [ ] Near-boundary substitutability/competition limit
- [ ] High-cost / low-cost limit
- [ ] Fixed-cost zero limit where relevant
- [ ] Model nests known benchmark correctly

## Reproducibility

- [ ] Script/notebook saved
- [ ] Exact software/version documented when material
- [ ] Simplification/factorization steps reproducible
- [ ] Reported closed forms match code output after human simplification
- [ ] No numerical approximation presented as exact proof

## Verification status

For every main result record:

- Proposition/result:
- Symbolic identity verified?:
- SOC/feasibility verified?:
- Parameter region:
- Counterexample search required?:
- Proof status: `PROVED / CONDITIONAL / CONJECTURE / REJECTED`