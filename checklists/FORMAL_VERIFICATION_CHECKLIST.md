# Formal Verification Checklist

Use this checklist for theorem-bearing theory projects before Stage 8 theory freeze. Its purpose is to make formal verification a deliberate, recorded decision rather than an optional step that can be forgotten.

Formal verification is an additional proof-assurance layer. It does **not** replace Stage 4 construction, Stage 4A independent adversarial certification, global-deviation analysis, alternative-equilibrium search, counterexample search, or Stage 7.5A quantifier/scope certification.

The required pre-freeze outcome is exactly one of:

- `FORMAL VERIFICATION PASS`; or
- `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

`NOT TESTED`, `PLANNED`, `PARTIAL BUT UNASSESSED`, compilation failure, or an unexplained omission is not a passing state.

## 1. Applicability decision

Record the applicability decision explicitly for the project and for each headline theorem/proposition.

Formal verification should normally be treated as applicable when one or more proof-critical claims depend materially on:

- nontrivial algebraic or order identities;
- piecewise cases, regime partitions, kinks, or threshold logic;
- quantified inequalities over parameter ranges;
- global-deviation partitions or best-response inequalities;
- existence, uniqueness, multiplicity, or equilibrium-selection conditions;
- boundary or knife-edge cases;
- welfare identities or cancellations central to the contribution;
- a correction/replication claim that a published mathematical result is false;
- a proof component whose failure would materially change the paper's headline result.

Do not mark the project `NOT APPLICABLE` merely because a full formalization of the economic model would be expensive. First ask whether a smaller proof-critical core can be formalized usefully.

`FORMALIZATION NOT APPLICABLE` is allowed only with a written reason explaining why formalizing either the whole claim or a material proof-critical core would not add meaningful assurance relative to the certified evidence already available.

## 2. Formalization target map

Before implementation, create a target map:

`claim ID | paper theorem/proposition | proof-critical component | formalization target | excluded component | reason for exclusion | expected assurance gain`.

Prioritize components that are both mechanically formalizable and high-consequence. Typical targets include:

- algebraic identities and factorization;
- inequality signs over exact parameter domains;
- case exhaustiveness once the cases themselves are correctly specified;
- threshold ordering and boundary consistency;
- exact counterexamples;
- welfare identities;
- logical implications among already certified conditions.

Do not spend effort formalizing decorative or low-risk algebra while leaving the actual theorem's fragile step outside the target map without explanation.

## 3. Tool choice

Lean 4 with mathlib is the default recommended assistant for new project-specific formal proof artifacts when no other proof assistant is already established. Coq, Isabelle/HOL, Agda, HOL, or another auditable proof assistant may be used when better matched to the project.

Record:

- proof assistant and version;
- standard library and exact version/commit where feasible;
- package/dependency lock information;
- build command;
- platform assumptions that matter to reproduction.

The workflow requires a formal certificate, not allegiance to one tool.

## 4. Statement fidelity

For every formalized result:

- [ ] Map the formal theorem/lemma name to the paper claim ID.
- [ ] State the exact formal theorem signature.
- [ ] Compare its quantifiers with the paper theorem.
- [ ] Compare parameter domains and inequality strictness.
- [ ] Compare strategy/function domains where represented.
- [ ] Identify assumptions passed into the theorem rather than proved inside the assistant.
- [ ] Identify economic primitives or demand/equilibrium facts encoded as hypotheses.
- [ ] Confirm the formal theorem is not materially weaker than the component it is claimed to certify.
- [ ] Confirm no manuscript prose says the assistant proves a larger object than it actually formalizes.

A theorem that proves `P -> Q` does not certify `P` unless `P` is separately derived or formalized.

## 5. No conclusion-smuggling

Audit the formal source for assumptions, axioms, definitions, and helper lemmas that could encode the desired conclusion.

- [ ] No `sorry`, `admit`, placeholder proof, or equivalent escape hatch remains in the certified source.
- [ ] Any project-specific axiom is listed and justified.
- [ ] Standard logical/library axioms are distinguished from project-specific assumptions.
- [ ] Definitions do not bake the theorem conclusion into the object being certified.
- [ ] A condition structure such as `UCond` or `CandidateCond` is not presented as a formal proof of equivalence to Nash equilibrium unless that equivalence is itself formalized.
- [ ] Imported generated facts are provenance-audited and are not treated as proof merely because they are imported.

Where the proof assistant supports it, retain an axiom/dependency report such as `#print axioms` or an equivalent artifact for headline formal theorems.

## 6. Model-boundary certificate

Formal verification must state explicitly what remains outside the formal model.

Record at minimum:

- primitives derived inside the assistant;
- primitives assumed as hypotheses;
- demand/allocation correspondence formalized or not;
- equilibrium definition formalized or not;
- global best-response domain formalized or not;
- case partition derived from primitives or assumed;
- welfare accounting derived or assumed;
- asymmetric/mixed/off-path objects formalized or excluded, where relevant.

If the assistant certifies only a proof-critical algebraic/inequality core, say exactly that. Do not call it a formal certification of the complete model or equilibrium correspondence.

## 7. Build and reproducibility

- [ ] Formal source is committed to the project repository or an immutable linked repository.
- [ ] Toolchain version is pinned where feasible.
- [ ] Dependency versions/commits are pinned where feasible.
- [ ] A clean build command is documented.
- [ ] The formal target builds from a clean checkout/environment.
- [ ] CI runs the formal build where practical.
- [ ] CI or an explicit audit checks for `sorry`/`admit`/equivalent placeholders.
- [ ] The build output or workflow run is retained as evidence.
- [ ] Formal source included in reproducibility/submission supplement is the same certified source or its exact frozen descendant.

A green build establishes proof-assistant acceptance of the encoded statements. It does not establish that the encoded statements faithfully represent the economic model; statement fidelity remains a separate audit.

## 8. Interaction with independent certification

Formal proof and independent adversarial certification answer different questions.

- Formal proof: does the encoded statement follow from the encoded assumptions under the proof assistant's kernel?
- Stage 4A / Stage 7.5A: are the assumptions, cases, strategy domains, equilibrium concept, quantifiers, and economic interpretation the right ones?

Therefore:

- [ ] Do not count compilation of the production formalization as the independent Stage-4A attack by itself.
- [ ] Preserve clean-room derivation/counterexample/global-deviation work even when Lean passes.
- [ ] If formalization exposes a missing assumption or false theorem, route to the earliest affected analytic stage rather than patching only the formal statement.
- [ ] If the paper theorem changes materially after formal certification, mark the formal certificate stale and repeat the affected formal build/certificate before refreeze.

## 9. Required certificate

For every project with `FORMAL VERIFICATION PASS`, preserve a certificate containing at least:

1. proof assistant/toolchain/library versions;
2. formal source paths;
3. paper-claim-to-formal-theorem map;
4. theorem signatures and quantifier/domain comparison;
5. assumptions/hypotheses imported rather than proved;
6. axiom/placeholder audit;
7. clean-build/CI evidence;
8. proof-critical components certified;
9. components explicitly not certified;
10. known limitations and surviving risks;
11. rollback rule if the theorem or assumptions change;
12. final formal-verification state.

Suggested evidence row:

`claim | formal theorem | encoded assumptions | certified component | not certified | build evidence | axiom/placeholder status | state`.

## 10. Passing states

### `FORMAL VERIFICATION PASS`

Use only when:

- the applicability target map is complete;
- the selected high-value formal targets compile/check successfully;
- statement fidelity has been audited;
- no unexplained placeholder or conclusion-smuggling issue remains;
- toolchain/build provenance is reproducible;
- limitations are explicit; and
- the formal certificate matches the current theorem scope.

### `FORMALIZATION NOT APPLICABLE — REASON RECORDED`

Use only when the project records why neither full nor targeted formalization would materially improve assurance for the current headline claims. The reason must be claim-specific enough to audit later.

### Blocking states

The following block Stage-7.5A `GO` and Stage 8 entry:

- `NOT TESTED`;
- `PLANNED`;
- applicable formalization with a failed build;
- unresolved statement-fidelity mismatch;
- unexplained `sorry`/`admit`/equivalent placeholder;
- project-specific axiom that effectively assumes the conclusion;
- formal certificate stale after a material theorem/quantifier change.

## 11. Rollback rules

- False theorem or missing economic condition discovered during formalization → Stage 4/4A or earlier as appropriate.
- Welfare identity/benchmark defect → Stage 7 or Stage 4 depending on source.
- Quantifier/scope mismatch with correct narrow theorem → Stage 7.5A.
- Formal source/build defect only, with unchanged certified mathematics → repair inside the Stage-7.5A formal-verification gate and rerun it.
- Post-freeze theorem/assumption change → Stage 8 change control plus earliest affected analytic/formal gates.

Formal verification is successful when it makes the proof boundary more explicit and the high-consequence core mechanically checkable. It is not successful merely because a proof assistant appears in the repository.