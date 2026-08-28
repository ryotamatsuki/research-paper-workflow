# Research Decision Log

Historical research label: Retail-service research redesign decisions D-00 through D-08

Canonical workflow mapping: Primarily Stages 1–6, with a Stage 3–5 loop after the first re-kill

Research status: `CONDITIONAL GO`; surviving branch is not theory-frozen

This log records decisions, not a reconstructed success narrative. A branch that failed mathematics, novelty, or economic identification remains failed even if it helped identify the next question.

## Decision D-00 — Do not modernize the old model directly

### Research question
Should the legacy seminar model be polished and modernized into a paper?

### Candidate mechanism
The inherited vertical-channel setup and comparative statics.

### What was changed
Nothing initially; the object was audited before extension.

### What remained frozen
The old paper as historical source material.

### Mathematical result
The inherited model could be analyzed, but correctness of selected formulas was not enough to establish a publishable contribution.

### Literature result
The underlying vertical-relations logic faced mature prior art and the old setup did not establish an independent modern mechanism.

### Strongest referee attack
`This is an old channel model with modern labels rather than a new economic mechanism.`

### Verdict
`NO-GO` for direct modernization.

### Why the branch stopped / continued
The legacy model was dropped; the economic question was retained.

### Allowed next modification
Reformulate the phenomenon from first principles.

### Prohibited rescue
Adding modern terminology or extra variables while retaining the same strategic logic.

Reusable lesson: **preserve the question, not the legacy model.**

---

## Decision D-01 — Retail service infrastructure hypothesis

### Research question
Why might a manufacturer maintain a local dealer when an efficient mass retailer can sell the product?

### Candidate mechanism
Cross-channel service-network externality: local service can increase value for buyers in both channels.

### What was changed
The old parameterization was replaced by conceptually separated margins: channel substitutability `γ`, brand-wide service spillover `β`, and local-specific service value `δ`.

### What remained frozen
One manufacturer, one local dealer, one mass retailer; no dynamics, bargaining, DTC, EC, manufacturer competition, or geography.

### Mathematical result
Not yet a contribution at this decision point; it defined the minimal candidate mechanism.

### Literature result
Known retail-service and vertical-control literatures made a novelty kill necessary before any claim could be retained.

### Strongest referee attack
`Service spillovers are standard; where is the new strategic margin?`

### Verdict
Candidate mechanism only; proceed to minimal-model kill test.

### Why the branch stopped / continued
The question was precise enough to test mathematically.

### Allowed next modification
Solve the smallest static service-spillover model.

### Prohibited rescue
Adding channels, firms, or contracts before learning why the minimal model fails.

---

## Decision D-02 — Static sales-margin-only model fails

### Research question
Can a local retailer survive primarily as service infrastructure if its service is financed from its own product margin?

### Candidate mechanism
Local retailer service effort financed by local retail profit.

### What was changed
A static service-spillover model was solved for `M`, `L`, and `R`.

### What remained frozen
No separate service transfer; no dynamics; no third-party service provider.

### Mathematical result
The Stage 1 service first-order condition yielded

`e* = (ell/k) q_L*`.

Therefore

`q_L → 0  ⇒  e → 0`.

Status: `REPORTED / REQUIRES REPRODUCTION` in a future production repository, despite prior symbolic checks during the research conversation.

### Literature result
Not decisive for this negative result; the mathematics itself killed the desired service-only interpretation under the baseline financing structure.

### Strongest referee attack
`Your own model implies that service disappears with local sales, so the retailer is not service infrastructure in any independent sense.`

### Verdict
Model mathematics: `SUCCESSFUL` as a diagnostic exercise.

Publication baseline: `NO-GO`.

Research question: `CONDITIONAL GO`.

### Why the branch stopped / continued
The negative result identified a precise missing margin: service financing independent of local product sales.

### Allowed next modification
Change only the service-financing/contract margin.

### Prohibited rescue
Adding dynamics, online channels, bargaining, additional retailers, or manufacturer competition at the same time.

---

## Decision D-03 — Static wholesale result is not enough

### Research question
Can a clean wholesale-price distortion from cross-channel service be the contribution even if service-only survival fails?

### Candidate mechanism
Brand-wide service creates asymmetric manufacturer incentives across the local and mass-retail channels.

### What was changed
Nothing; this was a novelty assessment of an existing Stage 1 result.

### What remained frozen
The Stage 1 static model.

### Mathematical result
The prior research conversation reported a clean ordering conceptually summarized as

`w_L < standard benchmark < w_R`.

Status: `REPORTED / REQUIRES REPRODUCTION`.

### Literature result
The result was judged too close to existing retail-service, O2O/service-sharing, asymmetric-retailer, and vertical-control mechanisms. Prior research identified Xu–Fu–Fan (2020), Chai–Duan–Huo (2021), Lei–Li–Cheng (2024), and Zhang–Lim–Ye (2025) as critical threats. Exact bibliographic and proposition-level verification must be repeated in any production-paper repository.

### Strongest referee attack
`The wholesale-price response is already a known strategic implication of service spillovers and asymmetric channel roles.`

### Verdict
`NO-GO` as the main contribution.

### Why the branch stopped / continued
A mathematically clean theorem was not enough to justify the paper.

### Allowed next modification
Continue only on the diagnosed service-infrastructure identity problem.

### Prohibited rescue
Rebranding the wholesale wedge as novelty without a surviving closest-paper distinction.

Reusable lesson: **a clean theorem can still be a research dead end.**

---

## Decision D-04 — Service contract solves feasibility but kills novelty

### Research question
If service financing is separated from product sales, can the local dealer become a genuine service-only node?

### Candidate mechanism
Sales-independent service compensation or service-capacity contracting.

### What was changed
Only the missing service-financing margin.

### What remained frozen
Static environment, same core actors, no installed base, no relationship-specific state.

### Mathematical result
A contract can support a state with `q_L = 0` and `e > 0`.

### Literature result
In the static model, a former dealer that only provides service has no payoff-relevant history distinguishing it from a generic third-party service provider. The branch therefore collapses toward known service-outsourcing/service-channel-choice problems.

### Strongest referee attack
`You created service-only survival by giving the manufacturer a service contract; economically this is just outsourcing.`

### Verdict
Historical `STAGE 2 NO-GO`.

### Why the branch stopped / continued
The contract fixed feasibility but did not solve provider identity or novelty.

### Allowed next modification
Ask why former-dealer history changes current service value.

### Prohibited rescue
Adding more elaborate static transfers, fees, or cost-sharing instruments solely to differentiate the former dealer.

Reusable lesson: **fixing feasibility can destroy novelty.**

---

## Decision D-05 — Installed base alone is insufficient

### Research question
Can durable-good installed base make a former dealer economically distinct after its retail sales disappear?

### Candidate mechanism
Past product sales create an installed base `I_t` that continues to require service.

### What was changed
A dynamic state representing installed durable goods was introduced conceptually.

### What remained frozen
Provider service technology remained identical across former dealer and generic third party.

### Mathematical result
Installed base can explain persistence of service demand after current local sales stop.

### Literature result
Installed-base and aftermarket dynamics are known components, so persistence itself is not enough. More importantly, if `I_t` is a brand-level state independent of provider identity, both providers face the same service opportunity.

### Strongest referee attack
`Installed base explains why someone provides service, not why the former dealer must provide it.`

### Verdict
`Installed Base Only = INSUFFICIENT`.

### Why the branch stopped / continued
The failure identified a different missing state: provider-specific capability inherited from the past relationship.

### Allowed next modification
Add one relationship-specific service-capability state.

### Prohibited rescue
Adding multiple histories, warranties, geography, switching costs, search, or online channels.

Reusable lesson: **a state variable can explain persistence without explaining organizational identity.**

---

## Decision D-06 — Legacy service capital

### Research question
What payoff-relevant state can make a former dealer different from a fresh service contractor?

### Candidate mechanism
`K_t`: manufacturer-specific legacy service capability accumulated through prior dealer activity.

### What was changed
One provider-specific state was allowed after installed base alone failed.

### What remained frozen
The research still excluded extra channels, multiple manufacturers, bargaining, geography, warranties as strategic instruments, and explicit restart costs.

### Mathematical result
With `K_t > 0` for the former dealer and lower/zero inherited capability for a fresh provider, the two service providers can be economically distinct.

### Literature result
Relationship-specific investment and manufacturer-specific dealer capabilities are known components; their mere existence is not the contribution. The potential contribution must come from their interaction with installed base, downstream function exit, and current vertical terms.

### Strongest referee attack
`K_t is an ad hoc advantage parameter inserted only to rescue former-dealer identity.`

### Verdict
Proceed only conditionally.

### Why the branch stopped / continued
Institutional and theoretical motivations make relationship-specific capability plausible, but its accumulation must be microfounded.

### Allowed next modification
Future work may microfound `K_t` through one explicit investment/training mechanism.

### Prohibited rescue
Treating the candidate law `K_{t+1} = (1-δ_K)K_t + φ q_{Lt}` as established fact.

---

## Decision D-07 — Dynamic vertical distortion candidate

### Research question
Can a manufacturer favor the local dealer today because current dealer activity builds service capability valuable tomorrow?

### Candidate mechanism

`q_L1 → K_2 → future service capability → future manufacturer value`.

### What was changed
The relationship-specific state was connected to future value in a two-period conceptual model.

### What remained frozen
No full-paper theory freeze; no additional institutional margins.

### Mathematical result
The prior research conversation reported that, under the candidate accumulation structure, symmetric current product-market primitives can coexist with `q_L1 > q_R1` and corresponding wholesale terms favoring the local dealer. This is the surviving candidate dynamic vertical distortion.

Status: `CONDITIONAL / REQUIRES MICROFOUNDATION AND REPRODUCTION`.

### Literature result
This interaction was judged more promising than the static service results, but no submission-level novelty audit is stored here.

### Strongest referee attack
`The result is generated by assuming that local sales mechanically build future service capital.`

### Verdict
Historical `STAGE 3 CONDITIONAL GO`.

### Why the branch stopped / continued
The result creates a new strategic question rather than merely preserving service, but its primitive is not yet sufficiently founded.

### Allowed next modification
Microfound the accumulation of manufacturer-specific service capability and then re-run novelty and mathematical kill tests.

### Prohibited rescue
Calling the candidate a theorem-level contribution or proceeding directly to full-paper construction.

---

## Decision D-08 — Current blocker

### Research question
Why should product sales quantity itself build manufacturer-specific service capability?

### Candidate mechanism
Candidate law:

`K_{t+1} = (1-δ_K)K_t + φ q_{Lt}`.

### What was changed
Nothing in this case-study PR; this entry records the unresolved blocker.

### What remained frozen
All Stage 3 conclusions remain conditional.

### Mathematical result
The accumulation law is a modeling assumption, not a verified institutional law.

### Literature result
Possible future microfoundations include explicit dealer investment, service training/certification, relationship-specific investment, or financing of future service capability from current retail rents. No option is selected here.

### Strongest referee attack
`Sales volume creates service capital only because the model says so.`

### Verdict
`UNRESOLVED BLOCKER` under a broader `CONDITIONAL GO`.

### Why the branch stopped / continued
The next research step is sharply defined, but the workflow forbids implementing it inside this documentation PR.

### Allowed next modification
Exactly one microfoundation for service-capital accumulation, followed by a new kill test.

### Prohibited rescue
Adding multiple investment channels or unrelated extensions simultaneously.
