# Journal Requirements Evidence Checklist

Use this checklist for the selected journal at Stage 12 and re-run it from current official sources at Stage 14 immediately before submission freeze.

This checklist is evidence-bearing. A checked box without a current source, access date, interpretation, and mapped submission artifact/portal field is not sufficient for a material requirement.

## Evidence hierarchy

When requirements conflict, use the most specific current authority and record the conflict:

1. direct current instruction from the journal/editorial office applying to the actual submission;
2. current authenticated submission-portal instruction, required field, file designation, or generated-PDF behavior;
3. current journal-specific Guide for Authors / Instructions for Authors / journal policy page;
4. current publisher-wide official guidance;
5. secondary source, previous submission, repository note, memory, or inference.

Lower levels may provisionally fill gaps but may not override a more specific current source. Memory or prior experience alone never closes a material requirement.

## Required Journal Requirements Ledger

Maintain `JOURNAL_REQUIREMENTS_LEDGER.md` or an equivalent auditable artifact in the production-paper repository. For each material item record:

- requirement/topic;
- exact current official source URL or identifiable journal communication;
- source level from the hierarchy above;
- access/receipt date;
- operative requirement in concise words;
- affected manuscript file, source archive, declaration, metadata field, or portal action;
- verification method;
- status: `PASS`, `NOT APPLICABLE`, `UNVERIFIED`, or `CONFLICT`;
- resolution note when a conflict existed.

Material `UNVERIFIED` or unresolved `CONFLICT` blocks Stage-14 `SUBMISSION QA PASS`.

## Journal and article identity

- [ ] Journal title and publisher confirmed
- [ ] Current target article type/category confirmed
- [ ] Current submission system/portal confirmed
- [ ] Special issue/section requirements checked if applicable
- [ ] Current journal/publisher dates and links recorded

## Review model and author identification

- [ ] Single-, double-, or other anonymization model confirmed from current official evidence
- [ ] Main manuscript author-name requirement confirmed
- [ ] Separate title-page requirement confirmed
- [ ] Affiliation placement confirmed
- [ ] Corresponding-author designation confirmed
- [ ] Author email placement confirmed
- [ ] Acknowledgment/funding/conflict text handled consistently with anonymity rules
- [ ] PDF metadata/hidden identifying information checked when anonymity applies

## Initial-submission file requirements

- [ ] Whether PDF-only initial submission is permitted confirmed
- [ ] Whether editable Word/LaTeX source is required at initial submission confirmed
- [ ] Main manuscript file designation confirmed
- [ ] Title-page file designation confirmed if separate
- [ ] Figure file requirements/designations confirmed
- [ ] Table file requirements/designations confirmed
- [ ] Supplement/appendix file requirements/designations confirmed
- [ ] Cover-letter file requirements confirmed
- [ ] Highlights/graphical abstract/other ancillary files confirmed

## LaTeX/source-package requirements

Complete when LaTeX is used:

- [ ] `.tex` source requirement confirmed
- [ ] bibliography/BibTeX requirement confirmed
- [ ] figure files included in accepted formats
- [ ] table-source files included where applicable
- [ ] custom `.sty`, `.cls`, `.bst`, fonts, or non-standard dependencies handled as required
- [ ] archive format confirmed
- [ ] folder/subfolder restrictions confirmed
- [ ] source archive compiles from a clean extraction in the structure actually submitted
- [ ] source archive contains no unnecessary private/internal files
- [ ] generated PDF from source matches the intended manuscript

## Manuscript-format requirements

- [ ] Template/document class requirement confirmed
- [ ] page/word limits checked
- [ ] abstract limit checked
- [ ] keyword count/format checked
- [ ] JEL/classification codes checked if applicable
- [ ] line numbering/double spacing/margins/font rules checked when applicable
- [ ] equation/appendix/supplement conventions checked
- [ ] reference style requirement checked

## Figures, tables, and artwork

- [ ] figure/table count or placement rules checked
- [ ] accepted vector/raster formats checked
- [ ] resolution/effective-DPI rules checked
- [ ] font-embedding rules checked
- [ ] color/grayscale/accessibility rules checked
- [ ] separate artwork upload requirement checked
- [ ] caption/legend/table-note rules checked
- [ ] final outputs inspected at submission size

## Declarations and research-policy requirements

- [ ] Funding statement requirement checked
- [ ] Competing-interest/conflict declaration checked
- [ ] CRediT/author-contribution requirement checked
- [ ] Data availability requirement checked
- [ ] Code availability requirement checked
- [ ] Ethics/consent requirement checked if applicable
- [ ] Generative-AI / AI-assisted technologies policy checked
- [ ] Acknowledgment requirements checked
- [ ] Preprint/prior-publication/thesis/conference-paper rules checked when relevant
- [ ] Repository/data deposit requirements checked when relevant

## Submission metadata and portal fields

- [ ] Title exactly matches manuscript
- [ ] Author names/order exactly match manuscript
- [ ] Affiliations exactly match manuscript/title page
- [ ] Corresponding author matches system designation
- [ ] Emails/ORCID fields checked
- [ ] Abstract/keywords/JEL/classifications match manuscript
- [ ] Funding/conflict/data/code/AI declarations match uploaded files
- [ ] Suggested/opposed reviewer requirements checked
- [ ] Editor/section/topic selections checked
- [ ] Preprint/prior-submission questions checked
- [ ] Required author attestations/originality statements identified

## Fees, access, and licensing

- [ ] Submission fee checked
- [ ] Mandatory publication/page/color charges checked
- [ ] APC/open-access options distinguished from mandatory charges
- [ ] waiver/discount relevance checked where applicable
- [ ] license/copyright choices identified when required before acceptance/submission

## Authenticated portal preflight

Perform this before the final submit action whenever the journal uses an authenticated portal:

- [ ] Log in to the actual submission record
- [ ] Inspect current required fields and file-designation options rather than relying on remembered screens
- [ ] Reconcile every uploaded file with the ledger
- [ ] Confirm author/affiliation/corresponding-author fields
- [ ] Confirm declarations/attestations
- [ ] Confirm any journal-generated warnings are resolved
- [ ] Build/generate the portal PDF when supported
- [ ] Inspect the portal-generated PDF page by page
- [ ] Confirm first page author identification/anonymity is exactly as currently required
- [ ] Confirm all figures/tables/equations/citations/appendices render
- [ ] Confirm no file is missing, duplicated, misdesignated, or stale

If the authenticated portal reveals a requirement that conflicts with a lower-level source, treat the portal or direct editorial instruction as controlling for the current submission, record the conflict, update the package, and rerun the affected Stage-14 checks.

## Unresolved material-rule escalation

If a material submission rule remains genuinely unresolved after checking the current journal-specific instructions, relevant publisher guidance, and the authenticated portal when available, do not infer the answer from system behavior or absence of a warning.

Examples of material rules that require explicit resolution include:

- whether editable Word/LaTeX source is required at initial submission;
- whether the main manuscript must be anonymous or identified;
- where author names, affiliations, email, and corresponding-author information must appear;
- whether a separate title page is required;
- required declarations or prior-publication disclosures;
- mandatory charges or submission fees;
- required supplement/data/code files.

For any such unresolved item:

1. mark it `UNVERIFIED` in the Journal Requirements Ledger;
2. contact the journal/editorial office or publisher submission support for clarification when no authoritative current source resolves it;
3. preserve the reply or ticket reference as submission evidence;
4. update the ledger with the controlling instruction and receipt date;
5. rerun every affected Stage-14 package check before full PASS.

A submission portal accepting a file or allowing the workflow to continue is **not** by itself evidence that the file satisfies editorial-office technical requirements. Likewise, the absence of a public rule is not evidence that the requirement is optional.

## Final fail-closed gate

Stage 14 cannot return `SUBMISSION QA PASS` when any material requirement is:

- `UNVERIFIED`;
- supported only by memory/inference when an official source should exist;
- in unresolved `CONFLICT`;
- inconsistent with the actual file package;
- pending an authenticated portal check that is required to know the operative rule;
- pending journal/editorial-office clarification needed to resolve a material ambiguity.

A project may receive a documented `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED` only when all non-portal requirements pass and the sole remaining uncertainty genuinely requires authenticated portal access.

Stage 15 may freeze the preflight package, but `SUBMITTED` is prohibited until the authenticated portal reconciliation and final generated-PDF inspection are complete and the journal has issued submission confirmation.