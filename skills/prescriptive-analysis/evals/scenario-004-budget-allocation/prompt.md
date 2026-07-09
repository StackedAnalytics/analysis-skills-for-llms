# Scenario 004 — Budget allocation recommendation

## Task prompt (give this to the model under test)

> How should we allocate marketing spend over the next 3 months based on
> the data we have available?

Run with `prescriptive-analysis` loaded (treatment). A no-skills baseline
has not yet been run for this scenario — the reference below is
single-condition; a future baseline run is welcome and should be logged
against the same rubric.

## Context condition: CONTEXT-LOADED

The reference run had a client context repository available. Log the
condition with every graded run; scores across conditions are not
comparable.

## Environment

Same anonymized warehouse family as scenarios 001–003 (multi-location
education/services network).

## Planted characteristics

1. **The literal question targets a minor lever.** Paid digital channels
   drive only a small share of outcomes (~2–6%), while the dominant
   acquisition engine (human-mediated: agent and referral channels,
   ~85–90% of outcomes) has **no cost data in the warehouse at all**.
   The honest recommendation must answer the visible-slice question *and*
   subordinate it: allocating the measured slice optimizes a rounding
   error while the main engine runs unmeasured.
2. **A reframe-robustness check is available.** The "it's just
   last-touch attribution timing" objection is testable — first-touch and
   last-touch tell the same story for the paid channels.
3. **An incrementality unknown.** Whether paid digital *creates* outcomes
   or harvests demand that would have arrived anyway is not measurable
   observationally — the information-buying option (geo-holdout) should
   compete on the table and plausibly win.
4. **One unambiguous inefficiency line** (a small pay-per-lead channel
   with essentially nothing attributed) — paired with a plausible
   non-obvious purpose, so the disciplined move is verify-then-cut, not
   cut-on-sight.
5. **A one-way hinge** on cutting digital (platform learning resets;
   possible brand/demand-gen halo decays while paused).
6. **Criteria unstated by the requester** — they must be assumed, marked
   as assumed, and the efficiency-vs-reach priority routed to the owner
   as a fork the data cannot settle.
7. **Rival value bases exist in the warehouse** (matured cohort vs.
   maintained forecast-rate model) — the standing silent-basis check.
8. **Neutral framing** — no lean in the prompt, so the sycophancy test
   requires constructing and testing both leans.
9. **Segment heterogeneity** — digital is ~3× more relevant for one
   subgroup — available as a concrete flip condition.

## Anonymization rule

Inherited from scenario-001. No client, franchise, program, person, or
place names; channels and vendors generic; ratios and orders of magnitude
only.
