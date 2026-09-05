# research-paper-workflow v1.2

v1.2 is a backward-compatible safety refinement for sequential/game-theoretic research.

## What changed

### Off-path continuation completeness

Sequential models must now verify downstream continuations needed to evaluate upstream deviations. An on-path or regular interior branch is not sufficient for an SPNE claim.

### Fail-closed solver semantics

`None`, NaN, invalid active set, branch failure, exception, or nonconvergence is classified as unresolved unless economic infeasibility or equilibrium nonexistence is separately established. Such outcomes cannot be counted as unprofitable deviations.

### Stronger equilibrium verification

The workflow now requires, where relevant:

- complete strategy and consumer/agent choice domains;
- downstream re-solution after material deviations;
- global/finite deviation checks in addition to FOC/SOC/interiority;
- corner, active-set, ordering, participation, multiplicity, and nonexistence treatment;
- independent direct-payoff/allocation reconstruction for high-stakes sequential claims when feasible;
- permanent regression tests for discovered equilibrium counterexamples.

### Stage integration

- Stage 4: continuation completeness is a GO requirement for SPNE claims.
- Stage 8: theory freeze is blocked by material unresolved continuations.
- Stage 11: hostile review must independently attack downstream continuation validity rather than merely rerun the production solver.
- Numerical Verification and Referee Attack checklists now use fail-closed semantics.
- New checklist: `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md`.

## What did not change

- Stage 0–15 architecture, including Stage 7.5
- `GO / CONDITIONAL GO / NO-GO` semantics
- normal Stage routing
- one-diagnosed-fix discipline
- rollback/stale-state architecture
- theory/submission freeze concept

## Migration note

Active sequential/game-theoretic projects that claim SPNE, global equilibrium, or whole-domain deviation validity should be re-audited against the new continuation checklist before submission. A previously green CI run or reproduction of on-path numbers does not substitute for this re-audit.

Historical `v1.0` and `v1.1` remain unchanged.
