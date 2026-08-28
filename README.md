# research-paper-workflow

A reusable, reproducible workflow for developing research papers from initial motivation to submission freeze.

This repository is designed primarily for theory-oriented economics research, especially projects that require rigorous literature mapping, mathematical verification, novelty kill tests, staged model selection, welfare analysis, referee simulation, reproducibility, and journal positioning.

## Governing principle

> Do not preserve an idea because effort has already been invested in it. Kill weak mechanisms early. Retain only results that survive mathematics, prior art, institutional scrutiny, robustness checks, and referee-style attacks.

The workflow is intentionally stage-gated. A project is not assumed to deserve a paper. Every stage may end in `GO`, `CONDITIONAL GO`, or `NO-GO`, and later stages may invalidate earlier optimism.

## Canonical documents

- [`THEORY_PAPER_RESEARCH_PIPELINE.md`](THEORY_PAPER_RESEARCH_PIPELINE.md): canonical Stage 0–15 workflow, including Stage 7.5.
- [`GOVERNANCE.md`](GOVERNANCE.md): repository governance, evidence rules, verification rules, and change-control policy.

The hierarchy is `GOVERNANCE.md` → canonical pipeline → stage templates → checklists → examples. Lower-level materials may elaborate but may not weaken higher-level gates.

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

## Recommended workflow

1. Start at Stage 0 unless a prior project has already produced a verified input for a later stage.
2. Fill only the placeholders relevant to the project; mark unknown items `UNRESOLVED` rather than inventing them.
3. Run the stage as an executable research prompt and preserve the required report output.
4. Record an explicit `GO`, `CONDITIONAL GO`, or `NO-GO` and the next-stage contract.
5. If a minimal model fails, change only the diagnosed margin in Stage 5.
6. Re-kill novelty after actual results are known in Stage 6.
7. Do not initialize a full-paper repository until Stage 7.5 approves full-paper investment and Stage 8 freezes the theory.
8. Preserve rejected branches and negative results as part of the research provenance.

## Repository structure

```text
research-paper-workflow/
├── README.md
├── THEORY_PAPER_RESEARCH_PIPELINE.md
├── GOVERNANCE.md
├── templates/
├── checklists/
└── examples/        # worked cases added in later PRs
```

## Intended use

This repository is a research-development and research-termination system, not a prompt collection. Its main value is to make weak, derivative, ad hoc, or mathematically fragile research branches fail early and visibly before full-paper writing begins.

## Status

Canonical workflow and reusable Stage 0–15 templates/checklists are available. Worked case studies and automation/CI are intentionally deferred to later PRs.