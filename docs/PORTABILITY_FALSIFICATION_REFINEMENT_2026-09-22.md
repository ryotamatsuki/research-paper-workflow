# Economic Portability / Falsification Refinement — 2026-09-22

## Problem

The workflow already had strong mathematical certification, theorem-scope auditing, novelty re-kill, and late journal positioning. A remaining failure mode was exposed by a theory-paper redevelopment case:

- the canonical model was mathematically correct and reproducible;
- the contribution could be described as an economic mechanism inside that model;
- hostile audit found no fatal proof error;
- yet the workflow had not required a sufficiently strong pre-freeze attempt to determine whether the political/economic sign survived a genuinely different microfoundation;
- journal positioning therefore risked treating a model-specific mechanism as if it were portable enough for a more general field-journal claim.

The defect was not primarily Stage-12 journal selection. Stage 12 already exists to choose journals from the surviving contribution. The missing capability was a stronger **journal-neutral research-strength certification before theory freeze**.

## Design principle

The workflow must answer two different questions in two different places.

### Stage 7.5A

> What is the maximum defensible research strength of the theory that actually survived adversarial testing?

Stage 7.5A must certify portability, conditional portability, model dependence, institutional dependence, or falsification without reference to preferred journal prestige.

### Stage 12

> Which current journal is appropriate for that already-certified contribution?

Stage 12 consumes the Stage-7.5A certificate and calibrates the journal choice from current official scope and recent comparable papers.

The direction is therefore:

`research-strength certification → theory freeze → manuscript hostile audit → journal positioning`

not:

`preferred journal → retrofitted robustness requirement → repeated model rescue`.

## Stage-7.5A refinement

For every headline claim presented as more than baseline/model-specific:

1. identify the mechanism invariant;
2. identify assumptions plausibly carrying the result;
3. pre-specify at least one economically meaningful alternative formulation before solving;
4. record the alternative primitives, equilibrium concept, credibility rationale, and exact success/failure criterion;
5. re-solve the affected equilibrium rather than reusing baseline formulas outside their derivation domain;
6. preserve negative results;
7. identify failure boundaries or abstract sufficient conditions where possible;
8. classify the claim as:
   - `PORTABLE`;
   - `CONDITIONALLY PORTABLE`;
   - `MODEL-SPECIFIC`;
   - `INSTITUTION-SPECIFIC`; or
   - `FALSIFIED`;
9. record the classification in a Contribution Robustness Certificate.

Diagnostic alternatives are allowed inside Stage 7.5A only as falsification instruments. A new mechanism or substantive model redesign must roll back to the earliest affected research stage and be recertified.

## Stop rule

The workflow should strengthen a paper aggressively but should not optimize indefinitely for a preferred result.

Normally stop attempted cross-model rescue and certify the claim as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` when:

- two economically meaningful, pre-specified, non-cosmetic portability attacks overturn the same claimed cross-model mechanism;
- the failures are not due to implementation error;
- no defensible abstract sufficient-condition theorem survives; and
- subsequent alternatives would mainly be chosen to recover the preferred sign.

Further research remains possible, but only as a consciously distinct research program routed back to the appropriate earlier Stage.

## Why this is not Stage-12 duplication

Stage 7.5A does not rank journals, inspect impact factors, or determine a submission ladder. It produces research evidence.

Stage 12 does not decide whether a theorem is portable. It compares the certified contribution with:

- current aims and scope;
- recent comparable articles;
- demonstrated theoretical sophistication;
- article/contribution type;
- empirical/policy expectations;
- likely editor/referee fit;
- current submission obligations.

If a journal appears to require greater generality than the certificate supports, the normal response is to reject or downgrade that **journal candidate**, not to silently strengthen the claim or repeatedly redesign the model.

## New artifact

Stage 7.5A now produces a **Contribution Robustness Certificate** for each headline claim, recording:

- canonical claim;
- mechanism invariant;
- baseline assumptions;
- pre-specified alternative formulations;
- ex ante success/failure criteria;
- re-solved equilibrium/proof/code artifacts;
- results under alternatives;
- failure boundary or sufficient conditions;
- portability classification;
- maximum defensible manuscript wording;
- prohibited stronger wording;
- stop-rule status;
- authorization or prohibition of further generality engineering.

Stage 12 must consume this certificate.

## Version impact

This refinement:

- adds no canonical Stage;
- removes no Stage;
- changes no `GO / CONDITIONAL GO / NO-GO` semantics;
- changes no normal routing;
- preserves theory-freeze and rollback architecture;
- strengthens Stage 7.5A evidence requirements and Stage 12 handoff discipline.

Under `docs/VERSIONING_POLICY.md`, this is a backward-compatible **MINOR** refinement and is classified as prospective **v2.4**.

## Files affected

Canonical / operational changes:

- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`
- `templates/STAGE_12_JOURNAL_POSITIONING.md`
- `checklists/PORTABILITY_FALSIFICATION_CHECKLIST.md`

Documentation / navigation changes:

- `README.md`
- `docs/VERSIONING_POLICY.md`
- this record.

## Governing rule

The core rule introduced by this refinement is:

> **Certify the strongest theory the economics actually supports first; choose the journal that fits that certified strength afterward.**
