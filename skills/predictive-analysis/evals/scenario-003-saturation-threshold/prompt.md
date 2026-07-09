# Scenario 003 — Saturation threshold forecast

## Task prompt (give this to the model under test)

> At what spend level does the return ratio (revenue per dollar of spend)
> drop below 2 for our search channel and our social channel?

Run baseline vs. treatment (with `predictive-analysis` loaded) and grade
against `rubric.md`.

## Context condition: CONTEXT-LOADED

Unlike scenarios 001–002, both reference runs had a client context
repository available (warehouse conventions, channel scope definitions,
known measurement history). Scores are **not comparable** to zero-context
scenarios. Future runs should state their condition.

## Environment

Same anonymized warehouse family as scenarios 001–002 (multi-location
education/services network). Requires the characteristics below.

## Planted characteristics

1. **Short spend history** (~7 months); no year-ago frame exists.
2. **No observed saturation for the search channel** — cost-per-lead *fell*
   as spend scaled several-fold (learning/optimization dominates), so the
   question as asked is **unanswerable-as-scoped** for that channel: any
   specific spend threshold is an assumption-driven extrapolation, not a
   forecast. The social channel shows a plateau with a faint late uptick
   (weeks, not a trend).
3. **THE CENTERPIECE — a value-conversion basis fork, segment-specific.**
   Two credible bases exist in the warehouse for converting leads to
   eventual revenue: (a) a matured historical cohort, and (b) a maintained
   forecast-rate model. For the search channel they agree within ~6%. For
   the social channel they disagree by ~7× — flipping the verdict between
   "enormous cushion above the threshold" and "never clears the threshold
   at any spend level." Each basis has an identifiable input weakness
   (the cohort rests on channel tags from an unreliable-attribution era;
   the model's estimation window overlaps a poor-attribution period), so
   the fork is *shrinkable* by auditing inputs — and which basis to trust
   is partly external client knowledge.
4. **Marginal vs. average matters.** The question is a scaling decision;
   under diminishing returns the next-dollar return runs below the blended
   average (≈ elasticity × average), so an above-threshold average can
   coexist with a below-threshold marginal return.
5. **Ramp contamination.** The earliest months of spend data have an
   attribution ramp (leads undercounted → unit costs spuriously high) and
   must be excluded or explicitly handled.
6. **A second, distinct sensitivity axis:** booked vs. completed (or
   gross vs. net) contract value — separate from the basis fork and worth
   showing separately.
7. **A regime-shift early warning** in the search channel (impressions
   down sharply while unit costs rise intra-quarter) — a candidate
   saturation signal to route for diagnosis, not to narrate as one.

## Anonymization rule

Inherited from scenario-001. Channels generic (search/social); ratios and
orders of magnitude only; no client, program, person, or place names.
