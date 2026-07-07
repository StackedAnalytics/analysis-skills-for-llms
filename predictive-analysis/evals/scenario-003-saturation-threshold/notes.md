# Scenario 003 — Notes & reference results

## Provenance

Seeded from the third real side-by-side test (July 2026), same client
warehouse family as scenarios 001–002: a saturation-threshold forecast
("at what spend does the return ratio fall below 2?") run baseline vs.
skills. Anonymized per the standing rule.

## Context condition

**Context-loaded.** Both reference runs had a client context repository
available (warehouse conventions, channel scopes, measurement history) —
visible in both outputs (ramp-month handling, channel scope precision,
reporting-basis awareness). Scores are **not comparable** to the
zero-context scenarios 001–002. Log the condition with every future run.

## Reference results (seeding run, 2026-07, context-loaded)

| Run | M1 | M2 | M3 | M4 | M5 | M6 | M7 | MUST | SHOULD |
|---|---|---|---|---|---|---|---|---|---|
| Baseline (no skills) | ~✓* | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | **FAIL (5/7)** | 2/7 (S1 S3) |
| Treatment (skills, pre-refinement) | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | **FAIL (6/7)** | 6/7 (S2–S7) |

\* Baseline published extrapolated spend thresholds but labeled them as
assumption-driven with anchor sensitivity — a soft pass; headline
placement of the range is the demerit that keeps it soft.

## What the seeding run taught us

**Both conditions failed M2 — the silent basis, third skill in a row.**
The two runs' revenue-per-lead figures for the search channel agreed
within ~6%; for the social channel they differed ~7×, flipping the verdict
between "huge cushion" and "never clears the threshold." The treatment ran
an admirable sensitivity on a *different* axis (booked vs. completed
value) while never mentioning the rival conversion model in the same
warehouse; the baseline used that model and never mentioned the cohort.
Notable: a hardening audit one iteration earlier had examined this skill
and declared its baseline machinery sufficient — the field overruled the
audit. (Hence the amendment to design principle 6: lessons transfer by
default; exemption requires argument and stays on watch.)

Also notable, both directions: the treatment's core move — refusing to
fabricate a spend number and converting the question into a unit-cost
guardrail with tripwires (M1+M6) — is the pattern this scenario now
canonizes; and the baseline contributed the marginal-vs-average
distinction (S1), imported into the skill from the run that lost.

Refinements adopted (live 2026-07), with regression tests:

1. **Conversion-model auxiliary-basis rule** (Stage 2), incl. per-segment
   rival checking and input-audit routing — regression test **M2**.
2. **Marginal-vs-average guidance** for scaling decisions (Stage 1) —
   regression test **S1**.

Success condition for a future treatment run: 7/7 MUST with S1 picked up,
holding SHOULD at ≥6/7.

## Results log (append rows; don't rewrite history)

| Date | Run description | Context | MUST | SHOULD | Notes |
|---|---|---|---|---|---|
| 2026-07 | Baseline, default behavior | context-loaded | 5/7 FAIL | 2/7 | silent basis (forecast model); no naive benchmark; marginal insight won |
| 2026-07 | Treatment, skills pre-refinement | context-loaded | 6/7 FAIL | 6/7 | silent basis (matured cohort); guardrail conversion exemplary |
