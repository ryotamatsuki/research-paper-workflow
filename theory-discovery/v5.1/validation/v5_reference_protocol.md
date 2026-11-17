# TDF v5.0 — Loop Protocol (RC1)

## 1. Scope and invariant
Question discovery remains distinct from formal model construction. Use canonical Stage 2's literature standards at hypothesis level; do not assert theorem-level equivalence before a theorem exists. Preserve v4's creative question selection and L2 pattern catalog. The formal pipeline and author selection remain authoritative. A stopped project requires fresh author-approved intake before a pivot enters Stage 0.

Four separate axes: `question` (clear/unclear), `mathematics` (HYPOTHESIS/COMPUTATION-ONLY/MATHEMATICALLY VERIFIED within exact scope), `absorption` (ABSORBED/APPARENTLY DISTINCT/UNRESOLVED), `novelty` (UNSCREENED/PRE-SCREEN SURVIVED/UNRESOLVED/ABSORBED). TDF cannot award evidence-scoped novelty certification. A positive prescreen is permission to propose, not a formal Stage verdict.

## 2. Bounded search plan
Default per run: up to 3 discovery rounds, 12 distinct candidate versions (including successors), 6 deep-screened candidate versions, 60 actual search requests (individual query/index operations, not tool batches), 30 primary-document inspection attempts. Reserve at least one discovery round and 12 requests for killed-candidate recycling until either a candidate clears the gate or no justified pivot exists. Optional time/token cap must be stated if known; never fabricate elapsed time or counts. EPOCH defaults to same budget, explicitly expandable; stricter selection not automatic unlimited work. Counts are caps, never targets or sufficient quality criteria. Log counters cumulatively; cap exhaustion yields HOLD_BUDGET for unfinished work. An API/index outage yields HOLD_ACCESS for affected candidates. If no viable candidate or defensible pivot remains, EXHAUSTED_IN_SCOPE. Do not reset counters on resume; explicit budget extension creates a new authorized limit without erasing prior work.

## 3. State machine
| State | Work | Transition |
|---|---|---|
| INTAKE | Explicit theme, evidence, benchmark, scope, budget | FRONTIER_BASELINE + FREE_DISCOVERY |
| FRONTIER_BASELINE | Strongest standard explanations, seminal + current source map, observed contrast | GENERATE |
| FREE_DISCOVERY | Question alternatives without mechanically selecting from prior mechanisms; avoid simulated independence claims | GENERATE |
| GENERATE | Stable candidate ID/version, claim, rivals, fingerprint, discriminating comparison, economic learning | TRIAGE |
| TRIAGE | Structural merge, triviality/known theorem screen, quick targeted search | DEEP_SCREEN / RECYCLE / HOLD |
| DEEP_SCREEN | Search lanes L1–L8, primary source comparisons, gap record, evidence ledger | RED_TEAM / HOLD |
| RED_TEAM | Canonical mapping, strongest counterexample, whole-game and result-level attack | RECYCLE / HOLD / PRESCREEN_SURVIVED |
| RECYCLE | Explain exact failure; derive new contrast from limitation or free discovery; dedup | GENERATE (new version) or EXHAUSTED |
| HOLD | List decisive missing evidence; process other active candidates | resume affected state only with new evidence or explicit budget |
| PRESCREEN_SURVIVED | Complete gate; score economic promise separately; checkpoint | AUTHOR_SELECTION or continue for stronger EPOCH candidates |
| AUTHOR_SELECTION | Author picks explicitly | STAGE0_HANDOFF (not a Stage verdict) |
| STAGE0_HANDOFF | Deliver evidence, killed claims, residual exact target, provenance | canonical workflow starts separately |

Every transition logs from/to, actual reason, evidence IDs, candidate and run counters. On each round process the queue until all active candidates are screened, deliberately held, merged, or within a stronger-survivor search. Preserve competing candidates instead of anchoring on the first idea. Stop with selection when at least one qualifies and frontier opportunities are addressed proportionately; do not mechanically spend remaining budget. A user direction change updates scope; it never rewrites historical status. An unavailable independent AI reviewer is recorded as `SELF_RED_TEAM`, not independent peer review.

Pseudocode:
```
load_or_initialize(run, budget, ledgers)
while authorization_and_budget_allow:
    if viable_queue_empty:
        if no_new_discriminating_contrast: break EXHAUSTED_IN_SCOPE
        generate_from_frontier_and_failure_memory(); round += 1
    for candidate in viable_queue:
        triage_and_deduplicate(candidate)
        if killed: recycle(candidate); continue
        search_and_read(candidate, all_applicable_lanes)
        attack(candidate, most_dangerous_parent, same_question_same_benchmark)
        if absorbed_or_trivial: record_kill_and_recycle(candidate)
        elif missing_material_evidence_or_no_distinction: HOLD(candidate)
        elif prescreen_gate(candidate): mark_survived(candidate)
    if qualifying_survivors and no justified higher_priority_search: break AUTHOR_SELECTION
checkpoint(actual_counts, evidence, queue, state, restart_condition)
```

## 4. Search specification — Stage-2-style prescreen
Use multiple accessible scholarly discovery routes (e.g. Crossref/OpenAlex/RePEc/Semantic Scholar/Google Scholar/publisher or institutional repositories), not invented index access. If only general web exists, explicitly record how each lane was implemented and its limitations. Prefer primary papers to AI summaries. Search at least two genuinely distinct discovery routes for serious threats, including one scholarly index/repository or an explicit documented access limitation; a missing decisive route blocks if material. Deduplicate DOI/version; check newer versions, appendices, working papers. Search in applicable languages.

| Lane | What to search and preserve |
|---|---|
| L1 INSTITUTION | Exact real-world terms,制度, policy documents, sector + outcome; for conceptual theme, search motivating phenomenon and mark institutional search NA with reason |
| L2 STRUCTURE | Anonymous actors, choice, information, timing, payoff, constraints, feedback, outcome; e.g. not `startup subsidy`, but `team reward absence loss substitutability investment` |
| L3 CLAIM | The predicted sign/ranking/impossibility, alternative vocabulary (including opposite result), potential direct corollary |
| L4 PARENT | Generic theorem/model families in standard economics; theorem/assumptions/results keywords, closest paper references |
| L5 ADJACENT | Other fields with same structure (e.g. computer science, accounting, operations, political economy); preserve translation boundaries |
| L6 BACKWARD | References of decisive papers, original theorem/source, predecessor and variants |
| L7 FORWARD/AUTHOR | Citing studies, later same-author work, version history; actual citation-index results distinguished from title-search proxy |
| L8 FRONTIER | Last 5 years and current year-to-cutoff; recent preprints and working papers (RePEc/SSRN/NBER/arXiv/institutional repositories as applicable), journal version check |

Each lane: query, source/index, date, result IDs, inspection outcome, material coverage gap. A result count is not evidence of completeness. `NA` requires reason; L2/L3/L4/L5/L6/L7/L8 are mandatory for a deep survivor (if no identifiable cite target, hold or explain why evidence rules can nevertheless be met; don't mark an unavailable index completed). Only meaningful searches count. Stop expanding a lane when marginal searches add no material distinct parent threat, supported by logged query families; do not infer global priority. Review recent threats even if classics look sufficient. For triage rejection a supported single exact absorption may suffice; no need to spend all lanes to kill a claim.

## 5. Evidence and absorption
Record source ID, title/authors/date/venue/DOI or stable URL, version, source type, exact section/page/theorem, evidence depth (`FULL_MODEL_PROOF`, `MODEL_RESULT`, `ABSTRACT_ONLY`, `AUTHOR_SUMMARY`, `METADATA`, `UNAVAILABLE`), and verified-as-of date. `FULL_MODEL_PROOF` requires actual reading of relevant full model and proof, including material appendices; snippets cannot qualify. Record source access errors, alternative attempts, and PDF visual-check status where applicable. No invented links, dates or claims.

For each decisive source, inspect intro/positioning; assumptions/model; objective, choices and timing; results/proof scope; welfare benchmark; conclusion/extensions. Compare candidate and source via fingerprint: players/roles; objectives; controls; feasible set; information; timing/commitment; technology/state transition; strategic response; equilibrium/solution; target result and welfare/accounting. Unknown fields stay unknown. Attempt a concrete relabel, parameter restriction, normalization, elimination, nested recovery, or immediate-corollary derivation. Record the mapping and where it succeeds/fails; identical mechanisms do not establish identical full games. For multiple sources, identify whether the proposed joint interaction leads to a distinct falsifiable consequence. Do not add ingredients during absorption to engineer distance.

Kill rules: exact prior claim/direct corollary; definitional truth; only labels or numerical examples; no distinguishable consequence. Mark `ABSORBED` only with adequate evidence and scope; if no economic distinction yet but a source's full model is missing, `HOLD` or `REJECT_NO_RESIDUAL` (not proven prior art). Partial overlap is not automatic NO-GO: preserve legitimate generalizations or corrections. If a source is decisive and not accessible or material proof missing, HOLD. Red-team record must include strongest objection and what would falsify it. For a proof target, B0/B1 retain feasible set/accounting except the declared margin; test removal, limits, and strongest cheap counterexample. Simple consistency checks only; do not move to full model or imply Stage 4 proof.

Gap extraction after deep screen: label `AUTHOR-STATED` only with exact location, `AUDITOR-INFERRED`, or `CROSS-PAPER`; check later papers and parent theory for each lead. Status `RESOLVED / PARTIALLY RESOLVED / OPEN WITH EVIDENCE / UNRESOLVED`; no search-hit absence as openness. A useful source limit must change an economist's prediction/decision, not merely add a parameter.

## 6. Prescreen gate (all necessary conditions)
A candidate may be `PRESCREEN_SURVIVED` only when every applicable condition is evidenced:
A. Precise question, exact candidate result, economic learning, observed or explicitly hypothetical contrast, meaningful competing explanation and falsifier.
B. L1–L8 logged with justified NA only when truly irrelevant; required primary source, version/currentness, backwards/forwards/author routes documented; material source/coverage blockers closed. Relevant model/proof depth adequate for every decisive threat.
C. Strongest source and application-neutral parent class mapped; an actual result- or architecture-level distinction survives, not only keyword absence. Removal/cheap counterfactual test attempted, and central economic result is not a tautology.
D. Red-team attempted (record independence and limitations); all material fatal objections resolved within hypothesis-level scope. Question still economically meaningful, minimal next audit feasible; no claim of certified novelty or math.
E. EPOCH only: meaningful conceptual reframe or unification; two or more structurally distinct settings showing why new distinction matters, nontrivial prediction that differs from strongest known theory, no trivial relabel. `EPOCH` remains ambition, not Nobel prediction. If only STANDARD-quality candidate, preserve it as `STANDARD_POSSIBLE`, not selected under EPOCH.
No score, numeric example, or large bibliography can override conditions. Author must select before Stage 0. Complete candidate status is `PRE-SCREEN SURVIVED` only; Stage 2 independently re-audits. Formal Stage 0 may be initiated independently by the author, but TDF does not recommend a blocked candidate as screened.

## 7. Recycle protocol (mandatory after kill)
1. Record killed claim, strongest evidence, exact absorption mapping or missing distinction, scope, and failure source (e.g. missing synonym, missed parent, abstract-only comparison, new paper, tautology).
2. Ask what the best existing explanation already covers; extract only source-supported limits and mark origin. If no genuine puzzle remains, close this branch.
3. Use an orthogonal discovery operation: a different actor's decision, a genuinely different comparison, a distinct axiom or institutional feasibility issue; OR free exploration of another observation. Record why the new counterfactual differs, how it can fail and what new learning it yields. No rescue by relabel/parameter piling.
4. Dedup against killed bank by fingerprint + target result + falsifier. If same, merge and keep killed status. If changed, create child ID, connect ancestor, label which elements changed and identify new search lanes. Retest all still-relevant prior threats plus new threats; inherited literature evidence may be reused with version/access/time checks. Reopen same claim only with identified new evidence that challenges kill. HOLD rather than claiming novelty if decisive evidence is missing.
5. On exhausted budget, return checkpoint (state, IDs, evidence, pending tasks, cumulative counters, exact reopening conditions), not a new confident idea. Keep project-specific logs private.

## 8. Validation / adoption
Before replacing v4, run private retrospective failure replay and prospective blinded retrieval tests without giving the decisive paper names, plus positive/partial-overlap, inaccessible-source, duplicate, no-candidate and interrupted-resume cases. Record search budget, human adjudication of decisive hits, false passes, false kills, handoff rate, downstream Stage 2 kill/rollback and actual time/effort. Compare with v4 on identical themes, independent fresh runs and comparable budgets; evaluate recall of seeded/retrospectively established threats without claiming true global recall. A deterministic gate test is not an empirical comparison. Explicit author adoption required; no silent rewrite of v4 or canonical stages.
