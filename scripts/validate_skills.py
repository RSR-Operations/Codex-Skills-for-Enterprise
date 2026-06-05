#!/usr/bin/env python3
"""Validate repository skill structure and core metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - depends on local environment
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DISALLOWED_SKILL_DOCS = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str] | None, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter"

    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unterminated YAML frontmatter"

    raw = text[4:end]
    if yaml is not None:
        data = yaml.safe_load(raw)
    else:
        data = {}
        for line in raw.splitlines():
            if ":" not in line:
                return None, f"cannot parse frontmatter line without PyYAML: {line}"
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    if not isinstance(data, dict):
        return None, "frontmatter must be a mapping"
    return data, None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_name = skill_dir.name

    if not NAME_RE.fullmatch(skill_name):
        errors.append(f"{skill_name}: folder name must be lowercase hyphen-case")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_name}: missing SKILL.md")
        return errors

    data, parse_error = parse_frontmatter(skill_md)
    if parse_error:
        errors.append(f"{skill_name}: {parse_error}")
        return errors

    assert data is not None
    keys = set(data)
    if keys != {"name", "description"}:
        errors.append(f"{skill_name}: frontmatter must contain only name and description")

    if data.get("name") != skill_name:
        errors.append(f"{skill_name}: frontmatter name must match folder name")

    description = str(data.get("description", "")).strip()
    if len(description) < 120:
        errors.append(f"{skill_name}: description is too short for reliable triggering")
    if "use when" not in description.lower():
        errors.append(f"{skill_name}: description must include explicit 'Use when' trigger language")

    body = skill_md.read_text(encoding="utf-8")
    if "[TODO" in body or "TODO:" in body:
        errors.append(f"{skill_name}: SKILL.md contains placeholder TODO text")

    agents_file = skill_dir / "agents" / "openai.yaml"
    if not agents_file.exists():
        errors.append(f"{skill_name}: missing agents/openai.yaml")
    else:
        agents_text = agents_file.read_text(encoding="utf-8")
        if "default_prompt" not in agents_text:
            errors.append(f"{skill_name}: agents/openai.yaml missing default_prompt")
        if f"${skill_name}" not in agents_text:
            errors.append(f"{skill_name}: default_prompt must mention ${skill_name}")

    for filename in DISALLOWED_SKILL_DOCS:
        if (skill_dir / filename).exists():
            errors.append(f"{skill_name}: disallowed auxiliary doc {filename}")

    references_dir = skill_dir / "references"
    if references_dir.exists():
        nested = [path for path in references_dir.glob("*/*") if path.is_file()]
        if nested:
            errors.append(f"{skill_name}: references must be one level deep")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("Missing skills/ directory", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("No skills found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
