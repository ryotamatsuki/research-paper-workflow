# Stage 03 — Dynamic Legacy Service

Historical research label: Stage 3 — Installed base / legacy service-capital branch

Canonical workflow mapping: Stage 3 mechanism search → Stage 4 minimal-model logic → Stage 5 hardening; still before canonical Stage 7.5

Research status: `CONDITIONAL GO`

## Candidate 1 — Installed base

The first dynamic state was the manufacturer's durable-good installed base:

`I_{t+1} = (1-ρ) I_t + q_{Lt} + q_{Rt}`.

This creates a clean reason for service demand to persist after current local retail sales disappear. Even if `q_{Lt}=0`, previously sold durable goods can remain in use and continue to require repair, maintenance, troubleshooting, or related service.

### Result

Installed base explains **service-demand persistence**.

It does not by itself explain **provider identity**. If a former dealer and a fresh third-party provider have the same service technology and access to the same brand-level installed base, `I_t` gives both the same opportunity.

Verdict for installed-base-only branch: `INSUFFICIENT`.

Evidence status: conceptual result `VERIFIED` as a logical implication of provider-independent `I_t`; publication-level novelty implications require re-audit.

## Candidate 2 — Legacy service capital

After installed base failed to distinguish providers, the project allowed one additional state:

`K_t = manufacturer-specific legacy service capability`.

Possible institutional interpretations include manufacturer-specific training, diagnostic know-how, certification, special tools, repair capability, and customer/install-base knowledge. These are collected into one abstract state rather than treated as separate mechanisms.

A candidate accumulation law used in the historical analysis was

`K_{t+1} = (1-δ_K) K_t + φ q_{Lt}`.

This equation is not treated as an established institutional fact. Its microfoundation is the main current blocker.

## Former dealer versus fresh third party

With `K_t > 0` inherited by the former dealer and lower or zero inherited capability for a fresh provider, former-dealer identity becomes payoff-relevant. The former dealer can have lower effective service cost or higher service effectiveness for the manufacturer's installed base.

This is the first branch in the case where

`former dealer ≠ anonymous service contractor`

has economic content rather than a label.

## Functional persistence candidate

The historical analysis identified a candidate region in which the local dealer's selling function exits while the service function remains. The conceptual distinction is:

- current retail viability depends on current product-market conditions and selling-function costs;
- service-network viability depends on installed base, inherited service capability, and service-network costs.

Because these margins depend on different state variables, retail exit need not coincide with service exit.

Evidence status: `REPORTED / REQUIRES REPRODUCTION` for exact thresholds; the conceptual separation is retained.

## Dynamic vertical distortion candidate

The highest-value surviving mechanism was not merely service persistence. It was the possibility that the manufacturer favors the local dealer **today** because current dealer activity contributes to service capability valuable **tomorrow**.

Conceptual chain:

```text
q_L1
  ↓
K_2
  ↓
future manufacturer-specific service capability
  ↓
future manufacturer value from the installed base
```

Under the candidate law, the prior research conversation reported that even when current product-market primitives are symmetric, the manufacturer can induce

`q_L1 > q_R1`

and corresponding wholesale terms that favor the local dealer.

Interpretation: **current dealer protection for future service capability**.

Evidence status: `CONDITIONAL / REQUIRES MICROFOUNDATION AND REPRODUCTION`.

## Welfare candidate

The historical analysis also reported a possible wedge in which the manufacturer exits a legacy service network earlier than would be socially optimal because some installed-base service value accrues to consumers rather than the manufacturer.

Evidence status: `REPORTED / REQUIRES REPRODUCTION`; not a frozen theorem.

## History dependence versus hysteresis

The state variables `I_t` and `K_t` can make current organization depend on past sales and relationship history. That is **history dependence / state dependence**.

The case does **not** claim hysteresis. No canonical result with distinct entry/exit thresholds, irreversibility, or restart costs has been established.

## Verdict

`STAGE 3 CONDITIONAL GO`.

The surviving mechanism is promising because it links current vertical terms to future relationship-specific service capability. It is not yet a successful paper.

## Main blocker

Why should current local sales quantity mechanically build service capital?

The candidate law

`K_{t+1} = (1-δ_K) K_t + φ q_{Lt}`

requires a defensible microfoundation.

Possible future candidates include explicit dealer investment, training/certification, relationship-specific investment, or a financing channel from current retail rents to future service capability. None is selected or implemented in this case-study PR.

## Next-stage contract

If this research branch is resumed, change exactly one margin: microfound the accumulation of `K_t`. Then re-run mathematical and novelty kill tests before any full-paper investment.
