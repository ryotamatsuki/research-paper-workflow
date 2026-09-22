# Portability / Falsification Checklist

Use this checklist inside Stage 7.5A for every headline economic mechanism that is presented as more than a baseline/model-specific result.

The purpose is not to maximize journal prestige. The purpose is to determine the maximum defensible research strength of the existing theory before Stage 8 theory freeze.

## 1. Journal-neutrality

- [ ] No journal name, ranking, quartile, impact factor, or desired target is being used to decide whether a mechanism counts as portable.
- [ ] The portability test would be considered informative even if the eventual journal target changed.
- [ ] Stage 12, not Stage 7.5A, will decide which journals fit the certified result.

## 2. Headline mechanism invariant

For each headline claim:

- [ ] State the canonical claim.
- [ ] State the minimal economic mechanism/invariant that should survive if the result is genuinely portable.
- [ ] Distinguish the invariant from a particular closed-form expression or numerical sign.
- [ ] List the baseline assumptions most plausibly carrying the result.
- [ ] Record whether the manuscript currently presents the claim as baseline-specific, robust, generic, institutional, or broadly portable.

## 3. Pre-specification of diagnostic alternatives

Before solving the alternative:

- [ ] Select at least one economically meaningful alternative formulation whenever the claim is presented as more than model-specific.
- [ ] The alternative changes a plausibly result-driving feature rather than a cosmetic normalization.
- [ ] Examples considered where relevant: demand substitution, strategic variable, network microfoundation, cost technology, timing, information, heterogeneity, market size, coalition/blocking rule, institutional menu.
- [ ] State why the alternative is economically credible.
- [ ] Freeze its primitives and equilibrium concept before seeing the result.
- [ ] State the exact ex ante survival/failure criterion.
- [ ] Record the alternative in a dated artifact or committed file before the result is computed.

A test chosen after seeing the desired answer does not count as portability evidence.

## 4. Independent re-solution

- [ ] Re-solve the affected equilibrium or continuation problem from the alternative primitives.
- [ ] Do not insert changed primitives into baseline formulas outside their derivation domain.
- [ ] Recheck existence, feasibility, relevant corners/boundaries, and equilibrium selection under the alternative.
- [ ] Use symbolic/analytic derivation where possible.
- [ ] Use numerical evidence only as supporting evidence unless the claim itself is numerical.
- [ ] Preserve code, algebra, or proof artifacts sufficient to reproduce the portability result.
- [ ] Where feasible, use an evaluator/derivation path independent of the canonical production code.

## 5. Failure analysis

If the headline effect fails:

- [ ] Identify whether the failure comes from a sign reversal, disappearance of the initial condition, change in equilibrium selection, loss of existence/uniqueness, altered welfare accounting, or institutional sensitivity.
- [ ] Identify the smallest assumption or payoff component that explains the failure where possible.
- [ ] Attempt an abstract sufficient-condition formulation without redesigning the failed alternative.
- [ ] Distinguish “the mechanism fails” from “the chosen alternative is outside the claimed class.”
- [ ] Preserve exact counterexamples and negative results.
- [ ] Reflect the failure in the claim-scope ledger and manuscript wording.

## 6. Optional second orthogonal attack

A second attack is required when the first surviving test is too close to the baseline to discriminate real portability, or when a second dimension is necessary to support a broad claim.

- [ ] The second test changes a genuinely different margin from the first.
- [ ] It is pre-specified before solving.
- [ ] It is not selected because the first test failed and a more favorable alternative was sought.
- [ ] Its result is preserved even if unfavorable.

## 7. Stop rule against research creep

Normally classify the claim as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` and stop rescue attempts when all of the following hold:

- [ ] two economically meaningful, pre-specified, non-cosmetic portability attacks overturn the same claimed cross-model mechanism;
- [ ] the failures are not explained by a coding/derivation defect;
- [ ] no defensible abstract sufficient-condition theorem survives;
- [ ] further alternatives would mainly be chosen to recover the preferred sign.

Further development after the stop rule requires a distinct research question or theoretically motivated architecture change and must roll back to the earliest affected research stage. It is not an in-gate rescue.

## 8. Required classification

Assign exactly one classification to each headline claim:

### `PORTABLE`

Use only when the mechanism survives meaningful alternative formulations and the surviving statement is not tied to a single baseline microfoundation.

### `CONDITIONALLY PORTABLE`

Use when a clear abstract condition or identified class supports the mechanism, but portability requires substantive restrictions.

### `MODEL-SPECIFIC`

Use when the result is correct and potentially important in the canonical microfoundation but fails credible cross-model tests or lacks evidence beyond the baseline.

### `INSTITUTION-SPECIFIC`

Use when the result materially depends on a coalition rule, refinement, timing protocol, institutional menu, symmetry, or related institutional structure.

### `FALSIFIED`

Use when the headline statement itself is not supported even under its claimed domain and must be withdrawn or repaired.

## 9. Contribution Robustness Certificate

For each headline claim record:

- claim identifier;
- canonical theorem/proposition;
- mechanism invariant;
- baseline assumptions;
- alternative formulation(s);
- ex ante success/failure criterion;
- equilibrium/proof/code artifact;
- result;
- failure boundary or sufficient conditions;
- final classification;
- maximum defensible wording;
- prohibited stronger wording;
- stop-rule status;
- whether rollback for substantive strengthening is authorized.

## 10. Stage 12 handoff

Before Stage 8/12 downstream use:

- [ ] The Contribution Robustness Certificate is committed and auditable.
- [ ] Manuscript claims do not exceed the certificate.
- [ ] Negative results/failure boundaries are preserved where material.
- [ ] Stage 12 is instructed to match journals to this certified strength rather than to demand new theory to preserve a preferred target.
- [ ] A journal requiring materially stronger generality will be downgraded/rejected as a candidate unless an independently authorized research rollback occurs.

## Passing condition

This checklist passes when every headline claim has a defensible portability classification, all material alternatives were pre-specified and re-solved, unfavorable results are preserved, the stop rule has been applied where triggered, and the Contribution Robustness Certificate is complete.

A narrow `MODEL-SPECIFIC` theorem may pass. The checklist is designed to measure research strength accurately, not to force generality that the economics does not support.
