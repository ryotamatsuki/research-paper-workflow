# Exposition Streamlining Refinement — 2026-09-24

## Purpose

This refinement incorporates a generalized version of the exposition discipline that motivated the discussion: reach the central question and result quickly, keep section functions clean, consolidate the model, ration main-text exhibits, and remove material whose marginal contribution to understanding is low.

The motivating slide contained paper-specific page targets for a structural/empirical job-market paper. Those numerical targets are not promoted to universal workflow rules. The canonical implementation instead separates invariant principles from article-type-specific diagnostics.

## Design decision

The refinement uses the existing exposition lifecycle rather than creating a new canonical Stage:

Stage 7 → Stage 10 → Stage 13 → Stage 14

- **Stage 7:** candidate exposition vehicles.
- **Stage 10:** architecture design.
- **Stage 13:** aggressive streamlining of the integrated manuscript.
- **Stage 14:** final binary verification and rollback if the architecture has regressed.

This avoids overloading Stage 14 with late substantive editing.

## New operational artifact

checklists/EXPOSITION_STREAMLINING_CHECKLIST.md

The checklist introduces:

- Introduction compression test;
- section-purity test;
- manuscript-specific reader-arrival budget;
- main-text necessity classification (CORE, HELPFUL, APPENDIX, DELETE);
- five-exhibit thought experiment;
- redundancy audit;
- compression-without-damage audit;
- separate profiles for theory-first, structural/quantitative/empirical, and correction/comment/reassessment papers;
- explicit Stage-10 design, Stage-13 streamlining, and Stage-14 verification obligations.

## Compatibility

This is a backward-compatible minor refinement. It changes no Stage numbering, canonical verdict semantics, theorem-certification rules, or submission-freeze meaning.

The refinement is deliberately subordinate to:

1. scientific correctness and theorem/evidence scope;
2. current journal/article-type requirements;
3. reproducibility and source completeness.

A shorter paper is not automatically a better paper. Material needed to state assumptions, identify the model, prove the theorem, document evidence, or delimit scope may not be deleted merely to satisfy a length heuristic.

## Rollback rule

- Stage-14 exposition regression → normally reopen Stage 13.
- Architecture/design failure → reopen Stage 10.
- Any repair requiring new substantive theory, evidence, novelty, or claim scope → reopen the earliest affected research stage.

## Version classification

Minor-version class: **v2.5 exposition architecture / streamlining hardening**.
