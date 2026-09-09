# Governance

Version: v2.1

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
- whether mathematical verification matches the claimed theorem scope;
- whether global/SPNE claims audit off-path/boundary deviations rather than only regular branches;
- whether solver failures fail closed;
- whether theorem quantifiers exceed proof;
- whether broad function-class claims receive counterexample search;
- whether planner/benchmark labels match feasible choice sets;
- whether independent certification is genuinely independent rather than duplicate execution;
- whether formal-verification applicability is explicitly closed before theory freeze;
- whether proof-assistant statements faithfully match paper claims and do not smuggle conclusions through assumptions/definitions;
- whether source requirements are explicit and realistic;
- whether the workflow encourages unnecessary complexity;
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
- do not infer novelty from search failure alone.

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

AI/chat output, scratch calculations, and historical notes are provenance inputs, not independent evidence.

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
- explicit claims not made.

Sequential/game-theoretic models additionally require explicit continuation-completeness and solver-outcome records covering material strategy/history domains.

### 8.2 Submission freeze

Submission freeze records at minimum:

- canonical repository SHA/tag;
- final manuscript/supplement;
- reproducibility outputs and theorem certificates;
- formal-verification source/build certificate where applicable;
- journal-specific files;
- disclosure statements where applicable.

No silent post-freeze theoretical edits are permitted.
