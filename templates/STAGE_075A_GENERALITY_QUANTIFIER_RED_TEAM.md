# Stage 7.5A — Generality / Quantifier / Portability Red-Team Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a hostile theory editor focused on theorem scope and economic portability rather than algebra alone. Your job is to determine both (i) whether the paper claims more generality, uniqueness, equilibrium-selection robustness, or welfare robustness than the proved object supports and (ii) how far the headline economic mechanism actually survives credible changes in microfoundation or institution.

Do not reward elegant prose, a plausible mechanism, or a successful baseline calibration. Attack quantifiers, admissible function classes, equilibrium-set language, selection/refinement assumptions, benchmark definitions, robustness claims, hidden functional-form dependence, and the exact boundary between a portable mechanism and a model-specific result. This stage is journal-neutral: do not use a desired outlet to decide what counts as robust.

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
- Pre-specified portability/falsification plan: `[PORTABILITY_PLAN]`
- Planner/benchmark definitions: `[BENCHMARKS]`

## 2. Stage objective

Certify that every headline theorem, robustness statement, equilibrium characterization, welfare benchmark, and contribution sentence states exactly the scope that has actually been proved before theory freeze, and determine the maximum defensible research strength of each headline mechanism through pre-specified economic falsification.

Stage 7.5 may decide that a project deserves a full paper. Stage 7.5A separately decides whether its theorem scope, equilibrium-set language, selection robustness, generality claims, and cross-model portability claims are licensed. It must produce a Contribution Robustness Certificate that Stage 12 later uses for journal positioning.

Stage 7.5A is also the final pre-freeze **Formal Verification Gate**. The Stage number and routing do not change: formal verification is an embedded certification obligation inside Stage 7.5A, not a new canonical Stage. Stage 7.5A may issue `GO` only after the project records either `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED` under `checklists/FORMAL_VERIFICATION_CHECKLIST.md`.

## 3. Frozen inputs

No result-driven rescue mechanism, player, instrument, equilibrium refinement, or theorem engineering is allowed inside this gate. Stage 7.5A may introduce only pre-specified diagnostic alternatives whose purpose is to test the portability of the existing mechanism. A diagnostic alternative does not become canonical theory merely because it produces an attractive result. Any substantive strengthening or new mechanism routes back to the earliest affected research stage and then repeats downstream certification.

Formalization or portability testing may expose a missing assumption, false inequality, incomplete case partition, hidden functional-form dependence, or theorem-scope mismatch. Such a discovery is evidence about the existing theory; it does not authorize silent weakening, result-driven redesign, or alteration of the theorem merely to recover the desired conclusion.

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
14. Identify the **mechanism invariant** for each headline economic claim: the smallest causal/strategic object that should survive if the claim is genuinely portable rather than merely preserving one closed-form sign.
15. For every headline claim presented as more than baseline/model-specific, apply `checklists/PORTABILITY_FALSIFICATION_CHECKLIST.md`. Before solving, pre-specify at least one economically meaningful alternative formulation that changes a plausibly result-driving feature such as demand substitution, strategic variable, network microfoundation, cost technology, timing, information, heterogeneity, or coalition/institutional rule.
16. Record ex ante the alternative's primitives, equilibrium concept, why it is economically credible, and the exact survival/failure criterion. Commit or otherwise timestamp the diagnostic specification before computing the result.
17. Re-solve the affected equilibrium/subgame under the alternative formulation. Do not transport baseline formulas into a domain where their derivation no longer applies.
18. If the first portability test survives but remains too close to the baseline to support the manuscript's breadth, pre-specify an orthogonal second attack. Do not choose a favorable second alternative after an unfavorable first result.
19. If portability fails, identify the payoff component, assumption, sign condition, or institutional rule that carries the failure where possible, and attempt an abstract sufficient-condition formulation without redesigning the failed alternative.
20. Classify each headline claim as exactly one of `PORTABLE`, `CONDITIONALLY PORTABLE`, `MODEL-SPECIFIC`, `INSTITUTION-SPECIFIC`, or `FALSIFIED`.
21. Apply the stop rule: if two economically meaningful, pre-specified, non-cosmetic portability attacks overturn the same claimed cross-model mechanism and no defensible abstract sufficient-condition theorem survives, normally close the portability claim as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` instead of repeatedly redesigning alternatives to rescue it.
22. Preserve negative portability results, exact counterexamples, and failure boundaries as first-class research artifacts.
23. Produce a **Contribution Robustness Certificate** for every headline claim, including the mechanism invariant, pre-specified alternatives, evidence artifacts, essential assumptions/failure boundaries, portability classification, maximum defensible wording, prohibited stronger wording, and stop-rule status.
24. Audit benchmark terminology by writing the planner's optimization problem and feasible choice set. Reserve `first best` for the unrestricted relevant planner problem; otherwise use the exact constrained benchmark label.
25. Verify that `second best`, `constrained efficient`, `fixed-allocation`, `partial standardization`, `decentralized equilibrium`, and related terms match the mathematical choice sets being compared.
26. For every welfare statement, verify whether it is quantified over all relevant equilibria, one selected equilibrium, or a refinement-defined subset. If multiple markets, regions, subgames, or stages admit multiplicity, verify whether their equilibrium selections may vary independently and whether the prose covers the resulting combinations.
27. Produce a claim-scope ledger connecting each manuscript-level claim to a theorem certificate, equilibrium-set certificate, welfare-selection artifact, proof/robustness artifact, portability classification, Contribution Robustness Certificate entry, maximum defensible wording, and prohibited stronger wording.
28. Apply `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` to any headline claim whose quantifier, equilibrium-selection, benchmark, or welfare scope changed after Stage 4A.
29. Require evidence-linked PASS: `claim -> attack performed -> proof/counterexample/code artifact -> surviving limitation`. A prose assertion that a scope issue was `checked` is not sufficient.
30. Apply `checklists/FORMAL_VERIFICATION_CHECKLIST.md` to the current, scope-certified theorem set. Reassess the preliminary Stage-4A applicability decision because theorem scope may have changed. Record exactly one final state: `FORMAL VERIFICATION PASS`, `FORMALIZATION NOT APPLICABLE — REASON RECORDED`, or a blocking state.
31. When formal verification is applicable, select the highest-value proof-critical core rather than automatically formalizing the full economic model. At minimum consider exact algebraic identities, quantified inequalities, case-partition logic, thresholds/boundaries, exact counterexamples, global-deviation inequality skeletons, equilibrium-condition implications, and welfare identities that materially support headline claims.
32. For each formalized theorem/lemma, map the proof-assistant statement to the paper claim, compare quantifiers/domains, list hypotheses supplied rather than derived, and state explicitly which economic/model components remain outside the formalization.
33. Audit the formal source for `sorry`, `admit`, equivalent placeholders, project-specific axioms, definitions that encode conclusions, and condition structures that are mistaken for proofs of economic equivalence. Retain an axiom/dependency report where supported by the proof assistant.
34. Require a pinned and reproducible formal build where feasible: proof-assistant version, library/dependency version, build command, committed source, and clean build/CI evidence. A green proof-assistant build certifies only the encoded statement; it does not replace statement-fidelity or Stage-4A economic/globality certification.
35. If the formalization uncovers a false theorem, missing economic condition, or incorrect case domain, route to the earliest affected analytic stage. If it uncovers only a mismatch between an otherwise correct narrow theorem and the formal statement/prose, repair and re-audit at the appropriate scope stage rather than weakening the mathematics silently.

### Author intellectual-contribution checkpoint

Before this Stage can issue `GO`, apply `checklists/AI_PROVENANCE_AUTHOR_ACCOUNTABILITY_CHECKLIST.md` and create an `AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD` or equivalent for each central result/set of tightly related central results.

The record must identify the author's substantive judgment on:

- the economic mechanism and why it matters;
- the assumptions/restrictions carrying the central result;
- the proof/equilibrium logic and its material weak points;
- boundary conditions, failure cases, and limitations;
- what was checked by the author versus AI, computation, formal proof, or an external human;
- the maximum defensible theorem/contribution wording.

A universal AI-free rediscovery or memorized re-proof is not required. However, an AI explanation, AI audit, computation, or green Lean/proof-assistant build cannot by itself satisfy this checkpoint.

## 5. Quantifier/generality/selection certificate and Contribution Robustness Certificate

For each headline result record:

- manuscript claim;
- formal mathematical statement;
- quantifiers;
- equilibrium-set quantifier (`exists`, `unique`, `all equilibria`, selected/refined subset);
- domain and admissible function class;
- assumptions actually used;
- selection/refinement assumptions and provenance;
- baseline vs robustness vs general-theorem classification;
- mechanism invariant;
- pre-specified diagnostic alternatives and ex ante success/failure criteria;
- portability-test result and artifact path;
- essential assumption/failure boundary where identified;
- portability classification (`PORTABLE`, `CONDITIONALLY PORTABLE`, `MODEL-SPECIFIC`, `INSTITUTION-SPECIFIC`, or `FALSIFIED`);
- stop-rule status and whether further generality engineering is authorized;
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
- an alternative formulation was chosen or redesigned after observing results in order to rescue the preferred sign;
- a cosmetic perturbation is presented as economic portability;
- the alternative equilibrium was not independently re-solved on its own valid domain;
- a material portability failure is hidden, omitted, or dismissed without narrowing the claim;
- the stop rule is triggered but the manuscript continues to call the mechanism general/robust without an abstract sufficient-condition theorem;
- a material PASS lacks an identifiable adversarial attack and supporting artifact;
- formal-verification applicability is left `NOT TESTED` or `PLANNED` at exit;
- an applicable formal artifact has an unresolved build, statement-fidelity, placeholder, or conclusion-smuggling defect;
- the manuscript describes the proof assistant as certifying the complete economic model, Nash correspondence, or strategy domain when only an algebraic/inequality core is formalized.

## 8. Success criteria

`GO` requires a complete claim-scope ledger and Contribution Robustness Certificate with no headline theorem, equilibrium characterization, welfare statement, benchmark, or portability claim overstated relative to its proof and equilibrium-set evidence.

Generality need not be maximal. A narrow but exact theorem can pass, including a result correctly classified as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC`. An existence-only result can pass if described as such. A selection-conditional welfare theorem can pass if the selection condition is explicit and defensible. The gate penalizes overclaiming and result-driven rescue, not specialization.

In addition, `GO` requires exactly one acceptable formal-verification state: `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

## 9. Failure routing

- Pure wording inflation with correct underlying mathematics may be corrected within Stage 7.5A and re-audited.
- A formal-source/build defect with unchanged certified mathematics may be repaired within the Stage-7.5A Formal Verification Gate and rebuilt.
- A missing proof, false uniqueness claim, omitted equilibrium, invalid refinement, false robustness theorem, or wrong benchmark optimization problem reopens Stage 4 or Stage 7 as appropriate.
- A false theorem or missing economic assumption discovered during formalization reopens the earliest affected analytic stage; after repair, affected Stage-4A and Stage-7.5A certificates and formal artifacts must be rerun.
- A portability failure that only narrows the claim may be certified here as `MODEL-SPECIFIC` or `INSTITUTION-SPECIFIC` with no repair required.
- A diagnostic alternative that reveals a genuinely valuable new mechanism or a required substantive model change reopens the earliest affected stage and must subsequently repeat Stage 4A, Stage 6, Stage 7, Stage 7.5, and Stage 7.5A as applicable.
- A journal preference is never sufficient reason by itself to authorize that rollback; journal fit is assessed later at Stage 12.

## 10. Required final output

1. Executive scope-certification verdict
2. Formal quantifier table
3. Equilibrium-set / uniqueness / selection-scope table
4. Assumption-dependence table
5. Selection/refinement provenance and symmetry audit
6. Function-class counterexample audit
7. Pre-specified economic portability/falsification plan and execution record
8. Contribution Robustness Certificate with per-claim portability classification and stop-rule status
9. Baseline vs robustness vs general-theorem classification
10. Welfare-selection robustness audit
11. Benchmark-definition audit
12. Claim-scope ledger
13. Evidence ledger
14. Formal-verification applicability decision
15. Formal-verification certificate or recorded `NOT APPLICABLE` rationale
16. Paper-claim ↔ formal-theorem mapping and explicit non-formalized scope, where applicable
17. Required wording downgrades, if any
18. Earliest-stage rollback requirement, if any
19. Canonical stage verdict and routing

## 11. Final verdict

Choose exactly one:

- `GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS`
- `CONDITIONAL GO` — name exactly one scope/proof/selection/formal-verification blocker and route to the earliest affected stage
- `NO-GO / REOPEN EARLIER STAGE`

Only a `GO` may route to Stage 8 Canonical Theory Freeze, and `GO` is unavailable unless the Formal Verification Gate is closed with `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.
