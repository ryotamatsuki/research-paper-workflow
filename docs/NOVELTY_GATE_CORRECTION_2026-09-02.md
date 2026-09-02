# Novelty-Gate Correction — Whole-Game Absorption and Generalization

Date: 2026-09-02

Status: **release-blocking pre-v1.0 correction pending review**

Starting canonical main SHA: `07466bcb1a6d3bc654b52945f21b034b38e45281`

## 1. Problem identified

The v1.0 release-ready candidate correctly rejected cosmetic novelty and combination novelty, but its Stage 2–6 wording could be applied too aggressively in strategic/game-theoretic projects.

The failure mode is:

1. decompose a candidate game into individual ingredients;
2. locate a prior literature for each ingredient;
3. infer that only the one unmatched ingredient can carry novelty;
4. prematurely kill the full strategic architecture without establishing whole-game equivalence or result-level redundancy.

This conflates **component overlap** with **whole-game absorption**.

A second omission was that the workflow did not explicitly recognize an economically substantive **generalization/unification** as a possible theory contribution when it nests important prior models and generates new strategic or welfare results.

## 2. Corrected principle

For strategic/game-theoretic research:

> Known components do not by themselves imply that the full game is absorbed.

An absorption verdict requires at least one of:

1. a prior model that reproduces the economically relevant players, objectives, strategy sets, timing, endogenous allocation, strategic-feedback network, and equilibrium after direct mapping/restriction; or
2. a prior theorem that makes the candidate headline result an immediate corollary.

If multiple distinct prior literatures are needed to reconstruct separate ingredients, the default classification is component overlap or structural proximity until the full-game interaction is evaluated.

The converse is equally important:

> “Nobody combined these ingredients” is not sufficient novelty.

A combined/generalized model must generate a genuinely new strategic interaction and a nontrivial theorem, threshold, equilibrium region, ranking, sign reversal, welfare wedge, or conditions-for-effectiveness result.

## 3. Generalization / unification route

A model may qualify as a main theoretical contribution when it:

- transparently nests important prior models;
- correctly recovers their benchmark equilibria/results;
- endogenizes a strategic interaction absent from each benchmark;
- yields at least one result unavailable in the nested benchmarks alone.

A model does not qualify merely because it is more general in notation, functional form, or number of players.

## 4. Files changed by this correction

Canonical/operational behavior is updated in:

- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_02_NOVELTY_GATE.md`
- `templates/STAGE_03_MECHANISM_SEARCH.md`
- `templates/STAGE_04_MINIMAL_MODEL.md`
- `templates/STAGE_06_NOVELTY_REKILL.md`
- `checklists/LITERATURE_AUDIT_CHECKLIST.md`
- `checklists/NOVELTY_KILL_CHECKLIST.md`

## 5. New required tests

Strategic projects now require, where applicable:

### Whole-game absorption test

Compare:

- players;
- objective functions;
- strategy sets;
- timing/commitment;
- information;
- participation/outside options;
- endogenous allocation/sorting;
- market structure;
- strategic-feedback/best-response network;
- equilibrium concept;
- welfare incidence.

### Nested-benchmark test

For a generalization/unification claim:

- identify the prior models nested by the candidate;
- state the restriction/player/strategy removal that recovers each benchmark;
- recover the benchmark result;
- identify the result generated only by the full architecture.

## 6. Compatibility / version assessment

`docs/VERSIONING_POLICY.md` states that a change capable of altering prior project verdicts is normally a breaking semantic change after stable release.

However, the repository currently has **no `v1.0` Git tag or GitHub Release**. The existing state is only a `v1.0 release-ready candidate`.

Therefore this correction should be treated as a **pre-release release-blocking correction to the v1.0 candidate**, not as a silent post-release patch and not automatically as a v2.0 release.

Before creating a `v1.0` tag, the workflow should receive a fresh integration/readiness audit confirming that:

- the new whole-game standard does not weaken the anti-cosmetic novelty gate;
- combination novelty remains insufficient by itself;
- generalization/unification requires a full-model-only result;
- Stage 2, Stage 3, Stage 4, and Stage 6 remain internally consistent;
- negative results and `NO-GO` remain legitimate outcomes.

## 7. Migration implication for active projects

Any active theory project whose novelty verdict materially relied on:

- “all components are already known separately”; or
- a one-page absorption test that mapped different components to different papers rather than one full-game model;

should re-open the earliest affected novelty gate and distinguish:

- component overlap;
- whole-game absorption;
- economically substantive generalization/unification.

This does **not** imply automatic upgrade to `GO`. The full game must still produce a nontrivial result beyond its nested benchmarks.

## 8. Validation target

The correction is successful if it prevents both errors:

1. **false positive novelty** — accepting a mere ingredient combination;
2. **false negative novelty** — killing a strategically distinct generalization because its ingredients are individually known.
