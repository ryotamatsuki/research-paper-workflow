# Editorial Argument Quality Checklist

Use this **in addition to**, not instead of, `EXPOSITION_STREAMLINING_CHECKLIST.md`, `REVIEWER_VERIFIABILITY_CHECKLIST.md`, and `REFEREE_ATTACK_CHECKLIST.md`. Its purpose is to detect the case in which all required components are present and all claims are correct, yet the central economic finding is hard for a specialist reader to identify. An article can be concise, accurate, and still poorly argued.

## Lifecycle and bounded evidence

- **Stage 10 — exemplar and architecture:** create `EDITORIAL_EXEMPLAR_MAP.md` from real accessible published papers, plus a provisional opening, headline-result intuition and discussion structure. Stage 10 may not presume the final Stage-12 journal; use an explicitly provisional field/article-type comparator where the target is unsettled.
- **Stage 11 — independent editorial referee:** create `EDITORIAL_REFEREE_REPORT.md` using a reviewer/critical pass separate from the drafting pass. Test the **actual manuscript**, not just the architecture or the author summary. An independent AI critique is an independent *task/attack path*, not human peer review.
- **Stage 12 — journal calibration:** when the actual target is selected, revisit relevant comparators; a comparator is evidence of writing practice, not automatic evidence that this paper meets the target's novelty, generality, or acceptance threshold.
- **Stage 13 — editorial revision and regression:** create `EDITORIAL_REVISION_AUDIT.md` with before/after passages, the exact referee criticism each addresses, and proof/claim-scope integrity evidence. Re-run the hostile reader test on the revised manuscript.
- **Stage 14 — final-package check:** verify all above artifacts exist and still correspond to the final PDF; do not perform a first substantive editorial rewrite in the submission QA stage.

Use `PASS`, `REVISE`, `UNRESOLVED`, or `NOT APPLICABLE — REASON` for each material item. A vague “clear,” “substantially improved,” “contains an introduction,” or checklist tick without manuscript evidence is not a PASS.

## A. Real-paper writing exemplar gate (Stage 10; refreshed Stage 12/13)

- [ ] Record **2–3 real, relevant, accessible published papers** where feasible; identify author, title, venue, year, DOI/permanent URL, inspected section, and actual access/read depth.
- [ ] Use distinct exemplars for **problem-first Introduction**, **post-theorem economic intuition**, and **Discussion/policy interpretation** where available. One paper can fill multiple roles when justified; no fixed count if a meaningful comparator is unavailable.
- [ ] Compare the **rhetorical/argument structure**, not only mathematical model, publication rank, topic, or reference count.
- [ ] For each role record **actual observed sequencing**: economic problem → missing inference → research question → central result; expected sign → countervailing channels → condition; economic lesson → practical mapping → unresolved limits, **only when those steps are actually in the paper**.
- [ ] State the precise move to adopt and why it fits the article's certified contribution; state what **must not** be copied (empirical causal strength, welfare claim, policy recommendation, result generality, institution-specific evidence).
- [ ] Do not invent inaccessible full text or exact section observations. Log `UNVERIFIED` and choose an accessible substitute. Exemplar selection never substitutes for near-neighbour theorem-absorption review.
- [ ] Do not copy source prose or extended passages; extract original writing principles and produce new text.

Suggested evidence table:

| Manuscript location | Source / section / inspected evidence | Observed writing move | Proposed adaptation | Claim/evidence guardrail | Status |
| --- | --- | --- | --- | --- | --- |

## B. Cold-reader argument test (Stages 10/11/13)

Give a critical reader only the manuscript in its ordinary reading order; do not provide the author's abstract of intended contribution, past conversation, proof audit, or the editorial exemplar map during the first pass. Record exact passages/pages supporting the responses:

1. **Opening:** after the opening one or two paragraphs, can a specialist state the **economic puzzle**, affected decision-maker, and why the answer is not obvious? The two-paragraph window is a diagnostic, **not** a universal word/page limit.
2. **Distinctive finding:** can the reader state the main result **in plain economic language**, with the sign/ranking/object it concerns, **without translating displayed mathematics**?
3. **Novelty:** can the reader distinguish (a) inherited mechanism, (b) actual new conditional inference, and (c) unsupported stronger result? “We combine X and Y” alone is insufficient when the paper claims a distinct proposition.
4. **Scope:** can the reader state the binding restrictions and separate conditional derivative/level results, numerical examples, full-game equilibrium claims, welfare benchmarks and causal evidence as appropriate?
5. **Location/time:** are these answers discoverable early enough for the chosen article type, without requiring unnecessary symbols or a long literature review?
6. **Disagreement:** write the strongest plausible **editorial rejection paragraph about communication**, separate from novelty/importance. If the critique can identify a named unresolved exposition defect, a generic “substantially clearer” does not close it.

Record the reader's first-pass paraphrase **before** seeing author-provided explanations, then compare with the author's verified claim register. A materially wrong paraphrase is evidence of a possible exposition failure; test against the actual passage, not against the reader's infallibility.

## C. Immediate post-result economic-intuition test (Stages 10/11/13)

- [ ] Select the single headline proposition/result, or one per substantively distinct mechanism when necessary.
- [ ] Identify the **baseline/naive prediction**, the **countervailing forces**, the **endogenous adjustment**, and **which primitive restrictions determine dominance**.
- [ ] Explain why an inequality or sign condition has an economic role, not only what the algebra says.
- [ ] Separate change from level, local from aggregate, conditional from full equilibrium, and analytic theorem from numerical witness where applicable.
- [ ] Show the causal/economic reasoning in original prose near the proposition, not scattered solely through captions, supplementary proofs or Discussion.
- [ ] Preserve proof-critical bridge equations; do **not** replace the mathematics with a verbal explanation or incorrectly apply an envelope theorem.

## D. Discussion as economic interpretation, not institutional catalog

- [ ] Start with the **economic inference that changes a decision or comparison**; distinguish it from the familiar instruction to include every cost and benefit.
- [ ] Identify decision-relevant observables/counterfactuals and the welfare/benchmark object the paper actually assesses; label unknown estimation needs.
- [ ] Use institutional or empirical cases as illustrations **unless** causal/evaluative identification has actually been supplied.
- [ ] State the main unmodeled instruments, external-validity boundaries, negative robustness tests, and interpretation limits without making them a rhetorical footnote.
- [ ] Do not infer a particular policy instrument, causal effect, equilibrium switch, or large magnitude from a conditional sign or a narrow parameter certificate.
- [ ] Avoid simply repeating the Results section or listing institutions before explaining what the model teaches.

## E. Evidence-bearing verdicts and repair routing

A material `PASS` requires: **file + page/paragraph + cold-reader paraphrase + comparison to the verified claim + explicit challenge attempted + result**. An exemplar comparison alone, model correctness, a PDF clean build, AI agreement, or a favorable journal-fit assessment cannot close this gate.

- `REVISE / MAJOR BUT FIXABLE — EDITORIAL`: the paper is scientifically intact but a critical reader cannot recover the puzzle, result mechanism, novelty boundary, or substantive interpretation. Revise in Stage 10 (architecture) or Stage 13 (integrated prose); repeat the editorial attack before GO.
- `CERTIFICATION REGRESSION`: the suggested wording requires an unproved substantive claim, reveals a missing theorem assumption, misstates prior art, or conceals an adverse benchmark/robustness result. Return to the earliest affected **scientific** Stage under existing governance.
- `JOURNAL-SPECIFIC FIT`: venue conventions/exposition mismatches alone normally return to Stage 12/13, not a theory redesign.
- `NOT APPLICABLE`: identify the article type and why an omitted element (e.g., policy Discussion in a narrowly mathematical correction) is not appropriate; do not manufacture relevance.

Stage 11 **cannot** issue an unconditional `GO` with an unresolved material editorial `REVISE`. Stage 13 **cannot** pass a report that only confirms all required headings exist. Stage 14 must reopen Stage 13 (or Stage 10 for architecture defects) when a final-PDF regression is identified.

## F. Required per-project artifacts

1. `EDITORIAL_EXEMPLAR_MAP.md` or equivalent: verified paper locations, adapted writing moves, prohibited inferences, Stage-12 journal refresh status.
2. `EDITORIAL_REFEREE_REPORT.md` or equivalent: first-pass paraphrases, source passages/pages, strongest communication-only desk-reject case, independent attack method, severities, resolution/routing.
3. `EDITORIAL_REVISION_AUDIT.md` or equivalent: before/after excerpt or diff, prior defect, verified theorem/claim guardrails, re-read verdict, page/section arrival and final source SHA.

These can be integrated into existing project reports, provided the corresponding evidence and gate decisions are individually identifiable. None is a blanket new mandatory paper section or an invented journal requirement.
