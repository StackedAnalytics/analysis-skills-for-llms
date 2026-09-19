---
name: causal-impact
description: >
  Structured method for estimating the causal effect of a known intervention —
  "did X work," "what was the impact of Y," "how much lift did Z drive,"
  "prove the campaign/feature/rebrand/price change moved the metric." Use this
  skill whenever a cause is named and its effect must be measured or defended,
  including A/B test analysis, pre/post comparisons, campaign measurement,
  incrementality questions, and any request containing causal verbs (drove,
  caused, resulted in, boosted, reduced) applied to an intervention. Do NOT
  use when the effect is known and the cause is unknown (use
  root-cause-analysis) or for open-ended pattern hunting (use
  exploratory-data-analysis).
---

# Causal Impact

## Why this skill exists

This is the forward-causal complement to root-cause analysis. RCA starts from an observed effect and hunts the unknown cause; this skill starts from a known candidate cause — a campaign, feature, rebrand, price change — and estimates its unknown effect. Teams call this "determining causality," "measuring impact," or "incrementality." It is the highest-stakes analysis type in the taxonomy, because its outputs justify budgets, and it is where an unscaffolded LLM does its most confident damage.

The core failure is **counterfactual blindness**. A causal effect is, by definition, a comparison: what happened, versus what *would have happened without the intervention*. That second quantity — the counterfactual — is invisible, directly unmeasurable, and must be deliberately constructed. LLMs skip the construction entirely: asked "what was the impact of X," the model computes a before/after delta and calls it the effect. No counterfactual, no confound check — a difference wearing a causal costume.

Three sub-failures compound it:

- **Free causal verbs.** Fluency makes "drove," "boosted," "resulted in" costless to generate from purely observational data. The linguistic slide from correlation to causation happens mid-sentence, without any analytical event corresponding to it.
- **Method theater.** The model will name a legitimate technique — difference-in-differences, synthetic control — and apply it without checking the assumptions that make it valid. This is *worse* than naive analysis: it launders a weak claim through impressive vocabulary, and the reader's skepticism, which raw pre/post would have triggered, stands down.
- **Sycophantic causality.** Impact requests arrive wanting a particular answer ("show that the campaign worked"). The model finds it. Combined with method theater, this produces rigorous-looking confirmations of whatever the requester hoped.

The scaffold below externalizes the state the model cannot hold — the counterfactual as an explicit construct — and permanently attaches to every conclusion the strength of the design that produced it. The governing principle: **the deliverable is the strongest claim the data actually supports, labeled with its strength — not the claim the requester asked for.**

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] Claim class needed + framing pressure noted
- [ ] Counterfactual sentence written explicitly; rival constructions enumerated (effect construction-conditional if they disagree)
- [ ] Confound inventory: co-timed changes + selection into treatment
- [ ] Design rung chosen; every checkable assumption checked
- [ ] Falsification tests run (placebo / unaffected outcomes / dose-response / specification)
- [ ] Conclusion phrased at its rung; upgrade path stated
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Classify the claim needed (before choosing any method)

Consume the Refined Question Brief if one exists; if none does, run the question-refinement triage (INFER / DECLARE / ASK) inline first — for a clear impact question a one-line DECLARE is enough. Establish what strength of claim the *decision* actually requires — many "impact" requests don't need causal proof:

- **Decision needs a defensible point estimate** (budget justification, incrementality-based bidding, pricing): full causal workup required.
- **Decision needs a direction or a bound** ("is it plausibly positive?", "is the effect at least break-even?"): a bounded or ceiling estimate may suffice — cheaper and more honest than a shaky point estimate.
- **Decision needs neither** (post-hoc narrative, curiosity): say so, and offer descriptive results with causal language withheld. Do not build a causal apparatus for a question that descriptive evidence answers.

Also surface the **desired-answer pressure** now: if the request phrasing presupposes the conclusion ("show that…", "quantify the success of…"), note it in the output as a framing risk and proceed symmetrically — the analysis must be equally capable of returning "no detectable effect."

**Artifact required:** claim class needed, decision it feeds, and any noted framing pressure.

## Stage 2 — State the counterfactual, explicitly

Write the sentence. It is mandatory, and it is the skill's central artifact:

> "The effect of [intervention] is measured against [specific construction of what would have happened without it]."

Candidate constructions, roughly strongest to weakest: a randomized control group; an untreated comparison group (region, cohort, platform); the unit's own pre-period *projected forward* (trend/seasonal model, not raw average); a synthetic composite of untreated units; last resort, an assumed flat baseline — which must be labeled as an assumption, not a measurement.

Rules:

- **No counterfactual, no causal claim.** If no defensible construction exists (intervention hit everyone at once, no pre-period, confounded launch), that is the finding. State it plainly and route to bounded/adjacent claims (Stage 6) rather than manufacturing certainty.
- **A raw pre-period average is not a counterfactual** when trend or seasonality exists — "compared to the prior 4 weeks" silently assumes the world would have stood still. Project the counterfactual; don't freeze it.
- **Rival constructions get enumerated, not buried.** When more than one credible construction exists (an untreated comparison group *and* a projected own-baseline, say), estimate against both where feasible. If they materially disagree, the effect is reported **construction-conditional** — a range across constructions, not a point from the favored one — and reconciling the constructions becomes a named step. The counterfactual is this analysis's auxiliary basis; committing to one silently when a credible rival changes the answer is the "silent basis" failure in causal clothes.

**Artifact required:** the counterfactual sentence, why this construction is the strongest available, and the credible rival constructions with a note on whether they agree.

## Stage 3 — Confound inventory

Before estimating anything, enumerate what else could produce the observed difference. Two lists:

1. **Co-timed changes** — everything else that changed around the intervention window: other campaigns, pricing, seasonality, holidays, site changes, platform algorithm shifts, tracking/definition changes (run the measurement-artifact check from the RCA categories — an "effect" that is a tag change is depressingly common).
2. **Selection into treatment** — for non-randomized designs: what determines who/what got treated? Retargeted users were selected *because* they were likely to convert; stores chosen for the pilot were chosen for a reason; users who adopted the feature differ from those who didn't. Selection is the default explanation for observational "effects" and must be argued away, not ignored.

**Artifact required:** the two-list inventory, each item marked addressed-by-design / adjusted-for / unaddressed.

## Stage 4 — Choose the rung: the design ladder

Identify the **strongest feasible design given the data**, and permanently label the conclusion with its rung. The rung label is to causal claims what the status label is to EDA findings — it travels with the number forever.

| Rung | Design | Load-bearing assumptions (state and check) |
|---|---|---|
| **1 — Randomized** | A/B test, geo experiment, holdout | Valid randomization (check covariate balance); no interference/spillover between groups; no peeking-driven stopping; sample sized for the effect you care about |
| **2 — Quasi-experimental** | Difference-in-differences; regression discontinuity; interrupted time series; synthetic control | DiD: parallel pre-trends (plot them — this is checkable). RD: no manipulation of the cutoff. ITS: stable pre-trend model, no co-timed shocks. Synthetic: credible donor pool, good pre-period fit |
| **3 — Adjusted observational** | Regression / matching / propensity on treated vs. untreated | *All* relevant confounders observed and correctly modeled — an untestable assumption; say so out loud. Overlap between groups |
| **4 — Raw pre/post** | Before vs. after, no comparison group | The world would have stood still absent the intervention — almost never true; results are directional at best |

Rules:

- **Climbing beats adjusting.** A feasible rung-2 design (an unlaunched region, a staggered rollout, a hard eligibility cutoff) beats elaborate rung-3 modeling. Look for natural experiments in the rollout before reaching for regression.
- **Assumptions are named and checked, not name-dropped.** Using DiD without plotting pre-trends is method theater, and the skill treats it as a violation, not a shortcut. Every checkable assumption gets checked; every uncheckable one gets stated as an assumption in the conclusion.
- **Rung 4 never yields causal verbs.** Its output is phrased as "the metric was X% higher post-launch" with the co-timed confound list attached — never "the launch drove X%."

**Artifact required:** chosen rung with justification, the assumption checklist with check results.

## Stage 5 — Falsification tests

Before reporting any effect, actively try to break it. These are cheap and models never run them unprompted:

- **Placebo timing:** apply the same method to a date when nothing launched. A "significant effect" at a placebo date means the method is finding noise or trend, not impact.
- **Unaffected outcomes:** the intervention shouldn't move metrics it has no mechanism to touch. A campaign that "lifted" conversions in a region it never ran in is measuring seasonality.
- **Dose-response coherence:** where exposure varies, the effect should track it (more exposure → more effect). Flat dose-response with a big average "effect" is a selection-story tell.
- **Robustness of specification:** does the estimate survive reasonable alternative windows, control sets, model choices? An effect that appears in exactly one specification was found by the garden of forking paths, not by the intervention.

A candidate effect that fails falsification is downgraded or discarded *before* the conclusion is written — not footnoted after.

**Artifact required:** falsification results (which tests ran, which passed, which weren't possible).

## Stage 6 — Conclude at the strength earned

The conclusion must contain all of these:

1. **The estimate, phrased at its rung.** Rung 1–2 with clean checks: causal language permitted, with confidence interval. Rung 3: "consistent with an effect of X, assuming no unobserved confounding." Rung 4: descriptive phrasing only. When the design is weak, prefer **bounds and ceilings** to point estimates: "after removing the tracked paid contribution and seasonal baseline, at most X remains attributable to the intervention" is honest and usually decision-sufficient.
2. **The counterfactual sentence, restated.** The reader must see what the effect is measured against.
3. **Assumption ledger:** what the conclusion assumes, what was checked, what is uncheckable.
4. **Falsification summary.**
5. **The upgrade path:** what would earn a stronger claim next time — a holdout in the next flight, staggered rollout, geo split. Causal confidence is usually *designed in advance*, not extracted after the fact; the most valuable long-term output of a weak-design analysis is the design for the next one.
6. **If the finding is "no detectable effect" or "not answerable as scoped," say it plainly.** The skill must be symmetric: an analysis that can only ever confirm is an instrument of sycophantic causality. Where no design is feasible at all, the Bradford Hill lens (strength, consistency across segments/markets, temporality, dose-response, plausible mechanism) can structure an honest "how much does this *behave* like causation" narrative — labeled as exactly that.

## Anti-patterns (self-check before delivering)

- **The costume delta.** A before/after difference presented as an effect. If the counterfactual sentence is missing, whatever follows is not a causal estimate.
- **Free causal verbs.** "Drove/caused/boosted" attached to rung-3/4 evidence. Verbs must match the rung.
- **Method theater.** Naming a quasi-experimental method without checking its assumptions. Plot the pre-trends or don't say "difference-in-differences."
- **Sycophantic symmetry failure.** An analysis structurally incapable of returning "it didn't work." Check: if the effect were zero, would this workup have detected and reported it?
- **Selection amnesia.** Comparing adopters to non-adopters, retargeted to not-retargeted, pilot stores to others — without confronting why the treated were treated.
- **Point-estimate machismo.** Reporting "the campaign drove 14.2% lift" from a design that supports "plausibly positive, at most ~20%." Bounds are not weakness; unsupported precision is.
- **Post-hoc rescue.** When the planned analysis shows nothing, slicing until some segment shows an "effect." That's the forking-paths failure wearing a causal costume; segment effects need the same falsification gauntlet, plus the multiple-comparisons disclosure.
- **Ignoring the artifact hypothesis.** The most mundane "effect" in analytics is a measurement change coinciding with the launch. Check the tracking timeline before celebrating.

## Output format

```
# Causal impact: [intervention] → [outcome]

## Claim needed & framing
[claim class · decision it feeds · framing-pressure notes]

## Counterfactual
[the sentence · why this construction is the strongest available ·
 rival constructions and whether they agree]

## Confound inventory
[co-timed changes · selection into treatment · each: addressed/adjusted/unaddressed]

## Design & assumptions   [RUNG N]
[design chosen · assumption checklist with check results]

## Falsification
[placebo / unaffected outcomes / dose-response / specification robustness]

## Conclusion   [RUNG N]
[estimate or bound, phrased at rung strength · assumption ledger ·
 what would earn a stronger claim next time]
```

For lightweight cases the format compresses, but three elements are never optional: the counterfactual sentence, the rung label on the conclusion, and causal verbs matched to the rung.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| The counterfactual sentence | "compared to what would have happened anyway — here's how we constructed that" |
| Rung 1–2 (checks passing) | "test-quality (or close to it) evidence — this supports a causal claim" |
| Rung 3 | "consistent with an effect of X, if nothing unmeasured explains the difference" |
| Rung 4 | "before-and-after only — directional at best, not proof" |
| Falsification tests | "we actively tried to break this result — here's what survived" |
| Construction-conditional effect | "the estimate depends on which comparison you trust: under A it's X, under B it's Y — here's how to settle it" |
| Upgrade path | "how to get a definitive answer next time (design it in before launch)" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"what about the rollout, the data, or the metric would a skeptic poke at that no falsification test covered?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
