# Worked Example: "Should We Cut Paid Social?"

A compressed run of the prescriptive-analysis skill — deliberately picking up where the question-refinement worked example left off (the CMO's Thursday budget meeting), to show the skills composing end-to-end. The instructive beats: the request arrives leaning hard, the winning option wasn't on the menu, the consequence table carries upstream uncertainty labels into the final call, and the sycophancy test gets answered in writing.

**Prompt (via the Refined Question Brief):** CMO believes paid social is wasting money and wants it cut; decision Thursday; real question scoped as "is paid social underperforming enough to justify cutting, accounting for its upper-funnel role?"

---

## Stage 1 — Frame

- **Decision & owner:** reallocate (or not) the paid social budget (~$38k/mo) for next quarter. Owner: CMO. Deadline: Thursday.
- **Framing pressure, noted:** the request leans *cut* — "wasting money" is in the brief verbatim. Analysis designed symmetric; see Stage 5.
- **Criteria, weighted before evaluation (confirmed with requester):** (1) marketing efficiency — blended CPA within 10% of target [highest]; (2) pipeline protection — don't damage upper-funnel volume feeding other channels [high]; (3) decision reversibility [medium]; (4) team capacity — no new-channel builds this quarter [constraint, not preference].
- **Hard constraints:** total budget fixed; compliance-sensitive vertical rules out two alternative channels outright.

## Stage 2 — Widen the options

Offered frame: **cut** vs. **keep**. Additions:

- **A. Keep as-is** (status quo, honestly costed: current last-click CPA is 2.3× target — the status quo has a real problem; this isn't a defense of it).
- **B. Cut entirely** (the leaned-to option).
- **C. Restructure** *(out-of-frame)*: kill prospecting (the expensive 70%), keep retargeting + branded audiences, redeploy the difference to the two channels with headroom.
- **D. Measure, then decide** *(information-buying)*: 6-week geo-holdout on prospecting to get a rung-1 incrementality number, ~$4k design cost, decision rule pre-committed ("if incremental CPA > 1.5× target, cut prospecting permanently").

## Stage 3 — Consequence table (evidence labels carried in)

| Criterion → | Efficiency | Pipeline risk | Reversibility | Capacity |
|---|---|---|---|---|
| **A. Keep** | CPA 2.3× target on last-click; 1.4–1.7× on MTA [comparative: distinguishable from other channels' CPA at volume] | none | full | fine |
| **B. Cut all** | Saves $38k/mo *if* conversions truly non-incremental — **UNKNOWN: no incrementality estimate exists** [best evidence is rung-4: platform-reported lift, self-graded] | Branded-search & direct volume historically co-move with social reach [comparative, observational — selection-confounded]; downside range −4% to −12% on assisted pipeline [bounded, weak] | **one-way hinge:** audience pools & platform learning decay in ~4–6 wks; rebuild cost real | fine |
| **C. Restructure** | Retargeting CPA ≈ 0.9× target [strong]; prospecting cut saves $27k/mo with same UNKNOWN as B but smaller exposure | reduced but nonzero (prospecting feeds the retargeting pool — pool shrinks over ~8 wks) | mostly two-way | fine |
| **D. Holdout first** | costs ~$4k + 6 wks of status-quo inefficiency (~$14k excess spend vs. C) | none during test | full | fine |

**Dominance notes:** A is dominated by C on every criterion except reversibility (tie). B vs. C vs. D is a genuine trade-off — exactly what the table is for. The efficiency column's load-bearing cell (is prospecting incremental *at all*?) is UNKNOWN across the board — which is the argument for D.

## Stage 4 — Risk & reversibility

- **B (cut all):** advertised as reversible; actually a one-way hinge — audience decay plus retargeting-pool starvation means "turn it back on" returns to a worse position than today. Downside tail: if social prospecting is meaningfully incremental to branded search, a full cut is a slow leak discovered two quarters late, misattributed to "market conditions."
- **C (restructure):** two-way on retargeting; the prospecting cut shares B's tail at ~70% of the exposure, with the retargeting pool as an early-warning canary.
- **D (holdout):** no tail; costs ~$18k of patience and requires the CMO to accept "not yet" as a Thursday answer.

## Stage 5 — Stress test

- **Pre-mortem (chose C, 12 months on, it failed):** (1) prospecting was quietly feeding branded search; pipeline eroded over two quarters and nobody connected it → maps to the UNKNOWN cell; mitigated only by D or by C-with-monitoring. (2) Retargeting pool starved; its CPA drifted up 40% by month 3 → known mechanism, tripwire-able. (3) Redeployed budget hit diminishing returns in the receiving channels → checkable now against their marginal-CPA curves (checked: headroom exists for ~$20k, not $27k — table amended, C's redeploy trimmed).
- **Runner-up steelman (D):** the entire efficiency case turns on one UNKNOWN cell; $18k to convert a rung-4 guess into a rung-1 number that settles this argument permanently — and prevents both the slow-leak tail *and* the re-litigating of this decision every quarter — is cheap. This case is strong, and it rests on weights (reversibility + evidence quality over speed), not on different facts.
- **Sycophancy test, answered:** *If the CMO had leaned "keep," would this analysis recommend keeping?* No — the status quo is dominated on the frozen criteria regardless of lean; A loses under any defensible weighting. But note honestly: the *choice between B and C/D* is where the lean could have pushed, and the table's UNKNOWN cell is what stops a clean "cut everything" endorsement. The evidence, not the framing, is what's withholding B.

## Stage 6 — Recommendation (as delivered)

> **Recommend C+D combined: restructure now, measure the contested part before killing it.** Concretely — this week: cut prospecting spend by half (not fully), keep retargeting and branded audiences intact, redeploy $13k to the two channels with verified headroom. Simultaneously launch the 6-week geo-holdout on remaining prospecting ($4k), with the decision rule pre-committed: incremental CPA above 1.5× target → prospecting dies permanently at week 7; below → it survives at the efficient scale the test indicates.
>
> **Confidence:** high that A (status quo) is wrong — it's dominated. Moderate on the B-vs-C boundary, *because the decisive cell is unmeasured* — which is precisely why the recommendation buys the measurement instead of pretending certainty. [Evidence status: retargeting efficiency is solid; the prospecting incrementality question is rung-4 until the holdout reports.]
>
> **This rests on:** weighting reversibility and pipeline protection above maximum immediate savings, and on the marginal-headroom check in the receiving channels. Challenge those weights and B becomes defensible — that's your call to make, and here is the fork stated plainly: full-cut-now saves an extra ~$14k/quarter against a tail risk of a slow, misattributable pipeline leak.
>
> **Flip conditions & tripwires:** recommendation reverses toward full cut if the holdout shows incremental CPA > 1.5× target, or if retargeting CPA rises >20% within 6 weeks (pool starvation — the canary). Reversal plan: prospecting campaigns paused, not deleted; audiences exported; platform learning preserved for 6 weeks either way.

---

**What the process bought us:** the obliging response reads the CMO's lean, builds the "paid social is wasting money" case from the last-click table, and recommends the full cut — a one-way door through an unmeasured wall, discovered two quarters later as an unexplained branded-search decline (and, neatly, a future RCA engagement). The scaffolded version killed the actual loser (status quo), surfaced the option nobody offered, refused to launder a rung-4 guess into a confident cut, gave the CMO a direct actionable call for Thursday *plus* the honestly-stated fork that belongs to her — and pre-committed the decision rule so the argument ends in six weeks instead of recurring forever.
