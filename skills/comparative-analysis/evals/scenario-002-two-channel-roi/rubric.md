# Scenario 002 — Rubric

Same two-tier structure as scenario-001. **MUST** = discipline gate
(fail any one → run fails). **SHOULD** = breadth score (x/6). Grade against
`prompt.md`'s planted characteristics.

## MUST (pass/fail gate)

| # | Check | Maps to |
|---|---|---|
| M1 | Comparability audit excludes non-commensurable platform metrics from head-to-head use: platform conversions ruled fatal (or equivalent), impressions/CPM/CTR kept as within-channel context only | 6 |
| M2 | The entity-scope decision on the third spend component is surfaced **as a decision** — included or excluded explicitly, with the basis for the choice stated (and its provenance sourced, not asserted) | 2 |
| M3 | Censoring handled: no verdict rests on immature landed rates alone (bracket/floor-vs-modeled, or a matured basis, or equivalent) | 4 |
| M4 | **The basis fork is exposed.** Both credible auxiliary bases are enumerated; because they flip the ranking, the verdict is presented as basis-conditional (or the analysis halts to reconcile the bases) — never a single-basis verdict with the rival basis unmentioned | 5 |
| M5 | Interpretation firewall holds: no budget-reallocation recommendation from this observational comparison; incrementality/holdout named as the licensing step | — |
| M6 | Funnel grain and matching method stated; any fan-out bridge deduped to the counting grain | 3 |
| M7 | Ranking discipline on segment cells: min-n stated; tiny-n bait reported but not ranked | 9 |

## SHOULD (quality score, x/6; x/7 for runs after the 2026-07 communication convention)

| # | Check | Maps to |
|---|---|---|
| S1 | Catches the search channel's intra-quarter regime shift (monthly granularity) and routes it rather than narrating a cause | 7 |
| S2 | Catches the social channel's intra-quarter saturation divergence (volume down / CPL up on flat spend) | 8 |
| S3 | Runs the geography (or equivalent) stratification and states the mix/performance decomposition | 9 |
| S4 | Attribution weakness carried as a symmetric caveat into the conclusion — used to qualify absolutes, not to dodge the comparison | 10 |
| S5 | Spend treated as a managed input (not triaged/narrated as an outcome); efficiency outcomes get the analytical attention | — |
| S6 | Conclusion pairs the characterization with named next-step designs (incrementality test; RCA on signals) | — |
| S7 | *(runs after the 2026-07 communication convention only)* Deliverable body is plain-language: internal vocabulary translated, checklist and artifacts in a workings layer, calibration distinctions preserved in the translation | — |

## Grading notes

- M4 is the centerpiece and the reason this scenario exists: in the seeding
  run, **both** the baseline and the treatment failed it — each silently
  committed to a different basis and produced opposite verdicts from
  identical data. A future treatment run passing M4 is the regression test
  for the auxiliary-basis refinement added to the skill (2026-07).
- M2's provenance clause matters: asserting "component X belongs to channel
  A per the client" without a source is a scope decision smuggled as fact.
  Sourcing it (a table description, a documented client statement, an
  overlay file) passes; asserting it does not.
- Append future results to `notes.md`'s log; don't rewrite history.
