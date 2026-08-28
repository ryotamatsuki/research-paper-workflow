# Versioning Policy

Status: prospective v1.0 policy

This document defines version compatibility for the `research-paper-workflow` repository. It does not override `GOVERNANCE.md`; governance remains the highest-authority repository rule.

## 1. Purpose

A workflow version is a promise about research-decision behavior, not merely a documentation snapshot. Version changes therefore reflect whether an existing project can continue to interpret stages, gates, evidence requirements, handoffs, rollback, and freezes in the same way.

## 2. Version format

Stable releases use `vMAJOR.MINOR` or `vMAJOR.MINOR.PATCH` Git tags, for example `v1.0`, `v1.1`, and `v1.0.1`.

Pre-release labels such as `v1-rc1` or `v1.0-rc1` may describe a document/repository state. They do **not** imply that a Git tag or GitHub Release exists unless that tag/release is independently present in GitHub.

## 3. Major changes

A major version is required when a change can alter the meaning or routing of an existing project's canonical research decisions. Examples include:

- removing, merging, renumbering, or materially redefining canonical stages;
- changing the canonical hierarchy;
- changing `GO / CONDITIONAL GO / NO-GO` semantics;
- materially weakening or strengthening the novelty standard in a way that changes prior project verdicts;
- changing the one-diagnosed-fix rule;
- changing theory-freeze, submission-freeze, or rollback/stale-state semantics incompatibly;
- changing required evidence or handoff contracts so that an existing v1 project can no longer be interpreted without migration;
- changing the primary canonical method architecture rather than adding a companion route.

Such a change is normally a `v2.0` candidate after v1.x.

## 4. Minor changes

A minor version adds backward-compatible capability while preserving existing canonical behavior. Examples include:

- a separate empirical companion workflow that does not change the v1 theory path;
- a new optional checklist or optional template variant;
- a new worked example;
- optional bootstrap/repository guidance;
- optional automation or evidence tooling;
- additional non-breaking provenance aids.

Such changes are normally `v1.1`, `v1.2`, and so on.

## 5. Patch changes

A patch version does not change research-decision behavior. Examples include:

- typo or formatting fixes;
- broken-link repair;
- metadata corrections;
- wording clarification that does not change a gate;
- documentation-only corrections;
- corrections to historical/audit navigation that do not rewrite the historical record.

Such changes are normally `v1.0.1`, `v1.0.2`, and so on.

## 6. Backward compatibility

A change is backward compatible within v1 when an existing v1 project can continue to rely on the same:

- Stage numbering and identity;
- canonical gate meanings;
- material evidence requirements;
- major handoff contracts;
- one-diagnosed-fix discipline;
- rollback/stale-state behavior;
- theory-freeze and submission-freeze meaning.

If a change can alter a prior project's canonical verdict or required research route, it is presumptively breaking and requires explicit major-version assessment.

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

- prospective version;
- release-ready repository state;
- actual Git tag;
- actual GitHub Release.

`v1.0 release-ready` is not synonymous with `v1.0 released`.

## 11. Tag immutability

Published stable version tags are immutable historical references.

- Do not silently move or overwrite an existing stable tag.
- A release tag must point to a reviewed `main` state.
- If a released version is defective, create a corrective patch/minor/major release as appropriate instead of moving the historical tag.

## 12. Release correction policy

After a stable release:

- documentation-only non-behavioral defects use a patch release where a new release is warranted;
- backward-compatible capability uses a minor release;
- breaking canonical behavior uses a major release;
- security/legal/administrative issues should be handled explicitly according to their actual impact rather than disguised as ordinary wording changes.

## 13. Deprecation expectations

Backward-compatible deprecation should be documented before removal where practical. Removal or semantic replacement of a stable canonical Stage/path is a breaking change unless the removed item was explicitly experimental/non-canonical.

## 14. v1.0 interpretation

The prospective `v1.0` release promises a stable **theory-oriented economics research-decision workflow**. It does not promise a complete empirical pipeline, automatic execution, CI enforcement, proof automation, guaranteed novelty, guaranteed publication, or a production-paper repository scaffold.
