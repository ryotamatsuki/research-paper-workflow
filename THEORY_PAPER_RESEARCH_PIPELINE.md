# Theory Paper Research Pipeline

Version: v2.0

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
2. **Stage 7.5A — Generality / Quantifier Red-Team Gate**: attacks theorem scope, functional-form generality, quantifiers, robustness language, and planner/benchmark terminology before the theory can be frozen.

The required routing is therefore:

`Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8`.

Neither Stage 4A nor Stage 7.5A may be bypassed by a green symbolic check, CI run, production solver, or prior `GO`.

The workflow uses a three-layer mathematical defense:

- **construction/verification layer** — solve and verify the model at Stage 4;
- **independent adversarial layer** — Stage 4A and Stage 7.5A attempt to falsify correctness and scope without inheriting the construction path;
- **full-manuscript hostile layer** — Stage 11 repeats high-stakes attacks after exposition has been added and treats any newly discovered mathematical failure as a rollback event and workflow regression signal.

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

For theorem-bearing stages preserve a claim/proposition register. For headline mathematical claims, use `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` as required by Stage 4A and Stage 7.5A.

For manuscript exposition, use the four-step lifecycle:

- Stage 7 — identify candidate exposition vehicles;
- Stage 10 — design and implement the figure/table architecture;
- Stage 13 — integrate for the target journal;
- Stage 14 — verify regeneration, numerical integrity, artwork compliance, source completeness, and legibility.

There is no minimum figure/table quota. Every visual must materially reduce the reader's cost of understanding a verified result.

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
- preserve all counterexamples as regression artifacts.

## Hard gate

A material theorem-certificate field marked `NOT TESTED` blocks `GO` unless explicitly `NOT APPLICABLE` with a valid reason.

A headline claim fails certification if it relies on local conditions as global proof, an omitted profitable boundary/regime deviation, unresolved continuation treated as unprofitable, a regular formula outside its domain, solver failure filtering, an implementation-independent contradiction, or a benchmark label inconsistent with the optimization problem.

## Verdict and routing

- `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS` → Stage 6.
- `CONDITIONAL GO` → earliest affected stage; proof/equilibrium/domain errors normally reopen Stage 4, while exactly one authorized economic modification may route to Stage 5 and must then repeat Stage 4 and 4A.
- `NO-GO` → terminate or reopen Stage 4/3/0 as required.

No project may bypass Stage 4A because Stage 4, CI, symbolic algebra, or the production solver is green.

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
- Re-open closest literature in light of the solved result.
- Distinguish component novelty, whole-game novelty, and theorem novelty.
- Re-run whole-game absorption against the actual model.
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

# Stage 7.5A — Generality / Quantifier Red-Team Gate

## Objective

Certify that every headline theorem, robustness statement, welfare benchmark, and contribution sentence states exactly the scope actually proved.

This stage attacks over-generalization rather than merely rechecking baseline algebra.

## Mandatory tasks

For every headline theorem/proposition and material robustness/generalization statement:

- rewrite the claim in formal quantifier form (`for all`, `exists`, `unique`, `generic`, `local`, `global`, etc.);
- list assumptions actually used, separating economic assumptions, shape restrictions, parameter restrictions, regularity, normalization, and tractability;
- compare formal theorem scope with the strongest abstract/introduction/contribution/welfare/robustness prose;
- distinguish baseline closed form, restricted function class, sufficient-condition theorem, numerical robustness evidence, conjectured generality, and truly general theorem;
- for broad function classes, identify which derivative/order restrictions are required for each sign, concavity, uniqueness, or threshold conclusion;
- construct admissible counterexample functions designed to reverse claimed comparative statics/curvature/orderings;
- stress-test nonquadratic, low/high-curvature, boundary, and near-boundary cases when the baseline is convenient/parametric;
- verify that a parametric-family result is not called generic without a separate argument;
- write the planner optimization problem and feasible choice set for every welfare benchmark and reserve `first best` for the unrestricted relevant planner problem;
- produce a claim-scope ledger mapping each manuscript claim to theorem certificate, proof, robustness artifact, maximum defensible wording, and prohibited stronger wording;
- reapply the theorem-certification checklist whenever claim scope changed after Stage 4A.

## Kill tests

Fail the gate if a broad-function-class strict comparative static is not implied by stated restrictions, curvature/uniqueness is generalized beyond available derivatives, a parametric result is relabeled generic, numerical robustness is called proof, an existence result is called universal uniqueness, a local result is called global, a sufficient condition is called necessary-and-sufficient, a constrained benchmark is mislabeled first best, manuscript prose exceeds the certificate, or an admissible counterexample exists inside the claimed class.

## Verdict and routing

- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS` → Stage 8.
- `CONDITIONAL GO` → earliest affected stage; pure wording inflation may be corrected and re-audited here, but missing/false mathematics reopens Stage 4/7 as appropriate.
- `NO-GO` → reopen the earliest invalidated stage or terminate.

A narrow exact theorem can pass. The gate penalizes overclaiming, not specialization.

---

# Stage 8 — Canonical Theory Freeze

## Objective

Freeze the theoretical object before manuscript construction.

## Entry hard gate

Stage 8 is blocked unless the project has:

- Stage 4A `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`; and
- Stage 7.5A `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`.

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
- benchmark-definition register;
- counterexample/regression-test register.

For sequential/game-theoretic models additionally freeze off-path history classes, continuation-equilibrium status, active-set/corner/order/participation handling, solver outcome taxonomy, multiplicity/nonexistence/selection assumptions, and independent direct-payoff/allocation verification artifacts.

Classify each proposition as `PROVED`, `CONDITIONAL`, `NUMERICALLY SUPPORTED ONLY`, `CONJECTURE`, or `REJECTED`.

Changes after freeze require explicit theory-change control and repetition of every affected gate, including Stage 4A/7.5A where correctness or scope is affected.

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
- counterexample and benchmark-definition artifacts;
- Makefile or equivalent build orchestration;
- dependency/environment specification;
- CI where feasible;
- decision log and provenance notes.

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

## Figure/Table Architecture Gate

Assign every headline theorem, comparative static, welfare result, benchmark contrast, robustness result, and scope condition one primary vehicle: theorem/proposition, figure, table, numerical illustration, or concise prose.

Every quantitative figure/table must be generated from verified scripts or authoritative sources, preserve actual economic scale/sign/domain, be regression-checked at representative values/thresholds when feasible, retain source/generator files, avoid arbitrary normalization presented as the economic object, and be interpreted in the manuscript.

There is no minimum visual count.

## Exit criterion

Each section compiles, matches the frozen theory and theorem certificates, and is integrated through controlled changes. Every headline result has an explicit exposition vehicle and every required figure/table is reproducibly implemented or has a documented blocker.

---

# Stage 11 — Robustness / Referee Attack Gate

## Objective

Try to reject the full manuscript before external referees do.

Stage 11 is not a substitute for Stage 4A or 7.5A. It is a late independent layer that checks whether exposition, extensions, journal framing, or post-freeze implementation reintroduced vulnerabilities.

## Mandatory attacks

Attack at least:

- classic-result/relabeling;
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
- benchmark terminology drift;
- global/SPNE claims relative to Stage-4A certificates.

For sequential models independently reconstruct at least one material continuation/deviation from primitives, deliberately search for a finite deviation leaving the regular branch, and inspect all `None`/NaN/invalid/nonconvergent code outcomes.

For broad theorem/generalization claims independently attempt at least one admissible-function counterexample or assumption-relaxation attack rather than merely rereading the production proof.

Classify attacks as `FATAL`, `MAJOR BUT FIXABLE`, or `MINOR`.

If Stage 11 discovers a failure that Stage 4A or 7.5A should have caught, record it explicitly as a **certification regression** and route to the earliest affected stage. Do not patch it only in prose.

---

# Stage 12 — Journal Positioning

## Objective

Choose journals based on the actual surviving contribution, not desired prestige.

## Mandatory tasks

- Read current aims/scope and recent related papers.
- Compare model sophistication and contribution type with actual publications.
- Estimate desk-reject risk and likely referee objections.
- Assess whether empirical content is expected.
- Define stretch, primary, realistic fallback, and safety-net routes when appropriate.

Do not distort substantive economics to fit a preferred journal family.

---

# Stage 13 — Full-Paper Integration

## Objective

Turn independently correct sections into one coherent argument and reconcile the Stage-10 figure/table architecture with the selected journal.

## Audit

- Introduction states question, mechanism, result, and contribution without exceeding the Stage-7.5A claim-scope ledger.
- Related Literature is organized by conceptual relationship.
- Model introduces no assumptions solely to rescue prose.
- Results prove rather than narrate.
- Discussion interprets scope rather than enlarging it.
- Conclusion introduces no new claims.
- Terminology/notation are consistent.
- Every contribution claim maps to a verified theorem and prior-art distinction.
- Every retained figure/table maps to a verified generator/source and is correctly captioned/referenced.
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
- quantitative figures/tables regenerate and agree with reported values/signs/thresholds;
- current journal artwork/file/format rules are checked and dated;
- fonts/resolution/accessibility/legibility are satisfactory where required;
- all citations and cross-references resolve;
- journal formatting/anonymity/supplement/disclosure requirements are satisfied;
- abstract, highlights, cover letter, manuscript, and theorem scope agree;
- final PDF is inspected page by page.

Use `checklists/SUBMISSION_CHECKLIST.md` and `checklists/FIGURE_TABLE_CHECKLIST.md`.

A substantive mathematical, novelty, theory, welfare, institutional, or claim-scope problem triggers rollback to the earliest affected stage and a fresh downstream QA cycle.

---

# Stage 15 — Submission Freeze

## Objective

Create an immutable, auditable submission state.

## Freeze

- canonical commit SHA/tag;
- manuscript PDF and source archive;
- appendices/supplement;
- verification outputs and theorem certificates;
- final figures/tables and generator/source provenance;
- cover letter and journal-specific files/metadata;
- disclosure statement where required.

After submission freeze, substantive changes reopen affected stages; no silent theory edits.

---

# 3. Cross-stage rules

## 3.1 Literature integrity and continuity

Do not invent citations, metadata, propositions, or novelty claims. Stage 2 establishes the baseline literature ledger; later searches are incremental and purpose-specific. Preserve the distinction between component overlap and whole-game absorption throughout.

## 3.2 Mathematical certification and independence

Where symbolic derivation is feasible, independently verify it. Never treat an FOC solution as equilibrium without SOC/KKT, feasibility, relevant constraints, and—when claimed—global best-response verification.

For sequential games, re-solve material continuation games rather than extending an on-path formula beyond its validity domain. Solver failures fail closed.

For all headline theorem-bearing theory projects:

- Stage 4 constructs and verifies;
- Stage 4A independently tries to falsify correctness/globality;
- Stage 7.5A independently tries to falsify scope/generality/benchmark language;
- Stage 11 repeats high-stakes attacks at the manuscript level.

Whenever feasible, the adversarial reviewer/model/implementation should differ from the construction path. Re-running the same solver or asking the same derivation path to confirm itself is reproduction, not independent certification.

A project must retain theorem certificates and counterexamples as research artifacts. A material `NOT TESTED` field is not equivalent to `PASS`.

## 3.3 Theorem quantifier discipline

Every headline theorem must have a formal scope. Distinguish local from global, existence from uniqueness, sufficient from necessary, parametric from generic, baseline from robustness, and numerical evidence from proof.

A theorem may be narrow. It may not be broader than its proof.

## 3.4 Benchmark terminology discipline

Welfare labels are mathematical claims. `First best` requires the unrestricted relevant planner problem over the relevant feasible choices. If instruments, allocations, technology, information, commitment, or R&D allocation are fixed/restricted, use the exact constrained/second-best/fixed-allocation label.

## 3.5 Negative results are first-class outputs

A stage that proves a desired proposition false succeeds by killing a weak branch. Preserve counterexamples and rejected branches.

## 3.6 No complexity rescue

Complexity must solve a diagnosed economic deficiency and may change only under the Stage-5 one-margin rule. Generalization/unification is not exempt.

## 3.7 Contribution discipline

Variables, functional forms, and applications are not automatically contributions. A contribution should be an economic mechanism, theorem, comparative-static reversal, organizational result, welfare implication, or strategically substantive generalization/unification that survives prior-art comparison.

## 3.8 Exposition architecture integrity

Figures/tables are evidence-bearing manuscript objects, not decoration. They may not create a weaker proof standard or hide theorem scope restrictions.

## 3.9 Provenance and evidence maturity

Distinguish remembered/AI/scratch outputs from reproduced project artifacts and submission-level re-verification. Do not silently upgrade conjectures or temporary computations into theorems.

## 3.10 Rollback and stale downstream outputs

If a later stage invalidates an earlier canonical input, return to the earliest affected stage and mark dependent downstream outputs stale. A Stage-11 mathematical failure normally reopens Stage 4/4A; a scope/generality failure normally reopens Stage 7.5A and any earlier stage whose theorem is actually false.

## 3.11 Decision logs

Preserve major rejected branches, discovered counterexamples, certificate failures, repairs, and reasons for routing decisions.

---

# 4. Companion materials

Reusable Stage templates, theorem/math/literature verification checklists, and worked examples live in this repository under the canonical hierarchy.

Future extensions may add empirical/cross-discipline variants, machine-readable theorem certificates, automated property-based testing, and release tooling after explicit audit.

This document is the canonical workflow architecture. Stage-specific templates may elaborate it but may not silently weaken its gates.
