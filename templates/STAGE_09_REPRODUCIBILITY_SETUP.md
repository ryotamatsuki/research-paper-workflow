# Stage 9 — Repository / Reproducibility Setup

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a research engineer establishing the production repository only after theory freeze.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Working title: `[WORKING_TITLE]`
- Theory-freeze record: `[CURRENT_STAGE_RESULT]`
- Source repository, if any: `[SOURCE_REPOSITORY]`
- Target journal: `[TARGET_JOURNAL]`

## 2. Stage objective

Create a reproducible research repository in which manuscript, symbolic verification, numerical checks, figures, tables, references, and build outputs can be regenerated and audited.

## 3. Canonical inputs

The Stage 8 theory freeze is authoritative. Repository design may operationalize but not modify it.

## 4. Allowed changes

File organization, build tooling, environment specification, tests, scripts, and documentation.

## 5. Prohibited changes

- no theory edits hidden inside implementation;
- no unconditional checkout/reset to a historical SHA;
- no hand-edited reported numbers that are not generated from source;
- no nonreproducible figures/tables when generation is feasible.

## 6. Mandatory tasks

At work start:

1. fetch/inspect the latest remote state;
2. record current `main`, open PRs, relevant branches, and freeze SHA;
3. avoid overwriting concurrent work.

Create an appropriate scaffold, typically including some subset of:

```text
paper/
sections/
figures/
tables/
scripts/
tests/
references/
docs/
.github/workflows/
Makefile
README.md
```

Implement:

- modular LaTeX (or discipline-appropriate source);
- bibliography management;
- symbolic verification scripts;
- numerical verification scripts;
- deterministic figure/table generation;
- dependency/environment specification;
- one-command or clearly documented build;
- local-equivalent validation gates;
- CI where feasible;
- provenance/decision-log locations.

## 7. Evidence requirements

Every generated manuscript object should have an identifiable source. Document software versions and non-obvious external inputs.

## 8. Verification protocol

Run a clean local build, symbolic checks, numerical checks, and figure/table regeneration. If CI cannot run for account/platform reasons, document the blocker and run local-equivalent gates.

## 9. Kill tests

Setup is not complete if:

- manuscript cannot build cleanly from documented steps;
- reported outputs require manual hidden steps;
- theory in code differs from the freeze;
- source/reference files are missing;
- concurrent remote changes were overwritten.

## 10. Success criteria

A new collaborator should be able to clone the repository, understand the structure, reproduce verification, and build the current manuscript scaffold.

## 11. Failure criteria

Do not proceed to section writing until the reproducibility baseline is functioning or a clearly documented external blocker exists with local-equivalent validation.

## 12. Required final output

1. Starting remote/main SHA
2. Repository tree
3. Build system
4. Verification scripts/tests
5. Environment/dependencies
6. Figure/table pipeline
7. CI/local-equivalent gate status
8. Provenance locations
9. Remaining blockers
10. Exact Stage 10 writing contract

## 13. Final verdict

Choose one:

- `REPRODUCIBILITY BASELINE READY`
- `CONDITIONAL GO` — external/tooling blocker documented
- `NO-GO`

## 14. Next-stage contract

Stage 10 may write sections only against the frozen theory and verified repository infrastructure.