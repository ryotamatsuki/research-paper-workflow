# research-paper-workflow

A reusable, reproducible workflow for developing theory-oriented economics research from initial motivation to submission freeze.

The canonical workflow is designed for projects requiring rigorous literature mapping, mathematical verification, novelty kill tests, model selection, welfare analysis, independent theorem certification, referee simulation, reproducibility, exposition architecture, and journal positioning.

## Governing principle

> Do not preserve an idea because effort has already been invested. Kill weak mechanisms early, and do not freeze a theorem until both its mathematical correctness and its claimed scope survive independent adversarial attack.

Every stage records `GO`, `CONDITIONAL GO`, or `NO-GO`. A later stage may invalidate an earlier `GO`.

## Canonical documents

- [`GOVERNANCE.md`](GOVERNANCE.md) — repository governance, evidence standards, routing, rollback, certification independence, and freeze policy.
- [`THEORY_PAPER_RESEARCH_PIPELINE.md`](THEORY_PAPER_RESEARCH_PIPELINE.md) — canonical Stage 0–15 theory workflow, including Stage 4A, Stage 7.5, and Stage 7.5A.

Canonical hierarchy:

`GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → stage templates → checklists → examples.

## v2.0 architecture: mathematical adversarial certification before theory freeze

v2.0 is a major workflow architecture change because it adds mandatory stages and changes routing.

The core research path is now:

`Stage 4 Minimal Model`  
→ `Stage 4A Independent Mathematical Adversarial Certification`  
→ `Stage 6 Novelty Re-Kill`  
→ `Stage 7 Welfare / Generality / Institutional Validation`  
→ `Stage 7.5 Full-Theory Freeze Decision`  
→ `Stage 7.5A Generality / Quantifier Red-Team`  
→ `Stage 8 Canonical Theory Freeze`.

A Stage-4 `GO` can no longer route directly to Stage 6. A Stage-7.5 `GO` can no longer route directly to Stage 8.

### Why the new gates exist

Two recurring mathematical failure classes motivate v2.0:

1. **Global-equilibrium failure** — an interior/regular candidate satisfies FOCs, SOCs, Hessians, symbolic checks, and even production regression tests, but a boundary, corner, active-set, zero-output, regime-switch, or off-path deviation is profitable.
2. **Theorem-scope failure** — a baseline or restricted theorem is correct, but the manuscript extends it to a broader function class, strict comparative static, generic concavity/uniqueness claim, or planner benchmark label that the proof does not support.

These are different from ordinary algebra errors. Re-running the same derivation or solver is often insufficient because it inherits the same branch assumptions.

### Three-layer mathematical defense

v2.0 therefore requires:

1. **Construction and verification — Stage 4**  
   Solve the model, perform symbolic/numerical checks, enumerate relevant regimes, search for counterexamples, and create preliminary theorem records.

2. **Independent adversarial certification — Stage 4A and Stage 7.5A**  
   Use a logically independent path where feasible: a different model, clean-room derivation, separately written evaluator/solver, or equivalent approach that does not simply call the production solver.

3. **Late manuscript hostile audit — Stage 11**  
   Repeat high-stakes attacks after the full paper is built. Any flaw that Stage 4A/7/7.5A should have caught is recorded as a `CERTIFICATION REGRESSION` and routed back to the earliest invalidated stage.

## Stage 4A — Independent Mathematical Adversarial Certification

Template: [`templates/STAGE_04A_MATH_RED_TEAM.md`](templates/STAGE_04A_MATH_RED_TEAM.md)

Stage 4A independently attacks:

- global best responses and finite deviations;
- **candidate-deviation validity and alternative-equilibrium/multiplicity as separate questions**;
- payoff-indifferent, zero-demand, zero-output, and zero-profit actions that may alter other players' best responses;
- equilibrium-selection/refinement provenance and symmetry;
- corners, boundaries, active-set changes, regime switches, ordering changes, entry/exit, and zero-output states;
- off-path continuations and solver-failure semantics;
- local/interior claims that may have been promoted to global equilibrium;
- independent reconstruction of high-stakes payoff/allocation objects;
- welfare robustness across the relevant equilibrium set;
- welfare benchmark definitions;
- counterexample search and permanent regression tests;
- evidence-bearing PASS: `claim -> attack -> artifact -> surviving limitation`.

Every headline theorem receives a certificate. Material `NOT TESTED` fields block `GO`.

## Stage 7.5A — Generality / Quantifier Red-Team

Template: [`templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`](templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md)

Stage 7.5A attacks:

- `for all` / `exists` / `unique` / `generic` / `local` / `global` scope;
- equilibrium-set quantifiers such as `all equilibria`, `selected equilibrium`, and refinement-defined subsets;
- existence being written as uniqueness or complete characterization;
- selection-dependent welfare being written as selection-free;
- baseline functional-form dependence;
- claims over broad classes such as `C^2`, convex, concave, monotone, supermodular, or single-crossing functions;
- strict comparative statics whose sign is not implied by the stated restrictions;
- curvature/uniqueness generalization beyond what derivatives establish;
- numerical robustness relabeled as proof;
- planner labels such as `first best` when the choice set is actually constrained;
- abstract/introduction wording that exceeds the proved theorem.

A narrow exact theorem can pass. The gate penalizes overclaiming, not specialization.

## Theorem certification checklist

Use [`checklists/THEOREM_CERTIFICATION_CHECKLIST.md`](checklists/THEOREM_CERTIFICATION_CHECKLIST.md) for every headline equilibrium, theorem, proposition, welfare result, and broad robustness claim.

Each certificate records at least:

- exact claim and quantifiers;
- parameter/strategy/function domains;
- assumptions actually used;
- local/branch/global status;
- candidate-deviation audit;
- alternative-equilibrium / multiplicity audit when required by claim scope;
- indifference / zero-payoff trigger audit;
- selection/refinement provenance and symmetry;
- FOC/KKT/SOC/globality evidence;
- boundary/corner/regime audit;
- independent reconstruction status;
- counterexample search;
- welfare-selection robustness;
- functional-form/generality status;
- benchmark-definition status;
- evidence maturity and artifact paths;
- maximum defensible manuscript wording;
- `PASS`, `CONDITIONAL`, or `FAIL`.

## Post-v2.1 equilibrium-multiplicity / evidence-bearing refinement

The 2026-09-09 refinement does **not** add a new Stage. It makes existing mathematical-certification principles operational by requiring distinct evidence for distinct claims.

The central rule is:

> Verifying that a proposed profile has no profitable deviation is not evidence that no other equilibrium exists.

Payoff indifference and zero-demand/zero-profit states now trigger explicit alternative-equilibrium attacks; equilibrium refinements must be provenance-tracked and applied symmetrically; welfare claims must state whether they hold for one selected equilibrium or all relevant equilibria; and material PASS states must identify the attack and supporting artifact.

Paper-specific routes such as correction-paper `C0–C6` protocols inherit the same obligations through [`checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`](checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md).

Regression rationale: [`docs/EQUILIBRIUM_MULTIPLICITY_CERTIFICATION_REFINEMENT_2026-09-09.md`](docs/EQUILIBRIUM_MULTIPLICITY_CERTIFICATION_REFINEMENT_2026-09-09.md).

Under [`docs/VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md), this is a **minor-version class** backward-compatible refinement because Stage identities, verdict semantics, and routing are unchanged. The published `v2.1` tag remains immutable until a later release is separately reviewed and published.

## Theory freeze requirements

Stage 8 requires both:

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` from Stage 4A; and
- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS` from Stage 7.5A.

The freeze retains theorem certificates, equilibrium-set/multiplicity status, selection/refinement conditions, welfare-selection robustness, claim-scope ledger, benchmark-definition register, evidence ledger, and counterexample/regression-test register.

Production repositories should retain these under `theorem_certificates/` or an equivalent auditable directory.

## Reusable templates

Templates live under [`templates/`](templates/):

- Stage 0 — Idea / Motivation Intake
- Stage 1 — Source & Mathematical Audit
- Stage 2 — Literature Frontier / Novelty Kill Gate
- Stage 3 — Candidate Mechanism Search
- Stage 4 — Minimal Model Gate
- **Stage 4A — Independent Mathematical Adversarial Certification Gate**
- Stage 5 — Mechanism Hardening
- Stage 6 — Novelty Re-Kill
- Stage 7 — Welfare / Generality / Institutional Validation
- Stage 7.5 — Full-Theory Freeze Decision
- **Stage 7.5A — Generality / Quantifier Red-Team Gate**
- Stage 8 — Canonical Theory Freeze
- Stage 9 — Repository / Reproducibility Setup
- Stage 10 — Section-by-Section Paper Construction
- Stage 11 — Robustness / Referee Attack Gate
- Stage 12 — Journal Positioning
- Stage 13 — Full-Paper Integration
- Stage 14 — Submission QA
- Stage 15 — Submission Freeze

## Verification checklists

Reusable checklists live under [`checklists/`](checklists/), including:

- [`LITERATURE_AUDIT_CHECKLIST.md`](checklists/LITERATURE_AUDIT_CHECKLIST.md)
- [`NOVELTY_KILL_CHECKLIST.md`](checklists/NOVELTY_KILL_CHECKLIST.md)
- [`SYMBOLIC_VERIFICATION_CHECKLIST.md`](checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md)
- [`NUMERICAL_VERIFICATION_CHECKLIST.md`](checklists/NUMERICAL_VERIFICATION_CHECKLIST.md)
- [`EQUILIBRIUM_CONTINUATION_CHECKLIST.md`](checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md)
- **[`THEOREM_CERTIFICATION_CHECKLIST.md`](checklists/THEOREM_CERTIFICATION_CHECKLIST.md)**
- **[`PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`](checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md)**
- [`FIGURE_TABLE_CHECKLIST.md`](checklists/FIGURE_TABLE_CHECKLIST.md)
- [`REFEREE_ATTACK_CHECKLIST.md`](checklists/REFEREE_ATTACK_CHECKLIST.md)
- **[`JOURNAL_REQUIREMENTS_CHECKLIST.md`](checklists/JOURNAL_REQUIREMENTS_CHECKLIST.md)**
- [`SUBMISSION_CHECKLIST.md`](checklists/SUBMISSION_CHECKLIST.md)

A check may be `NOT APPLICABLE` only with a recorded reason. Material `NOT TESTED` is not a passing state.

## v2.1 release: fail-closed live journal compliance

v2.1 makes submission compliance evidence-bearing. Stage 12 creates a Journal Requirements Ledger; Stage 13 carries verified requirements into the package; Stage 14 re-checks current official journal rules and fails closed on material unknowns/conflicts; Stage 15 reconciles the authenticated portal and generated submission PDF where applicable.

A successful upload is not proof of technical compliance. If a material rule cannot be resolved from current journal/publisher/portal evidence, clarification from the editorial office or submission support is required before full submission QA PASS.

For actual submissions, the most specific current authority controls: direct editorial-office instruction → explicit authenticated-portal requirement → journal-specific official guidance → publisher-wide official guidance → secondary/internal/memory evidence.

## Historical releases

- `v1.0` — first stable release.
- `v1.1` — strengthened component-overlap vs whole-game absorption and generalization/unification treatment.
- `v1.2` — added equilibrium-continuation safety for sequential/game-theoretic models: off-path continuation completeness, fail-closed solver semantics, independent direct-payoff reconstruction, and permanent counterexample regression tests.
- `v1.3` — added result-to-exposition and figure/table architecture lifecycle across Stages 7/10/13/14.
- `v2.0` — mathematical-adversarial-certification architecture merged/audited on 2026-09-06; not separately tagged as a stable GitHub Release.
- `v2.1` — first stable tagged v2 release; includes the v2.0 architecture plus fail-closed live journal-compliance and portal-preflight controls.

Under [`docs/VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md), v2.0 is MAJOR because it adds Stage 4A and Stage 7.5A and changes canonical routing.

## Recommended workflow

1. Start at Stage 0 unless verified prior work justifies later entry.
2. Preserve unknowns as `UNRESOLVED`; do not invent missing facts.
3. Run each stage as a research gate and preserve its report, verdict, rejected branches, blockers, and next-stage contract.
4. If Stage 4 gives `GO`, run Stage 4A before any Stage-6 novelty re-kill. Separate candidate-deviation verification from alternative-equilibrium search whenever the claim requires characterization, uniqueness, or selection-free conclusions.
5. Trigger indifference/multiplicity attacks when zero-demand, zero-output, zero-profit, ties, or other payoff-equivalent actions occur.
6. If Stage 4/4A identifies exactly one repairable economic deficiency, Stage 5 may change only that one margin; then repeat Stage 4 and Stage 4A.
7. Re-kill actual novelty at Stage 6.
8. Validate welfare/generality/institutions at Stage 7, including welfare robustness to equilibrium selection.
9. Use Stage 7.5 to decide whether a full paper is justified, then run Stage 7.5A before theory freeze.
10. Freeze theory only after both independent certificates pass with evidence-linked artifacts.
11. At Stage 7 identify exposition vehicles; at Stage 10 implement figure/table architecture; at Stage 13 integrate it; at Stage 14 verify it.
12. At Stage 11 repeat hostile mathematical, equilibrium-set, welfare-selection, and theorem-scope attacks from a fresh perspective.
13. If a later stage invalidates earlier work, return to the earliest affected stage and mark downstream outputs stale.
14. Preserve rejected branches, additional equilibria, counterexamples, negative results, theorem-certificate failures, and certification regressions as research provenance.
15. When using a paper-specific route such as `C0–C6`, map each strong claim to the inherited canonical certification obligation and required evidence artifact.

## Repository structure

```text
research-paper-workflow/
├── README.md
├── THEORY_PAPER_RESEARCH_PIPELINE.md
├── GOVERNANCE.md
├── LICENSE
├── templates/
├── checklists/
├── docs/
└── examples/
```

## Intended use

Use this repository as the stable workflow reference, not as the production LaTeX repository for every paper. Project-specific Stage reports, decision logs, calculations, theorem certificates, equilibrium-set artifacts, counterexamples, and verification evidence should live in the project's own repository.

## License

Except where otherwise noted, contents are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [`LICENSE`](LICENSE).

Suggested attribution: **Ryota Matsuki, `research-paper-workflow`**.

## Status

Current stable published workflow: **v2.1**.

`main` may contain reviewed post-v2.1 backward-compatible refinements pending a later release. Stable tag/release: **`v2.1`**. Historical stable tags `v1.0`–`v1.3` remain immutable. The v2.0 architecture was merged and audited but not separately tagged; v2.1 is the first stable tagged release in the v2 line.
