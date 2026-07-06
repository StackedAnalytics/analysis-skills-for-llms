---
name: comparative-analysis
description: >
  Structured method for comparing entities or groups — "which channel/segment/
  region/campaign/vendor performs better," "rank our stores/reps/pages,"
  "compare A vs B," benchmark and league-table requests, cohort-vs-cohort
  comparisons. Use this skill whenever the task is characterizing a difference
  between groups measured observationally, even when phrased as a simple data
  pull ("show me conversion by channel" is usually a comparison). Do NOT use
  for a change over time in one entity (root-cause-analysis), for estimating
  an intervention's effect (causal-impact), or for open-ended exploration
  (exploratory-data-analysis).
---

# Comparative Analysis

## Why this skill exists

Comparison looks like the easy analysis type — compute the metric for each group, line them up, describe the gaps. That apparent ease is the trap. LLMs handed a comparison execute it *as handed*: same query, side-by-side numbers, fluent narration of whoever is on top. Three characteristic failures hide inside that fluency:

- **Composition blindness (Simpson's paradox).** Aggregate comparisons silently assume the groups have the same mix — of devices, programs, customer sizes, traffic sources. When mix differs, the aggregate gap measures the *blend*, not the performance, and can shrink, vanish, or fully reverse under stratification. The model compares aggregates by default because that's what the request's grammar asks for, and it narrates the blend as if it were performance.
- **Ranking noise (the league-table failure).** Asked to rank 30 stores/reps/pages by a rate, the model ranks raw observed rates and narrates the extremes — which, by de Moivre's equation, are systematically the *smallest-sample* entities, since variance scales with 1/√n. The top and bottom of any raw league table are where the noise lives, and next period's "most improved" is usually just regression to the mean. Models never flag this unprompted; they write the story of the flukes.
- **Unlike-for-unlike acceptance.** Comparing entities measured over different windows, at different maturities (a 2-month-old cohort's LTV vs. a 2-year-old one's), under different definitions, or with mismatched denominators. The model accepts the comparison's terms as given rather than auditing whether the two numbers are commensurable at all.

And one meta-failure that turns descriptive errors into prescriptive ones: **smuggled causality.** Groups in observational comparisons selected themselves — mobile users differ from desktop users, channel audiences differ by construction. Reading a group difference as a performance verdict ("mobile converts worse → fix the mobile site") silently assumes the group *label* causes the gap. Sometimes it does; often the gap is who's in the group.

The discipline: **a comparison is only as good as its terms.** The skill audits the terms first, decomposes mix from performance, respects sample size before narrating rankings, and firewalls description from attribution.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete:

```
- [ ] Comparability audit: definition / window / maturity / denominator / measurement
- [ ] Comparison-quantity sentence written
- [ ] Composition check: stratified results + mix/performance decomposition
- [ ] Ranking discipline applied: min-n threshold, funnel logic, regression-to-mean caveats
- [ ] Interpretation firewall: selection stories before performance stories; causal handoff if needed
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Comparability audit: are these numbers commensurable?

Before computing anything, audit the terms of the comparison. For each entity/group being compared, verify:

| Term | Check |
|---|---|
| **Definition** | Same metric definition on both sides? (Same event, same filters, same dedup — cross-*system* comparisons route to metric-reconciliation first) |
| **Window** | Same time period? Same seasonality exposure? (Comparing A's Q4 to B's Q2 compares quarters, not entities) |
| **Maturity** | Same age/tenure? Cohorts, campaigns, stores, and content all have lifecycle curves — a young entity mid-curve vs. a mature one post-curve is a *pipeline-lag* comparison, not a performance one |
| **Denominator** | Same base, correctly scoped? Rates vs. counts; per-session vs. per-user vs. per-lead; excluded populations symmetric? |
| **Measurement conditions** | Both groups equally trackable? (Consent rates, platform coverage, and bot filtering can differ *by group* — a measurement gap masquerading as a performance gap) |

Every mismatch gets fixed (re-scope the window, age-align the cohorts, normalize the denominator) or, if unfixable, **flagged as a standing caveat that survives into the conclusion**. If the entities are fundamentally incommensurable, that is the finding.

**Artifact required:** the comparability table, with each mismatch marked fixed / flagged / fatal.

## Stage 2 — Define the comparison quantity

State explicitly what is being compared, and defend the choice:

- **Rate, count, or distribution?** Totals answer "who contributes most"; rates answer "who converts best"; they rank differently and serve different decisions. Pick per the Brief.
- **Mean or median?** Skewed quantities (revenue, LTV, session depth) compared on means are comparisons of whales. Use medians/percentiles by default; compare means only when the total is what matters — and say which you're doing.
- **Absolute and relative gaps, both.** "B is 2× A" (relative) and "B exceeds A by 0.4 points" (absolute) can describe the same data and license very different reactions. Report both; small bases make relative gaps theatrical.

**Artifact required:** one sentence — "comparing [quantity], [aggregation], per [denominator], over [window], because [decision]."

## Stage 3 — Composition check: decompose mix from performance

This stage is mandatory for every comparison, not just suspicious ones — composition effects are invisible from the aggregate by construction.

1. **Identify the plausible mix drivers**: the 2–4 dimensions most likely to differ between groups *and* correlate with the metric (device, new-vs-returning, product/program mix, customer size, geography).
2. **Stratify**: compute the comparison within each stratum. Three outcomes:
   - Gap holds within strata → the difference is (descriptively) real performance; the aggregate understates or overstates it by the mix.
   - Gap shrinks or vanishes within strata → the aggregate difference is mostly **mix**. The interesting question becomes *why the mixes differ* — often a routing, targeting, or acquisition question, not a performance one.
   - Gap **reverses** within strata (full Simpson's) → the aggregate conclusion is wrong, and reporting it would drive the wrong decision. This is exactly the case the stage exists to catch.
3. **Standardize when mix differs** (borrowed from epidemiology's age-adjusted rates): recompute each group's metric on a *common reference mix*. The standardized comparison answers "how would these groups compare if they served the same blend" — usually the question the decision actually needs.
4. **Report the decomposition**: "the 3.1-point aggregate gap = 2.2 points mix + 0.9 points within-segment performance."

**Artifact required:** the stratified table and the mix/performance decomposition sentence.

## Stage 4 — Ranking discipline: respect the noise

Whenever the output ranks more than a handful of entities, or compares small groups:

- **Minimum base size before narration.** Set an explicit n threshold below which entities are reported but not ranked ("insufficient volume to distinguish from noise"). The threshold is stated, not silent.
- **Funnel logic for league tables** (Spiegelhalter): judge each entity's deviation from the overall rate *relative to its sample size* — an entity is notable when it sits outside the variability expected at its n, not when it tops a raw sort. Small entities need much larger deviations to mean anything. A funnel plot (rate vs. n with control limits) is the honest picture of a league table; produce one, or apply its logic in prose.
- **Shrink before you rank.** When ranking is unavoidable, rank estimates pulled toward the overall mean in proportion to smallness (an empirical-Bayes habit, applied roughly is fine). Raw-rate rankings systematically crown flukes.
- **Regression-to-the-mean warning, stated.** Extreme performers this period will, on average, be less extreme next period *with no underlying change*. Any "most improved / most declined" comparison across periods must carry this caveat — and before-after comparisons of entities *selected for being extreme* (coaching the worst reps, fixing the worst pages) are contaminated by it almost by definition.

**Artifact required:** stated minimum-n threshold; identification of which ranked entities are statistically distinguishable from the pack, and which are merely small.

## Stage 5 — Interpretation firewall: describe, don't attribute

The conclusion of an observational comparison is a **characterized difference**, not a verdict on merit:

1. **Selection stories before performance stories.** For each surviving gap, ask: who ends up in this group, and would they have performed differently in any group? List the selection explanations explicitly *before* any performance framing. "Email converts at 3× paid social" is mostly "email reaches people who already know us."
2. **Causal handoff.** If the decision requires knowing whether the group *label* causes the gap ("should we shift budget to the better channel?"), that is a causal question — route it to causal-impact with the comparison as the entry evidence, and say what design would answer it (a reallocation test, a holdout). Do not let a comparison quietly become a reallocation recommendation.
3. **Conclusion contract:** the finding states magnitude (absolute and relative), the mix/performance split, the uncertainty status (which gaps are distinguishable from noise), the standing caveats from Stage 1, and what the comparison *cannot* say (the selection/causal boundary).

## Anti-patterns (self-check before delivering)

- **Aggregate-only comparison.** No stratification performed. The composition check is mandatory precisely because this failure is invisible from the output.
- **League-table narration.** Writing the story of the top and bottom of a raw ranking. The extremes of any raw sort are where the small samples live.
- **Whale-mean comparison.** Comparing skewed quantities on means without saying so — a comparison of each group's biggest customers wearing a comparison-of-groups costume.
- **Tenure-blind cohort comparison.** Comparing entities at different lifecycle stages on cumulative metrics. Age-align or don't compare.
- **Relative-gap theater.** "3× better!" on a base of 40. Absolute gaps and base sizes travel with every relative claim.
- **Significance theater.** Declaring differences "significant" without a denominator of comparisons made (forking paths applies here too), or treating statistical detectability as practical importance. State whether the gap is big enough to *matter for the decision* separately from whether it's distinguishable from noise.
- **The smuggled verdict.** Sliding from "group A's rate is higher" to "group A is better" to "do more of A" in one paragraph. Each step needs its own evidence; the last one usually needs causal-impact.
- **Symmetric-measurement assumption.** Forgetting that trackability itself can differ by group. Check it (Stage 1) before crowning a winner.

## Output format

```
# Comparison: [entities] on [quantity]

## Terms of the comparison
[comparability table: definition/window/maturity/denominator/measurement —
 fixed/flagged/fatal · comparison-quantity sentence]

## Headline vs. decomposed
[aggregate gaps (absolute + relative) · stratified results ·
 mix/performance decomposition]

## Ranking reliability   (when ranking)
[min-n threshold · which entities are distinguishable from the pack ·
 regression-to-mean caveats where applicable]

## What the difference is — and isn't
[characterized difference · selection stories · causal boundary ·
 handoff to causal-impact if the decision needs attribution]
```

For lightweight cases the format compresses, but three elements are never optional: the comparability audit, the composition check, and the selection-story acknowledgment before any performance framing.
