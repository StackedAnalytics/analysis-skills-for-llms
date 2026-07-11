---
name: question-refinement
description: >
  Intake discipline for data analysis requests: figure out what is actually
  being asked before analyzing anything. Use this skill when the analysis
  type is AMBIGUOUS or the request needs reconstruction before work can
  start: a bare data pull or report request ("pull X," "show me Y by Z,"
  "look into the numbers"), a request with an implied cause or solution
  baked in, a metric that is a proxy for something else, or an unclear
  decision behind the ask. The output is a refined question brief that
  routes to the appropriate analysis skill (RCA, EDA, comparative, etc.).
  Do NOT use this when the request already clearly matches one analysis
  type — those skills run their own inline intake triage — and do NOT
  re-run it for follow-ups inside an already-scoped analysis where the
  brief still holds: refine once, then work.
---

# Question Refinement

## Why this skill exists

LLMs handed an analysis request exhibit **obliging literalism**: they answer the question as asked, immediately, thoroughly, and with confidence. This feels like helpfulness. It is frequently the least helpful possible move, because analysis requests are systematically not the real question.

Here is the mechanism. Before anyone asks an analyst (human or LLM) for anything, they have already run an amateur analysis in their head: they have a real problem → they've guessed at a cause → they've guessed what data would confirm the guess → they ask for *that data*. You receive the **last link of a private reasoning chain**. "Can you pull conversion rate by channel for the last 90 days?" is not a question; it is the residue of an unstated one — perhaps "the CMO thinks paid is underperforming and I need to know if she's right before Thursday's budget meeting." Answering the literal request means executing someone's guess with none of their context, and inheriting every error in the chain you never saw.

Human reference librarians formalized this decades ago as the *reference interview*, after establishing empirically that the question patrons ask is reliably not the question they need answered. Senior analysts do the same thing instinctively. LLMs do not, because pushing back on a request feels like non-compliance and because they can't tolerate leaving a question unanswered in the current turn. This skill is permission and procedure to **not answer the question yet** — briefly, cheaply, and without becoming an interrogation.

The quality of the question predicts the quality of the outcome, because the question determines the analysis type, and the analysis type determines the method. Get the question wrong and everything downstream is well-executed waste.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete. In deliverables, the completed checklist belongs in the workings layer ("How we checked this"), not at the top of the document:

```
- [ ] Triage path chosen: INFER / DECLARE / ASK
- [ ] Decision anchor established (or "no decision" noted)
- [ ] Pathology screen run: presupposed-solution / proxy / unanswerable-as-scoped
- [ ] Analysis type classified on intent markers (sequence declared if applicable)
- [ ] Refined Question Brief written with CONFIRMED vs ASSUMED split
- [ ] Beyond-the-scaffold pass done; quirks log kept
- [ ] Decision log maintained (choice / alternative / why / USER-SETTABLE); verdict-shaping decisions surfaced
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Triage: infer, declare, or ask

Not every request deserves an interview. Full clarification of every request is its own failure mode ("interrogation theater") — it burns goodwill, and users start ignoring the questions. Route every request through this gate:

**INFER (say nothing, just proceed)** when the literal request and the real question are plausibly identical AND getting it wrong is cheap:
- Genuinely mechanical asks with self-evident purpose ("export last month's orders to CSV").
- Follow-ups inside an established analysis where context is already loaded.
- Requests where any reasonable interpretation leads to the same work.

**DECLARE (state your interpretation, then proceed — the default for everything else)**:
- Restate the request as the question you believe is actually being asked, name the analysis type you're bringing, state the key assumptions, and *proceed without waiting*.
- Format: *"I'm reading this as a diagnostic question — why did mobile conversion drop — rather than a reporting request, so I'll run it as a root-cause analysis. I'm assuming the June numbers you mentioned are the trigger. Flag me if you meant something else."*
- This captures most of the value of asking at near-zero conversational cost. The user corrects you only if you're wrong, and the correction itself surfaces the hidden context.

**ASK (stop and clarify before working)** only when a genuine fork exists — i.e., different plausible answers route to *different analysis types or materially different work* — AND proceeding down the wrong branch wastes significant effort or produces something misleading:
- The decision the analysis informs is invisible and would change scope/precision requirements.
- The request names a proxy metric and the underlying concern is ambiguous ("look at engagement" — churn risk? content performance? feature adoption?).
- The request presupposes a cause or solution and executing it would foreclose the real investigation.
- Constraints matter and are unknown (deadline, audience, data access).

When you do ask: **maximum two or three questions, decision-oriented, with candidate answers offered** ("Is this for the Thursday budget decision, ongoing monitoring, or something else?"). Offering candidates makes answering nearly effortless and demonstrates you've thought about it. Never send an unstructured wall of clarifying questions.

## Stage 2 — The interview core: walk the chain backward

Whether declaring or asking, reconstruct the reasoning chain behind the request. Three moves, in priority order:

### 2a. Anchor to the decision

The single highest-value question in analysis intake (per Hubbard's decision-first measurement discipline):

> **"What will be done differently depending on the answer?"**

Ask it (or infer the answer) because it does four jobs at once:
- **Separates decisions from curiosities.** Both are legitimate, but they warrant different investments and different outputs.
- **Reveals the real stakeholder.** The requester is often an intermediary; the decision-owner's needs govern, not the messenger's phrasing.
- **Sets required precision.** Many decisions flip on a directional answer ("is it getting worse?"); others need defensible point estimates. Analysis calibrated to the wrong precision is either wasted effort or unusable.
- **Exposes questions with no decision attached** — which should be flagged as exploratory/monitoring, scoped accordingly, and not gold-plated.

If no decision exists, that is a finding, not a failure. Say so: "This appears to be situational awareness rather than a decision input — I'll keep it light unless something surprising turns up."

### 2b. Screen for the three question pathologies

From the reference-interview tradition, adapted. Check every request against these; each has a signature and a corrective move.

**The presupposed-solution question.** The request embeds a guessed cause or a guessed remedy. *Signature:* the request is oddly specific about method or cut ("pull conversion by channel," "check if the new landing page is the problem"). *Move:* honor the specific ask, but reattach it to the open question — "I'll check the landing page, and since the real question seems to be why signups dropped, I'll also test the other usual suspects so we don't stop at the first plausible story." Never *only* execute the presupposition: confirming a guess without testing alternatives is premature convergence outsourced to the requester.

**The compressed/proxy question.** A measurable stand-in for something unmeasurable or unarticulated. *Signature:* abstract metric words — engagement, health, performance, quality, "how are we doing." *Move:* decompress before measuring. "Engagement" for a subscription business usually means "are customers about to churn"; for content it means "is anyone consuming this." State the decompression explicitly in the brief; measuring the proxy without naming the referent produces numerically correct, semantically empty answers.

**The unanswerable-as-scoped question.** The question as posed cannot be answered with available data, or at all ("did the rebrand cause the lift?" with no control, no baseline, confounded launch timing). *Signature:* causal certainty demanded from observational data; comparisons with no comparator; effects with no counterfactual. *Move:* do NOT oblige with false confidence, and do not just refuse. Offer the answerable adjacent question: "We can't isolate the rebrand's causal effect with this data, but we can establish whether the lift is concentrated where the rebrand was most visible, which is weaker but real evidence." Naming what the data cannot support is one of the most valuable outputs an analyst produces.

### 2c. Capture constraints

Deadline, audience (analyst peer vs. executive vs. board), data actually available, and sensitivity. These don't change the question but they change what "answered" looks like. Infer from context where possible; this is rarely worth a standalone clarifying question unless stakes are high.

## Stage 3 — Classify the analysis type on intent, not surface form

The grammatical form of a request is a poor predictor of its analytical type. "Show me revenue by region" is descriptive in form but is usually comparative (which region is the problem?) or diagnostic (what's dragging the total?) in intent. Classify on **intent markers**:

| Marker present in request/context | Route to |
|---|---|
| A surprise, change, drop, spike, or discrepancy ("why did…", "what happened to…", "these don't match") | **Diagnostic / RCA** |
| An option set or a choice to be made ("which is better," "should we," "A vs. B") | **Comparative** (evidence) → **Prescriptive** (recommendation) |
| A number needed for a plan or commitment ("what should we expect," "will we hit…") | **Predictive** |
| No specific expectation; unfamiliar data; "anything interesting," "poke around," "get a feel for" | **Exploratory / EDA** |
| A claim, report, or dataset whose correctness is in question ("does this look right," "why don't these tools agree") | **Evaluative / validation** |
| Recurring informational need, no decision fork ("weekly numbers," "how are we doing") | **Descriptive** — resist upgrading it into something fancier |

Two rules that prevent most misroutes:

- **The sequencing rule.** Many real requests are honestly a *sequence*, and saying so is the correct classification: "This is exploratory now — we don't yet know if anything is wrong — and becomes diagnostic if we find something." Declare the sequence and the trigger for the handoff rather than forcing a single type.
- **The upgrade check.** When a request classifies as descriptive, check once for a hidden decision (2a). If none, deliver descriptive work well — with a point of view, not a data dump — instead of inventing a deeper question no one asked. Over-classification is as real a failure as under-classification.

## Stage 4 — Output contract: the Refined Question Brief

Produce this brief before (or as the header of) any analysis. It is the entry artifact for downstream skills — the RCA skill's problem specification and the EDA skill's mode declaration consume it directly.

```
## Question brief
- Real question (one sentence): …
- As originally asked: "…" [verbatim]
- Decision this informs & owner: … (or: "none — situational awareness")
- Analysis type: … (or sequence: X → Y, handoff trigger: …)
- "Answered" looks like: [directional / estimate / defensible number],
  at [confidence needed], by [deadline], for [audience]
- In scope / out of scope: …
- CONFIRMED with requester: …
- ASSUMED (correct me): …
```

The **CONFIRMED vs. ASSUMED split is mandatory.** Assumptions made at intake are the sensitivity statement of the entire framing: if an assumption is wrong, everything downstream flips, and the requester can only catch it if the assumption is visible. Silent assumptions are how well-executed analyses answer the wrong question.

For lightweight requests the brief compresses to two sentences of the DECLARE pattern — but the real question, the type, and the load-bearing assumption must always be stated somewhere.

## Anti-patterns (self-check)

- **Obliging literalism.** Executing the request as phrased with no reconstruction of intent. The politest form of answering the wrong question.
- **Interrogation theater.** Opening with 5+ clarifying questions, or asking things the context already answers. Erodes trust in the questions that matter; DECLARE exists precisely to avoid this.
- **Answering the proxy.** Measuring "engagement" without ever stating what it's standing in for. Numerically correct, semantically empty.
- **Executing the presupposition.** Testing only the requester's embedded guess. If the request names a suspect, the real question is still "whodunit," not "did this suspect do it."
- **Form-based classification.** Routing "show me X by Y" to descriptive because the verb is "show." Classify on intent markers, not grammar.
- **The false-confidence oblige.** Answering an unanswerable-as-scoped question as if the data supported it. Offer the answerable adjacent question instead.
- **Question-refinement as stalling.** The output of this skill is a *better analysis*, not a philosophy seminar. If you can DECLARE and proceed, do; reserve full interviews for genuine forks. Bias toward motion with visible assumptions.

## Communicating results (two layers)

The vocabulary above is enforcement machinery, not deliverable prose. Output splits into two layers:

**Layer 1 — the deliverable.** Plain business language, lede first, no skill vocabulary. The reader should not be able to tell a "skill" was involved — only that the analysis is unusually clear about what is solid and what is not. Every calibration distinction survives translation: translating a label is required; smoothing it into uniform confident prose is the exact failure the label exists to prevent.

**Layer 2 — the workings.** All required artifacts, unchanged and still mandatory, under a plain heading such as "How we checked this" — appended to documents, offered on request in chat. The completed progress checklist lives here, never at the top of the deliverable.

**Audience dial:** the Brief's audience field governs. Default to plain language; use internal vocabulary in the deliverable body only for an analyst peer who has asked for it.

Translations for this skill's vocabulary:

| Internal | Reader-facing |
|---|---|
| Refined Question Brief | "Here's the question I'm answering, and what I'm assuming — correct me if I've got it wrong" |
| DECLARE path | just say it conversationally: "I'm reading this as X — flag me if you meant otherwise" |
| Presupposed-solution / proxy pathologies | never name the pathology; perform the reattachment or decompression in plain words |
| CONFIRMED / ASSUMED split | "You told me… / I'm assuming… — say the word if either is off" |

## Floor, not ceiling — and the decision log

Two failure modes live in this scaffold itself, both observed in field evals; both get mechanisms.

**1. The stages are a floor of discipline, never a ceiling of effort.** A completed checklist with no findings beyond what the stages demanded is a signal of satisficing, not success. Two mechanisms:

- **Beyond-the-scaffold pass (required).** After the required artifacts, take one deliberate unscripted pass — for this skill: *"what about this request would a veteran of this stakeholder's asks find odd or telling, that no triage step asked about?"* — and log its cuts and checks in the same ledger as everything else. Curiosity is made an artifact here because nothing else in this repo survives contact with a checklist.
- **Quirks log (required, cheap).** Everything odd noticed *in passing* — weird nulls, sentinel values, suspicious joins, columns that don't mean what their names say, grains that surprised you — recorded even when not analyzed. This is the messy-data knowledge analysts accumulate; suppressing it because no artifact asked is how a scaffolded analysis ends up knowing less than a wandering one. Quirks feed the engagement's overlay file.

**2. Method decisions belong to the user.** Executing the stages forces choices — filters, exclusions, thresholds, windows, scopes, bases, dedup rules. Log every one *as it is made* in a **decision log**: what was chosen, the credible alternative, why, and a **USER-SETTABLE** flag wherever a reasonable user might choose differently. Then triage, don't interrogate: the 1–3 decisions that shape the verdict are surfaced in the deliverable itself ("choices you might make differently — I proceeded with X; on Y the answer changes as follows") or, in chat, declared as they are encountered; the rest live in the workings. A silent methodological choice is a silent basis in miniature — this is the general rule that catches the next instance before a field test has to.

**Anti-patterns:** *checklist satisficing* (artifacts complete, curiosity absent) and *the manufactured silent decision* (a choice made only so the stage could proceed, never logged).

**Artifacts required:** the beyond-the-scaffold cuts (in the ledger), the quirks log, and the decision log with USER-SETTABLE flags — all in the workings layer, with the verdict-shaping decisions surfaced up front.
