# Equilibrium Continuation Safety Correction — 2026-09-05

Status: v1.2-candidate canonical correction

## Trigger

A hostile pre-submission audit of a sequential spatial-competition paper discovered that the production verification repeatedly certified a regular interior price branch while failing to solve economically relevant off-path price continuations after large location deviations.

The specific failure mode was structural:

1. a local/regular demand and price formula was analytically correct on its maintained branch;
2. an upstream whole-domain deviation search changed locations;
3. when the downstream regular price branch failed its interiority conditions, the payoff routine returned `None`;
4. the deviation search skipped those `None` outcomes;
5. repeated robustness/referee gates reused the same continuation engine and therefore inherited the same blind spot;
6. an independent direct consumer-choice calculation later produced a profitable price deviation at one of the omitted off-path histories.

The lesson is general and is not specific to spatial competition.

## Canonical correction

The v1.2-candidate workflow now requires sequential/game-theoretic projects to distinguish:

- local/regular candidate characterization;
- on-path equilibrium verification;
- off-path continuation completeness;
- full-strategy Nash/SPNE certification.

Solver failure is fail-closed. `None`, NaN, invalid active set, branch violation, exception, and nonconvergence are `UNRESOLVED` unless a separate argument establishes economic infeasibility or equilibrium nonexistence.

Material unresolved continuations block Stage 4 `GO`, Stage 8 theory freeze, and later SPNE/submission-readiness claims.

## New checklist

`checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` requires:

- explicit complete strategy and consumer/agent choice sets;
- downstream re-solution after material upstream deviations;
- active-set/corner/kink/order/participation handling;
- explicit pure-equilibrium nonexistence/multiplicity treatment;
- solver outcome taxonomy;
- independent direct-payoff/allocation reconstruction;
- adversarial histories designed to exit the maintained regular branch;
- permanent regression tests for discovered counterexamples.

## Stage integration

### Stage 4

The minimal-model gate now requires continuation completeness for sequential SPNE claims and prohibits using solver failure as an implicit deviation filter.

### Stage 8

Theory freeze is blocked if material off-path continuations remain unresolved. The freeze record must include continuation classes, failure counts, multiplicity/nonexistence, and selection assumptions where relevant.

### Stage 11

Hostile referee review must independently reconstruct at least one material payoff/allocation from primitives when feasible and deliberately attack the regular branch with a finite off-path deviation. Merely rerunning the production solver or reproducing headline numbers is not independent equilibrium validation.

### Numerical and referee checklists

Both now require fail-closed solver semantics and explicit off-path/global-deviation attacks.

## Version impact

This is classified as a v1-series MINOR change under `docs/VERSIONING_POLICY.md`:

- no Stage is added, removed, merged, or renumbered;
- `GO / CONDITIONAL GO / NO-GO` semantics are unchanged;
- normal routing is unchanged;
- rollback/freeze architecture is unchanged;
- verification criteria inside existing Stages are materially strengthened.

Because the change can cause previously completed projects to merit re-audit, active sequential/game-theoretic projects should be screened against the new checklist before submission. This backward-looking re-audit implication does not make the version change major under the existing policy.

## Non-goals

This correction does not require every theory paper to solve every conceivable equilibrium refinement. It requires the verification scope to match the equilibrium concept and strategy/history domain actually claimed.

A model may deliberately restrict choice sets, strategies, information, or admissible histories, but those restrictions must be explicit, economically defended, and consistently implemented. They cannot be introduced implicitly by a solver's validity domain.
