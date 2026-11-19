# Stage 13P — Independent Publication Prose Review & Exemplar Benchmarking

> **Prospective mandatory gate: MAJOR v4.0 candidate, not part of immutable v3.0.**
> Authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this template → `checklists/PUBLICATION_PROSE_REVIEW_CHECKLIST.md`.
> Proposed route: **Stage 13 GO → Stage 13P GO → Stage 14**.

## 0. Role and independence

You are an independent field-journal **publication-prose referee**, not a mathematical/novelty referee or a new-theory developer. Judge whether the finished paper is lucid, idiomatic and persuasive on its own stated, certified terms. Do not claim editorial acceptance probability.

Two phases must be completed **in this order**, with separate frozen reports.

**Phase A: blind cold reading.** Provide the reviewer only the *actual integrated manuscript PDF* (and submission-facing scientific appendix/supplements), a neutral target journal and article-type description, and no author-supplied interpretation. Withhold the Stage 10A exemplar map, other exemplar papers, Stage 11/13 reviews, PR history, AI conversations, internal workflow artifacts, issue logs and any intended answers. Record any unavoidable prior exposure. A new AI model/session is preferable, but a changed model label alone does not prove independence; an AI review is never human peer review.

**Phase B: published-paper benchmark.** Only after saving Phase A, reveal Stage 10A's verified **complete** exemplars, Stage 12 journal refresh, and Stage 13 editorial revision audit. Compare specific located techniques and the full draft; never rewrite the earlier blind report after seeing the exemplars or past corrections.

## 1. Inputs and immutability

- `[RESEARCH_PROJECT]`; target journal `[TARGET_JOURNAL]`; article type `[ARTICLE_TYPE]`.
- Stage 13 **GO**, integrated manuscript source SHA `[SOURCE_SHA]`, compiled PDF SHA-256 `[PDF_SHA]`, page count, proof appendix/supplement hashes and reading accessibility.
- Reviewer identity and **access log**: files shown/hidden, prior context, whole-text page coverage, date and time, reviewer type and report commit/time for both phases.
- Stage 10A exemplar full-text acquisition/reading register, with precise version and page/section locations, revealed only **after Phase A**. A title, abstract, publisher snippet, inaccessible URL or AI summary is **not** full text.
- The frozen theorem/proof/novelty/negative-evidence map becomes available only **after the first reading**, for guarding edits against scientific drift, never for retroactively answering the blind questions.

## 2. Phase A — independent prose-only referee

Read all pages: Abstract, Introduction, model/timing, proposition introductions and explanations, Results, welfare/robustness, Related Literature, Discussion, Conclusion, exhibit notes/captions, Appendices/proof prose, references/footnotes, Funding/Data/Code/AI and other Declarations.

Before inspecting any prior explanations, independently write a **120–200-word reader paraphrase**: the question; strongest result; what variables/shock are held fixed or changed; economic mechanism; distinct contribution; exact limits. Specify any point the text does not let a qualified reader recover.

Evaluate text-grounded dimensions:

1. **Opening:** economic problem/puzzle before technical machinery; relevance, result, assumptions and limits in coherent order.
2. **Paragraph and argument:** purposeful topic sentences, transitions, cumulative understanding, clean definition order, consistent voice and terminology.
3. **Scholarly English:** natural field-appropriate idiom, unforced syntax, accurate verbs, controlled length, no generic promotional or machine-like filler.
4. **Economic intuition:** identify countervailing forces and why the sign/result follows near the headline mathematics, not just “by algebra”.
5. **Contribution and prior work:** specific positive economic learning, precise source credit, no self-praise or repeated defensive assertions that a device is “not new”.
6. **Scope:** Abstract, Introduction, theorem wording, caption, Discussion and Conclusion agree; do not drop restrictions or disguise counterexamples.
7. **Economy:** no duplicated interpretation, redundant caveat or author-side process narrative; reader has a useful reason to read each paragraph.
8. **Publication-facing apparatus:** citations, Appendix prose and proof bridges, tables, legends, acknowledgments, Data/Code/AI/funding/competing-interest declarations read as submitted research, not an internal audit log.
9. **Internal workflow contamination:** exposed “Stage-4A certification”, “Stage-11 reconstruction”, “hostile audit”, PR/issue history, QA/CI bureaucracy, “regression test” as author process and self-referee verdicts. Those are examples to scrutinize, **not** a universal word ban: “Stage 1” may correctly describe an economic game; an essential replication claim must remain.

For **each material problem**, give a short *exact manuscript quotation*, section/page/paragraph, why it impedes a reader, severity `FATAL EDITORIAL / MAJOR / MINOR`, concrete corrected wording or repair instruction, and guardrail on theorem scope. No generic praise or ungrounded rating is sufficient.

Write the **strongest credible communication-only desk-reject paragraph** supported by the exact manuscript passages. Separate it from a claim about mathematical truth or literature priority; a discovered scientific error routes upstream.

Save `PROSE_REFEREE_REPORT.md` and freeze it **before** Phase B.

## 3. Phase B — exact exemplar comparison

Use only exemplars actually **fully acquired and read** at Stage 10A (including material appendices), as refreshed in Stage 12 for the target journal and article type. A missing exemplar should be replaced by the bounded Stage 10A full-text procedure, not hallucinated or evaluated from an abstract.

For each applicable role, place exact **exemplar title/version and section/page/paragraph locator** beside exact **manuscript section/page/paragraph locator**, summarize the observed writing *move*, evaluate strengths/tradeoffs, describe the project-specific adaptation and source-science guardrails.

Compare (i) opening question/importance, (ii) transitions and argument progress, (iii) natural, concise scholarly English, (iv) model and notation presentation, (v) theorem introduction and neighboring economic intuition, (vi) distinctive contribution and source credit, (vii) exhibits/proof exposition, (viii) Discussion/limits/Conclusion, and (ix) the entire paper's coherent narrative.

Mark every applicable role `STRONG / ADEQUATE / WEAK` with concrete text evidence, or `NOT APPLICABLE — reason`. This is not a numerical or publisher-probability score. **ADEQUATE** means defensible publication-standard communication for the *specific paper and article type*, not objectively equal quality to all exemplary articles. “Top journal”, high citations or lexical similarity never proves quality.

**Do not imitate sentences, distinctive phrases, author voice, examples, theory, or excessively quote the exemplar.** Transfer a writing technique (e.g. problem → opposing forces → conditional result), not copyrighted prose or the exemplar's scientific conclusions. Choose role-specific sources when no single paper covers all roles; avoid mechanically patching incompatible styles.

Save `EXEMPLAR_PROSE_COMPARISON.md` independently from Phase A.

## 4. Issue resolution and scientific safeguards

Combine all Phase A/B findings in `PROSE_ISSUE_REGISTER.md` with ID, text locator/short source quote, severity, repair owner, bounded fix, scientific guardrail, status, and closure test.

Minor prose repairs can be done in a controlled revision pass linked to Stage 13. For each changed passage keep **before/after**, reason, reviewer check and a tracked diff. Never change: theorem assumptions/quantifiers, proof-critical bridges, signs/numbers, welfare/objective interpretation, literature priority, causal language, negative evidence or AI/author verification claims. If a correction requires changed science, **stop and reopen the earliest relevant scientific Stage**. Legitimate limitations are not deleted just to make the article sound bolder.

After repairs, commission an **independent second cold read** of the actual revised complete manuscript without giving the solution key. The original reviewer may check small factual diffs but may not alone close disputed MAJOR issues. Include the second reviewer's access/independence record and closure evidence in `PROSE_REVISION_AUDIT.md`.

Keyword scanning, LaTeX/CI PASS, previous Stage 11 favorable comments, or the presence of a benchmark checklist are **not substitutes** for the actual all-page prose judgment.

## 5. Verdict and kill tests

Use canonical `GO / CONDITIONAL GO / NO-GO`, **not** invented submission clearance.

- **GO:** Phase A entire text read independently and *frozen first*, Phase B complete source-located comparisons, every material flaw repaired and confirmed by second cold read, no unresolved `FATAL EDITORIAL`/`MAJOR`, no unexplained `WEAK` material role, no scientific drift; exact accepted source/PDF hashes recorded.
- **CONDITIONAL GO:** exactly **one bounded editorial-only fix** with owner, passage, objective completion evidence and retest. **Does not authorize Stage 14.**
- **NO-GO:** multiple material prose defects, incomplete reading, fabricated source access, compromised “blind” report, unresolved desk-reject-quality communication failure, or failed independent retest. Return to Stage 13/10A as warranted. If a purported prose fault exposes false proof or novelty, return to the earlier scientific Stage.

Do not confer GO on publication acceptability, predicted journal decision or authorship approval.

## 6. Required five artifacts and Stage 14 handoff

1. `PROSE_REFEREE_REPORT.md` — phase-A cold read, exact source/PDF snapshot, access log, independent paraphrase, strongest communication-only editor rejection and text-located findings; **commit before opening Phase B**.
2. `EXEMPLAR_PROSE_COMPARISON.md` — verified complete source versions, page/section-level role-wise comparison, supported ratings and transfer limits.
3. `PROSE_ISSUE_REGISTER.md` — complete finding/repair/closure matrix.
4. `PROSE_REVISION_AUDIT.md` — verified before/after diff, science-preservation checks, new source/PDF snapshot, **second cold reader** record and retest.
5. `STAGE13P_GATE_REPORT.md` — complete evidence matrix, verdict, accepted exact manuscript/PDF hashes and Stage-14 contract.

Stage 14 must compare its actual final PDF and source against the **GO snapshot**, including anonymous/title-page/appendix variants. Any post-GO text change (even in captions, footnotes, cover-facing statements, AI/Data/Code Declarations) triggers at least a targeted changed-passage and cross-section retest. Mechanical spelling may get a bounded retest; material rhetorical rewrites require fresh independent all-text evaluation and exemplar comparison of affected roles. Scientific drift returns upstream. **No unreviewed material change may reach Stage 14 PASS or Stage 15 freeze.**

A final human author sign-off remains separate; AI-assisted prose review does not substitute for it.
