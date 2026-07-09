---
name: root-cause-analysis
description: >
  Structured method for diagnosing why a metric, system, or process changed —
  drops, spikes, anomalies, discrepancies, regressions, or "why did X happen"
  questions. Use this skill whenever the task involves explaining an observed
  change or difference, even if the user doesn't say "root cause": questions
  like "why did conversions drop," "what's driving this spike," "why don't
  these two numbers match," or "something broke, figure out what" all qualify.
  Do NOT use for open-ended exploration of unfamiliar data (use an EDA skill)
  or for forward-looking "what will happen" questions.
---

# Root Cause Analysis

## Why this skill exists

LLMs performing diagnosis exhibit a characteristic failure: **premature convergence**. The first plausible hypothesis written down begins to organize every subsequent observation around itself. Evidence gets read as confirmation; alternatives stop being generated; the analysis becomes an essay defending an early guess. This is not a knowledge problem — it is a structural consequence of generating text sequentially without a native way to hold several hypotheses at partial confidence simultaneously.

This skill compensates by externalizing epistemic state into **required artifacts**. You cannot reliably *hold* five hypotheses at 20% confidence each, but you can *maintain a table* that does it for you. Every stage below produces an artifact. Producing the artifact is not optional paperwork — the artifact IS the reasoning discipline. If you find yourself confident in a cause before the artifacts are built, treat that confidence itself as a symptom of the failure mode.

Do the stages in order. Do not skip ahead even when the answer seems obvious. Obvious answers that are correct survive the process cheaply; obvious answers that are wrong are exactly what the process exists to catch.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] IS/IS-NOT specification built, UNKNOWNs flagged
- [ ] 6+ hypotheses enumerated across 4+ categories (incl. measurement artifact)
- [ ] Evidence x hypothesis matrix scored, rows basis-tagged (measured/reported/assumed); diagnostic items identified
- [ ] Disconfirmation pass written (falsifier check + runner-up steelman)
- [ ] Conclusion: contributions / confidence / sensitivity / residual / verification
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Specify the problem (before any hypothesizing)

Adapted from Kepner-Tregoe Problem Analysis. Before asking *why*, pin down precisely *what*. Most bad RCA starts by explaining a problem that was never accurately described.

Build the **IS / IS-NOT specification**:

| Dimension | IS (observed) | IS-NOT (could be, but isn't) |
|---|---|---|
| What | What exactly changed? Which metric, at what magnitude? | What similar metrics did NOT change? |
| Where | Which segments, platforms, geographies, channels? | Which comparable segments are unaffected? |
| When | When did it start? Sudden or gradual? Recurring pattern? | When was it NOT happening? Does it pause/recover? |
| Extent | How big? Trend, step change, or one-time event? | How big is it NOT? (e.g., "down 40%, not 100%") |

Rules for this stage:

- **Quantify everything.** "Conversions dropped" is not a specification. "Web checkout conversion fell from 3.1% to 1.9% starting June 14, mobile web only, paid channels only, desktop and app unaffected" is.
- **The IS-NOT column is the most valuable real estate in the entire analysis.** Every entry is a free hypothesis-killer: a valid cause must explain the *boundary* of the problem, not just its existence. A hypothesis that explains why mobile dropped but not why desktop held steady is incomplete.
- If you cannot fill in a cell, mark it **UNKNOWN** and list it as a data-gathering question. Do not silently guess.
- If the data available cannot support the specification (e.g., no segment breakdown exists), say so explicitly. An honest "we cannot localize this yet" beats a confident diagnosis of an unspecified problem.

**Artifact required:** the completed IS/IS-NOT table, with UNKNOWNs flagged.

## Stage 2 — Enumerate hypotheses (before evaluating any of them)

Generate the candidate set *completely* before assessing *any* candidate. Evaluation contaminates generation: once you start weighing evidence for hypothesis A, you stop generating hypotheses B through F.

Requirements:

- **Minimum six hypotheses**, spanning at least four of these categories (fishbone-derived, adapted for data/analytics contexts):
  1. **Measurement artifact** — tracking broke, tag changed, bot filtering changed, definition changed, pipeline failure, timezone/attribution window shift. *This category is mandatory in every RCA.* In analytics work, the "change" is an artifact of measurement — not real behavior — an embarrassingly large fraction of the time.
  2. **Mix shift** — composition changed, not performance. Overall rate moved because the blend of segments moved (Simpson's paradox territory).
  3. **Internal change** — deploys, pricing, site changes, campaign launches/pauses, budget shifts, policy changes.
  4. **External event** — competitor actions, seasonality, holidays, weather, news, platform algorithm changes, regulation.
  5. **Genuine behavior change** — real shift in user/customer behavior.
  6. **Interaction/conjunction** — two or more of the above combining (e.g., a small real drop amplified by a tracking gap).
- Write each hypothesis as a **falsifiable statement**, not a theme. Not "maybe tracking" but "the June 13 GTM container publish broke the purchase event on mobile web."
- Include at least one hypothesis you consider unlikely. The point of enumeration is to protect against your own priors.
- **Do not rank, weigh, or editorialize yet.** No "most likely," no "probably." The list is deliberately flat.

**Artifact required:** the numbered hypothesis list with category labels.

## Stage 3 — Build the evidence matrix (Analysis of Competing Hypotheses)

Adapted from Heuer's ACH. Now gather evidence and score it against **every** hypothesis simultaneously — never against one hypothesis at a time.

Build the matrix: rows = evidence items, columns = hypotheses. Each cell gets one of:

- **C** — consistent with this hypothesis
- **I** — inconsistent with this hypothesis
- **N** — neutral / not diagnostic for this hypothesis
- **?** — untested; we haven't checked

Rules that carry most of the value:

- **Diagnosticity over consistency.** Evidence consistent with *all* hypotheses is worthless, no matter how vivid or compelling it feels. The evidence that matters is evidence that *discriminates* — consistent with some columns and inconsistent with others. After filling the matrix, explicitly identify which evidence rows are diagnostic and disregard the rest when concluding. (Every IS-NOT entry from Stage 1 should appear here as an evidence row — they are usually the most diagnostic rows you have.)
- **Seek to eliminate, not to confirm.** Your working question for each hypothesis is "what would prove this false, and did I check?" The conclusion will be reached by elimination: the hypothesis with the least inconsistent evidence wins — not the one with the most consistent evidence. Those are different questions, and confusing them is the confirmation-bias engine.
- **"?" cells are findings.** A column full of ?s means you have not tested that hypothesis, not that it is false. Before concluding, either resolve the critical ?s or name them as limitations.
- **Every evidence row carries a basis tag: MEASURED** (queried or verified directly), **REPORTED** (someone's claim — a vendor's explanation, a stakeholder's account), or **ASSUMED**. Evidence credibility is first-class in ACH for a reason: a matrix that weighs a vendor's story and a ground-truth query as equal rows will eliminate the wrong hypotheses. Reported claims that carry a prediction ("it's a competitor surge — it will revert") are held to that prediction, not re-accepted each period.
- If you have tool access (SQL, data files, logs), the matrix tells you what to query next: prioritize checks that are diagnostic across multiple columns. If you don't have data access, the ?-cells become your list of questions for the user.

**Artifact required:** the evidence × hypothesis matrix with every row basis-tagged (measured / reported / assumed), plus one sentence identifying the most diagnostic evidence.

## Stage 4 — Disconfirmation pass

Before writing any conclusion, attack your own leading hypothesis:

1. State the current leading hypothesis.
2. State **what evidence would falsify it** — concretely, not rhetorically.
3. Answer: **did you actually look for that evidence?** If no, and you can look, look now. If you can't look, the conclusion must carry that caveat.
4. State the **strongest case for the runner-up hypothesis** as if you were advocating for it. If you can't construct a serious case for any alternative, either the evidence is genuinely decisive or your enumeration was too weak — decide which, honestly.
5. Check the boundary: does the leading hypothesis explain every IS-NOT? Each unexplained IS-NOT is a standing objection.

**Artifact required:** the four answers above, written out.

## Stage 5 — Conclude with structure, sensitivity, and residual

Real incidents are usually conjunctions, not culprits. The question "what was THE root cause" grammatically demands a single answer; resist the grammar.

The conclusion must contain all five of these elements:

1. **Causal structure with contribution estimates** — e.g., "~70% of the drop is the June 13 tag regression; ~20% is normal seasonal decline that the regression made look worse; ~10% unexplained." Rough numbers are fine; the discipline is the decomposition itself. If it genuinely is one cause, say so — but arrive there, don't assume it.
2. **Confidence level with justification** — high/medium/low, tied to the diagnosticity of the evidence, not to the coherence of the narrative.
3. **Sensitivity statement** — which specific evidence items the conclusion depends on most, *with their basis tags*. "This conclusion rests critically on the GTM version history and the app-vs-web comparison; if the version timeline is wrong, the conclusion flips." A conclusion resting on two measured items reads differently — and should — than the same conclusion resting on one measured item and one reported claim. This tells the reader exactly what to verify, and how much verifying it needs.
4. **Unexplained residual** — what the leading explanation does *not* account for. Stating the residual is the single strongest defense against narrative smoothing. "Fully explained" conclusions in messy data are usually over-fitted stories.
5. **Verification/next steps** — the cheapest test that would confirm or kill the conclusion (e.g., "republish the prior container version in a debug environment and replay a test purchase").

## Anti-patterns (self-check before delivering)

- **The confident opening.** If your draft's first sentence names the cause, you likely converged before analyzing. The specification comes first — including in the write-up.
- **Evidence narration.** Walking through evidence as a story ("first we noticed X, which suggested Y...") is the anchoring failure in prose form. The matrix exists precisely to prevent story-ordering of evidence.
- **Consistency stacking.** Ten pieces of evidence consistent with your hypothesis prove nothing if they're also consistent with three others. Count inconsistencies against alternatives, not confirmations of your favorite.
- **5-Whys as primary method.** 5-Whys assumes a single causal chain and drills depth-first — it is premature convergence, formalized. Use it only *after* Stages 1–4 have selected a cause, to trace that cause's upstream origins.
- **Silent artifact-skipping.** If any required artifact is missing from your output, the analysis is incomplete regardless of how convincing the conclusion reads.
- **Manufactured uncertainty.** The inverse failure: if after honest work the evidence is decisive, say so plainly. The goal is calibration, not hedging theater.

## Output format

Deliver the analysis in this order (artifacts inline, not appendixed):

```
# RCA: [one-line problem statement]

## Problem specification
[IS/IS-NOT table, UNKNOWNs flagged]

## Hypotheses considered
[numbered list with categories]

## Evidence
[evidence × hypothesis matrix, rows basis-tagged (measured/reported/assumed);
 note on most diagnostic items]

## Disconfirmation
[falsifiability check + strongest runner-up case]

## Conclusion
[causal structure w/ contributions · confidence · sensitivity ·
 unexplained residual · verification steps]
```

For quick/interactive contexts a compressed version is acceptable, but the five conclusion elements and the IS-NOT boundary check are never optional.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| IS/IS-NOT specification | "what's affected — and, just as important, what isn't" |
| Evidence × hypothesis matrix; diagnosticity | "what we checked, and which checks actually ruled things out" |
| MEASURED / REPORTED / ASSUMED tags | "verified directly" / "per [source] — not independently verified" / "assumed" |
| Disconfirmation pass | "what would prove us wrong — we looked for it" |
| Sensitivity statement | "this conclusion hinges on X and Y; if either is wrong, the answer changes" |
| Unexplained residual | "what this doesn't explain (about Z% — noted, not solved)" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"what else looks off in this system beyond what any hypothesis needed — and does it change the hypothesis set?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
