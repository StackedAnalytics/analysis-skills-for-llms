---
name: metric-reconciliation
description: >
  Evaluative analysis for cross-system metric discrepancies — "why don't these
  two tools agree," GA4 vs. the ad platform, analytics vs. the backend, BI vs.
  finance, "which number is right." Use this skill whenever two or more systems
  report different values for nominally the same metric and someone wants the
  difference explained, resolved, or adjudicated — even if they frame it as
  "fix the tracking" or "make these match." Do NOT use for a change over time
  within a single system (use root-cause-analysis) or for validating a single
  analysis's methodology.
---

# Metric Reconciliation

## Why this skill exists

Two failure modes meet here — one human, one LLM — and they reinforce each other.

The human failure is **the matching quest**: organizations treat disagreement between systems as a defect to be eliminated and pour analyst-months into forcing two tools to say the same thing. But systems that collect data differently — different collection points, identity models, attribution logic, filtering, timing — **will never agree, at the most fundamental level**, and cannot be made to. Chasing convergence past a certain point has steeply diminishing returns: each percentage point of "explained gap" costs more than the last, and full agreement is not merely expensive but *unachievable*, because the remaining difference is structural. The quest also rests on a false premise — that there exists one true number both systems are approximating. Usually there are two differently-defined numbers, each correct by its own definition.

The LLM failure is **obliging the quest with false precision**: handed "why don't these match," the model accepts the framing that matching is the goal, hunts for *the* discrepancy cause as if the gap were a single bug, and produces confident narratives that promise closure. Gaps between systems are almost never one cause — they are a **stack of small structural differences plus noise**, and treating the stack as a mystery-with-a-culprit guarantees an unsatisfying investigation that restarts next month.

This skill's reframe, applied before any investigation: **the goal is decision confidence, not data matching.** The question is never "how do we make these agree" — it is "which number should we trust, for which decision, and is the disagreement big enough to change any decision we'd make?" The deliverable is not agreement. It is an *explained, bounded, documented* gap — and, critically, **permission to stop looking**.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete:

```
- [ ] Decisions, materiality thresholds, and stop condition declared up front
- [ ] Expected-difference inventory + expected gap range written BEFORE decomposing
- [ ] Gap waterfall built; each component marked measured / bounded / assumed
- [ ] Verdict rendered against materiality (not zero); defects routed to RCA
- [ ] Operating agreement: system of record per decision / disagreement band / re-check triggers
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Reframe: attach the gap to decisions and set materiality

Before measuring anything, convert the matching request into a decision question (consume the Refined Question Brief if one exists):

1. **What decisions does each number feed?** List them concretely: budget allocation, board reporting, bid optimization, revenue recognition. Different decisions can legitimately use different systems' numbers — that is normal, not a problem to fix.
2. **Set the materiality threshold** (borrowed from audit practice): for each decision, how big would the disagreement have to be to change what anyone does? A 12% gap between GA4 and the ad platform is immaterial to a "keep vs. kill the channel" call and highly material to a CPA-based bid strategy. Materiality is a property of the decision, not the data.
3. **State the stop condition now, before investigating**: "We will decompose the gap until the unexplained residual is below X% or until the explained components account for the decision-relevant portion — then we stop." Declaring the stop condition in advance is the direct defense against the diminishing-returns spiral; without it, investigation continues until exhaustion rather than until sufficiency.

**Artifact required:** decisions list, materiality threshold per decision, and the declared stop condition.

## Stage 2 — Expected-difference inventory: why these systems *should* disagree

Before treating any of the gap as anomalous, enumerate the differences that are **architecturally guaranteed** — the disagreement the two systems would show even if both were working perfectly. Work through this checklist for the specific pair at hand; for each applicable item, estimate direction (which system reads higher) and rough magnitude where possible:

| Category | Typical mechanisms |
|---|---|
| **Collection point** | Client-side vs. server-side; browser events vs. transaction records; what one side physically cannot see (ad blockers, ITP, script failures, consent declines, offline events) |
| **Identity & scope** | User vs. session vs. cookie vs. account; cross-device stitching; logged-in vs. anonymous populations; what counts as "a user" differs by construction |
| **Attribution & credit** | Attribution windows (1-day vs. 7-day vs. 30-day), click vs. view-through, last-click vs. data-driven; every ad platform grades its own homework by design |
| **Definitions & inclusion** | What counts as the event: refunds, cancellations, test orders, subscription renewals, internal traffic, bot filtering rules, dedup logic |
| **Time** | Timezone of record; event time vs. processing time vs. report time; late-arriving data and restatement windows; when each system "closes the books" |
| **Processing** | Sampling, thresholding, cardinality limits, modeled/estimated data (consent-mode modeling, conversion modeling), aggregation quirks |

Two rules:

- **The inventory is the null hypothesis.** The burden of proof is on the claim that any part of the gap is a *defect* rather than a structural difference. This inverts the matching quest's default, where all disagreement is presumed broken.
- **Estimate the expected gap range before decomposing the actual one.** "Given these mechanisms, we'd expect System A to run 15–30% below System B" — written down *before* looking hard at the numbers, this is the reconciliation analog of stating priors, and it makes the eventual verdict falsifiable.

**Artifact required:** the inventory table for this specific system pair, with direction and rough magnitude per item, and the expected gap range.

## Stage 3 — Decompose the gap: build the waterfall

Now quantify. Take the observed gap and allocate it across the inventory, component by component, producing a **gap waterfall**: System A's number → adjustment for each named mechanism (estimated or measured) → System B's number, with an explicit **residual** for what the named components don't cover.

Discipline for this stage:

- **Measure where cheap, bound where not.** Some components can be measured directly (test orders: query them; timezone: shift and re-compare; refunds: count them). Others can only be bounded (ad-blocker loss: industry ranges plus your audience's tech profile). A bounded estimate honestly labeled beats a precise-looking guess.
- **Segment-level comparison beats aggregate.** Compare where the systems *should* be closest (e.g., logged-in users, direct traffic, a single timezone-clean day). If the gap collapses in the clean segment, the mechanisms are confirmed; if it persists, something genuinely anomalous is present. This is the single most diagnostic move in reconciliation.
- **The residual is a finding, not a failure.** Every reconciliation has one. Its job is to be (a) small relative to materiality, and (b) stable over time. A 4% stable residual is a healthy reconciliation; do not torture it toward zero.
- **Watch for the compensating-errors trap**: components that offset can make the headline gap look small while both systems are individually wrong. Decompose even when the totals happen to agree.

**Artifact required:** the waterfall — each component with its estimate, measurement basis (measured / bounded / assumed), and the residual.

## Stage 4 — Verdict: adjudicate against materiality, not against zero

Compare the decomposition to Stage 1:

1. **Is the residual below materiality for every listed decision?** If yes, the reconciliation is *complete* — regardless of the headline gap's size. A 25% fully-explained gap is a closed case; a 3% unexplained gap feeding a precision decision is not.
2. **Is any *explained* component itself a defect?** Structural differences are permanent; defects (a broken tag, double-firing events, misconfigured filters) are fixable. Route genuine defects to root-cause-analysis, phrased as falsifiable hypotheses. Do not confuse "explains the gap" with "acceptable" — or the reverse.
3. **If the residual is material and unexplained**, run the stop-condition check: is another round of decomposition likely to change a decision, or only to shrink a number nobody acts on? Recommend further investigation *only* with a specific mechanism to test and a decision that depends on it. "Keep digging" without both is the diminishing-returns spiral restarting.

## Stage 5 — Institutionalize: the durable outputs that end the recurring fight

The matching quest recurs monthly because reconciliations end with a number instead of an operating agreement. The final deliverable must include:

1. **System-of-record designation, per decision.** "For budget allocation: the data warehouse blend. For in-platform bid optimization: the platform's own conversions (it can only optimize on what it sees). For revenue reporting: the backend, full stop." One source of truth *per purpose* — not one global winner, which is the matching quest in disguise.
2. **The documented expected-disagreement band.** "These systems run 15–25% apart for these structural reasons [link to waterfall]. Investigate only when the gap exits that band." This converts the gap from a recurring alarm into a monitored control limit — the single highest-leverage sentence in the whole exercise, because it is what grants everyone permission to stop re-litigating.
3. **Defect fixes routed** (to RCA / implementation), with the expected band updated after fixes land.
4. **A re-check trigger**, not a re-check schedule: re-open when the gap exits the band, when either system changes collection/definitions, or when a new decision with tighter materiality arrives. Otherwise leave it alone.

## Anti-patterns (self-check before delivering)

- **Obliging the matching quest.** Accepting "make these agree" as the goal. The correct opening move is replacing the goal, explicitly and diplomatically.
- **The single-culprit hunt.** Investigating the gap as one mystery with one answer. Cross-system gaps are stacks; the waterfall exists because the answer is plural.
- **False precision.** Reporting "the gap is 18.3% due to attribution" when the honest statement is "attribution windows plausibly account for 10–20 points." Precision the methodology can't support is the LLM's signature failure here.
- **Default ground-truthing.** Silently treating one system as truth because it's newer, more expensive, or closer to money. Ground truth is decision-relative and must be *argued* (Stage 5), not assumed. (Backend transaction systems usually do win for revenue — but say why.)
- **Reconciling to zero.** Continuing past the stop condition because a residual "feels unfinished." A stable, sub-materiality residual is the definition of finished.
- **Compensating-errors complacency.** "The totals are close, so we're fine." Decompose anyway; offsetting defects are still defects.
- **The number without the treaty.** Delivering the decomposition but not the system-of-record designations and expected band — which guarantees the identical investigation re-runs next quarter.

## Output format

```
# Reconciliation: [System A] vs [System B] — [metric]

## Decision context & materiality
[decisions each number feeds · materiality per decision · declared stop condition]

## Expected differences (why these systems cannot agree)
[inventory table: mechanism · direction · rough magnitude · expected gap range]

## Gap waterfall
[System A figure → named components (measured/bounded/assumed) → System B figure
 → residual, with basis for each estimate]

## Verdict
[residual vs. materiality per decision · defects found (routed to RCA) ·
 further investigation warranted? (mechanism + decision, or stop)]

## Operating agreement
[system of record per decision · expected-disagreement band ·
 re-check triggers · fixes in flight]
```

For lightweight cases the format compresses, but three elements are never optional: the materiality threshold, the residual with its basis, and the expected-disagreement band. Without the band, the fight is scheduled to recur.
