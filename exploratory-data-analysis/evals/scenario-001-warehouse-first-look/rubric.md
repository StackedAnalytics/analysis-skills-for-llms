# Scenario 001 — Rubric

Two tiers. **MUST** items are the skill's core discipline: failing any one
means the run fails, regardless of how polished the output reads. **SHOULD**
items are a quality score (x/6) measuring breadth and craft. Grade against
the planted characteristics in `prompt.md`.

## MUST (pass/fail gate)

| # | Check | Maps to planted characteristic |
|---|---|---|
| M1 | Declares exploratory mode and produces a data-credentials note stating coverage boundaries (spend-history start, attribution cutover, contact-population split) | 1, 2 |
| M2 | Identifies the two-population contact table and excludes/flags the undated pool before computing any funnel or conversion rate — the diluted blended rate is never presented as *the* rate | 1 |
| M3 | Checks attribution coverage **by year**; identifies the click-level columns as ~empty historically; does **not** describe attribution as well-populated on the strength of the derived channel column | 2 |
| M4 | Screens the volume surge against benign explanations (footprint, zero-value share, unit value) and — finding none — labels it unresolved/ARTIFACT SUSPECT with a routed next step, rather than narrating it as growth | 3 (and 4 if the rate is examined) |
| M5 | No unlabeled causal or attributive language on observational cuts; the channel gradient, if reported, carries its definitional-confound caveat | 5 |
| M6 | Discloses the cuts-examined denominator and maintains a cut ledger | — |
| M7 | Every reported finding carries an epistemic status label; ARTIFACT SUSPECTs include a confirmation/routing step | — |

## SHOULD (quality score, x/6; x/7 for runs after the 2026-07 communication convention)

| # | Check | Maps to |
|---|---|---|
| S1 | Sweeps the primary entity (product/program) dimension and catches the normalization-gap bucket | 7 |
| S2 | Sweeps time at two granularities and catches the one-quarter dip | 8 |
| S3 | Identifies the placeholder-contract status specifically (not just the legacy ≤$0 concentration) | 6 |
| S4 | Reports decision-relevant nulls (e.g., the spend-table reconciliation) | 9 |
| S5 | Flags the tracking-birth boundary on the new event type | 10 |
| S6 | Cut ledger closes with a NOT-EXAMINED line naming unswept dimensions/granularities | — |
| S7 | *(runs after the 2026-07 communication convention only)* Deliverable body is plain-language: internal vocabulary translated, checklist and artifacts in a workings layer, calibration distinctions preserved in the translation | — |

## Grading notes

- The MUST tier is deliberately insensitive to thoroughness: a shorter run
  that respects all seven disciplines beats a comprehensive run that
  narrates the surge as real. That asymmetry is the point of the skill.
- S1/S2 double as regression tests for the sweep-coverage refinement added
  to the skill after the first run of this scenario (see `notes.md`) —
  they were the treatment run's misses.
- When grading future runs, append a dated row to the results table in
  `notes.md` rather than editing history.
