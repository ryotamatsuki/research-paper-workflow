# Literature Audit Checklist

Use this checklist for serious prior-art and novelty work. It supplements, but does not weaken, `GOVERNANCE.md` and the canonical pipeline.

## Bibliographic identity

- [ ] Authors verified
- [ ] Title verified
- [ ] Year verified
- [ ] Journal / working-paper series verified
- [ ] Volume / issue / pages verified where applicable
- [ ] DOI or stable identifier verified
- [ ] Publisher / official record checked
- [ ] Working-paper and published versions deduplicated
- [ ] Most recent version identified

## Access and reading depth

- [ ] Abstract read
- [ ] Introduction read for claimed contribution
- [ ] Model / methods section checked
- [ ] Timing / information structure checked
- [ ] Utility / demand / technology checked
- [ ] Contract / institutional structure checked
- [ ] Main propositions/results checked
- [ ] Welfare section checked
- [ ] Robustness/extensions checked where relevant
- [ ] Appendix/proofs checked when they may contain the closest result
- [ ] Evidence limitation recorded if only abstract/snippet access was possible

## Citation-chain audit

- [ ] Seminal predecessor papers identified
- [ ] Backward citations checked
- [ ] Forward citations checked where feasible
- [ ] Same-author neighborhood checked
- [ ] Terminology synonyms searched
- [ ] Adjacent-field terminology searched
- [ ] Recent working papers searched
- [ ] Duplicate/circulating versions reconciled

## Model-level comparison

- [ ] Players compared
- [ ] Objective functions compared player by player
- [ ] Strategy sets / endogenous controls compared
- [ ] Timing and commitment compared
- [ ] Information compared
- [ ] Endogenous variables compared
- [ ] Demand / utility compared
- [ ] Costs / technology compared
- [ ] Contracts / transfers compared
- [ ] Participation / entry / exit / outside options compared
- [ ] Endogenous allocation / sorting / intermediary or facility choice compared
- [ ] Market structure compared
- [ ] Best-response / strategic-feedback network compared
- [ ] Equilibrium concept compared
- [ ] Main theorem compared
- [ ] Welfare mechanism and incidence compared
- [ ] Extensions checked for hidden overlap

## Whole-game absorption audit

For game-theoretic work, do not stop after finding separate precedents for separate ingredients.

- [ ] Is there a **single** prior model that reproduces the economically relevant player set, objectives, strategies, timing, endogenous allocation, and equilibrium feedback after relabeling/normalization/parameter restriction?
- [ ] If not, does an existing theorem nevertheless make the candidate headline result an immediate corollary?
- [ ] If multiple different prior literatures are required to reconstruct the candidate, has this been recorded as component overlap rather than automatic absorption?
- [ ] Has the strategic interaction created only by the full architecture been identified explicitly?
- [ ] Has label stripping been applied to the **whole game**, not only to individual primitives?

`Known component A + known component B + known component C` is not by itself proof that `A+B+C` is an absorbed game. The combination still fails as novelty if it produces no new strategic interaction or theorem.

## Generalization / nesting audit

When the claimed contribution is a generalization, synthesis, or unification:

- [ ] Prior models nested by the candidate are identified explicitly
- [ ] Parameter restrictions/player removals that recover each benchmark are stated
- [ ] Benchmark equilibrium/results are recovered correctly
- [ ] The full model introduces an economically meaningful strategic feedback absent from the benchmarks
- [ ] At least one theorem/threshold/ranking/sign reversal/welfare wedge/conditions result is unavailable in each benchmark alone
- [ ] The contribution is not merely a more general functional form with unchanged economics
- [ ] The paper can explain what question the general model answers that the nested models cannot

## Prior-art classification

For every closest paper, assign one:

- [ ] `EXACT PRIOR ART`
- [ ] `STRUCTURALLY VERY CLOSE`
- [ ] `COMPONENT OVERLAP`
- [ ] `MERELY RELATED`
- [ ] `POTENTIALLY NOVEL`

Record the exact reason for the classification. Do not upgrade to `EXACT PRIOR ART` merely because all components appear somewhere in the literature.

## Novelty statement discipline

- [ ] Contribution claim maps to a specific model/result distinction
- [ ] Contribution type is stated: `NEW MECHANISM / GENERALIZATION / UNIFICATION / NEW RESULT IN KNOWN MODEL / APPLICATION`
- [ ] No claim relies only on a new application label
- [ ] No claim relies only on a different parameter name
- [ ] No claim relies only on failure to find a paper
- [ ] No claim relies only on “nobody combined these ingredients”
- [ ] If the contribution is a generalization, the new strategic/welfare result is stated separately from the broader model
- [ ] Search limitations are stated
- [ ] Closest-paper threat is acknowledged explicitly

> **Rule:** “I did not find it” is not evidence of novelty. Novelty is a model/proposition-level claim that survives serious comparison. Equally, “all ingredients are known separately” is not evidence of absorption; whole-game equivalence or result-level redundancy must be demonstrated.