# research-paper-workflow v1.1

v1.1 is a backward-compatible refinement of the theory-oriented economics research workflow.

## What changed

### Whole-game novelty assessment

Strategic/game-theoretic projects now distinguish **component overlap** from **whole-game absorption**. Separate papers covering separate ingredients are no longer sufficient evidence that the complete game is absorbed.

The workflow now compares players, objectives, strategy sets, timing, endogenous allocation, strategic-feedback/best-response structure, equilibrium and welfare incidence before making a game-level absorption judgment.

### Generalization and unification contributions

A general model may qualify as a theoretical contribution when it:

- nests important prior models transparently;
- correctly recovers their benchmark results;
- makes a new strategic interaction endogenous; and
- generates at least one full-model-only theorem, threshold, ranking, sign reversal, equilibrium region, conditions-for-effectiveness result, or welfare wedge.

“Those ingredients have never been combined” remains insufficient novelty.

### Stronger benchmark discipline

Stages 3–4 now require explicit nested-benchmark architecture for generalization claims. Stage 6 re-kills the actual solved result against the benchmark literature and direct prior theorems.

### Versioning policy

Workflow releases now use:

- **PATCH** for typo/link/metadata/non-substantive clarification fixes;
- **MINOR** for criteria/check/verification additions or refinements that preserve Stage structure, verdict semantics and routing;
- **MAJOR** for incompatible Stage, verdict, routing or workflow-architecture changes.

## What did not change

- Stage 0–15 architecture, including Stage 7.5
- `GO / CONDITIONAL GO / NO-GO` semantics
- Stage 4 routing
- one-diagnosed-fix rule
- rollback/stale-state discipline
- theory freeze and submission freeze

## Migration note

An active project whose novelty verdict was based mainly on “all components are already known separately” should re-open the earliest affected novelty gate and run the new whole-game absorption test. This is a re-audit obligation, not an automatic upgrade to GO.

## Audit

v1.1 passed a fresh integration/readiness audit after PR #6. See:

- `docs/WORKFLOW_V1_1_INTEGRATION_AUDIT.md`
- `docs/WORKFLOW_V1_1_READINESS_CHECKLIST.md`
- `docs/V1_1_RELEASE_MANIFEST.md`

Historical `v1.0` remains unchanged.
