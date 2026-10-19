# Premature Novelty Claim Regression Fixture

Date established: 2026-10-19. Status: manual, evidence-sensitive regression cases for prospective post-v2.9 MINOR-class refinement. **Not a certification of whether a particular 2014 paper proves the exact mechanism.**

## Incident: procurement-induced obsolescence in circular durables

A manufacturer repurchases used products as production inputs, and can reduce the used owners' outside option after the initial sale. A proposed second-period payoff contains an input-acquisition term `(+e)R - H(e)`, where `e` degrades the used-product market value, `R` is repurchase volume and `H` is degradation cost. A researcher solves the quadratic optimum and finds `e > 0`; adding capitalization of the resale price to initial sales yields a commitment wedge.

### What was initially claimed

The mechanism was described as a new independent economics result, based on mathematical derivation and the novel circular-manufacturing interpretation.

### Critical generic reduction

Rename used goods to inputs, the original owner to an input seller, and resale value to a supplier outside option. The mechanism becomes **a procuring buyer's incentive to lower a seller's outside option**. Time inconsistency in durable goods is a separate known parent family. A successful mathematical calculation establishes neither theorem originality nor independence from these parent classes.

Potential strongest prior sources requiring claim-level comparison include Waldman (1996), Liu & Tan (2014) and Shankar (2024); incomplete full-text access must be labeled `UNRESOLVED`, not represented as a proof of exact duplication or novelty. Do not assert that any one paper contains the identical full game without showing its actual proof and mapping.

## Regression tests and expected decisions

| ID | Input / failure injection | Required response | Forbidden response |
|---|---|---|---|
| PN-01 | Industry-specific "new" mechanism with payoff `eR-H(e)` | Strip labels; test generic monopsony/outside-option parent; record `ABSORBED` if exact mapping proven or `UNRESOLVED` if missing decisive evidence | "Independent new theory" based only on circular-industry nouns |
| PN-02 | Closed-form equilibrium or SymPy numerical PASS | Set `MATHEMATICS` to appropriate verified level and keep `NOVELTY` separate | Promote math success to `EVIDENCE-SCOPED NOVELTY CERTIFIED` |
| PN-03 | Closest relevant theorem exists only behind inaccessible article/appendix | Record source/version/missing proof, classify `UNRESOLVED`; apply existing narrow `CONDITIONAL GO` or `NO-GO` semantics when warranted | Claim "not in literature" because search did not return it |
| PN-04 | Known pieces A and B combined but model may have a new strategic feedback | Test whole-game equivalence and any genuinely new theorem in full architecture | Kill automatically solely because both components are known |
| PN-05 | Stage-2 pre-screen survives, but Stage-6 actual result reduces to standard theorem | Downgrade or kill claim; record false-positive novelty regression with parent-class mapping | Preserve a positive novelty claim due to sunk effort |
| PN-06 | Well-supported Stage-6 theorem-level non-absorption under dated source scope | Permit `EVIDENCE-SCOPED NOVELTY CERTIFIED` only with exact theorem, scope, citations and residual risks | Represent it as proof no paper anywhere has the result |

## Manual execution record

- Executor/date:
- Current workflow SHA:
- Cases exercised: PN-01 through PN-06 (PASS / FAIL / BLOCKED + evidence for each):
- One representative generic parent-model mapping checked:
- Strongest unresolved primary-source blocker:
- Contradictions between governance/pipeline/templates/checklists:
- Scope of check: manual logic/wording; **not** a full source, mathematical or external peer-review certificate.

## Non-goals

This fixture cannot settle novelty in any submitted paper and cannot be substituted for Stage-2/6 original-paper reading, Stage-4A independent mathematics, or Stage-11 hostile regression. Its purpose is to prevent early, overconfident originality announcements and improve correction when a parent theory is found late.
