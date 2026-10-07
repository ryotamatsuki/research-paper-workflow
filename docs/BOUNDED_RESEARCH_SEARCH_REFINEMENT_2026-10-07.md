# Bounded Research Search / Selection — Final Design Judgment

Date: 2026-10-07  
Reviewed baseline: stable v2.7, `91ecb3597183e4d420926cdc7b99744636e0690f`  
Decision: adopt an incremental **MINOR v2.8** refinement; retain the canonical architecture.

## 1. What was reviewed

The review used the latest GitHub `main`, Governance, the complete canonical pipeline, the versioning policy, v2.7 release/audit records, early-search/minimal-model/certification/novelty/welfare/freeze templates, and the relevant literature, novelty, numerical, theorem, and paper-specific inheritance checklists. There were no open PRs at baseline retrieval.

The source-inspired proposal was assessed against this actual workflow, rather than assuming it was a simple idea → model → proof → manuscript sequence.

## 2. OpenAI Math evidence and inference

Public source inspected on 2026-10-07: [OpenAI Math README](https://github.com/openai/math/blob/main/README.md) and its linked [Lean README](https://github.com/openai/math/blob/main/lean/README.md).

The README reports approximately 4,000 posed problems, 722 manuscripts in 372 families, significance-based aggregation/selection, and an unreleased internal model. It describes different verification maturities and explicitly does not claim that every result has a Lean formalization. These are source reports, not an independent validation of the mathematics.

The public description does not establish that the model generated the research questions itself, that every result received complete independent certification, or that the reported compute maps to the capabilities/cost of an ordinarily available model. The economics candidate-generation system below is a proposed adaptation, not a reproduction of a proven published economics workflow. No solve rate, publication probability, productivity multiplier, or candidate/draw quota is inferred from the catalogue counts.

## 3. Comparison with the actual v2.7 controls

| Proposed element | Existing v2.7 control | Final decision |
|---|---|---|
| Competing candidates | Stage 0: 3–8 distinct candidates; Stage 3: approximately 8–12, TOP 3, one Stage-4 model | Retain guidance; optional broader bank, structural deduplication, finite budget |
| Literature collision | Stage 2 whole-game audit; Stage 4 canonical form; Stage 6 parent-theorem absorption; Stage 11 regression attack | Retain; attach exact evidence/reading depth to serious candidate records |
| Discovery/verification separation | Governance 2.9, Stage 4A, Stage 7.5A, Stage 11 | Retain; record exposed inputs, independent path, discrepancies |
| Counterexample search | Stage 4/4A/7.5A; numerical/theorem/continuation checklists | Retain; clarify targeted coverage and finite stopping limits; no draw-count proof |
| Significance selection | Stage-0/3/4/6 kill tests and Stage 7.5 full-paper decision | Add short memo in 3/4, update against certified results in 6 before discretionary expansion |
| Related-result family | Claim/certificate registers, Stage-7 robustness, Stage-8 freeze and rollback | Add optional bounded dependency/disposition register; no automatic coverage inheritance |
| Negative branches | Governance 2.2 and pipeline 3.5/3.12 | Retain; link reasons and reopening conditions to candidate IDs |
| New-mechanism-only gate | Existing new-result/generalization routes; bespoke correction-route inheritance | Clarify substantive correction assessment; retain prior-art and certification requirements |
| Delayed full manuscript | Stage 8 freeze, Stage 9 production setup, Stage 10 manuscript | Retain; permit short provisional research memos earlier |

The material gap is the connection between candidate evidence, the next bounded investment, and related-result scope. Independent verification and prior-art kill are already strong existing controls; adding duplicate mandatory gates would increase burden without filling that gap.

## 4. Options not adopted

- Mandatory generation of 50–200 questions or 50–100 mechanisms regardless of the domain.
- Replacing the canonical Stage 0–15 structure with the proposed Stage 0–8 sequence.
- Deferring independent certification until after broad family expansion.
- Treating a new agent/model name, large random grid, or no-counterexample result as certification.
- Removing applicability-gated formal verification because the mathematics is economic rather than pure.
- Rejecting every correction or result in a known model for lack of a new mechanism.
- Automatically adding all extensions to one manuscript or treating every family member as a separate paper.
- Reopening frozen projects or changing their production artifacts solely because this workflow version advanced.

## 5. Version-impact judgment

MINOR under `VERSIONING_POLICY.md`: the change adds/refines evidence and selection criteria inside existing Stages and an optional-format companion record. It preserves Stage identities, normal/conditional/rollback routing, `GO / CONDITIONAL GO / NO-GO`, the one-diagnosed-fix rule, and theory/submission freeze meanings. It is not PATCH because the new evidence obligations are substantive.

A mandatory replacement Stage sequence, added canonical search/significance Stage, or moving Stage 4A behind expansion would require MAJOR. Those options are not adopted.

An existing Stage-8 template label omitted `PORTABILITY` from the Stage-7.5A certificate name. It is synchronized to the canonical full name without changing the certificate meaning or route.

## 6. Migration and practical evaluation

- New/broad Stage-0/3 searches use the applicable register content or equivalent existing records. Keep current candidate guidance and authorized project stop points.
- Active pre-freeze projects update contribution evidence at the next applicable Stage. Recover prior rationale only from existing evidence; missing history stays missing.
- Before discretionary Stage-7 exploration, use the Stage-6 memo and a finite purpose/budget. No extension quota applies.
- Frozen/submitted projects are not automatically thawed or required to regenerate a past portfolio. A newly discovered material defect uses existing rollback/change control. Future related work has its own authorized route.
- Paper-specific correction routes retain all claim-dependent certification/formal-verification obligations. Cosmetic corrections still fail the substantive contribution test.
- Evaluate the first use through actual distinct candidates, strongest prior-art comparisons, termination reasons, unresolved evidence, and work spent before a decision. Generated counts or finished-page counts alone do not establish improvement.

The weekly scouting automation and individual paper repositories are outside this canonical-document update. No new schedule or automatic research execution is introduced.
