# Changelog

All notable changes to the `stacked-analysis` plugin are documented here.
Versioning is plugin-level [semver](https://semver.org/), and **the version
tracks the plugin's contents — the skills themselves** — not repo plumbing,
tooling, or contribution guidelines. Skill changes bump minor (or major for
breaking restructures); everything else is at most a patch. The version in
`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, and `package.json`
is bumped together (the validator enforces that they match), and each release
is tagged `vX.Y.Z` — automatically: when a new version lands on `main`, the
`tag-release` workflow creates the tag.

## [1.1.0] — 2026-07-11

Skill content: trigger precedence between question-refinement and the eight
type skills (issue #8).

### Changed

- `question-refinement` description: fires on *ambiguous* or
  reconstruction-needing requests instead of "the START of any analysis
  request"; the `"why did A drop"` / `"which option is better"` examples
  (which route cleanly to type skills) are removed, and a negative trigger
  defers clearly-typed requests to their type skill.
- All eight type skills: Stage 1 now opens with an intake bootstrap — if no
  Refined Question Brief exists, run the question-refinement triage
  (INFER / DECLARE / ASK) inline first, typically a one-line DECLARE. The
  intake→type composition now happens regardless of which skill's
  description wins selection.
- `root-cause-analysis` description: the "why don't these two numbers match"
  example (metric-reconciliation's territory) is replaced by an explicit
  carve-out to metric-reconciliation.

## [1.0.1] — 2026-07-10

Packaging and tooling only; skill content is unchanged from 1.0.0.

### Added

- This CHANGELOG, and the release-tagging convention above.
- Manifest sync validation in `validate_skills.py`: the plugin `name` must
  match across all four manifests and the `version` across the three that
  carry one — drift now fails CI.
- Progress-checklist content check in `validate_skills.py`: each skill's
  checklist must contain checkbox items, including the standing
  beyond-the-scaffold and decision-log items.
- `homepage`, `repository`, `license`, and `keywords` in the Claude plugin
  manifest; `license` and `repository` in `package.json`.

### Changed

- README: retired the per-skill "Draft v0.1" labels — the plugin-level semver
  above is the versioning story. Skill content is unchanged.

## [1.0.0] — 2026-07-08

Initial plugin release.

- Nine analysis skills (question-refinement, root-cause-analysis,
  exploratory-data-analysis, metric-reconciliation, causal-impact,
  comparative-analysis, predictive-analysis, prescriptive-analysis,
  descriptive-analysis) packaged as the `stacked-analysis` plugin.
- Distribution via the Claude Code plugin marketplace, pi, and OpenAI Codex.
- Structural validator (`validate_skills.py`) and CI workflow.
