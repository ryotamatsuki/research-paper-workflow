# Workflow v1.3 Integration Audit

Audit date: 2026-09-06

Stable baseline: `v1.2` at `944e6bace951e13645b02200a63bf25363dc7242`.

Change under audit: PR #10 — result-to-exposition and figure/table architecture hardening.

## Executive verdict

**`WORKFLOW v1.3 READY`**

No unresolved FATAL or MAJOR integration defect remains.

## Version classification

The change is **MINOR**, not MAJOR, under `docs/VERSIONING_POLICY.md`.

Compatibility reasons:

- [x] Canonical hierarchy unchanged.
- [x] Stage 0–15 architecture, including Stage 7.5, unchanged.
- [x] No Stage added, removed, merged, or renumbered.
- [x] `GO / CONDITIONAL GO / NO-GO` semantics unchanged.
- [x] Normal Stage routing unchanged.
- [x] One-diagnosed-fix discipline unchanged.
- [x] Rollback/stale-state behavior unchanged; the new text only identifies whether an exposition defect belongs to Stage 10, 13, or bounded Stage-14 artwork repair under the existing rollback rule.
- [x] Theory-freeze meaning unchanged; Stage-7 exposition triage is explicitly outside the Stage-8 theory freeze.
- [x] Submission-freeze meaning unchanged; Stage 15 only adds final figure/table provenance to the frozen package.
- [x] Existing `v1.0`, `v1.1`, and `v1.2` releases remain immutable.

Therefore the compatible next release is `v1.3`, not `v2.0`.

## Canonical integration audit

### Stage 7 — identify

PASS.

Stage 7 now requires a result-to-exposition triage for each surviving headline result. Candidate vehicles are theorem/proposition, figure, table, numerical illustration, or concise prose.

The rule does **not** force graphics before theory freeze and does **not** impose a minimum figure count. The triage is explicitly a planning artifact and cannot justify changing the model or theorem.

### Stage 10 — design and implement

PASS.

A mandatory Figure/Table Architecture Gate now occurs before the Introduction is finalized. Every headline result receives one primary exposition vehicle. Required quantitative figures/tables must be generated from verified scripts or authoritative source data and must preserve the actual economic scale, sign, and proven domain.

The gate explicitly rejects:

- manual/unverified quantitative visuals;
- decorative figure quotas;
- arbitrary normalized polynomial/index curves presented as the underlying economic object;
- visuals whose interpretation exceeds the theorem's scope.

### Stage 11 — hostile exposition attack

PASS.

The canonical pipeline and `REFEREE_ATTACK_CHECKLIST.md` now attack visuals that hide domain restrictions, use arbitrary normalization as if it were the reported economic object, or visually imply a stronger result than the proof establishes.

This is an additional referee check inside the existing Stage 11 gate; it does not change Stage 11 routing or verdict semantics.

### Stage 13 — integrate

PASS.

Stage 13 now reconciles the Stage-10 architecture with the selected journal. It checks placement, captions, manuscript references, journal-specific limits/file types/color/accessibility rules, and generator/source preservation.

A bounded presentation gap for an already verified result may be closed at Stage 13 with an explicit no-theory/no-result-change record. If a defensible figure/table would require a new substantive computation, result, or robustness exercise, the existing rollback rule sends the project to the earliest affected research stage.

### Stage 14 — verify

PASS.

Stage 14 is explicitly an artwork/reproducibility QA gate rather than the normal design stage. It now checks:

- regeneration from source;
- representative values, signs, thresholds, and benchmark identities;
- current journal artwork rules;
- vector-font embedding when required;
- raster effective resolution where applicable;
- final-size legibility and grayscale/color accessibility;
- source/generator inclusion in the package;
- page-by-page visual inspection.

A bounded artwork-format defect may still be repaired at Stage 14 if the underlying verified object and interpretation are unchanged. A missing central exposition vehicle routes to Stage 10/13 under the existing rollback logic.

## Cross-document consistency audit

PASS.

The following canonical and supporting documents are aligned:

- `THEORY_PAPER_RESEARCH_PIPELINE.md` — defines the Stage 7 → 10 → 13 → 14 lifecycle and exposition-integrity cross-stage rule;
- `templates/STAGE_07_WELFARE_GENERALITY.md` — performs triage;
- `templates/STAGE_10_PAPER_BUILD.md` — designs and implements architecture;
- `templates/STAGE_13_FULL_PAPER_INTEGRATION.md` — performs journal-specific integration;
- `templates/STAGE_14_SUBMISSION_QA.md` — performs submission artwork QA;
- `checklists/FIGURE_TABLE_CHECKLIST.md` — provides the reusable lifecycle checklist;
- `checklists/SUBMISSION_CHECKLIST.md` — incorporates final artwork/package checks;
- `checklists/REFEREE_ATTACK_CHECKLIST.md` — adds visual-overclaim and arbitrary-normalization attack;
- `README.md` and `docs/VERSIONING_POLICY.md` — classify the change as a v1.3 minor candidate.

The PR patch for `THEORY_PAPER_RESEARCH_PIPELINE.md` was reviewed against v1.2. No unrelated Stage content was removed; modifications are limited to the exposition lifecycle, Stage 7/10/11/13/14 obligations, Stage-15 provenance, and renumbering of later cross-stage subsection labels after insertion of exposition integrity.

## Stress tests

### 1. Correct but visually trivial scalar comparative static

Scenario: a headline result is a simple monotone sign theorem and a figure would merely redraw the theorem.

Expected: Stage 7/10 may select theorem/prose; no figure is forced.

Result: **PASS**.

### 2. Threshold/sign-reversal headline result

Scenario: the economic response is negative, becomes more negative, then crosses zero at a verified threshold.

Expected: Stage 7 flags it as a figure candidate; Stage 10 decides whether a figure materially lowers reader cost and, if required, implements it from the actual verified derivative; Stage 13 integrates it; Stage 14 checks artwork/package compliance.

Result: **PASS**.

### 3. Only an arbitrary normalized switching polynomial is readily available

Scenario: the sign polynomial is verified but the absolute derivative curve has not been reconstructed.

Expected: the normalized polynomial may not be labeled or plotted as the actual economic derivative. Either verify/reconstruct the actual object or retain theorem/prose/appropriately labeled sign-index presentation.

Result: **PASS**.

### 4. Stage 14 detects non-embedded vector fonts

Scenario: the figure is mathematically correct and already integrated, but the target journal requires embedded fonts.

Expected: bounded Stage-14 artwork repair is allowed because the underlying object and interpretation are unchanged; re-run Stage-14 QA after repair.

Result: **PASS**.

### 5. Stage 14 discovers that a central visual requires a new parameter experiment

Scenario: a missing figure can only be produced by adding a new substantive numerical experiment or robustness result.

Expected: Stage 14 must not invent it. Roll back to the earliest affected research/manuscript stage.

Result: **PASS**.

### 6. Target journal imposes a strict figure/table count

Scenario: Stage-10 architecture contains more visuals/tables than the target permits.

Expected: Stage 13 compresses, combines, relocates, or removes redundant presentation while preserving verified results; no theory change is implied.

Result: **PASS**.

### 7. Existing v1.2 project

Scenario: a project completed under v1.2 is already at Stage 14.

Expected: its prior Stage verdicts remain interpretable. The stronger v1.3 checks may motivate a bounded exposition/artwork re-audit but do not invalidate the old Stage numbering, verdicts, routing, or freeze semantics by version definition alone.

Result: **PASS**.

## Release automation audit

PASS, subject to the normal post-merge execution check.

`.github/workflows/publish-v1.3.yml`:

1. triggers only on a push to `main` whose head commit message contains `Complete v1.3 integration audit`;
2. requires both v1.3 readiness records to say READY;
3. requires the new figure/table checklist and key Stage-10/14 integration markers;
4. refuses to overwrite an existing `v1.3` tag;
5. finalizes only release metadata (`GOVERNANCE.md`, pipeline version header, README candidate status, version-policy candidate wording);
6. creates immutable tag/release `v1.3` using `docs/V1_3_RELEASE_NOTES.md`.

At audit time, `v1.3` tag is absent and `v1.2` remains fixed at `944e6bace951e13645b02200a63bf25363dc7242`.

## Release contract

After this PR is merged with a head commit message containing `Complete v1.3 integration audit`:

1. verify the release workflow succeeds;
2. verify final metadata reports `v1.3` rather than `v1.3-candidate`;
3. verify immutable tag `v1.3` exists and points to the finalized metadata commit;
4. verify GitHub Release `research-paper-workflow v1.3` exists;
5. leave `v1.0`, `v1.1`, and `v1.2` unchanged.

Therefore: **`WORKFLOW v1.3 READY`**
