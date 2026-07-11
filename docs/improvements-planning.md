# Improvements Plan

A plan derived from a two-angle review of this repository: maturity/idiomatic
quality as a skills-marketplace plugin, and the effectiveness of each skill as
an *agentic* skill (independent of its analysis-domain content). Reviewed
2026-07-10; work items triaged into PRs, issues, deferred, and done. Nothing
below has been executed yet.

## Overall assessment (context, not a work item)

This is an unusually strong skills repo: the failure-mode-first design,
negative triggers in every description, required artifacts, worked examples,
and eval scenarios are things most marketplace plugins never get to. The plan
below is mostly about **maturity mechanics** (versioning, maintenance surface,
eval automation) and one **real agentic-design tension** (nine long skills
sharing ~55 lines of copy-pasted boilerplate, with no execution-layer guidance
for agents that actually have tools).

---

## PR 1 — "Plugin packaging & marketplace maturity" (the plugin PR)

One PR covering the packaging/versioning fixes:

1. **Normalize versioning on 1.0.0.** The repo has been shared with real users
   as a plugin, so 1.0.0 stands; retire the "Draft v0.1" labels in the README
   in favor of the plugin-level semver. Add a `CHANGELOG.md`, tag releases,
   and bump `version` in all three manifests (`.claude-plugin/plugin.json`,
   `.codex-plugin/plugin.json`, `package.json`) on every meaningful change.
   (Marketplace users who run `/plugin marketplace update` currently get new
   content with no way to see what changed.)

2. **Manifest sync — validate AND document.** The plugin name/description
   lives in four places (`.claude-plugin/plugin.json`,
   `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`,
   `package.json`), already with slightly different description strings. Do
   both halves: add a sync check to `validate_skills.py` (parse all four,
   compare name/version), and explain that validation in CONTRIBUTING.

3. **Fill out the manifests.** Add `homepage`, `repository`, `license`, and
   `keywords` to the Claude manifest (only the Codex one has keywords today).
   These feed marketplace browsing UIs.

4. **Validator: pick up the cheap checks that belong to this PR.** Alongside
   the manifest-sync check above: a check that each skill's progress-checklist
   block matches its actual required artifacts. (The boilerplate byte-identity
   check is tracked separately as an issue — see Issues #5 below — since it
   depends on deciding the single-sourcing approach first.) The hand-rolled
   frontmatter parser stays; stdlib-only is deliberate.

## PR 2 — Consolidate the "private repo" access caveats

Its own PR. The README currently weaves private-repo credential caveats
through each installation section, but the license is MIT and the plugin is
being distributed — if/when the repo goes public, three paragraphs go stale at
once. Isolate visibility caveats into one short "Access" note referenced from
the installation sections.

## PR 3 — Eval coverage table

Its own PR. 4 of 9 skills have eval scenarios; the README says "first
instance" and points at one. Add a coverage table (skill × has-eval ×
last-scored-run) so the "skills earn trust through scored runs" claim is
inspectable and the gaps read as invitations to contribute.

---

## Issues filed

All 17 issues below were filed on 2026-07-10. The list numbers used in this
doc (and in cross-references like "issue #4") map to GitHub issue numbers as
follows:

| Doc item | GitHub issue |
|---|---|
| 1. CONTRIBUTING vs. validator | [#4](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/4) |
| 2. CI validate check required | [#5](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/5) |
| 3. Boilerplate single-sourcing | [#6](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/6) |
| 4. Execution-layer guidance | [#7](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/7) |
| 5. Trigger contention | [#8](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/8) |
| 6. Lightweight contract | [#9](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/9) |
| 7. Checklist placement | [#10](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/10) |
| 8. Two anti-pattern lists | [#11](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/11) |
| 9. question-refinement | [#12](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/12) |
| 10. root-cause-analysis | [#13](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/13) |
| 11. exploratory-data-analysis | [#14](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/14) |
| 12. metric-reconciliation | [#15](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/15) |
| 13. causal-impact | [#16](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/16) |
| 14. comparative-analysis | [#17](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/17) |
| 15. predictive-analysis | [#18](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/18) |
| 16. prescriptive-analysis | [#19](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/19) |
| 17. descriptive-analysis | [#20](https://github.com/StackedAnalytics/analysis-skills-for-llms/issues/20) |

### Repo/infrastructure issues

1. **CONTRIBUTING vs. validator disagreement.** CONTRIBUTING lists 7 required
   sections; `validate_skills.py` checks only 4 patterns (`Why this skill
   exists`, `Anti-patterns`, `Progress checklist`, `Floor, not ceiling`).
   `Output format` and `Communicating results` are unchecked — and
   `question-refinement` has no `## Output format` section (its Stage 4 fills
   that role). Align: either add the missing patterns to the validator or trim
   the CONTRIBUTING list.

2. **Make the CI validate check required.** CONTRIBUTING admits the red ✗
   "isn't (yet) a mechanically enforced gate." The issue should include
   step-by-step instructions for the repo admin: GitHub → Settings → Branches
   → add a branch protection rule (or ruleset) for `main` → enable "Require
   status checks to pass before merging" → select the `validate` check → save.
   Once enforced, remove the honor-system paragraph from CONTRIBUTING.

### Cross-cutting agentic-effectiveness issues (one issue each)

3. **Boilerplate duplicated nine times (~55 lines).** The `Communicating
   results (two layers)` and `Floor, not ceiling` sections are copy-pasted
   verbatim across all nine skills (only the beyond-the-scaffold prompt
   sentence varies). Costs: (a) *maintenance* — a change to the decision-log
   convention requires nine synchronized edits, against the repo's own
   "evolve in one place" principle; (b) *context* — when skills compose
   (question-refinement → RCA → prescriptive), the agent loads the same
   ~1,500 tokens three times. Candidate approaches, in order of preference:
   keep the duplication but enforce byte-identity in the validator (drift
   becomes a CI failure); compress the inline version to ~10 lines with the
   full rationale in a per-skill `references/shared-conventions.md`; or a
   build step that assembles SKILL.md from a template.

4. **No execution-layer guidance for agents with tools.** The skill bodies are
   deliberately model-agnostic, but in Claude Code/Codex these run as agentic
   skills with SQL access, filesystems, and script runners — and the bodies
   never say: run the queries yourself before marking cells `?`, prefer
   reproducible scripts over mental arithmetic, write the workings layer to a
   file, save the decision log where the next session can find it. Proposal: a
   short optional `references/agentic-execution.md` per skill (or one shared
   note) that keeps the bodies model-agnostic while making agent runs
   materially better.

5. **Trigger contention between question-refinement and the type skills.**
   `question-refinement`'s description claims "the START of any analysis
   request" including "why did A drop" — which `root-cause-analysis`'s
   description also claims verbatim; skill selection is single-winner in most
   harnesses, so the model will sometimes skip intake entirely and sometimes
   do intake when the type is obvious. Fix in the descriptions: give
   question-refinement precedence language ("when the analysis type is
   ambiguous or the request smells like a proxy/presupposition") and/or have
   each type skill open with "if no Refined Question Brief exists, run the
   question-refinement triage inline first" — the latter makes composition
   robust to whichever skill fires.

6. **Artifact load vs. lightweight mode.** Each skill mandates 7–8 checklist
   artifacts plus quirks log, decision log, and a beyond-the-scaffold pass.
   The skills say "for lightweight cases the format compresses, but X/Y/Z are
   never optional" — good design — but the *checklist* doesn't compress with
   it, so a quick pacing check still nominally owes eight checked boxes. Add a
   one-line "lightweight contract" per skill: which checklist items collapse
   and which survive.

7. **Checklist-placement contradiction.** "Copy this checklist into the
   response and check items off" vs. "the completed checklist belongs in the
   workings layer, never at the top." Agents follow the first instruction
   literally. Reword to "maintain this checklist and deliver it in the
   workings layer."

8. **Two anti-pattern lists per skill.** The main `## Anti-patterns` section
   plus another inside Floor-not-ceiling. Merge or cross-reference;
   duplication dilutes the self-check.

### Per-skill issues (one issue each)

9. **question-refinement.** The INFER/DECLARE/ASK triage is the best agentic
   pattern in the repo (it explicitly prices interrupting the user). Issues to
   address: trigger contention (see issue #5); no `## Output format` section
   (see issue #1); and the description is 740 chars — nearing the 800-char
   warn threshold.

10. **root-cause-analysis.** The strongest skill; the worked example teaches
    the payoff well (E2 resolving the UNKNOWN). The "minimum six hypotheses
    across four categories" hard floor will feel like busywork on genuinely
    obvious incidents; keep it, but add an eval scenario testing the
    *cheap-obvious-cause* path to confirm it doesn't produce theater.

11. **exploratory-data-analysis.** The cut ledger is genuinely enforceable and
    the eval rubric is well built (MUST tier insensitive to thoroughness —
    good asymmetry). Heaviest skill in practice; would benefit most from the
    execution-layer guidance (issue #4) since sweeping requires real queries.

12. **metric-reconciliation.** Tight, and the "operating agreement" output is
    the most decision-shaped deliverable in the set. No eval scenario yet —
    and its discipline (stop conditions, materiality) is the easiest to grade
    mechanically, making it a good next eval.

13. **causal-impact.** The rung ladder + "verbs must match the rung" is very
    enforceable. Gap: no guidance for when the agent *can't* check assumptions
    (no data access) — does it downgrade the rung or just caveat? Currently
    ambiguous; specify.

14. **comparative-analysis.** Stage 2's auxiliary-basis bullet is a ~200-word
    single paragraph including warehouse-access instructions mid-body (see
    issue #4), dense enough that the load-bearing rule (basis-conditional
    verdicts) risks getting lost. Break it up.

15. **predictive-analysis.** Stage 6 (backtest) is written as mandatory but is
    often impossible in a chat context with a pasted table; the skill allows
    "asserted" intervals elsewhere yet the checklist demands "method
    backtested against naive." Add the explicit fallback: "if backtesting
    isn't feasible, say so and mark the interval asserted."

16. **prescriptive-analysis.** The sycophancy test-in-writing and "the false
    hedge" anti-pattern make this well-calibrated for agents. Gap: the
    owner's-fork pattern presumes a human decision-owner is reachable — fine
    interactively, unspecified in autonomous runs. Specify the autonomous
    behavior (e.g., present the fork in the deliverable rather than blocking).

17. **descriptive-analysis.** The ROUTINE/SIGNAL triage is the most
    mechanically checkable discipline in the repo — the easiest skill to eval,
    and it has no eval yet. SPC limits need historical data; same
    execution-gap note as issue #4.

---

## Deferred (revisit later)

- **README restructure for marketplace audience.** A marketplace visitor
  wants: what is this, install command, skill list, one example of the
  payoff — and currently scrolls past the failure-modes essay first. Idea: a
  short "What you get / Install / When each skill fires" block up top, essay
  after (or in `docs/DESIGN.md`). The essay stays — it's the differentiator.

- **Before/after demonstration in the README.** Nothing currently shows a
  baseline-vs-skill output snippet; one compressed A/B example (~10 lines
  each) would sell the repo better than prose.

- **Eval harness.** The `prompt.md`/`rubric.md`/`notes.md` structure is good,
  but nothing executes it. A minimal script that runs `prompt.md` under
  baseline and treatment and emits the rubric as a grading checklist would
  convert the append-only results log from aspiration to habit. Highest-
  leverage infrastructure investment available when we're ready for it.

## Done

- **`.gitignore` for `.claude/settings.local.json`** — already handled by the
  maintainer.
