---
name: prescriptive-analysis
description: >
  Structured method for recommendation and decision-support requests — "what
  should we do," "should we cut/keep/switch/buy X," "which option do you
  recommend," vendor selections, budget reallocations, go/no-go calls. Use
  this skill whenever the deliverable is a recommendation or a choice among
  actions, including when the request arrives pre-leaning ("should we finally
  kill X?"). This skill consumes the outputs of the other analysis skills
  (comparative, causal-impact, predictive) — it is where evidence becomes
  advice. Do NOT use for pure evidence questions with no action attached
  (comparative / causal-impact) or for requests that only need a forecast
  (predictive-analysis).
---

# Prescriptive Analysis

## Why this skill exists

Prescriptive is where every other analysis converges — and where an LLM's deepest behavioral bias lives. The signature failure is **sycophancy**: recommendation requests almost never arrive neutral. "Should we finally cut paid social?" carries its desired answer inside it, and the model — trained to be agreeable, fluent at building cases — senses the lean and constructs the recommendation the framing implies, complete with supporting evidence assembled after the conclusion. The result reads like analysis and functions like an echo.

Four accomplice failures make the echo convincing:

- **Option-set capture.** The model chooses among the options *offered*, as if they were the universe. It almost never adds the options that discipline a decision: *do nothing*, *wait and buy information*, or anything outside the requester's frame. A choice between two options is frequently a false dilemma that a third option dissolves.
- **Criteria back-fit.** The model evaluates options first and articulates criteria afterward — so the criteria always happen to favor the recommendation. Real decision discipline runs the other way: objectives and weights stated *before* any option is scored (the same enumeration-before-evaluation principle as RCA, applied to values instead of hypotheses).
- **Certainty laundering.** Upstream uncertainty — a rung-3 causal estimate, a comparison indistinguishable from noise, a forecast interval — silently vanishes at the recommendation step. "The data suggests X might outperform" becomes "switch to X." The recommendation inherits none of the humility of the evidence it stands on.
- **Risk flatness.** Options get compared on expected value alone, ignoring reversibility and downside shape. A modest-EV two-way door and a higher-EV one-way door are not comparable on their means — and "you can always undo it" is frequently false in ways the model doesn't check (audiences decay, teams disband, contracts bind, algorithms lose their learning).

The stance this skill enforces: **a recommendation is a conclusion that survives having wanted the opposite.** The analysis must be constructed so that, had the requester's lean been reversed, the same evidence and the same criteria would produce the same advice. And per this repo's calibration principle, the antidote to sycophancy is *not* refusing to recommend — a hedge-everything "here are some options to consider" response is its own failure when a recommendation was requested. The goal is a direct recommendation with its dependencies exposed.

## Progress checklist

Copy this into the response and check items off as the artifacts are produced -- an unchecked item at delivery time means the analysis is incomplete:

```
- [ ] Criteria and weights frozen (each CONFIRMED or ASSUMED) before any option is evaluated; framing pressure noted
- [ ] Option set widened: status quo, information-buying, at least one out-of-frame option
- [ ] Consequence table built with evidence labels carried in; UNKNOWNs explicit; upstream forks kept forked
- [ ] Risk & reversibility pass: door type + downside shape per option
- [ ] Stress test: pre-mortem / runner-up steelman / sycophancy test answered in writing
- [ ] Direct recommendation with load-bearing weights, flip conditions, and tripwires
```

If unsure what good looks like at any stage, read [references/worked-example.md](references/worked-example.md) -- a compressed end-to-end run of this skill.

## Stage 1 — Frame the decision and fix the criteria (before touching options)

Consume the Refined Question Brief. Establish, in order:

1. **The actual decision and its owner.** What is being decided, by whom, by when, and is it one decision or several tangled together? The analysis advises; the owner decides — built correctly, any disagreement at the end should localize to *weights*, not facts.
2. **Framing-pressure check, stated in the output.** Does the request lean? ("Should we finally…", "make the case for…", "leadership wants to…"). Name it, then design symmetric: the analysis must be equally capable of recommending against the lean.
3. **Objectives and weights, committed now.** What is being optimized — revenue, efficiency, risk reduction, speed, optionality — and what's the rough priority order when they conflict? Include the unstated-but-real criteria (political capital, team morale, contract exposure) explicitly; leaving them implicit is how they secretly dominate. Mark each criterion and weight **CONFIRMED** (the owner said it) or **ASSUMED** (the analyst inferred it) — the intake skill's split, applied at the one stage where a wrong assumed weight silently flips the recommendation; assumed weights that prove load-bearing in Stage 6 get surfaced for confirmation, not defended. These criteria are frozen before options are evaluated. If evaluation later reveals a missing criterion, adding it is fine — *visibly*, with a note that it changes the frame.
4. **Constraints vs. preferences.** Hard constraints (budget ceiling, compliance, deadline) filter options; preferences trade off. Do not let preferences masquerade as constraints — that's how option sets get artificially narrowed.

**Artifact required:** decision + owner + deadline, the framing-pressure note, and the weighted criteria list — each criterion marked CONFIRMED or ASSUMED — timestamped before evaluation.

## Stage 2 — Widen the option set

The offered options are a starting point, never the universe. Mandatory additions before evaluation:

- **Status quo, honestly costed.** "Do nothing" is always an option and is the baseline every other option must beat — including the cost of deciding later with more information.
- **The information-buying option.** Per value-of-information thinking: would a cheap test, pilot, or short delay materially improve the choice? "Run a 6-week geo-holdout, then decide" is frequently the highest-value option on the table, and models never generate it unprompted. Weigh it seriously — but see the analysis-paralysis anti-pattern: information-buying must name what will be learned, by when, at what cost, and what decision rule follows.
- **At least one option outside the offered frame.** Apply the vanishing-options test (Heath): "if none of the offered options were available, what would we do?" Restructures, partial versions, hybrids, and renegotiations live here.
- **No strawmen.** Every option in the table gets steelmanned enough to genuinely compete. An option added to make the favorite look good corrupts the table.

**Artifact required:** the widened option list, with additions labeled as such.

## Stage 3 — The consequence table (uncertainty carried, not laundered)

Build the central artifact: **options × criteria**, each cell filled with the best available evidence *at its native uncertainty*:

- Cells cite their source and strength: causal estimates carry their **rung label**, comparisons carry their **distinguishable-from-noise status**, forecasts carry their **intervals**. This is where the skills compose — and where laundering is prevented structurally, because the table format demands the label travel into the cell.
- **Conditional evidence stays forked.** When an upstream analysis delivers a basis- or construction-conditional result ("under basis A, X wins; under basis B, Y wins"), the fork enters the table *as a fork* — two labeled cell values — never collapsed to the analyst's preferred branch. If the fork flips the leading option, route it to the machinery built for it: the owner's fork (when the branch choice is a judgment the decision-owner holds) or the information-buying option (when resolving the basis is cheap and decisive — it frequently is, and "resolve the basis" is often the best information purchase on the table).
- Cells with no evidence say **UNKNOWN**, not a guess in evidence's clothing. A column of UNKNOWNs is itself an argument for the information-buying option.
- Where a cell is an estimate, prefer ranges to points (the predictive skill's discipline, inherited).
- **Dominance check:** an option worse-or-equal on every criterion is eliminated and said so; if one option dominates outright, the decision is easy and the table proves it. Most real tables show trade-offs — which is the point: the table converts "which is better" into "which trade-off do we prefer," which is the owner's call to make with the weights visible.

**Artifact required:** the consequence table with evidence labels per cell.

## Stage 4 — Risk and reversibility pass

Expected value is not enough. For each surviving option:

- **Door type (Bezos):** one-way or two-way? What *actually* happens on reversal — and what decays in the meantime (audience pools, ad-platform learning, staff, vendor relationships, data continuity)? "Reversible" claims get checked, not assumed; many two-way doors have one-way hinges.
- **Downside shape:** what does the bad tail look like, and is any outcome ruinous or trust-destroying rather than merely costly? Options with ruin exposure are not redeemed by attractive means.
- **Regret check for close calls:** if the table is tight, ask which wrong choice would be hardest to live with (minimax regret) — often more decision-relevant than a small EV edge.

**Artifact required:** door-type + downside note per surviving option.

## Stage 5 — Stress the leading option

Before writing the recommendation, attack it — this stage mirrors RCA's disconfirmation pass:

1. **Pre-mortem (Klein):** "It is twelve months from now and this choice failed badly. What happened?" Write the three most plausible failure stories; each should map to a criterion, a table cell, or an assumption — if a failure story reveals a criterion the table lacks, go fix the table.
2. **Steelman the runner-up:** write the strongest honest case for the second-place option, as its advocate would. If the case is compelling and rests on different *weights*, present the fork to the owner rather than burying it.
3. **The sycophancy test, answered in writing:** *"If the request had leaned the opposite way, would this analysis have recommended the opposite?"* If yes, the framing — not the evidence — is driving, and the honest output is "the evidence doesn't discriminate; here's what would" rather than a recommendation.

**Artifact required:** the pre-mortem stories, the runner-up steelman, and the sycophancy-test answer.

## Stage 6 — Recommend: direct, conditioned, and owned

The deliverable is a **direct recommendation with its dependencies exposed** — not a menu:

1. **The recommendation, stated plainly**, with confidence tied to the table's evidence strength (not to the prose's fluency).
2. **What it depends on:** the 2–3 criteria weights and table cells doing the most work. "This recommendation rests on weighting risk-of-irreversibility over near-term efficiency, and on the rung-2 incrementality estimate; challenge either and the answer can change."
3. **Flip conditions:** the specific, observable circumstances under which the recommendation reverses ("if the holdout shows incrementality below X"; "if the vendor won't move on the liability cap"). A recommendation without flip conditions is dogma.
4. **Tripwires and the reversal plan:** for the chosen path, what gets monitored, what threshold triggers reconsideration, and — for any one-way-ish elements — what's preserved to keep the door ajar (data exports, paused-not-deleted campaigns, contract terms).
5. **The owner's fork, when weights genuinely divide:** if two options win under different defensible weightings, say exactly that — "under weights A, option 1; under weights B, option 2; the weights are your call" — which is a direct recommendation *about the real decision*, not a hedge.

## Anti-patterns (self-check before delivering)

- **The mirror.** The recommendation the framing implied, with evidence assembled post-hoc. Run the sycophancy test honestly; it exists for exactly this.
- **Option capture.** Choosing among only the offered options. Status quo, information-buying, and one out-of-frame option are mandatory table rows.
- **Criteria back-fit.** Weights articulated after evaluation, mysteriously favoring the winner. Criteria are timestamped in Stage 1 for this reason.
- **Certainty laundering.** Rung labels, noise statuses, and intervals present in the analysis but absent from the recommendation. The labels travel all the way to the final sentence.
- **EV blindness to ruin and doors.** Recommending the higher mean while ignoring reversibility and tail shape.
- **The false hedge.** "Here are some options to consider" delivered when a recommendation was requested. Refusing to conclude is not humility; it's the deliverable withheld. Recommend, with dependencies exposed.
- **Reflexive more-analysis.** Recommending further study as a default posture rather than as a priced option with a named payoff and decision rule. Information-buying must beat deciding-now on the table, like any other option.
- **Strawman padding.** Options included to lose. Every row competes or gets cut.
- **The unowned decision.** Forgetting the analysis advises and the owner decides — the output should make the owner's genuine choices (weights, risk appetite) visible, not usurp them.

## Output format

```
# Recommendation: [decision]

## Frame
[decision · owner · deadline · framing-pressure note ·
 weighted criteria (timestamped, CONFIRMED/ASSUMED) · hard constraints]

## Options considered
[offered + mandatory additions (status quo, information-buying, out-of-frame)]

## Consequence table
[options × criteria · evidence labels per cell (rungs, noise status,
 intervals) · UNKNOWNs explicit · upstream forks kept as forks ·
 dominance notes]

## Risk & reversibility
[door type + downside shape per option · regret note if close]

## Stress test
[pre-mortem · runner-up steelman · sycophancy-test answer]

## Recommendation
[direct call · confidence tied to evidence · load-bearing weights & cells ·
 flip conditions · tripwires & reversal plan · owner's fork if weights divide]
```

For lightweight calls the format compresses, but four elements are never optional: criteria before evaluation, the status-quo and information-buying rows, evidence labels carried into the table, and flip conditions on the final recommendation.
