# Scenario 001 — Warehouse first look

## Task prompt (give this to the model under test)

> You have query access to a client's BigQuery warehouse. Explore the `marts`
> dataset — the gold/presentation layer feeding their BI tool — and tell us
> anything worth knowing before we build reporting on top of it. Approach it
> fresh from the schema and the data itself; assume no prior knowledge of
> this warehouse.

Run once **without** the `exploratory-data-analysis` skill loaded (baseline)
and once **with** it (treatment). Grade both against `rubric.md`.

## Environment

Any warehouse with the characteristics below works. The original run used a
live client mart (anonymized here); a synthetic dataset planting the same
characteristics is an acceptable substitute. Rough shape: ~20 objects — fact
tables for contacts/leads, inquiries, contracts/orders, and daily ad spend,
plus conformed dimensions (date, location, channel, campaign, product/program)
— for a multi-location education/services network, ~15 years of history.

## Planted characteristics (what the data contains for the rubric to test)

1. **A two-population contact table.** Roughly two-thirds of contact records
   have a NULL created-date, no attributed location, and near-zero conversion
   (imported/purchased list records); the dated third converts at a high rate.
   Including the undated pool in any denominator dilutes rates ~3×.
2. **An attribution mirage.** A derived `channel` column is 100% populated
   (sourced from CRM self-report). The *click-level* attribution columns
   (ad-click IDs, web-analytics IDs, social lead IDs) are ~0% populated for
   all historical years and <10% populated after a tracking cutover roughly
   six months before the analysis date — the same date spend data begins.
3. **An unexplained volume surge.** Contract/order volume grows ~5× across
   the four most recent years while the location footprint stays nearly flat
   and per-unit value *rises*; zero-value record share is low and stable. No
   benign explanation is visible inside the mart.
4. **A censoring-defying rate.** The inquiry→contract realization rate rises
   sharply in the most recent years — the opposite direction right-censoring
   predicts — mechanically linked to (3).
5. **A channel-intent gradient with a confound.** Paid digital channels
   convert at ~5%; human-mediated channels (agents, referrals, funded
   programs) at 40–90%. The gradient is stable across eras and large-n, but
   high-intent channels may be *logged later in the funnel*, making part of
   the gap definitional.
6. **Placeholder records.** A specific contract status holds ~$1
   cost-per-lead placeholder rows; separately, ≤$0 values concentrate in
   pre-2015 legacy years.
7. **A normalization gap.** A large "(Historical/Other)" bucket in the
   product/program dimension holds a material share of volume and value;
   one flagship program dominates value.
8. **A granularity-hidden dip.** One recent quarter shows a pronounced dip
   in monthly contract starts, invisible in yearly aggregates.
9. **A decision-relevant null.** The two ad-spend tables reconcile to the
   dollar.
10. **A tracking-birth boundary.** One event type (reinquiries) exists only
    from a recent start date — a new-tracking artifact, not a new behavior.

## Anonymization rule for this folder

Nothing here may identify the client: no organization, location, franchise,
person, or program names; no exact revenue figures; sector described only as
"multi-location education/services network." Keep it that way in any files
added from future runs.
