# Editorial argument quality — regression fixtures

These are reusable *failure-mode tests*, not claims about a particular journal's decision or a substitute for real source reading. Use in a workflow QA rehearsal whenever Stage 10/11/13 editorial gates change. Assume the scientific content is correct unless otherwise specified.

## Case 1 — Correct sections, poor opening (must not PASS)

**Manuscript:** begins by listing two governments, a private intermediary, type distributions and price formulas. The economic question and unexpected sign implication are present on later pages. The section checklist marks “question included,” “result included” and “Introduction present.”

**Expected decision:** `REVISE — EDITORIAL`. Stage 10/13 must reorder the introduction around an accessible puzzle and main inference. An assertion that all required elements are present does not pass the cold-reader test.

## Case 2 — Correct proposition, intuition scattered (must not PASS)

**Manuscript:** theorem derives a sign reversal from a lower/upper share interval; text separately lists primitives and policy indicators. It does not explain which opposing forces generate the reversal or why the share has two roles.

**Expected decision:** `REVISE — EDITORIAL`. The Stage-11 editorial referee must flag missing explanation near the theorem even if the mathematical reviewer and symbolic tests pass; Stage 13 revises prose without changing the theorem.

## Case 3 — Institutional examples replace the economic lesson (must not PASS)

**Manuscript:** Discussion lists three real institutions and a paragraph about scope, but starts without explaining the welfare counterfactual or what new economic inference the model supplies. Institution descriptions are accurate and cited.

**Expected decision:** `REVISE — EDITORIAL`. The existence of an institutional section and citations does not satisfy the economic-lesson test. Explain the decision object first and label examples illustrative.

## Case 4 — Good style but theorem inflation (scientific rollback)

**Manuscript:** revised Introduction is concise and engaging but presents a conditional positive derivative as proof that public provision raises total welfare, or relabels a numerical equilibrium witness as a general equilibrium theorem.

**Expected decision:** `CERTIFICATION REGRESSION`; return to the earliest affected scientific Stage. No rhetorical polishing or lower-fidelity scope disclaimer can close this defect.

## Case 5 — No suitable accessible exemplar (honest bounded route)

**Manuscript:** very narrow mathematical correction; the editor can verify one relevant source article but cannot access a second relevant published full text.

**Expected decision:** record the accessible exemplar, explicit search/read limitation and the correction-specific `NOT APPLICABLE` elements. Do **not** invent two extra exemplars or mandate an irrelevant policy discussion; the cold-reader and theorem-scope gates still apply.

## Case 6 — Reviewer says “substantially clearer” (must not auto-PASS)

**Manuscript:** an adversarial scientific referee praises improved clarity but supplies no first-pass paraphrase, page/paragraph evidence, post-proposition mechanism reconstruction, or strongest communication-only rejection paragraph.

**Expected decision:** `UNRESOLVED — EDITORIAL ATTACK NOT PERFORMED`. A favorable overall opinion is not a completed editorial gate.

## Regression acceptance checklist

- [ ] All four material failure cases block unconditional GO.
- [ ] Case 4 routes to scientific rollback instead of prose-only repair.
- [ ] Case 5 permits documented legitimate N/A rather than fabricated evidence.
- [ ] Case 6 prevents praise-only PASS.
- [ ] None of the cases requires extra theorem, new data, a specific page count, a mandatory figure, or an unsupported journal rule.
