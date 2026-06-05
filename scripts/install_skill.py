#!/usr/bin/env python3
"""Install local Codex skills or skill packs from this repository."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PACKS_FILE = ROOT / "skill-packs.json"


def default_dest() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def load_packs() -> dict[str, list[str]]:
    try:
        data = json.loads(PACKS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Missing pack file: {PACKS_FILE}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {PACKS_FILE}: {exc}")

    if not isinstance(data, dict):
        raise SystemExit("skill-packs.json must contain an object")

    packs: dict[str, list[str]] = {}
    for pack_name, skills in data.items():
        if not isinstance(pack_name, str) or not isinstance(skills, list):
            raise SystemExit("skill-packs.json must map pack names to skill lists")
        packs[pack_name] = [str(skill) for skill in skills]
    return packs


def available_skills() -> list[str]:
    if not SKILLS_DIR.exists():
        raise SystemExit(f"Missing skills directory: {SKILLS_DIR}")
    return sorted(path.name for path in SKILLS_DIR.iterdir() if path.is_dir())


def validate_skill(skill_name: str) -> Path:
    skill_dir = SKILLS_DIR / skill_name
    skill_md = skill_dir / "SKILL.md"
    if not skill_dir.is_dir() or not skill_md.is_file():
        raise SystemExit(f"Unknown or invalid skill: {skill_name}")
    return skill_dir


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def resolve_selection(skills: list[str], packs: list[str], pack_map: dict[str, list[str]]) -> list[str]:
    selected = list(skills)
    for pack_name in packs:
        if pack_name not in pack_map:
            known = ", ".join(sorted(pack_map))
            raise SystemExit(f"Unknown pack '{pack_name}'. Known packs: {known}")
        selected.extend(pack_map[pack_name])

    selected = dedupe(selected)
    for skill_name in selected:
        validate_skill(skill_name)
    return selected


def ensure_destination(dest: Path, dry_run: bool) -> None:
    if dry_run:
        parent = dest if dest.exists() else dest.parent
        if parent.exists() and not os.access(parent, os.W_OK):
            raise SystemExit(f"Destination parent is not writable: {parent}")
        return

    dest.mkdir(parents=True, exist_ok=True)
    if not dest.is_dir():
        raise SystemExit(f"Destination is not a directory: {dest}")
    if not os.access(dest, os.W_OK):
        raise SystemExit(f"Destination is not writable: {dest}")


def install_skill(skill_name: str, dest: Path, force: bool, dry_run: bool) -> None:
    source = validate_skill(skill_name)
    target = dest / skill_name

    if target.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing skill: {target}. Use --force to replace it.")

    if dry_run:
        action = "replace" if target.exists() else "install"
        print(f"Would {action} {skill_name} -> {target}")
        return

    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    print(f"Installed {skill_name} -> {target}")


def print_listing(pack_map: dict[str, list[str]]) -> None:
    print("Skills:")
    for skill_name in available_skills():
        print(f"  - {skill_name}")

    print("\nPacks:")
    for pack_name in sorted(pack_map):
        skills = ", ".join(pack_map[pack_name])
        print(f"  - {pack_name}: {skills}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Install Codex skills from this local repository.")
    parser.add_argument("skills", nargs="*", help="Skill names to install")
    parser.add_argument("--pack", action="append", default=[], help="Install all skills in a named pack")
    parser.add_argument("--list", action="store_true", help="List available skills and packs")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be installed without copying files")
    parser.add_argument("--dest", type=Path, default=default_dest(), help="Destination skills directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing installed skills")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    pack_map = load_packs()

    if args.list:
        print_listing(pack_map)
        if not args.skills and not args.pack:
            return 0

    if not args.skills and not args.pack:
        parser.error("provide at least one skill name, --pack, or --list")

    selected = resolve_selection(args.skills, args.pack, pack_map)
    dest = args.dest.expanduser()
    ensure_destination(dest, args.dry_run)

    for skill_name in selected:
        install_skill(skill_name, dest, args.force, args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
