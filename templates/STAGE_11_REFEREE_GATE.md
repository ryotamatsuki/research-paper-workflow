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

For sequential/game-theoretic papers, independently attack the completeness of downstream continuations rather than merely re-running the author's equilibrium solver.

## 3. Canonical inputs

The current full draft and theory freeze are the object under attack. Do not presume acceptance.

## 4. Allowed changes

You may recommend exposition fixes, additional verification, or an approved robustness exercise. Any proposed substantive theory change must trigger formal theory-change control and reopening of affected stages.

## 5. Prohibited changes

Do not respond to every criticism by adding an extension. Do not bury fatal objections in a long list of minor comments.

Do not treat a green CI run, successful reproduction of the author's numbers, or repeated execution of the same solver as independent equilibrium validation.

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

For sequential/game-theoretic models, additionally:

- apply `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md`;
- select at least one material upstream deviation/off-path history and reconstruct the downstream allocation/payoff from primitives without calling the manuscript's candidate equilibrium solver;
- deliberately search for a large finite deviation that exits the regular/interior branch;
- inspect every place where code returns `None`, NaN, invalid, exception, or nonconvergence and verify that no such outcome is treated as an unprofitable deviation;
- challenge pure-strategy continuation existence and multiplicity where the model permits discontinuous active-set/order/participation changes;
- verify that labels such as `global`, `whole-domain`, `whole-circle`, or `SPNE` match the actual economic domain audited.

For every serious attack state:

`Attack → Severity → Evidence → Can the paper answer now? → Required fix → Does the fix reopen theory?`

## 7. Evidence requirements

Referee attacks must cite exact model assumptions, manuscript passages, prior papers, or verification failures. Avoid generic complaints with no target.

For equilibrium attacks, reproducing the manuscript's reported equilibrium path is not enough. The audit must distinguish on-path numerical correctness from off-path continuation validity.

## 8. Verification protocol

Re-run key symbolic and numerical gates where attacks concern mathematics. Re-open closest papers where attacks concern novelty. Check source evidence for institutional attacks.

At least one high-stakes mathematical attack should use an implementation or direct-payoff reconstruction that is logically independent of the code path used to generate the headline result, when feasible.

## 9. Kill tests

Classify each attack as:

- `FATAL`
- `MAJOR BUT FIXABLE`
- `MINOR`

A `FATAL` attack on the core contribution blocks submission preparation. If the only fix changes the core mechanism, reopen the appropriate earlier stage rather than patching the manuscript.

For an SPNE/sequential claim, a material off-path continuation that is `UNRESOLVED` or `NUMERICAL_FAILURE` is at least a major correctness blocker and is fatal to submission readiness until resolved.

## 10. Success criteria

No unresolved fatal attack on the main contribution; major fixes are bounded and do not require uncontrolled theory drift.

For sequential/game-theoretic papers, continuation completeness must independently survive the hostile audit, with no material solver failure silently excluded from deviation evaluation.

## 11. Failure criteria

Return to an earlier stage if novelty, identification of the mechanism, mathematical validity, continuation completeness, or institutional coherence remains fatally vulnerable.

## 12. Required final output

1. Executive referee-gate verdict
2. Referee A: novelty/mechanism report
3. Referee B: assumptions/math report
4. Referee C: welfare/institution report
5. Referee D: journal/exposition report
6. Independent equilibrium/continuation re-audit, where applicable
7. Solver-failure/unresolved-continuation ledger, where applicable
8. Consolidated severity table
9. Required fixes
10. Theory-change implications
11. Resolved vs unresolved attacks
12. Verdict and Stage 12 contract

## 13. Final verdict

Choose one:

- `GO TO JOURNAL POSITIONING`
- `CONDITIONAL GO` — bounded major fixes
- `REOPEN EARLIER STAGE / NO-GO`

## 14. Next-stage contract

Stage 12 selects a journal for the actual surviving contribution. It must not reshape the result to fit a preferred journal.
