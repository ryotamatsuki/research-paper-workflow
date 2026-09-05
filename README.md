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

## Stable release and current refinement

`v1.0` is the first stable historical release and remains immutable at its published tag.

The stable `v1.1` refinement strengthened the distinction between **component overlap** and **whole-game absorption** and recognized economically substantive **generalization/unification** as a contribution route.

The current `v1.2-candidate` refinement adds an **equilibrium-continuation safety gate** for sequential/game-theoretic projects after a production-paper audit exposed a failure mode in which a regular interior downstream formula was reused off path and solver `None` outcomes silently removed economically relevant deviations.

The v1.2-candidate standard requires:

- complete strategy/consumer-choice domains to be explicit;
- downstream subgames to be re-solved after material upstream deviations;
- FOC/SOC/interiority checks to be distinguished from full-strategy Nash verification;
- solver failures to fail closed as `UNRESOLVED` rather than count as unprofitable deviations;
- active sets, corners, ordering/participation changes, multiplicity, and possible pure-equilibrium nonexistence to be audited when relevant;
- at least one independent direct-payoff/allocation reconstruction for high-stakes sequential equilibrium claims when feasible;
- Stage 11 hostile review to include an implementation-independent continuation attack rather than only rerunning the production solver;
- equilibrium counterexamples to become permanent regression tests.

The new canonical checklist is [`checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md`](checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md).

Under [`docs/VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md), this is a **minor-version candidate** because it strengthens verification inside existing Stages without changing Stage numbering, verdict semantics, or routing. Stable published version remains `v1.1` until integration/readiness review and release are completed.

## Integration/readiness audits

The original v1 audit remains a historical record:

- [`WORKFLOW_V1_INTEGRATION_AUDIT.md`](docs/WORKFLOW_V1_INTEGRATION_AUDIT.md)
- [`WORKFLOW_V1_READINESS_CHECKLIST.md`](docs/WORKFLOW_V1_READINESS_CHECKLIST.md)
- [`WORKFLOW_V1_CHANGELOG.md`](docs/WORKFLOW_V1_CHANGELOG.md)

The v1.1 refinement passed a fresh integration/readiness audit:

- [`WORKFLOW_V1_1_INTEGRATION_AUDIT.md`](docs/WORKFLOW_V1_1_INTEGRATION_AUDIT.md)
- [`WORKFLOW_V1_1_READINESS_CHECKLIST.md`](docs/WORKFLOW_V1_1_READINESS_CHECKLIST.md)
- [`V1_1_RELEASE_MANIFEST.md`](docs/V1_1_RELEASE_MANIFEST.md)
- [`V1_1_RELEASE_NOTES.md`](docs/V1_1_RELEASE_NOTES.md)

## Versioning

The current versioning rule is:

- **PATCH** — typo, link, metadata, and non-substantive clarification fixes;
- **MINOR** — criteria/check/verification additions or refinements that preserve Stage structure, canonical verdict semantics, and routing;
- **MAJOR** — Stage addition/removal/merger, verdict-semantic changes, routing changes, or incompatible workflow-architecture changes.

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
- [`EQUILIBRIUM_CONTINUATION_CHECKLIST.md`](checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md)
- [`REFEREE_ATTACK_CHECKLIST.md`](checklists/REFEREE_ATTACK_CHECKLIST.md)
- [`SUBMISSION_CHECKLIST.md`](checklists/SUBMISSION_CHECKLIST.md)

Verification is method-dependent. A non-applicable check may be skipped only with a recorded reason; it cannot be used to bypass a substantive project gate.

## Recommended workflow

1. Start at Stage 0 unless a prior project has already produced a verified input for a later stage.
2. Fill only the placeholders relevant to the project; mark unknown items `UNRESOLVED` rather than inventing them.
3. Run the stage as an executable research prompt and preserve the required report output.
4. Record the canonical stage verdict, route/status, rejected branches, blockers, and next-stage contract.
5. If a minimal theory model has exactly one diagnosed repairable deficiency, use Stage 5; a Stage 4 `NO-GO` does not itself authorize hardening.
6. Re-kill actual novelty after results are known in Stage 6, updating the Stage 2 literature ledger rather than blindly starting over.
7. For strategic/game-theoretic work, distinguish component overlap from whole-game absorption and use nested benchmarks when the contribution is a generalization/unification.
8. For sequential games, apply the equilibrium-continuation checklist before Stage 4 `GO`, repeat the independent hostile continuation attack at Stage 11, and fail closed on unresolved solver outcomes.
9. If a later stage invalidates an earlier result, return to the earliest affected stage and treat dependent downstream outputs as stale.
10. Do not initialize a full-paper production repository until Stage 7.5 approves full-paper investment and Stage 8 freezes the theory.
11. Preserve rejected branches, counterexamples, and negative results as part of the research provenance.

## Recommended reuse mode

Use this repository as the **stable workflow reference**, not as the production LaTeX repository for every paper.

For a research project:

1. consult the canonical documents here;
2. use/copy the relevant Stage template as needed;
3. preserve the project's Stage reports, decision log, sources, calculations, and verification artifacts in the project's own research repository;
4. create the production paper repository at Stage 9 after Stage 7.5 approval and Stage 8 theory freeze.

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

Except where otherwise noted, the contents of this repository are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [`LICENSE`](LICENSE).

Suggested attribution: **Ryota Matsuki, `research-paper-workflow`**.

## Status

Stable published release: **`v1.1`**.

Current unreleased canonical refinement branch: **`v1.2-candidate`** — equilibrium-continuation safety hardening.

Historical releases remain immutable. See GitHub Releases for published release records.
