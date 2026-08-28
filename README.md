# research-paper-workflow

A reusable, reproducible workflow for developing research papers from initial motivation to submission freeze.

This repository is designed primarily for theory-oriented economics research, especially projects that require rigorous literature mapping, mathematical verification, novelty kill tests, staged model selection, welfare analysis, referee simulation, reproducibility, and journal-positioning.

## Governing principle

> Do not preserve an idea because effort has already been invested in it. Kill weak mechanisms early. Retain only results that survive mathematics, prior art, institutional scrutiny, robustness checks, and referee-style attacks.

The workflow is intentionally stage-gated. A project is not assumed to deserve a paper. Every stage may end in `GO`, `CONDITIONAL GO`, or `NO-GO`, and later stages may invalidate earlier optimism.

## Canonical documents

- [`THEORY_PAPER_RESEARCH_PIPELINE.md`](THEORY_PAPER_RESEARCH_PIPELINE.md): canonical Stage 0–15 workflow.
- [`GOVERNANCE.md`](GOVERNANCE.md): repository governance, evidence rules, verification rules, and change-control policy.

## Planned repository structure

```text
research-paper-workflow/
├── README.md
├── THEORY_PAPER_RESEARCH_PIPELINE.md
├── GOVERNANCE.md
├── templates/
├── checklists/
└── examples/
```

The first bootstrap milestone freezes the workflow architecture and governance. Reusable stage templates, checklists, and worked research case studies will be added only after that foundation is reviewed.

## Intended use

For a new project, instantiate the workflow from Stage 0 rather than jumping directly to manuscript writing. In particular, do not initialize a full paper repository until the research has survived the novelty, minimal-model, mechanism-hardening, and theory-freeze gates.

## Status

Bootstrap v1 in progress.
