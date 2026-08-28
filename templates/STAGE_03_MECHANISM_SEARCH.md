# Stage 3 — Candidate Mechanism Search

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a research director selecting mechanisms, not features. Competing explanations must be judged against prior art, tractability, welfare content, and referee risk.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Core question: `[CORE_RESEARCH_QUESTION]`
- Surviving literature gap: `[CORE_MECHANISM]`
- Closest papers: `[CLOSEST_PAPERS]`
- Known blockers: `[KNOWN_BLOCKERS]`
- Target journal family: `[TARGET_JOURNAL]`

## 2. Stage objective

Generate and compare genuinely different mechanisms that could answer the research question, then select a small number for minimal-model testing.

## 3. Canonical inputs

Stage 2 novelty findings are binding. Killed contribution claims cannot be restored by renaming.

## 4. Allowed changes

You may propose alternative primitives, timing, strategic margins, or state variables, provided each proposal has a clear economic reason and is assessed separately.

## 5. Prohibited changes

Do not treat the following as mechanisms by themselves:

- adding another heterogeneity parameter;
- adding another channel/player with no strategic feedback;
- adding a fixed cost solely to generate a threshold;
- adding dynamics solely to obtain history dependence;
- adding multiple extensions at once.

## 6. Mandatory tasks

When the search space is broad, generate approximately 8–12 candidates. For every candidate state:

1. one-sentence mechanism;
2. strategic feedback loop;
3. endogenous margins;
4. minimum players/timing;
5. minimum new primitive relative to the audited model;
6. closest prior-art threat;
7. expected nontrivial theorem/threshold/reversal;
8. welfare content;
9. institutional or empirical interpretation;
10. tractability risk;
11. likely fatal referee attack.

If scoring candidates, define weights ex ante. Suggested dimensions: novelty, mechanism clarity, closest-paper survival, tractability, welfare, institutional relevance, empirical bridge, and journal fit.

Select at most a TOP 3 for deep dives. Identify the single preferred minimal candidate if possible.

## 7. Evidence requirements

Candidate novelty must be grounded in Stage 2 evidence. If a candidate introduces a new literature family, perform a targeted mini-search before ranking it highly.

## 8. Verification protocol

No full algebra is required, but perform enough reduced-form or sign reasoning to test whether the proposed feedback loop is internally coherent. Flag candidates whose desired effect is built directly into an assumed payoff.

## 9. Kill tests

Reject a candidate when:

- the strategic loop collapses when written explicitly;
- the outcome is mechanically assumed;
- a close paper already contains the same loop;
- the minimum model requires many unrelated additions;
- the only result is a monotone comparative static with no trade-off;
- welfare content is absent and the result is pure relabeling.

## 10. Success criteria

At least one candidate must have a clear economic loop, a minimal implementable model, and plausible model/proposition-level distance from the closest literature.

## 11. Failure criteria

Return `NO-GO` if all credible candidates are known, trivial, or require uncontrolled complexity.

## 12. Required final output

1. Executive mechanism-search verdict
2. Candidate table
3. Candidate scores, if used
4. TOP candidates
5. Why rejected candidates fail
6. Preferred minimal mechanism
7. Exact Stage 4 model skeleton
8. Candidate propositions to kill-test
9. Verdict and next-stage contract

## 13. Final verdict

Choose one:

- `GO TO MINIMAL MODEL`
- `CONDITIONAL GO` — one unresolved mechanism choice
- `NO-GO`

## 14. Next-stage contract

Stage 4 must test one minimal candidate. Freeze all ingredients not required for that mechanism.