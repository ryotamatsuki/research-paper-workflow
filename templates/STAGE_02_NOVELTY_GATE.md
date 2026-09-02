# Stage 2 — Literature Frontier / Novelty Kill Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a skeptical field referee and literature-audit lead. Your task is to kill false novelty claims before model expansion begins without falsely killing strategically distinct generalizations merely because their components are individually familiar.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Core question: `[CORE_RESEARCH_QUESTION]`
- Canonical audited model/result: `[CANONICAL_MODEL]`
- Candidate mechanism: `[CORE_MECHANISM]`
- Known close papers: `[CLOSEST_PAPERS]`
- Target journal family: `[TARGET_JOURNAL]`
- Current date: `[CURRENT_DATE]`

## 2. Stage objective

Determine whether the surviving setup, strategic architecture, mechanism, theorem, threshold, welfare result, or proposed generalization is already known, structurally contained in prior work, an immediate corollary of known work, or still potentially novel.

The novelty unit must be evaluated at **two levels**:

1. component level — which primitives, players, margins, and results are individually known;
2. whole-game/result level — whether the economically relevant player-objective-strategy-timing-allocation-feedback structure and headline results are already solved.

## 3. Canonical inputs

Treat Stage 1 outputs as frozen. Do not modify assumptions to manufacture distance from the literature.

## 4. Allowed changes

You may refine terminology, identify better comparison papers, split contribution claims, classify the intended contribution as a new mechanism/generalization/unification/new result in a known model, or recommend a pivot. You may not add new model ingredients during this gate.

## 5. Prohibited changes

- no novelty inference from search failure;
- no abstract-only judgment for closest papers when fuller text is reasonably accessible;
- no counting an application label as theory novelty;
- no duplicate counting of working-paper and published versions;
- no ignoring an appendix or extension that contains the same result;
- no declaring absorption solely because every component appears somewhere in different literatures;
- no claiming novelty solely because nobody combined the exact ingredients.

## 6. Mandatory tasks

Search and map:

1. seminal literature;
2. classic mechanism papers;
3. modern literature;
4. 2020–current frontier;
5. current working papers where material.

For the closest papers, inspect as far as feasible:

- players and their objective functions;
- strategy sets/endogenous controls;
- timing and commitment;
- utility/demand;
- costs and contracts;
- information;
- endogenous variables;
- equilibrium concept;
- participation/entry/exit/outside options;
- endogenous allocation/sorting/intermediary or facility choice;
- best-response/strategic-feedback network;
- main propositions;
- welfare and incidence;
- robustness/extensions/appendices.

Perform targeted backward and forward citation searches, same-author neighborhood searches, synonym searches, adjacent-field searches, and working-paper/published-version deduplication.

### Whole-game absorption test

For a strategic/game-theoretic candidate, explicitly answer:

- Is there one prior model that reproduces the economically relevant full game after direct relabeling, normalization, parameter restriction, or deletion of nonessential notation?
- If no single prior model does so, is the proposed headline result nonetheless an immediate corollary of an existing theorem?
- If reconstructing the candidate requires combining different prior models with different players/objectives/strategies, what genuinely new strategic feedback, if any, appears only in the full architecture?

Do not infer `EXACT PRIOR ART` from component overlap alone.

### Generalization / unification test

If the candidate deliberately extends or unifies existing models:

- identify each important nested benchmark;
- state the parameter restriction/player or strategy removal that recovers it;
- identify the strategic interaction endogenous only in the full model;
- state at least one candidate theorem, threshold, ranking, sign reversal, equilibrium region, welfare wedge, or conditions-for-effectiveness result unavailable in each benchmark alone.

A meaningful generalization can survive Stage 2 even when all ingredients are known separately. A mere longer model with no new interaction/result cannot.

Classify each closest-paper relationship as:

- `EXACT PRIOR ART`
- `STRUCTURALLY VERY CLOSE`
- `COMPONENT OVERLAP`
- `MERELY RELATED`
- `POTENTIALLY NOVEL`

Use `checklists/LITERATURE_AUDIT_CHECKLIST.md` and `checklists/NOVELTY_KILL_CHECKLIST.md`.

## 7. Evidence requirements

Verify bibliographic metadata. Prefer publisher/DOI pages and full papers or author versions for model-level comparison. State explicitly when only abstract-level evidence is available.

Game-level absorption claims require model-level evidence. A list of papers covering separate ingredients is not sufficient evidence that the full game is absorbed.

## 8. Verification protocol

For each proposed contribution, map the exact claim to at least the closest relevant paper. Re-run searches using theorem language, economic mechanism language, game-architecture language, player/objective/strategy combinations, and alternative terminology. Keep a citation trail sufficient for independent reproduction.

If a generalization/unification route is claimed, create a nested-benchmark map showing which prior model is recovered by each restriction and what result remains unique to the full candidate.

## 9. Kill tests

Kill or downgrade a contribution if:

- the same proposition already exists;
- only parameter names or institutional labels differ;
- a single close paper already contains the same economically relevant player/objective/strategy/timing/allocation/feedback structure;
- the same endogenous margin and strategic trade-off are already present and the candidate result is an immediate corollary;
- the novelty is merely a combination of known components with no new strategic interaction or theorem;
- a claimed generalization only broadens a functional form while leaving the economics unchanged;
- a fixed cost mechanically creates the only threshold;
- the claimed new mechanism appears in an appendix or extension of a close paper;
- the project predates a newer working paper that now occupies the contribution.

Do **not** kill solely because all components are separately known if no prior model reproduces the full strategic architecture and the combination plausibly creates a new equilibrium or welfare problem.

## 10. Success criteria

At least one model/proposition-level distinction must survive a serious closest-paper comparison. A qualifying distinction may be:

- a genuinely new mechanism; or
- an economically substantive generalization/unification that nests important prior models and creates a new strategic interaction plus a nontrivial candidate result.

“No exact title match” and “nobody combined these ingredients” are both insufficient.

## 11. Failure criteria

Return `NO-GO` if the main contribution is exact prior art, structurally so close that only cosmetic changes distinguish it, an immediate corollary of known theory, or a combination/generalization with no new strategic or welfare implication.

## 12. Required final output

1. Executive novelty verdict
2. Search strategy and coverage
3. Literature-family map
4. Closest-paper matrix
5. Component-level overlap map
6. Whole-game absorption test
7. Nested-benchmark/generalization map, where applicable
8. Backward/forward citation findings
9. Contribution-by-contribution classification
10. Killed claims
11. Surviving claim(s)
12. Strongest prior-art threat
13. Exact implication for mechanism search

## 13. Final verdict

Choose one canonical stage verdict and route:

- `GO` → `GO TO MECHANISM SEARCH`
- `CONDITIONAL GO` — identify the precise novelty uncertainty
- `NO-GO`

## 14. Next-stage contract

Stage 3 may generate alternative mechanisms or a minimal generalization/unification architecture only around the surviving research question. It may not revive killed claims by relabeling them. If the surviving route is generalization/unification, Stage 3 must preserve and test the nested-benchmark map rather than treating the known components as independent novelty claims.