# Contributing

Thanks for helping sharpen these skills. This repo is a distillation of analysis judgment, and it improves fastest through one specific kind of feedback: **"I used skill X and the model still failed in way Y."** A concrete failure with a reproducible prompt is worth more than a general suggestion — it's the loop the whole design is built on.

Before writing code or prose, skim the [design principles](./README.md#design-principles-for-skills-in-this-repo) in the README. They are the bar every change is held to.

## Ways to contribute

- **Report a failure** — open an issue with the skill name, the prompt you ran, what the model did, and what it should have done. If you can, note whether a skill was loaded (baseline vs. treatment).
- **Add an eval scenario** — the highest-leverage contribution. A scored scenario that reproduces a failure turns an anecdote into a regression test. See [Contributing evals](#contributing-evals).
- **Refine a skill** — tighten a stage, add an anti-pattern, fix a failure mode. Refinements should trace back to an observed failure, ideally one captured in an eval.
- **Improve tooling / docs** — the validator, the README, this file.

## Before every commit

Run the validator. CI runs it too (`.github/workflows/validate.yml`, on every push and PR) and shows a green ✓ / red ✗ `validate` check on your PR. Treat a red check as a hard stop — don't merge over it — even though it isn't (yet) a mechanically enforced gate:

```bash
python validate_skills.py
```

It reports two severities:

- **ERROR → fails CI.** Hard [Agent Skills spec](https://platform.claude.com) violations: missing frontmatter, missing `name`/`description`, a `name` over 64 chars or not `lowercase-with-hyphens`, a `name` containing a reserved word (`anthropic`, `claude`), a `description` over 1024 chars, or a UTF-8 BOM at the start of the file.
- **warn → advisory, does not fail CI.** Structural conventions: a missing required section, a `description` over 800 chars or lacking a negative trigger, a `SKILL.md` over 500 lines, or a `references/` file never mentioned in `SKILL.md` (the model can't discover it). **Treat warnings as must-fix in review** — they don't block the machine, but they block a good review.

## Anatomy of a skill

Each skill is a folder: a `SKILL.md` plus an optional `references/` directory (worked examples, templates). The core skill body is deliberately generic — organization-specific knowledge layers in via `references/`, never by forking `SKILL.md` (see the README's *Customizing* section).

**Frontmatter** — a YAML block at the very top (no BOM before it):

```yaml
---
name: root-cause-analysis          # lowercase, hyphens, matches the folder name
description: >
  One paragraph the model uses to decide when to trigger this skill. Describe
  the analysis situations it fires on in the user's words ("why did X drop"),
  and end with a negative trigger — "Do NOT use for ..." — to prevent
  over-triggering into neighboring skills.
---
```

**Required sections.** Keep the canonical structure — the validator warns when these are missing and reviewers expect them:

- `## Why this skill exists` — name the failure mode this skill prevents, and *why* it happens. Rationale makes instructions legible, and models follow legible instructions better.
- `## Progress checklist` — the required artifacts, as checkboxes the model copies into its response.
- The stages themselves (`## Stage 1 — …`), sequenced so the failure is structurally hard (e.g. enumeration strictly before evaluation).
- `## Anti-patterns (self-check before delivering)`
- `## Output format`
- `## Communicating results (two layers)` — the deliverable reads in plain business language; the artifacts ship in a "How we checked this" workings layer. Include the vocabulary translation table.
- `## Floor, not ceiling — and the decision log` — the beyond-the-scaffold pass, the quirks log, and the decision log with `USER-SETTABLE` flags.

The clearest template is any existing skill; [`skills/root-cause-analysis/SKILL.md`](./skills/root-cause-analysis/SKILL.md) is a good reference.

## Contributing evals

Evals are how skills earn trust — through scored runs, not authorship. The convention lives under each skill as `evals/scenario-NNN-short-name/`, three files:

- **`prompt.md`** — the task given to the model under test, plus the *planted characteristics* the rubric is designed to catch.
- **`rubric.md`** — two tiers: **MUST** (a pass/fail discipline gate — fail any and the run fails) and **SHOULD** (an x/N breadth score). A rubric check that maps to a skill refinement doubles as that refinement's regression test — say so.
- **`notes.md`** — provenance, the reference results table, what the run taught us, and an **append-only results log**. Add rows; never rewrite history — the point of the log is the trajectory.

Ideal scenarios come from real A/B runs (baseline vs. skill loaded), and always record the **context condition** (zero-context vs. context-loaded) — scores across conditions are not comparable.

### ⚠️ The anonymization rule — non-negotiable

Eval scenarios are seeded from real client work. **Nothing committed here may identify a client.** This is the single easiest mistake to make in a PR and the most damaging, so it is a hard review gate:

- **No** client, company, person, location, franchise, or program/product names.
- **No** exact revenue or spend figures — use ratios and orders of magnitude only ("~5×", "a small minority of outcomes", "the search channel").
- Sectors and channels described generically ("multi-location education/services network", "search channel", "social channel").

Every existing scenario states this rule at the bottom of its `prompt.md` and inherits it forward — keep that. When in doubt, abstract harder. A scenario that's too vague can be sharpened later; a leaked client name cannot be un-pushed.

## Pull request workflow

1. **Branch** off `main` — don't commit directly.
2. **One logical change per PR.** A skill refinement and its motivating eval belong together; unrelated cleanups belong apart.
3. **Run `python validate_skills.py`** and make sure it's clean (no errors, warnings addressed).
4. **Open the PR** — describe the failure the change addresses, and link the eval that proves it where applicable. Wait for the green CI check.
5. Contributions are accepted under the repo's [MIT License](./LICENSE) (GitHub's inbound = outbound default).

### Line endings

The repo normalizes all text to LF via [`.gitattributes`](./.gitattributes). If your editor writes CRLF, git will convert on commit and may print a one-time "CRLF will be replaced by LF" notice — that's expected and harmless; the stored files are LF.
