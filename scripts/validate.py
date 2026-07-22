#!/usr/bin/env python3
"""Validate the documentation-only, English frontend guidelines repository."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    ".editorconfig",
    "README.md",
    "AGENTS.md",
    "FRONTEND_SPEC.md",
    "VERSION",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "docs/README.md",
    "docs/10-validation-checklist.md",
    "docs/14-performance-and-resilience.md",
    "docs/15-permissions-security-and-privacy.md",
    "docs/16-localization-and-formatting.md",
    "docs/17-state-routing-and-persistence.md",
    "docs/18-editability-and-lifecycle.md",
    "templates/PROJECT_FRONTEND_PROFILE.md",
    "templates/FRONTEND_TASK_PLAN.md",
    "templates/FRONTEND_CHANGE_REPORT.md",
}

FORBIDDEN_SUFFIXES = {
    ".astro",
    ".cjs",
    ".css",
    ".htm",
    ".html",
    ".js",
    ".jsx",
    ".less",
    ".mjs",
    ".mdx",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
    ".wasm",
}

TEXT_SUFFIXES = {"", ".md", ".py", ".txt", ".yaml", ".yml", ".json"}
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
CHANGELOG_VERSION_PATTERN = re.compile(r"^## (\d+\.\d+\.\d+) — \d{4}-\d{2}-\d{2}$", re.MULTILINE)
RULE_ID_PATTERN = re.compile(r"^### (FG-[A-Z0-9]+-\d{3})\b", re.MULTILINE)
RULE_HEADING_PATTERN = re.compile(
    r"^### (FG-[A-Z0-9]+-\d{3}) — (.+) \[(MUST|SHOULD|MAY)\]$",
    re.MULTILINE,
)
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RULE_REFERENCE_PATTERN = re.compile(r"\bFG-[A-Z0-9]+-\d{3}\b")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def repository_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def validate_required_files() -> int:
    errors = 0
    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")
            errors += 1
    return errors


def validate_version() -> int:
    errors = 0
    version_path = ROOT / "VERSION"
    changelog_path = ROOT / "CHANGELOG.md"
    if not version_path.is_file() or not changelog_path.is_file():
        return errors

    version = version_path.read_text(encoding="utf-8").strip()
    if not SEMVER_PATTERN.fullmatch(version):
        fail(f"VERSION is not semantic versioning: {version!r}")
        return 1

    changelog = changelog_path.read_text(encoding="utf-8")
    versions = CHANGELOG_VERSION_PATTERN.findall(changelog)
    if not versions:
        fail("CHANGELOG.md has no valid version heading")
        return 1
    if versions[0] != version:
        fail(f"VERSION {version} does not match latest changelog version {versions[0]}")
        errors += 1
    if len(versions) != len(set(versions)):
        fail("CHANGELOG.md contains duplicate version headings")
        errors += 1
    return errors


def validate_repository_boundary(files: list[Path]) -> int:
    forbidden = [path.relative_to(ROOT) for path in files if path.suffix.lower() in FORBIDDEN_SUFFIXES]
    if forbidden:
        fail("UI implementation files are forbidden: " + ", ".join(map(str, sorted(forbidden))))
        return 1
    return 0


def validate_english_and_whitespace(files: list[Path]) -> int:
    errors = 0
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"expected UTF-8 text: {path.relative_to(ROOT)}")
            errors += 1
            continue

        relative = path.relative_to(ROOT)
        for offset, character in enumerate(text):
            if character.isalpha() and not ("A" <= character <= "Z" or "a" <= character <= "z"):
                line = text.count("\n", 0, offset) + 1
                fail(f"non-English alphabetic character in {relative}:{line}")
                errors += 1
                break

        if text and not text.endswith("\n"):
            fail(f"missing final newline: {relative}")
            errors += 1

        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith((" ", "\t")):
                fail(f"trailing whitespace: {relative}:{line_number}")
                errors += 1
    return errors


def validate_rules() -> int:
    spec_path = ROOT / "FRONTEND_SPEC.md"
    if not spec_path.is_file():
        return 0

    errors = 0
    spec = spec_path.read_text(encoding="utf-8")
    all_ids = RULE_ID_PATTERN.findall(spec)
    headings = list(RULE_HEADING_PATTERN.finditer(spec))
    valid_ids = [match.group(1) for match in headings]

    malformed = [rule_id for rule_id in all_ids if rule_id not in valid_ids]
    if malformed:
        fail("malformed rule headings: " + ", ".join(malformed))
        errors += 1

    duplicates = sorted(rule_id for rule_id, count in Counter(valid_ids).items() if count > 1)
    if duplicates:
        fail("duplicate rule IDs: " + ", ".join(duplicates))
        errors += 1

    if len(valid_ids) < 70:
        fail(f"expected at least 70 normative rules, found {len(valid_ids)}")
        errors += 1

    for index, heading in enumerate(headings):
        body_start = heading.end()
        body_end = headings[index + 1].start() if index + 1 < len(headings) else len(spec)
        body = spec[body_start:body_end].strip()
        if len(body) < 40:
            fail(f"rule {heading.group(1)} has an insufficient normative body")
            errors += 1

    category_counts = Counter(rule_id.split("-")[1] for rule_id in valid_ids)
    for required_category in {"CORE", "LAYOUT", "FORM", "OVERLAY", "NAV", "STATE", "ACTION", "A11Y", "QUALITY"}:
        if category_counts[required_category] == 0:
            fail(f"missing required rule category: {required_category}")
            errors += 1

    print(f"rules: {len(valid_ids)} unique IDs across {len(category_counts)} categories")
    return errors


def validate_markdown_integrity(files: list[Path]) -> int:
    errors = 0
    spec_path = ROOT / "FRONTEND_SPEC.md"
    defined_ids = set()
    if spec_path.is_file():
        defined_ids = set(RULE_ID_PATTERN.findall(spec_path.read_text(encoding="utf-8")))

    for markdown in [path for path in files if path.suffix.lower() == ".md"]:
        text = markdown.read_text(encoding="utf-8")
        relative = markdown.relative_to(ROOT)
        if text.count("```") % 2 != 0:
            fail(f"unbalanced fenced code blocks: {relative}")
            errors += 1

        for reference in sorted(set(RULE_REFERENCE_PATTERN.findall(text))):
            if reference not in defined_ids:
                fail(f"undefined rule reference in {relative}: {reference}")
                errors += 1
    return errors


def validate_relative_links(files: list[Path]) -> int:
    errors = 0
    for markdown in [path for path in files if path.suffix.lower() == ".md"]:
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (markdown.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                errors += 1
                continue
            if not resolved.exists():
                fail(f"broken relative link: {markdown.relative_to(ROOT)} -> {target}")
                errors += 1
    return errors


def validate_docs_index() -> int:
    index_path = ROOT / "docs" / "README.md"
    if not index_path.is_file():
        return 0

    errors = 0
    index = index_path.read_text(encoding="utf-8")
    for path in sorted((ROOT / "docs").glob("*.md")):
        if path.name == "README.md":
            continue
        if f"({path.name})" not in index:
            fail(f"docs/README.md does not index {path.name}")
            errors += 1
    return errors


def main() -> int:
    files = repository_files()
    errors = 0
    errors += validate_required_files()
    errors += validate_version()
    errors += validate_repository_boundary(files)
    errors += validate_english_and_whitespace(files)
    errors += validate_rules()
    errors += validate_markdown_integrity(files)
    errors += validate_relative_links(files)
    errors += validate_docs_index()

    if errors:
        print(f"validation failed: {errors} error(s)", file=sys.stderr)
        return 1

    print(f"files: {len(files)} checked")
    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
