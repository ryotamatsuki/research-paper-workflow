# AI Provenance / Human Accountability Refinement — 2026-09-24

Status: merged-design record for a prospective minor workflow revision after v2.5.

## Problem

The existing workflow already distinguishes provenance from evidence, requires independent mathematical attacks, embeds formal verification before theory freeze, and checks generative-AI declarations at submission. It did not, however, require a continuous material-AI-use record, did not explicitly separate AI verification from author verification, and did not require evidence of the author's own intellectual judgments before theory/submission freeze.

This creates two risks:

1. an AI/adversarial/formal check can be rhetorically collapsed into "the author independently verified the result"; and
2. a generic disclosure statement can overstate or understate what actually occurred.

## Design decision

Do not add a new Stage.

Strengthen existing stages and evidence rules:

- Stage 0 onward — log material AI use by reference, not transcript duplication;
- Stage 7.5A — require a central-result author intellectual-contribution record before the gate can close;
- Stage 8 — freeze that record with the theory object;
- Stage 14 — reconcile the use log against Methods/repository disclosure, manuscript-preparation disclosure, journal policy, and portal fields;
- Stage 15 — require personal author sign-off tied to the exact frozen commit/package;
- SSRN-only — check current SSRN disclosure locations and high-volume/bulk-submission rules without manufacturing submission spacing or artificial chronology.

## Verification-actor distinction

The workflow now distinguishes:

- AUTHOR;
- AI;
- COMPUTATION;
- FORMAL;
- EXTERNAL HUMAN.

Different actors may provide complementary evidence. They are not interchangeable.

A second AI or separate chat may improve adversarial independence but is not external human review and does not establish that the author personally verified a claim.

## Human contribution standard

The workflow does not impose universal AI-free rediscovery or memorized re-proof.

Instead, central results require evidence of substantive author judgment: research question/mechanism, assumptions, proof/equilibrium logic, limitations/failure boundaries, maximum defensible claim, and the author's acceptance/rejection/modification of AI-assisted suggestions.

Mere approval of AI output or a successful Lean build is insufficient.

## Formal verification boundary

No change to the existing formal-verification architecture. Lean/proof-assistant PASS remains a certificate about encoded statements under encoded assumptions. It is explicitly prohibited from serving as a proxy for authorship, author understanding, model-to-formal fidelity outside the mapping audit, economic validity, novelty, or unformalized case completeness.

## Disclosure rule

Disclosure language must be generated from evidence, not from boilerplate.

Statements such as "all substantive claims were independently verified by the author" are allowed only if the author-verification record supports that scope. AI checks, computation, Lean, and external review are recorded separately.

## SSRN rule

SSRN compliance is submission-destination-specific rather than a universal research gate. When SSRN is actually used, the project checks the current official rules, required disclosure locations, and any bulk/high-volume-submission constraints.

The workflow explicitly forbids artificial spacing, staged dates, or manufactured process history intended to make submission activity appear normal.

## Version impact

This is a MINOR-class change under `docs/VERSIONING_POLICY.md`.

It adds evidence and accountability obligations inside existing Stages 7.5A/8/14/15 and cross-stage provenance rules. It does not add, remove, renumber, merge, or reroute a canonical Stage; it does not change `GO / CONDITIONAL GO / NO-GO` semantics; and it does not change theory-freeze or submission-freeze architecture.

Accordingly, the merged state may be described as a prospective v2.6 refinement until a separate release audit/tag is completed.
