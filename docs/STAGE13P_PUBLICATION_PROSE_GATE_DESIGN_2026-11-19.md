# Stage 13P — Independent Publication Prose & Exemplar Benchmarking: Design and Version Impact

**Date:** 2026-11-19 JST  
**Status:** PROPOSED in Draft PR; **not** released, merged, or included in immutable `v3.0`.  
**Version classification:** **MAJOR v4.0 candidate** under `docs/VERSIONING_POLICY.md`: mandatory new Stage and canonical route `Stage 13 → Stage 13P → Stage 14`.

## 1. Observed failure and causal diagnosis

A theoretically and computationally audited economics paper can nevertheless carry into a proposed journal submission language suited only to the author's internal workflow: “Stage-4A certification record”, “Stage-11 independent reconstruction”, “hostile-audit counterexample”, CI/regression history in the body, and weakened contribution self-assessments such as “Its possible value is …”. These are **publication-prose issues**, not proofs of mathematical failure or scientific priority, and they can survive manuscript-building exemplar analysis and a simulation of scientific referee attacks.

The Green Subsidies project exposed this gap after earlier Stage 10A/11/13 processes. A favorable theoretical referee report, a correctly compiling PDF and an existing published-paper writing blueprint **do not guarantee that the actual final manuscript reads like a polished journal article**. Later edits may even reintroduce internal wording after a past editorial PASS.

## 2. Alternatives and why a separate gate is selected

| Design | Advantage | Failure in this case | Choice |
|---|---|---|---|
| Add banned-word scan to Stage 14 only | Cheap and reliable for exact strings | Cannot detect rhetorical self-defensiveness, unnatural sentences, incoherent section transitions or underdeveloped economic intuition; generates false positives for actual game stages | Supplemental regression, **not sufficient** |
| Reuse Stage 11 mathematical/referee audit | Existing independent reviewer machinery | Reviewer sees research evidence/history; high stakes math and novelty overshadow prose quality; post-review edits invalidate early prose judgment | Keep scientific Stage 11 distinct |
| Strengthen Stage 13 writer's self-review only | Integrated drafts readily editable | Same agent knows intended meaning, may excuse unnatural meta-language and score its own changes | Needed for drafting, **not independent certification** |
| Add independent Phase A + exemplar Phase B Stage 13P | Cold-reader independence, full-text comparator discipline, specific evidence and source/PDF binding | Adds cost and a major new routing barrier | **Selected**, with bounded reuse of Stage10A verified sources |

Stage 13P does not eliminate Stage 10A: **10A designs** writing from fully read exemplars; 10B writes; 11 attacks scientific and editorial claims; 12 refreshes comparator relevance; 13 integrates and repairs; **13P tests whether the actual complete article attained publication-standard prose**; 14 verifies the accepted text and submission compliance.

## 3. Phase A → Phase B: why this order matters

**Phase A** is a “first editor” simulation. The reviewer reads only the full manuscript and a neutral target/article-type descriptor. It must independently reconstruct the actual economic question, inference and bounds, produce the strongest credible *communication-only* rejection, and locate unnatural passages across all pages and appendices. The report is **frozen before comparator release**. Access logs identify any hidden contamination; a new model/session alone never counts as proof of blindness.

**Phase B** evaluates the actual manuscript against the **Stage 10A verified complete texts**, after Stage 12 journal fit refresh. Per role, exact exemplar and manuscript locations support STRONG/ADEQUATE/WEAK descriptions, writing moves, and bounded repairs. A human editor can judge style differently: these are evidence-led editorial judgments, not objective probabilities or "top journal level" certificates. Do not mimic copyrighted language or borrow prior papers' scientific results.

After corrections, an **independent second cold reader** checks the revised full article. This prevents the editing agent from declaring its own material criticisms resolved.

## 4. Scope preservation and accountability

This is a prose-only gate. It may improve clarity and flow but cannot weaken or enlarge frozen hypotheses, theorem quantifiers, counterexamples, source priority, formal proof coverage, causal interpretation, benchmark welfare or quantitative signs. It must not erase substantive negative evidence as “defensive style”. Anything requiring changed science returns upstream.

Author-level responsibility and AI manuscript-use disclosure remain separate. The AI reader is not external peer review; no metric or mere clean build establishes human sign-off or acceptance prospects.

## 5. Hard stop, evidence and SHA binding

Required artifacts:
1. `PROSE_REFEREE_REPORT.md` — original Phase A and access log, time-stamped before Phase B.
2. `EXEMPLAR_PROSE_COMPARISON.md` — complete-source locators and role-wise ratings.
3. `PROSE_ISSUE_REGISTER.md` — issues and closure criteria.
4. `PROSE_REVISION_AUDIT.md` — before/after diffs and independent new cold read.
5. `STAGE13P_GATE_REPORT.md` — exact accepted **source SHA/PDF hash**, verdict and next-stage contract.

**GO** only if the paper has passed both phases, full-text source access and independent post-repair check, with no unresolved material defect. **CONDITIONAL GO** may name exactly one bounded remaining fix but **does not authorize Stage 14**. **NO-GO** routes to prose/exemplar stages or scientific stages as appropriate. Every post-GO text change invalidates the relevant clearance until independently rechecked; a material whole-paper rewrite requires fresh full-manuscript review.

## 6. Compatibility and rollout

- **v3.0 tag** is a historical immutable published interface; it is not edited, moved or represented as containing Stage 13P.
- The feature branch/Draft PR defines a **candidate v4.0 workflow**, not a new release. Existing v3.0 projects remain governed by their chosen release until the author **explicitly selects migration**.
- An adopting active project may carry forward valid Stage 8 mathematical freeze and Stage 10A verified full texts/Stage 12 comparators, provided actual acquisition and source version records exist. It must still run Stage 13P on the new **exact current manuscript**; a Stage 11 editorial PASS cannot be grandfathered as its substitute.
- Before any future release: independent PR review for routing consistency, all new templates/checklist navigation, seven canonical artifact tests, positive and negative regression cases, freeze/rollback compatibility, and main-branch readiness audit. Only after separate author authorization should a reviewed `main` commit receive a new immutable version tag and release.
- No automatic merge, model modification, paper submission or dashboard configuration change is authorized by this workflow-design PR.

## 7. Positive and negative routing acceptance tests

| Test | Expected |
|---|---|
| Stage 13 GO, 13P missing | **Block Stage 14** |
| 13P Phase A written after benchmark access and called blind | **NO-GO** unless rerun with defensible independent sequence |
| Stage 10A exemplar retrieved only from search abstract | **NO-GO Phase B**, bounded return to 10A source acquisition |
| Stage13P same paper reads fluently but original-workflow phrases remain | **MAJOR / no GO** |
| Human-writer-proposed style improvement drops essential theorem qualifier | **Stop; substantive rollback** |
| Stage13P issue closed only by same AI reviewer that edited it | **Not independently closed; no GO** |
| Stage13P GO at SHA X, Stage14 reads reworded SHA Y | **Reject stale GO / retest**, even if PDF page count matches |
| Author uses “Stage 1” correctly for game timing | **Not an issue** |
| Final text matches independently reviewed snapshot, all material prose findings closed | **GO to Stage 14**, not submission authorization |

See `examples/PUBLICATION_PROSE_REVIEW_REGRESSION.md` for detailed synthetic fixtures. They are not a substitute for the review of a real paper.
