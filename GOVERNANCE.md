# Governance

Version: v2.9-candidate (unreleased; v2.8 is the last documented release)

## 1. Purpose

This repository defines reusable research workflows. Changes therefore affect future projects, not one manuscript. Governance favors traceability, explicit gates, reproducibility, independent verification, conservative theorem scope, and visible failure.

The repository should function as a research operating system, not an informal prompt dump.

---

## 2. Core governance principles

### 2.1 Evidence before claims

Do not state that a result, equilibrium, theorem scope, paper, journal requirement, institutional fact, or novelty claim has been verified unless the supporting source, proof, computation, and verification scope actually support the claim asserted.

When evidence is incomplete, state the limitation explicitly.

### 2.2 Negative results are retained

Rejected models, failed novelty claims, algebraic/equilibrium counterexamples, theorem-scope counterexamples, benchmark-definition failures, and hostile-referee objections are valuable outputs. Preserve them when they materially affect later research decisions.

### 2.3 No silent theory drift

After theory freeze, changes to players, timing, utility/demand, information, contracts, equilibrium concept, strategy domains, main propositions, theorem quantifiers, admissible function classes, welfare benchmarks, or contribution claims require explicit change control and re-validation of affected stages.

### 2.4 One diagnosed fix at a time

A failed minimal model or certification gate must not trigger uncontrolled feature accumulation. The next modification must address one precisely diagnosed deficiency.

### 2.5 No prestige-driven distortion

Target journals may affect exposition and robustness expectations, but may not determine the substantive result before the research is solved and certified.

### 2.6 Equilibrium certification must fail closed

For sequential/game-theoretic models, an on-path or regular-branch solution is not an SPNE/global-equilibrium certificate. Economically material upstream deviations must receive valid downstream continuations on the stated strategy/history domain.

`None`, NaN, exception, nonconvergence, invalid active set, violated interiority, or branch failure means `UNRESOLVED` unless nonexistence has separately been proved. It must never be treated as evidence that a deviation is unprofitable.

FOCs, SOCs, Hessians, positivity, and local interiority establish properties of a candidate/branch. They do not by themselves establish a global Nash equilibrium over unrestricted strategies.

Unresolved material continuations block Stage 4 `GO`, Stage 4A certification, theory freeze, and any later SPNE/subgame-perfect claim.

### 2.7 Theorem quantifiers must match proof scope

Every headline theorem/proposition must state its exact quantifiers, domain, assumptions, and evidence maturity.

Distinguish at minimum:

- local from global;
- existence from uniqueness;
- sufficient from necessary;
- weak from strict;
- parametric from generic;
- baseline result from restricted-class result;
- numerical robustness from proof;
- conjecture from theorem.

A narrow theorem is acceptable. An overstated theorem is not.

### 2.8 Benchmark labels are mathematical claims

Terms such as `first best`, `constrained first best`, `second best`, `fixed-allocation benchmark`, and `restricted-instrument optimum` must correspond to explicitly stated planner objectives and feasible choice sets.

`First best` is reserved for the unrestricted relevant planner problem. If relevant instruments, allocations, information, commitment, technology, or research allocation are fixed/restricted, use the exact constrained label.

### 2.9 Independent certification is distinct from reproduction

Re-running the same symbolic derivation, production solver, or code path is reproduction, not independent certification.

Whenever feasible, high-stakes theorem/equilibrium claims must receive a logically independent attack through a different model, clean-room derivation, separately written evaluator/solver, or equivalent method that does not inherit the production branch assumptions.

The canonical three-layer defense is:

1. Stage 4 — construction and verification;
2. Stage 4A / Stage 7.5A — independent adversarial certification of correctness/globality and scope/generality;
3. Stage 11 — full-manuscript hostile regression attack.

For a material independent attack, record the inputs exposed to the reviewer, the construction artifacts withheld during first reconstruction where feasible, the independent reasoning/evaluator path, and discrepancy reconciliation. A different model, agent, chat, or prompt alone does not establish logical independence. When a blind first pass is infeasible, disclose the shared inputs and justify a distinct attack path; duplicate execution is not independent certification.

### 2.10 Submission compliance must be evidence-bearing

For journal submission, current operational requirements must be verified from current evidence rather than memory, old repository assumptions, prior submissions, or generic system behavior.

For the actual submission, use the most specific current authority available: direct editorial-office instruction, then explicit authenticated-portal requirements, then journal-specific official guidance, then publisher-wide guidance. Lower-level evidence may not override a more specific current instruction.

Production projects must preserve an auditable Journal Requirements Ledger or equivalent. Material `UNVERIFIED` or unresolved `CONFLICT` items block full submission QA. If a material rule remains unresolved after current journal/publisher/portal research, obtain clarification from the editorial office or submission support before full PASS.

A portal accepting a file, allowing progression, or showing no warning is not by itself proof of editorial-office technical compliance.

### 2.11 Formal verification is applicability-gated, complementary, and fail-closed

Every theorem-bearing theory project must make an explicit formal-verification applicability decision before theory freeze. The decision may not be omitted because the project already passed symbolic, numerical, adversarial, or manuscript review.

Formal verification is normally warranted when a headline claim depends materially on proof-critical algebra, quantified inequalities, piecewise case logic, threshold/boundary reasoning, global-deviation inequalities, equilibrium-condition implications, welfare identities, or correction of a published mathematical result. Full formalization of the entire economic model is not required when a targeted proof-critical core yields substantial assurance.

The required Stage-7.5A pre-freeze state is exactly one of:

- `FORMAL VERIFICATION PASS`; or
- `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

`NOT TESTED`, `PLANNED`, failed compilation, stale formal statements, unexplained proof placeholders, or unresolved statement-fidelity gaps are not passing states.

Proof-assistant acceptance certifies the encoded statement from the encoded assumptions. It does not establish that the assumptions, demand correspondence, equilibrium domain, case partition, or economic interpretation were encoded correctly unless those objects are themselves formalized. Formal proof therefore complements rather than replaces Stage 4A independent adversarial certification and Stage 7.5A scope certification.

Where formal verification is applicable, projects must preserve the proof-assistant/toolchain/library provenance, claim-to-formal-theorem mapping, assumptions supplied rather than proved, axiom/placeholder audit, reproducible build evidence, and explicit scope not formalized. Use `checklists/FORMAL_VERIFICATION_CHECKLIST.md`.

### 2.12 Novelty must survive canonical-form and theorem-absorption review

A theory contribution may not be treated as new merely because the application, notation, institutional vocabulary, or exact closed-form expression is absent from prior papers.

For theorem-bearing work, Stage 4 must preserve an application-neutral canonical mathematical representation where reasonably possible. Stage 6 must search plausible standard parent classes and explicitly test whether headline results are direct specializations, boundary cases, or short corollaries of known general theorems. Stage 11 must repeat the strongest known-model-in-disguise attack on the final manuscript.

At minimum distinguish:

- theorem/mechanism novelty;
- new result within a known model class;
- application/interpretation novelty;
- empirical/institutional relevance;
- notation/relabeling only.

If a plausible parent theorem remains untested at the mapping/specialization level, a theorem-novelty claim fails closed. Search failure or absence of the same application-specific formula is not positive novelty evidence.

### 2.13 Journal candidate universes precede journal ranking

Stage 12 must construct a broad candidate-journal universe from the **actual surviving paper** before journals are ranked or a preferred target is defended.

Candidate generation should use the paper's field/audience, contribution and article type, methodological level, manuscript scale, and any materially relevant geographic or institutional audience. It must not begin from prestige, a remembered target, or a shortlist inherited from prior submissions.

The journals containing the closest literature from Stages 2/6/11 are a **completeness cross-check**, not an automatic target list. A journal is not a serious candidate merely because a close paper appeared there. Conversely, an obvious field journal or a venue repeatedly represented in close literature may not disappear silently: it must either be evaluated or receive an explicit exclusion reason.

For correction, comment, replication, re-examination, or closely related source-audit papers, the venue of the target/source paper has special archival relevance and must be explicitly considered unless a reason for exclusion is recorded. This conditional rule does not apply mechanically to ordinary original research.

Stage 12 should preserve a candidate-universe ledger or equivalent record showing how serious candidates entered the set and why plausible alternatives were excluded. Discovery of a material omitted venue after Stage-12 closure is a **journal-positioning completeness regression** and normally reopens Stage 12 only; it does not by itself invalidate the frozen theory or Stage-11 certification.

---

### 2.14 Material AI use must be provenance-tracked

Material AI assistance is permitted only with evidence that accurately distinguishes assistance, verification, and authorship/accountability.

From Stage 0 onward, projects must preserve a material-use record for AI activity that affects a research decision, adopted result, proof/counterexample path, code/formal artifact, literature assessment, manuscript text/structure, or submission declaration. The record may point to existing chats, commits, diffs, audit reports, test logs, and formal certificates; full transcript duplication is not required.

At minimum, the record should identify the tool/model when reasonably available, date, purpose, adopted artifact/decision, disposition, verification method, verification actor, evidence reference, and downstream effect.

Verification actors must be distinguished explicitly where material:

- `AUTHOR`;
- `AI`;
- `COMPUTATION`;
- `FORMAL`;
- `EXTERNAL HUMAN`.

A second AI, separate chat, or different prompt may strengthen an AI-side adversarial check, but it is not author verification or external human review.

### 2.15 Author accountability cannot be inferred from AI, code, or formal PASS

Before Stage 8 freeze, every central result or tightly related central-result set must have an auditable author intellectual-contribution record. It must show the author's substantive judgment about the research question/mechanism, assumptions, proof/equilibrium logic, limitations/failure boundaries, verification evidence, and maximum defensible claim.

A universal AI-free rediscovery or memorized re-proof is not required. However, reading an AI explanation, approving an AI audit, accepting a computation, or observing a green Lean/proof-assistant build is not by itself evidence that the author made or understood the substantive research judgment.

AI/adversarial review, deterministic computation, formal verification, and external human review are complementary evidence sources. They may not be silently relabeled as author verification.

Proof-assistant acceptance remains limited to the encoded statement under encoded assumptions. It does not establish authorship, author understanding, model-to-formal fidelity outside the mapping audit, unformalized case completeness, novelty, empirical relevance, or economic interpretation.

Use `checklists/AI_PROVENANCE_AUTHOR_ACCOUNTABILITY_CHECKLIST.md`.

### 2.16 AI disclosure must be evidence-matched and destination-specific

Stage 14 must reconcile the material AI-use record against the actual manuscript, Methods/appendix/repository documentation, manuscript-preparation declaration, cover letter, and portal fields required by the current target journal/publisher.

Do not use generic disclosure boilerplate that overstates what the author personally verified. A statement such as "all substantive claims were independently verified by the author" is permitted only when the author-verification record supports that scope.

Where the operative policy distinguishes research-method use from manuscript-preparation use, record and disclose them in the required locations accordingly.

SSRN-specific checks apply only when SSRN is an actual submission destination. In that case, re-check current official SSRN requirements, including disclosure locations and any bulk/high-volume-submission rules. Preserve the real research chronology. Do not manufacture submission spacing, dates, staged commits, or artificial process history to make activity appear normal.


### 2.17 Reviewer verifiability is distinct from correctness and reproducibility

A manuscript may contain a correct theorem and a reproducible computation while still failing scientific communication if a specialist referee cannot identify or audit the proof-critical bridge from primitives/evidence to the claimed result.

For theorem-bearing or technically dense manuscripts, the manuscript-facing package must expose enough structure for a competent specialist referee to:

- identify the mathematical/statistical object being solved or certified;
- follow non-routine derivation steps without guessing omitted conceptual bridges;
- distinguish local/branch calculations from global conclusions;
- identify the domain, assumptions, and aggregation linking intermediate objects to the headline result;
- understand what any computer-assisted, symbolic, numerical, interval, certificate, or formal-verification step actually certifies;
- understand why the certified property implies the paper's theorem/result; and
- locate the reproducible artifact for delegated mechanical computation.

This does **not** require printing every algebraic expansion, coefficient list, root-isolation trace, or proof-assistant kernel trace. Routine/repetitive algebra may be delegated to Appendix/Supplement/code. The main manuscript and its explicit cross-references must preserve proof-critical bridges.

Apply `checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md` across Stages 10/11/13/14 where applicable. A presentation-only failure normally returns to Stage 13; a derivation-architecture failure may return to Stage 10; a gap that exposes an unproved or false substantive claim returns to the earliest affected research stage.

### 2.18 Research search is bounded and evidence-bearing

Broad searches at Stages 0/3 may use a larger candidate bank, but this is an aid inside existing Stages, not a new Stage or replacement route. Preserve stable candidate IDs, source/puzzle provenance, contribution route, structural mechanism fingerprint, closest-literature evidence and reading depth, selection/disposition reasons, and the current batch budget. Merge structural duplicates rather than counting alternative wording as independent candidates.

Set a finite candidate, time, or compute budget before a broad batch. Novelty scores and generated-candidate counts prioritize attention; they do not establish novelty or research productivity. There is no universal requirement to generate 50–100 ideas or conduct a fixed number of random parameter draws. Expand the budget only for a recorded research reason, not to preserve a preferred result. Retain material rejected/deferred branches and revisit them only for new evidence or a genuinely distinct mechanism.

Use `templates/RESEARCH_SEARCH_REGISTER.md` or equivalent existing project records. Do not duplicate logs solely to satisfy a filename requirement or invent a retrospective research chronology.

### 2.19 Contribution selection precedes discretionary result-family expansion

Stages 3/4 must state the anticipated economic contribution in a short working memo. Stage 6 updates it against the actual Stage-4A-certified result and strongest prior-art threat before discretionary Stage-7 expansion. Record the closest result, exact surviving difference, economic consequence, evidence maturity, strongest objection, and reason for the next investment. This strengthens existing gates; it does not insert a new verdict or bypass Stage 4A, Stage 6, Stage 7.5, or Stage 7.5A. An early memo is not a manuscript and does not authorize full-paper construction before theory freeze.

Evaluate the contribution route actually claimed. New mechanisms, substantive new results within known models, generalization/unification, and economically consequential correction/reassessment have different novelty units. A correction must identify the source claim, establish the defect/corrected result, search prior corrections, and show what equilibrium, welfare, policy interpretation, or substantive economic understanding changes. A cosmetic algebraic repair does not automatically qualify for a paper; absence of a new mechanism does not automatically kill a substantive correction.

Related results may share a family/dependency register, but grouping does not transfer proof, novelty, scope, or submission authorization. Separate core results, necessary robustness, Appendix material, future research, and rejected claims. Every adopted material claim inherits the existing certification gates. New strategic primitives or headline claims require the existing rollback/change-control route. Family expansion is optional and budgeted; it does not authorize multiple papers, automatic extension, or reopening a frozen project without a diagnosed reason.

### 2.20 Economic significance and question-completeness are independent of correctness and novelty

A mathematically certified and genuinely distinctive result is not automatically a full-paper contribution. Before Stage 8, test (a) *what economic understanding changes*, (b) *why the field audience should care*, and (c) *whether the motivating question leaves a material explanatory, welfare, allocation, policy, or implementation question unanswered*. An unanswered question is not automatically a fatal defect: classify it as `IN SCOPE / ESSENTIAL FOLLOW-UP / BOUNDED LIMITATION / FUTURE PAPER / NOT APPLICABLE` with reasons and evidence.

For **policy-oriented** claims, distinguish identifying a failure from showing what *should* be done (a welfare benchmark) and what *could* work (feasible instruments, incentives, institutions, administration, information, finance). When practical implementation is central to the claimed contribution but absent, either (i) justify an intentionally diagnostic-only paper with a demonstrated field-journal/audience case, (ii) undertake one bounded pre-freeze mechanism exploration with independent novelty/mathematics audits, or (iii) reframe, downgrade, or stop the full-paper route. Pure theory, corrections, comments, and diagnostic work are **not** universally required to propose a policy instrument, create a new theorem, or add data.

The **Contribution Completeness & Editorial Value Audit** belongs to Stage 6 (working memo), Stage 7 (welfare/institution), Stage 7.5 (**mandatory pre-freeze decision**), Stage 11 (independent editorial red-team), and Stage 12 (journal-specific fit). Apply `checklists/ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md` or equivalent evidence. It must record: a source-grounded closest-paper distinction, a one-paragraph editor-facing reason to publish, the strongest missing-question attack, at least a bounded `BASELINE ONLY / MINIMAL POLICY OR MECHANISM EXTENSION / REFRAME OR NOTE` counterfactual when material, whether the extension would create *new economics* instead of cosmetic complexity, and a reasoned adoption/deferral decision. A `GO` with an unresolved **essential** question-completeness objection is prohibited; use the existing `CONDITIONAL GO` or `NO-GO` route. An already frozen paper requires normal rollback and re-certification before adding new theory.

This is a **v2.9 minor refinement proposal** inside existing stages and routing, not a newly numbered Stage, a relaxation of mathematical/novelty gates, or a requirement to satisfy editor preferences by arbitrary theory expansion.

### 2.21 Phase-calibrated novelty: legitimate extensions and stage-specific proof burden

**Principle:** research INVESTMENT eligibility is not the same event as POST-PROOF certification of new economics. The novelty standard was correctly revised in v1.1 (2026-09-02) to distinguish familiar ingredients from model/result absorption and recognize generalization; the remaining operational defect was imposing certification-level absorption and an obligatory "new joint-endogeneity mechanism" before the researcher could test a theorem extension.

Recognize **six legitimate contribution routes**, without a hierarchy that requires a new mechanism: (G) economically meaningful generalization under weaker conditions; (B) sharper theorem boundary / substantive counterexample; (W) new equilibrium, comparative-static, welfare or policy result in a known model class; (U) explanatory generalization or unification of known benchmarks; (M) genuinely new mechanism; (C) consequential correction or reassessment of a prior claim.

- **Pre-Stage F and Stage 0:** verify actual parent-theorem knowledge and specify an ECONOMICALLY IMPORTANT, falsifiable, expressly UNPROVED extension Delta Card with a smallest bounded probe. Do not demand proof of independent theorem novelty as an entry requirement. The same literature can admit zero feasible candidates without a quota.
- **Stage 2:** a categorical "already known" NO-GO needs a source-grounded same-result/theorem and actual parameter/variable mapping or other demonstrable result-level equivalence. Similar vocabulary, familiar model class or separate component precedents are NOT by themselves proof of absorption. Nonetheless obvious tautologies, no-material-economic-result projects and renamings may be killed. A test-worthy candidate can be GO for limited derivation while theorem novelty remains UNPROVED; a truly decisive unread source stays a narrowly scoped CONDITIONAL GO with exactly one blocker.
- **Stage 3:** plan bounded tests for any G/B/W/U/M/C route. An extension can weaken a known theorem's assumptions without creating a new full-game interaction. Avoid ad hoc architecture expansion, and stop after a mathematically demonstrated empty result or a known exact absorption.
- **Stages 4/4A/5/6/7.5/7.5A/11:** original independent mathematical certification, strict post-proof theorem absorption, quantifier discipline, economic significance and journal referee attacks are unchanged. A mathematically correct but economically trivial result is not automatically a publishable paper. If a known general theorem immediately implies the actual result, it fails theorem-novelty despite a fresh application label.

Use [NOVELTY_ASSESSMENT_PHASED_EXTENSION_STANDARD.md](NOVELTY_ASSESSMENT_PHASED_EXTENSION_STANDARD.md) as the operational crosswalk. Preserve all earlier negative cases; re-open a prior NO-GO only upon a **new, precisely different Delta Card** that gives a substantiated reason to reconsider, never by quietly undoing a proven counterexample.

This is a draft operational *minor* refinement under v2.8/v2.9-candidate governance. It does not yet release a new version, alter three-valued Stage verdicts, weaken proof gates, or retroactively authorize any failed or frozen paper.

---

### 2.22 Applied economic theory: economic problem is necessary; mathematics is a method

The reusable workflow has multiple theoretical research traditions. For a project explicitly established as **APPLIED ECONOMICS researched theoretically** (e.g., local-government industrial policy), activate [APPLIED_ECONOMIC_THEORY_TRACK.md](APPLIED_ECONOMIC_THEORY_TRACK.md) from Pre-Stage F/Stage0 onward. This is NOT a requirement to add empirical data, a structural estimate, or an immediately implementable policy prescription.

**Do not evaluate applied-theory ideas on two independent axes "mathematically interesting" and "editorially valuable."** Only economic explanatory/positive/normative relevance is an independent source of applied research value. Math feasibility is a necessary means, proof correctness a strict downstream gate; neither substitutes for economic significance. Stage0–2 must ask which substantive conclusion about actors' incentives, industry/location allocation, institutional choice, welfare or policy effectiveness changes IF the unproved conjecture holds, and which audience has reason to care.

- **Required early positive case:** source-anchored economic puzzle, exact existing benchmark, anticipated substantive change in economic understanding, the relevant readers/research community, and a limited theory test. The prospective full-paper vs note/comment scale is provisional and does not impose venue selection.
- **Early applied NO-GO:** no defensible economic insight even IF a new theorem is derived; pure notation/formal strengthening with no material economic interpretation; arbitrary payoff/accounting assumption creating desired policy signs; or no real economic question a model would resolve. This does **not** pronounce mathematical work valueless in a separately chosen pure-theory discipline.
- **Positive/diagnostic theory is allowed:** explaining a policy failure or economically relevant phenomenon can be substantive without specifying the optimal corrective policy, provided the actual claimed contribution and editorial readership support it.
- **Strictness remains:** Stage4/4A equilibrium/global mathematical certification, Stage6 actual result originality, Stage7.5/7.5A theorem scope, and Stage11 referee/editorial completeness are unchanged. No early GO makes the result novel or publishable.

The earlier **2026-10-10 journal-alignment audit** identified an early "mathematical test worthwhile" vs "editorially plausible if successful" two-flag screen. That framing is **SUPERSEDED IN THIS APPLIED TRACK**: economic problem/expected insight is a gate to whether the math should be done at all; technical feasibility is its instrument check, not an equal independent dimension. Any field-editor preview serves the economic question, not a second unrelated value track.

---

### 2.23 Distinguish scholarly merit from the current project scope (JME/TE literature audit, 2026-10-10)

The scholarly merit of a new result in **MATHEMATICAL ECONOMICS** must NOT be assessed by whether it changes the USER's industrial policy rankings. Official Journal of Mathematical Economics scope permits important mathematical generalizations of equilibrium, choice, and economic-theory methods in ALL fields; Theoretical Economics welcomes pure and applied theory. Published 2024/2025 articles extend economic equilibrium existence under discontinuity/nonconvexity and extend finite theories to infinite settings without a specific municipal policy result. See [docs/GENERALIZATION_SCHOLARLY_VALUE_AUDIT_2026-10-10.md](docs/GENERALIZATION_SCHOLARLY_VALUE_AUDIT_2026-10-10.md).

Every candidate must distinguish **(i) discipline-level economic theory contribution** (including generalizations of existence/uniqueness/stability, methodological theorems, robust choice/strategic results), **(ii) CURRENT PROJECT TOPIC FIT** (DIRECT / ADJACENT / OUTSIDE), **(iii) originality/evidence confidence** and **(iv) plausible JOURNAL FAMILY**. No project-specific relevance is not a NO-GO on field-wide mathematical economics value; use DEFER/ROUTE/SEPARATE PROJECT while preserving findings and a suitable theory-journal possibility. A purely mathematical assertion with no substantive ECONOMIC model or theory content still does not automatically meet an economics journal's bar. Maintain existing strict proof, substantial-result and post-proof absorption requirements.

This controls any overly broad language in §2.22 that could confuse the purpose of the applied project with the wider scholarly significance of a mathematical-economic contribution. Do not require datasets or a new policy prescription; nor claim any abstract new theorem is guaranteed to publish.

---

## 3. Repository change policy

### 3.1 Main branch

`main` is the canonical workflow state.

Substantive workflow changes should normally enter through a feature/bootstrap branch and pull request. Direct commits to `main` should be limited to initialization or genuinely trivial administrative corrections.

### 3.2 Branch naming

Recommended patterns:

- `bootstrap/<topic>`
- `workflow/<stage-or-policy>`
- `templates/<stage-range>`
- `checklists/<topic>`
- `examples/<case>`
- `docs/<topic>`
- `audit/<topic>`
- `release/<version-or-topic>`

### 3.3 Pull-request requirements

A substantive PR should state:

1. problem solved;
2. canonical files changed;
3. whether gates are strengthened/weakened;
4. routing/stage compatibility implications;
5. validation performed;
6. open questions intentionally deferred.

### 3.4 Review standard

Review should focus on:

- internal consistency across stages;
- whether gates can be bypassed unintentionally;
- whether novelty standards are weakened;
- whether application labels have been stripped and plausible standard parent-model/theorem absorption has been tested for theory-novelty claims;
- whether mathematical verification matches the claimed theorem scope;
- whether global/SPNE claims audit off-path/boundary deviations rather than only regular branches;
- whether solver failures fail closed;
- whether theorem quantifiers exceed proof;
- whether broad function-class claims receive counterexample search;
- whether planner/benchmark labels match feasible choice sets;
- whether independent certification is genuinely independent rather than duplicate execution;
- whether formal-verification applicability is explicitly closed before theory freeze;
- whether proof-assistant statements faithfully match paper claims and do not smuggle conclusions through assumptions/definitions;
- whether material AI use is provenance-tracked and verification actors are correctly labeled;
- whether central-result author intellectual-contribution evidence exists before theory freeze;
- whether AI disclosure wording is supported by the provenance record rather than generic boilerplate;
- whether theorem-bearing/technically dense manuscripts are reviewer-verifiable: proof-critical intermediate objects and bridge equations are visible or precisely cross-referenced, delegated computer-assisted steps identify object/domain/property/implication, and streamlining has not made the proof logically opaque;
- whether source requirements are explicit and realistic;
- whether the workflow encourages unnecessary complexity;
- whether mathematical/novelty PASS is being mistaken for sufficient economic/editorial importance;
- whether policy-facing papers distinguish a diagnosed externality from practical implementation and document any material missing-question attack before theory freeze;
- whether bounded extension-versus-baseline selection has evidence and does not force new instruments for pure theory, corrections, or notes;
- whether `NO-GO` remains a legitimate outcome.

### 3.5 Release and version changes

Release/version changes are substantive because published versions define stable workflow behavior.

- Assess compatibility under `docs/VERSIONING_POLICY.md` before changing stable canonical behavior.
- A stable release tag must point to a reviewed `main` state.
- Published stable tags are immutable historical references.
- Correct released defects with later versions rather than moving tags.
- Release/audit docs record version state but do not override the canonical hierarchy.

Stage additions/removals/mergers, canonical routing changes, verdict-semantic changes, or incompatible workflow architecture changes require a MAJOR version under the current versioning policy. The Stage 4A and Stage 7.5A additions therefore define v2.0 architecture.

Adding a formal-verification obligation **inside** existing Stage 4A/7.5A/8 boundaries, without renumbering Stages or changing canonical routing/verdict semantics, is a MINOR-version class refinement rather than a new Stage.

Likewise, adding mathematical canonicalization at Stage 4, theorem-level absorption testing at Stage 6, and a known-model-in-disguise hostile attack at Stage 11 preserves Stage identities, verdict semantics, and routing; this is a MINOR-version refinement and is classified as v2.2.

The Stage-12 candidate-universe completeness refinement likewise leaves Stage identity, verdict semantics, and routing unchanged. It strengthens how serious journal candidates are generated and audited before ranking, so it is a MINOR-version refinement and is classified as v2.3.

---

## 4. Canonical workflow hierarchy

Priority order:

1. `GOVERNANCE.md`
2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
3. stage templates under `templates/`
4. checklists under `checklists/`
5. worked examples under `examples/`

Lower-level files may elaborate but may not weaken higher-level rules. If conflict exists, the higher-level document governs until repaired through PR.

---

## 5. Research evidence standards

### 5.1 Literature

For serious novelty assessment:

- verify bibliographic information;
- prefer publisher/DOI/RePEc/NBER/SSRN/author records as appropriate;
- inspect full model/proposition content for closest papers when reasonably possible;
- perform backward/forward citation search where the literature is mature;
- distinguish exact prior art, structural proximity, component overlap, and broad relatedness;
- do not infer novelty from search failure alone;
- for theorem-bearing work, search both the application literature and the application-neutral canonical mathematical class;
- explicitly attempt variable/parameter mappings from the strongest plausible general prior theorems to the candidate headline results;
- treat a short specialization/corollary as theorem absorption even when the prior source does not print the same application-specific formula or threshold.

### 5.2 Institutional facts

Prefer primary sources. Label secondary evidence. Do not transform suggestive institutional facts into model primitives without stating the inferential step.

### 5.3 Mathematics

When applicable:

- re-derive rather than copy formulas;
- verify equilibrium identities;
- check FOCs/KKT, SOCs/Hessians, feasibility, participation, and limiting/boundary cases;
- distinguish numerical support from proof;
- search for counterexamples to proposed global propositions;
- enumerate economically meaningful corners, active sets, regime switches, entry/exit, zero-output states, ordering/participation changes, and possible equilibrium nonexistence;
- for sequential games distinguish on-path calculations from off-path continuation validity;
- re-solve downstream subgames after material upstream deviations rather than extrapolating an on-path formula;
- treat solver failure as evidence of incompleteness, not failed deviation;
- independently reconstruct payoffs/allocations for high-stakes claims where feasible;
- record theorem quantifiers and function classes explicitly;
- attempt admissible-function counterexamples to broad comparative-static/curvature/uniqueness claims;
- write planner optimization problems explicitly before applying welfare benchmark labels;
- make a formal-verification applicability decision for every theorem-bearing project;
- where applicable, formalize the highest-value proof-critical core using Lean 4/mathlib or another auditable proof assistant, with statement-fidelity and model-boundary audits;
- distinguish kernel-checked statements from economic assumptions/hypotheses supplied to the proof assistant;
- preserve clean-build and axiom/placeholder evidence for formal artifacts.

Sequential/game-theoretic projects must apply `checklists/EQUILIBRIUM_CONTINUATION_CHECKLIST.md` whenever continuation validity matters.

Headline theorem-bearing projects must apply `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` at Stage 4A and again at Stage 7.5A whenever scope changed.

All theorem-bearing projects must apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md`: Stage 4A records applicability and target candidates; Stage 7.5A closes the pre-freeze formal-verification state.

### 5.4 Numerical work

Numerical grids and simulations are diagnostics unless the research design is explicitly computational. They may identify regions, counterexamples, or conjectures but must not be reported as analytic proofs.

Solver failure rates and unresolved continuation counts are evidence and may not be silently filtered.

### 5.5 Evidence maturity and provenance

Distinguish at minimum:

- reported/remembered/scratch result requiring reproduction;
- mathematical/numerical result reproduced from committed artifacts;
- literature/institutional claim verified against an identifiable source;
- claim re-verified for the actual submission package;
- conjecture/model assumption still unverified;
- rejected claim/branch.

AI/chat output, scratch calculations, and historical notes are provenance inputs, not independent evidence. An AI review remains AI evidence even if produced in a separate chat or by a different model; it does not become author verification or external human review. Material AI use must be tracked under `checklists/AI_PROVENANCE_AUTHOR_ACCOUNTABILITY_CHECKLIST.md`.

### 5.6 Method applicability

Verification must match method. `NOT APPLICABLE` is allowed only with a recorded reason and may not bypass a substantive gate.

For formal verification, project-level `NOT APPLICABLE` must additionally explain why neither full nor targeted proof-assistant formalization would materially improve assurance for the current headline claims.

---

## 6. Stage verdict and routing policy

Every research stage records one canonical verdict:

### GO

Current success criteria are met and the project may proceed only under the stated next-stage contract.

### CONDITIONAL GO

Exactly one clearly specified blocker remains. This is not permission for arbitrary extension.

### NO-GO

The branch stops. A pivot may reopen only at the earliest stage justified by a distinct question or diagnosed deficiency.

Subtests may use `PASS / CONDITIONAL / FAIL`. Routing/status labels are secondary.

### v2.0 hard routing

For theorem-oriented projects:

- Stage 4 `GO` routes to **Stage 4A**, never directly to Stage 6.
- Stage 5 repair returns to **Stage 4 then Stage 4A**.
- Stage 4A `GO` routes to Stage 6.
- Stage 7.5 `GO` routes to **Stage 7.5A**, never directly to Stage 8.
- Stage 7.5A `GO` is required for Stage 8 theory freeze.

The Stage structure and routing remain unchanged by the Formal Verification Gate. Instead, Stage 7.5A may issue `GO` only after its embedded formal-verification state is either `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

No green CI/symbolic/numerical/proof-assistant result bypasses these gates.

---

## 7. Rollback and stale-state policy

When a later stage discovers a substantive error, return to the earliest stage whose canonical output is invalidated. Dependent downstream outputs become stale until required gates are rerun.

Examples:

- newly discovered prior art → Stage 2 or Stage 6 depending on whether the issue concerns the pre-model gap or actual derived result;
- newly discovered parent-theorem absorption / known-model-in-disguise result → Stage 6, or Stage 0/3/4 if the research question/mechanism/model architecture itself must change;
- false proposition/equilibrium/globality error → Stage 4 then Stage 4A;
- off-path continuation or hidden boundary/regime deviation failure → Stage 4 then Stage 4A;
- one authorized economic repair → Stage 5, then repeat Stage 4 and 4A;
- failed welfare optimization problem → Stage 7 or Stage 4 depending on source of error;
- theorem quantifier/function-class overclaim with correct underlying narrow theorem → Stage 7.5A and downstream stages;
- theorem actually false within claimed domain → Stage 4/4A and then all affected downstream stages;
- benchmark label wrong but underlying planner problem correct → Stage 7.5A; benchmark optimization problem itself wrong → Stage 7/4 as appropriate;
- formalization exposes a false theorem or missing economic condition → earliest affected analytic stage, then rerun affected Stage 4A/7.5A/formal certification;
- formal source/build/statement-mapping defect only with unchanged certified mathematics → Stage 7.5A Formal Verification Gate;
- material theorem/quantifier change after formal certification → mark the formal certificate stale and rerun the affected analytic/scope and formal-verification gates before refreeze;
- post-freeze theory change → Stage 8 change control plus every affected earlier gate;
- Stage 11 fatal attack → earliest affected stage, not prose-only patch;
- Stage 13/14 substantive inconsistency → earliest affected research stage plus fresh integration/QA.

If Stage 11 detects a failure that Stage 4A or 7.5A should have caught, record `CERTIFICATION REGRESSION` and preserve the case as workflow evidence.

Silent downstream repair is prohibited.

---

## 8. Freeze policy

### 8.1 Theory freeze

Theory freeze requires Stage-4A and Stage-7.5A `GO` certificates. For theorem-bearing projects, Stage-7.5A `GO` additionally requires a closed Formal Verification Gate with either `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

Freeze at minimum:

- research question and canonical model;
- complete strategy/choice domains;
- parameter restrictions and admissible function classes;
- equilibrium concept;
- main/welfare propositions with exact quantifiers;
- proof/evidence state;
- closest-paper positioning;
- approved robustness scope;
- Stage-4A theorem certificates;
- Stage-7.5A claim-scope ledger;
- formal-verification applicability state and certificate/N-A rationale;
- claim-to-formal-theorem mapping and explicit non-formalized scope where applicable;
- proof-assistant/toolchain/library/build and axiom/placeholder provenance where applicable;
- benchmark-definition register;
- counterexample/regression-test register;
- material AI-use/provenance record where applicable;
- author intellectual-contribution record for central results;
- explicit claims not made.

Sequential/game-theoretic models additionally require explicit continuation-completeness and solver-outcome records covering material strategy/history domains.

### 8.2 Submission freeze

Submission freeze records at minimum:

- canonical repository SHA/tag;
- final manuscript/supplement;
- reproducibility outputs and theorem certificates;
- formal-verification source/build certificate where applicable;
- journal-specific files;
- disclosure statements where applicable;
- final AI-disclosure reconciliation where material AI use occurred;
- author sign-off tied to the exact frozen commit/package.

No silent post-freeze theoretical edits are permitted.
