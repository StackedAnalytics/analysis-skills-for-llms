# Worked Example: GA4 Purchases vs. Shopify Orders

A compressed run of the reconciliation skill on the most common fight in ecommerce analytics. The instructive parts: the expected-gap range written *before* decomposition (Stage 2), the clean-segment comparison doing the heavy diagnostic lifting (Stage 3), and an ending where a 19% gap is a *closed case* while a defect hiding inside it still gets fixed.

**Prompt:** "GA4 says we had 8,210 purchases last month, Shopify says 10,140. Marketing and ops are fighting about which is right. Can you figure out what's broken and get these matching?"

---

## Stage 1 — Reframe, decisions, materiality

Note the request contains the matching quest verbatim ("get these matching") plus a presupposed defect ("what's broken"). Neither is accepted as the goal.

- **Decisions fed:** (1) Monthly revenue/order reporting to leadership — Shopify's number, ops. (2) Channel ROAS and budget shifts — GA4's number, marketing. (3) A planned CPA-based Google Ads bid strategy — would consume GA4 conversions.
- **Materiality:** Decision 1: any gap is immaterial to reporting *as long as we designate one source* — the fight is about authority, not magnitude. Decision 2: gaps under ~15% don't change channel rankings (checked: rank order is stable under ±15% perturbation). Decision 3: materially sensitive — a 20% undercount in GA4 systematically starves bids; threshold ~10%.
- **Stop condition (declared now):** decompose until the unexplained residual is < 5 points of the 19% gap, or until all Decision-3-relevant mechanisms are quantified. Not until the numbers match — they won't, ever, and that is expected.

## Stage 2 — Expected-difference inventory (before touching the data)

| Mechanism | Direction | Rough magnitude |
|---|---|---|
| Consent declines + Consent Mode behavior (EU traffic ~30% of base) | GA4 lower | 4–8% |
| Ad blockers / ITP / script failures on client-side gtag | GA4 lower | 3–8% |
| Subscription renewals (billed server-side, no site visit) | GA4 lower | ~6% (measurable) |
| Draft/phone orders entered in Shopify admin | GA4 lower | 1–2% (measurable) |
| Shopify counts orders incl. later-cancelled; GA4 purchase fires at confirmation | mixed, small | ±1% |
| Timezone: Shopify store TZ (EST) vs GA4 property (PST) | boundary noise | <1% monthly |
| Test orders | GA4 higher or lower | <0.5% (measurable) |

**Expected gap range, written before decomposition: GA4 should run 14–25% below Shopify.** Observed gap: 19.0%. *The observed gap sits inside the expected band before we've investigated anything* — a fact worth stating to both departments immediately, because it reframes the fight: nothing is presumptively broken.

## Stage 3 — Gap waterfall

Shopify 10,140 → GA4 8,210. Gap: 1,930 orders (19.0%).

| Component | Orders | Basis |
|---|---|---|
| Subscription renewals (no session) | −612 | **measured** — Shopify order tags |
| Admin/draft/phone orders | −158 | **measured** — order source field |
| Consent declines (unmodeled) | −430 ±120 | **bounded** — consent rate × EU share |
| Ad blockers / ITP / script loss | −340 ±150 | **bounded** — industry range × device mix |
| Cancelled-order timing | −74 | **measured** |
| Test orders | −11 | **measured** |
| **Residual** | **−305 ±190 (≈3.0%)** | unexplained |

**Clean-segment check (the decisive move):** compared logged-in, non-subscription, US-only, consented desktop orders for one mid-month week: Shopify 412 vs GA4 396 — a 3.9% gap, consistent with the residual. The structural mechanisms are confirmed: where they don't apply, the systems nearly agree.

**One defect found while measuring:** the Shopify admin-order component *should* be near zero for the online store's GA4 purchase event, but 89 of the 158 admin orders *did* fire GA4 purchases — a mis-scoped server-side tag double-counting a subset. That's a genuine defect (fixable), worth ~0.9%, currently *shrinking* the apparent gap (a compensating error: it was masking part of the consent loss).

## Stage 4 — Verdict

- Residual ≈3%, stable in the clean-segment check: **below the 5-point stop condition. Investigation complete.** The 19% headline gap is ~16 points structural + ~3 points residual noise. Nothing about the gap's *size* is broken.
- One defect routed to root-cause-analysis/implementation: the admin-order tag mis-scope (falsifiable statement: "server-side purchase tag fires for order sources other than online store; fixing the source filter removes ~89 orders/month from GA4"). Fixing it will *widen* the headline gap by ~1 point — flag this in advance or the fix will look like a regression.
- Decision 3 (CPA bidding): GA4's structural undercount (~16%) is material at the 10% threshold. Recommendation: bid strategy should use enhanced conversions + a modeled uplift factor, or optimize on a warehouse-side conversion feed — *not* raw GA4 counts.

## Stage 5 — Operating agreement (the part that ends the fight)

- **System of record:** Revenue/order reporting → **Shopify** (it's the transaction system; GA4 physically cannot see ~16% of orders). Channel performance & ROAS → **GA4** (Shopify has no acquisition context). Bid optimization → GA4 *with* the modeled adjustment above.
- **Expected-disagreement band: GA4 will run 15–23% below Shopify** (widens ~1pt after the tag fix). This is documented, linked to the waterfall, and is now a control limit: **investigate only if the monthly gap exits the band.**
- **Re-check triggers:** gap exits band; consent banner or tag architecture changes; subscription mix shifts materially; a new decision needs tighter tolerance. No standing monthly reconciliation meeting — that meeting is the diminishing-returns spiral with a calendar invite.

---

**What the process bought us:** the obliging response to "get these matching" spends weeks hunting a single bug that doesn't exist, "fixes" things until the numbers coincidentally converge (likely by breaking something, e.g., leaving the double-counting tag in place *because* it narrows the gap), and reconvenes next quarter. This process instead: declared the gap 84% structural within the first pass, found one real defect precisely *because* it decomposed rather than matched (the defect was making the totals look better), told marketing their bidding plan needed an adjustment that raw matching would never have surfaced, and ended with a treaty — designated sources, a band, and triggers — that makes the recurring fight structurally unnecessary.
