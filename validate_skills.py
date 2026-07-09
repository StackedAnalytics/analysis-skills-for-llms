#!/usr/bin/env python3
"""Structural lint for analysis skills.

Checks every skill folder for the conventions the skills depend on, including
the Agent Skills spec's hard frontmatter rules. Errors fail the run (exit 1);
warnings are advisory.

Usage:  python validate_skills.py [repo_root]
"""

import re
import sys
from pathlib import Path

REQUIRED_FRONTMATTER = ("name", "description")

# Agent Skills spec hard limits (platform.claude.com skill authoring docs)
NAME_MAX_CHARS = 64
NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
RESERVED_NAME_WORDS = ("anthropic", "claude")
DESCRIPTION_MAX_CHARS = 1024      # spec cap -> ERROR above this
DESCRIPTION_WARN_CHARS = 800      # headroom warning

MAX_SKILL_LINES = 500             # progressive-disclosure guidance

# Repo conventions (soft checks -> warnings)
EXPECTED_SECTION_PATTERNS = {
    "rationale section ('Why this skill exists')": r"^##\s+Why this skill exists",
    "anti-patterns self-check": r"^##\s+Anti-patterns",
    "progress checklist": r"^##\s+Progress checklist",
    "floor-not-ceiling / decision-log section": r"^##\s+Floor, not ceiling",
}


def parse_frontmatter(text: str):
    """Return (frontmatter_dict, ok). Tolerates folded scalars (>-style)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, False
    fm = {}
    current_key = None
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if kv:
            current_key = kv.group(1)
            fm[current_key] = kv.group(2).strip().lstrip(">|").strip()
        elif current_key and line.startswith((" ", "\t")):
            fm[current_key] = (fm[current_key] + " " + line.strip()).strip()
    return fm, True


def validate_skill(skill_dir: Path):
    errors, warnings = [], []
    skill_md = skill_dir / "SKILL.md"

    # BOM check first: a UTF-8 BOM sits before '---' and silently breaks
    # frontmatter detection in most loaders. Known real-world failure mode
    # (Windows PowerShell's Set-Content -Encoding UTF8 writes one).
    raw = skill_md.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("file begins with a UTF-8 BOM (breaks frontmatter "
                      "detection; rewrite BOM-free)")
        raw = raw[3:]
    text = raw.decode("utf-8")
    lines = text.splitlines()

    fm, has_fm = parse_frontmatter(text)
    if not has_fm:
        errors.append("missing YAML frontmatter block")
    else:
        for key in REQUIRED_FRONTMATTER:
            if not fm.get(key):
                errors.append(f"frontmatter missing required field: {key}")

        name = fm.get("name", "")
        if name:
            if len(name) > NAME_MAX_CHARS:
                errors.append(f"name is {len(name)} chars (spec max {NAME_MAX_CHARS})")
            if not NAME_PATTERN.match(name):
                errors.append("name must be lowercase letters, numbers, and "
                              "hyphens only (spec rule)")
            for word in RESERVED_NAME_WORDS:
                if word in name:
                    errors.append(f"name contains reserved word '{word}' (spec rule)")
            if name != skill_dir.name:
                warnings.append(
                    f"frontmatter name '{name}' != folder name '{skill_dir.name}'"
                )

        desc = fm.get("description", "")
        if desc:
            n = len(desc)
            if n > DESCRIPTION_MAX_CHARS:
                errors.append(f"description is {n} chars (spec max "
                              f"{DESCRIPTION_MAX_CHARS}; it will be truncated)")
            elif n > DESCRIPTION_WARN_CHARS:
                warnings.append(f"description is {n} chars (spec cap is "
                                f"{DESCRIPTION_MAX_CHARS}; consider tightening)")
            if not re.search(r"\bdo not\b|\bDon't\b|\bDo NOT\b", desc, re.IGNORECASE):
                warnings.append(
                    "description has no negative trigger ('Do NOT use for...') - "
                    "helps prevent over-triggering"
                )

    if len(lines) > MAX_SKILL_LINES:
        warnings.append(f"SKILL.md is {len(lines)} lines (> {MAX_SKILL_LINES}); "
                        "consider moving detail to references/")

    for label, pattern in EXPECTED_SECTION_PATTERNS.items():
        if not re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
            warnings.append(f"missing {label}")

    # Bundled files must be signaled from SKILL.md, or the model never
    # discovers them ('ignored content' failure in the authoring docs).
    refs = skill_dir / "references"
    if refs.is_dir():
        ref_files = [f for f in refs.iterdir() if f.is_file()]
        if not ref_files:
            warnings.append("references/ exists but is empty")
        for f in ref_files:
            if f.name not in text:
                warnings.append(f"references/{f.name} is never mentioned in "
                                "SKILL.md - the model has no way to discover it")

    return errors, warnings


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    # Skills live under skills/ (plugin layout); fall back to the repo root
    # so the script still works when pointed at a bare collection of skills.
    skills_root = root / "skills" if (root / "skills").is_dir() else root
    skill_dirs = sorted(
        d for d in skills_root.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    )
    if not skill_dirs:
        print(f"No skill folders (containing SKILL.md) found under {root}")
        sys.exit(1)

    total_errors = 0
    for d in skill_dirs:
        errors, warnings = validate_skill(d)
        status = "FAIL" if errors else ("WARN" if warnings else "OK")
        print(f"[{status}] {d.name}")
        for e in errors:
            print(f"    ERROR: {e}")
        for w in warnings:
            print(f"    warn:  {w}")
        total_errors += len(errors)

    print(f"\n{len(skill_dirs)} skill(s) checked, {total_errors} error(s).")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
