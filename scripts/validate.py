#!/usr/bin/env python3
"""Validate the documentation-only frontend guidelines repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "README.md",
    "AGENTS.md",
    "FRONTEND_SPEC.md",
    "VERSION",
    "LICENSE",
    "CHANGELOG.md",
    "docs/10-validation-checklist.md",
    "templates/PROJECT_FRONTEND_PROFILE.md",
}
FORBIDDEN_SUFFIXES = {
    ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".css", ".scss", ".less"
}
RULE_PATTERN = re.compile(r"^### (FG-[A-Z0-9]+-\d{3})\b", re.MULTILINE)
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0

    for relative in sorted(REQUIRED):
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")
            errors += 1

    version_path = ROOT / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if not SEMVER_PATTERN.fullmatch(version):
            fail(f"VERSION is not semantic versioning: {version!r}")
            errors += 1

    forbidden = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            forbidden.append(path.relative_to(ROOT))
    if forbidden:
        fail("UI implementation files are forbidden: " + ", ".join(map(str, forbidden)))
        errors += 1

    spec_path = ROOT / "FRONTEND_SPEC.md"
    if spec_path.is_file():
        spec = spec_path.read_text(encoding="utf-8")
        rule_ids = RULE_PATTERN.findall(spec)
        duplicates = sorted({rule for rule in rule_ids if rule_ids.count(rule) > 1})
        if duplicates:
            fail("duplicate rule IDs: " + ", ".join(duplicates))
            errors += 1
        if len(rule_ids) < 20:
            fail(f"expected at least 20 normative rules, found {len(rule_ids)}")
            errors += 1
        print(f"rules: {len(rule_ids)} unique IDs")

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                errors += 1
                continue
            if not resolved.exists():
                fail(f"broken relative link: {markdown.relative_to(ROOT)} -> {target}")
                errors += 1

    if errors:
        print(f"validation failed: {errors} error(s)", file=sys.stderr)
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
