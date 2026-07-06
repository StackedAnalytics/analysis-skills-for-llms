# Scenario 001 — Notes & reference results

## Provenance

Seeded from a real side-by-side test (July 2026) on a live client mart:
the same first-contact prompt run once with default model behavior and once
with the `exploratory-data-analysis` skill loaded. All identifying details
removed per the anonymization rule in `prompt.md`; the planted
characteristics are the real dataset's, described generically.

## Context condition

**Zero-context.** Both reference runs were given warehouse access only — no client knowledge, no overlay files, no supplementary documentation. This isolates the skill's marginal contribution to reasoning discipline. Future runs made with an overlay or other context loaded are a **different condition**: log them, but do not compare their scores against these baselines as if the skill changed.

## Reference results (first run, 2026-07)

| Run | M1 | M2 | M3 | M4 | M5 | M6 | M7 | MUST | SHOULD |
|---|---|---|---|---|---|---|---|---|---|
| Baseline (no skill) | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **FAIL (1/7)** | 4/6 (S1 S2 S3 S5) |
| Treatment (skill) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS (7/7)** | 1/6 (S4) |

## What the first run taught us

The score pattern is the finding. The baseline was *broader* (4/6 SHOULD —
it caught the program normalization gap, the monthly dip, the placeholder
status, and the tracking-birth boundary) but failed the discipline gate in
six of seven places — most consequentially describing attribution as
well-populated (the M3 mirage) and narrating the 5× surge as real growth
(M4). Those two errors alone would have misdirected downstream reporting
and budget analysis. The treatment inverted this: perfect discipline,
narrow sweep — it never examined the program dimension or sub-yearly
granularity, and gave the reader no visibility into that boundary.

Two skill refinements were adopted directly from the treatment's misses
(both live in the skill as of 2026-07):

1. The cut ledger now requires a closing **NOT-EXAMINED line** (S6), making
   sweep-coverage gaps visible scope decisions.
2. The segment pass now defaults to the business's **primary entity
   dimensions**, and the time pass requires **two granularities** (S1/S2
   as regression tests).

A future treatment run should therefore hold 7/7 MUST while pulling the
SHOULD score up toward the baseline's breadth — that convergence, not
either single score, is the success condition for the skill.

## Results log (append rows; don't rewrite history)

| Date | Run description | Context | MUST | SHOULD | Notes |
|---|---|---|---|---|---|
| 2026-07 | Baseline, default behavior | zero-context | 1/7 FAIL | 4/6 | pre-refinement skill era |
| 2026-07 | Treatment, skill v0.1 | zero-context | 7/7 PASS | 1/6 | pre-refinement (no S6 rule yet) |
