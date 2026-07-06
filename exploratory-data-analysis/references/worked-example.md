# Worked Example: First Look at a Subscription Business's Usage Data

A compressed run of the EDA skill. The instructive part is Stage 3 — watch three of the five "striking" candidate findings die in the gauntlet, and note that the most valuable survivor is an ARTIFACT SUSPECT, not an insight.

**Prompt:** "We just got 18 months of product usage data joined to our billing data. Poke around and tell us anything interesting before the retention offsite."

**Brief consumed:** exploratory → (diagnostic if warranted); audience: exec offsite; "interesting" = anything bearing on retention; deadline: Friday.

---

## Stage 1 — Data credentials

- Grain: one row per account per day (usage) joined to account-level billing. 214k account-days, 1,930 accounts.
- Coverage: usage events begin **Jan 2025**, but accounts date to 2021 — usage tracking is 18 months old, the business isn't. Blind spot flagged.
- Quality: 4.1% of account-days missing plan tier (join failures on renamed accounts); seat counts top-coded at 500; one enterprise account is 11% of all usage rows.
- Robust defaults: usage per account is heavily right-skewed → medians + p10/p90 throughout; the whale account examined separately.

## Stage 2 — Sweep (cut ledger excerpt)

23 cuts examined across the five passes. Selected entries:

| # | Cut | One-line outcome |
|---|---|---|
| 3 | Usage distribution | Bimodal: a near-zero-usage mode (~14% of accounts) and a healthy mode |
| 6 | Usage over time (all) | Step increase in March 2026 (+22%) — PARKED, artifact suspect |
| 9 | Churned vs. retained, usage in final 90 days | Churned accounts' median usage ~60% lower — PARKED |
| 11 | Usage by acquisition channel | Partner-sourced accounts show 2.1× median usage — PARKED |
| 12–16 | Usage by plan tier, region, seat band, industry, signup year | All flat or small — logged as nulls |
| 19 | Weekly usage by weekday | Strong weekday cycle, as expected — null (unsurprising) |
| 21 | Feature-level: "exports" feature vs. renewal | Accounts using exports renew at 91% vs. 74% — PARKED |
| 23 | Residuals vs. seasonal baseline | One negative residual cluster: accounts onboarded Nov–Dec 2025 run below expectation — PARKED |

## Stage 3 — Gauntlet results for the five parked candidates

**C1. March 2026 step increase (+22%).** Artifact screen: **FAIL** — March 2026 is when the SDK v3 rollout added background-sync events. The "increase" is instrumentation. → **ARTIFACT SUSPECT**, and a consequential one: any usage trend crossing March 2026 is contaminated, including several the offsite deck probably already contains.

**C2. Churned accounts used less before churning.** Split-half: pass. Outliers: pass. Breadth: pass across tiers. But selection honesty: this is the textbook direction (usage predicts retention — of course), and magnitude check reveals the decline concentrates in the final 30 days, i.e., much of it is accounts *that had already decided to leave* winding down. Predictive value at a 90-day horizon is much weaker than the headline number implies. → **TENTATIVE** — real, directionally useful, but the "60%" figure would mislead the offsite; the actionable version needs a proper lead-time analysis.

**C3. Partner-sourced accounts use 2.1× more.** Breadth: **FAIL** — the effect collapses within seat bands. Partner-sourced accounts are simply larger; within any size band the channel difference is ~1.1×. Classic mix effect. → **CURIOSITY**, near-null. (Also the finding most likely to have launched a "partners drive engagement!" slide — this kill is the gauntlet earning its keep.)

**C4. Exports users renew at 91% vs. 74%.** Outliers: pass. Split-half: pass. Breadth: holds within seat bands and tiers (unlike C3). Selection honesty: exports was one of 9 features checked — with that denominator, a 17-point gap still stands out, but the label must say correlation: exports use plausibly *marks* operationally-embedded accounts rather than causing renewal. → **ROBUST PATTERN** (as a marker; causal claim untested).

**C5. Nov–Dec 2025 onboarding cohort underperforms baseline.** Split-half: untestable (single cohort). Base size: pass (n=142). Artifact screen: partial — that window overlaps a known onboarding-team staffing gap AND the holiday season. Two candidate mechanisms, can't separate here. → **TENTATIVE**, routed to RCA.

## Stage 5 — Report (as delivered)

> **Mode: exploratory — everything below is hypothesis, not conclusion.** Findings selected from 23 cuts examined; full ledger attached.
>
> **Three things deserve attention before the offsite:**
>
> 1. **[ARTIFACT SUSPECT] Your usage trends are contaminated from March 2026 onward.** The SDK v3 rollout inflated event counts ~22%. Any chart showing usage growth across that boundary — including, likely, ones already in the offsite deck — overstates it. *Next step: validation pass to build an adjusted series before Friday. This is the most urgent item because it silently corrupts every other usage number.*
> 2. **[ROBUST PATTERN] Exports usage is the strongest single renewal marker we found** (91% vs. 74%, holds within size and tier, one of 9 features checked). Treat as a health-score candidate and a segmentation flag — *not* as "make everyone use exports," which the data doesn't support. *Next step: formal test as a leading indicator on a holdout period.*
> 3. **[TENTATIVE] The Nov–Dec 2025 onboarding cohort is running below baseline** (n=142). Two candidate explanations we can't separate here: the onboarding staffing gap, or seasonal signup quality. *Next step: RCA — entry hypotheses: (a) staffing-gap accounts received fewer onboarding touches and show correspondingly lower week-4 activation; (b) holiday-window signups skew lower-intent independent of onboarding.*
>
> **Downgraded en route:** the "partner accounts are 2× more engaged" pattern is a size mix effect (~1.1× within seat bands) — recommend it not appear in the deck. The "churned accounts used 60% less" headline is real but mostly measures accounts already leaving; the decision-useful version requires a lead-time analysis we haven't run.
>
> **What we did not find:** no meaningful usage differences by region, industry, or plan tier — retention risk does not localize along the dimensions the team usually segments by. Given the offsite's agenda, that null is itself worth two minutes.

---

**What the process bought us:** the unstructured response to this prompt reports C1 as "usage is growing," C2 as "low usage predicts churn — 60%!", and C3 as "partner-sourced customers are twice as engaged" — three fluent, decked-ready, wrong-or-hollow findings — while likely missing C1's contamination of everything else. The gauntlet inverted the output: the flashiest candidates died, an artifact became the top priority, and the survivors shipped with labels that tell the offsite exactly how hard to lean on each.
