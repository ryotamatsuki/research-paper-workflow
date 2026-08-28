# Stage 11 — Robustness / Referee Attack Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as multiple hostile referees and an editor. Try to reject `[WORKING_TITLE]` before external review does.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Frozen theory: `[CANONICAL_MODEL]`
- Core mechanism: `[CORE_MECHANISM]`
- Main propositions: `[CURRENT_STAGE_RESULT]`
- Closest papers: `[CLOSEST_PAPERS]`
- Target journal: `[TARGET_JOURNAL]`
- Repository/manuscript: `[SOURCE_REPOSITORY]`

## 2. Stage objective

Identify fatal conceptual, mathematical, novelty, robustness, institutional, welfare, and journal-fit objections; require fixes only when they address a genuine vulnerability.

## 3. Canonical inputs

The current full draft and theory freeze are the object under attack. Do not presume acceptance.

## 4. Allowed changes

You may recommend exposition fixes, additional verification, or an approved robustness exercise. Any proposed substantive theory change must trigger formal theory-change control and reopening of affected stages.

## 5. Prohibited changes

Do not respond to every criticism by adding an extension. Do not bury fatal objections in a long list of minor comments.

## 6. Mandatory attack classes

Use `checklists/REFEREE_ATTACK_CHECKLIST.md` and explicitly test at least:

- classic-result attack;
- ad-hoc-assumption attack;
- result-built-into-assumption attack;
- no-new-mechanism attack;
- alternative-demand attack;
- alternative-contract/information attack;
- participation/corner/boundary attack;
- welfare-is-mechanical attack;
- institution-too-specific attack;
- external-validity/generality attack;
- numerical-not-proof attack;
- proof/notation inconsistency attack;
- wrong-journal / insufficient-contribution attack;
- exposition/claim-inflation attack.

For every serious attack state:

`Attack → Severity → Evidence → Can the paper answer now? → Required fix → Does the fix reopen theory?`

## 7. Evidence requirements

Referee attacks must cite exact model assumptions, manuscript passages, prior papers, or verification failures. Avoid generic complaints with no target.

## 8. Verification protocol

Re-run key symbolic and numerical gates where attacks concern mathematics. Re-open closest papers where attacks concern novelty. Check source evidence for institutional attacks.

## 9. Kill tests

Classify each attack as:

- `FATAL`
- `MAJOR BUT FIXABLE`
- `MINOR`

A `FATAL` attack on the core contribution blocks submission preparation. If the only fix changes the core mechanism, reopen the appropriate earlier stage rather than patching the manuscript.

## 10. Success criteria

No unresolved fatal attack on the main contribution; major fixes are bounded and do not require uncontrolled theory drift.

## 11. Failure criteria

Return to an earlier stage if novelty, identification of the mechanism, mathematical validity, or institutional coherence remains fatally vulnerable.

## 12. Required final output

1. Executive referee-gate verdict
2. Referee A: novelty/mechanism report
3. Referee B: assumptions/math report
4. Referee C: welfare/institution report
5. Referee D: journal/exposition report
6. Consolidated severity table
7. Required fixes
8. Theory-change implications
9. Resolved vs unresolved attacks
10. Verdict and Stage 12 contract

## 13. Final verdict

Choose one:

- `GO TO JOURNAL POSITIONING`
- `CONDITIONAL GO` — bounded major fixes
- `REOPEN EARLIER STAGE / NO-GO`

## 14. Next-stage contract

Stage 12 selects a journal for the actual surviving contribution. It must not reshape the result to fit a preferred journal.