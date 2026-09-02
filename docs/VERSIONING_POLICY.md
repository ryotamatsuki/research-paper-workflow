# Versioning Policy

Status: active v1-series policy

This document defines version compatibility for the `research-paper-workflow` repository. It does not override `GOVERNANCE.md`; governance remains the highest-authority repository rule.

## 1. Purpose

A workflow version is a promise about the stability of the research workflow interface. Version changes should distinguish between non-substantive corrections, backward-compatible refinement of existing gates, and incompatible changes to the workflow architecture.

The version number therefore tracks the **kind of workflow change**, not merely whether a later interpretation could alter an earlier research judgment.

## 2. Version format

Stable releases use `vMAJOR.MINOR` or `vMAJOR.MINOR.PATCH` Git tags, for example `v1.0`, `v1.1`, and `v1.0.1`.

Pre-release labels may describe an unreleased repository state. They do **not** imply that a Git tag or GitHub Release exists unless that tag/release is independently present in GitHub.

## 3. Patch changes — `v1.0.1`

A patch version is for non-substantive corrections that do not materially change research-decision logic.

Examples include:

- typo or formatting fixes;
- broken-link repair;
- metadata corrections;
- non-substantive wording clarification;
- documentation-only corrections;
- corrections to historical/audit navigation that do not rewrite the historical record.

A patch must not add a material new decision criterion, verification obligation, Stage, verdict meaning, or route.

## 4. Minor changes — `v1.1`

A minor version may add or refine research-decision capability **while preserving the existing Stage structure, canonical verdict semantics, and routing architecture**.

Examples include:

- adding or refining novelty, literature, mathematical, empirical, or referee checks within an existing Stage;
- clarifying an existing gate in a way that improves discrimination between false positives and false negatives;
- adding verification obligations or comparison tests within existing Stages;
- adding backward-compatible optional checklists, templates, worked examples, provenance aids, automation, or companion guidance;
- recognizing an additional legitimate contribution route, such as generalization/unification, when it is evaluated inside the existing Stage and routing structure;
- strengthening or refining evidence requirements without changing what the Stage itself is or where its canonical verdict routes.

A minor release may cause a previously completed project to merit re-audit under the improved criteria. **That fact alone does not make the workflow change major** so long as the Stage architecture, `GO / CONDITIONAL GO / NO-GO` meanings, and routing remain compatible.

Typical v1-series minor releases are `v1.1`, `v1.2`, and so on.

## 5. Major changes — `v2.0`

A major version is required when the workflow architecture or canonical decision interface changes incompatibly.

Examples include:

- adding, removing, merging, renumbering, or materially redefining mandatory canonical Stages;
- changing the canonical hierarchy in an incompatible way;
- changing the meaning of `GO / CONDITIONAL GO / NO-GO`;
- changing normal Stage routing, such as where a `GO`, `CONDITIONAL GO`, or `NO-GO` must proceed;
- removing or reversing the one-diagnosed-fix discipline;
- incompatibly changing rollback/stale-state, theory-freeze, or submission-freeze semantics;
- changing the primary canonical method architecture so that existing v1 projects cannot be interpreted under the same Stage structure;
- replacing an existing mandatory workflow path with a materially different one.

Such a change is normally a `v2.0` candidate after v1.x.

## 6. Compatibility test

A change is normally backward compatible within the v1 line when an existing v1 project can continue to rely on the same:

- Stage numbering and identity;
- canonical hierarchy;
- `GO / CONDITIONAL GO / NO-GO` semantics;
- normal Stage routing;
- one-diagnosed-fix discipline;
- rollback/stale-state behavior;
- theory-freeze and submission-freeze meaning.

Changes to the **quality, precision, or coverage of checks inside those stable boundaries** may be minor even when they create a reason to re-audit an active project.

When classification is ambiguous, document the version-impact reasoning in the PR and audit it before release.

## 7. Canonical versus non-canonical changes

Authority remains:

1. `GOVERNANCE.md`
2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
3. `templates/*.md`
4. `checklists/*.md`
5. `examples/*`

Release/audit documentation under `docs/` records version, history, and readiness; it does not outrank the canonical hierarchy.

Changes to examples normally do not change canonical compatibility unless they expose and trigger a separate canonical correction.

## 8. Worked examples

Adding a worked example is normally a minor-version feature. Correcting a factual or link error in an existing example may be a patch. Reinterpreting an example does not silently change canonical rules.

## 9. Audit and historical documents

Audit documents are historical records of the repository state that was reviewed. Later releases should not rewrite prior audit conclusions merely to make old documents read as if they were created under the new release state.

A factual correction to an audit record should be explicit and traceable.

## 10. Pre-release states

A release-candidate state may use a version label in documentation while the Git tag is still pending. Release-facing documentation must clearly distinguish:

- current stable version;
- prospective version;
- release-ready repository state;
- actual Git tag;
- actual GitHub Release.

`v1.1 release-ready` is not synonymous with `v1.1 released`.

## 11. Tag immutability

Published stable version tags are immutable historical references.

- Do not silently move or overwrite an existing stable tag.
- A release tag must point to a reviewed `main` state.
- If a released version is defective or incomplete, create a later patch/minor/major release as appropriate instead of moving the historical tag.

## 12. Release correction policy

After a stable release:

- typo, link, metadata, and non-substantive clarification defects use a patch release where a new release is warranted;
- backward-compatible additions or refinements to checks, criteria, verification capability, or optional workflow aids use a minor release;
- incompatible Stage, verdict, routing, or workflow-architecture changes use a major release;
- security/legal/administrative issues should be handled explicitly according to their actual impact rather than disguised as ordinary wording changes.

## 13. Deprecation expectations

Backward-compatible deprecation should be documented before removal where practical. Removal or semantic replacement of a stable canonical Stage/path is a breaking change unless the removed item was explicitly experimental/non-canonical.

## 14. Current interpretation

`v1.0` is the first stable historical release of the theory-oriented economics research-decision workflow.

The 2026-09-02 novelty-gate refinement preserves Stage structure, canonical verdict semantics, and routing while adding more precise whole-game absorption and generalization/unification checks. After fresh integration/readiness audit, it was released as the **minor version `v1.1`**.
