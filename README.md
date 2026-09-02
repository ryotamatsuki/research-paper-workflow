# research-paper-workflow

A reusable, reproducible workflow for developing research papers from initial motivation to submission freeze.

The v1 canonical pipeline is designed primarily for **theory-oriented economics research**, especially projects that require rigorous literature mapping, mathematical verification, novelty kill tests, staged model selection, welfare analysis, referee simulation, reproducibility, and journal positioning. Stages 0–3 can also help identify an empirical or mixed route, but v1 does not yet provide a complete empirical post-Stage-3 workflow and non-theory projects should not be force-fit through the Stage 4 theory gate.

## Governing principle

> Do not preserve an idea because effort has already been invested in it. Kill weak mechanisms early. Retain only results that survive mathematics, prior art, institutional scrutiny, robustness checks, and referee-style attacks.

The workflow is intentionally stage-gated. A project is not assumed to deserve a paper. Every stage records a canonical `GO`, `CONDITIONAL GO`, or `NO-GO`; routing/status labels are secondary, and later stages may invalidate earlier optimism.

## Canonical documents

- [`THEORY_PAPER_RESEARCH_PIPELINE.md`](THEORY_PAPER_RESEARCH_PIPELINE.md): canonical Stage 0–15 theory workflow, including Stage 7.5.
- [`GOVERNANCE.md`](GOVERNANCE.md): repository governance, evidence/provenance rules, verdict/rollback policy, verification rules, release/change control, and canonical hierarchy.

The hierarchy is `GOVERNANCE.md` → canonical pipeline → stage templates → checklists → examples. Release/audit documents under `docs/` record version/readiness state but do not override this hierarchy.

## Stable release and v1.1 refinement

`v1.0` is the first stable historical release and remains immutable at its published tag.

A 2026-09-02 refinement now under review strengthens the distinction between **component overlap** and **whole-game absorption** for strategic/game-theoretic projects and explicitly recognizes economically substantive **generalization/unification** as a possible contribution route.

The refined standard requires:

- whole-game comparison of players, objectives, strategy sets, timing, allocation, and strategic feedbacks before declaring absorption;
- no novelty claim based only on “nobody combined these ingredients”;
- nested-benchmark recovery for generalization/unification claims;
- at least one full-model strategic or welfare result unavailable in the nested benchmarks alone.

See [`docs/NOVELTY_GATE_CORRECTION_2026-09-02.md`](docs/NOVELTY_GATE_CORRECTION_2026-09-02.md).

Under the revised [`VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md), this is a **v1.1 minor-version candidate** because Stage structure, canonical verdict semantics, and routing remain unchanged. A fresh integration/readiness audit is required before the `v1.1` tag and GitHub Release are created.

## v1 integration audit

PR #4 audited the original complete workflow before the first stable release:

- [`WORKFLOW_V1_INTEGRATION_AUDIT.md`](docs/WORKFLOW_V1_INTEGRATION_AUDIT.md)
- [`WORKFLOW_V1_READINESS_CHECKLIST.md`](docs/WORKFLOW_V1_READINESS_CHECKLIST.md)
- [`WORKFLOW_V1_CHANGELOG.md`](docs/WORKFLOW_V1_CHANGELOG.md)

Those files remain historical records of the repository state they reviewed. The 2026-09-02 novelty-gate refinement requires a fresh audit for v1.1 rather than rewriting the v1.0 history.

## Versioning

The current versioning rule is:

- **PATCH (`v1.0.1`)** — typo, link, metadata, and non-substantive clarification fixes;
- **MINOR (`v1.1`)** — criteria/check/verification additions or refinements that preserve Stage structure, canonical verdict semantics, and routing;
- **MAJOR (`v2.0`)** — Stage addition/removal/merger, verdict-semantic changes, routing changes, or incompatible workflow-architecture changes.

See [`docs/VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md) for the full compatibility test.

## Reusable templates

Executable prompt/report templates live under [`templates/`](templates/):

- Stage 0: Idea / Motivation Intake
- Stage 1: Source & Mathematical Audit
- Stage 2: Literature Frontier / Novelty Kill Gate
- Stage 3: Candidate Mechanism Search
- Stage 4: Minimal Model Gate
- Stage 5: Mechanism Hardening
- Stage 6: Novelty Re-Kill
- Stage 7: Welfare / Generality / Institutional Validation
- Stage 7.5: Full-Theory Freeze Decision
- Stage 8: Canonical Theory Freeze
- Stage 9: Repository / Reproducibility Setup
- Stage 10: Section-by-Section Paper Construction
- Stage 11: Robustness / Referee Attack Gate
- Stage 12: Journal Positioning
- Stage 13: Full-Paper Integration
- Stage 14: Submission QA
- Stage 15: Submission Freeze

Each template is designed to be instantiated with project placeholders such as `[RESEARCH_TOPIC]`, `[CORE_RESEARCH_QUESTION]`, `[TARGET_JOURNAL]`, `[CANONICAL_MODEL]`, `[CLOSEST_PAPERS]`, `[KNOWN_BLOCKERS]`, `[ALLOWED_CHANGES]`, and `[PROHIBITED_CHANGES]`.

## Verification checklists

Reusable checklists live under [`checklists/`](checklists/):

- [`LITERATURE_AUDIT_CHECKLIST.md`](checklists/LITERATURE_AUDIT_CHECKLIST.md)
- [`NOVELTY_KILL_CHECKLIST.md`](checklists/NOVELTY_KILL_CHECKLIST.md)
- [`SYMBOLIC_VERIFICATION_CHECKLIST.md`](checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md)
- [`NUMERICAL_VERIFICATION_CHECKLIST.md`](checklists/NUMERICAL_VERIFICATION_CHECKLIST.md)
- [`REFEREE_ATTACK_CHECKLIST.md`](checklists/REFEREE_ATTACK_CHECKLIST.md)
- [`SUBMISSION_CHECKLIST.md`](checklists/SUBMISSION_CHECKLIST.md)

Verification is method-dependent. A non-applicable check may be skipped only with a recorded reason; it cannot be used to bypass a substantive project gate.

## Worked examples

Worked research-decision trails live under [`examples/`](examples/). They are examples, not canonical rules, and preserve rejected branches as well as surviving ideas.

- [`retail-service-infrastructure`](examples/retail-service-infrastructure/) — a worked case showing how a legacy retail-channel question was repeatedly killed and reformulated through service spillovers, contract design, installed-base dynamics, and relationship-specific service capability. Current documented status: `CONDITIONAL GO`, before canonical Stage 7.5.

## Recommended workflow

1. Start at Stage 0 unless a prior project has already produced a verified input for a later stage.
2. Fill only the placeholders relevant to the project; mark unknown items `UNRESOLVED` rather than inventing them.
3. Run the stage as an executable research prompt and preserve the required report output.
4. Record the canonical stage verdict, route/status, rejected branches, blockers, and next-stage contract.
5. If a minimal theory model has exactly one diagnosed repairable deficiency, use Stage 5; a Stage 4 `NO-GO` does not itself authorize hardening.
6. Re-kill actual novelty after results are known in Stage 6, updating the Stage 2 literature ledger rather than blindly starting over.
7. For strategic/game-theoretic work, distinguish component overlap from whole-game absorption and use nested benchmarks when the contribution is a generalization/unification.
8. If a later stage invalidates an earlier result, return to the earliest affected stage and treat dependent downstream outputs as stale.
9. Do not initialize a full-paper production repository until Stage 7.5 approves full-paper investment and Stage 8 freezes the theory.
10. Preserve rejected branches and negative results as part of the research provenance.

## Recommended reuse mode

Use this repository as the **stable workflow reference**, not as the production LaTeX repository for every paper.

For a research project:

1. consult the canonical documents here;
2. use/copy the relevant Stage template as needed;
3. preserve the project's Stage reports, decision log, sources, calculations, and verification artifacts in the project's own research repository;
4. create the production paper repository at Stage 9 after Stage 7.5 approval and Stage 8 theory freeze.

The worked example is a reference decision trail and should not be copied as a model or project state.

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

This repository is a research-development and research-termination system, not a prompt collection and not a production-paper repository scaffold. Its main value is to make weak, derivative, ad hoc, or mathematically fragile research branches fail early and visibly before full-paper writing begins.

## License

Except where otherwise noted, the contents of this repository are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may share and adapt the material for any purpose, including commercial use, provided that you give appropriate credit, link to the license, and indicate if changes were made. See [`LICENSE`](LICENSE) for details.

Suggested attribution: **Ryota Matsuki, `research-paper-workflow`**.

## Status

Stable release: **`v1.0`**.

Current development state: **`v1.1 candidate — novelty-gate refinement pending fresh integration/readiness audit`**.

Planned release route: `PR #6 merge → fresh integration/readiness audit → audit PR merge → v1.1 tag / GitHub Release`.
