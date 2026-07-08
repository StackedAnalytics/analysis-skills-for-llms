---
name: descriptive-analysis
description: >
  Structured method for reporting and characterization — "how are we doing,"
  "summarize the month/quarter," recurring performance reports, metric
  reviews, "walk me through the numbers," status updates, and profiling a
  known scope for an audience. Use this skill whenever the deliverable
  describes what happened (rather than why, what's coming, or what to do) —
  especially recurring reports, where doing description WELL is the job and
  upgrading it into something fancier nobody asked for is its own failure.
  Do NOT use for open-ended pattern hunting on unfamiliar data
  (exploratory-data-analysis), explaining a change (root-cause-analysis), or
  recommending actions (prescriptive-analysis).
---

# Descriptive Analysis

## Why this skill exists

Descriptive is the type everyone underestimates — including the other skills in this repo, which exist to prevent *errors*. Descriptive's signature failure is not an error; it is an **absence**: accurate observations with no point of view. The model produces **the tour** — a fluent walk through every metric in dashboard order ("sessions rose 3%, conversion dipped 0.2 points, email held steady…"), each observation individually correct, collectively useless. The reader is handed the raw material of a briefing and left to do the actual analysis themselves: figuring out what matters, what's normal, and what deserves attention. A tour is description that has abdicated.

Three accomplice failures fill the vacuum where the point of view should be:

- **Comparison to nothing.** Numbers reported without an expectation frame. "Conversion was 4.2%" is not information until it stands next to *compared to what* — prior period, plan, seasonal norm. Description without a baseline is recitation.
- **Noise narration.** Every wiggle gets a mini-story ("the mid-month dip was likely driven by…"). This is EDA's pareidolia wearing a monthly-report costume, and it is actively corrosive: it trains the audience to see events in routine variance, triggers investigations of nothing, and buries real signals in a sea of narrated noise. Most period-over-period movement in any metric is routine variation — Deming and Wheeler built an entire management literature on the damage done by treating it as news.
- **Uniform emphasis.** Twelve metrics, twelve sentences, equal weight — materiality absent. The one thing that matters gets a sentence indistinguishable from the ten that don't.

And the quietest failure of all: **fear of the boring report.** When nothing notable happened, the model manufactures notability, because returning "steady state" feels like underdelivery. It is the opposite: "everything within normal ranges, nothing needs your attention" is a complete, valuable, *calibrated* report — and an audience that can trust that sentence has a reporting function worth paying for.

The scaffold forces what the tour lacks: an expectation frame for every number, a statistical triage separating signal from routine variation, and a committed lede. **Description done well is an act of judgment, not transcription.**

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] Frame: audience, materiality thresholds, open loops from last period
- [ ] Expectation frame fixed for every reported number
- [ ] Variation triage complete: every movement labeled ROUTINE or SIGNAL
- [ ] Lede committed (max 3 items, or the steady-state lede)
- [ ] Proportional emphasis; loops closed; signals handed off without inline speculation
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Frame: audience, use, and materiality

Consume the Refined Question Brief if one exists. Establish:

1. **Who reads this and what they do with it.** A CMO's monthly review, an ops standup, a board packet — each implies different metrics, altitude, and vocabulary. Recurring reports serve a recurring decision (or a monitoring duty); name it.
2. **Materiality thresholds, per key metric.** What size of movement would this audience actually act on or need to know? These thresholds calibrate emphasis in Stage 5 — and they are about *decision relevance*, which is a different question from the statistical one in Stage 3. A movement can be a genuine signal and still immaterial, or material and still (so far) indistinguishable from noise; the report must be able to say either.
3. **Open loops from last period.** For recurring reports: what was flagged last time? Each open flag gets resolved, updated, or explicitly carried — reports that never close their own loops teach readers to ignore the flags.

**Artifact required:** audience + use, materiality notes, and the open-loops list.

## Stage 2 — Expectation frames: every number stands next to "compared to what"

No metric is reported naked. For each, choose the comparison frame(s) deliberately:

- **Prior period** (momentum), **plan/target** (accountability), **same period last year / seasonal norm** (context), and where relevant **the trajectory implied by trend**. Different metrics warrant different frames; the choice is made once and stated, not improvised per sentence.
- Watch the frame-shopping temptation: picking, metric by metric, whichever comparison flatters (or alarms). Frames are fixed per metric across periods; changing one is a visible, explained event.
- Denominator hygiene applies (rates vs. counts, consistent definitions period over period) — and any definition or tracking change in the window is disclosed *with the numbers it affects*, because a definition change narrated as performance is the reporting version of the measurement-artifact failure.

**Artifact required:** the metric table — value, frame(s), delta against each frame.

## Stage 3 — Variation triage: signal or routine? (the central discipline)

Before any movement earns narrative, classify it — this is statistical process control's core distinction (Shewhart; Wheeler's *Understanding Variation*), and it is the single highest-leverage import in this skill:

1. **Establish each metric's routine variability** from its own history: the range of normal period-over-period movement (a simple approach — the distribution of historical deltas, or XmR-style natural process limits — beats no approach; precision matters less than having limits at all).
2. **Classify every movement:**
   - **ROUTINE** — within natural limits. Reported as within normal range, *once, collectively* ("the remaining nine metrics moved within their normal ranges"). Routine variation gets **no narrative, no causes, no story**. This rule does more to raise report quality than any other.
   - **SIGNAL** — outside natural limits, or a run/pattern history says is rare (e.g., seven consecutive periods same direction). Signals get attention, narrative, and — where cause matters — a handoff.
3. **Signals get described, not explained.** The descriptive report states what the signal is, its size, its frame, and its signal status. Cause is RCA's job: route it as a falsifiable entry ("purchase conversion on mobile web fell outside natural limits beginning the 14th → RCA") rather than inlining a speculative cause. If a likely cause is *known and verified* (a launched campaign, a price change), it may be stated as context, labeled as such — but "likely due to…" guesses are banned; they are noise narration with confidence.

**Artifact required:** the triage — each movement labeled ROUTINE or SIGNAL, with the basis for the limits noted once.

## Stage 4 — Commit to the lede

The report opens with the point of view (Minto's answer-first; the briefer's bottom-line-up-front):

- **The 1–3 things this audience most needs to know, stated first, each with its "so what."** Not the first metrics in the dashboard — the most material signals (or the most material *absences* of signals).
- **The steady-state lede is legitimate and complete:** "Everything tracked is within normal ranges; nothing this period needs your attention. Two items to watch: …" An analyst who will say this earns the credibility that makes their non-boring ledes land.
- The lede is written *after* Stages 2–3 and is constrained by them: nothing appears in the lede that isn't a SIGNAL, a materiality-threshold crossing, an open-loop resolution, or a genuinely decision-relevant steady-state confirmation.

**Artifact required:** the lede, ≤3 items, each with its so-what.

## Stage 5 — Proportional emphasis: structure follows materiality

Build the body as a pyramid under the lede:

- **Wordcount tracks materiality.** Signals and threshold-crossings get paragraphs; routine variation gets one collective sentence; the full detail lives in the metric table, present but not narrated.
- **Group by story, not by dashboard order.** Supporting detail clusters under the lede point it supports; the report's structure *is* its argument.
- **Close the loops:** last period's flags get their update in a visible, consistent place.
- **Keep the descriptive/interpretive boundary visible:** observations plainly stated; verified context labeled as context; anything requiring diagnosis, forecast, or recommendation handed off to its skill rather than smuggled in as narration.

## Anti-patterns (self-check before delivering)

- **The tour.** Metrics narrated in dashboard order with uniform weight. If your draft's structure matches the dashboard's, the analysis hasn't happened yet.
- **Comparison to nothing.** A number without a frame. Every value stands next to its "compared to what."
- **Noise narration.** Stories attached to routine variation; "likely due to" speculation on wiggles inside natural limits. The triage exists to make this impossible.
- **The buried lede.** The one signal that matters appearing in paragraph six, after four paragraphs of routine metrics. Materiality order, not dashboard order.
- **Manufactured notability.** Inflating routine movement into news because "steady state" feels like underdelivery. The boring report, honestly delivered, is the product.
- **Frame shopping.** Rotating comparison baselines to flatter or alarm. Frames are fixed and changes are announced.
- **Inline causal speculation.** Guessed mechanisms narrated as context. Signals route to RCA; verified context gets labeled.
- **Emphasis inflation.** Everything "notable," everything bolded, every section a highlight. If everything is a signal, the triage failed.
- **The unclosed loop.** Flags raised last period, never mentioned again. Recurring reports keep their own books.
- **Template inertia.** The same narration skeleton every period regardless of what happened — the surest sign the report is being transcribed, not written.

## Output format

```
# [Period] report: [scope]

## Bottom line
[1–3 lede items with so-whats — or the steady-state lede]

## Signals & threshold items
[each: what, size, frame, signal basis · verified context labeled ·
 RCA/other handoffs as falsifiable entries]

## Open loops
[last period's flags: resolved / persisting / carried]

## Within normal ranges
[one collective sentence naming the routine movers]

## Metric table
[value · frame(s) · delta · ROUTINE/SIGNAL — complete, unnarrated]
```

For lightweight updates the format compresses, but three elements are never optional: an expectation frame on every reported number, the routine/signal triage, and a committed lede — including the steady-state lede when that's the truth.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| SIGNAL | "genuinely unusual for this metric — worth your attention" |
| ROUTINE (within natural limits) | "normal fluctuation — no story, no action" |
| Natural process limits / triage basis | "outside its normal range, based on its own history" |
| Steady-state lede | "nothing needs your attention this period — here's what we're watching" |
| Open loops | "updates on what we flagged last time" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"what did you notice while computing the metrics that no triage required — the quirks readers eventually ask about?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
