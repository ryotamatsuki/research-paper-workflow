# research-paper-workflow v2.2 — Release Notes

Date: 2026-09-18  
Release class: **MINOR**

## Summary

v2.2 strengthens theorem-oriented novelty control without changing the canonical Stage architecture, verdict semantics, routing, rollback rules, theory-freeze meaning, or submission-freeze meaning.

The central new rule is:

> **Absence of the same application-specific formula is not evidence of theorem novelty.**

A theory project must now test whether its headline result is a direct specialization, boundary case, or short corollary of a known general theorem after application labels are removed.

## Canonical changes

### Stage 4 — mathematical canonicalization

Stage 4 now requires an application-neutral canonical representation of the solved model, including:

- strategy-set geometry;
- payoff/function class;
- interaction matrix/operator or aggregate coupling;
- coupling constraints;
- equilibrium/planner object;
- plausible standard parent model classes.

Where relevant, projects must attempt recentering, normalization, variable elimination, matrix/KKT/complementarity form, potential/network/aggregative form, or simplex/transportation/assignment-polytope representation.

### Stage 6 — theorem-level absorption

Stage 6 now requires both application-specific and application-neutral searches.

For every serious general parent theorem, projects must preserve an explicit mapping:

`prior theorem → candidate variables/parameters → restrictions/transformations → candidate headline result → absorption verdict`.

Allowed verdicts are:

- `DIRECTLY ABSORBED`;
- `PARTIALLY ABSORBED`;
- `NOT ABSORBED`.

A plausible parent theorem left untested blocks a theorem-novelty PASS.

### Stage 11 — known-model-in-disguise hostile attack

The final manuscript must be attacked as a possible known model in disguise. The hostile referee repeats the strongest canonical reduction and parent-theorem specialization. A newly discovered absorption is recorded as:

`CERTIFICATION REGRESSION — NOVELTY ABSORPTION`

and routed back to Stage 6 or earlier.

## Supporting changes

v2.2 synchronizes:

- `checklists/LITERATURE_AUDIT_CHECKLIST.md`;
- `checklists/NOVELTY_KILL_CHECKLIST.md`;
- `checklists/REFEREE_ATTACK_CHECKLIST.md`;
- `GOVERNANCE.md`;
- `docs/VERSIONING_POLICY.md`;
- `README.md`.

The previously integrated post-v2.1 formal-verification refinement is also included in the v2.2 published state.

## Compatibility

v2.2 is MINOR, not PATCH, because it adds material verification obligations and a new novelty-discrimination criterion inside existing Stages.

It is not MAJOR because it does not:

- add, remove, merge, or renumber a canonical Stage;
- change `GO / CONDITIONAL GO / NO-GO` semantics;
- change canonical routing;
- weaken rollback/freeze rules;
- replace the v2 architecture.

Existing projects remain interpretable under the same Stage structure, but an active project may require re-audit if theorem novelty previously relied on application-specific prior-art search.

## Migration rule

For active theorem papers that have already passed Stage 6:

1. retain their existing mathematical certification;
2. reconstruct the Stage-4 canonical mathematical form;
3. run the new Stage-6 parent-theorem absorption map;
4. if already manuscript-complete, also run the Stage-11 known-model-in-disguise attack;
5. mark submission authorization HOLD if a serious unclosed parent-theorem candidate exists.

No project should silently preserve a prior novelty PASS solely because it pre-dates v2.2.
