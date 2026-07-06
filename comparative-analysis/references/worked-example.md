# Worked Example: Ranking 14 Campuses by Lead-to-Enrollment Conversion

A compressed run of the comparative-analysis skill on a league-table request for a career-college network. The instructive beats: the raw ranking's top and bottom are both small-n artifacts, the two-flagship comparison *reverses* under program-mix stratification, and one "underperformer" is just young.

**Prompt:** "Leadership wants a ranking of our 14 campuses by lead-to-enrollment conversion for the semester. Which campuses are best and worst, and what should the bottom ones learn from the top?"

Note the request pre-commits to a smuggled verdict ("what should the bottom learn from the top") — it assumes the ranking will measure practice quality. Proceed, but the conclusion will address that framing.

---

## Stage 1 — Comparability audit

| Term | Finding | Status |
|---|---|---|
| Definition | "Enrollment" consistent (registrar-confirmed starts). "Lead" is NOT: 11 campuses use web forms; 3 heavy on phone leads logged manually in the CRM — undercounted denominator inflates their rate | **flagged** — phone-heavy campuses (Riverside, Dover, Mesa) carry a ⚠ throughout |
| Window | Same semester for all | fixed by scoping |
| Maturity | Kirkwood campus opened 5 months ago; median lead-to-enrollment lag is 9 weeks, so a large share of its recent leads *cannot have converted yet* | **flagged** — Kirkwood reported but not ranked on this metric; age-aligned view provided instead |
| Denominator | Leads deduped per campus consistently | fixed |
| Measurement | Consent/tracking symmetric across campuses (same site platform) | pass |

## Stage 2 — Comparison quantity

Comparing **lead-to-enrollment conversion rate, per unique lead, semester window, because leadership is allocating admissions-coaching resources.** (Rate, not enrollment volume — volume answers a different question and would rank the big-metro campuses first regardless of practice quality.)

## Stage 3 — Composition check

Mix drivers: **program mix** (healthcare programs convert ~2× trades/business — shorter decision cycle, clearer job outcome), and **lead source mix** (referral/walk-in leads convert far above paid-search leads).

The headline fight is between the two flagships: **Ashford 11.8% vs. Brampton 9.1%** — a 2.7-point gap leadership already attributes to Ashford's admissions team.

Stratified by program:

| Program group | Ashford | Brampton |
|---|---|---|
| Healthcare | 14.0% | **15.2%** |
| Trades | 7.9% | **8.4%** |
| Business | 6.8% | **7.1%** |

**Full Simpson's reversal: Brampton outperforms Ashford within every program group.** Ashford's aggregate lead is entirely mix — 61% of its leads are healthcare vs. Brampton's 34%. Standardized to the network's common program mix: **Brampton 10.6%, Ashford 10.1%.** The decomposition: the +2.7 aggregate gap = +3.2 points mix − 0.5 points within-program performance. The "what should Brampton learn from Ashford" premise is backwards; the real question surfaced is *why Brampton's lead mix skews away from healthcare* — a marketing/targeting question, not an admissions-coaching one.

## Stage 4 — Ranking discipline

Raw league table extremes: #1 **Talmadge, 16.3%** — on **43 leads** (7 enrollments). #14 **Ellsworth, 4.1%** — on **74 leads**. Network rate: 9.4%; minimum base for ranking set at **150 leads** (stated threshold).

Funnel logic against expected variability at each campus's n: **Talmadge and Ellsworth both sit inside their control limits** — neither is distinguishable from the network average at their volumes. Two mid-table campuses, unremarkable in the raw sort, *are* genuine outliers at their large n: **Hartwell (8.1% on 1,900 leads, significantly below)** and **Pineda (10.9% on 1,650, significantly above)**. The raw ranking's story ("What's Talmadge's secret? What's wrong with Ellsworth?") is a story about noise; the funnel's story — boring mid-table names with big samples — is the real one. Regression-to-mean caveat attached: Talmadge should be expected to look "worse" next semester with no change whatsoever, and any initiative aimed at Ellsworth will "work" for the same reason.

## Stage 5 — Conclusion (as delivered)

> **The ranking you asked for is attached; it should not drive the coaching allocation, and here is what should.** Three findings survive scrutiny:
>
> 1. **Pineda is the genuine top performer and Hartwell the genuine laggard** — mid-table in the raw sort, but the only two campuses whose rates are distinguishable from the network average at their volumes (both 1,600+ leads). If coaching resources follow performance evidence, they flow toward Hartwell, and the practices worth studying are Pineda's. [distinguishable at stated thresholds]
> 2. **The Ashford-vs-Brampton gap is program mix, reversed underneath.** Brampton converts *better* in every program; Ashford's aggregate lead comes from a healthcare-heavy lead blend. Action item is for marketing (Brampton's lead mix), not Brampton's admissions team. [full stratified table attached]
> 3. **Talmadge (#1) and Ellsworth (#14) are small-sample noise**, inside expected variability at their volumes. No lessons live there yet. Kirkwood is excluded from rate ranking — 5 months old against a 9-week conversion lag, its number is pipeline math, not performance. ⚠ Riverside, Dover, and Mesa's rates are inflated by undercounted phone leads; fix the CRM logging before their numbers are compared to anyone's.
>
> **What this comparison cannot say:** whether any campus's practices *cause* its rate — campuses differ in local labor markets, program portfolios, and lead sources they didn't choose. If leadership wants to know whether Pineda's practices transfer, that's a causal question: pilot the practices at 2–3 matched campuses with a comparison group [→ causal-impact], rather than mandating them network-wide off an observational ranking.

---

**What the process bought us:** the obliging response delivers the raw table, celebrates Talmadge, condemns Ellsworth, and recommends Brampton study Ashford — four conclusions, all wrong, each capable of misdirecting a semester of coaching budget. The scaffolded version found the two campuses that actually differ, flipped the flagship narrative, rescued a new campus from an unfair metric, caught a denominator defect worth fixing, and converted "make the bottom learn from the top" into a testable pilot instead of a mandate.
