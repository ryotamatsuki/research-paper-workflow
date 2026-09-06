# v2.0 Release Notes — Mathematical Adversarial Certification Architecture

## Status

Architecture version: `v2.0`

This is a MAJOR workflow change under `docs/VERSIONING_POLICY.md` because it adds mandatory stages and changes canonical routing before theory freeze.

## Problem addressed

v1.2/v1.3 already strengthened sequential-equilibrium continuation safety and exposition QA, but two failure classes could still survive too long:

1. an interior/regular-branch candidate could satisfy local algebra and production checks while failing a global boundary/corner/regime deviation; and
2. a correct baseline/restricted theorem could be overstated as a broader functional-form, strict comparative-static, generic curvature/uniqueness, or planner-benchmark result.

Both failures are especially vulnerable to correlated verification when the same derivation/model/solver that constructs the result also performs most of the subsequent checking.

## Architecture change

v2.0 adds:

### Stage 4A — Independent Mathematical Adversarial Certification Gate

Mandatory after Stage 4 `GO` and before Stage 6.

It independently attacks:

- full strategy domains and finite/global deviations;
- boundaries, corners, active sets, regime switches, ordering changes, zero-output and entry/exit states;
- sequential off-path continuations and fail-closed solver semantics;
- local/regular candidates promoted to global/SPNE claims;
- independent direct-payoff/allocation reconstruction;
- counterexample search and permanent regression tests;
- planner/benchmark definitions;
- theorem certificates.

### Stage 7.5A — Generality / Quantifier Red-Team Gate

Mandatory after Stage 7.5 `GO` and before Stage 8.

It independently attacks:

- theorem quantifiers and domains;
- baseline functional-form dependence;
- broad function-class claims;
- strict comparative statics and curvature/uniqueness statements;
- numerical robustness described as proof;
- existence/uniqueness, local/global, sufficient/necessary inflation;
- `first best` and other benchmark terminology;
- abstract/introduction/robustness wording beyond the proved theorem.

## New hard routing

Old:

`Stage 4 → Stage 6 → Stage 7 → Stage 7.5 → Stage 8`

v2.0:

`Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8`

A Stage-5 repair returns to Stage 4 and then Stage 4A.

## New checklist

`checklists/THEOREM_CERTIFICATION_CHECKLIST.md`

Each headline theorem records:

- exact claim and quantifiers;
- parameter/strategy/function domains;
- assumptions actually used;
- local/branch/global status;
- equilibrium/globality evidence;
- independent reconstruction;
- counterexample search;
- functional-form/generality classification;
- planner/benchmark definition;
- proof/evidence maturity;
- maximum defensible manuscript wording;
- certificate state.

Material `NOT TESTED` blocks certification.

## Stage 7 change

Welfare/generality validation now writes each planner objective and complete feasible choice set before benchmark labels are applied, and classifies each generality claim as baseline-only, restricted-class, sufficient-condition theorem, numerical robustness, conjectured generality, or general theorem. This creates explicit inputs for Stage 7.5A.

## Stage 8 change

Theory freeze now requires both:

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`; and
- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`.

The freeze retains theorem certificates, claim-scope ledger, benchmark-definition register, and counterexample/regression-test register.

## Stage 9 change

Production repositories should retain certification artifacts under `theorem_certificates/` or an equivalent auditable directory and preserve counterexamples as regression tests.

## Stage 11 change

Stage 11 remains a full-manuscript hostile audit. It must independently repeat at least one high-stakes globality/continuation attack and one theorem-scope/function-class attack when applicable.

A failure discovered at Stage 11 that Stage 4A/7.5A should have caught is labeled `CERTIFICATION REGRESSION`, preserved as workflow evidence, and routed to the earliest invalidated stage.

## Compatibility

Existing projects using v1.3 remain reproducible under their recorded workflow version.

Projects that adopt v2.0 and have not yet reached Stage 8 should run the new gates before theory freeze.

For already frozen or completed theory projects, migration is not automatically required for historical reproducibility. However, before a new submission based on a v1.x freeze, applying Stage 4A and Stage 7.5A is recommended when the paper contains high-stakes global/SPNE claims, broad functional-form generalizations, strict comparative statics, or sensitive planner-benchmark terminology.

## Canonical files changed

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `README.md`
- `templates/STAGE_04_MINIMAL_MODEL.md`
- `templates/STAGE_04A_MATH_RED_TEAM.md`
- `templates/STAGE_07_WELFARE_GENERALITY.md`
- `templates/STAGE_075_FREEZE_DECISION.md`
- `templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`
- `templates/STAGE_08_THEORY_FREEZE.md`
- `templates/STAGE_09_REPRODUCIBILITY_SETUP.md`
- `templates/STAGE_11_REFEREE_GATE.md`
- `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`
- `checklists/REFEREE_ATTACK_CHECKLIST.md`
- `docs/V2_0_READINESS_CHECKLIST.md`
