# Stage 5 — Mechanism Hardening

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a mechanism-hardening lead. Repair exactly the weakness exposed by Stage 4; do not use complexity to rescue a desired result.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Previous Stage 4 result: `[CURRENT_STAGE_RESULT]`
- Previous failure: `[KNOWN_BLOCKERS]`
- Allowed modification: `[ALLOWED_CHANGES]`
- Everything else: `FROZEN`
- Closest papers: `[CLOSEST_PAPERS]`

## 2. Stage objective

Determine whether one precisely diagnosed modification makes the mechanism coherent without turning the project into a known model or a feature bundle.

## 3. Canonical inputs

Use the Stage 4 model and negative/conditional result as the baseline. Quote the exact blocker before changing anything.

## 4. Allowed changes

Only `[ALLOWED_CHANGES]`. If the blocker cannot be addressed with one change, stop and return to mechanism selection rather than adding multiple margins.

## 5. Prohibited changes

- simultaneous addition of dynamics, geography, bargaining, new channels, multiple manufacturers, and heterogeneity;
- changing demand/utility merely to obtain a sign;
- adding transfer instruments solely to implement the desired outcome;
- reopening assumptions unrelated to the diagnosed blocker.

## 6. Mandatory tasks

1. Restate the exact Stage 4 failure.
2. Explain why the proposed modification addresses that failure economically.
3. State the smallest revised model.
4. Re-solve only the affected equilibrium blocks, then re-verify the full equilibrium.
5. Compare the revised result directly with the Stage 4 baseline.
6. Test whether the new ingredient creates the result mechanically.
7. Search the literature family associated with the new ingredient before claiming progress.
8. Identify what is genuinely new after the modification, if anything.

## 7. Evidence requirements

The added primitive must have either a clear microfoundation, institutional support, or a recognized theoretical rationale. Label any remaining modeling assumption explicitly.

## 8. Verification protocol

Re-run all symbolic, feasibility, participation, welfare, and numerical checks affected by the change. Do not rely on the Stage 4 verification for altered equations.

## 9. Kill tests

Return `NO-GO` if:

- the revised model is simply a standard known model from another literature;
- the new assumption directly imposes the desired result;
- the original blocker remains;
- a second unrelated modification is needed before any nontrivial result appears;
- the only gain is more complicated algebra.

## 10. Success criteria

The change must solve the diagnosed deficiency and reveal a coherent mechanism that still has plausible novelty.

## 11. Failure criteria

If the single permitted change cannot rescue the mechanism on economic grounds, terminate this branch or return to Stage 3 with a new candidate mechanism.

## 12. Required final output

1. Previous failure
2. One allowed modification
3. Revised model block
4. Re-derived equilibrium/results
5. What changed vs Stage 4
6. New artefact risks
7. New closest-literature threats
8. Surviving propositions
9. Remaining blocker
10. Verdict and next-stage contract

## 13. Final verdict

Choose one:

- `GO TO NOVELTY RE-KILL`
- `CONDITIONAL GO` — one remaining blocker only
- `NO-GO`

## 14. Next-stage contract

If `GO`, freeze the hardened mechanism and send the actual resulting propositions—not the intended setup—to Stage 6.