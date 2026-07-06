# Analysis Skills for LLMs

Structured skill instructions that make LLMs better at high-level data analysis — by engineering around their characteristic reasoning failures rather than just describing good process.

## The premise

LLMs doing analysis fail in predictable, *type-specific* ways that differ from how humans fail:

| Analysis type | Signature LLM failure |
|---|---|
| Question intake (all types) | Obliging literalism — answering the request as phrased instead of the question actually being asked |
| Root cause analysis | Premature convergence — the first plausible hypothesis anchors everything after it |
| Exploratory analysis | Pareidolia — a confident narrative for every pattern, including noise |
| Comparative analysis | Mix-shift blindness (Simpson's paradox) plus league-table noise — narrating the extremes of raw rankings, where the small samples live |
| Descriptive analysis | The tour — accurate observations with no point of view: no lede, no expectation frame, noise narrated as events, and materiality absent |
| Predictive analysis | Naked point estimates and recency overfit — a confident single number, no interval, extrapolated from the last few data points, built from the story instead of the base rates |
| Prescriptive analysis | Sycophancy — recommending what the framing implies, choosing among only the offered options, with criteria back-fit to the conclusion and upstream uncertainty laundered out of the advice |
| Evaluative / reconciliation | False precision — obliging "make these match" with a single-culprit hunt, when cross-system gaps are structural stacks that will never close |
| Causal impact (effect estimation) | Counterfactual blindness — reporting a before/after delta as "the effect," with free causal verbs, unchecked method assumptions, and sycophantic confirmation of the hoped-for answer |

Exhortation ("consider multiple hypotheses," "avoid anchoring") does not fix these — the model agrees, then does it anyway. What works is **procedural scaffolding with required artifacts**: converting internal epistemic states the model can't reliably hold (e.g., "several hypotheses at partial confidence") into external structures it must produce (e.g., an evidence × hypothesis matrix). The artifact *is* the discipline.

The methods are adapted from the analysis literature — Heuer's Analysis of Competing Hypotheses, Kepner-Tregoe Problem Analysis, Ishikawa categories, Tukey's exploratory/confirmatory distinction, Gelman & Loken's garden of forking paths — modified where the LLM failure mode differs from the human one the method was designed for.

## Skills

| Skill | Status | Description |
|---|---|---|
| [`question-refinement/`](./question-refinement/) | Draft v0.1 | The front door: reconstruct the real question behind an analysis request (reference-interview + decision-first framing), classify the analysis type on intent, and produce a Refined Question Brief that routes to the skill below |
| [`root-cause-analysis/`](./root-cause-analysis/) | Draft v0.1 | Root cause analysis: IS/IS-NOT specification → hypothesis enumeration → ACH evidence matrix → disconfirmation → structured conclusion with sensitivity + residual |
| [`exploratory-data-analysis/`](./exploratory-data-analysis/) | Draft v0.1 | Exploratory analysis: mode declaration + data credentials → systematic sweep with a cut ledger (forking-paths accounting) → robustness gauntlet → status-labeled hypothesis slate |
| [`metric-reconciliation/`](./metric-reconciliation/) | Draft v0.1 | Evaluative analysis for cross-system metric discrepancies: decision/materiality framing → expected-difference inventory → gap waterfall → verdict against materiality (not zero) → operating agreement (system of record per decision + expected-disagreement band) |
| [`causal-impact/`](./causal-impact/) | Draft v0.1 | Forward causality / effect estimation ("did X work, how much did it drive"): claim classification → explicit counterfactual → confound inventory → design ladder with rung-labeled conclusions → falsification tests → bounds over false precision |
| [`comparative-analysis/`](./comparative-analysis/) | Draft v0.1 | Comparing entities/groups: comparability audit → composition check with mix/performance decomposition (Simpson's defense) → ranking discipline (funnel logic, shrinkage, regression-to-mean) → interpretation firewall between description and attribution |
| [`predictive-analysis/`](./predictive-analysis/) | Draft v0.1 | Forecasting & pacing: outside view + naive baselines as the anchor → decomposition with recency/regime checks → itemized adjustment ledger → empirical intervals from backtests → revision triggers and forecast scoring |
| [`prescriptive-analysis/`](./prescriptive-analysis/) | Draft v0.1 | Recommendations & decision support (the capstone — consumes the other skills' outputs): criteria frozen before evaluation → widened option set (status quo, information-buying, out-of-frame) → consequence table with uncertainty labels carried in → reversibility & pre-mortem → direct recommendation with flip conditions |
| [`descriptive-analysis/`](./descriptive-analysis/) | Draft v0.1 | Reporting & characterization: expectation frames on every number → variation triage (SPC — routine vs. signal; routine gets no narrative) → a committed lede including the steady-state lede → proportional emphasis and loop-closing |

All seven analysis types from the failure table are now drafted, plus the intake and reconciliation layers. The skills compose: the Refined Question Brief produced by `question-refinement` is the entry artifact consumed by each type-specific skill, and evidence labels (rungs, signal statuses, intervals) flow downstream into `prescriptive-analysis`.

## Quick routing (for humans)

The `question-refinement` skill routes requests at runtime; this table is the same map for a person browsing the repo:

| You're facing... | Start with |
|---|---|
| A metric dropped/spiked, a number looks wrong, "what happened?" | `root-cause-analysis` |
| Unfamiliar data, "anything interesting?", hypothesis hunting | `exploratory-data-analysis` |
| Two systems disagree on the same metric | `metric-reconciliation` |
| "Which is better?" / rank these / segment vs. segment, group vs. group | `comparative-analysis` |
| "Did X work?" / "What was the impact of Y?" / prove-the-campaign requests | `causal-impact` |
| "Will we hit the target?" / "Where do we land?" / project or forecast a number | `predictive-analysis` |
| "What should we do?" / "Should we cut/keep/switch X?" / pick a vendor, make the call | `prescriptive-analysis` |
| A recurring report, "summarize the month," "how are we doing" | `descriptive-analysis` |
| A vague or suspicious analysis request from a stakeholder | `question-refinement` |
| Not sure | `question-refinement` — deciding is its job |

## Usage

Each skill is a folder containing a `SKILL.md` (the instructions) and optional `references/` (worked examples, templates). Portable across LLM products:

- **Claude (Skills / Projects):** install the folder as a skill, or paste `SKILL.md` into project knowledge.
- **Claude Code / agents:** drop the folder into your skills directory; the frontmatter `description` handles triggering.
- **ChatGPT / Gemini / other:** paste `SKILL.md` contents into a custom GPT / Gem / system prompt. The frontmatter can be dropped; everything below it is model-agnostic.
- **Ad hoc:** paste the skill body above your question.

## Customizing for an organization or client

The skill bodies are deliberately generic — the reasoning discipline doesn't change between companies. Organization-specific knowledge layers on via each skill's `references/` folder, without touching `SKILL.md`:

```
root-cause-analysis/
├── SKILL.md                      ← never forked per client
└── references/
    ├── worked-example.md          ← ships with the skill
    ├── client-metric-definitions.md   ← what "conversion" means here
    ├── client-known-artifacts.md      ← tag history, consent quirks, definition changes
    └── client-schema-notes.md         ← tables, grains, join logic
```

The model reads these when the skill runs. This split matters for maintainability: the core skills evolve in one place, while each engagement gets its own overlay — the same vendor-managed-core / local-context pattern used for upstream data packages. A `client-known-artifacts.md` file is especially high-leverage for `root-cause-analysis` and `exploratory-data-analysis`, since measurement history is exactly the context the mandatory data-artifact hypothesis and artifact screen feed on.

When sharing with a client, share the core skills plus *their* overlay only.

## Works alongside execution-layer tooling

These skills govern *reasoning*; they deliberately don't cover the execution layer -- connecting to warehouses, writing SQL, profiling tables, building charts. Tools like Anthropic's official Data Analyst plugin (`knowledge-work-plugins/data`) cover that layer well, and the two compose cleanly:

- Its `/explore-data` profile (grain, null rates, distributions, quality flags) satisfies `exploratory-data-analysis` Stage 1's data-credentials artifact almost exactly -- run it, then apply the sweep, gauntlet, and labeling discipline to what it finds.
- `/analyze` requests of the form "what's driving the drop" are diagnostic questions: route them through `root-cause-analysis` rather than generic pattern-finding.
- `/validate-data` is the mechanical QA pass (join explosion, average-of-averages, calculation spot-checks); run it alongside -- not instead of -- the epistemic discipline here. One checks the arithmetic, the other checks the reasoning.
- Its `data-context-extractor` generates company-specific context in the same SKILL.md + `references/` overlay structure documented above; its output slots directly into the per-engagement overlay convention.

The general division: execution tooling answers "how do I do this task with these tools"; this repo answers "how do I think while doing it so the output is trustworthy."

## Design principles for skills in this repo

1. **Failure-mode-first.** Every skill names the failure it exists to prevent, and explains *why* it happens — models follow instructions better when the rationale is legible.
2. **Artifacts over exhortation.** Every stage produces a required, inspectable output. Skipping is visible.
3. **Order matters.** Stages are sequenced to make the failure structurally difficult (e.g., enumeration strictly before evaluation).
4. **Calibration, not hedging.** The goal is honest uncertainty — including plain confidence when evidence is decisive.
5. **Model-agnostic.** No product-specific features in skill bodies.
6. **Load-bearing choices are visible.** Scope boundaries (what wasn't examined), auxiliary bases and constructions (what the numbers rest on), and context provenance (sourced vs. asserted) are declared, never silent — because silent choices are how two rigorous analyses reach opposite conclusions from identical data.

## Evaluations

Skills earn trust through scored runs, not authorship. The convention: each skill may carry an `evals/` folder of scenarios, each scenario a folder containing `prompt.md` (the task, plus the planted data characteristics the rubric tests), `rubric.md` (a MUST pass/fail gate for the skill's core discipline and a SHOULD x/N quality score for breadth), and `notes.md` (provenance and an append-only results log). Scenarios are seeded from real usage -- ideally true A/B runs (baseline vs. skill) -- and are **anonymized**: no client, person, location, or program names, no exact revenue figures. Rubric checks that map to a skill refinement double as regression tests for it. First instance: `exploratory-data-analysis/evals/scenario-001-warehouse-first-look/`.

## Status & feedback

This is an evolving distillation of practitioner judgment, currently maintained for internal use and shared with select clients — not (yet) a public library. Versioning is deliberate: point people at the repo, not at copies, so everyone runs the latest thinking. The feedback that improves these fastest is the specific form: *"I used skill X and the model still failed in way Y"* — that's the loop the whole design is built on. Run `python validate_skills.py` before committing changes.
