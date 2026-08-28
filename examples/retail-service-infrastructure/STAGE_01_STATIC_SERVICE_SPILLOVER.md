# Stage 01 — Static Service-Spillover Model

Historical research label: Stage 1 — Minimal static service-spillover model

Canonical workflow mapping: Primarily Stage 4 — Minimal Model Gate, with elements of Stage 1 mathematical audit and Stage 2 novelty assessment

Research status: Mathematics diagnostically successful; publication baseline `NO-GO`; research question `CONDITIONAL GO`

## Model idea

Players:

- manufacturer `M`;
- local dealer `L`;
- mass retailer `R`.

The local dealer chooses costly service effort `e`. Service can affect value across channels, while `L` and `R` compete in the product market.

## Core primitive

Cross-channel service spillover. The model separates brand-wide service effects from local-specific service effects and product-market substitutability.

## Deliberate exclusions

To preserve the minimality gate, the historical baseline excluded:

- DTC;
- EC as a third channel;
- endogenous retailer count `N`;
- bargaining;
- RPM;
- manufacturer competition;
- dynamics;
- installed base;
- third-party service provision.

## Key mathematical negative result

The solved service first-order condition was reported as

`e* = (ell/k) q_L*`.

Therefore,

`q_L → 0  ⇒  e → 0`.

Economic interpretation: when the local dealer finances service only through its own retail margin, loss of the dealer's selling function also destroys its service function. The baseline therefore cannot produce a dealer that survives purely as service infrastructure.

Evidence status: `REPORTED / REQUIRES REPRODUCTION`. The historical research conversation included symbolic verification, but this workflow case does not contain the SymPy scripts or a production reproducibility archive.

## Candidate proposition killed

The desired state

`q_L → 0` with `e > 0`

is impossible under the baseline sales-margin-only financing structure.

This is recorded as a successful negative result, not as a minor defect to be hidden.

## Additional result that did not rescue the branch

The historical analysis also reported a service-induced wholesale-price ordering of the form

`w_L < standard benchmark < w_R`.

Evidence status: `REPORTED / REQUIRES REPRODUCTION`.

The result was mathematically cleaner than the service-survival result but did not survive the novelty screen as a plausible main contribution.

## Novelty problem

Prior research identified substantial overlap with retail-service, service-sharing/O2O, asymmetric-retailer, and vertical-control literatures. The specific papers treated as important threats included Xu–Fu–Fan (2020), Chai–Duan–Huo (2021), Lei–Li–Cheng (2024), and Zhang–Lim–Ye (2025).

Evidence status for these literature comparisons in this repository: `REPORTED / REQUIRES RE-VERIFICATION`. This worked case does not substitute for a production-level closest-paper audit.

## Verdict

```text
Model mathematics: SUCCESSFUL AS DIAGNOSTIC WORK
Publication baseline: NO-GO
Research question: CONDITIONAL GO
```

The distinctions matter. A model can be solved correctly and still fail as a paper.

## Why the next step was permitted

The negative result isolated one missing economic margin: service financing independent of current local product sales.

The only allowed next modification was therefore the service-financing/contract margin.

## Prohibited rescue

The project did not permit simultaneous addition of dynamics, online channels, bargaining, more retailers, geography, or manufacturer competition.
