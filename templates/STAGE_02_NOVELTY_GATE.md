# Stage 2 — Literature Frontier / Novelty Kill Gate

> Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template.

## 0. Role

Act as a skeptical field referee and literature-audit lead. Your task is to kill false novelty claims before model expansion begins.

## 1. Project context

- Topic: `[RESEARCH_TOPIC]`
- Core question: `[CORE_RESEARCH_QUESTION]`
- Canonical audited model/result: `[CANONICAL_MODEL]`
- Candidate mechanism: `[CORE_MECHANISM]`
- Known close papers: `[CLOSEST_PAPERS]`
- Target journal family: `[TARGET_JOURNAL]`
- Current date: `[CURRENT_DATE]`

## 2. Stage objective

Determine whether the surviving setup, mechanism, theorem, threshold, or welfare result is already known, structurally contained in prior work, or still potentially novel.

## 3. Canonical inputs

Treat Stage 1 outputs as frozen. Do not modify assumptions to manufacture distance from the literature.

## 4. Allowed changes

You may refine terminology, identify better comparison papers, split contribution claims, or recommend a pivot. You may not add new model ingredients during this gate.

## 5. Prohibited changes

- no novelty inference from search failure;
- no abstract-only judgment for closest papers when fuller text is reasonably accessible;
- no counting an application label as theory novelty;
- no duplicate counting of working-paper and published versions;
- no ignoring an appendix or extension that contains the same result.

## 6. Mandatory tasks

Search and map:

1. seminal literature;
2. classic mechanism papers;
3. modern literature;
4. 2020–current frontier;
5. current working papers where material.

For the closest papers, inspect as far as feasible:

- players and timing;
- utility/demand;
- costs and contracts;
- information;
- endogenous variables;
- equilibrium concept;
- participation/entry/exit;
- main propositions;
- welfare;
- robustness/extensions/appendices.

Perform targeted backward and forward citation searches, same-author neighborhood searches, synonym searches, and working-paper/published-version deduplication.

Classify each overlap as:

- `EXACT PRIOR ART`
- `STRUCTURALLY VERY CLOSE`
- `COMPONENT OVERLAP`
- `MERELY RELATED`
- `POTENTIALLY NOVEL`

Use `checklists/LITERATURE_AUDIT_CHECKLIST.md` and `checklists/NOVELTY_KILL_CHECKLIST.md`.

## 7. Evidence requirements

Verify bibliographic metadata. Prefer publisher/DOI pages and full papers or author versions for model-level comparison. State explicitly when only abstract-level evidence is available.

## 8. Verification protocol

For each proposed contribution, map the exact claim to at least the closest relevant paper. Re-run searches using theorem language, economic mechanism language, and alternative terminology. Keep a citation trail sufficient for independent reproduction.

## 9. Kill tests

Kill or downgrade a contribution if:

- the same proposition already exists;
- only parameter names or institutional labels differ;
- the same endogenous margin and strategic trade-off are already present;
- the novelty is merely a combination of known components with no new interaction;
- a fixed cost mechanically creates the only threshold;
- the claimed new mechanism appears in an appendix or extension of a close paper;
- the project predates a newer working paper that now occupies the contribution.

## 10. Success criteria

At least one model/proposition-level distinction must survive a serious closest-paper comparison. “No exact title match” is insufficient.

## 11. Failure criteria

Return `NO-GO` if the main contribution is exact prior art or structurally so close that only cosmetic changes distinguish it.

## 12. Required final output

1. Executive novelty verdict
2. Search strategy and coverage
3. Literature-family map
4. Closest-paper matrix
5. Backward/forward citation findings
6. Contribution-by-contribution classification
7. Killed claims
8. Surviving claim(s)
9. Strongest prior-art threat
10. Exact implication for mechanism search

## 13. Final verdict

Choose one:

- `GO TO MECHANISM SEARCH`
- `CONDITIONAL GO` — identify the precise novelty uncertainty
- `NO-GO`

## 14. Next-stage contract

Stage 3 may generate alternative mechanisms only around the surviving research question. It may not revive killed claims by relabeling them.