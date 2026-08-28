# Governance

Version: bootstrap-v1

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
- `docs/<topic>` for non-substantive documentation.

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
- whether mathematical verification is adequately required;
- whether source requirements are realistic and explicit;
- whether the workflow encourages unnecessary complexity;
- whether failures and `NO-GO` outcomes remain legitimate outcomes.

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

---

## 6. Stage verdict policy

Every research gate should produce an explicit verdict.

### GO

The project has satisfied the current stage's success criteria and may proceed under the next-stage contract.

### CONDITIONAL GO

The project may proceed only to resolve a clearly specified blocker. A conditional verdict is not permission for arbitrary extension.

### NO-GO

The current branch should stop. A new branch or pivot may be opened only when it addresses a distinct research question or a precisely diagnosed deficiency.

Repeatedly converting `NO-GO` into additional assumptions until a desired result appears violates this workflow.

---

## 7. Freeze policy

### 7.1 Theory freeze

A theory freeze records at minimum:

- research question;
- canonical model;
- parameter restrictions;
- main propositions;
- welfare results;
- proof/verification state;
- closest-paper positioning;
- approved robustness scope.

### 7.2 Submission freeze

A submission freeze records at minimum:

- canonical repository SHA/tag;
- final manuscript and supplement;
- reproducibility outputs;
- journal-specific files;
- disclosure statements where applicable.

No silent post-freeze theoretical edits are permitted.

---

## 8. Provenance and decision logs

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

## 9. AI-assisted research

AI may be used extensively for search planning, algebra, coding, drafting, review simulation, and workflow execution, but AI output is not itself evidence.

Project-specific work should independently validate:

- citations and bibliographic facts;
- equations and numerical results;
- claims about journal policies;
- institutional facts;
- final contribution/novelty statements.

Where a target journal requires disclosure of generative-AI use, the project should verify the current policy at submission time and comply with it.

---

## 10. Future extensions to this governance

Later PRs may add:

- versioning and release policy;
- machine-readable stage metadata;
- CI checks for template completeness;
- standard decision-log schemas;
- project bootstrap scripts;
- economics-specific and cross-discipline variants.

Such additions should preserve the core principle: the workflow exists to improve research quality and terminate weak branches early, not to maximize the number of papers produced.
