# Equilibrium Multiplicity & Evidence-Bearing Certification Refinement — 2026-09-09

Status: workflow regression lesson and refinement rationale

## 1. Why this refinement was added

The existing v2.1 architecture already requires global-deviation checks, existence/uniqueness analysis, theorem quantifier discipline, equilibrium-continuation safety, Stage-7.5A scope certification, and Stage-11 regression attacks.

The regression exposed here is therefore not primarily a missing principle. It is an execution/credentialing failure: a project can perform one valid equilibrium check, report `PASS`, and still fail to show that it executed the distinct attack required by the stronger claim.

The refinement makes that distinction operational and evidence-bearing.

## 2. Regression pattern

A recurring failure pattern is:

1. a preferred strategy profile is proposed as an equilibrium;
2. the reviewer verifies that no player has a profitable unilateral deviation from that profile;
3. the project treats this as if the equilibrium had been characterized or shown unique;
4. another strategy profile, often involving a boundary, tie, zero-demand, zero-output, or zero-profit action, also satisfies equilibrium conditions;
5. the second profile changes another player's best response, allocation, price/action, or welfare conclusion even though the player taking the payoff-equivalent action is personally indifferent.

The key logical point is that `the proposed profile is an equilibrium` and `the equilibrium is unique / completely characterized` are different propositions and require different attacks. A no-profitable-deviation check addresses the first proposition. It does not by itself search for a second equilibrium.

## 3. Indifference is an audit trigger

Payoff indifference, zero demand, zero output, zero profit, participation ties, bidding ties, matching ties, and contract-choice ties now trigger an explicit equilibrium-set attack. The indifferent action must be varied and other players' best responses recomputed. Unchanged own payoff is not evidence that the action is strategically irrelevant.

## 4. Selection/refinement regression lesson

When a newly discovered equilibrium is inconvenient, an added refinement must be audited symmetrically:

- whether it belongs to the original model or is newly imposed;
- which equilibria it removes;
- whether it also removes the preferred candidate;
- what remains true without it; and
- what becomes refinement-conditional.

A concrete lesson from the motivating correction work is that weak-dominance reasoning cannot be invoked selectively to eliminate an inconvenient payoff-equivalent equilibrium if the same reasoning would also eliminate a marginal-cost or otherwise necessary preferred action.

## 5. Welfare regression lesson

For every welfare comparison, distinguish one selected equilibrium, all relevant equilibria, a refinement-defined subset, and an equilibrium-invariant allocation/welfare object. If separate markets, regions, subgames, or stages each admit multiplicity, their selections may be independently variable unless the model supplies a coordination/selection device.

## 6. Evidence-bearing PASS rule

Every material PASS must now be tied to:

`claim -> adversarial attack actually performed -> proof/counterexample/code artifact -> surviving limitation`.

The words `checked`, `verified`, `reviewed`, or a green CI job are not enough when the certificate does not identify what attack was executed.

## 7. Paper-specific routes

Correction papers, replication projects, fast-track notes, and other bespoke workflows may use route labels such as `C0–C6` instead of canonical Stage numbers. Those routes inherit the canonical certification obligations for the claims they make and must preserve equivalent evidence artifacts using `checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`.

Renaming the route does not waive candidate-deviation audit, alternative-equilibrium/multiplicity audit when required by claim scope, indifference-trigger audit, refinement provenance/symmetry audit, welfare-selection robustness, theorem quantifier/scope certification, or evidence-linked PASS.

## 8. Version impact

This refinement does not add, remove, renumber, or reroute canonical Stages. It strengthens checks and evidence obligations inside the existing v2 architecture. Under `docs/VERSIONING_POLICY.md`, that is a backward-compatible minor-version class change.

The stable v2.1 tag remains immutable. This document records the post-v2.1 refinement rationale pending normal integration/release governance.

## 9. Files implementing the refinement

- `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`
- `templates/STAGE_04A_MATH_RED_TEAM.md`
- `templates/STAGE_07_WELFARE_GENERALITY.md`
- `templates/STAGE_075A_GENERALITY_QUANTIFIER_RED_TEAM.md`
- `templates/STAGE_11_REFEREE_GATE.md`
- `checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md`

The intended regression guarantee is:

> A strong equilibrium, welfare, or scope claim cannot receive PASS merely because a related but logically weaker check was performed. The certificate must show the specific adversarial attack and evidence appropriate to the exact claim.
