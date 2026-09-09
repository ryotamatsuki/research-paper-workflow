# Formal Verification Gate Refinement — 2026-09-10

## Status

Proposed post-v2.1 backward-compatible workflow refinement.

## Problem

The canonical workflow already requires symbolic/numerical verification, independent mathematical adversarial certification, theorem-scope certification, and late hostile manuscript review. It did not, however, make proof-assistant formalization an explicit applicability decision.

That omission creates a process risk: a project can benefit materially from targeted formal proof but still reach theory freeze without anyone recording whether formalization was considered. Conversely, making Lean or another assistant mandatory for every theorem would create unnecessary work and could encourage superficial formalization of easy algebra while leaving the economically fragile step outside the assistant.

A recent correction-paper workflow supplied a useful regression lesson. Targeted Lean certification was valuable for the long-arc identity, exact counterexample arithmetic, quantified inequality skeleton, equilibrium-condition implications, and welfare identities. At the same time, the formal source did not reconstruct the entire economic demand correspondence or the complete Nash-equilibrium problem from primitives. The useful lesson is therefore not `formalize everything`; it is `make applicability explicit, formalize the highest-value proof-critical core, and certify the boundary of the formal model`.

## Design

The refinement does **not** add a new canonical Stage.

It uses the existing route:

`Stage 4 → Stage 4A → Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A → Stage 8`.

The formal-verification lifecycle is embedded as follows:

1. **Stage 4A — planning:** record `FORMALIZATION APPLICABLE` with a preliminary target map, or a reasoned preliminary N/A decision. Formal proof is not counted as the independent hostile certification itself.
2. **Stage 7.5A — execution/closure:** reassess applicability after theorem scope is stable. The Stage may issue `GO` only with `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.
3. **Stage 8 — freeze:** retain the formal certificate/N-A rationale, theorem mapping, encoded assumptions, non-formalized scope, toolchain/build provenance, and axiom/placeholder status.
4. **Stage 9 — reproducibility:** preserve formal source and pinned build dependencies in the production repository when applicable.
5. **Stage 11 — hostile regression:** attack proof-assistant scope inflation and stale formal statements after manuscript integration.
6. **Stage 14 — submission QA:** rebuild or re-verify the frozen formal artifact where applicable and check that manuscript claims still match formal coverage.
7. **Stage 15 — submission freeze:** retain the exact formal source/build certificate or the recorded N/A rationale with the immutable submission state.

## Applicability rule

Formal verification is normally useful for high-consequence claims involving nontrivial algebra/order reasoning, quantified inequalities, piecewise cases, thresholds/boundaries, global-deviation inequality partitions, equilibrium-condition implications, welfare identities, and mathematical corrections to published work.

Full-model formalization is not the default requirement. A project should first ask whether a smaller proof-critical core materially reduces residual risk.

The passing pre-freeze states are exactly:

- `FORMAL VERIFICATION PASS`; or
- `FORMALIZATION NOT APPLICABLE — REASON RECORDED`.

`NOT TESTED` and `PLANNED` do not pass.

## Proof-assistant boundary rule

A green Lean/Coq/Isabelle/etc. build proves the encoded theorem from the encoded assumptions. It does not by itself show that:

- a demand formula follows from the economic primitives;
- a case partition is exhaustive;
- a candidate condition is equivalent to Nash equilibrium;
- all asymmetric/mixed/off-path equilibria were covered; or
- the manuscript theorem has the same quantifiers as the formal theorem.

Accordingly, every formal certificate must include statement-fidelity and model-boundary records. Formal verification is complementary to Stage 4A and Stage 7.5A, not a replacement.

## Safety controls

The new checklist requires, where applicable:

- paper-claim ↔ formal-theorem mapping;
- quantifier/domain comparison;
- assumptions/hypotheses supplied rather than proved;
- explicit non-formalized scope;
- proof-assistant and library version pinning where feasible;
- clean build/CI evidence;
- `sorry`/`admit`/equivalent placeholder audit;
- project-specific axiom/conclusion-smuggling audit;
- stale-certificate invalidation after theorem or encoded-hypothesis changes.

## Version classification

Under `docs/VERSIONING_POLICY.md`, this is a **MINOR-version class** change.

Reason:

- no Stage is added, removed, merged, or renumbered;
- `GO / CONDITIONAL GO / NO-GO` meanings are unchanged;
- normal canonical routing is unchanged;
- the one-diagnosed-fix rule is unchanged;
- rollback and freeze semantics are strengthened but not replaced;
- the change adds a verification obligation inside existing Stage boundaries.

It is therefore a natural candidate for a future `v2.2`, subject to integration review and release procedure. The existing `v2.1` tag must not be moved.

## Canonical files affected

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_04A_MATH_RED_TEAM.md`
- `templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`
- `templates/STAGE_08_THEORY_FREEZE.md`
- `checklists/FORMAL_VERIFICATION_CHECKLIST.md`
- `checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`
- `README.md`
- `docs/VERSIONING_POLICY.md`

## Intended effect

The workflow should now make it mechanically difficult to reach theory freeze while simply forgetting formal verification. At the same time, it should remain possible to record a defensible N/A decision instead of forcing low-value or performative full formalization.