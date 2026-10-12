# Frontier-Limitations and Next-Research-Question Refinement — Design and Regression Record
Date: 2026-10-12 JST
State: **unreleased v2.9-candidate minor amendment; proposed through feature branch/PR, not a new stable Git tag**.
Authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → stage templates → checklists.

## Problem / evidence motivating the change

The prior Stage-2/6 workflow was strong at checking whether an already-constructed theorem survived neighboring paper/model comparisons. It was weak at translating those source readings into **fresh, important, verifiably still-open economic questions**, including the limitations that authors themselves explicitly discuss in Abstract/Introduction/Conclusion and the gaps produced by comparing papers.

A completed symbolic proof, a novel-looking parameter threshold, and a high-quality submission package do not establish full-paper importance. Conversely, a well-founded `NO-GO` decision should retain the literature information as reusable research capital, not force the team to start the frontier search from zero. The specific Green Policy Competition sequence illustrates both issues: original cross-instrument derivative theorem was mathematically certified but later judged thin in field value; the no-transfer-cooperation pivot uncovered direct cooperative-subsidy asymmetric-R&D predecessors after extensive proof work. **These retrospective judgments remain historical; this refinement does not retroactively certify a new theme, relabel any old result as wrong, or edit either scientific repository.**

## Scientific design requirements

1. **Source fidelity:** For decisive papers, inspect Abstract/Introduction positioning, actual theorem, conditions and scope, Discussion/Conclusion limitations and future research. Attribute a problem to authors only when the source supports that exact claim, with page/section; otherwise mark it auditor-inferred or cross-paper synthesis. Missing full text is `NOT INSPECTED / UNRESOLVED`, not an invitation to speculate.
2. **Temporal closure:** Explicitly test forward citations, same-author follow-ups, adjacent-field/theorem parents and recent working papers at a stated literature cutoff. The frontier status is `RESOLVED / PARTIALLY RESOLVED / OPEN WITH EVIDENCE / UNRESOLVED`. `OPEN WITH EVIDENCE` is bounded literature status, not an impossible global proof of absence.
3. **Economics before feature design:** Each question must say which inference about incentives/equilibria/welfare/optimal policy hierarchy/organization would change relative to the strongest existing result. Propose a falsifiable theorem, counterexample, identification estimand, welfare ranking or classification, with minimum required model/data and strongest prior-theorem kill.
4. **Evidence maturity and scarce attention:** `HYPOTHESIS → LITERATURE-SCREENED → MODEL-TESTED → CERTIFIED`, or `KILLED`. These are research-status labels, not new canonical stage decisions. Up to three credible future questions, **including zero**, is preferable to forced ideation. Preserve stable IDs, deduplicate structurally and honor finite search budgets.
5. **Dual independent Stage-6/7.5 outputs:** The current paper receives its normal `GO/CONDITIONAL GO/NO-GO`. Future opportunities are a separate memo, even when the current paper is GO. A bright next idea does not rescue the current paper; a current NO-GO does not establish novelty or authorize the follow-up. Fresh author-selected objective + appropriate Stage 0/2/3 is required.
6. **Preserve legitimate contribution classes:** General equilibrium/existence theorems, important corrections, pure mathematics, negative results and intentionally diagnostic work may pass without policy instruments/data if substantively valuable. Do not demand manuscript expansion solely to generate a follow-up.
7. **No new Stage / compatible routing:** Stage numbering, v2.8 stable release, v2.9 candidate status, original GO/NO-GO meanings, rollback, one-diagnosed-fix discipline, Stage-4A/7.5A and theory freeze semantics are unchanged. **MINOR** per `docs/VERSIONING_POLICY.md`; if later merged/released, release manifests and tag must be handled separately.

## File-level implementation

- `GOVERNANCE.md`: §2.21 independent present-paper versus future-opportunity decisions, source attribution, time-resolved frontier status, author authorization.
- `THEORY_PAPER_RESEARCH_PIPELINE.md`: v2.9-candidate overview and mandatory Stage 2/3/6/7.5 clauses.
- `templates/STAGE_02_NOVELTY_GATE.md`: source-grounded stated limits, later studies, provisional question map.
- `templates/STAGE_03_MECHANISM_SEARCH.md`: choose research question before adding parameters; falsifier and expected learning.
- `templates/STAGE_06_NOVELTY_REKILL.md`: exact dual outputs and alternative question evidence even if current result is killed.
- `templates/STAGE_075_FREEZE_DECISION.md`: independent skeptical-editor recommendation and current-paper verdict.
- `checklists/LITERATURE_AUDIT_CHECKLIST.md` + `checklists/NOVELTY_KILL_CHECKLIST.md` + `checklists/ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md`: guard old failure modes.
- `checklists/FRONTIER_OPPORTUNITY_CHECKLIST.md`, `templates/FRONTIER_OPPORTUNITY_REGISTER.md`: source-location, later-solution, opportunity and decision records.
- `templates/RESEARCH_SEARCH_REGISTER.md`: companion bridge without duplicated bibliographic logs.
- `README.md`: navigation/status.

## Adversarial regression scenarios

| Case | Input / known threat | Required output | Prohibited failure |
|---|---|---|---|
| R1: Explicit but already solved future question | A close paper's conclusion says "consider asymmetric spillovers"; a later paper proves the corresponding general asymmetry result | `AUTHOR-STATED` gap marked `RESOLVED` or narrowly `PARTIALLY RESOLVED`; derivative question only if a different unabsorbed theorem is specified | Advertise author's 2025 future work as a presently open 2026 novelty |
| R2: No stated future work | A decisive paper states no explicit limitations in sections accessed | `NOT FOUND`, then a separately attributed `AUDITOR-INFERRED` or `CROSS-PAPER` opportunity if independently defensible | Invent a quote or attribute assistant speculation to authors |
| R3: Generic textbook decentralization corollary | Proposed "province vs national intervention" cutoff reduces to the standard spillover-internalization criterion after simple mapping | `KILLED` or narrow beyond-parent question with proved mapping; record parent class | Promote policy-relevant vocabulary as theorem novelty |
| R4: Current N1 paper NO-GO but new important question | A paper's current theorem is economically absorbed while a different policy-allocation boundary is plausible | **CURRENT NO-GO**; future Q1 marked `PROPOSED / NOT AUTHORIZED`, fresh Stage 0/2/3 and tests needed | Convert present-paper verdict to CONDITIONAL GO solely because Q1 sounds promising |
| R5: Pure theorem / substantive correction | Novel mathematically consequential equilibrium theorem is self-contained; no immediate policy implementation | Current-paper GO allowed when economics/theory significance genuinely defensible, with future opportunities optional | Force an ad hoc policy instrument or data study |
| R6: Source access insufficient | Only abstract accessible; no appendix or theorem pages; unresolved nearby working papers | `UNRESOLVED` plus acquisition/verification plan | Describe whole-game novelty or authors' future question as certified |
| R7: Search budget exhausted with no strong leads | All candidates are either solved, parent-theorem corollaries or impossible within resources | `NO DEFENSIBLE NEXT QUESTION FOUND IN SEARCH BUDGET`; preserve candidates and stop/revisit triggers | Generate 3 invented ideas or promise future research automatically |
| R8: Current paper GO and useful frontier still open | Certified narrow diagnostic theorem is field-important but a later generalization is unsolved | Preserve current GO and a separately proposed future question | Downgrade paper just because it cannot answer every next question |
| R9: Contract extension temptation | Current NO-GO and one can make novelty by adding transfers without a distinct predicted economic result | Kill as model complexity/known theorem; propose a **question** only if a new specific answer survives hostile parent mapping | Uncontrolled Stage-4 additions and silent refreeze |

## Static validation and remaining gates

Check unique scope markers in governance/pipeline, presence of all four Stage edits, two independent outputs and normal routing, author-versus-auditor evidence distinctions, later-work statuses, zero-candidate fallback, parent theorem attack, and v2.9-candidate unreleased disclosure. These are source/text **consistency checks only**, not evidence that this workflow has been field-tested on multiple real literature reviews or independently peer-reviewed. A real Stage-2-to-7.5 project run should later check whether the opportunity ledger is discriminating without creating excessive paperwork.

**Release status:** these source changes are v2.9-candidate only until a separately reviewed stable tag/release is issued. Merging the feature PR does not itself create that tag and does not retroactively change historical per-project verdicts.
