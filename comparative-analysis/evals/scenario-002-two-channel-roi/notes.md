# Scenario 002 — Notes & reference results

## Provenance

Seeded from the second real side-by-side test (July 2026), on the same
client warehouse as scenario-001: a descriptive + comparative prompt on two
ramped paid channels, run baseline vs. skills. Anonymized per the standing
rule. This is the scenario that produced the **opposite-verdicts** result:
two competent analyses of identical data concluded opposite channel-ROI
winners, because each silently committed to a different auxiliary value
basis (matured historical cohort vs. maintained forecast-rate model).

## Context condition

**Zero-context.** Both reference runs were given warehouse access only — no client knowledge, no overlay files, no supplementary documentation. This isolates the skill's marginal contribution to reasoning discipline. Future runs made with an overlay or other context loaded are a **different condition**: log them, but do not compare their scores against these baselines as if the skill changed.

## Reference results (seeding run, 2026-07)

| Run | M1 | M2 | M3 | M4 | M5 | M6 | M7 | MUST | SHOULD |
|---|---|---|---|---|---|---|---|---|---|
| Baseline (no skills) | ✗ | ~✓* | ✓ | ✗ | ✗ | ✓ | ✓ | **FAIL (4/7)** | 4/6 (S2 S4 S5† S6) |
| Treatment (skills) | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | **FAIL (5/7)** | 5/6 (S1 S3 S4 S5 S6) |

\* Baseline surfaced the entity-scope decision explicitly (a genuine win)
but asserted its provenance ("per client") without a source — a soft pass
pending verification; graded ~✓ with the provenance clause noted.
† Baseline did not narrate spend as an outcome, passing S5 by absence
rather than by discipline.

## What the seeding run taught us

**Both runs failed M4 — the centerpiece.** The treatment obeyed every
discipline it had been given (audit, stratification, censoring bracket,
min-n, firewall — all held, and the firewall prevented the baseline's
smuggled reallocation verdict) but the skill contained no instruction to
enumerate rival auxiliary bases, so it committed to the matured-cohort
basis without mentioning the forecast-rate model sitting in the same
warehouse. The baseline committed to the forecast-rate model without
mentioning the matured cohort. Opposite silent choices → opposite
"data-driven" verdicts, both fluent, both confident.

Postscript that sharpens the lesson: external client knowledge — not
visible anywhere in the warehouse — later indicated the matured-cohort
basis was the *suspect* one. Which basis to trust was a client-knowledge
question the analysis could only have surfaced, never settled. That is
exactly what the refinement instructs: expose the fork, report
basis-conditionally, and route basis resolution as a named next step.

Two refinements adopted from this scenario (live in the skill as of
2026-07), with their regression tests:

1. **Auxiliary-basis discipline** (Stage 2 + "the silent basis"
   anti-pattern) — regression test **M4**.
2. **Entity-scope row** in the comparability audit — regression test
   **M2**, including the provenance clause.

Success condition for a future treatment run: 7/7 MUST (the two new checks
now being taught by the skill) while holding SHOULD at ≥5/6 — ideally
picking up S2, the saturation divergence the treatment's triage missed.

## Results log (append rows; don't rewrite history)

| Date | Run description | Context | MUST | SHOULD | Notes |
|---|---|---|---|---|---|
| 2026-07 | Baseline, default behavior | zero-context | 4/7 FAIL | 4/6 | silent basis (forecast model); smuggled reallocation verdict |
| 2026-07 | Treatment, skills pre-refinement | zero-context | 5/7 FAIL | 5/6 | silent basis (matured cohort); scope inherited from table structure |
