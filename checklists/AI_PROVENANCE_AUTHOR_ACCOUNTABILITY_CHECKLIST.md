# AI Provenance and Author Accountability Checklist

Status: active cross-stage checklist

Canonical authority: `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → this checklist.

## 1. Purpose

This checklist makes material AI use traceable without turning the workflow into a transcript archive. It also prevents AI review, proof-assistant success, or computation from being mislabeled as author verification.

The governing rule is:

> AI may assist discovery, checking, coding, exposition, and submission preparation, but evidence must identify who or what performed each verification. An AI check does not become an author check merely because the author accepted the output.

## 2. What to log

Log material AI use when it affects a research decision, adopted result, proof/counterexample path, code/formal artifact, literature assessment, manuscript text/structure, or submission declaration.

Routine spelling, formatting, or other non-material assistance may be summarized rather than logged item by item unless the target journal/publisher requires more.

A material-use record should identify, where applicable:

- date;
- tool/provider and model or model family when reasonably available;
- task/purpose;
- input context or artifact reference sufficient to reconstruct the task;
- adopted output or affected artifact;
- whether the output was accepted, modified, rejected, or used only diagnostically;
- verification method;
- verification actor;
- evidence/reference to the verification;
- downstream claim/file affected.

Existing chats, commits, diffs, audit reports, test logs, formal certificates, or review notes may be referenced. Do not duplicate full conversations merely to satisfy this checklist.

Suggested row:

`date | tool/model | purpose | adopted artifact/decision | disposition | verification method | verification actor | evidence ref | downstream effect`

## 3. Verification-actor taxonomy

Use explicit actor labels rather than the vague word "verified":

- `AUTHOR` — the author personally inspected, reasoned through, tested, derived, or otherwise performed the stated check;
- `AI` — an AI system performed the stated analysis/check;
- `COMPUTATION` — deterministic or stochastic code/symbolic computation produced the stated evidence;
- `FORMAL` — a proof assistant/kernel checked the encoded statement;
- `EXTERNAL HUMAN` — a person other than the author reviewed the work.

Multiple labels may apply to the same claim, but do not collapse them into one.

A second AI, separate chat, or different prompt is an AI-side independence measure only. It is not external human review and not author verification.

## 4. Author intellectual-contribution record

Before Stage 8 freeze, create an `AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD` or equivalent for each central result/set of tightly related results.

Record concise evidence that the author has made and understands the substantive research judgments, including:

- why the research question and mechanism matter;
- why the central assumptions/restrictions were adopted;
- the proof/equilibrium logic at the level needed to detect a material mistake;
- the principal boundary conditions, failure modes, and limitations;
- the distinction between what was proved analytically, checked computationally, formally certified, or only suggested by AI;
- the author's own acceptance, revision, rejection, or qualification of AI-assisted suggestions;
- the author's judgment on the maximum defensible claim.

A complete AI-free rediscovery or memorized re-proof is not a universal requirement. However, merely reading an AI explanation, observing a green Lean build, or approving an AI audit without substantive author reasoning is insufficient.

Acceptable evidence can include dated research notes, author-written derivations, corrections prompted by the author's review, recorded claim-scope decisions, annotated proofs, or a concise sign-off note tied to the relevant commit/artifacts.

## 5. AI-audit independence record

When an AI system is used for adversarial or "independent" review, record:

- what artifacts/context the reviewer received;
- whether it saw the production proof/derivation/solver or only primitives/claim statements;
- whether the review used a genuinely different derivation/evaluation path;
- which assumptions or conclusions were withheld to enable a clean-room attack;
- what failure modes the review could not independently test.

Do not describe an AI self-audit as external peer review. Do not describe a second AI as human-independent verification.

## 6. Formal-verification boundary

Lean or another proof assistant certifies only the encoded statement from encoded assumptions.

- [ ] The formal certificate states what assumptions are supplied.
- [ ] The paper/model ↔ formal statement mapping has been checked separately.
- [ ] Unformalized economic cases, interpretation, novelty, empirical relevance, and equilibrium-domain completeness remain explicitly outside the formal guarantee unless actually encoded.
- [ ] A green formal build is not used as evidence of author contribution or human verification.

## 7. Stage 14 disclosure reconciliation

At Stage 14:

- [ ] Compare the material-use log with the final manuscript, Methods/appendix/repository documentation, and required AI declaration.
- [ ] Separate research-method use (e.g. proof search, coding, analysis, formalization support) from manuscript-preparation use (e.g. organization, language, rewriting) when the operative policy distinguishes them.
- [ ] Verify the target journal/publisher's current required wording and placement.
- [ ] Remove boilerplate that claims more human verification than the record supports.
- [ ] Do not omit material AI use merely because the result was later checked by Lean, code, or another AI.
- [ ] Ensure manuscript, cover letter, portal fields, and disclosure statement are mutually consistent.

A sentence such as "all substantive claims were independently verified by the author" may be used only if the evidence record actually supports that scope. Otherwise state the narrower, accurate division of checks.

## 8. Stage 15 author sign-off

Before final submission freeze, the author must personally sign off the exact final commit/PDF/package.

Record:

- exact commit/SHA and final PDF/package;
- confirmation that the author contribution record still matches the final central claims;
- confirmation that the AI-use disclosure matches the material-use log;
- confirmation that no AI/Lean/computational result is being represented as an author check unless the author actually performed the corresponding review;
- any unresolved limitation explicitly accepted for submission.

AI-generated approval, automated CI, or proof-assistant PASS cannot substitute for this sign-off.

## 9. SSRN-specific checks

Apply this section only when SSRN is an actual submission destination.

- [ ] Re-check the current SSRN AI/submission rules from official sources at Stage 14/15.
- [ ] Confirm every required disclosure location, including PDF and submission/abstract metadata when currently required.
- [ ] Check current restrictions or review practices concerning bulk/high-volume submission and duplicate/redundant content.
- [ ] Preserve the real research chronology and submission record.
- [ ] Do not manufacture spacing, dates, staged commits, or artificial process history merely to make submission activity appear normal.
- [ ] If the current rule is unclear or the planned submission pattern creates a material compliance question, obtain clarification rather than infer a safe numerical threshold.

## 10. Blocking conditions

Stage 8, 14, or 15 is blocked as applicable when:

- a central result has no author intellectual-contribution/sign-off evidence;
- material AI use cannot be reconciled with the disclosure;
- an AI check is represented as author or external-human verification;
- a formal/computational PASS is used to imply economic/model validity outside its encoded/tested scope;
- the disclosure contains a factual claim about verification that the provenance record does not support;
- SSRN-specific requirements are assumed from memory rather than re-checked when SSRN is the actual destination.

## 11. Minimal completion record

Production repositories may satisfy this checklist with three linked artifacts rather than a transcript dump:

1. `AI_PROVENANCE_LOG` — material uses and dispositions;
2. `AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD` — central-result understanding/judgment evidence;
3. `AI_DISCLOSURE_RECONCILIATION` — Stage-14/15 mapping from actual use to final disclosure and placement.

Equivalent names/formats are acceptable if the required information is auditable.
