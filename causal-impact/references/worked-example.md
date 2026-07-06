# Worked Example: "Prove the Spring Campaign Drove the Signup Lift"

A compressed run of the causal-impact skill. The instructive beats: the request arrives pre-concluded ("prove"), the naive pre/post number gets replaced by a climbable design hiding in the rollout, a falsification test kills half the headline effect, and the deliverable includes the design for next time.

**Prompt:** "Our Spring brand campaign ran March 10 – April 20. Signups are up 31% vs. the prior six weeks. Leadership wants a slide proving the campaign drove it. Budget for a fall repeat depends on this."

---

## Stage 1 — Claim needed & framing

- **Decision:** fund a fall repeat (~comparable spend). This needs more than a direction — leadership is deciding whether the *incremental* signups justify the cost — but it needs a defensible estimate or bound, not a decimal point.
- **Framing pressure, flagged:** the request says "prove," and the requester benefits from a yes. Analysis proceeds symmetric: designed to be equally capable of reporting no detectable effect. The slide will say what the data supports.

## Stage 2 — Counterfactual

Naive framing ("vs. the prior six weeks") assumes signups would have stayed flat — but the pre-period covers Feb/early March and signups have spring seasonality plus an existing upward trend. A frozen baseline is not a counterfactual.

**Available constructions, strongest feasible first:** the campaign rolled out **staggered** — paid media went live in the US on March 10 but Canada (≈12% of signups, historically parallel) didn't get the campaign until April 1. That's an untreated comparison group for three weeks, plus a projected-baseline check for the full window.

> The effect of the Spring campaign is measured against (a) Canada's signup trajectory as an untreated control during Mar 10–31 (difference-in-differences), and (b) a trend-plus-seasonal projection of each region's own pre-period for the full flight.

## Stage 3 — Confound inventory

**Co-timed:** (1) spring seasonality — signups rose ~9% in the same window last year with no campaign [addressed by design: both the control and the projection carry seasonality]; (2) a pricing-page redesign shipped March 24 [unaddressed by DiD if it shipped globally — it did; flagged, partially separable via the Canada comparison since both got the redesign]; (3) tracking timeline checked: no tag, consent, or definition changes in the window [artifact hypothesis cleared]; (4) PR mention on April 3 [confounded with the campaign's US flight; noted].

**Selection:** none at the region level for the staggered window — Canada's later start was a media-buying logistics decision, not a performance one (confirmed with the media team; this matters, and the confirmation is cited, not assumed).

## Stage 4 — Design & assumptions — [RUNG 2: difference-in-differences]

- **Parallel pre-trends:** plotted US vs. Canada weekly signups for 16 pre-weeks — visually parallel, no divergence in the 4 weeks before launch. **Checked, passes.**
- **No spillover:** could US media reach Canadian users? Checked geo-targeting settings and Canadian referral sources during the US-only window — Canadian branded-search volume flat until their own April 1 start. **Checked, passes (approximately).**
- **Stable composition:** no mix change in either region's acquisition channels pre-window. **Checked.**

**Estimate:** during Mar 10–31, US signups exceeded the Canada-implied counterfactual by **+14% (±5)**. The raw US pre/post for the same window was +24% — meaning the naive number roughly **doubles** the defensible one, with the difference being seasonality and trend the campaign doesn't own.

## Stage 5 — Falsification

- **Placebo timing:** same DiD applied to a fabricated "launch" on Feb 3 → effect ≈ +1.5%, not distinguishable from zero. **Pass** — the method isn't hallucinating effects.
- **Unaffected outcome:** the campaign was top-of-funnel brand media; it has no mechanism to lift *existing-customer logins*. Logins: flat vs. counterfactual. **Pass.**
- **Dose-response:** US DMAs with heavier media weight show larger lifts (rank correlation positive, monotonic-ish). **Pass — this is the strongest single piece of corroboration.**
- **Specification robustness:** effect ranges +11% to +16% across reasonable window/control choices. Stable. One failure worth reporting: extending the "campaign effect" through the full flight (Apr 1–20, after Canada was also treated) requires the projection-based counterfactual, which is rung-2.5-ish and *cannot* separate the April 3 PR bump — the full-flight estimate is therefore reported as a **range with a ceiling**, not a point.

## Stage 6 — Conclusion — [RUNG 2 for weeks 1–3; bounded thereafter]

> **The campaign produced a real, measurable lift — smaller than the headline number.** For the cleanly identified window (Mar 10–31), the campaign caused approximately **+14% incremental signups (±5)** versus the untreated-region counterfactual [RUNG 2: DiD, pre-trends verified, dose-response corroborates]. The widely-quoted +31% pre/post figure is roughly half seasonality and trend; it should not appear on the slide. For the full flight, the defensible statement is a **bound**: total incremental signups between ~3,100 and ~5,400, the upper range inseparable from the April 3 PR effect.
>
> **Assumption ledger:** Canada's later start was operationally, not performance, motivated (confirmed with media team — the conclusion leans on this); no unobserved US-only shock in the window (the pricing redesign was global; PR is inside the bound, not the point estimate).
>
> **Fall decision input:** at the campaign's cost, break-even required ~2,400 incremental signups; even the lower bound clears it. The recommendation to repeat is supported — by the bounded number, not the inflated one.
>
> **Upgrade path (do this in the fall):** hold out 3–5 matched DMAs for the full flight. That converts next season's analysis to a designed geo-experiment [RUNG 1], makes the incrementality number bid-able, and costs a few percent of reach. Causal confidence is designed in advance; this flight got lucky that the rollout stagger existed at all.

---

**What the process bought us:** the obliging response builds the "+31% — campaign success!" slide leadership asked for, which then fails the first sharp question ("wasn't spring already trending up?") and poisons trust in the next ask. This process delivered a *smaller number that survives interrogation*, killed the inflated one before it reached a slide, separated what the data can prove (weeks 1–3, causally) from what it can only bound (the full flight), still supported the fall repeat — and left behind the holdout design that makes next year's version of this question trivial instead of forensic.
