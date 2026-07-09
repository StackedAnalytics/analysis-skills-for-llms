# Scenario 002 — Two-channel ROI comparison

## Task prompt (give this to the model under test)

> Over the last three months we have increased spend in our two paid channels
> — a search platform and a social platform. Do a descriptive and comparative
> analysis of these two channels across that timeframe.

Run once **without** the `comparative-analysis` (and `descriptive-analysis`)
skills loaded (baseline) and once **with** them (treatment). Grade against
`rubric.md`. This scenario assumes warehouse access with the characteristics
below (the original run followed scenario-001's warehouse; the same
anonymization rule applies — see that scenario's `prompt.md`).

## Planted characteristics

1. **A clean spend layer.** Both channels' spend/click/impression tables
   reconcile exactly; the disagreement surface is entirely downstream.
2. **An entity-scope trap.** A third spend component (a call-center program)
   is arguably part of the search channel — a defensible claim exists that
   it is entirely search-driven — and is roughly a sixth of that channel's
   total. Including or excluding it is a material scope decision that must
   be made explicitly, not inherited from table structure.
3. **Two funnel grains that disagree.** Conversions can be counted via a
   contact-grain table or via an inquiry×contract bridge that fans out
   (multi-match); the two methods disagree by ~4× on landed conversions for
   the social channel in-window. Any method must be stated and deduped.
4. **Right-censored recent cohorts.** In-window conversion is immature for
   both channels (weeks-to-months lag); judging on landed rates alone is
   invalid.
5. **THE CENTERPIECE — two credible auxiliary bases that flip the verdict.**
   The warehouse contains (a) a matured historical cohort implying rough
   value-per-lead parity between channels, and (b) a maintained
   forecast-rate model implying the search channel's leads are worth ~6–7×
   the social channel's. Under (a) the social channel wins on ROAS; under
   (b) the search channel wins decisively. Neither basis is self-evidently
   correct from inside the warehouse — and external client knowledge (not
   visible in the data) bears on which is trustworthy.
6. **Non-commensurable platform metrics.** Platform-reported conversions
   are defined differently per platform (one blank in the warehouse, one
   counting actions not people); impressions/CPM/CTR compare a search ad
   product to a social one and are not head-to-head comparable.
7. **An intra-quarter regime shift** in the search channel: impressions
   roughly halve while CPM triples and CTR jumps, visible only at monthly
   granularity.
8. **An intra-quarter divergence** in the social channel: lead volume
   declines on roughly flat spend (cost-per-lead rising into quarter end) —
   a saturation/fatigue signal, also monthly-only.
9. **A geography stratification** that confirms the cheaper channel's lead
   cost advantage within every adequately-sized region (no mix reversal),
   with one tiny-n region cell as ranking bait.
10. **Asymmetric-but-symmetric attribution.** Channel tagging is
    self-reported/low-click-verified for both channels — weak absolutely,
    fair comparatively; the caveat must be carried, not used to dodge.

## Anonymization rule

Inherited from scenario-001: no client, location, franchise, person, or
program names; platforms referred to generically (search/social); no exact
revenue figures — ratios and orders of magnitude only.
