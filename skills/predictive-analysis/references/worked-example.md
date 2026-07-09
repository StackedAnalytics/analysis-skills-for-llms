# Worked Example: "Will We Hit 2,400 Leads This Quarter?"

A compressed run of the predictive-analysis skill on a pacing question for a career-college lead-gen program. The instructive beats: the recency trap is live (a spike scheduled to end), the naive baseline nearly wins the backtest, the ledger's symmetry check adds the downside entries the inside view forgot, and the forecast and the target get formally divorced.

**Prompt:** "We're 5 weeks into Q3 with 1,140 leads against a 2,400 target. The last two weeks were our best ever (620 combined). Are we going to hit it? Marketing is feeling great."

---

## Stage 1 — Frame

- **Decision:** whether to approve incremental paid spend in weeks 7–8 (lead time means the call happens at week 6) and whether admissions staffing holds for a September surge.
- **Horizon/granularity:** 8 remaining weeks, weekly resolution; the decision needs "probability of hitting 2,400" more than a point.
- **Asymmetry:** missing the target with no warning is worse than a conservative forecast that triggers spend which turns out unneeded (spend is recoverable; a surprise miss burns a semester's cohort). Report the honest distribution; the decision rule can be conservative.
- **Forecast vs. target:** the request phrase "are we going to hit it" invites bending the expectation toward 2,400. The forecast will be built blind to the target, then compared to it.

## Stage 2 — Outside view

- **Reference class:** the last 3 Q3s finished at 2,050, 2,210, 2,320 — growing ~6–7%/yr, with weeks 6–13 contributing 52–56% of quarterly volume (September-heavy academic seasonality). Spread on the back-8-weeks share: meaningful — ±4 points of share is ±90 leads.
- **Naive baselines:**
  - *Seasonal naive:* last Q3's back-8 weeks (1,205) × 1.065 growth ≈ **1,285** → quarter total ≈ **2,425**.
  - *Seasonally-shaped run-rate:* weeks 1–5 pace vs. historical week 1–5 share (46%) implies quarter total ≈ 1,140 / 0.46 ≈ **2,478**.

Both baselines land near the target — before any adjustments. Notably, the run-rate baseline already *contains* the recent spike; treating the spike as additional upside would double-count it.

## Stage 3 — Decomposition & known events

- **Trend, long vs. recent:** 24-month trend is +6%/yr. The last 2 weeks' slope, annualized, implies +180%/yr — the two are wildly inconsistent, so the recent slope is an *event*, not a trend. Identified: a paid-social burst campaign started week 4.
- **Known future events (the recency trap, defused):** that campaign **ends week 7**. Also: fall program pages launch week 8 (historically small, positive); Labor Day week (week 10) runs ~15% below adjacent weeks; no tracking or definition changes in the window (artifact check clean).
- **Regime check:** none — same channels, same forms, same market.

## Stage 4 — Adjustment ledger (relative to seasonal-naive 2,425)

| Adjustment | Dir | Size | Evidence |
|---|---|---|---|
| Burst campaign runs 2 more weeks | + | +95 | campaign's incremental daily rate (vs. pre-campaign baseline) × 14 days |
| Campaign ends week 7 | − | −140 | weeks 8–13 revert to pre-campaign organic+always-on pace; seasonal naive implicitly assumed *last year's* mix, which had no burst to lose |
| Fall pages launch (wk 8) | + | +25 | last year's launch bump, scaled |
| **Symmetry check additions:** campaign-fatigue decay already visible (wk-5 daily rate 12% under wk-4) | − | −20 | observed decay applied to remaining flight |
| Lead-quality dilution flag (not a volume adjustment) | ⚠ | — | burst leads' contact rate runs 30% below organic — flagged for the staffing decision, since 2,400 *leads* ≠ the enrollment pipeline the target proxies for |

**Ledgered forecast: 2,425 + 95 − 140 + 25 − 20 ≈ 2,385.**

## Stage 5 — Uncertainty

Backtest errors (Stage 6) on 8-week-out pacing forecasts: median absolute error ≈ 4.5%, roughly symmetric. Empirical **80% interval: 2,275 – 2,495**. The interval *straddles the target*: hitting 2,400 is roughly a coin flip leaning slightly under (~45%). One lumpy scenario branched rather than smeared: if the proposed incremental spend is approved at week 6, its expected contribution (+70 ± 30, from the current campaign's observed incremental rate with fatigue applied) shifts the distribution to ~65% over target.

## Stage 6 — Backtest

Method (seasonal naive + event ledger) rolled over the past 6 quarters at the same week-5 vantage: median error 4.5% vs. seasonal naive alone at 5.8% and shaped run-rate at 6.4%. The method beats naive — modestly. Honest note: most of the edge comes from the known-events ledger, not sophistication; in quarters with no scheduled events, plain seasonal naive tied it. (If it hadn't beaten naive, naive ships.)

## Stage 7 — Delivery (as sent)

> **Forecast: ~2,385 leads, 80% interval 2,275–2,495 — the target is genuinely in play but not safe: ~45% to hit as things stand.** The last two weeks are real but scheduled to end: the burst campaign that produced them stops at week 7, and its daily rate is already decaying. "Best two weeks ever" is an event in the ledger, not a trend — extrapolating it would forecast ~2,600 and set up a surprise miss.
>
> **The decision:** approving the incremental weeks 7–8 spend moves the odds to ~65% (+70 ± 30 leads at observed incremental rates). Given the asymmetry — a quiet miss costs a cohort, unneeded spend is recoverable — the analysis supports approving it at week 6.
>
> **Two cautions attached:** (1) burst-campaign leads contact at ~70% of organic rates — the *enrollment* pipeline is thinner than the lead count implies; staffing should plan on lead-quality-adjusted volume. (2) **Revision trigger:** if cumulative leads at end of week 7 are below 1,610, the 80% interval no longer contains 2,400 — auto-escalate rather than waiting for month-end. Forecast logged for scoring at quarter close.

---

**What the process bought us:** the obliging response extrapolates the best-two-weeks-ever, forecasts ~2,600, tells marketing they're cruising, and skips the spend decision — then the campaign ends, week 8 lands soft, and the quarter finishes at ~2,350 with everyone surprised. The scaffolded version identified the spike as a scheduled-to-end event, priced its ending, split the forecast from the target so the coin-flip truth could be stated, converted the finding into a spend decision with explicit odds, flagged that the target's *proxy relationship to enrollments* was quietly degrading, and left a tripwire so a miss can't arrive unannounced.
