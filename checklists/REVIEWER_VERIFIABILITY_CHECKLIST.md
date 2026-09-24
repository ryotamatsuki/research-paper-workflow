# Reviewer Verifiability Checklist

Use this checklist for theorem-bearing, proof-heavy, computational, structural, quantitative, or otherwise technically dense manuscripts whenever a referee must be able to verify a material derivation or proof chain from the manuscript-facing package.

The target reader is a competent specialist referee, not an undergraduate. The standard is therefore **not** “show every algebraic step.” The standard is:

> A referee should be able to identify the mathematical/evidentiary object being proved, follow the non-routine derivation and implication chain without guessing missing bridges, understand exactly what any computer-assisted component certifies, and locate enough reproducible detail to verify the delegated computation.

This checklist complements mathematical correctness, formal verification, and exposition streamlining. It does not replace them.

## 1. Applicability and scope

Record one:

- [ ] **FULL** — headline results materially depend on nontrivial derivations, proofs, exact computation, formal verification, or technical identification/estimation logic.
- [ ] **PARTIAL** — only specified sections/results require reviewer-verifiability auditing.
- [ ] **NOT MATERIAL** — explain why no material result depends on a derivation/proof chain requiring this audit.

For each material result, record:

`claim/result | manuscript location | derivation/proof location | computational/formal artifact if any | reviewer-verifiability state`.

## 2. Governing distinction

Do not confuse these three standards:

1. **Correctness** — is the claim actually true under the stated assumptions?
2. **Reproducibility** — can the computation/formal artifact be rerun?
3. **Reviewer verifiability** — can a specialist referee understand and check the logical route from manuscript primitives/evidence to the claim without reconstructing unstated bridges?

A green solver, CI run, symbolic notebook, or proof-assistant build can support correctness/reproducibility while the manuscript still fails reviewer verifiability.

## 3. Derivation-chain audit

For every headline theorem, proposition, equilibrium characterization, welfare result, correction claim, structural object, or other proof-critical result:

- [ ] Start from primitives, definitions, or identified inputs that are visible in the manuscript or explicitly cross-referenced.
- [ ] Identify every non-routine transformation that changes the mathematical/economic object.
- [ ] Show the short bridge equation when omitting it would force the reader to infer how one object became another.
- [ ] Define intermediate objects before they are used in a proof or certificate.
- [ ] State the domain and assumptions under which each key transformation is valid.
- [ ] Distinguish local/branch calculations from global results.
- [ ] Distinguish a stationary point/FOC solution from a global optimum or equilibrium.
- [ ] For sequential games, show how upstream policies/actions map into downstream continuation objects used in deviations.
- [ ] For welfare or expected-payoff calculations, show how state/profile-specific objects are aggregated when that aggregation is proof-critical.
- [ ] For matrix/KKT/active-set reductions, display the compact system or conditions when they are the bridge to later claims.
- [ ] For empirical/structural work, provide the analogous bridge from primitive data/moments/likelihood/estimating equations to the reported estimator or counterfactual object when nonstandard.

The manuscript may suppress routine repeated algebra. It may not suppress the bridge that tells the referee **what was algebraically transformed into what**.

## 4. Proof exposition audit

For every formal theorem/proposition/lemma whose proof is material:

- [ ] The proof has a visible start and end under the journal/style convention.
- [ ] The proof states which earlier definitions/lemmas are being used.
- [ ] Each nontrivial implication is justified by a named property, displayed calculation, lemma, or explicit argument.
- [ ] Phrases such as “straightforward algebra,” “it follows,” “similarly,” or “the certificate verifies” do not hide multiple proof-critical transformations.
- [ ] If concavity/convexity is used to turn an FOC into a global result, the relevant domain and sign argument are explicit.
- [ ] If contraction, monotonicity, fixed-point, envelope, implicit-function, or other theorem machinery is used, the conditions actually needed for the application are visible or clearly cross-referenced.
- [ ] Boundary/corner conclusions are explained when the headline claim is global.
- [ ] A proof that relies on several lemmas states how those lemmas combine to yield the theorem.
- [ ] Proof notation matches the main manuscript notation and does not silently change domains or normalization.

A referee should not have to reverse-engineer the intended proof architecture from code or scratch files.

## 5. Computer-assisted / exact-certificate bridge

When any material claim relies on symbolic computation, exact arithmetic, root isolation, interval arithmetic, Bernstein/SOS certificates, exhaustive enumeration, theorem-prover output, or another computer-assisted proof step:

- [ ] The manuscript names the exact mathematical object being certified.
- [ ] The manuscript states the domain on which the certificate applies.
- [ ] The manuscript states the exact property certified: sign, root count, uniqueness, positivity, feasibility, exhaustive case coverage, implication, etc.
- [ ] The manuscript explains why that certified property implies the stated lemma/theorem.
- [ ] The route from manuscript primitives to the certified object is visible through equations or explicit cross-references.
- [ ] The route from the certified property back to the economic/statistical conclusion is visible.
- [ ] Any normalization/scaling that affects sign or interpretation is stated.
- [ ] Numerical stress tests are not presented as substitutes for exact/analytic proof when the claim is exact.
- [ ] Reproduction artifacts identify the script/formal theorem/certificate that checks the claim.

### Acceptable delegation

The following may normally be moved to Appendix/Supplement/code when they are mechanically generated and do not improve human understanding:

- very long polynomial expansions;
- long coefficient lists;
- repetitive case arithmetic after the cases are defined;
- raw root-isolation traces;
- machine-generated exact rational numerators/denominators;
- routine symbolic simplification;
- proof-assistant kernel traces.

However, delegation is acceptable only if the manuscript still identifies the input object, the certified property, and the logical implication.

### Automatic failure examples

Fail reviewer verifiability if a material proof says only:

- “computer verification confirms the theorem”;
- “all coefficients have the required sign” without identifying the polynomial/certificate target;
- “the solver finds the unique equilibrium” without showing the equilibrium conditions/domain and why uniqueness follows;
- “formal verification passes” without mapping the formal theorem to the paper claim;
- “substitution yields the result” when the substitution crosses several economically distinct stages and the aggregation/bridge is not shown.

## 6. Reviewer reconstruction test

Perform one clean-room pass using the manuscript-facing package rather than the production derivation/code path.

For each headline result, attempt to reconstruct this chain:

`primitives / data / definitions`
→ `key intermediate objects`
→ `equilibrium / estimator / welfare / certificate target`
→ `lemma / proposition`
→ `headline theorem / substantive conclusion`.

Record every point where the reviewer would have to guess:

- an omitted equation;
- an undefined intermediate object;
- an unstated normalization;
- an unstated aggregation;
- an unstated domain;
- an unexplained move from local to global;
- an unexplained move from numerical to exact;
- an unexplained move from a machine certificate to the economic conclusion.

Classify each gap:

- **ROUTINE** — standard one-step manipulation a specialist can reasonably supply.
- **BRIDGE NEEDED** — short displayed equation or sentence should be added.
- **APPENDIX DETAIL NEEDED** — derivation belongs in Appendix/Supplement.
- **SUBSTANTIVE DEFECT** — the gap may reflect an unproved or false claim; route to the earliest affected research stage.

The purpose is not pedagogical completeness. It is to eliminate avoidable referee guesswork at proof-critical transitions.

## 7. Compression versus verifiability

Exposition streamlining must not remove proof-critical bridges.

Before deleting or moving technical material, ask:

- [ ] Does the main text still identify the object being solved/certified?
- [ ] Does the referee still see how the preceding model/evidence produces that object?
- [ ] Does the referee still see why the certified property implies the paper claim?
- [ ] Is the omitted material routine/repetitive rather than conceptually connective?
- [ ] Is the Appendix/Supplement cross-reference precise enough to recover the omitted detail?

The rule is:

> Compress routine algebra; preserve conceptual bridges.

## 8. Article-type adaptations

### Theory-first

Prioritize:

- primitives → payoff/equilibrium system;
- equilibrium system → continuation/selection object;
- state/profile objects → expected payoff/welfare;
- local conditions → globality argument;
- model object → computer-assisted certificate target;
- lemma chain → theorem.

### Correction / comment / reassessment

Prioritize:

- source statement → exact defect;
- corrected assumptions/domain → corrected proposition;
- source proof step → replacement proof step;
- mathematical correction → substantive consequence.

### Structural / quantitative / empirical

Apply the same logic to:

- data/moments → identifying equations;
- identifying equations → estimator;
- estimator/parameters → counterfactual/welfare object;
- numerical algorithm → economic/statistical claim;
- computational approximation → error/robustness statement.

The manuscript need not teach standard econometrics or numerical analysis, but it must expose any nonstandard or claim-critical bridge.

## 9. Stage-specific obligations

### Stage 10 — construction

Before or while drafting technical sections:

- [ ] identify the proof/derivation chain for each headline result;
- [ ] mark which intermediate equations are **BRIDGE EQUATIONS** that must remain visible;
- [ ] decide what routine algebra can move to Appendix/Supplement;
- [ ] identify every computer-assisted or formal target and how it connects to manuscript objects;
- [ ] avoid finalizing proof prose that depends on unnamed placeholder objects.

Recommended artifact: `REVIEWER_VERIFIABILITY_MAP.md`.

### Stage 11 — hostile referee attack

Independently attempt the reviewer reconstruction test.

- [ ] Reconstruct at least one complete headline proof/derivation from the manuscript-facing package.
- [ ] Flag every proof-critical jump that requires guessing or opening production code merely to learn what object is being proved.
- [ ] Attack “straightforward algebra,” “by symmetry,” “the certificate verifies,” and similar compression phrases.
- [ ] Distinguish exposition gaps from substantive mathematical defects.
- [ ] Treat a newly discovered substantive defect as a certification regression.

### Stage 13 — integrated manuscript audit

Run this checklist on the actual integrated manuscript.

- [ ] Every headline result has an intact derivation/proof chain.
- [ ] Proof-critical bridge equations survived streamlining.
- [ ] Main-text/Appended detail is split by conceptual importance rather than by arbitrary length.
- [ ] Computer-assisted proof sections identify object, domain, certified property, and implication.
- [ ] Formal-verification claims map to the manuscript claim without forcing the referee to inspect source code merely to understand scope.
- [ ] Produce `REVIEWER_VERIFIABILITY_REPORT.md` or equivalent.

A material reviewer-verifiability failure blocks Stage-13 closure.

### Stage 14 — submission QA

Binary final check:

- [ ] Stage-13 reviewer-verifiability report exists or equivalent evidence is preserved.
- [ ] Journal formatting did not remove bridge equations, proof boundaries, definitions, or Appendix cross-references.
- [ ] The exact submission PDF/package preserves the claim → derivation → proof/certificate → conclusion chain.
- [ ] No material proof now depends on an undefined object or opaque machine result.
- [ ] All delegated computational/formal artifacts referenced by the manuscript are present and reproducible as required.

A presentation-only gap normally reopens Stage 13. A proof-architecture design failure may reopen Stage 10. A gap that reveals an unproved/false claim reopens the earliest affected research stage.

## 10. Passing standard

Record one:

- **PASS — REVIEWER VERIFIABILITY**: a competent specialist referee can follow and audit every material proof/derivation chain from the manuscript-facing package; delegated computations are mathematically identified and reproducible; no material bridge requires guesswork.
- **CONDITIONAL**: one precise exposition/bridge blocker remains, with an explicit repair location.
- **FAIL**: a material result relies on an opaque, undefined, or logically disconnected derivation/certificate, or the audit exposes a substantive proof defect.

This PASS is not a claim that every equation can be reproduced by hand from the PDF. It means the manuscript exposes enough mathematics and logic for a specialist referee to verify what is being claimed, what has been delegated, and why the evidence supports the conclusion.
