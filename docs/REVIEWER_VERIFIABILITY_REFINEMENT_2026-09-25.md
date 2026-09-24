# Reviewer Verifiability / Proof Exposition Refinement — 2026-09-25

## Status

Prospective v2.7 minor refinement.

## Problem

The workflow already separated mathematical correctness, independent adversarial certification, formal verification, reproducibility, and exposition streamlining. A remaining failure mode was not explicit enough: a manuscript could pass those checks while still making a specialist referee reconstruct unstated proof-critical bridges.

Typical examples include:

- a proof says a two-equation system is solved but never displays the compact system that later determinant/interiority claims refer to;
- state/profile-specific objects are defined, but the aggregation that produces the policy/welfare object used by the theorem is omitted;
- a computer-assisted proof says a certificate verifies a sign or root without identifying the exact manuscript object, domain, or implication;
- streamlining removes the equation that connects an economic model to a later exact certificate;
- a proof is reproducible from code but not understandable as a mathematical argument from the manuscript-facing package.

These are not necessarily correctness failures. They are reviewer-verifiability failures.

## Design choice

Do not add a new canonical Stage.

Instead integrate a dedicated reviewer-verifiability obligation into existing manuscript stages:

- **Stage 10:** design derivation/proof architecture and mark bridge equations.
- **Stage 11:** independently reconstruct at least one headline proof/derivation from the manuscript-facing package.
- **Stage 13:** require reviewer-verifiability closure on the integrated manuscript.
- **Stage 14:** verify the exact final package preserved the chain.

The operational checklist is `checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md`.

## Target standard

The target reader is a competent specialist referee, not an undergraduate. The manuscript need not teach standard mathematics/econometrics or print every routine algebraic step.

The required standard is:

> The referee can identify the object being proved/certified, follow non-routine transitions without guessing conceptual bridges, understand any delegated computation/formal result, and see why it implies the manuscript claim.

The compression rule is:

> **Compress routine algebra; preserve proof-critical bridges.**

## Computer-assisted proof rule

Long generated objects may remain outside the main text when they are mechanically reproducible, including:

- long polynomial expansions;
- coefficient tables;
- raw root-isolation traces;
- repetitive case arithmetic;
- proof-assistant kernel traces.

But the manuscript must expose or precisely cross-reference:

1. the mathematical object supplied to the computation;
2. its relevant domain;
3. the exact property certified;
4. the route from manuscript primitives to that object; and
5. the logical implication from the certified property to the theorem/result.

## Relationship to existing gates

- **Theorem certification** asks whether the result is mathematically correct at its stated scope.
- **Formal verification** asks whether the encoded theorem follows from encoded assumptions.
- **Reproducibility** asks whether the computation can be rerun.
- **Exposition streamlining** minimizes reader cost and redundancy.
- **Reviewer verifiability** asks whether a specialist can audit the derivation/proof chain from the manuscript-facing package without reverse-engineering missing bridges.

These are complementary, not substitutes.

## Routing

- presentation/bridge gap only → Stage 13;
- derivation architecture is fundamentally opaque → Stage 10;
- hostile reconstruction reveals substantive mathematical/economic error → earliest affected research/certification stage;
- final formatting breaks an otherwise passed proof chain → Stage 13 from Stage 14.

## Version impact

This refinement changes the quality and coverage of checks inside existing Stages 10/11/13/14. It does not change Stage numbering, canonical verdict semantics, normal routing, rollback architecture, or freeze meaning. Under `docs/VERSIONING_POLICY.md`, it is therefore a minor-version-class change, prospective v2.7.
