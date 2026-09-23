# Theory Paper Research Pipeline

Version: v2.5

## 1. Purpose

This document defines the canonical workflow for taking a theory-oriented economics research idea from initial motivation to submission freeze.

The workflow is a research-development, research-verification, and research-termination system. It is designed to make weak, derivative, ad hoc, mathematically fragile, over-generalized, or poorly communicated branches fail before manuscript and submission effort becomes costly.

A project advances only when it survives the relevant gate. A previous `GO` never guarantees a later `GO`.

Each major stage records exactly one canonical verdict:

- `GO` — the evidence is sufficient to proceed;
- `CONDITIONAL GO` — exactly one material blocker remains and the next-stage contract is narrowly defined;
- `NO-GO` — the branch stops unless a genuinely distinct pivot re-enters at the appropriate earlier stage.

Routing/status labels such as `GO TO STAGE 6`, `THEORY FROZEN`, or `SUBMISSION QA PASS` are secondary and never replace the canonical verdict.

This pipeline is theory-oriented. Stages 0–3 may recommend empirical or mixed research, but a project whose primary method is not theoretical should leave this pipeline rather than pretend to pass the Stage-4 mathematical gate.

### v2.0 mathematical-safety architecture

v2.0 adds two mandatory independent red-team gates before theory freeze:

1. **Stage 4A — Independent Mathematical Adversarial Certification Gate**: independently tries to break the solved model, including global deviations, boundaries, corners, regime switches, continuation completeness, solver failure semantics, benchmark definitions, and theorem certificates.
2. **Stage 7.5A — Generality / Quantifier / Portability Red-Team Gate**: attacks theorem scope, functional-form generality, quantifiers, robustness language, hidden microfoundation dependence, economic portability, and planner/benchmark terminology before the theory can be frozen.

The required routing is therefore:

`Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8`.

Neither Stage 4A nor Stage 7.5A may be bypassed by a green symbolic check, CI run, production solver, or prior `GO`.

The workflow uses a three-layer mathematical defense:

- **construction/verification layer** — solve and verify the model at Stage 4;
- **independent adversarial layer** — Stage 4A and Stage 7.5A attempt to falsify correctness and scope without inheriting the construction path;
- **full-manuscript hostile layer** — Stage 11 repeats high-stakes attacks after exposition has been added and treats any newly discovered mathematical failure as a rollback event and workflow regression signal.

### Embedded Formal Verification Gate

Every theorem-bearing project must also make a formal-verification applicability decision. This is an embedded verification obligation, **not a new canonical Stage**, so Stage numbering and normal routing remain unchanged.

The lifecycle is:

- **Stage 4A:** record preliminary applicability and a proof-critical formalization target map;
- **Stage 7.5A:** reassess against the final theorem scope and close the Formal Verification Gate;
- **Stage 8:** refuse theory freeze unless the gate is closed;
- **Stages 9/11/14/15:** preserve, attack, rebuild, and freeze the formal artifacts where applicable.

The required Stage-7.5A pre-freeze state is exactly one of:

- `FORMAL VERIFICATION PASS`; or
- `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

`NOT TESTED`, `PLANNED`, failed compilation, stale formal statements, unexplained proof placeholders, or unresolved statement-fidelity gaps are blocking states.

Formal verification complements rather than replaces analytic derivation, global-deviation analysis, alternative-equilibrium search, independent adversarial certification, and quantifier/scope audit. A proof assistant certifies the encoded theorem from encoded hypotheses; it does not certify unformalized economic primitives or equilibrium domains by implication.

Apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md`.

### v2.2 structural-isomorphism / theorem-absorption hardening

v2.2 is a backward-compatible minor refinement. It adds no Stage, changes no canonical verdict meaning, and changes no normal routing.

Its purpose is to prevent false novelty caused by application-specific language hiding a known mathematical model or theorem. The workflow now requires three linked controls:

1. **Stage 4 — mathematical canonicalization:** strip application labels and write the solved model in an application-neutral canonical form, including strategy geometry, payoff/function class, interaction operator or matrix, constraints, and equilibrium concept. Record plausible standard parent classes and simple transformations such as recentering, normalization, variable elimination, matrix form, KKT reduction, or polytope representation.
2. **Stage 6 — theorem-level absorption test:** for the closest general results, explicitly attempt to derive each headline theorem by mapping the candidate model into the prior theorem. Novelty does not survive merely because the same application, notation, or exact closed-form threshold has not appeared before.
3. **Stage 11 — known-model-in-disguise attack:** a hostile referee must try to reduce the manuscript to a known model class and ask whether the headline result is a direct specialization, boundary case, or short corollary of an existing theorem.

The governing distinction is:

`same application not found` ≠ `new theorem`.

A Stage-6 novelty PASS requires an evidence-bearing explanation of why the strongest plausible parent theorem does **not** absorb the headline result, or an explicit downgrade to application/interpretation contribution if it does.


### v2.5 exposition architecture / streamlining hardening

v2.5 is a backward-compatible minor refinement. It adds no Stage, changes no canonical verdict meaning, and changes no normal research routing.

Its purpose is to prevent scientifically correct papers from reaching submission with avoidable reader-cost, scattered model content, redundant exhibits, or late-stage structural rewrites. It generalizes an Igami-style exposition discipline without treating paper-specific page landmarks as universal rules.

The exposition lifecycle is:

`Stage 7 → Stage 10 → Stage 13 → Stage 14`.

1. **Stage 7 — candidate vehicles:** identify candidate theorem/proposition/figure/table/numerical/prose vehicles for headline results.
2. **Stage 10 — architecture design:** choose an article-type exposition profile, define section roles and reader-arrival targets, consolidate the model/evidence architecture, and run an exhibit-scarcity thought experiment before finalizing the Introduction.
3. **Stage 13 — streamlining:** audit the integrated manuscript item by item, classify material as `CORE` / `HELPFUL` / `APPENDIX` / `DELETE`, compress the Introduction, enforce section purity, rerun actual page-arrival diagnostics, and remove or relocate redundant material without weakening theorem/evidence scope.
4. **Stage 14 — verification:** perform a binary exposition audit on the final package. A structural exposition failure normally reopens Stage 13; an architecture failure may reopen Stage 10; a substantive theory/evidence/novelty change reopens the earliest affected research stage.

Generic page counts are diagnostics only. Current journal instructions and article type control. The paper-specific milestones that motivated this refinement may be used as examples for a conventional structural/empirical paper, but they are never universal pass/fail thresholds.

Every project using the exposition lifecycle must apply `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md` together with `checklists/FIGURE_TABLE_CHECKLIST.md` where figures/tables are present.

The governing objective is **minimum reader cost subject to complete and accurate scientific communication**, not maximum brevity.


### v2.4 economic portability / falsification hardening

v2.4 is a backward-compatible minor refinement. It adds no Stage, changes no canonical verdict meaning, and changes no normal routing.

Its purpose is to prevent a technically correct baseline model from being frozen before the workflow has determined how far the headline economic mechanism survives credible changes in microfoundation or institution. The refinement separates two questions that must not be conflated:

1. **Stage 7.5A — research-strength certification:** determine the maximum defensible strength of each headline result by pre-specified economic falsification, portability testing, and exact classification of failure boundaries.
2. **Stage 12 — journal positioning:** match the already-certified contribution to journals whose current editorial bar and article type fit that contribution. Stage 12 does not ask the theory to become stronger merely to preserve a preferred target.

For any headline claim presented as more than baseline/model-specific, Stage 7.5A must pre-specify at least one economically meaningful alternative formulation that changes a plausibly result-driving assumption, re-solve the relevant equilibrium rather than transporting baseline formulas, and record whether the claim is:

- `PORTABLE`;
- `CONDITIONALLY PORTABLE`;
- `MODEL-SPECIFIC`;
- `INSTITUTION-SPECIFIC`; or
- `FALSIFIED`.

Negative portability results are first-class research outputs. A failed alternative model may narrow the theorem, identify the economic assumption carrying the result, or terminate an attempted generality claim.

To prevent research creep, Stage 7.5A also applies a stop rule: if two economically meaningful, pre-specified, non-cosmetic portability attacks both overturn the same claimed cross-model sign/mechanism and no defensible abstract sufficient-condition formulation survives, the claim must normally be certified `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` rather than repeatedly redesigning alternatives to rescue it. Further theory development requires a distinct research reason and rollback to the earliest affected stage.

Stage 7.5A remains journal-neutral. Journal names, rankings, and target prestige do not determine whether a mechanism counts as portable. Stage 12 consumes the resulting **Contribution Robustness Certificate** and compares it with current journal scope and recent comparable papers.

Apply `checklists/PORTABILITY_FALSIFICATION_CHECKLIST.md`.

### v2.3 journal-candidate-universe completeness hardening

v2.3 is a backward-compatible minor refinement. It changes no Stage, verdict meaning, or normal routing.

Its purpose is to prevent Stage 12 from ranking an incomplete, path-dependent shortlist. The workflow now requires three linked controls:

1. **Contribution-first generation:** build the broad journal universe from the paper that actually survived Stage 11 — field/audience, contribution/article type, methodological level, manuscript scale, and any materially relevant audience constraints — before ranking journals.
2. **Literature-venue completeness cross-check:** use venues represented in the closest literature as a diagnostic for omissions, not as automatic targets. An obvious field venue or repeatedly represented relevant venue must be evaluated or explicitly excluded.
3. **Conditional source-venue rule:** only for correction, comment, replication, re-examination, or closely related source-audit papers, explicitly evaluate the target/source paper's journal unless there is a documented reason not to.

The governing distinction is:

`close paper appeared there` ≠ `serious target`.

Likewise:

`not on the first shortlist` ≠ `not a plausible target`.

Stage 12 must preserve an auditable candidate-universe/exclusion record before selecting the primary journal.

---

## 2. Universal stage schema

Every stage-specific prompt, report, or template should include, unless genuinely inapplicable:

1. Objective
2. Inputs
3. Mandatory tasks
4. Evidence requirements
5. Verification
6. Kill tests
7. Success criteria
8. Failure criteria
9. Required output
10. Canonical stage verdict
11. Routing/status output
12. Next-stage contract

For efficient handoff preserve at least: outputs to carry forward, frozen facts, rejected branches, open blockers, and the one allowed next change when conditional work is authorized.

For theorem-bearing stages preserve a claim/proposition register. For headline mathematical claims, use `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` as required by Stage 4A and Stage 7.5A. Every theorem-bearing project must also apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md`: Stage 4A records applicability/targets and Stage 7.5A closes the pre-freeze formal-verification state.

For manuscript exposition, use the four-step lifecycle:

- Stage 7 — identify candidate exposition vehicles;
- Stage 10 — design the full exposition architecture, including section roles, reader-arrival targets, model/evidence consolidation, and figure/table architecture;
- Stage 13 — integrate and aggressively streamline the target-journal manuscript using actual page/order evidence;
- Stage 14 — verify that the final package still satisfies the exposition architecture while also checking regeneration, numerical integrity, artwork compliance, source completeness, and legibility.

Apply `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md` across this lifecycle. Stage 10 is the design gate, Stage 13 is the streamlining gate, and Stage 14 is a verification gate rather than the normal place for a late structural rewrite.

There is no minimum figure/table quota. Every visual must materially reduce the reader's cost of understanding a verified result. The five-exhibit thought experiment is a prioritization device, not a universal exhibit limit.

---

# Stage 0 — Idea / Motivation Intake

## Objective

Extract the genuine economic question from a phenomenon, old paper, policy problem, institutional fact, anomaly, or informal idea without assuming it deserves a paper.

## Mandatory tasks

- State the observed phenomenon or theoretical puzzle.
- Separate phenomenon from proposed explanation.
- Identify agents, decisions, frictions, and outcomes that appear essential.
- Distinguish theoretical contribution from application or institutional motivation.
- Generate multiple plausible mechanisms before committing to one.
- Write a one-sentence research question that can in principle be falsified by prior art or model analysis.

## Kill tests

Stop or reframe if the project is only a policy description, parameterization exercise, known comparative static in a new application, old model with modern labels, or phenomenon with no strategic/welfare mechanism.

## Exit criterion

Proceed only if there is a precise economic question worth literature and mathematical audit.

---

# Stage 1 — Source & Mathematical Audit

## Objective

Reconstruct the starting model or argument from first principles and determine what it actually proves.

## Mandatory tasks

- Read all source material, including equations, appendices, figures, notes, and assumptions.
- Reconstruct players, timing, information, objectives, contracts, demand, costs, and equilibrium concept.
- Re-derive mathematical starting objects from zero.
- Use Python/SymPy or equivalent symbolic tools where applicable.
- Derive SOCs, feasibility, participation, and boundary cases.
- Identify parameters that mix economic interpretations.
- Distinguish algebraic identities from economic mechanisms.

## Kill tests

Kill or repair if a key proposition depends on algebraic error, equilibrium fails in the meaningful region, a comparative static is mechanically built into normalization, a payoff split has no defensible microfoundation and drives the result, or cross-regime comparison silently changes population/outside options/accounting.

## Exit criterion

A verified canonical starting object and list of surviving research questions.

---

# Stage 2 — Literature Frontier / Novelty Kill Gate

## Objective

Determine whether the candidate mechanism, strategic architecture, result, or proposed generalization is already known before model investment.

Novelty must be assessed at both:

1. component level; and
2. whole-game/result level.

Known components do not automatically absorb the full game. Conversely, absence of one paper containing the exact ingredient combination does not establish novelty.

## Mandatory tasks

Search seminal work through the current frontier, including relevant working papers. For close papers inspect players/objectives, strategies, timing, demand/utility, contracts/information, endogenous margins, participation/allocation, strategic-feedback network, equilibrium concept, propositions, welfare, and extensions.

Perform backward citation, forward citation, author-neighborhood, adjacent-field/synonym, and working-paper/published-version searches where relevant.

For strategic projects perform a **whole-game absorption test**:

- can one prior model reproduce the economically relevant full game by relabeling, normalization, or restriction?
- if not, is the proposed headline result nonetheless an immediate corollary of an existing theorem?
- if multiple literatures are required to reconstruct the candidate, what strategic interaction exists only in the full architecture?

For generalization/unification identify important nested prior models, restrictions that recover them, and a candidate result that should exist only in the full model.

Classify overlap as `EXACT PRIOR ART`, `STRUCTURALLY VERY CLOSE`, `COMPONENT OVERLAP`, `MERELY RELATED`, or `POTENTIALLY NOVEL` only when a model/result-level distinction survives.

## Kill tests

Kill contributions that are renamed known results, cosmetic new variables, immediate corollaries of the closest model, keyword-search novelty, “nobody combined these ingredients” novelty without new strategic feedback, or notation-only generalization.

## Exit criterion

Closest-paper matrix, overlap map, whole-game absorption verdict, nested-benchmark map when relevant, and explicit killed/weakened/surviving contribution set.

---

# Stage 3 — Candidate Mechanism Search

## Objective

Generate competing explanations and select mechanisms or strategically meaningful generalizations, not feature lists.

## Mandatory tasks

- Generate multiple candidate mechanisms/architectures when the search space is broad.
- Identify each strategic feedback loop.
- State what changes relative to closest literature.
- Identify the smallest model capable of producing the proposed mechanism.
- For generalization/unification, identify nested benchmarks and the interaction that exists only when components are jointly endogenous.
- State a candidate result unavailable in each benchmark alone.
- Score candidates on novelty, mechanism clarity, whole-game prior-art survival, tractability, welfare content, institutional relevance, and journal fit when useful.

## Kill tests

Reject “another parameter/channel/fixed cost/player” additions that create no new strategic problem or theorem. Familiar components may survive only if their joint endogeneity creates a strategically non-equivalent equilibrium problem.

---

# Stage 4 — Minimal Model Gate

## Objective

Solve the strongest candidate mechanism/generalization completely in the smallest defensible model.

## Mandatory tasks

- Freeze players, timing, information, complete strategy/choice sets, and primitives.
- Produce an **application-neutral canonical mathematical representation** of the solved model: strategy-set geometry, payoff/function class, interaction matrix/operator, coupling constraints, and equilibrium concept.
- Strip application labels and test simple equivalence-preserving transformations where relevant: affine recentering, normalization, variable elimination, matrix representation, KKT/complementarity form, potential-game representation, aggregative/network representation, simplex/transportation/assignment-polytope representation, or another standard form suggested by the mathematics.
- Record plausible standard parent model classes and whether the headline result appears prima facie to be a specialization/corollary candidate. This is a screening record, not the final novelty verdict; Stage 6 performs the literature-backed absorption test.
- Derive allocation/demand from the microfoundation where applicable.
- Solve analytically where possible.
- Verify closed forms symbolically.
- Derive FOCs/KKT, SOCs/Hessians, feasibility, participation, existence, uniqueness, and limiting cases as applicable.
- Distinguish local/regular/interior candidates from global equilibrium.
- Test finite/global deviations, corners, boundaries, active-set changes, kinks, regime switches, ordering changes, participation changes, entry/exit/zero-output states, and nonexistence/multiplicity where relevant.
- For sequential games, re-solve downstream subgames after material upstream deviations on the actual strategy/history domain.
- Treat `None`, NaN, exception, invalid branch, nonconvergence, and branch failure as `UNRESOLVED` unless nonexistence is separately proved.
- Construct an independent direct-payoff/allocation evaluator for at least one high-stakes claim where feasible.
- Search symbolically/analytically for counterexamples before numerical search where feasible.
- Preserve discovered counterexamples as permanent regression tests.
- Derive profits, consumer surplus, total welfare, and private/social benchmarks when part of the research question.
- Write each desired result as a Candidate Proposition and actively try to falsify it.
- Identify sign-switch/threshold conditions rather than forcing ambiguous derivatives into monotone claims.
- For generalization/unification, solve/recover nested benchmarks and identify at least one full-model result unavailable as an immediate benchmark corollary.

Apply `checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md`, `checklists/NUMERICAL_VERIFICATION_CHECKLIST.md` when applicable, and `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` in full whenever off-path continuations matter.

## Success standard

`GO` requires a coherent solved object plus at least one clean strategic trade-off, threshold ordering, sign reversal, organizational wedge, welfare result, or conditions-for-effectiveness characterization. A sequential SPNE claim additionally requires continuation completeness with no material `UNRESOLVED`/`NUMERICAL_FAILURE` continuation.

## Failure handling and routing

- `GO` → **Stage 4A**, not Stage 6.
- `CONDITIONAL GO` → Stage 5 only when exactly one diagnosed economic deficiency can be tested by one authorized model modification.
- `NO-GO` → terminate the branch or return to Stage 3/0 only for a genuinely distinct architecture/question.

A negative proof is a valid Stage-4 output.

---

# Stage 4A — Independent Mathematical Adversarial Certification Gate

## Objective

Independently try to falsify the solved Stage-4 object before novelty or welfare work continues.

The preferred reviewer/implementation must be logically independent of the construction path: a different model, clean-room derivation, separately written evaluator/solver, or equivalent method that does not inherit the production branch assumptions.

## Mandatory tasks

For every headline claim:

- formalize exact quantifiers, parameter domain, strategy domain, assumptions, and local/branch/global status;
- reconstruct payoffs/allocation from primitives without relying only on the production solver;
- re-audit FOCs/KKT, SOCs/Hessians, feasibility, participation, existence/uniqueness as relevant;
- enumerate and attack corners, boundaries, active-set changes, regime switches, order changes, entry/exit, zero-output states, discontinuities, kinks, and material off-path histories;
- search for profitable finite/global deviations over the actual strategy set;
- for sequential games independently challenge continuation completeness and fail closed on solver failures;
- deliberately choose stress histories/parameters that break maintained interiority or the preferred regular branch;
- conduct analytic/symbolic and then numerical counterexample search where applicable;
- independently verify at least one high-stakes claim through a separate evaluator/solver where feasible;
- audit welfare benchmark labels against the planner's actual objective and feasible choice set;
- create one theorem certificate per headline claim using `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`;
- preserve all counterexamples as regression artifacts;
- apply the applicability portion of `checklists/FORMAL_VERIFICATION_CHECKLIST.md` and record either `FORMALIZATION APPLICABLE` with a preliminary proof-critical target map or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

The preliminary formalization map should prioritize high-consequence algebra, quantified inequalities, piecewise/case logic, thresholds, exact counterexamples, global-deviation inequalities, equilibrium-condition implications, and welfare identities. Formal proof planning does not count as the independent Stage-4A attack itself.

## Hard gate

A material theorem-certificate field marked `NOT TESTED` blocks `GO` unless explicitly `NOT APPLICABLE` with a valid reason.

A headline claim fails certification if it relies on local conditions as global proof, an omitted profitable boundary/regime deviation, unresolved continuation treated as unprofitable, a regular formula outside its domain, solver failure filtering, an implementation-independent contradiction, or a benchmark label inconsistent with the optimization problem.

Formal-verification implementation may remain pending until Stage 7.5A, but the applicability decision and preliminary target map may not be silently omitted.

## Verdict and routing

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` → Stage 6.
- `CONDITIONAL GO` → earliest affected stage; proof/equilibrium/domain errors normally reopen Stage 4, while exactly one authorized economic modification may route to Stage 5 and must then repeat Stage 4 and 4A.
- `NO-GO` → terminate or reopen Stage 4/3/0 as required.

No project may bypass Stage 4A because Stage 4, CI, symbolic algebra, a proof assistant, or the production solver is green.

---

# Stage 5 — Mechanism Hardening

## Objective

Repair exactly one diagnosed economic deficiency exposed by Stage 4/4A without uncontrolled model growth.

## Rule

Change one essential margin at a time. Examples include replacing an ad hoc transfer with participation, adding one missing contractibility margin, replacing static demand with a state variable when history is essential, or adding relationship-specific investment when provider identity otherwise has no content.

## Prohibition

Do not add multiple mechanisms because the baseline failed.

## Exit criterion and routing

Either the repair becomes structurally coherent or the branch terminates. A repaired model returns to **Stage 4 and then Stage 4A**; it does not jump directly to Stage 6.

---

# Stage 6 — Novelty Re-Kill

## Objective

Search the literature again using the actual certified propositions.

## Mandatory tasks

- Turn surviving propositions into targeted searches.
- Search the exact strategic mechanism, threshold, welfare wedge, transition, and game-architecture language.
- **Re-run the search with application labels removed**, using the Stage-4 canonical mathematical representation, standard parent-class terminology, constraint geometry, interaction structure, and theorem object.
- Re-open closest literature in light of the solved result.
- Distinguish component novelty, whole-game novelty, theorem novelty, and application/interpretation novelty.
- Re-run whole-game absorption against the actual model.
- For each serious parent-theorem candidate, construct an explicit **theorem-absorption map**: `prior theorem → variable/parameter mapping → required restriction/transformation → candidate headline result → DIRECTLY ABSORBED / PARTIALLY ABSORBED / NOT ABSORBED`.
- Treat a short derivation from a known general theorem as absorption even when the prior paper does not print the same application-specific formula or threshold.
- For generalization/unification, verify the full-model result is unavailable in material nested benchmarks and is not an immediate corollary of a known theorem.

A result that looked novel before the mathematics may be killed now. Remove it immediately from the contribution set.

Stage 6 updates the Stage-2 literature ledger rather than repeating the entire search from zero unless the mechanism materially changed.

---

# Stage 7 — Welfare / Generality / Institutional Validation

## Objective

Determine whether the certified mechanism matters beyond firm profit and one motivating case, and identify efficient exposition vehicles before theory freeze.

## Mandatory tasks

- Derive consumer surplus and total welfare consistently from the model utility/accounting system.
- Compare private and social decisions.
- Identify under/over-provision or other organizational wedges.
- Audit institutional support for core primitives, preferring primary sources.
- Test whether the mechanism generalizes across credible environments without changing the theory.
- Produce testable predictions where possible.
- Perform result-to-exposition triage for every headline result: theorem/proposition, figure, table, numerical illustration, or concise prose.
- Flag thresholds, sign reversals, non-monotonicity, regime changes, benchmark separation, welfare decomposition, and multi-case scope patterns for visual consideration when useful.

## Kill tests

Kill or downgrade if welfare is transfer accounting, generality is relabeling only, a crucial primitive lacks theoretical/institutional defense, policy claims require absent assumptions, or visual interest requires unverified computation/overclaiming.

## Exit criterion

A welfare/generality verdict and result-to-exposition triage map for Stage 10.

---

# Stage 7.5 — Full-Theory Freeze Decision

## Objective

Decide whether the project contains a general economic mechanism worthy of full-paper investment rather than only a technically correct model-specific result.

## Required questions

- Can the core result be stated without model-specific notation?
- What is the minimal causal/strategic chain?
- Which assumptions are essential versus normalization/tractability?
- Does the contribution survive at least one credible alternative formulation already tested?
- Is the welfare/organizational implication substantive?
- Would a skeptical field referee see more than a parameter exercise?
- If generalization/unification is claimed, which important prior models are nested and what result cannot be obtained from them separately?

## Verdict and routing

- `GO` → **Stage 7.5A**, not Stage 8.
- `CONDITIONAL GO` → return only to the stage needed to resolve the one named blocker, then repeat affected downstream gates.
- `NO-GO` → stop the full-paper route or classify as research note/pivot without treating that label as `GO`.

Do not initialize a full manuscript merely because a closed-form model exists.

---

# Stage 7.5A — Generality / Quantifier / Portability Red-Team Gate

## Objective

Certify both the exact scope and the maximum defensible research strength of every headline theorem, robustness statement, welfare benchmark, and contribution sentence before theory freeze.

This stage attacks over-generalization, hidden functional-form dependence, and false portability rather than merely rechecking baseline algebra. It is **journal-neutral**: the question is what the theory actually supports, not what a preferred journal would like it to support. It also contains the final pre-freeze **Formal Verification Gate**.

## Mandatory tasks

For every headline theorem/proposition and material robustness/generalization statement:

- rewrite the claim in formal quantifier form (`for all`, `exists`, `unique`, `generic`, `local`, `global`, etc.);
- list assumptions actually used, separating economic assumptions, shape restrictions, parameter restrictions, regularity, normalization, tractability, and institutional assumptions;
- compare formal theorem scope with the strongest abstract/introduction/contribution/welfare/robustness prose;
- distinguish baseline closed form, restricted function class, sufficient-condition theorem, numerical robustness evidence, conjectured generality, and truly general theorem;
- identify the **mechanism invariant**: the smallest economic chain/object whose survival would count as genuine portability rather than mere preservation of a numerical sign;
- before computing the result, pre-specify at least one economically meaningful alternative formulation for every headline claim presented as more than baseline/model-specific. The alternative must change a plausibly result-driving feature such as demand substitution, strategic variable, network microfoundation, cost technology, information, timing, heterogeneity, or coalition/institutional rule; cosmetic relabeling does not count;
- record ex ante the alternative's primitives, equilibrium concept, the exact success/failure criterion, and why the perturbation is economically credible;
- re-solve the affected equilibrium/subgame under the alternative formulation. Do not insert altered primitives into a baseline formula whose derivation no longer applies;
- if the first portability test survives and a second orthogonal test would materially distinguish broad portability from one-dimensional robustness, perform that second pre-specified attack;
- if portability fails, attempt to identify an abstract sufficient-condition formulation or exact assumption boundary that explains the failure without redesigning the alternative model after observing the result;
- classify each headline claim as exactly one of `PORTABLE`, `CONDITIONALLY PORTABLE`, `MODEL-SPECIFIC`, `INSTITUTION-SPECIFIC`, or `FALSIFIED`, with evidence;
- apply the stop rule in `checklists/PORTABILITY_FALSIFICATION_CHECKLIST.md`: repeated result-driven redesign is prohibited. Two economically meaningful, pre-specified, non-cosmetic failures of the same claimed cross-model mechanism normally terminate the portability claim unless an abstract sufficient-condition theorem survives;
- preserve negative portability results, counterexamples, and failure boundaries as first-class research artifacts rather than hiding them as unsuccessful extensions;
- for broad function classes, identify which derivative/order restrictions are required for each sign, concavity, uniqueness, or threshold conclusion;
- construct admissible counterexample functions designed to reverse claimed comparative statics/curvature/orderings;
- stress-test nonquadratic, low/high-curvature, boundary, and near-boundary cases when the baseline is convenient/parametric;
- verify that a parametric-family result is not called generic without a separate argument;
- write the planner optimization problem and feasible choice set for every welfare benchmark and reserve `first best` for the unrestricted relevant planner problem;
- produce a claim-scope ledger mapping each manuscript claim to theorem certificate, proof, robustness artifact, portability classification, maximum defensible wording, and prohibited stronger wording;
- produce a **Contribution Robustness Certificate** summarizing, for each headline result, the mechanism invariant, tested alternatives, survival/failure result, essential assumptions, failure boundary, and final portability classification;
- reapply the theorem-certification checklist whenever claim scope changed after Stage 4A;
- apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md` to the current scope-certified theorem set and reassess the Stage-4A preliminary applicability decision;
- when applicable, formalize the highest-value proof-critical core using Lean 4/mathlib or another auditable proof assistant rather than automatically requiring full-model formalization;
- map paper claims to formal theorem/lemma statements, compare quantifiers/domains, list hypotheses supplied rather than derived, and state explicit non-formalized economic/model scope;
- audit formal source for `sorry`, `admit`, equivalent placeholders, project-specific axioms, conclusion-smuggling definitions, and condition structures mistaken for proofs of economic equivalence;
- retain pinned/reproducible proof-assistant, library/dependency, build, and CI evidence where feasible.

### Diagnostic-alternative rule

Stage 7.5A may introduce **pre-specified diagnostic alternatives solely to test portability**. It may not silently replace the canonical model, add a result-driven rescue mechanism, or convert a failed robustness exercise into a new headline theorem inside this gate.

If a diagnostic alternative reveals a genuinely valuable new mechanism or shows that a substantive model change could strengthen the paper, route to the earliest affected research stage, implement the change there, and repeat all downstream certification. Stage 7.5A measures and attacks research strength; substantive theory engineering remains subject to rollback and recertification.

## Contribution Robustness Certificate

For each headline claim record:

- canonical claim and mechanism invariant;
- baseline assumptions plausibly carrying the result;
- pre-specified alternative formulation(s);
- ex ante survival/failure criterion;
- re-solved equilibrium/proof artifact;
- result under each alternative;
- abstract sufficient conditions or identified failure boundary, if available;
- classification: `PORTABLE`, `CONDITIONALLY PORTABLE`, `MODEL-SPECIFIC`, `INSTITUTION-SPECIFIC`, or `FALSIFIED`;
- strongest manuscript wording licensed by that classification;
- prohibited stronger wording;
- stop-rule status and whether further generality engineering is authorized.

Stage 12 must consume this certificate as an input. Stage 12 may not reinterpret a `MODEL-SPECIFIC` claim as portable merely because a preferred journal has a higher generality bar.

## Formal Verification Gate

Stage 7.5A may issue `GO` only if the project records exactly one acceptable state:

- `FORMAL VERIFICATION PASS`; or
- `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

`FORMALIZATION NOT APPLICABLE` requires a claim-specific reason explaining why neither full nor targeted proof-assistant formalization would materially improve assurance. Cost or inconvenience alone is not sufficient if a small proof-critical core can usefully be checked.

Blocking states include `NOT TESTED`, `PLANNED`, failed compilation, stale formal theorems after scope changes, unresolved statement-fidelity mismatch, unexplained proof placeholders/axioms, or a formal certificate that overstates what the assistant actually proves.

Proof-assistant acceptance is not independent evidence that the economic assumptions/case partition are correct unless those objects are formalized. Formal verification therefore cannot replace Stage 4A globality, multiplicity, continuation, counterexample certification, or the economic portability tests above.

## Kill tests

Fail or downgrade the relevant claim if:

- an alternative formulation is chosen or redesigned after seeing results in order to preserve the preferred sign;
- a cosmetic perturbation is presented as evidence of economic portability;
- the alternative model is not re-solved on its own valid strategy/equilibrium domain;
- a portability failure is omitted from the claim-scope ledger or described only as an unimportant numerical exception;
- two meaningful pre-specified portability attacks overturn the same claimed cross-model mechanism, no abstract sufficient-condition theorem survives, and the manuscript nevertheless continues to call the mechanism general/robust;
- a broad-function-class strict comparative static is not implied by stated restrictions;
- curvature/uniqueness is generalized beyond available derivatives;
- a parametric result is relabeled generic;
- numerical robustness is called proof;
- an existence result is called universal uniqueness;
- a local result is called global;
- a sufficient condition is called necessary-and-sufficient;
- a constrained benchmark is mislabeled first best;
- manuscript prose exceeds the theorem/equilibrium/portability certificates;
- an admissible counterexample exists inside the claimed class;
- formal-verification applicability remains unclosed; or
- an applicable formal certificate has a material statement-fidelity/build/placeholder/conclusion-smuggling defect.

## Verdict and routing

- `GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS` → Stage 8, but only after the Contribution Robustness Certificate is complete and the embedded Formal Verification Gate is closed with an acceptable state.
- `CONDITIONAL GO` → earliest affected stage; pure wording inflation or formal-source/build defects with unchanged mathematics may be corrected and re-audited here, but substantive strengthening, missing/false mathematics, or a new mechanism reopens the appropriate earlier research stage.
- `NO-GO` → reopen the earliest invalidated stage or terminate.

A narrow exact theorem can pass. A claim may pass as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` when that is its actual research strength. The gate penalizes overclaiming and result-driven rescue, not specialization.

---

# Stage 8 — Canonical Theory Freeze

## Objective

Freeze the theoretical object before manuscript construction.

## Entry hard gate

Stage 8 is blocked unless the project has:

- Stage 4A `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`;
- Stage 7.5A `GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS`; and
- a closed Stage-7.5A Formal Verification Gate with `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

## Freeze at minimum

- research question and contribution statement;
- players, objectives, timing, information, complete strategy/choice sets;
- utility/demand, technology/costs, contracts/transfers;
- parameter restrictions and admissible function classes;
- equilibrium concept;
- baseline equilibrium objects;
- main and welfare propositions with exact conditions and quantifiers;
- proof/evidence status;
- approved robustness scope;
- empirical/institutional interpretation;
- closest-paper distinction;
- explicit claims not made;
- Stage-4A theorem certificates;
- Stage-7.5A claim-scope/quantifier certificates;
- Stage-7.5A Contribution Robustness Certificate, including per-claim portability classifications, tested alternatives, failure boundaries, and stop-rule status;
- formal-verification applicability state and certificate/N-A rationale;
- paper-claim ↔ formal-theorem mapping and explicit non-formalized scope where applicable;
- proof-assistant/toolchain/library/build and axiom/placeholder provenance where applicable;
- benchmark-definition register;
- counterexample/regression-test register.

For sequential/game-theoretic models additionally freeze off-path history classes, continuation-equilibrium status, active-set/corner/order/participation handling, solver outcome taxonomy, multiplicity/nonexistence/selection assumptions, and independent direct-payoff/allocation verification artifacts.

Classify each proposition as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`. Where formal verification is used, separately classify the formal coverage as `FULL CLAIM`, `PROOF-CRITICAL CORE`, or another exact bounded scope.

Changes after freeze require explicit theory-change control and repetition of every affected gate, including Stage 4A/7.5A and the Formal Verification Gate where correctness, scope, formal theorem statements, or encoded assumptions are affected.

---

# Stage 9 — Repository / Reproducibility Setup

## Objective

Create the production research repository only after the theory is frozen.

## Recommended components

- modular LaTeX manuscript;
- bibliography;
- symbolic/numerical verification scripts;
- deterministic figure/table generation;
- tests and regression tests;
- `theorem_certificates/` or equivalent directory containing Stage-4A and Stage-7.5A certificates;
- `formal/` or equivalent directory for applicable proof-assistant source, toolchain/dependency locks, build instructions, and formal certificate;
- CI target that rebuilds applicable formal artifacts and checks proof placeholders where practical;
- counterexample and benchmark-definition artifacts;
- Makefile or equivalent build orchestration;
- dependency/environment specification;
- CI where feasible;
- decision log and provenance notes.

If the project recorded `FORMALIZATION NOT APPLICABLE`, retain that rationale with the frozen theorem-certification artifacts rather than silently omitting formal-verification status.

Never reset to an old reference SHA without checking the latest remote state.

---

# Stage 10 — Section-by-Section Paper Construction

## Objective

Build the manuscript in dependency order and establish the Figure/Table Architecture before finalizing the Introduction.

## Recommended order

1. Model
2. Equilibrium characterization
3. Main propositions
4. Welfare
5. Robustness/extensions
6. Institutional/empirical bridge
7. Related literature
8. Figure/Table Architecture Gate
9. Introduction
10. Discussion
11. Conclusion

## Exposition Architecture Gate

Before finalizing the Introduction, apply `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md` and create an exposition architecture for the manuscript.

At minimum:

- choose the appropriate exposition profile: theory-first, structural/quantitative/empirical, correction/comment/reassessment, or a justified alternative;
- map each main section to one dominant function and separate background facts from modeling choices;
- define a reader-arrival budget for the question, main finding, core primitives/data, full core model or identification logic, and first headline result;
- ensure economically material model primitives, timing, information, strategies, payoffs, constraints, equilibrium concepts, and benchmark definitions are not scattered across unrelated sections;
- run the main-text necessity test and identify obvious `APPENDIX` / `DELETE` candidates;
- run the five-exhibit thought experiment for full-length papers, adjusted downward for short notes/corrections;
- preserve assumptions, scope conditions, evidence, and formal-verification boundaries even when compressing.

Recommended production artifact: `EXPOSITION_ARCHITECTURE.md`.

Paper-specific page landmarks are soft diagnostics only. Current journal/article-type requirements control.

## Figure/Table Architecture Gate

Assign every headline theorem, comparative static, welfare result, benchmark contrast, robustness result, and scope condition one primary vehicle: theorem/proposition, figure, table, numerical illustration, or concise prose.

Every quantitative figure/table must be generated from verified scripts or authoritative sources, preserve actual economic scale/sign/domain, be regression-checked at representative values/thresholds when feasible, retain source/generator files, avoid arbitrary normalization presented as the economic object, and be interpreted in the manuscript.

There is no minimum visual count.

## Exit criterion

Each section compiles, matches the frozen theory and theorem certificates, and is integrated through controlled changes. Every headline result has an explicit exposition vehicle and every required figure/table is reproducibly implemented or has a documented blocker. The exposition architecture is explicit, the Introduction is not finalized before that architecture exists, and no known reader-arrival or section-purity blocker is deferred to Stage 14.

---

# Stage 11 — Robustness / Referee Attack Gate

## Objective

Try to reject the full manuscript before external referees do.

Stage 11 is not a substitute for Stage 4A or 7.5A. It is a late independent layer that checks whether exposition, extensions, journal framing, or post-freeze implementation reintroduced vulnerabilities.

## Mandatory attacks

Attack at least:

- classic-result/relabeling;
- **known-model-in-disguise / theorem-absorption attack**, including recentering, normalization, variable elimination, matrix/KKT form, standard game-class mapping, and constraint-geometry reduction;
- whole-game novelty and generalization redundancy;
- ad hoc assumptions and results built into assumptions;
- alternative demand/contract/information structures;
- participation/corner/boundary/regime-switch behavior;
- welfare mechanicality;
- institutional specificity and external validity;
- numerical-not-proof;
- proof/notation inconsistency;
- journal fit/contribution level;
- exposition/claim inflation;
- theorem quantifier inflation relative to Stage-7.5A certificates;
- portability/classification inflation relative to the Stage-7.5A Contribution Robustness Certificate;
- benchmark terminology drift;
- global/SPNE claims relative to Stage-4A certificates;
- proof-assistant scope inflation relative to the frozen formal-verification certificate;
- stale or diverged formal theorem statements/hypotheses after post-freeze manuscript or theory edits.

For sequential models independently reconstruct at least one material continuation/deviation from primitives, deliberately search for a finite deviation leaving the regular branch, and inspect all `None`/NaN/invalid/nonconvergent code outcomes.

For broad theorem/generalization claims independently attempt at least one admissible-function counterexample or assumption-relaxation attack rather than merely rereading the production proof.

For every theory manuscript whose Stage-4 canonicalization identified a plausible standard parent class, independently repeat the strongest **known-model-in-disguise** reduction at Stage 11 and verify that the manuscript's contribution statement is consistent with the Stage-6 theorem-absorption map. If the headline theorem can now be obtained as a direct specialization/corollary of prior work, record a novelty certification regression and route back to Stage 6 (or earlier if the research question itself is invalidated).

Where formal verification is applicable, inspect the paper-claim ↔ formal-theorem map and explicit non-formalized scope. Do not infer that a green Lean/Coq/Isabelle/etc. build certifies unencoded demand, equilibrium, or case-partition facts.

Classify attacks as `FATAL`, `MAJOR BUT FIXABLE`, or `MINOR`.

If Stage 11 discovers a failure that Stage 4A or 7.5A should have caught, including a manuscript claim that exceeds the frozen portability classification or suppresses a material negative portability result, record it explicitly as a **certification regression** and route to the earliest affected stage. Do not patch it only in prose. A material change to a formally certified theorem or encoded hypothesis also marks the formal certificate stale.

---

# Stage 12 — Journal Positioning

## Objective

Choose journals based on the actual surviving contribution, not desired prestige, verify that the ranked shortlist was drawn from a sufficiently broad candidate universe, and explicitly match each candidate journal's demonstrated editorial bar to the **certified** strength of the theory.

Stage 12 is where journal-specific calibration occurs. Stage 7.5A is deliberately journal-neutral.

## Mandatory tasks

Before ranking journals:

- ingest the Stage-7.5A **Contribution Robustness Certificate** and Stage-11 surviving contribution set;
- treat the portability classifications (`PORTABLE`, `CONDITIONALLY PORTABLE`, `MODEL-SPECIFIC`, `INSTITUTION-SPECIFIC`, `FALSIFIED`) as fixed research evidence unless a later substantive defect reopens an earlier stage;
- construct a broad candidate universe from the paper's surviving field/audience, contribution and article type, methodological level, manuscript scale, and any materially relevant geographic or institutional audience;
- do not start from prestige, a remembered target, or a shortlist inherited from prior submissions;
- cross-check the candidate universe against journals represented in the closest literature from Stages 2/6/11. Treat those venues as omission diagnostics, not automatic targets;
- for any obvious field journal or repeatedly represented relevant literature venue that is not treated as a serious candidate, record an explicit exclusion reason;
- for correction, comment, replication, re-examination, or closely related source-audit papers, explicitly consider the target/source paper's journal unless a documented exclusion reason applies;
- preserve a candidate-universe ledger or equivalent record showing discovery path, serious-candidate status, and inclusion/exclusion rationale.

Then, for each serious candidate:

- read current aims/scope and recent related papers;
- compare model sophistication, article type, and contribution style with actual publications;
- compare the journal's demonstrated generality/robustness expectations with the Contribution Robustness Certificate rather than assuming that journal rank mechanically determines required theory;
- estimate desk-reject risk and likely referee objections;
- assess whether empirical content is expected;
- identify whether the paper fits as general theory, conditional/applied theory, model-specific theory with explicit boundaries, institutional application, correction/note, or another supported article type;
- define stretch, primary, realistic fallback, and safety-net routes when appropriate.

If a candidate journal appears to require materially stronger generality than the frozen certificate supports, downgrade or reject that **journal candidate**. Do not reopen theory merely to preserve a preferred journal. A new substantive research program may be authorized separately, but it must roll back to the earliest affected research stage and repeat downstream certification.

Do not distort substantive economics to fit a preferred journal family.

## Journal-fit matrix

For each serious candidate, preserve an auditable mapping:

`certified contribution strength → recent comparable papers / official scope → fit or mismatch → desk/referee risk`.

The matrix must distinguish descriptive evidence from judgment. Journal rank, impact factor, quartile, or prestige is not a substitute for evidence about the kind of contribution the journal actually publishes.

## Completeness gate

Stage 12 may not close merely because one journal fits well. Before selecting the primary target, ask whether any obvious field venue or materially relevant venue surfaced by the closest-literature cross-check was never evaluated. If yes, evaluate it or record a reasoned exclusion.

A later discovery that a material candidate was omitted is a **journal-positioning completeness regression**. Reopen Stage 12 and rerun the ranking with the enlarged candidate set. Do not reopen the frozen theory or Stage 11 unless the new journal analysis itself exposes a substantive research defect.

---

# Stage 13 — Full-Paper Integration

## Objective

Turn independently correct sections into one coherent argument and reconcile the Stage-10 figure/table architecture with the selected journal.

## Audit

Apply `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md` to the actual integrated manuscript before submission QA. Stage 13 is the primary streamlining gate.

- select/confirm the article-type exposition profile;
- run the Introduction compression test: question, importance, setting/model choice, finding, method, novelty, and scope should be discoverable with low reader search cost;
- run the section-purity test and remove model assumptions from Background-style prose unless the placement is explicitly justified;
- rerun the reader-arrival budget using actual page numbers/order;
- classify major sections, subsections, exhibits, and paragraph clusters as `CORE`, `HELPFUL`, `APPENDIX`, or `DELETE`;
- rerun the five-exhibit thought experiment and challenge all lower-priority exhibits for merger, Appendix relocation, or deletion;
- remove repetitive contribution statements, duplicated intuition, redundant literature exposition, and main-text/appendix duplication;
- after compression, verify that assumptions, theorem domains, quantifiers, evidence, caveats, source links, and formal-verification boundaries remain intact;
- preserve an `EXPOSITION_STREAMLINING_REPORT.md` or equivalent auditable artifact.
- Introduction states question, mechanism, result, and contribution without exceeding the Stage-7.5A claim-scope ledger.
- Related Literature is organized by conceptual relationship.
- Model introduces no assumptions solely to rescue prose.
- Results prove rather than narrate.
- Discussion interprets scope rather than enlarging it.
- Conclusion introduces no new claims.
- Terminology/notation are consistent.
- Every contribution claim maps to a verified theorem and prior-art distinction.
- Every retained figure/table maps to a verified generator/source and is correctly captioned/referenced.
- Any statement about formal verification matches the frozen formal-verification certificate and explicit non-formalized scope.
- Journal-specific figure/table rules are incorporated without changing substantive results.

Substantive inconsistency triggers rollback to the earliest affected stage.

---

# Stage 14 — Submission QA

## Objective

Verify the complete submission package, including mathematical artifacts and artwork compliance.

## Mandatory checks

- fresh build from a clean environment;
- all applicable symbolic/numerical tests pass;
- theorem-certificate artifacts referenced by the freeze remain present and consistent;
- when formal verification is applicable, the frozen proof-assistant source/toolchain is present, the formal target rebuilds cleanly where feasible, placeholder/axiom checks remain valid, and the submitted manuscript does not overstate formal coverage;
- when formalization was `NOT APPLICABLE`, the recorded rationale remains attached to the frozen certification record;
- quantitative figures/tables regenerate and agree with reported values/signs/thresholds;
- current journal artwork/file/format rules are checked and dated;
- fonts/resolution/accessibility/legibility are satisfactory where required;
- all citations and cross-references resolve;
- journal formatting/anonymity/supplement/disclosure requirements are satisfied;
- abstract, highlights, cover letter, manuscript, theorem scope, and any formal-verification claim agree;
- final PDF is inspected page by page.
- the final PDF passes the Stage-13 exposition architecture/streamlining audit: Introduction compression, section purity, reader-arrival budget, exhibit scarcity, and concise/no-new-claims conclusion; any structural failure reopens Stage 13 rather than being solved by an unreviewed late rewrite.

Use `checklists/SUBMISSION_CHECKLIST.md`, `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md`, `checklists/FIGURE_TABLE_CHECKLIST.md`, and the frozen `checklists/FORMAL_VERIFICATION_CHECKLIST.md` certificate/N-A rationale where applicable.

A substantive mathematical, novelty, theory, welfare, institutional, claim-scope, or formal-statement mismatch triggers rollback to the earliest affected stage and a fresh downstream QA cycle.

---

# Stage 15 — Submission Freeze

## Objective

Create an immutable, auditable submission state.

## Freeze

- canonical commit SHA/tag;
- manuscript PDF and source archive;
- appendices/supplement;
- verification outputs and theorem certificates;
- formal-verification source, toolchain/dependency lock, build certificate, claim mapping, and explicit non-formalized scope where applicable, or the recorded N/A rationale;
- final figures/tables and generator/source provenance;
- cover letter and journal-specific files/metadata;
- disclosure statement where required.

After submission freeze, substantive changes reopen affected stages; no silent theory edits.

---

# 3. Cross-stage rules

## 3.1 Literature integrity and continuity

Do not invent citations, metadata, propositions, or novelty claims. Stage 2 establishes the baseline literature ledger; later searches are incremental and purpose-specific. Preserve the distinction between component overlap and whole-game absorption throughout.

## 3.2 Mathematical certification, formal verification, and independence

Where symbolic derivation is feasible, independently verify it. Never treat an FOC solution as equilibrium without SOC/KKT, feasibility, relevant constraints, and—when claimed—global best-response verification.

For sequential games, re-solve material continuation games rather than extending an on-path formula beyond its validity domain. Solver failures fail closed.

For all headline theorem-bearing theory projects:

- Stage 4 constructs and verifies;
- Stage 4A independently tries to falsify correctness/globality and records preliminary formal-verification applicability/targets;
- Stage 7.5A independently tries to falsify scope/generality/benchmark language and closes the Formal Verification Gate;
- Stage 11 repeats high-stakes attacks at the manuscript level.

Formal verification uses `checklists/FORMAL_VERIFICATION_CHECKLIST.md`. It should target the highest-value proof-critical core rather than defaulting to complete-model formalization. Lean 4/mathlib is the recommended default for new formal artifacts when no other proof assistant is established, but another auditable proof assistant may be used when better matched to the project.

For applicable formalization, preserve exact theorem signatures, quantifier/domain mapping, hypotheses supplied rather than proved, explicit non-formalized model scope, toolchain/library/dependency provenance, clean build/CI evidence, and axiom/placeholder audit. A condition structure or encoded profit formula is not a formal proof that the condition/formula follows from the economic primitives unless that bridge is itself formalized.

Whenever feasible, the adversarial reviewer/model/implementation should differ from the construction path. Re-running the same solver or asking the same derivation path to confirm itself is reproduction, not independent certification. A proof-assistant build is also not, by itself, the independent Stage-4A economic/globality attack.

A project must retain theorem certificates, formal-verification state, and counterexamples as research artifacts. A material `NOT TESTED` field is not equivalent to `PASS`.

## 3.3 Theorem quantifier discipline

Every headline theorem must have a formal scope. Distinguish local from global, existence from uniqueness, sufficient from necessary, parametric from generic, baseline from robustness, and numerical evidence from proof.

A theorem may be narrow. It may not be broader than its proof.

A formal theorem may also be narrower than the paper theorem. In that case the paper may claim only that the narrower proof-critical component is formally certified unless the remaining bridge is separately formalized.

## 3.4 Benchmark terminology discipline

Welfare labels are mathematical claims. `First best` requires the unrestricted relevant planner problem over the relevant feasible choices. If instruments, allocations, technology, information, commitment, or R&D allocation are fixed/restricted, use the exact constrained/second-best/fixed-allocation label.

## 3.5 Negative results are first-class outputs

A stage that proves a desired proposition false succeeds by killing a weak branch. Preserve counterexamples and rejected branches.

Formalization failures that expose false statements, missing hypotheses, or invalid quantified inequalities are also research evidence and must not be hidden by weakening the formal statement without corresponding analytic/scoped change control.

## 3.6 No complexity rescue

Complexity must solve a diagnosed economic deficiency and may change only under the Stage-5 one-margin rule. Generalization/unification is not exempt.

Complete-model formalization is not required merely for prestige. Formalization effort should follow risk and proof-critical value.

## 3.7 Contribution discipline

Variables, functional forms, and applications are not automatically contributions. A contribution should be an economic mechanism, theorem, comparative-static reversal, organizational result, welfare implication, or strategically substantive generalization/unification that survives prior-art comparison.

Formal verification strengthens assurance; it is not itself a substitute for an economic contribution.

## 3.8 Exposition architecture integrity

Exposition is a cross-stage scientific-communication object, not a cosmetic Stage-14 concern. Apply `checklists/EXPOSITION_STREAMLINING_CHECKLIST.md` across Stages 7/10/13/14.

Stage 10 designs section roles, reader-arrival targets, model/evidence consolidation, and the Figure/Table Architecture. Stage 13 performs the aggressive streamlining pass on the integrated manuscript. Stage 14 verifies the resulting architecture and rolls back rather than performing a late substantive rewrite.

Figures/tables are evidence-bearing manuscript objects, not decoration. They may not create a weaker proof standard or hide theorem scope restrictions. Generic page or exhibit counts are diagnostics only; current journal/article-type rules and scientific completeness control.

## 3.9 Provenance and evidence maturity

Distinguish remembered/AI/scratch outputs from reproduced project artifacts and submission-level re-verification. Do not silently upgrade conjectures or temporary computations into theorems.

Distinguish analytic proof, numerical evidence, independent adversarial certification, and proof-assistant certification. Each has a different evidentiary scope.

## 3.10 Rollback and stale downstream outputs

If a later stage invalidates an earlier canonical input, return to the earliest affected stage and mark dependent downstream outputs stale. A Stage-11 mathematical failure normally reopens Stage 4/4A; a scope/generality failure normally reopens Stage 7.5A and any earlier stage whose theorem is actually false.

A false theorem or missing economic condition exposed by formalization reopens the earliest affected analytic stage. A formal-source/build defect with unchanged certified mathematics returns to the Stage-7.5A Formal Verification Gate. A material theorem/quantifier/encoded-hypothesis change marks the formal certificate stale and blocks refreeze until rebuilt and re-audited.

## 3.11 Decision logs

Preserve major rejected branches, discovered counterexamples, certificate failures, formalization applicability decisions, formalization failures, repairs, and reasons for routing decisions.

## 3.12 Live journal compliance and portal evidence

After a primary journal is selected, journal compliance is evidence-bearing. Stage 12 creates an initial Journal Requirements Ledger; Stage 13 integrates verified requirements without guessing unresolved ones; Stage 14 re-opens and dates current official requirements, verifies the exact source/submission package, and fails closed on material `UNVERIFIED` or unresolved `CONFLICT` items; Stage 15 reconciles the authenticated submission record and portal-generated PDF where applicable before `SUBMITTED` may be declared.

For the actual submission, direct current editorial-office instructions outrank explicit authenticated-portal rules, which outrank journal-specific official guidance, which outranks publisher-wide guidance. Memory, prior submissions, and repository notes are non-authoritative when a more specific current source exists.

If a material requirement remains unresolved after current journal/publisher/portal research, obtain clarification from the journal/editorial office or submission support before full Stage-14 PASS. Portal acceptance alone is not proof of technical compliance.

---

# 4. Companion materials

Reusable Stage templates, theorem/math/literature verification checklists, the formal-verification checklist, and worked examples live in this repository under the canonical hierarchy.

Future extensions may add empirical/cross-discipline variants, machine-readable theorem certificates, automated property-based testing, and release tooling after explicit audit.

This document is the canonical workflow architecture. Stage-specific templates may elaborate it but may not silently weaken its gates.
