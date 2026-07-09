---
name: exploratory-data-analysis
description: >
  Structured method for exploring data without a specific hypothesis —
  "poke around," "anything interesting?", "get a feel for this dataset,"
  "what should we know," first contact with unfamiliar data, or hypothesis
  generation ahead of a deeper analysis. Use this skill whenever the task is
  open-ended pattern-finding rather than answering a specific question, even
  if the user doesn't say "EDA" or "explore." Do NOT use for diagnosing a
  specific known change (use the RCA skill) or answering a specific
  pre-formed question (route through question-refinement first).
---

# Exploratory Data Analysis

## Why this skill exists

LLMs performing exploration exhibit **pareidolia**: they find a confident, well-written narrative in every pattern — including noise. This is the mirror image of the RCA failure. In diagnosis, the model converges too early on one story; in exploration, the model generates a story for *everything*, presents every finding with the same fluent confidence, and almost never says "this is probably just variance."

The mechanism compounds itself. An LLM exploring a dataset is a **garden-of-forking-paths machine** (Gelman & Loken) running at superhuman speed: it will slice the data twenty ways, notice the three cuts with the largest deltas, and present those three as findings — as if each had been the *only* comparison made, rather than the winners of a twenty-way tournament that noise alone would have produced medalists for. Selection plus fluent narration equals manufactured insight. No individual step is dishonest; the aggregate is misleading.

Tukey's founding distinction governs everything here: **exploratory and confirmatory analysis are different modes and must never be silently conflated.** Exploration's job is to generate hypotheses and expose structure; nothing it finds is *confirmed*, no matter how striking. The RCA skill manages the convergence dial by forcing divergence before convergence; this skill manages the same dial in reverse — divergence is the whole point, so the discipline goes into **honest bookkeeping of what the divergence produced**. Every finding leaves this process wearing an explicit epistemic status label, and the count of what was examined travels with what was found.

Do the stages in order. The bookkeeping artifacts are not paperwork — they are the only thing standing between exploration and a slide deck of coincidences.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] Mode declared; data-credentials note written
- [ ] Systematic sweep complete; cut ledger maintained (incl. nulls, PARKED items, and a NOT-EXAMINED line)
- [ ] Robustness gauntlet run on every candidate finding
- [ ] Every finding labeled: ROBUST / TENTATIVE / CURIOSITY / ARTIFACT SUSPECT / NULL
- [ ] Report: ranked lede / forking-paths sentence / handoffs / decision-relevant nulls
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Orient: declare the mode and check the data's credentials

Before finding anything, establish what you're standing on.

**1a. Mode declaration.** State explicitly: *"This is exploratory analysis. Its output is hypotheses and structure, not conclusions. Nothing below is confirmed."* If a Refined Question Brief exists (from the question-refinement skill), consume it here — it defines what "interesting" means for this audience and whether this exploration feeds a decision or is situational awareness. If exploration is one leg of a sequence ("exploratory now, diagnostic if we find something"), restate the handoff trigger.

**1b. Data credentials check.** Profile before interpreting. At minimum: row counts and grain (what is one row?), time coverage and gaps, key-field completeness/null rates, duplicates, category cardinality, and the join logic if multiple tables. Establish **what the data cannot show** — populations excluded, censoring, survivorship, tracking start dates — because the most seductive false findings are artifacts of coverage, not behavior. A "surge in March" that coincides with a tracking launch is not a surge.

**1c. Set robust defaults.** Per Tukey: prefer medians and percentile ranges over means and standard deviations at this stage — exploration should not be hijacked by outliers before you've decided what an outlier *is*. Note skew; consider log/re-expression early for heavy-tailed quantities (revenue, latency, session counts). Outliers get examined as their own finding class, not silently averaged in or silently dropped.

**Artifact required:** a short data-credentials note (grain, coverage, known blind spots, quality flags) preceding any findings.

## Stage 2 — Structured divergence: sweep systematically, log every cut

Divergence is the goal — but *systematic* divergence, not attracted-to-shiny divergence. An unstructured explorer gravitates to the first interesting thing and over-mines it (premature convergence sneaking back in through the side door). Instead, sweep planned passes:

1. **Distributions** — shape, spread, modes, mass at zero, top-coding, impossible values.
2. **Time** — trend, seasonality/cyclicality, step changes, gaps — **at two granularities** (coarse for trend, fine for dips and step timing): a one-quarter dip is invisible in a yearly series, and a step change's exact date is invisible in a quarterly one. Step changes are prime artifact suspects (definition or tracking changes).
3. **Segments** — the handful of dimensions most plausibly decision-relevant (per the Brief), not every dimension available. Default the set to the business's **primary entity dimensions** — product/program, location/geography, acquisition channel — plus whatever the Brief adds; skipping a primary entity dimension is a scope decision that must land in the NOT-EXAMINED line, not a silent omission.
4. **Relationships** — correlations/covariation between key measures; concentration (what share of Y comes from the top decile of X?).
5. **Residuals** — Tukey's deepest move: fit a crude expectation (last year + trend, a simple seasonal baseline, a group average) and study the *deviations from it*. The interesting structure lives in residuals; raw values mostly restate the obvious.

**The cut ledger (mandatory).** Maintain a running count and list of every comparison examined — every segment split, every correlation checked, every time window tried — including the boring ones. This is the forking-paths denominator. It exists because of a statistical fact the reader deserves to see: **examine 20 independent cuts and the largest delta will look impressive by chance alone.** A finding's meaning depends on how many places you looked, and only the ledger preserves that.

Rules for this stage:

- **Note the boring.** "Conversion is flat across all five regions" is a real finding (and often a decision-relevant one). Log null results in the ledger; they are what make the non-null results interpretable.
- **Chase surprises with one follow-up cut, then log and move on.** Depth-first mining of the first shiny pattern is how the sweep dies. Mark it PARKED in the ledger and finish the passes; Stage 3 is where survivors get real attention.
- **No causal or explanatory language yet.** Not "mobile drives churn" — "churn is higher in mobile-acquired users." Description of pattern, not attribution of mechanism. Explanatory verbs (drives, causes, because, due to) are banned in Stage 2 output.

**Artifact required:** the cut ledger — total cuts examined, list with one-line outcomes (including nulls), PARKED items flagged, and a closing **NOT-EXAMINED line** naming the dimensions and granularities deliberately not swept. This is the sweep's own IS-NOT column: findings are only as trustworthy as the visible boundary of where you looked, and a reader deserves to know that program mix or monthly granularity went unexamined rather than examined-and-boring.

## Stage 3 — The robustness gauntlet: try to kill every candidate finding

A pattern is interesting in proportion to **how hard you tried to make it go away and failed** (the severity principle, Mayo/Fisher). Before any candidate finding earns a status above CURIOSITY, run it through these checks — they are cheap, and each one is a common false-finding assassin:

| Check | Question | Kills |
|---|---|---|
| **Outlier dependence** | Does it survive removing the top/bottom 5 rows (or winsorizing)? | Patterns that are secretly 3 whale customers |
| **Split-half stability** | Does it hold in both halves of the time period? In odd vs. even weeks? | One-time events masquerading as structure |
| **Breadth** | Is it one micro-segment, or broad-based? Does the direction hold across most subgroups? | Simpson's-paradox reversals; cherry cuts |
| **Base size & magnitude** | Is n big enough to matter, and is the effect big enough to care? ("Conversion doubled" on 11 sessions is nothing.) | Small-denominator drama |
| **Artifact screen** | Could a tracking change, definition change, backfill, or coverage boundary produce this? Check the timing against known system changes. | Measurement ghosts — the most common false finding in analytics data |
| **Selection honesty** | Was this the biggest of many similar comparisons? If so, is it still notable *given* the ledger denominator? | Forking-paths winners |

You do not need formal statistics here (exploration is the wrong place for p-values, which the forking paths have already invalidated anyway) — you need the *adversarial habit*. Each candidate finding's gauntlet results get recorded: which checks it passed, which it failed, which weren't possible with available data.

**Artifact required:** gauntlet results per candidate finding (pass/fail/untestable per check).

## Stage 4 — Label every finding with an epistemic status

Every finding that appears in the output carries exactly one label. The labels are the whole point — they are the external prosthetic for the "possibility vs. certainty" state the model cannot natively hold, and they are what prevents the fluent-equal-confidence failure:

- **ROBUST PATTERN** — survived the full gauntlet; broad-based; artifact screen clean. Still *not confirmed* (this is exploration), but worth acting on or formally testing.
- **TENTATIVE** — survived some checks, failed or couldn't run others. State which. Worth a targeted follow-up before anyone repeats it in a meeting.
- **CURIOSITY** — striking but unvetted, or a forking-paths winner that shrinks once the denominator is attached. Explicitly labeled as possibly noise.
- **ARTIFACT SUSPECT** — the pattern is real in the data but probably reflects measurement, not behavior. Often the most *valuable* finding class (it means the data is lying to everyone else too). Route to RCA/validation.
- **NULL / BORING** — checked, nothing there. Reported when decision-relevant ("no region is underperforming" is an answer).

Findings must be **ranked by decision relevance** (per the Brief), not by statistical drama. A modest ROBUST PATTERN that touches a live decision outranks a spectacular CURIOSITY.

## Stage 5 — Report: hypotheses out, with the honesty attached

The deliverable is a **hypothesis slate**, not a conclusions memo. Requirements:

1. **Lead with a point of view.** Exploration without prioritization is the descriptive failure (accurate observations, no lede). Open with the 1–3 things that most deserve attention and why — with their status labels inline.
2. **The forking-paths disclosure, in one sentence.** "These findings were selected from N cuts examined; the full ledger is below." Non-negotiable; it's the difference between exploration and data dredging with good typography.
3. **Explicit handoffs.** Each ROBUST PATTERN or ARTIFACT SUSPECT gets a next step: "test formally via [holdout/experiment]," or "run RCA — entry hypothesis: …". Findings routed to the RCA skill should be phrased as falsifiable statements ready for its Stage 2 hypothesis list. This is where the skills compose.
4. **Permission to find nothing.** If the gauntlet killed everything, say so plainly: "Nothing in this data rises above noise given how many places we looked. That is the finding." A forced insight is worse than an honest null — and an explorer who never returns empty-handed should not be trusted.
5. **Confirmatory firewall.** If the user's next request is to *act* on a finding, restate its status label and what confirmation would require. Exploration findings do not silently upgrade to conclusions by being repeated.

## Anti-patterns (self-check before delivering)

- **A story for everything.** If every pattern in your draft has an explanation attached, you are narrating noise. Some patterns should be reported as unexplained; several should be labeled possibly-nothing.
- **Uniform confidence prose.** All findings written in the same assured register, labels missing or decorative. The register should *audibly change* between a ROBUST PATTERN and a CURIOSITY.
- **The hidden tournament.** Presenting the biggest deltas without disclosing how many comparisons produced them. If the ledger is missing, the findings are unfalsifiable.
- **Shiny-object mining.** Abandoning the sweep to drill into the first interesting pattern. That's RCA behavior smuggled into EDA — park it, finish the passes.
- **Explanatory verbs in exploratory clothing.** "Drives," "causes," "because," "due to" attached to observational cuts. Exploration describes; it does not attribute.
- **Mean-and-outlier hijack.** Averages quietly dominated by a few extreme rows; outliers silently dropped or silently included. Either way, decide visibly.
- **Coverage mirage.** Trends that start when tracking started; "growth" that is backfill; segments that appeared when a definition changed. Run the artifact screen before the champagne.
- **The obligatory insight.** Manufacturing a takeaway because returning "nothing here" feels like failure. It isn't; it's calibration.

## Output format

```
# EDA: [dataset / scope, one line]
*Mode: exploratory — output is hypotheses, not conclusions.*

## Data credentials
[grain, coverage, blind spots, quality flags]

## What deserves attention (ranked, labels inline)
1. [ROBUST PATTERN] …  → next step: …
2. [ARTIFACT SUSPECT] … → route to: RCA/validation
3. [TENTATIVE] … — passed X, untested on Y

## Findings selected from N cuts examined
[forking-paths sentence]

## Full findings & gauntlet results
[per finding: description, status, checks passed/failed/untestable]

## Cut ledger
[all comparisons examined, incl. nulls and PARKED items ·
 NOT-EXAMINED line: dimensions/granularities deliberately not swept]

## What we did not find
[decision-relevant nulls]
```

For lightweight passes the format compresses, but three elements are never optional: the mode declaration, the status labels, and the cuts-examined denominator.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| ARTIFACT SUSPECT | "this looks like a tracking/measurement issue, not real behavior — verify before anyone reports it" |
| ROBUST PATTERN | "held up under every stress-test we ran — solid enough to act on or test formally" |
| TENTATIVE | "early signal — promising, but don't repeat it in a meeting yet" |
| CURIOSITY | "interesting, quite possibly nothing — noted for honesty" |
| Forking-paths sentence / cut ledger | "we looked in about N places to find these M things — full list at the end, including where nothing turned up" |
| NOT-EXAMINED line | "what we haven't looked at yet" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"which dimension, grain, or relationship would a curious analyst poke at that no pass required?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
