---
name: predictive-analysis
description: >
  Structured method for forecasting and projection — "what should we expect,"
  "will we hit the target," "project Q4," pacing questions ("are we on track"),
  demand/lead/revenue forecasts, and any request for a future number. Use this
  skill whenever the deliverable is an expectation about the future, even when
  phrased casually ("where do we land this month?"). Do NOT use for estimating
  what an intervention caused (causal-impact), for choosing between options
  (comparative/prescriptive), or for explaining a past change
  (root-cause-analysis).
---

# Predictive Analysis

## Why this skill exists

Prediction is where an LLM's fluency is most seductive and least earned. Asked "where will we land this quarter," the model produces a single confident number wrapped in a plausible story. Four failures hide inside that answer:

- **The naked point estimate.** A forecast without an interval is not a forecast; it is a guess wearing a suit. The decision consuming the forecast almost always depends more on the *range* ("could we plausibly miss by 20%?") than the center — yet the model volunteers only the center, because a point is what the question's grammar requested.
- **Recency overfit.** The last few data points get treated as *the trend*. Two strong weeks become a growth story; a holiday dip becomes decline. Extrapolating the most recent slope is the model's default because recent tokens dominate its attention, and it is the single most common way real-world forecasts embarrass their authors.
- **Narrative smoothing (the inside view).** The model builds the forecast from the specifics of the situation — the plans, the pipeline, the enthusiasm in the prompt — rather than from how similar periods have actually turned out. This is Kahneman and Tversky's planning fallacy, automated: inside-view forecasts are systematically optimistic and systematically overconfident, because the story of how things go right is easier to generate than the distribution of how things usually go.
- **The unbeaten naive.** Decades of forecasting competitions (Makridakis's M-series) established an embarrassing result: simple baselines — last year same period, seasonal naive, recent run-rate — beat sophisticated methods remarkably often. A forecast that has not been compared to the naive baseline has not demonstrated it adds anything; the model never runs that comparison unprompted, because sophistication *feels* like diligence.

The scaffold inverts the model's instincts: **outside view before inside view, intervals before points, naive baselines as the burden of proof, and every adjustment to the baseline itemized and priced.** The story is allowed into the forecast only after it has been decomposed into named, sized, evidenced components.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] Frame: decision / horizon / error-cost asymmetry / forecast-vs-target split
- [ ] Outside view: reference class + at least two naive baselines computed; conversion-model basis named, rivals enumerated
- [ ] Decomposition done: trend (long vs recent), seasonality, known future events, regime check
- [ ] Adjustment ledger itemized and symmetry-checked
- [ ] Interval stated with basis; method backtested against naive
- [ ] Revision triggers set; forecast logged for later scoring
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Frame: decision, horizon, and the cost of being wrong

Consume the Refined Question Brief if one exists; if none does, run the question-refinement triage (INFER / DECLARE / ASK) inline first — for a clear forecasting request a one-line DECLARE is enough. Establish:

1. **What decision consumes this forecast**, at what granularity and horizon. A staffing decision needs monthly resolution; a pacing check needs "on/off track with what confidence." Scaling decisions ("how much more can we spend/produce/hire before returns break") need the **marginal** quantity, not the average: under diminishing returns, marginal return ≈ elasticity × average return, so a healthy blended average can hide a next-unit return already at or below the threshold. If the decision is about the next dollar, forecast the next dollar — and say plainly when only an experiment can measure it.
2. **Asymmetric error costs.** Which direction of wrong is worse? Overforecasting leads means overstaffed admissions; underforecasting inventory means stockouts. The *reported* number can legitimately sit off-center of the distribution when costs are asymmetric — but that choice is made explicitly, not smuggled.
3. **Forecast vs. target.** A forecast is an expectation; a target is an aspiration. Requests routinely conflate them ("forecast us hitting 2,400"). Untangle: the forecast is what the evidence says; the gap to target is a separate, useful output. A forecast bent toward the target corrupts both numbers.

**Artifact required:** one sentence each — decision, horizon/granularity, asymmetry, and the forecast/target distinction if live.

## Stage 2 — Outside view: reference class and naive baselines first

Before touching the specifics of *this* quarter/campaign/launch, establish what history says about periods like it:

- **Reference class:** how have comparable periods actually turned out? (Same quarter in prior years; similar campaigns; similar launches.) Note the spread, not just the average — the reference class's variance is the first honest estimate of forecast uncertainty.
- **Naive baselines, computed, minimum two:**
  - *Seasonal naive:* same period last year (× known structural growth if defensible).
  - *Run-rate:* current pace extrapolated with seasonal shape, not straight-line.
  - Optionally *drift:* last year + recent average growth.
- **The baselines are the anchor and the burden of proof.** Every departure from them in later stages must be justified by named evidence. If the final forecast differs wildly from all baselines, either something identifiable and large is happening — or the inside view has taken over.
- **Conversion models are auxiliary bases — enumerate their rivals.** When the forecast quantity reaches the decision through a conversion model (revenue-per-lead, LTV, margin or take rates, a maturity curve), that model is an auxiliary basis of the entire forecast, exactly like a comparison basis or a counterfactual construction. Name it, and enumerate the credible rivals present in the data or the business (a matured-cohort estimate *and* a maintained forecast-rate model, say). Enumeration is an active search, not a recall prompt: check the warehouse for maintained rate, forecast, LTV, or attribution model tables (rate dimensions, model-output tables, semantic-layer measures) before concluding no rival basis exists — a rival sitting in a dimension table has been missed by every field run that didn't go looking. Rivals can agree for one segment and diverge wildly for another — check per segment, not just in aggregate. If rivals materially disagree — above all if they change the decision — the forecast is reported **basis-conditional** ("on basis A the channel clears the threshold with room to spare; on basis B it never does"), and resolving the basis becomes a named step. Which basis is trustworthy is frequently client knowledge the data cannot supply; the next-cheapest resolution is an audit of each basis's own inputs, which can collapse the fork before any experiment.

**Artifact required:** the reference class with its spread, the computed baselines, and — where a conversion model is used — the named basis with its enumerated rivals.

## Stage 3 — Decompose the series

Separate what is *structural* from what is *assumed*:

- **Trend** — and be suspicious of it: fit it on the full relevant history, not the last month. State what the recent slope looks like vs. the longer trend; if they disagree, that disagreement is a finding to explain, not a license to pick the flattering one.
- **Seasonality and calendar** — weekly/monthly shape, holidays, academic calendars, fiscal effects, number-of-weekdays quirks.
- **Known future events** — planned campaigns, price changes, site launches, closures, a campaign *ending* (the recency trap's favorite hiding place: a spike that is scheduled to stop gets extrapolated as growth). List them with dates.
- **Regime checks** — has anything structural changed that makes history a bad guide (tracking changes, definition changes, a new channel, a market shift)? A measurement change mid-history will masquerade as trend; run the artifact check before fitting anything through it.

**Artifact required:** the decomposition notes and the known-future-events list.

## Stage 4 — Inside-view adjustments: itemized, signed, sized, evidenced

Now — and only now — the specifics of the situation are allowed to move the number. Every adjustment to the baseline goes in a ledger:

| Adjustment | Direction | Size | Evidence |
|---|---|---|---|
| e.g., "paid campaign runs 3 more weeks" | + | +180 leads | current campaign daily rate × remaining days |
| e.g., "that campaign then ends" | − | −60/wk thereafter | pre-campaign baseline |

Rules:

- **No un-ledgered adjustments.** If the final number differs from baseline-plus-ledger, the difference is narrative smoothing by definition — find it and either price it or delete it.
- **Adjustments need evidence, not vibes.** "Momentum," "the team is confident," and "pipeline looks strong" are not ledger entries until converted into a rate, a count, or a documented commitment.
- **Symmetry check:** inside views generate upside adjustments far more fluently than downside ones. For every positive entry, ask what the corresponding downside entries are (campaign fatigue, capacity limits, the thing ending). A ledger that is all pluses is a story, not an analysis.

**Artifact required:** the adjustment ledger.

## Stage 5 — Uncertainty as a first-class output

The deliverable is a distribution communicated honestly, not a number:

- **Interval, always.** A central estimate plus a range at stated coverage ("80% interval: X–Y"). Prefer *empirical* intervals — derived from the errors the same method makes on past periods (Stage 6) — over intervals asserted from feel.
- **Intervals widen with horizon.** A quarter-out range should be visibly wider than a week-out range; if it isn't, the uncertainty is understated.
- **Scenario bounds for lumpy risks.** Discrete events (a deal closing or not, a campaign approved or not) don't average well — present branched scenarios rather than smearing them into one blurry midpoint.
- **Two failure modes, both named:** the naked point (no interval) and the **CYA interval** — a range so wide it can't be wrong and can't be used. The interval must be tight enough to inform the Stage 1 decision or the honest statement is "this horizon isn't forecastable at decision-useful precision."

**Artifact required:** central estimate + interval with stated coverage and basis (empirical / asserted), scenarios where applicable.

## Stage 6 — Backtest: would this method have worked?

Before shipping, apply the exact method (baseline + decomposition + ledger logic) to past periods where the answer is known:

- Roll through several held-out periods; record the errors.
- **Compare against the naive baselines.** If the method doesn't beat naive on held-out history, *ship the naive forecast* and say so — that is a respectable, honest result, not a failure.
- Use the backtest error distribution to set the Stage 5 intervals empirically.

**Artifact required:** backtest summary — method error vs. naive error, and the derived interval basis.

## Stage 7 — Deliver with triggers, and close the loop

1. **The forecast contract:** central + interval + the assumptions ledger it rests on (so when an assumption breaks, everyone knows the number moved *because of that*, not because the forecast was "wrong").
2. **Revision triggers, not revision schedules:** "if week-4 cumulative pace falls below X, the 80% interval no longer contains the target — revise and escalate." Pre-committed triggers prevent both panic-revising on noise and complacent staleness.
3. **Score it later.** Log the forecast and its interval now; when the period closes, record the outcome and whether the interval contained it. Calibration only improves if forecasts are scored — an unscored forecast teaches nothing, and a forecaster whose 80% intervals contain the truth 40% of the time needs to know that more than they need a better model.

## Anti-patterns (self-check before delivering)

- **The naked point.** A future number with no interval. Not a forecast.
- **The CYA interval.** A range designed to be unfalsifiable rather than useful.
- **Recency extrapolation.** The last 2–4 data points' slope presented as the trend; a scheduled-to-end spike projected as growth.
- **Inside-view takeover.** A forecast far from every baseline with no ledger entries explaining the gap — the story is doing the forecasting.
- **All-plus ledger.** Adjustments that only ever move the number toward the hoped-for outcome. Run the symmetry check.
- **The unbeaten naive.** Shipping a method that was never tested against "same as last year, seasonally shaped."
- **Forecast-target contamination.** Bending the expectation toward the aspiration. Report the forecast, the target, and the gap as three separate facts.
- **Straight-line growth.** Extending a growth rate indefinitely without a saturation or capacity argument.
- **The unscored forecast.** No logging, no later comparison to actuals — guaranteeing the same calibration errors forever.

## Output format

```
# Forecast: [quantity] for [period]

## Frame
[decision · horizon/granularity · error-cost asymmetry · forecast vs. target]

## Outside view
[reference class + spread · naive baselines · conversion-model basis + rivals
 (basis-conditional forecast if they disagree)]

## Decomposition & known events
[trend (long vs. recent) · seasonality/calendar · scheduled events · regime checks]

## Adjustment ledger
[itemized: direction, size, evidence · symmetry check noted]

## Forecast
[central + interval (coverage, basis) · scenarios if lumpy ·
 vs. target gap if applicable]

## Backtest & triggers
[method vs. naive on held-out periods · revision triggers ·
 scoring plan]
```

For lightweight pacing checks the format compresses, but three elements are never optional: at least one naive baseline, an interval with stated basis, and the adjustment ledger for any departure from baseline.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| Naive baseline | "the simple benchmark — same as last year, seasonally adjusted — which any forecast has to beat" |
| Adjustment ledger | "what we added and subtracted from the benchmark, and the evidence for each" |
| 80% interval (empirical) | "we'd expect to land between X and Y roughly four times out of five, based on this method's actual track record" |
| Backtest vs. naive | "we tested the method on past periods where we know the answer" |
| Revision trigger | "if we're below X by [date], the forecast no longer holds — that's the tripwire" |
| Forecast vs. target split | "the forecast, the target, and the gap — three separate facts" |
| Basis-conditional forecast | "the answer depends on which value model you trust — on A it's X, on B it's Y; here's how to settle which" |
| Marginal vs. average return | "the average looks healthy; the question is what the *next* dollar returns — usually lower, and only a test measures it" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"what in the history looks strange that no baseline or ledger entry needed — breaks, sentinels, impossible weeks?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
