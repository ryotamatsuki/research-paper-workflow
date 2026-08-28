# research-paper-workflow

A reusable, reproducible workflow for developing research papers from initial motivation to submission freeze.

The v1 canonical pipeline is designed primarily for **theory-oriented economics research**, especially projects that require rigorous literature mapping, mathematical verification, novelty kill tests, staged model selection, welfare analysis, referee simulation, reproducibility, and journal positioning. Stages 0–3 can also help identify an empirical or mixed route, but v1 does not yet provide a complete empirical post-Stage-3 workflow and non-theory projects should not be force-fit through the Stage 4 theory gate.

## Governing principle

> Do not preserve an idea because effort has already been invested in it. Kill weak mechanisms early. Retain only results that survive mathematics, prior art, institutional scrutiny, robustness checks, and referee-style attacks.

The workflow is intentionally stage-gated. A project is not assumed to deserve a paper. Every stage records a canonical `GO`, `CONDITIONAL GO`, or `NO-GO`; routing/status labels are secondary, and later stages may invalidate earlier optimism.

## Canonical documents

- [`THEORY_PAPER_RESEARCH_PIPELINE.md`](THEORY_PAPER_RESEARCH_PIPELINE.md): canonical Stage 0–15 theory workflow, including Stage 7.5.
- [`GOVERNANCE.md`](GOVERNANCE.md): repository governance, evidence/provenance rules, verdict/rollback policy, verification rules, and change control.

The hierarchy is `GOVERNANCE.md` → canonical pipeline → stage templates → checklists → examples. Lower-level materials may elaborate but may not weaken higher-level gates.

## v1 integration audit

PR #4 audits the complete workflow before release preparation:

- [`WORKFLOW_V1_INTEGRATION_AUDIT.md`](docs/WORKFLOW_V1_INTEGRATION_AUDIT.md)
- [`WORKFLOW_V1_READINESS_CHECKLIST.md`](docs/WORKFLOW_V1_READINESS_CHECKLIST.md)
- [`WORKFLOW_V1_CHANGELOG.md`](docs/WORKFLOW_V1_CHANGELOG.md)

The post-audit verdict is **`WORKFLOW v1 READY`** for repeated use as a theory-oriented economics workflow. This is a release-candidate readiness verdict, not a GitHub `v1.0` tag or release.

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
7. If a later stage invalidates an earlier result, return to the earliest affected stage and treat dependent downstream outputs as stale.
8. Do not initialize a full-paper production repository until Stage 7.5 approves full-paper investment and Stage 8 freezes the theory.
9. Preserve rejected branches and negative results as part of the research provenance.

## Repository structure

```text
research-paper-workflow/
├── README.md
├── THEORY_PAPER_RESEARCH_PIPELINE.md
├── GOVERNANCE.md
├── templates/
├── checklists/
├── docs/
└── examples/
```

## Intended use

This repository is a research-development and research-termination system, not a prompt collection. Its main value is to make weak, derivative, ad hoc, or mathematically fragile research branches fail early and visibly before full-paper writing begins.

## Status

Workflow v1 has completed its integration audit and is ready for repeated theory-project use. The next repository step is a separate **v1 Release Preparation / Repository Template Readiness** review. No `v1.0` tag or release has been created by the integration audit.
