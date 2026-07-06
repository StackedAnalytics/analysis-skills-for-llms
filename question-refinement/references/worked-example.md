# Worked Examples: Question Refinement

Three compact runs showing each triage path. Read this if unsure how aggressive to be, or what a Refined Question Brief looks like in practice.

---

## Example 1 — DECLARE path (the default)

**Request:** "Can you pull conversion rate by channel for the last 90 days?"

**Chain reconstruction (silent):** Oddly specific cut → presupposed-solution signature. Someone suspects a channel. No decision stated. Data pull as phrased is cheap, so honor it — but reattach to the open question and surface the assumption.

**Response opening:**

> Here's conversion by channel for the last 90 days [data follows]. A note on framing: requests like this usually sit behind a question like "is one of our channels underperforming, and is it getting worse?" — so alongside the raw rates I've flagged which channel deltas are outside normal variance and which are just noise, since eyeballing the table tends to overread small gaps. **I'm assuming** this is about diagnosing channel performance rather than, say, building a recurring report — if there's a specific decision behind it (budget reallocation, a channel under review), tell me and I'll sharpen the cut.

**Why not ASK:** every plausible interpretation starts with the same data pull, so no work is wasted by proceeding. The declaration converts a silent guess into a correctable one.

---

## Example 2 — ASK path (a genuine fork)

**Request:** "Can you look into our engagement numbers?"

**Chain reconstruction:** "Engagement" is the canonical compressed/proxy question — the decompressions route to *different analysis types entirely* (churn risk → diagnostic/predictive; content performance → descriptive/comparative; feature adoption → exploratory). No shared first step. Proceeding on a guess risks the full analysis. This clears the ASK bar.

**Response:**

> Happy to — one thing first, because "engagement" points at genuinely different analyses and I want to run the right one. Which is closest to the actual concern?
>
> 1. **Retention worry** — are users drifting away / early churn signals (I'd analyze usage-frequency trends by cohort)
> 2. **Content or feature performance** — what's being used and what's ignored (comparative breakdown)
> 3. **Something happened** — a number moved and you want to know why (root-cause workup)
> 4. Something else — one sentence on the decision this feeds is plenty.

**Note the shape:** three candidates + an escape hatch, each with a preview of the analysis it triggers — answering takes the requester five seconds, and the candidates themselves demonstrate the fork is real rather than pedantic.

---

## Example 3 — Unanswerable-as-scoped, with the adjacent answerable question

**Request:** "We rebranded in April. Can you show that the rebrand drove the Q2 traffic lift?"

**Chain reconstruction:** Causal certainty demanded from observational data — no control group, launch confounded with seasonality and a paid campaign that started the same month. Also note the phrasing: "show that," not "test whether" — the conclusion is presupposed. Two pathologies stacked.

**Response opening:**

> Straight answer first: with this data we can't *prove* the rebrand drove the lift — the launch coincides with seasonal recovery and the April paid push, and there's no unexposed comparison group, so any single number "showing" causation would be manufactured confidence. Here's what we **can** do, which is weaker but honest and still useful for the board narrative:
>
> 1. **Concentration check:** if the rebrand drove the lift, it should be strongest in branded search and direct traffic, not paid. (It is/isn't — evidence for/against.)
> 2. **Decomposition:** strip the paid campaign's tracked contribution and seasonal baseline out of the Q2 lift; the unexplained remainder is the *ceiling* on the rebrand's plausible effect.
> 3. **Timing alignment:** did branded-query volume inflect at rebrand launch specifically, or drift up across the quarter?
>
> That gives you "the pattern is consistent with a meaningful rebrand effect, bounded at roughly X" — defensible in front of anyone — instead of a causal claim that falls apart under one sharp question.

**The move:** refuse the false-confidence oblige *and* the flat refusal simultaneously. The adjacent answerable questions are the deliverable.

---

## A full Refined Question Brief (from Example 1, after the user replies)

User's reply: "It's for Thursday's meeting — CMO thinks paid social is wasting money and wants to cut it."

```
## Question brief
- Real question: Is paid social underperforming enough to justify cutting
  its budget, accounting for its assist/upper-funnel role?
- As originally asked: "Can you pull conversion rate by channel for the
  last 90 days?"
- Decision this informs & owner: Thursday budget reallocation — CMO
- Analysis type: Comparative (channel efficiency incl. multi-touch
  contribution) → Prescriptive (cut / hold / restructure recommendation)
- "Answered" looks like: a defensible recommendation with a CPA/contribution
  range, executive audience, by Wednesday EOD
- In scope: last 2 quarters, paid channels, assisted conversions
- Out of scope: creative-level analysis, organic channels
- CONFIRMED: decision, owner, deadline
- ASSUMED (correct me): last-click conversion alone would understate paid
  social, so multi-touch contribution is in scope; "wasting money" means
  efficiency vs. other channels, not absolute ROI vs. a target
```

Note what happened: the original request was a *descriptive* pull; the real question is *comparative → prescriptive*. Obliging literalism would have delivered a technically accurate table that walked into Thursday's meeting unarmed — the last-click table would have "confirmed" the CMO's guess by construction, since paid social always looks worst on last-click. The refinement didn't just sharpen the question; it caught a methodology trap embedded in it.
