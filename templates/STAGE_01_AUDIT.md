# Stage 1 — Source & Mathematical Audit

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a research director and verification engineer. Reconstruct `[RESEARCH_TOPIC]` from first principles. Do not trust inherited formulas, prose claims, or old conclusions merely because they appear in the source.

## 1. Project context

- Working title: `[WORKING_TITLE]`
- Core question: `[CORE_RESEARCH_QUESTION]`
- Source files: `[SOURCE_FILES]`
- Source repository: `[SOURCE_REPOSITORY]`
- Current stage result: `[CURRENT_STAGE_RESULT]`
- Known blockers: `[KNOWN_BLOCKERS]`

## 2. Stage objective

Determine what the starting material actually assumes, proves, and fails to prove; produce a verified canonical representation for later novelty analysis.

## 3. Canonical inputs

Read all relevant source text, appendices, equations, tables, notes, code, and figures. Preserve source terminology when reporting source content. Distinguish source claims from your corrections or reconstruction.

## 4. Allowed changes

You may correct algebra, expose missing assumptions, re-derive demand/utility, and classify claims as valid/invalid/ambiguous. You may not add a new mechanism to rescue a failed result.

## 5. Prohibited changes

- no silent correction of the source;
- no reuse of inherited equilibrium formulas without re-derivation;
- no cross-regime welfare comparison when populations, outside options, or utility systems are inconsistent;
- no desired-result engineering.

## 6. Mandatory tasks

Reconstruct explicitly:

1. players and objectives;
2. timing and information;
3. utility or demand system;
4. technologies and costs;
5. contracts/transfers;
6. strategy sets;
7. equilibrium concept;
8. claimed propositions and welfare statements.

For mathematical models, re-derive from zero:

- direct and inverse demand consistency;
- best responses and FOCs;
- equilibrium solutions;
- SOCs / Hessians / concavity;
- feasibility and interiority;
- participation / individual rationality constraints;
- KKT or corners where relevant;
- parameter restrictions;
- limiting and boundary cases;
- profit, consumer-surplus, and welfare identities.

Classify each important inherited result as `CORRECT`, `CORRECT BUT ECONOMICALLY AD HOC`, `INCORRECT`, or `AMBIGUOUS`.

## 7. Evidence requirements

All mathematical claims must be reproducibly verified. If institutional or empirical assumptions appear in the source, record whether they are sourced, merely asserted, or contradicted by the model.

## 8. Verification protocol

Use Python/SymPy or an equivalent symbolic system whenever symbolic verification is applicable. At minimum, verify important identities with exact simplification, check Hessian conditions, and search for counterexamples to global comparative-static claims. Numerical work may diagnose but not replace proof.

Use `checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md` and, after analytic work, `checklists/NUMERICAL_VERIFICATION_CHECKLIST.md` where applicable.

## 9. Kill tests

Flag as potentially fatal if:

- a key result depends on algebraic error;
- the equilibrium does not exist in an economically meaningful region;
- a parameter mixes distinct economic effects and drives the headline result;
- a profit split or transfer is ad hoc and determines participation;
- a proposition is strict only in a subset but is stated globally;
- welfare comparison changes market definition or consumer utility across regimes;
- the result is a mechanical consequence of normalization or demand intercept shifts.

## 10. Success criteria

A successful audit yields a verified model map, exact list of valid results, explicit failure points, and a precise residual research question.

## 11. Failure criteria

Return `NO-GO` for the inherited branch if the key result is mathematically false or economically uninterpretable and no residual question remains. A failed inherited model may still generate a new Stage 0 question, but that is a separate branch.

## 12. Required final output

1. Executive audit verdict
2. Canonical source model
3. Equation-by-equation audit
4. SOC / feasibility / participation audit
5. Parameter-interpretation audit
6. Welfare/comparability audit
7. Correct vs incorrect claim table
8. Surviving economic questions
9. Inputs for novelty search
10. Verdict and next-stage contract

## 13. Final verdict

Choose one:

- `GO TO NOVELTY GATE`
- `CONDITIONAL GO` — state one unresolved verification issue
- `NO-GO`

## 14. Next-stage contract

Freeze the audited representation. Stage 2 may search and compare literature; it may not change the model to improve novelty.