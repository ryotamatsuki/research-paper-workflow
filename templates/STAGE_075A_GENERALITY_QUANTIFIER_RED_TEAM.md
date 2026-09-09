# Stage 7.5A — Generality / Quantifier Red-Team Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a hostile theory editor focused on theorem scope rather than algebra alone. Your job is to determine whether the paper claims more generality, uniqueness, equilibrium-selection robustness, or welfare robustness than the proved object supports.

Do not reward elegant prose, a plausible mechanism, or a successful baseline calibration. Attack quantifiers, admissible function classes, equilibrium-set language, selection/refinement assumptions, benchmark definitions, robustness claims, and the exact boundary between theorem and interpretation.

Before issuing `GO`, also close the project's formal-verification applicability decision. Where formal verification is applicable, certify the selected proof-critical core with a proof assistant and audit the boundary between what is formally proved and what remains analytically or economically assumed.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Canonical model: `[CANONICAL_MODEL]`
- Stage-4A certificates: `[VERIFICATION_ARTIFACTS]`
- Stage-4A equilibrium-set / selection certificate: `[EQUILIBRIUM_SELECTION_STATUS]`
- Stage-4A formalization applicability / target map: `[FORMALIZATION_APPLICABILITY_AND_TARGETS]`
- Stage-7 welfare-selection robustness table: `[WELFARE_SELECTION_TABLE]`
- Surviving propositions: `[CURRENT_STAGE_RESULT]`
- Claimed generality/robustness: `[CLAIMED_GENERALITY]`
- Baseline functional forms: `[BASELINE_FUNCTIONAL_FORMS]`
- Alternative formulations already tested: `[ALTERNATIVE_FORMULATIONS]`
- Planner/benchmark definitions: `[BENCHMARKS]`
- Target journal family: `[TARGET_JOURNAL]`

## 2. Stage objective

Certify that every headline theorem, robustness statement, equilibrium characterization, welfare benchmark, and contribution sentence states exactly the scope that has actually been proved before theory freeze.

Stage 7.5 may decide that a project deserves a full paper. Stage 7.5A separately decides whether its theorem scope, equilibrium-set language, selection robustness, and generality claims are mathematically licensed.

Stage 7.5A is also the final pre-freeze **Formal Verification Gate**. The Stage number and routing do not change: formal verification is an embedded certification obligation inside Stage 7.5A, not a new canonical Stage. Stage 7.5A may issue `GO` only after the project records either `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED` under `checklists/FORMAL_VERIFICATION_CHECKLIST.md`.

## 3. Frozen inputs

No new mechanism, player, instrument, equilibrium refinement, or theorem engineering is allowed. This is a scope-certification gate. Any required substantive repair routes back to the earliest affected stage.

Formalization may expose a missing assumption, false inequality, incomplete case partition, or theorem-scope mismatch. Such a discovery is evidence about the existing theory; it does not authorize silent weakening or alteration of the theorem merely to make a proof assistant accept it.

## 4. Mandatory tasks

For every headline theorem/proposition and every material robustness/generalization/welfare statement:

1. Rewrite the claim in formal quantifier form: `for all`, `there exists`, `unique`, `multiple`, `generic`, `almost everywhere`, `locally`, `globally`, `for every equilibrium`, `for a selected equilibrium`, `under refinement R`, `under baseline functional form`, or the exact applicable scope.
2. List every assumption actually used by the proof, distinguishing economic assumptions, shape restrictions, parameter restrictions, regularity conditions, normalization, tractability assumptions, and equilibrium-selection/refinement assumptions.
3. Compare the formal theorem scope with the strongest prose used in the abstract, introduction, contribution statement, welfare discussion, and robustness section.
4. Distinguish clearly among:
   - existence of at least one equilibrium;
   - uniqueness of equilibrium;
   - complete equilibrium characterization;
   - a result invariant across all relevant equilibria;
   - a result conditional on one selected equilibrium;
   - a result conditional on an explicit refinement/selection rule.
5. Re-open the Stage-4A candidate-deviation audit and alternative-equilibrium audit. Verify that manuscript words such as `the equilibrium`, `unique`, `the equilibrium price`, `always`, or `regardless of equilibrium selection` are licensed by the equilibrium-set certificate rather than inferred from candidate verification.
6. Re-open every indifference/zero-payoff trigger identified at Stage 4A and verify that the manuscript does not suppress multiplicity or selection dependence created by payoff-equivalent actions.
7. Audit every equilibrium-selection/refinement condition used in the paper. State whether it is original-model structure or an added restriction; identify which equilibria it removes; verify it does not also remove the preferred equilibrium; and state what remains true without it.
8. If weak-dominance elimination or another refinement is invoked, test it symmetrically against both inconvenient and preferred equilibria.
9. Distinguish clearly among:
   - baseline closed-form result;
   - result under a restricted function class;
   - sufficient-condition theorem;
   - numerical robustness evidence;
   - conjectured generality;
   - truly general theorem.
10. For any claim over a function class such as `C^2`, convex, concave, increasing, supermodular, or single-crossing, identify which derivatives/order properties are required for each sign or uniqueness conclusion.
11. Attempt to construct admissible counterexample functions satisfying the stated class while reversing the claimed sign, concavity, uniqueness, or threshold ordering.
12. Stress-test knife-edge, near-boundary, flat-curvature, high-curvature, and nonquadratic cases when the baseline uses a convenient functional form.
13. Verify that a result proved for one parametric family is not described as generic unless a separate argument establishes genericity.
14. Audit benchmark terminology by writing the planner's optimization problem and feasible choice set. Reserve `first best` for the unrestricted relevant planner problem; otherwise use the exact constrained benchmark label.
15. Verify that `second best`, `constrained efficient`, `fixed-allocation`, `partial standardization`, `decentralized equilibrium`, and related terms match the mathematical choice sets being compared.
16. For every welfare statement, verify whether it is quantified over all relevant equilibria, one selected equilibrium, or a refinement-defined subset. If multiple markets, regions, subgames, or stages admit multiplicity, verify whether their equilibrium selections may vary independently and whether the prose covers the resulting combinations.
17. Produce a claim-scope ledger connecting each manuscript-level claim to a theorem certificate, equilibrium-set certificate, welfare-selection artifact, proof/robustness artifact, maximum defensible wording, and prohibited stronger wording.
18. Apply `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` to any headline claim whose quantifier, equilibrium-selection, benchmark, or welfare scope changed after Stage 4A.
19. Require evidence-linked PASS: `claim -> attack performed -> proof/counterexample/code artifact -> surviving limitation`. A prose assertion that a scope issue was `checked` is not sufficient.
20. Apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md` to the current, scope-certified theorem set. Reassess the preliminary Stage-4A applicability decision because theorem scope may have changed. Record exactly one final state: `FORMAL VERIFICATION PASS`, `FORMALIZATION NOT APPLICABLE — REASON RECORDED`, or a blocking state.
21. When formal verification is applicable, select the highest-value proof-critical core rather than automatically formalizing the full economic model. At minimum consider exact algebraic identities, quantified inequalities, case-partition logic, thresholds/boundaries, exact counterexamples, global-deviation inequality skeletons, equilibrium-condition implications, and welfare identities that materially support headline claims.
22. For each formalized theorem/lemma, map the proof-assistant statement to the paper claim, compare quantifiers/domains, list hypotheses supplied rather than derived, and state explicitly which economic/model components remain outside the formalization.
23. Audit the formal source for `sorry`, `admit`, equivalent placeholders, project-specific axioms, definitions that encode conclusions, and condition structures that are mistaken for proofs of economic equivalence. Retain an axiom/dependency report where supported by the proof assistant.
24. Require a pinned and reproducible formal build where feasible: proof-assistant version, library/dependency version, build command, committed source, and clean build/CI evidence. A green proof-assistant build certifies only the encoded statement; it does not replace statement-fidelity or Stage-4A economic/globality certification.
25. If the formalization uncovers a false theorem, missing economic condition, or incorrect case domain, route to the earliest affected analytic stage. If it uncovers only a mismatch between an otherwise correct narrow theorem and the formal statement/prose, repair and re-audit at the appropriate scope stage rather than weakening the mathematics silently.

## 5. Quantifier/generality/selection certificate

For each headline result record:

- manuscript claim;
- formal mathematical statement;
- quantifiers;
- equilibrium-set quantifier (`exists`, `unique`, `all equilibria`, selected/refined subset);
- domain and admissible function class;
- assumptions actually used;
- selection/refinement assumptions and provenance;
- baseline vs robustness vs general-theorem classification;
- counterexample search result;
- welfare-selection robustness status where applicable;
- benchmark terminology status;
- formal-verification applicability;
- formal theorem/lemma mapping where applicable;
- formalized assumptions versus unformalized economic components;
- formal build/axiom/placeholder status where applicable;
- attack/evidence artifact path;
- maximum defensible prose wording;
- prohibited stronger wording;
- `PASS`, `CONDITIONAL`, or `FAIL`.

## 6. Formal Verification Gate

Stage 7.5A must record exactly one pre-freeze formal-verification state.

### `FORMAL VERIFICATION PASS`

Allowed only when the applicable proof-critical targets identified under `checklists/FORMAL_VERIFICATION_CHECKLIST.md` are implemented and checked, statement fidelity is audited, no unexplained proof escape hatch remains, reproducible build evidence exists, and the limits of the formalization are explicit.

### `FORMALIZATION NOT APPLICABLE — REASON RECORDED`

Allowed only with a written, claim-specific reason explaining why neither complete nor targeted formalization would materially improve assurance for the current headline theorem set. Cost or inconvenience alone is not sufficient if a small high-risk core can be formalized usefully.

### Blocking states

`NOT TESTED`, `PLANNED`, failed compilation, stale formal theorem after a scope change, unexplained placeholder/axiom, or statement-fidelity mismatch blocks Stage-7.5A `GO` and therefore blocks Stage 8.

Formal proof is complementary to, not a substitute for, Stage 4A. Encoding assumptions such as a demand formula or condition set and proving algebra from them does not formally certify that those assumptions follow from the economic primitives unless that derivation is also represented in the assistant.

## 7. Kill tests

Stage 7.5A fails if:

- an existence proof or candidate-deviation audit is written as uniqueness or complete equilibrium characterization;
- a result valid for one selected equilibrium is written as holding for all equilibria;
- an equilibrium-selection/refinement condition is added without being disclosed or is applied asymmetrically only to inconvenient equilibria;
- a payoff-indifferent/zero-profit action creates additional equilibria that the manuscript ignores;
- a strict comparative static is claimed for a broad function class but the sign is not implied by the stated restrictions;
- concavity/convexity/uniqueness is generalized beyond what the derivatives actually guarantee;
- a parametric result is relabeled as generic robustness;
- numerical robustness is described as proof;
- an existence result is written as universal uniqueness;
- a local result is written as global;
- a sufficient condition is written as necessary and sufficient;
- a constrained planner benchmark is called `first best` without qualification;
- prose in the abstract/introduction materially exceeds the theorem/equilibrium-set certificates;
- a selection-free welfare result fails under another certified equilibrium or admissible cross-component equilibrium combination;
- an admissible counterexample exists within the claimed theorem class;
- a material PASS lacks an identifiable adversarial attack and supporting artifact;
- formal-verification applicability is left `NOT TESTED` or `PLANNED` at exit;
- an applicable formal artifact has an unresolved build, statement-fidelity, placeholder, or conclusion-smuggling defect;
- the manuscript describes the proof assistant as certifying the complete economic model, Nash correspondence, or strategy domain when only an algebraic/inequality core is formalized.

## 8. Success criteria

`GO` requires a complete claim-scope ledger with no headline theorem, equilibrium characterization, welfare statement, or benchmark overstated relative to its proof and equilibrium-set certificate.

Generality need not be maximal. A narrow but exact theorem can pass. An existence-only result can pass if described as such. A selection-conditional welfare theorem can pass if the selection condition is explicit and defensible. The gate penalizes overclaiming, not specialization.

In addition, `GO` requires exactly one acceptable formal-verification state: `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

## 9. Failure routing

- Pure wording inflation with correct underlying mathematics may be corrected within Stage 7.5A and re-audited.
- A formal-source/build defect with unchanged certified mathematics may be repaired within the Stage-7.5A Formal Verification Gate and rebuilt.
- A missing proof, false uniqueness claim, omitted equilibrium, invalid refinement, false robustness theorem, or wrong benchmark optimization problem reopens Stage 4 or Stage 7 as appropriate.
- A false theorem or missing economic assumption discovered during formalization reopens the earliest affected analytic stage; after repair, affected Stage-4A and Stage-7.5A certificates and formal artifacts must be rerun.
- A required substantive model change reopens the earliest affected stage and must subsequently repeat Stage 4A, Stage 6, Stage 7, Stage 7.5, and Stage 7.5A as applicable.

## 10. Required final output

1. Executive scope-certification verdict
2. Formal quantifier table
3. Equilibrium-set / uniqueness / selection-scope table
4. Assumption-dependence table
5. Selection/refinement provenance and symmetry audit
6. Function-class counterexample audit
7. Baseline vs robustness vs general-theorem classification
8. Welfare-selection robustness audit
9. Benchmark-definition audit
10. Claim-scope ledger
11. Evidence ledger
12. Formal-verification applicability decision
13. Formal-verification certificate or recorded `NOT APPLICABLE` rationale
14. Paper-claim ↔ formal-theorem mapping and explicit non-formalized scope, where applicable
15. Required wording downgrades, if any
16. Earliest-stage rollback requirement, if any
17. Canonical stage verdict and routing

## 11. Final verdict

Choose exactly one:

- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`
- `CONDITIONAL GO` — name exactly one scope/proof/selection/formal-verification blocker and route to the earliest affected stage
- `NO-GO / REOPEN EARLIER STAGE`

Only a `GO` may route to Stage 8 Canonical Theory Freeze, and `GO` is unavailable unless the Formal Verification Gate is closed with `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.
