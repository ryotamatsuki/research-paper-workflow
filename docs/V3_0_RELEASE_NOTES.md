# research-paper-workflow v3.0 — Release Notes

Released from the reviewed `main` line on 2026-11-19 JST.

## Breaking change: a mandatory pre-writing benchmark

The canonical production path is **Stage 9 → Stage 10A → Stage 10B → Stage 11 → Stage 12 → Stage 13 → Stage 14 → Stage 15**.

- **Stage 10A — Exemplary Paper Benchmarking & Synthesis** is a mandatory, independently gated stage preceding the writing of a manuscript. Each selected writing exemplar must be lawfully obtained in full and read completely, including material proofs and supplements; abstract-only, preview-only and merely linked sources are excluded before selection or scoring.
- Usually compare **3–5 source-verified published articles** by their actual strengths for problem framing, notation/proof exposition, economic intuition, figures, Discussion and explicit limitations. An overall primary exemplar is optional. Smaller sets require a justified bounded search and complete role coverage.
- Produce **EXEMPLARY_PAPER_REGISTER.md**, **EDITORIAL_EXEMPLAR_MAP.md**, and **MANUSCRIPT_BLUEPRINT.md**, including role-by-role trade-offs and a whole-manuscript coherence audit, before Stage 10B may start.
- **Stage 10B** is the historical Stage 10 manuscript-construction task, renamed to reflect the new entry gate. The existing `templates/STAGE_10_PAPER_BUILD.md` path is retained.
- Stage 11 critically attacks an actual manuscript after a cold read; Stage 12 refreshes journal-specific exemplars; Stage 13 repairs demonstrated editorial defects; Stage 14 checks the exact PDF.

## Other integrated post-v2.9 changes in the tagged main snapshot

The release also captures the changes merged on `main` after v2.9: model-appropriate equilibrium/continuation clarification; independent editorial communication tests; premature novelty and parent-theorem absorption guardrails; result-reversal/boundary discovery prompts; TDF v5.1 optional discovery material; and selective route-aware contribution assessment. These do not override proof, source, scientific novelty, human accountability, or freeze gates.

## Compatibility and migration

This is a **MAJOR** release because it adds a mandatory Stage and changes normal stage routing. Existing submitted, published, or v2.x-certified papers retain historical provenance. For an existing manuscript undergoing extensive rewriting, run Stage 10A *prospectively* and then rerun manuscript integration, editorial referee attack, and required verification; never falsely backdate benchmarking or silently alter a frozen theory.

## Scientific and publication guardrails

An exemplary paper is a **writing reference**, not proof of novelty or an assurance of acceptance. Do not copy copyrighted passages, silently adopt exemplar assumptions, omit essential proof bridges, or expand the theorem scope without explicit rollback. `GO` requires actual source and reading evidence, not a checklist assertion.

## Source and validation

- `GOVERNANCE.md`
- `THEORY_PAPER_RESEARCH_PIPELINE.md`
- `templates/STAGE_10A_EXEMPLARY_PAPER_BENCHMARKING.md`
- `checklists/EXEMPLARY_PAPER_BENCHMARKING_CHECKLIST.md`
- `docs/V3_0_READINESS_CHECKLIST.md`
- `docs/V3_0_INTEGRATION_AUDIT.md`

The release tag is created only after the CI publication job verifies the reviewed main revision and that `v3.0` does not already exist.
