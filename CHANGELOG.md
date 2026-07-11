# Changelog

All notable changes to the `stacked-analysis` plugin are documented here.
Versioning is plugin-level [semver](https://semver.org/): the plugin version
in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, and
`package.json` is bumped together on every meaningful change (the validator
enforces that they match), and each release is tagged `vX.Y.Z`.

## [1.1.0] — 2026-07-10

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
