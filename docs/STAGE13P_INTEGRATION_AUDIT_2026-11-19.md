# Stage 13P integration and route audit — prospective v4.0 candidate

Date: 2026-11-19 JST. **Status:** feature branch / Draft PR for review; **not merged and not released**. No real economics manuscript has been newly refereed under this Stage merely because these files exist.

## 1. Version and branch integrity

- Stable v3.0 Git ref: `refs/tags/v3.0`, commit `7464e290775741f1435602ad655878a70e1f7b7e`.
- `main` remained at `7464e290775741f1435602ad655878a70e1f7b7e` when checked.
- Feature branch `workflow/stage13p-independent-prose-benchmark-20261119`, Draft PR #35, proposes a **MAJOR** canonical routing change because Stage 13P becomes mandatory.
- No release/tag/main commit, journal submission, scientific-model change, or portfolio configuration mutation was performed.

## 2. Authority and stage contract tests

| Test / evidence | Result |
|---|---|
| Governance `2.26 defines independent two-phase prose review, author accountability and post-GO text invalidation | PASS in feature branch |
| Pipeline order Stage 13 → Stage 13P → Stage 14 | PASS |
| Canonical GO/CONDITIONAL GO/NO-GO retained; no entry to Stage14 after Stage13P CONDITIONAL GO | PASS |
| Phase A independent manuscript-only reading saved before Phase B is shown exemplars | Defined and contract-checked |
| Phase B uses Stage10A fully acquired/read sources, Stage12 refreshed for venue/article type | Defined and contract-checked |
| Source-located STRONG/ADEQUATE/WEAK ratings and no exemplar-prose copying | Defined and contract-checked |
| Five required report artifacts and independent second cold reader | PASS |
| Stage14/15 stale source/PDF change invalidation with precise SHA/hash | PASS |
| Scientific guardrails: quantifiers, caveats, counterexamples, novelty and formal scope preserved | Defined and checked structurally |
| README, versioning, Stage10A/12/13/14/15 and submission checklists linked | PASS |
| Fifteen synthetic positive/negative prose regression cases in `examples/PUBLICATION_PROSE_REVIEW_REGRESSION.md` | Written; actual execution is scenario-dependent |

## 3. Automated structural verification

The repository includes `scripts/verify_stage13p_contract.py` and the dedicated GitHub Actions workflow `.github/workflows/stage13p-contract.yml`.

- [Latest structural CI run #44480429860](https://github.com/ryotamatsuki/research-paper-workflow/actions/runs/44480429860) at feature-branch commit `e37a6305009a7cf8db45dfe18b0b09d548716f4e`: **SUCCESS**; earlier corrected run [#44480266370](https://github.com/ryotamatsuki/research-paper-workflow/actions/runs/44480266370) also **SUCCESS**.
- Static test checks presence/sequence of Stages, mandatory progression, phase ordering, full-text example requirement, all deliverables, source/PDF snapshot, compatibility statement, and synthetic fixture coverage.
- The initial run failed because the static assertion was case-sensitive to an emphasized English sentence, not because a policy conflict was found. The test was corrected and rerun green, with error visible in Actions history.
- The structural CI **does not** read real manuscripts, verify genuine statistical/editorial independence, establish comparator source access, check math, determine writing quality, or replace a human publication decision.

## 4. Scientific/editorial edge cases deliberately preserved

- A legitimate game-timing phrase such as “Stage 1 governments choose policy” is not banned merely because a workflow also has Stages.
- A necessary external theorem or counterexample limitation cannot be polished away as weak prose.
- A Lean or CI pass cannot stand in for author-level or full-game theorem proof.
- A Stage 10A exemplary-paper citation is not proof the Stage 13P reader actually acquired/read a source; Phase B requires real source access.
- A manuscript source change after Stage13P GO invalidates affected prose clearance even when the PDF page count remains identical.
- The reviewer must be transparent when a genuinely blind Phase A is impossible due to context exposure.

## 5. Remaining approval and future release gates

1. Human review of Draft PR changes for route consistency and whether the distinct mandatory gate's cost is justified.
2. Optionally pilot one real manuscript with genuinely ordered Phase A/B and independent second cold read; save real issue closure evidence, not merely regression-fixture names.
3. User authorization to merge the reviewed proposal into `main`, then a separate formal v4.0 release readiness and immutable Git tag/GitHub Release.
4. Existing v3.0 projects may opt in to v4.0 only after the new route is actually adopted; no backdating of Stage13P GO or retrospective historical verdict rewrites.

**Integration judgment:** documentation and structural regression **PASS** for Draft PR review; a complete publication-quality gate is specified but no actual paper has yet passed it. Release status **NOT RELEASED**.
