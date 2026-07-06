# Worked Example: Mobile Web Conversion Drop

A compressed end-to-end run of the RCA skill, showing what the artifacts look like in practice. Read this if unsure what "good" looks like at any stage.

**Prompt:** "Our conversion rate dropped last week, can you figure out why?"

---

## Stage 1 — Problem specification

First move: the prompt is unspecified. Pull the data (or ask) to fill the table before theorizing.

| Dimension | IS | IS-NOT |
|---|---|---|
| What | Sitewide ecommerce conversion rate fell 3.1% → 2.2% (-29%) | Revenue per converting user unchanged; AOV flat |
| Where | Mobile web only (4.1% → 2.3%); paid search and paid social sessions | NOT desktop (flat at 2.9%); NOT app; NOT organic/email |
| When | Step change starting Tuesday June 14, ~10am ET; persistent since | NOT gradual; no recovery on weekend; NOT present June 13 |
| Extent | -45% on mobile-paid specifically; sessions volume unchanged | NOT a traffic drop; NOT -100% (some conversions still record) |
| UNKNOWN | Whether checkout *completions* (payment processor count) also fell | — flagged as top data-gathering question |

Note how much work the IS-NOT column does already: "sessions unchanged" kills traffic-mix stories; "app unaffected" narrows to web-specific causes; "not -100%" complicates a total-tracking-failure story.

## Stage 2 — Hypothesis enumeration

1. **[Measurement artifact]** GTM container publish on/around June 14 broke or partially broke the `purchase` event on mobile web.
2. **[Measurement artifact]** Consent-banner update reduced analytics consent rate on mobile, suppressing conversion recording (but not sessions, which fire pre-consent).
3. **[Internal change]** Checkout deploy on June 14 introduced a mobile-web bug that genuinely blocks some purchases.
4. **[Internal change]** Paid campaign change (new landing pages) sending lower-intent mobile traffic.
5. **[Mix shift]** Paid budget shifted toward a low-converting mobile campaign, dragging the blended rate down.
6. **[External event]** Google Ads algorithm/serving change altered mobile query mix.
7. **[Genuine behavior]** Real demand drop on mobile (macro, competitor promo).
8. **[Conjunction]** Small real seasonal dip + partial tracking loss stacking.

(Eight listed; #6 and #7 included despite low prior — that's deliberate.)

## Stage 3 — Evidence matrix

| Evidence | H1 tag | H2 consent | H3 checkout bug | H4 landing pages | H5 mix | H6 ads algo | H7 demand |
|---|---|---|---|---|---|---|---|
| E1: Step change at 10am Tue, not gradual | C | C | C | C | I | I | I |
| E2: Payment processor order count flat WoW (UNKNOWN resolved by query) | **C** | **C** | **I** | **I** | **I** | **I** | **I** |
| E3: GTM version history: container published June 14, 9:47am | **C** | N | N | N | N | N | N |
| E4: Desktop web unaffected (same container) | I? | C | C | C | N | N | N |
| E5: Sessions volume flat, campaign spend/mix flat | N | N | N | N | **I** | I | N |
| E6: `begin_checkout` events flat; only `purchase` fell | C | I | I | I | I | I | I |

**Diagnosticity note:** E2 is the decisive row — real orders didn't drop, so the "drop" is measurement, eliminating H3–H7 in one stroke. E6 discriminates within measurement: consent suppression (H2) would depress *all* events, but only `purchase` fell → H1 over H2. E1 and E3 are consistent-but-weaker (timing coincidence). E4 initially looks inconsistent with H1 — same container serves desktop — which forces a refinement: the publish broke something *mobile-conditional* (e.g., a trigger referencing a mobile-only checkout element).

## Stage 4 — Disconfirmation

- **Leading hypothesis:** June 14 GTM publish broke the mobile-web `purchase` tag.
- **What would falsify it:** purchase events firing correctly in a mobile debug session on the current container; or the diff between container v47→v48 showing no changes touching purchase triggers.
- **Did we look:** container diff pulled — v48 modified the purchase trigger's CSS selector for the confirmation button, which differs between mobile and desktop templates. Falsification attempted and failed → hypothesis strengthened.
- **Strongest runner-up case (H2, consent):** the consent banner *was* also updated in v48, and consent rates are noisy on mobile. But E6 (checkout events flat) is inconsistent with consent suppression, which is event-agnostic. Runner-up survives only if consent logic somehow gated purchase alone — no mechanism found.
- **Boundary check:** explains mobile-not-desktop (template-specific selector), explains not-100% (some mobile users hit the desktop-style template), explains timing (publish at 9:47, drop at ~10). All IS-NOTs accounted for except one — see residual.

## Stage 5 — Conclusion

- **Causal structure:** ~90% of the measured drop: purchase-tag trigger regression in GTM v48 (mobile-only selector break). ~10% unexplained (see residual). Business impact of lost *revenue*: none — orders are flat; this is a measurement incident, not a demand incident. Ad platforms optimizing on the broken conversion signal is the real ongoing damage.
- **Confidence:** High — grounded in two independent diagnostic evidence rows (E2 ground truth, E6 event asymmetry) plus a confirmed mechanism (the selector diff), not narrative fit.
- **Sensitivity:** Conclusion rests on E2 (processor order counts) and the container diff. If the processor data were misqueried (wrong date window), confidence drops to medium and H3 reopens.
- **Unexplained residual:** Mobile conversion pre-incident baseline shows a mild downward drift (~3%) over the prior 3 weeks that the tag regression does not explain. Likely seasonal; parked, not solved.
- **Verification:** Republish v47 to a debug environment (or fix the selector in v49), run a test purchase on the mobile template, confirm the event fires. ~15 minutes. Then backfill/annotate the gap and notify anyone consuming the conversion metric — especially paid media, whose bid strategies ingested a week of false negatives.

---

**What the process bought us:** the untrained response to this prompt is "conversions dropped → check what changed → a deploy happened → the checkout bug did it," reasoning that would have anchored on H3 (a plausible, vivid, *wrong* story) and sent engineering hunting a phantom bug. The single most valuable move was resolving the Stage 1 UNKNOWN (E2) — which came from the specification discipline, before any hypothesis was evaluated.
