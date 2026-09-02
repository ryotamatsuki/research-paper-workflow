# Novelty-Gate Correction — Whole-Game Absorption and Generalization

Date: 2026-09-02

Status: **v1.1 candidate pending fresh integration/readiness audit**

Starting canonical main SHA: `07466bcb1a6d3bc654b52945f21b034b38e45281`

Historical stable release: `v1.0` at commit `d5c5146098d97279ad3e90342fa757f0f31c8264`.

## 1. Problem identified

The v1.0 workflow correctly rejects cosmetic novelty and weak combination novelty, but its Stage 2–6 wording can be applied too aggressively in strategic/game-theoretic projects.

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
- `docs/VERSIONING_POLICY.md`

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

`v1.0` is already a stable historical release and its tag must not be moved.

The versioning policy is revised to classify changes by workflow-interface compatibility:

- **PATCH (`v1.0.1`)** — typo, link, metadata, and non-substantive clarification fixes;
- **MINOR (`v1.1`)** — additions or refinements to criteria, checks, and verification capability that preserve existing Stage structure, canonical verdict semantics, and routing;
- **MAJOR (`v2.0`)** — Stage addition/removal/merger, `GO / CONDITIONAL GO / NO-GO` semantic changes, routing changes, or incompatible workflow-architecture changes.

The novelty-gate correction preserves Stage 0–15 + 7.5, preserves canonical verdict meanings, and preserves routing. It therefore qualifies as a **v1.1 minor-version candidate** even though active strategic projects may merit re-audit under the improved criteria.

Before creating `v1.1`, the workflow must receive a fresh integration/readiness audit confirming that:

- the new whole-game standard does not weaken the anti-cosmetic novelty gate;
- combination novelty remains insufficient by itself;
- generalization/unification requires nested benchmark recovery plus a full-model-only result;
- Stage 2, Stage 3, Stage 4, and Stage 6 remain internally consistent;
- `NO-GO` and negative results remain legitimate outcomes;
- Stage identities, verdict semantics, and routing remain unchanged from the stable v1 architecture.

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

Release route:

`PR #6 merge → fresh integration/readiness audit → audit PR merge → v1.1 tag / GitHub Release`.
