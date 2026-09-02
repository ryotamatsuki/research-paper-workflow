# Theory Paper Research Pipeline

Version: v1.1

## 1. Purpose

This document defines the canonical workflow for taking a theory-oriented research idea from initial motivation to submission freeze.

The workflow is not a writing checklist. It is a research-development and research-termination system. Its primary purpose is to prevent weak, derivative, ad hoc, or mathematically fragile ideas from consuming manuscript-writing effort.

A project should move forward only when it survives the relevant gate.

Each major stage must record a canonical verdict:

- `GO`: the evidence is sufficient to proceed;
- `CONDITIONAL GO`: a precise unresolved condition remains and must become the next-stage target;
- `NO-GO`: the current research branch should stop unless a narrowly defined pivot survives a new gate.

Templates may additionally report a routing/status label such as `GO TO STAGE 6`, `THEORY FROZEN`, or `SUBMISSION QA PASS`; that label is secondary and does not replace the canonical stage verdict.

A previous `GO` never guarantees a later `GO`.

This v1 canonical pipeline is theory-oriented. Stage 0 may recommend empirical or mixed research, but a project whose primary method is not theoretical should not be force-fit through the Stage 4 mathematical model gate. A dedicated empirical workflow is outside v1 scope.

---

## 2. Universal stage schema

Every stage-specific prompt, report, or template should use the following schema unless there is a documented reason not to.

1. **Objective** — What uncertainty is this stage supposed to resolve?
2. **Inputs** — What prior results, files, models, data, and decisions are canonical inputs?
3. **Mandatory tasks** — What work must be completed before a verdict?
4. **Evidence requirements** — What literature, primary sources, code, mathematics, or data must support the result?
5. **Verification** — What independent symbolic, numerical, empirical, or source checks are required?
6. **Kill tests** — What findings would invalidate the candidate contribution?
7. **Success criteria** — What must be true for `GO`?
8. **Failure criteria** — What makes the stage `NO-GO`?
9. **Required output** — What artifacts and decision record must be produced?
10. **Stage verdict** — `GO`, `CONDITIONAL GO`, or `NO-GO`.
11. **Routing/status output** — Where the branch goes next, freezes, or stops.
12. **Next-stage contract** — Exactly what may and may not change in the next stage.

The next-stage contract is essential. Do not respond to a failed model by adding multiple new mechanisms simultaneously.

For efficient handoff, each stage should preserve at least: outputs to carry forward, frozen facts, rejected branches, open blockers, and the one allowed next change when conditional work is authorized.

---

# Stage 0 — Idea / Motivation Intake

## Objective

Extract the genuine economic question from a phenomenon, old paper, policy problem, institutional fact, anomaly, or informal idea without assuming that it deserves a paper.

## Mandatory tasks

- State the observed phenomenon or theoretical puzzle.
- Separate the phenomenon from the proposed explanation.
- Identify the agents, decisions, frictions, and outcomes that appear essential.
- Distinguish theoretical contribution from application or institutional motivation.
- Generate multiple plausible mechanisms before committing to one.
- Write a one-sentence research question that can in principle be falsified by prior art or model analysis.

## Kill tests

Stop or radically reframe if the project is only:

- a policy description;
- a parameterization exercise;
- a known comparative static in a new application;
- an old model with modern labels;
- a phenomenon with no strategic or welfare mechanism.

## Exit criterion

Proceed only if there is a precise economic question worth subjecting to literature and mathematical audit.

---

# Stage 1 — Source & Mathematical Audit

## Objective

Reconstruct the starting model or argument from first principles and determine what it actually proves.

## Mandatory tasks

- Read all source material, including equations, notes, appendices, figures, and assumptions.
- Reconstruct players, timing, information, objectives, contracts, demand, costs, and equilibrium concept.
- Re-derive all equations from zero when the starting object is mathematical.
- Use Python/SymPy or equivalent symbolic tools for algebraic verification whenever applicable.
- Derive SOCs, feasibility conditions, participation constraints, and boundary cases when applicable.
- Identify variables or parameters that mix multiple economic interpretations.
- Distinguish algebraic results from genuine economic mechanisms.

## Kill tests

- Key proposition depends on an algebraic error.
- Equilibrium does not exist in an economically meaningful region.
- Claimed comparative static is mechanically built into demand or normalization.
- A contract or payoff split has no microfoundation and drives the result.
- Cross-regime comparison changes the consumer population, outside option, or normalization without justification.

## Exit criterion

A verified canonical representation of the starting object and a list of surviving questions.

---

# Stage 2 — Literature Frontier / Novelty Kill Gate

## Objective

Determine whether the surviving mechanism, strategic architecture, result, or proposed generalization is already known before investing in model expansion.

Novelty must be evaluated at two distinct levels:

1. **component level** — which primitives, players, margins, and results are individually known;
2. **whole-game/result level** — whether the economically relevant player-objective-strategy-timing-allocation-feedback structure and the proposed headline result are already solved.

Known components do not by themselves imply that the full game is absorbed. Conversely, the absence of one paper containing the exact ingredient combination does not itself establish novelty.

## Mandatory tasks

Search from seminal work through the current frontier, including recent working papers where relevant.

For close papers, inspect as far as feasible:

- players and objective functions;
- strategy sets/endogenous controls;
- model and timing;
- demand or utility;
- contracts and information;
- endogenous variables;
- participation/outside options and endogenous allocation/sorting;
- best-response or strategic-feedback network;
- equilibrium concept;
- propositions;
- welfare and incidence;
- extensions and appendices.

Perform:

- backward citation search;
- forward citation search;
- author-neighborhood search;
- adjacent-field/synonym search;
- working-paper/published-version deduplication.

For strategic/game-theoretic projects, perform a **whole-game absorption test**:

- determine whether one prior model reproduces the economically relevant full game through direct relabeling, normalization, or parameter restriction;
- if no single prior model does so, determine whether the proposed headline result is nonetheless an immediate corollary of an existing theorem;
- if reconstructing the candidate requires multiple prior literatures with different players, objectives, strategies, or feedbacks, identify what strategic interaction exists only in the full architecture.

For a claimed **generalization or unification**, identify the important nested prior models, the restrictions that recover them, and the candidate result that should exist only in the full model.

Classify overlap as:

1. `EXACT PRIOR ART`
2. `STRUCTURALLY VERY CLOSE`
3. `COMPONENT OVERLAP`
4. `MERELY RELATED`
5. `POTENTIALLY NOVEL` only when a model/proposition-level distinction survives.

## Kill tests

- Contribution is a renamed known result.
- New variable does not create a new strategic interaction.
- A single close paper already contains the same economically relevant players/objectives/strategies/timing/allocation/feedback structure.
- Closest paper already contains the same endogenous margin and welfare logic and the proposed result is an immediate corollary.
- Novelty claim rests only on failure to find the exact combination of keywords.
- Novelty claim rests only on “nobody combined these ingredients.”
- A claimed generalization only broadens notation or functional form while leaving the economics unchanged.

Do **not** kill solely because every component is separately known if no prior model reproduces the full strategic architecture and the combination plausibly generates a new equilibrium or welfare problem.

## Exit criterion

A closest-paper matrix, component-overlap map, whole-game absorption verdict, nested-benchmark map where applicable, and an explicit list of contributions that are killed, weakened, or still alive.

---

# Stage 3 — Candidate Mechanism Search

## Objective

Generate competing explanations and select mechanisms or strategically meaningful generalizations, not feature lists.

## Mandatory tasks

- Generate approximately 8–12 candidate mechanisms/architectures when the search space is broad.
- For each candidate, identify the strategic feedback loop.
- State what would change relative to the closest literature.
- Identify the smallest model capable of producing the proposed mechanism.
- For a generalization/unification candidate, identify the prior models nested by the full game and the strategic interaction that exists only when the components are jointly endogenous.
- State the candidate result that should be unavailable in each nested benchmark alone.
- Score candidates on theoretical novelty, mechanism clarity, whole-game prior-art survival, tractability, welfare content, institutional relevance, and journal fit when scoring is useful.
- Select a small TOP set for deep dives.

## Kill tests

Reject candidates that are merely:

- another heterogeneity parameter;
- another channel;
- another fixed cost;
- another player with no strategic effect;
- another comparative static without a new trade-off;
- a combination of familiar ingredients whose full game changes no strategic feedback and produces no new theorem.

Do not reject a generalization merely because its components are familiar if the full architecture creates a strategically non-equivalent equilibrium problem that the nested benchmarks cannot reproduce.

---

# Stage 4 — Minimal Model Gate

## Objective

Test the strongest candidate mechanism or generalization in the smallest possible model.

## Mandatory tasks

- Freeze players and timing.
- Use the simplest defensible microfoundation.
- Derive the equilibrium analytically where possible.
- Verify all closed forms symbolically when applicable.
- Search numerically for counterexamples only after symbolic/analytic analysis when applicable.
- Derive participation, feasibility, welfare, and limiting cases.
- Explicitly test desired propositions rather than assuming them.
- If the contribution route is generalization/unification, define and solve/recover the minimum nested benchmark games obtained by removing or fixing one strategic component at a time.
- Verify benchmark recovery and compare the full model with the benchmarks for the headline equilibrium/welfare object.
- Identify whether the full architecture changes the best-response/strategic-feedback network and creates a result unavailable in each benchmark alone.

## Success standard

A `GO` requires more than `parameter up → outcome up`. At least one result should reveal a clean strategic trade-off, threshold ordering, sign reversal, organizational wedge, welfare implication, or nontrivial conditions-for-effectiveness characterization.

A generalization/unification can qualify as a theoretical contribution when it cleanly nests important prior models **and** the interaction of their strategic margins generates a new equilibrium or welfare result that is unavailable in the nested benchmarks alone.

## Failure handling and routing

- `GO`: the minimal mechanism/generalization survives without a substantive repair. Freeze the resulting propositions and proceed to Stage 6 Novelty Re-Kill.
- `CONDITIONAL GO`: exactly one diagnosed economic deficiency can plausibly be tested by one authorized modification. Proceed to Stage 5 Mechanism Hardening with everything else frozen.
- `NO-GO`: stop the branch. Return to Stage 3 only for a genuinely distinct mechanism/generalization architecture, or Stage 0 for a distinct research question. `NO-GO` does not itself authorize hardening.

A negative proof is a valid Stage 4 output.

For a generalization route, return `NO-GO` if the full model merely writes multiple known benchmark cases in one notation, changes no economically meaningful strategic feedback, or yields only results already obtainable as immediate benchmark corollaries.

---

# Stage 5 — Mechanism Hardening

## Objective

Repair the precise weakness exposed by Stage 4 without uncontrolled model growth.

## Rule

Change one essential margin at a time.

Examples of legitimate hardening steps include:

- replacing an ad hoc transfer with a participation constraint;
- adding a missing contractibility margin;
- replacing static demand with a state variable when history is essential;
- introducing relationship-specific investment when provider identity otherwise has no content.

## Prohibition

Do not simultaneously add online channels, bargaining, geography, multiple manufacturers, dynamics, and heterogeneity because the baseline failed.

## Exit criterion

Either the mechanism becomes structurally coherent or the branch is terminated.

---

# Stage 6 — Novelty Re-Kill

## Objective

Search the literature again using the actual propositions generated by the model.

## Mandatory tasks

- Turn each surviving proposition into targeted search queries.
- Search the exact strategic mechanism, threshold result, organizational transition, welfare wedge, and game-architecture language.
- Re-open the closest literature in light of the new result.
- Distinguish novelty of individual components, novelty of the whole game, and novelty of the theorem.
- Re-run the whole-game absorption test against the actual solved model.
- For a generalization/unification, re-open every material nested benchmark and verify that the full-model result is unavailable in each benchmark alone and is not an immediate corollary of a known theorem.

## Rule

A result that looked novel before the mathematics may be killed after the mathematics. Remove it from the contribution set immediately.

A model is not rescued merely because no prior paper has the exact setup. A model is also not killed merely because every ingredient is separately familiar. The relevant question is whether the full strategic architecture and its surviving results are economically redundant with prior theory.

Stage 6 should update the Stage 2 literature ledger and re-open the papers that are material to the actual derived result; it should not repeat the entire Stage 2 search from zero unless the mechanism has materially changed.

---

# Stage 7 — Welfare / Generality / Institutional Validation

## Objective

Determine whether the mechanism matters beyond firm profit and beyond one motivating case.

## Mandatory tasks

- Derive consumer surplus and total welfare consistently from the model's utility system.
- Compare private and social decisions.
- Identify under-provision, over-provision, premature exit, excessive preservation, or other organizational wedges.
- Audit whether core primitives are supported by institutional evidence.
- Prefer primary sources for institutional claims.
- Test whether the mechanism generalizes to other industries or environments without changing the theory.
- Produce testable empirical predictions where possible.

## Kill tests

- Welfare result is just transfer accounting.
- Generality is obtained only by relabeling the same institution.
- A crucial primitive has no institutional or theoretical defense.
- Policy implications require assumptions not present in the model.

---

# Stage 7.5 — Full-Theory Freeze Decision

## Objective

Decide whether the project has a general economic mechanism or merely a technically correct result in a specific model.

## Required questions

- Can the core result be stated without model-specific notation?
- What is the minimal causal/strategic chain?
- What assumption is genuinely essential?
- What assumption is normalization or tractability?
- Does the contribution survive at least one alternative formulation?
- Is there a clear welfare or organizational implication?
- Would a skeptical field referee understand why this is not a parameter exercise?
- If the contribution is a generalization/unification, what important prior models are nested and what full-model result cannot be obtained from them separately?

## Verdict and routing

- `GO`: full-paper investment is justified; route to Stage 8 Canonical Theory Freeze.
- `CONDITIONAL GO`: exactly one unresolved theorem/robustness requirement remains; return only to the stage needed to resolve it and repeat Stage 7.5.
- `NO-GO`: stop the full-paper route; optionally classify the output as research note or pivot without treating that label as a `GO`.

Do not initialize a full manuscript build merely because a closed-form model exists.

---

# Stage 8 — Canonical Theory Freeze

## Objective

Freeze the theoretical object before manuscript construction.

## Freeze at minimum

- research question;
- players;
- timing;
- information;
- utility/demand;
- cost and contract structure;
- parameter restrictions;
- equilibrium concept;
- main propositions;
- welfare propositions;
- proof strategy;
- robustness scope;
- contribution claims;
- closest-paper distinction.

Changes after freeze require an explicit theory-change record and re-running affected gates.

---

# Stage 9 — Repository / Reproducibility Setup

## Objective

Create the production research repository only after the theory is sufficiently stable.

## Recommended components

- modular LaTeX manuscript;
- BibTeX/BibLaTeX bibliography;
- symbolic verification scripts where applicable;
- numerical verification scripts where applicable;
- deterministic figure/table generation;
- Makefile or equivalent build orchestration;
- environment/dependency specification;
- tests or verification gates;
- CI where feasible;
- decision log and provenance notes.

## Rule

Never reset to an old reference SHA without first fetching and checking the latest remote state.

---

# Stage 10 — Section-by-Section Paper Construction

## Objective

Build the manuscript in dependency order rather than writing the introduction first and forcing the theory to fit it.

## Recommended order

1. Model
2. Equilibrium characterization
3. Main propositions
4. Welfare
5. Robustness/extensions
6. Institutional or empirical bridge
7. Related literature
8. Introduction
9. Discussion
10. Conclusion

Each section should be compiled, checked against the frozen theory, reviewed, and integrated through controlled changes.

---

# Stage 11 — Robustness / Referee Attack

## Objective

Try to reject the paper before external referees do.

## Mandatory attacks

- `This is classic result X in different notation.`
- `Every ingredient is known; does the full game actually create a new strategic interaction or result?`
- `The claimed generalization merely nests known cases without adding new economics.`
- `The result is driven by one ad hoc assumption.`
- `The extension merely adds a variable.`
- `The welfare result is mechanical.`
- `The motivating institution is too specific.`
- `The main theorem disappears under a standard alternative demand or contract.`
- `The result is numerically observed but not proved.`

Classify attacks as `FATAL`, `MAJOR BUT FIXABLE`, or `MINOR`.

A major claim with an unresolved fatal attack cannot proceed to submission preparation. Route any substantive fix to the earliest affected research stage under the rollback rule.

---

# Stage 12 — Journal Positioning

## Objective

Choose journals based on the actual contribution, not the desired prestige level.

## Mandatory tasks

- Read current aims/scope and recent related publications.
- Compare model sophistication and contribution type with papers actually published there.
- Estimate desk-reject risk and likely referee objection.
- Assess whether empirical content is expected.
- Define stretch, primary, realistic fallback, and safety-net routes when appropriate.

## Rule

Do not reshape an economics contribution into a managerial paper merely because another journal family appears easier.

Early stages may use a provisional journal family or quality bar. Stage 12 is the point for actual journal selection and submission sequencing.

---

# Stage 13 — Full-Paper Integration

## Objective

Turn independently correct sections into one coherent argument.

## Audit

- Introduction states the question, mechanism, result, and contribution without overclaiming.
- Related Literature is organized by conceptual relationship, not repetitive author-by-author summaries.
- Model contains no assumptions introduced solely to rescue later prose.
- Results section proves rather than narrates.
- Discussion interprets scope and implications rather than repeating results.
- Conclusion is short and does not introduce new claims.
- Terminology and notation are consistent.
- Every contribution claim maps to a verified theorem/result and literature distinction.

Substantive inconsistency triggers rollback to the earliest affected stage; it is not a manuscript-only edit.

---

# Stage 14 — Submission QA

## Objective

Verify the complete submission package.

## Mandatory checks

- fresh full build from a clean environment;
- all applicable symbolic verification passes;
- all applicable numerical tests regenerate reported results;
- figures/tables regenerate from source;
- all citations resolve;
- no unverified references;
- no broken labels/cross-references;
- journal formatting requirements satisfied;
- anonymity requirements satisfied;
- supplementary material consistent;
- AI/disclosure requirements checked against current journal policy;
- claims, abstract, highlights, and cover letter agree with the manuscript.

A substantive mathematical, novelty, theory, welfare, or institutional problem discovered here triggers rollback to the earliest affected stage and a fresh downstream QA cycle.

---

# Stage 15 — Submission Freeze

## Objective

Create an immutable, auditable submission state.

## Freeze

- canonical commit SHA/tag;
- manuscript PDF;
- source archive;
- appendices/supplement;
- verification outputs;
- cover letter and required submission files;
- journal-specific metadata;
- disclosure statement where required.

After submission freeze, theoretical changes require reopening the affected research stages, not silent edits.

---

# 3. Cross-stage rules

## 3.1 Literature integrity and continuity

Do not invent citations, bibliographic metadata, propositions, or novelty claims. For closest papers, rely on the strongest accessible evidence and document evidentiary limits.

Stage 2 establishes the baseline literature ledger. Later literature work is incremental and purpose-specific: Stage 3 performs targeted searches for newly proposed mechanisms; Stage 5 checks the literature introduced by the one new primitive; Stage 6 re-kills the actual derived results; Stage 7 validates institutions/generality; Stage 12 checks journal fit. Do not restart the complete literature review at every stage unless the research question or mechanism materially changes.

For strategic models, preserve the distinction between **component overlap** and **whole-game absorption** throughout the workflow. A later stage must not silently promote a collection of component precedents into an exact-absorption verdict without a model-level mapping or result-level corollary argument.

## 3.2 Mathematical and method integrity

Where symbolic derivation is feasible, independently verify it. Never treat a first-order condition solution as an equilibrium without SOC, feasibility, and relevant constraints.

Verification must match the research method. A check may be `NOT APPLICABLE` only with a reason. The theory-oriented Stage 4 gate should not be imposed on a project whose Stage 0–3 decision is to pursue a non-theory primary method; that project leaves this v1 canonical theory pipeline rather than pretending to pass Stage 4.

## 3.3 Negative results are first-class outputs

A stage that proves why a desired proposition cannot hold has succeeded if it eliminates a weak branch efficiently.

## 3.4 No complexity rescue

Complexity must solve a diagnosed economic deficiency. It may not be used to hide a failed minimal mechanism.

A generalization/unification is not exempt from this rule. Added players or strategic margins must be necessary to the economic question and must be evaluated through nested benchmarks.

## 3.5 Contribution discipline

Variables are not contributions. Functional forms are not contributions. Applications are not automatically contributions. The contribution should be expressible as an economic mechanism, theorem, comparative-static reversal, organizational result, welfare implication, or economically substantive generalization/unification that survives prior-art comparison.

A generalization/unification contribution must do more than place known models inside one notation. It should recover important benchmarks transparently and generate a new strategic interaction, equilibrium characterization, conditions result, or welfare implication unavailable in the benchmarks alone.

Likewise, known components do not automatically imply that a strategically distinct full game is absorbed. Absorption requires whole-game equivalence or result-level redundancy, not an ingredient checklist.

## 3.6 Provenance and evidence maturity

Every project should distinguish historical/AI/scratch outputs from results reproduced in the project repository and from claims re-verified for the actual submission package. Do not silently promote a conversation result, temporary notebook output, or remembered citation to submission-ready evidence.

## 3.7 Rollback and stale downstream outputs

If a later stage invalidates an earlier canonical input, return to the earliest affected stage. Mark all dependent downstream outputs stale until the necessary stages are re-run. Do not silently patch a downstream manuscript or submission artifact around an invalid research result.

## 3.8 Provenance and decision logs

Every project should preserve major rejected branches and the reason for rejection. A reusable research workflow depends as much on documented failures as on final successful results.

---

# 4. Planned companion materials

Reusable Stage 0–15 prompt/report templates, verification checklists, and worked examples are maintained in this repository under the canonical hierarchy.

Future extensions may add empirical/cross-discipline variants, machine-readable metadata, CI, and release tooling after explicit audit. These are not part of the v1 theory pipeline.

This document is the canonical workflow architecture. Stage-specific templates may elaborate it but must not silently weaken its gates.
