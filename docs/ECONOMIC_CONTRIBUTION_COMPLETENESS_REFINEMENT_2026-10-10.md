# Economic contribution / question-completeness hardening — design and regression record

**Date:** 2026-10-10 JST  
**Workflow proposal:** v2.9 MINOR candidate (not tagged / not released by this file)  
**Source case:** `ryotamatsuki/industrial-policy-composition-regional-value-chains`, JRS manuscript `1758654`  
**Source decision:** 2026-10-10 JRS desk rejection, signed Dr. Florian Mayneris; the decision was an editorial assessment without external review and was **not** a determination of mathematical invalidity.

## 1. Observed failure and evidence (do not rewrite past decisions)

The original paper showed an exact, positive-measure region of inefficient duplication of industrial-policy priorities in a fixed-capacity, two-region model. Its mathematical proofs and novelty restrictions survived Stage-11 checks, but an actual editor judged the economic-policy question too abstract and asked what **practically should or could be done** to internalize the identified spillover.

The prior project records themselves contained material warnings:

- [Stage 11 report](https://github.com/ryotamatsuki/industrial-policy-composition-regional-value-chains/blob/main/docs/STAGE11_REPORT.md): recognized that the underlying fiscal externality was familiar, the contribution could be too narrow, and no implementation theorem was present; classified this as a **journal-positioning** risk instead of an independently tested completeness issue.
- [Stage 12 positioning](https://github.com/ryotamatsuki/industrial-policy-composition-regional-value-chains/blob/main/docs/STAGE12_JOURNAL_POSITIONING.md): selected JRS based partly on the ability to publish the certified, compact model without expanding theory; prohibited new transfers/instruments merely to match journal prestige.
- [Stage 13 report](https://github.com/ryotamatsuki/industrial-policy-composition-regional-value-chains/blob/main/docs/STAGE13_REPORT.md): correctly confined the institutional bridge to analogues and limits, noting that no instrument or institutional prescription was introduced.
- [Decision record](https://github.com/ryotamatsuki/industrial-policy-composition-regional-value-chains/blob/main/submission/jrs/EDITORIAL_DECISION_2026-10-10.md): records the actual letter and separates the editor's comment from interpretation.

The old workflow correctly enforced mathematical validity, theorem scope, and no prestige-driven complexity. **The missed distinction** was that “the scope is honestly limited” is not equivalent to “the stated economic or policy question has been answered enough to warrant a full field paper.”

## 2. Desired behavior

Before Theory Freeze, ask two logically separate questions:

1. **Truth/novelty:** Is the formal result sound, properly scoped and nonabsorbed by existing theorems?
2. **Contribution/completeness:** What consequential question does it answer, why would a skeptical field editor publish it, and what material part of the *stated* question is left unanswered?

For a policy-facing research claim, diagnose **WHY**, define **SHOULD** under the feasible welfare benchmark, and investigate **COULD** under realistic contracts/incentives/finance/information — **or** justify why a diagnosis-only theorem is independently valuable. No universal intervention, empirical paper, arbitrary model growth or forced generalization.

A bounded comparison of baseline-only, one *meaningful* extension and reframe/note is required **only when a material gap is diagnosed**. Treat the extension as a hypothesis pending standard mathematics/novelty/institution audits. Research with negative or narrow results remains eligible where independently important.

## 3. Stage integration (same numbering and routing)

| Stage | Amendment | Failure prevented |
|---|---|---|
| 6 | Provisional editor-facing contribution case, unanswered-question classifications, bounded alternatives | Novelty PASS mistaken for full-paper significance |
| 7 | WHY–SHOULD–COULD feasibility table when applicable | Planner optimum silently used as actionable instrument |
| 7.5 | Mandatory independently challenged completeness closeout for GO | Essential gap deferred as mere journal risk |
| 8 | Store the Stage-7.5 audit with canonical theory scope | Theory Freeze erases unresolved policy boundary |
| 11 | Independent editor rejection and early-gate regression attack | Discussion disclaimer incorrectly marked as a cure |
| 12 | Journal-facing test of diagnosis-only versus implementability expectations | Venue ranked by scope and compactness alone |

All ordinary `GO / CONDITIONAL GO / NO-GO` meanings and routes remain; adding substantive theory still reopens Stage 3/4/4A/6 and all affected downstream gates.

## 4. Regression scenarios (acceptance criteria for the refinement)

### R1 — JRS-like policy paper: formerly missed

**Input:** Two-region policy-composition model has certified exact duplication equilibrium and welfare comparison; closest literature contains common fiscal spillovers; no practicable implementation model; stated title and research question claim to explain **how industrial policy should work**, not only why decentralized choices differ.

**Old behavior:** Stage 11 flags narrow contribution and absent implementation as a journal-fit risk; Stage 12 chooses a fitting venue; Stage 13 notes implementation is unmodeled and still passes.

**Required new behavior:** Stage 6 logs possible `ESSENTIAL FOLLOW-UP`, Stage 7 separates WHY–SHOULD–COULD, Stage 7.5 refuses an unreasoned full-paper GO; either establish a strong independently publishable *diagnostic-only* case, run a **bounded** extension through the earliest correct stages, or choose a narrower claim/note. A later editor's rejection is not proof that any proposed extension is novel.

### R2 — Pure mathematical economics theorem: should NOT be blocked mechanically

**Input:** Deep new equilibrium/existence result answering the stated pure-theory question; no policy instrument or empirical counterpart.

**Required behavior:** Policy implementation is `NOT APPLICABLE`; a defensible economic/theoretical consequence can pass Stage 7.5.

### R3 — Substantive correction: should NOT be forced to invent mechanisms

**Input:** Demonstrated flaw in a source theorem with a corrected welfare or equilibrium conclusion and proven significance.

**Required behavior:** Judge source-claim correction, novelty and substantive consequence. No required new instrument/theorem unrelated to that correction.

### R4 — Cosmetic policy subsidy: should NOT pass by complexity

**Input:** Adding a transfer to a classic spillover game yields only an immediate corollary of established fiscal-federalism results.

**Required behavior:** Fail novelty/absorption or classify as contextual illustration, not an independent headline result. Preserve original narrow model or reframe if the extension lacks economic contribution.

### R5 — Editor disagreement after legitimate freeze

**Input:** An editor later requests policy implementation from a well-justified, explicitly diagnostic-only paper.

**Required behavior:** Record new evidence and re-evaluate contribution/fit; no automatic claim the old freeze was invalid or that publication required a different theorem. A model change starts a new controlled revision branch.

## 5. Evidence and versioning

Evidence standard: source letter, exact stage artifacts and accessible bibliographic/model-level prior art, not an AI impression. When Stage 11 flags an `EARLY-GATE MISS`, identify which Stage-7.5 question/checklist field should have prevented it, and preserve the original historical verdict. Do not claim an external desk rejection confirms any new model or predicted acceptance probability.

**Version impact:** MINOR (v2.9 candidate) under `docs/VERSIONING_POLICY.md`: existing Stage numbering, canonical routing/verdict semantics, freeze and rollback behavior, and one-diagnosed-fix discipline remain unchanged. There is a newly mandatory **check inside Stage 7.5**, not a new Stage. This file does not create a release tag.

## 6. Open limitations

- No workflow can guarantee a journal editor will deem a particular theorem important.
- “What could be done” is a context-dependent test, not a universal policy requirement.
- The JRS letter identifies publication-fit concerns, not a proof that the proposed interregional-transfer extension adds sufficient novelty.
- Applying updated rules to an older project requires a **new** auditable reassessment; do not retroactively modify old certification/Stage decisions.
