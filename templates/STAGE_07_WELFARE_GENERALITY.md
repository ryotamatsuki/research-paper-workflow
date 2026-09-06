# Stage 7 — Welfare, Generality & Institutional Validation

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a welfare economist, institutional auditor, and field referee. Determine whether the surviving certified mechanism matters beyond firm profit and one motivating case.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Surviving mechanism: `[CORE_MECHANISM]`
- Canonical model: `[CANONICAL_MODEL]`
- Surviving propositions: `[CURRENT_STAGE_RESULT]`
- Stage-4A theorem certificates: `[STAGE_4A_CERTIFICATES]`
- Closest papers: `[CLOSEST_PAPERS]`
- Motivating institutions/sources: `[SOURCE_FILES]`

## 2. Stage objective

Derive welfare rigorously, compare private and social decisions, validate key primitives against evidence, test whether the mechanism generalizes without changing the theory, classify the actual scope of robustness claims, and identify how each surviving headline result should later be communicated most efficiently.

## 3. Canonical inputs

Model and contribution claims surviving Stage 6 are frozen for this stage. Institutional evidence may validate or weaken interpretation but may not silently alter primitives.

## 4. Allowed changes

You may add welfare notation, explicitly defined planner benchmarks, or empirical predictions implied by the frozen model. You may classify existing verified results by their appropriate exposition vehicle. You may not add a new strategic mechanism merely to create a more attractive result, figure, or table.

## 5. Prohibited changes

- no triangular CS shortcut when the utility system allows exact CS;
- no treating transfers as social costs unless they are real resource costs in the model;
- no `first best` label without writing the planner's objective and full feasible choice set;
- no policy claim outside the modeled margin;
- no converting suggestive institutional evidence into proven fact;
- no “generality” based on relabeling industries only;
- no upgrading numerical robustness into proof;
- no upgrading a baseline functional-form result into a generic theorem;
- no inventing a numerical illustration or visual pattern not already implied by verified theory.

## 6. Mandatory tasks

1. Derive exact consumer surplus from the model's utility/demand system.
2. Derive producer surplus and total welfare; distinguish transfers from real costs.
3. Verify welfare identities symbolically where possible.
4. For every planner benchmark, write explicitly:
   - planner objective;
   - complete choice/instrument set;
   - technology/information/commitment constraints;
   - any fixed allocation or restricted policy margin.
5. Label each benchmark exactly as `first best`, `constrained first best`, `second best`, `fixed-allocation benchmark`, `restricted-instrument optimum`, or another precise term. Reserve `first best` for the unrestricted relevant planner problem.
6. Compare private and social thresholds/choices using consistent population, outside options, feasibility, and accounting.
7. Identify under-/over-provision, premature/excessive entry/exit, or organizational misallocation.
8. Verify core institutional primitives using primary sources where feasible.
9. Label each institutional link as `ESTABLISHED`, `SUGGESTIVE`, `UNVERIFIED`, or `CONTRADICTED`.
10. Test generality across at least two genuinely different settings without changing the mechanism.
11. For every generality/robustness statement, classify it as:
   - `BASELINE FUNCTIONAL FORM`;
   - `RESTRICTED FUNCTION CLASS`;
   - `SUFFICIENT-CONDITION THEOREM`;
   - `NUMERICAL ROBUSTNESS ONLY`;
   - `CONJECTURED GENERALITY`;
   - `GENERAL THEOREM`.
12. If a broad function class is contemplated, record the exact shape/derivative restrictions believed necessary. Do not declare the broad theorem here unless already proved/certified.
13. Derive empirical predictions or comparative statics that could discipline the model.
14. Perform a **result-to-exposition triage** for every surviving headline result. Assign theorem/proposition, figure, table, numerical illustration, or concise prose and record why. Flag thresholds, non-monotonicity, regime changes, benchmark separation, welfare decomposition, or multi-parameter scope patterns for visual/table consideration when useful.

The Stage-7 triage is planning, not a mandate to create graphics before theory freeze. There is no minimum figure quota.

## 7. Evidence requirements

Primary sources first for institutional claims. Keep model implications separate from observed facts. Every welfare benchmark must be traceable to an explicit optimization problem. Every claimed robustness/generalization level must be traceable to the proof/evidence actually available.

## 8. Verification protocol

Use exact symbolic checks for CS/welfare identities and threshold comparisons where feasible. For parameter-dependent signs, derive conditions or search systematically for counterexamples after analytic work.

For benchmark language, mechanically compare the planner's feasible choice set with the decentralized game's endogenous/fixed margins.

For generality claims, identify possible admissible counterexample functions/parameter regions for Stage 7.5A rather than assuming a convenient baseline extends automatically.

For exposition triage, verify the proposed vehicle does not imply a stronger result than the certified theorem.

## 9. Kill tests

Downgrade or kill the branch if:

- welfare differences are only transfers;
- the private/social wedge disappears once accounting is correct;
- a benchmark called `first best` actually fixes a relevant planner choice without qualification;
- the core primitive lacks institutional or theoretical defense;
- the motivating institution contradicts the assumed mechanism;
- generality requires adding new assumptions in every application;
- a broad theorem is inferred only from one parametric baseline or numerical grid;
- policy conclusions require an instrument absent from the model;
- the only way to make the result visually interesting is to add an unverified exercise or strengthen the claim beyond certified theory.

## 10. Success criteria

The mechanism should yield a coherent welfare implication and be defensible beyond a single institutional label. Benchmarks must be defined exactly. Every material robustness/generality claim must have an evidence-classification ready for Stage 7.5/7.5A. Every surviving headline result must have a candidate exposition vehicle or an explicit reason for theorem/prose-only treatment.

## 11. Failure criteria

Return `NO-GO` or recommend a research note if the result is correct but institution-specific, welfare-trivial, benchmark-confused, or too narrow for the intended contribution.

## 12. Required final output

1. Executive welfare/generality verdict
2. Exact CS and welfare derivation
3. Planner-objective/choice-set register
4. Benchmark-definition table
5. Private vs social decision map
6. Welfare propositions / thresholds
7. Institutional evidence table
8. Generality/robustness evidence-classification table
9. Empirical predictions
10. Result-to-exposition triage table
11. Policy scope and limits
12. Candidate counterexample targets for Stage 7.5A
13. Remaining fatal/major concerns
14. Verdict and Stage 7.5 contract

The result-to-exposition triage table should minimally contain: `headline result`, `economic object`, `candidate vehicle`, `why this vehicle`, `verified source`, and `Stage-10 action`.

The generality table should minimally contain: `claim`, `baseline form/class`, `evidence type`, `assumptions used`, `current maximum defensible scope`, and `Stage-7.5A attack target`.

## 13. Final verdict

Choose one:

- `GO TO STAGE 7.5`
- `CONDITIONAL GO` — one unresolved welfare/institutional blocker
- `NO-GO`

## 14. Next-stage contract

Stage 7.5 is a full-paper value decision. No extensions are permitted there. Carry forward the exact planner/benchmark register and baseline-vs-robustness-vs-general-theorem classification so that Stage 7.5A can independently attack quantifiers and benchmark terminology before Stage 8 freeze.
