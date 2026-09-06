# v2.0 Readiness Checklist

Use this checklist before merging/tagging v2.0.

## Canonical architecture

- [ ] `GOVERNANCE.md` identifies v2.0 and states independent certification principles.
- [ ] `THEORY_PAPER_RESEARCH_PIPELINE.md` identifies v2.0.
- [ ] Stage 4 `GO` routes to Stage 4A, not Stage 6.
- [ ] Stage 5 repair returns to Stage 4 then Stage 4A.
- [ ] Stage 4A `GO` routes to Stage 6.
- [ ] Stage 7.5 `GO` routes to Stage 7.5A, not Stage 8.
- [ ] Stage 7.5A `GO` is required for Stage 8.
- [ ] Stage 8 explicitly blocks freeze without both certification passes.
- [ ] Stage 11 remains a late independent audit rather than a substitute for pre-freeze certification.

## Global-equilibrium safety

- [ ] Stage 4 retains FOC/KKT/SOC/Hessian/feasibility checks.
- [ ] Stage 4 retains boundary/corner/regime/global-deviation checks.
- [ ] Stage 4 retains fail-closed solver semantics.
- [ ] Stage 4A independently attacks full strategy domains and finite deviations.
- [ ] Stage 4A independently attacks off-path continuations where applicable.
- [ ] Stage 4A requires independent reconstruction where feasible.
- [ ] Counterexamples are preserved as permanent regression tests.

## Theorem-scope safety

- [ ] `THEOREM_CERTIFICATION_CHECKLIST.md` exists.
- [ ] Exact quantifiers and domains are mandatory.
- [ ] Baseline/restricted/general-theorem classifications are explicit.
- [ ] Broad function-class claims require admissible counterexample search.
- [ ] Numerical robustness is distinguished from proof.
- [ ] Local/global, existence/uniqueness, weak/strict, sufficient/necessary distinctions are explicit.
- [ ] Stage 7 produces exact planner/benchmark definitions.
- [ ] Stage 7.5A audits planner choice sets before allowing `first best` language.
- [ ] Stage 8 freezes maximum defensible claim scope and prohibited stronger claims.

## Independence

- [ ] Governance states that re-running the same solver is reproduction, not independent certification.
- [ ] Stage 4A prefers a different model, clean-room derivation, separate evaluator/solver, or equivalent independent path.
- [ ] Stage 11 repeats at least one independent high-stakes mathematical attack.
- [ ] Certification regressions are explicitly recorded and rolled back.

## Reproducibility

- [ ] Stage 9 carries theorem certificates into production repositories.
- [ ] `theorem_certificates/` or equivalent is recommended.
- [ ] Counterexample regression tests are retained.
- [ ] Manuscript claims remain traceable to certificates and proof artifacts.

## Documentation/versioning

- [ ] README documents the v2.0 routing.
- [ ] README documents historical v1.0–v1.3 releases.
- [ ] Release notes explain why v2.0 is MAJOR.
- [ ] Existing v1.x project reproducibility is preserved.
- [ ] No existing stable tag is moved.

## Merge gate

Do not merge if any canonical file still permits either bypass:

- `Stage 4 GO → Stage 6` without Stage 4A; or
- `Stage 7.5 GO → Stage 8` without Stage 7.5A.

Do not merge if Stage 8 can freeze theory without both certificates.
