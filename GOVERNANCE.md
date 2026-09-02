# Governance

Version: v1.1

## 1. Purpose

This repository defines reusable research workflows. Changes to it therefore affect future research projects, not merely one manuscript. Governance should favor traceability, explicit gates, reproducibility, and conservative claims.

The repository should function as a research operating system, not as an informal prompt dump.

---

## 2. Core governance principles

### 2.1 Evidence before claims

Do not state that a result, paper, journal requirement, institutional fact, or novelty claim has been verified unless the supporting source or computation has actually been checked.

When evidence is incomplete, mark the limitation explicitly.

### 2.2 Negative results are retained

Rejected models, failed novelty claims, algebraic counterexamples, and referee-style fatal objections are valuable outputs. They should be preserved in project decision logs when they materially shaped the next stage.

### 2.3 No silent theory drift

Once a project reaches theory freeze, changes to players, timing, utility/demand, information, contracts, equilibrium concept, main propositions, or welfare structure require explicit documentation and re-validation of affected stages.

### 2.4 One diagnosed fix at a time

A failed minimal model should not trigger uncontrolled feature accumulation. The next modification must address a specific failure identified by the prior stage.

### 2.5 No prestige-driven distortion

Target journals may affect exposition, robustness expectations, and presentation, but must not determine the substantive result before the research is solved.

---

## 3. Repository change policy

### 3.1 Main branch

`main` is the canonical workflow state.

Substantive workflow changes should normally enter through a feature/bootstrap branch and pull request.

Direct commits to `main` should be limited to repository initialization or genuinely trivial administrative corrections.

### 3.2 Branch naming

Recommended patterns:

- `bootstrap/<topic>` for initial repository construction;
- `workflow/<stage-or-policy>` for workflow architecture;
- `templates/<stage-range>` for reusable templates;
- `checklists/<topic>` for verification/checklist additions;
- `examples/<case>` for worked cases;
- `docs/<topic>` for non-substantive documentation;
- `audit/<topic>` for integration/readiness audits;
- `release/<version-or-topic>` for release preparation.

### 3.3 Pull-request requirements

A substantive PR should state:

1. what problem it solves;
2. what files define or change canonical behavior;
3. whether any existing stage gate is weakened or strengthened;
4. compatibility implications for existing project templates;
5. how the change was validated;
6. any open questions intentionally deferred.

### 3.4 Review standard

Review should focus on:

- internal consistency across stages;
- whether gates can be bypassed unintentionally;
- whether novelty standards are weakened;
- whether mathematical verification is adequately required when applicable;
- whether source requirements are realistic and explicit;
- whether the workflow encourages unnecessary complexity;
- whether failures and `NO-GO` outcomes remain legitimate outcomes.

### 3.5 Release and version changes

Release/version changes are substantive repository changes because a published version defines what future projects may treat as stable workflow behavior.

- Assess compatibility under [`docs/VERSIONING_POLICY.md`](docs/VERSIONING_POLICY.md) before changing stable canonical behavior.
- A stable release tag must point to a reviewed `main` state.
- Published stable tags are historical references and must not be silently moved or overwritten.
- Correct a released defect with an appropriate later version rather than rewriting the historical tag.
- Release/audit documents under `docs/` record version state but do not override the canonical hierarchy below.

---

## 4. Canonical workflow hierarchy

The priority order is:

1. `GOVERNANCE.md`
2. `THEORY_PAPER_RESEARCH_PIPELINE.md`
3. stage templates under `templates/`
4. checklists under `checklists/`
5. worked examples under `examples/`

Lower-level files may elaborate higher-level rules but may not silently contradict or weaken them.

If a conflict is discovered, the higher-level canonical document governs until the conflict is resolved by PR.

---

## 5. Research evidence standards

### 5.1 Literature

For serious novelty assessment:

- verify bibliographic information;
- prefer publisher pages, DOI records, RePEc/NBER/SSRN records, working-paper repositories, and author versions as appropriate;
- inspect full model/proposition content for closest papers whenever reasonably possible;
- perform backward and forward citation search where the literature is mature;
- distinguish exact prior art, structural proximity, component overlap, and broad relatedness;
- do not infer novelty from search failure alone.

### 5.2 Institutional facts

Prefer primary sources. If secondary sources are necessary, label them as such. Do not transform suggestive institutional evidence into a proven model primitive without stating the inferential step.

### 5.3 Mathematics

When symbolic tools are applicable:

- re-derive rather than copy legacy formulas;
- verify equilibrium identities;
- check SOCs/Hessians;
- check feasibility and participation constraints;
- inspect limiting and boundary cases;
- distinguish numerical support from proof;
- search for counterexamples to proposed global propositions.

### 5.4 Numerical work

Numerical grids and simulations are diagnostics unless the research design is explicitly computational. They may identify regions, counterexamples, or conjectures but must not be reported as analytic proofs.

### 5.5 Evidence maturity and provenance

Claim type and evidence maturity must be recorded separately. At minimum, distinguish:

- a result or claim merely reported in notes, conversation, or temporary computation and therefore requiring reproduction;
- a mathematical/numerical result reproduced from committed project artifacts;
- a literature or institutional claim verified against an identifiable source;
- a claim re-verified for the actual submission package when submission-level assurance is required;
- a conjecture/model assumption that remains unverified;
- a rejected claim or branch.

Worked examples may use more specific labels such as `REPORTED / REQUIRES REPRODUCTION`, `LITERATURE-VERIFIED`, `INSTITUTIONALLY SUGGESTIVE`, `CONJECTURE`, and `REJECTED`. Those labels do not automatically upgrade a claim to submission-ready evidence.

AI/chat output, scratch calculations, and historical notes are provenance inputs, not independent evidence. A later stage must not silently promote them into verified theorems or verified facts.

### 5.6 Method applicability

Verification must match the research method. Symbolic algebra is required only when a mathematical model makes it applicable; empirical, computational, institutional, or qualitative claims require their own appropriate verification.

A check may be marked `NOT APPLICABLE` only with a recorded reason. `NOT APPLICABLE` must not be used to bypass a gate that is substantive for the project.

---

## 6. Stage verdict and routing policy

Every research stage must record a canonical stage verdict:

### GO

The project has satisfied the current stage's success criteria and may proceed under the next-stage contract.

### CONDITIONAL GO

The project may proceed only to resolve a clearly specified blocker. A conditional verdict is not permission for arbitrary extension.

### NO-GO

The current branch should stop. A new branch or pivot may be opened only when it addresses a distinct research question or a precisely diagnosed deficiency.

Repeatedly converting `NO-GO` into additional assumptions until a desired result appears violates this workflow.

Subtests may use `PASS / CONDITIONAL / FAIL`. Operational templates may also emit routing or state labels such as `GO TO STAGE 6`, `THEORY FROZEN`, or `SUBMISSION QA PASS`. These are secondary routing/status outputs and do not replace the canonical `GO / CONDITIONAL GO / NO-GO` stage verdict.

---

## 7. Rollback and stale-state policy

The workflow is stage-gated but not strictly linear.

When a later stage discovers a substantive error, return to the earliest stage whose canonical output has been invalidated. Downstream outputs that depend on that input become stale until the affected stage and all necessary downstream gates are re-run.

Examples:

- newly discovered prior art returns to Stage 2 or Stage 6 depending on whether it concerns the pre-model gap or an actual derived result;
- a false proposition or equilibrium error returns to Stage 4, or Stage 5 if the issue is caused by an authorized hardening modification;
- a failed institutional/welfare premise returns to Stage 7 or earlier if the primitive itself changes;
- a post-freeze theory change reopens Stage 8 change control and every affected earlier verification/novelty gate;
- a Stage 11 fatal attack must be routed to the earliest stage capable of resolving it, not patched only in prose;
- a substantive inconsistency found in Stage 13 or Stage 14 reopens the earliest affected research stage, followed by a fresh integration/QA cycle.

A `NO-GO` branch does not automatically qualify for Stage 5. Stage 5 is available only when the previous minimal-model result identifies one precise economic deficiency that can be tested with one authorized modification. Otherwise stop or return to Stage 3/Stage 0 as a distinct pivot.

Silent repair in a later stage is prohibited.

---

## 8. Freeze policy

### 8.1 Theory freeze

A theory freeze records at minimum:

- research question;
- canonical model;
- parameter restrictions;
- main propositions;
- welfare results;
- proof/verification state;
- closest-paper positioning;
- approved robustness scope.

### 8.2 Submission freeze

A submission freeze records at minimum:

- canonical repository SHA/tag;
- final manuscript and supplement;
- reproducibility outputs;
- journal-specific files;
- disclosure statements where applicable.

No silent post-freeze theoretical edits are permitted.

---

## 9. Provenance and decision logs

Worked research projects should preserve a concise decision log containing:

- candidate mechanism;
- stage tested;
- result;
- why it survived or failed;
- strongest prior-art threat;
- strongest mathematical/referee threat;
- exact reason for the next modification.

A useful example should show rejected branches as well as successful ones.

---

## 10. AI-assisted research

AI may be used extensively for search planning, algebra, coding, drafting, review simulation, and workflow execution, but AI output is not itself evidence.

Project-specific work should independently validate:

- citations and bibliographic facts;
- equations and numerical results;
- claims about journal policies;
- institutional facts;
- final contribution/novelty statements.

Where a target journal requires disclosure of generative-AI use, the project should verify the current policy at submission time and comply with it.

An AI-generated `GO`, `PASS`, or positive referee simulation has no independent evidentiary weight. The recorded verdict must be supported by the stage's required evidence and verification artifacts.

---

## 11. Future extensions to this governance

Later PRs may add:

- machine-readable stage metadata;
- CI checks for template completeness;
- standard decision-log schemas;
- project bootstrap scripts;
- an empirical-research workflow or cross-discipline variants.

Such additions should preserve the core principle: the workflow exists to improve research quality and terminate weak branches early, not to maximize the number of papers produced.
