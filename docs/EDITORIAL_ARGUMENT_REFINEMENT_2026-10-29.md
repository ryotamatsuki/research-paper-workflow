# Editorial argument and independent referee refinement — 29 October 2026

## Motivation and diagnosed defect

A completed technical-paper cycle can pass proof checks, bibliography/static QA, section-existence checks and broad hostile scientific review while still making the economic question, main conditional inference, and its countervailing mechanisms unnecessarily expensive to find. A referee may correctly praise substantial improvements yet omit a **communication-specific falsification attempt**. The old exposition architecture and streamlining requirements remain valuable; the new requirement is to make their *implementation and independent verification evidence-bearing*.

## Change, limited to existing Stages

- **Stage 10:** read published papers for actual *writing moves*, not only near-neighbour novelty. Document Introduction, result-intuition and Discussion structures in an `EDITORIAL_EXEMPLAR_MAP`; use provisional comparators until Stage 12 selects a target.
- **Stage 11:** a distinct editorial-referee attack must cold-read the manuscript without the drafting explanation, reconstruct the economic finding and challenge the argument. “Clear” or “substantially improved” cannot close the gate without excerpt/paragraph evidence, a competing reject paragraph and a repair verdict.
- **Stage 13:** use before/after passages tied to each material objection, verify theorem and negative-result scope, and repeat the cold-reader test after integration. The rewrite should reduce reader cost, not add length for its own sake.
- **Stage 14:** test the final PDF for regression and record artifact provenance. Structural defects reopen Stage 13; architecture defects reopen Stage 10; substantive errors return to their scientific gate.
- **Cross-cutting:** new checklist, referee report template and failure fixtures. Reference papers serve as craft comparators and do not establish novelty, article acceptance or permission to claim stronger empirical/policy effects.

## Compatibility and version policy

This is an **unreleased MINOR-class refinement** of the active v2.9 workflow: it adds evidence requirements and falsification checks *within existing Stages* and retains all Stage numbers, routes, GO / CONDITIONAL GO / NO-GO meaning, mathematical and formal-verification gates, theory freeze, and submission freeze. Do not create or claim a v2.10 tag or GitHub Release solely because this PR exists. Existing project audits are historical and are not retroactively relabeled PASS or FAIL. Active projects must apply the new checks when they enter or repeat the affected stage.

## Risk controls

1. Exemplar count is a practical target, not a fake-citation quota: log actual access and mark unverified evidence. A non-standard article type may validly omit policy Discussion with recorded reason.
2. Stage 10 is field-calibrated; Stage 12 selects and validates the actual target, preventing premature journal lock-in or prestige-driven theory changes.
3. Separate editorial and scientific attacks, but retain their integration: any proposed prose unsupported by the frozen proof/evidence triggers scientific rollback.
4. No superficial style or page-length proxy substitutes for economic meaning. The cold-reader test is a reproducible critique procedure, not a numerical journal-quality score.
5. An AI “editorial referee” is not an external human referee; authorship, verification and independent-attack limits remain governed by AI provenance policies.

## Acceptance tests

Read `examples/EDITORIAL_ARGUMENT_REGRESSION.md` and confirm the expected routes for the six cases. Validate that the canonical pipeline, Stage 10/11/13/14 templates, the three existing QA checklists and README reference the new checklist and do not contradict the frozen theory / Stage-12 journal selection rule. Check added Markdown links against tracked paths and verify diff scope is limited to workflow documentation; no project/manuscript files or research data are changed.
