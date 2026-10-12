# research-paper-workflow v2.9 — Release Notes

Release date: 2026-10-12 JST
Classification: **MINOR** relative to v2.8
Baseline tag: `v2.8` (commit `aa80ffcd11615ce6da71807ee3dffde503c840e4`)

## Why this release exists

Previously, a mathematically sound, distinct model could progress toward a full field-journal paper without a sufficiently skeptical answer to **what economically consequential question it answers beyond the closest known theorem**. In addition, literature searches used to reject derivative novelty did not consistently preserve the original papers' limitations and follow-up discoveries as a structured source of fresh research questions.

v2.9 introduces two mutually complementary evaluations: **(1) an independent current-paper economic-value and question-completeness gate, and (2) evidence-based research-frontier extraction for a separately author-selected next question**. A new question cannot rescue the old paper's NO-GO.

## Change A — economic contribution and completeness (design dated 2026-10-10)

- **Stage 6:** a specialist-editor publication case and strongest skeptical objection, tied to the closest theorem, actual Stage-4A-certified results and **essential vs bounded** unanswered questions.
- **Stage 7:** when genuinely policy-oriented, distinguish diagnosis (**WHY**), modeled efficient alternative (**SHOULD**), and actionable institutional/financial feasibility (**COULD**), or defend why a diagnostic-only result stands on its own.
- **Stage 7.5:** independently enforce economic significance and completeness; a correct, non-isomorphic formula alone cannot produce full-paper GO when a central promised question remains unanswered.
- **Stages 8, 11, 12:** preserve the adoption audit, repeat the strongest field-editor objection, and test actual journal fit independently of mathematical correctness.
- **Proportionality:** pure theory, substantive corrections, negative/diagnostic work, and research notes are not mechanically forced to invent an implementation theorem, data set, or extra model.

Source: `docs/ECONOMIC_CONTRIBUTION_COMPLETENESS_REFINEMENT_2026-10-10.md`; operational checklist `checklists/ECONOMIC_CONTRIBUTION_COMPLETENESS_CHECKLIST.md`.

## Change B — prior-paper limitations to new research questions (design dated 2026-10-12)

- **Stage 2:** for decisive closest papers, inspect Abstract/Introduction positioning, verified theorem scope and assumptions, Discussion/Conclusion, author-stated limitations and future questions; clearly separate auditor-inferred or cross-paper gaps. Check same-author/later/forward-citing and working-paper results and generic parent theorems before suggesting any gap remains open.
- **Stage 3:** choose the potentially important **economic question before modeling a new mechanism**, with new learning over the strongest prior result, falsifiable theorem/estimand, minimal test and kill conditions.
- **Stage 6:** record **two independently justified outputs**: current-paper GO/CONDITIONAL GO/NO-GO and prospective next-question opportunities, including the honest case of **zero** defensible opportunities.
- **Stage 7.5:** independently judge the future opportunities, without changing the present-paper editorial verdict or authorizing a new paper. New projects require author selection and Stage 0/2/3 entry.
- **Evidence discipline:** author-stated `AUTHOR-STATED`, auditor-inferred `AUDITOR-INFERRED`, `CROSS-PAPER`; solution status `RESOLVED / PARTIALLY RESOLVED / OPEN WITH EVIDENCE / UNRESOLVED`.

Sources: `docs/FRONTIER_OPPORTUNITY_REFINEMENT_2026-10-12.md`, `checklists/FRONTIER_OPPORTUNITY_CHECKLIST.md`, `templates/FRONTIER_OPPORTUNITY_REGISTER.md`.

## Compatibility and migration

- No Stage is added, removed, renumbered or rerouted; all existing mathematical/novelty/scope, AI provenance, formal-verification and submission-gate standards still apply.
- The version remains **MINOR** under `docs/VERSIONING_POLICY.md`; the new obligation is evidence review inside existing gates, not a change in GO/NO-GO meaning.
- Existing completed/frozen research is not automatically regraded or retroactively redocumented. Apply v2.9 at the next authorized Stage or deliberately initiate a new scoped audit.
- A future-looking question is **not** evidence that the failed existing paper should get an extra extension; no automatic restart of stopped models.
- The previous v2.8 and older Git tags/Releases are immutable historical references.

## Reliability and release limitations

The v2.9 integration/readiness documents validate stage identity, route integrity, citations to local companion artifacts, text-level regression contracts and the publishing workflow's immutable-tag safeguards. These checks do **not** demonstrate that the upgraded frontier search always discovers important truly open questions; that requires subsequent genuine literature-project trials and author/external-referee scientific judgment. The tag/Release is created only after the main-branch publishing job passes; draft readiness text by itself is not publication evidence.
