# Active-version consistency audit — 2026-11-20

## Result
Canonical research-paper-workflow release: **v3.2** (2026-11-19). Architecture baseline: v3.0. Independent prose component: v3.1. Optional TDF: **v5.1** (independent version line).

## Inspection and changes
- The existing v3.2 Git tag, release notes, active protocol, README, governance and pipeline were checked.
- The v1.0..main comparison returned 160 changed paths, used as an inventory, not a complete tree listing. Active templates, checklists and CI entrypoints were checked for stale version declarations.
- Governance and Pipeline active headers now say v3.2; README and versioning policy distinguish current status from historical proposals. Incorrect proposal/unreleased headers in active checklists and Stage-13 template were corrected.
- WORKFLOW_VERSION records the machine-readable active version. scripts/verify_current_version.py and the research-design GitHub Action enforce equality of current declarations and preserve the separate TDF v5.1 label.
- Existing release tags, release publication workflows, dated archival notes, pinned v3.1 scientific regression snapshots and the historical v3.1 prose verifier were intentionally NOT changed.

## Release-update checklist
1. Verify the new canonical Git tag/release and release notes; never declare an unreleased candidate current.
2. Update WORKFLOW_VERSION, README current and stable references, Governance/Pipeline Version headers, docs/VERSIONING_POLICY.md and the current CI name/checks together.
3. Run scripts/verify_current_version.py, scripts/verify_research_design_contract.py, scripts/verify_integrated_prose_contract.py and the independent TDF checks before merging.
4. Do not mass-replace historical tags, source snapshots, older proposals or tests named for a subsystem's original version.
5. Version metadata does not override Governance → Pipeline → Stage templates → Checklists authority.

## Limitations
This is an active-version audit, not a byte-by-byte review of every historical file. CI guards active version declarations and cannot certify mathematical correctness or previously issued Stage decisions.
