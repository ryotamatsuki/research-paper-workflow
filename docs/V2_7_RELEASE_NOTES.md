# research-paper-workflow v2.7 — Release Notes

Date: 2026-10-06  
Release class: **MINOR**

## Summary

v2.7 is the stable release that consolidates the post-v2.2 minor refinements already merged into `main` and closes their version-status ambiguity.

It preserves the v2 Stage architecture, canonical verdict semantics, routing, rollback rules, theory-freeze meaning, and submission-freeze meaning.

The release consolidates:

- **v2.3-class** journal-candidate-universe completeness at Stage 12;
- **v2.4-class** economic portability / falsification hardening at Stage 7.5A and its Stage-12 handoff;
- **v2.5-class** exposition architecture / streamlining hardening across Stages 7/10/13/14;
- **v2.6-class** AI provenance / human-accountability hardening from Stage 0 onward and before theory/submission freeze;
- **v2.7** reviewer-verifiability / proof-exposition hardening across Stages 10/11/13/14.

## Canonical rule added at v2.7

> **Compress routine algebra; preserve proof-critical bridges.**

For theorem-bearing or technically dense work, correctness and reproducibility are not enough. A competent specialist referee must be able to identify and audit the proof-critical chain from primitives/evidence to intermediate objects, equilibrium/welfare/certificate targets, and the headline result.

## Compatibility

v2.7 is MINOR because all post-v2.2 refinements strengthen checks and evidence obligations inside the existing Stage architecture. No canonical Stage is added, removed, merged, renumbered, or rerouted, and `GO / CONDITIONAL GO / NO-GO` semantics are unchanged.

## Migration

Active projects should use v2.7 as the canonical workflow reference. Previously completed stages remain interpretable, but re-audit is required when a new v2.3–v2.7 obligation is material to an unresolved or not-yet-frozen claim.

Stable historical tags remain immutable.
