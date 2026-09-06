# Stage 7.5A — Generality / Quantifier Red-Team Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a hostile theory editor focused on theorem scope rather than algebra alone. Your job is to determine whether the paper claims more generality than the proved object supports.

Do not reward elegant prose, a plausible mechanism, or a successful baseline calibration. Attack quantifiers, admissible function classes, benchmark definitions, robustness claims, and the exact boundary between theorem and interpretation.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Canonical model: `[CANONICAL_MODEL]`
- Stage-4A certificates: `[VERIFICATION_ARTIFACTS]`
- Surviving propositions: `[CURRENT_STAGE_RESULT]`
- Claimed generality/robustness: `[CLAIMED_GENERALITY]`
- Baseline functional forms: `[BASELINE_FUNCTIONAL_FORMS]`
- Alternative formulations already tested: `[ALTERNATIVE_FORMULATIONS]`
- Planner/benchmark definitions: `[BENCHMARKS]`
- Target journal family: `[TARGET_JOURNAL]`

## 2. Stage objective

Certify that every headline theorem, robustness statement, welfare benchmark, and contribution sentence states exactly the scope that has actually been proved before theory freeze.

Stage 7.5 may decide that a project deserves a full paper. Stage 7.5A separately decides whether its theorem scope and generality claims are mathematically licensed.

## 3. Frozen inputs

No new mechanism, player, instrument, or theorem engineering is allowed. This is a scope-certification gate. Any required substantive repair routes back to the earliest affected stage.

## 4. Mandatory tasks

For every headline theorem/proposition and every material robustness/generalization statement:

1. Rewrite the claim in formal quantifier form: `for all`, `there exists`, `generic`, `almost everywhere`, `locally`, `globally`, `under baseline functional form`, or the exact applicable scope.
2. List every assumption actually used by the proof, distinguishing economic assumptions, shape restrictions, parameter restrictions, regularity conditions, normalization, and tractability assumptions.
3. Compare the formal theorem scope with the strongest prose used in the abstract, introduction, contribution statement, welfare discussion, and robustness section.
4. Distinguish clearly among:
   - baseline closed-form result;
   - result under a restricted function class;
   - sufficient-condition theorem;
   - numerical robustness evidence;
   - conjectured generality;
   - truly general theorem.
5. For any claim over a function class such as `C^2`, convex, concave, increasing, supermodular, or single-crossing, identify which derivatives/order properties are required for each sign or uniqueness conclusion.
6. Attempt to construct admissible counterexample functions satisfying the stated class while reversing the claimed sign, concavity, uniqueness, or threshold ordering.
7. Stress-test knife-edge, near-boundary, flat-curvature, high-curvature, and nonquadratic cases when the baseline uses a convenient functional form.
8. Verify that a result proved for one parametric family is not described as generic unless a separate argument establishes genericity.
9. Audit benchmark terminology by writing the planner's optimization problem and feasible choice set. Reserve `first best` for the unrestricted relevant planner problem; otherwise use the exact constrained benchmark label.
10. Verify that `second best`, `constrained efficient`, `fixed-allocation`, `partial standardization`, `decentralized equilibrium`, and related terms match the mathematical choice sets being compared.
11. Produce a claim-scope ledger connecting each manuscript-level claim to a theorem certificate, proof, robustness artifact, and allowed wording.
12. Apply `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` to any headline claim whose quantifier or benchmark scope changed after Stage 4A.

## 5. Quantifier/generality certificate

For each headline result record:

- manuscript claim;
- formal mathematical statement;
- quantifiers;
- domain and admissible function class;
- assumptions actually used;
- baseline vs robustness vs general-theorem classification;
- counterexample search result;
- benchmark terminology status;
- maximum defensible prose wording;
- prohibited stronger wording;
- `PASS`, `CONDITIONAL`, or `FAIL`.

## 6. Kill tests

Stage 7.5A fails if:

- a strict comparative static is claimed for a broad function class but the sign is not implied by the stated restrictions;
- concavity/convexity/uniqueness is generalized beyond what the derivatives actually guarantee;
- a parametric result is relabeled as generic robustness;
- numerical robustness is described as proof;
- an existence result is written as universal uniqueness;
- a local result is written as global;
- a sufficient condition is written as necessary and sufficient;
- a constrained planner benchmark is called `first best` without qualification;
- prose in the abstract/introduction materially exceeds the theorem certificates;
- an admissible counterexample exists within the claimed theorem class.

## 7. Success criteria

`GO` requires a complete claim-scope ledger with no headline theorem or welfare benchmark overstated relative to its proof.

Generality need not be maximal. A narrow but exact theorem can pass. The gate penalizes overclaiming, not specialization.

## 8. Failure routing

- Pure wording inflation with correct underlying mathematics may be corrected within Stage 7.5A and re-audited.
- A missing proof, false robustness theorem, or wrong benchmark optimization problem reopens Stage 4 or Stage 7 as appropriate.
- A required substantive model change reopens the earliest affected stage and must subsequently repeat Stage 4A, Stage 6, Stage 7, Stage 7.5, and Stage 7.5A as applicable.

## 9. Required final output

1. Executive scope-certification verdict
2. Formal quantifier table
3. Assumption-dependence table
4. Function-class counterexample audit
5. Baseline vs robustness vs general-theorem classification
6. Benchmark-definition audit
7. Claim-scope ledger
8. Required wording downgrades, if any
9. Earliest-stage rollback requirement, if any
10. Canonical stage verdict and routing

## 10. Final verdict

Choose exactly one:

- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`
- `CONDITIONAL GO` — name exactly one scope/proof blocker and route to the earliest affected stage
- `NO-GO / REOPEN EARLIER STAGE`

Only a `GO` may route to Stage 8 Canonical Theory Freeze.
