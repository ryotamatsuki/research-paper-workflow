# Frontier, Author-Limitations, and Next-Question Audit Checklist

> Companion checklist under `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md`. Use in Stages 2 and 6 and as an input to Stages 3 and 7.5. It is **not** an additional canonical Stage, a new GO criterion based on idea count, or permission to model an extension at an evaluative gate.

## A. Source-grounded limitations (Stage 2; update Stage 6)

- [ ] For each **decisive closest paper** inspect Abstract, Introduction/positioning, model/assumptions, main propositions/proofs, Discussion/Conclusion, stated limitations, and explicit future-work passages where accessible.
- [ ] Capture each limitation/question with paper identity/version, section/page and **short faithful paraphrase**; distinguish a **VERBATIM AUTHOR-STATED limitation/future question** (supported by an exact quotation/location where permitted) from an **AUDITOR-INFERRED gap** or a **CROSS-PAPER SYNTHESIS**.
- [ ] Classify the limitation: exogeneity/endogeneity; equilibrium selection; identification/data; welfare/incidence; institution/implementation; information/commitment; heterogeneity/network; functional form/regularity; generality/scope; other.
- [ ] Differentiate a tractability assumption the authors explicitly concede from a weakness conjectured by the auditor; the absence of a variable or extension **does not** itself prove a valuable research gap.
- [ ] Record whether an author-stated extension would merely add a mechanism already treated in another literature.
- [ ] Mark `NOT INSPECTED` (access unavailable), `NOT FOUND` (the sections read did not state one), or `UNRESOLVED` (classification unclear); do not invent limitations or attribute auditor suggestions to authors.

## B. Is the gap still open *now*?

- [ ] Forward-citation search from the relevant paper; later same-author papers; recent working papers, journal versions and adjacent-field terminology checked *as of a recorded cutoff date*.
- [ ] Candidate gap and proposed solution checked against the most plausible **general parent theory** and corresponding theorem, including appendix and working-paper versions.
- [ ] Mark current status `RESOLVED / PARTIALLY RESOLVED / OPEN WITH EVIDENCE / UNRESOLVED`. `OPEN WITH EVIDENCE` does not mean proof of global nonexistence of a paper.
- [ ] Document precise scope **already solved**, residual narrower question, strongest unresolved predecessor mapping, and primary-source access/reading depth.
- [ ] If only abstracts or secondary sources are available, leave theorem-level openness `UNRESOLVED`; record targeted acquisition/search action instead of claiming novelty.

## C. Generate *research questions*, not automatic model extensions

- [ ] Generate from three distinct sources where present: **explicit author limitations**, **cross-paper contradictory/partial coverage**, and **policy/economic decision gaps**. A source type may legitimately yield no candidate.
- [ ] State each candidate in economic terms (who chooses, what friction, what equilibrium/welfare outcome), **before** choosing a mathematical model or extra parameter.
- [ ] State the **counterfactual learning gain**: "If solved, a specialist would newly know when/why [specific behavior, welfare ranking, coordination or implementability result] instead of the strongest known conclusion [X]."
- [ ] Specify a falsifiable mathematical/econometric target: potential proposition, inequality, ranking, identification estimand, counterexample, corrected theorem or classification—not a generic wish to "study effects".
- [ ] Explain why the candidate is not merely a known externality, textbook decentralization criterion, generic LQ Hessian sign, cosmetic combination, unmotivated heterogeneity or different institutional label.
- [ ] Specify the **minimum** distinct strategic/information/technology margin required and which canonical nested benchmarks must reproduce the old result.
- [ ] Identify the single closest predecessor capable of killing the proposal, a general-model equivalent, and one fast 24–72 h feasibility/falsification test *if proportionate*. This is an investigation design, not work already completed.

## C2. Predecessor-result reversal / paradox / sharp-boundary exploration

- [ ] Alongside future questions, test up to a bounded set of **same-question / new-result** candidates; preserve original theorem identity, formal domain, conclusions, welfare benchmark and equilibrium selection.
- [ ] Search for sign/welfare-ranking reversals, non-monotonicity, impossibility, counterexamples, and unexpectedly strong robustness. A dramatic result is not required.
- [ ] Check differences in estimand, welfare/accounting, policy choice set, information and equilibrium concepts before calling two studies contradictory.
- [ ] Use one minimal economically justified assumption relaxation and a nested prior-theorem recovery test; record a precise falsifier, strongest generic parent theorem and later-work status.
- [ ] Distinguish a conjectured paradox from a proved counterexample and a certified general characterization; no fabricated reversal or result-driven rescue.
- [ ] Use `checklists/RESULT_REVERSAL_BOUNDARY_CHECKLIST.md` and Section C2 of `templates/FRONTIER_OPPORTUNITY_REGISTER.md` or equivalent compact ledger.

## D. Selection, provenance, and honest routing

- [ ] Keep a **structurally deduplicated, bounded** candidate bank; distinguish `HYPOTHESIS`, `LITERATURE-SCREENED`, `MODEL-TESTED`, `CERTIFIED`, and `KILLED` maturity.
- [ ] Compare credible candidates on (i) probable economic learning, (ii) novelty threat, (iii) feasible proof/data, (iv) portable conditions, (v) substantive welfare/organizational consequence, (vi) scope/implementation where relevant; scores never certify novelty.
- [ ] Prefer up to 3 **credible** alternatives when meaningful, with one preferred **question** if justified; **zero** is an acceptable output when evidence is insufficient. Do not fabricate three candidates.
- [ ] Store a short `EDITOR-REJECTION → OPPORTUNITY` mapping: strongest reason current paper fails, source limitation or cross-paper gap that suggests a different question, the most promising *unverified* answer and its kill test.
- [ ] **Separate decisions**: the present paper's Stage-6/7.5 verdict must be made **without** using an attractive future candidate as evidence of present-paper novelty, and without letting a present-paper NO-GO falsely certify a new idea.
- [ ] Never convert Stage-6/7.5 `NO-GO` into automatic Stage-3 `GO`; offer a **prospective Stage-0/2/3 intake** requiring author selection and fresh gates.
- [ ] A `GO` full paper should **still** preserve meaningful future questions without requiring their solution unless the current paper's promised question remains materially unanswered.
- [ ] For a substantive correction, pure mathematics, or important diagnostic/negative result, prioritize the matching contribution type; empirical identification, implementable policy and extra models are **not universal prerequisites**.
- [ ] Record source URLs/DOIs, last verification date, author-versus-auditor origin, evidence depth, verifier class (`AI / AUTHOR / COMPUTATION / FORMAL / EXTERNAL HUMAN`), unresolved blockers, and cost/time budget.

## Required output pointers

Use Section E of `templates/RESEARCH_SEARCH_REGISTER.md` or `templates/FRONTIER_OPPORTUNITY_REGISTER.md`, or an equivalent compact project record. Never duplicate the same bibliography merely to fill both. Stage 2 provides a **provisional** opportunity map, Stage 3 selects a research-question hypothesis, Stage 6 updates against actual certified results, Stage 7.5 separates the frozen-paper verdict from **future** recommendations.

**No viable candidate:** If all hypotheses are solved, absorbable, insufficiently evidenced or infeasible within the search budget, explicitly record `NO DEFENSIBLE NEXT QUESTION FOUND IN SEARCH BUDGET`, the papers checked, and what new evidence would justify reopening. This is a valid scientific output, not a failure of creativity.

**Failure condition:** Source limitations were not inspected for decisive papers where accessible; later relevant solutions were ignored; author language was misattributed; an unscreened speculation was described as a verified open question; or a new topic was used to bypass the previous project's stop/rollback decision. Mark the evidence incomplete or `UNRESOLVED`, not `GO`.
