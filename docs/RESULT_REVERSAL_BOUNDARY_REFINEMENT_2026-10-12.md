# Result-Reversal and Sharp-Boundary Discovery Refinement — 2026-10-12

## Status / release semantics

**Unreleased, post-v2.9 MINOR-class refinement.** This document records the change prepared for `main` via PR review. It is not a claim that `v2.10` was tagged or published. The stable `v2.9` tag and prior release audits remain unchanged.

Per `docs/VERSIONING_POLICY.md`, the change introduces backward-compatible research-discovery and verification checks **inside existing Stages**. It does not alter their identities, canonical `GO / CONDITIONAL GO / NO-GO` meanings, normal routing, freeze meaning or one-diagnosed-fix discipline.

## Problem

Question-first frontier search correctly rejects a cosmetically new application or ad hoc parameter added after a rejected result. But it can wrongly rule out important **new results answering the same question**, including reversal of known comparative statics or welfare rankings, unexpected nonmonotonicity, sharp domains for existing theorems, impossibility/counterexample results, and unexpectedly broad robustness.

A reversal must not be pursued as spectacle; the objective remains new **economic learning beyond an exactly characterized prior result**.

## Changes by existing Stage

- **Stage 2:** reproduce primary-source predecessor theorem scope, welfare/selection comparison and search both author limitations and minimal meaningful reversal/boundary possibilities; audit later/parent theorems.
- **Stage 3:** allow same-question/new-result candidates; pre-register competing no-reversal hypotheses, smallest justified change, nested-recovery restriction, candidate proposition and finite kill test.
- **Stage 4:** recover predecessor, solve changed full equilibrium, establish exact counterexample or theorem, test boundaries and retain no-reversal findings. Do not transfer invalid regular formulas or treat solver failure as evidence.
- **Stage 4A / 7.5A:** existing independent mathematics, equilibrium, proof scope, quantifier, benchmark and portability controls apply to every claimed reversal, impossibility or robust invariance.
- **Stage 6:** map actual certified claim into general parent theorems, later counterexamples and prior assumptions. Different welfare objects or equilibrium selections are not identical-domain reversals.
- **Stage 11:** independently repeat benchmark recovery, contrary-case falsification, economic-assumption and no-manufactured-paradox tests.

Companions: `checklists/RESULT_REVERSAL_BOUNDARY_CHECKLIST.md`, Stage-2/3/4/6/7.5A/11 templates, `templates/FRONTIER_OPPORTUNITY_REGISTER.md` Section C2 and `checklists/FRONTIER_OPPORTUNITY_CHECKLIST.md`.

## Exclusion and success examples (diagnostic only)

- **Fails:** a single simulation with a negative cross-term deliberately chosen for the desired sign; a supposed welfare-ranking reversal comparing private surplus to social surplus; a counterexample outside the published theorem's assumptions; a textbook Stag Hunt reversal obtained by renaming the players as municipalities.
- **May merit examination:** an exact minimal counterexample refuting a genuinely broad prior claim on the original domain; a new necessary-and-sufficient condition explaining why a prior sign becomes positive or negative on economically meaningful open regions; a strengthened general theorem showing that an influential apparent reversal is impossible for a broad defensible class.
- **Not mandatory:** an actual sign reversal. A valid impossibility or surprising robustness theorem may be equally consequential.

## Integration checks

- [ ] Stage numbering, `Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8` route unchanged.
- [ ] The canonical hierarchy `GOVERNANCE → PIPELINE → TEMPLATE → CHECKLIST` remains intact.
- [ ] Stage 2 and 3 permit same-question theorem improvements, not only new questions.
- [ ] Stage 4 preserves predecessor reproduction, cross-regime global/continuation checks and negative findings.
- [ ] Stage 6 and 11 do not mistake an assumed/renamed or already-known effect for novelty.
- [ ] Stage-7.5A claim-scope controls and independent current-paper/next-paper verdicts remain active.
- [ ] Referenced checklist, source register and templates exist and contain operational instructions.
- [ ] No historical tag, v2.9 release audit or published release statement changed.

These boxes are intended for an integration audit, not retrospective self-certification. Any defects should be fixed on the PR branch before merging.
