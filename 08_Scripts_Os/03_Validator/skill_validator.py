#!/usr/bin/env python3
"""
Skill Validator - SOTA Standard Validation

Validates skills against State of the Art standards with comprehensive scoring.
Tests: YAML frontmatter, name format, description triggers, progressive disclosure,
gotchas section, examples folder, dangerous commands, and absolute paths.

Scoring System:
- 90%+ = Excellent
- 70-89% = Good
- <70% = FAIL
"""

import os
import re
import yaml
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """Result of a single validation test."""

    test_name: str
    passed: bool
    score: float
    details: str = ""
    suggestions: list[str] = field(default_factory=list)


@dataclass
class ValidationReport:
    """Complete validation report for a skill."""

    skill_path: str
    skill_name: str
    tests: list[ValidationResult] = field(default_factory=list)
    total_score: float = 0.0
    grade: str = ""
    passed_tests: int = 0
    failed_tests: int = 0

    def calculate_final_score(self) -> None:
        """Calculate final score and grade based on all tests."""
        if not self.tests:
            self.total_score = 0.0
            self.grade = "FAIL"
            return

        # Fixed maximum score (sum of full scores for all tests)
        max_scores = {
            "test_yaml_frontmatter": 10.0,
            "test_name_format": 10.0,
            "test_description_triggers": 15.0,
            "test_progressive_disclosure": 15.0,
            "test_gotchas_section": 15.0,
            "test_examples_folder": 10.0,
            "test_no_dangerous_commands": 10.0,
            "test_absolute_paths": 10.0,
        }

        total_possible = sum(max_scores.get(t.test_name, 10.0) for t in self.tests)
        earned = sum(t.score for t in self.tests)

        self.total_score = (earned / total_possible * 100) if total_possible > 0 else 0
        self.passed_tests = sum(1 for t in self.tests if t.passed)
        self.failed_tests = sum(1 for t in self.tests if not t.passed)

        if self.total_score >= 90:
            self.grade = "EXCELLENT"
        elif self.total_score >= 70:
            self.grade = "GOOD"
        else:
            self.grade = "FAIL"


class SkillValidator:
    """Validates skills against SOTA standards."""

    MAX_NAME_LENGTH = 64
    MAX_SKILL_LINES = 500
    MIN_GOTCHAS_COUNT = 3

    # Dangerous commands that should not be in skills
    DANGEROUS_PATTERNS = [
        r"rm\s+-rf\s+/",  # Recursive force delete root
        r"mkfs\.",  # Format filesystem
        r"dd\s+if=.*of=/dev/",  # Direct disk write
        r":\(\)\{.*:\|:&\}",  # Fork bomb
        r"curl.*\|.*sh",  # Pipe to shell execution
        r"wget.*\|.*sh",  # Wget pipe to shell
        r"sudo\s+rm\s+-rf",  # Sudo delete
        r">\s*/dev/sd[a-z]",  # Direct device write
        r"chmod\s+-R\s+777",  # World writable
        r"chown\s+-R\s+-f\s+",  # Recursive force owner change
    ]

    # Trigger words that should be in description
    DESCRIPTION_TRIGGERS = [
        r"\bwhen\b",  # When to use
        r"\buse\b",  # Use when
        r"\btrigger\b",  # Trigger conditions
        r"\btriggered\b",  # Triggered by
        r"\bif\b",  # Conditional usage
    ]

    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.skill_md_path = self.skill_path / "SKILL.md"
        self.examples_path = self.skill_path / "examples"

    def _read_skill_content(self) -> tuple[str, dict]:
        """Read SKILL.md and parse YAML frontmatter."""
        if not self.skill_md_path.exists():
            return "", {}

        content = self.skill_md_path.read_text(encoding="utf-8")

        # Parse YAML frontmatter
        frontmatter = {}
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    content = parts[2].strip()
                except yaml.YAMLError:
                    pass

        return content, frontmatter

    def _extract_name_from_path(self) -> str:
        """Extract skill name from directory path."""
        return self.skill_path.name

    def test_yaml_frontmatter(self) -> ValidationResult:
        """Test: YAML frontmatter has required fields (name, description)."""
        content, frontmatter = self._read_skill_content()

        has_name = "name" in frontmatter and frontmatter["name"]
        has_description = "description" in frontmatter and frontmatter["description"]

        passed = has_name and has_description

        score = 10.0 if passed else 0.0
        details = []
        suggestions = []

        if not has_name:
            suggestions.append("Add 'name' field to YAML frontmatter")
        if not has_description:
            suggestions.append("Add 'description' field to YAML frontmatter")

        if has_name:
            details.append(f"name: {frontmatter.get('name', 'N/A')}")
        if has_description:
            desc = str(frontmatter.get("description", ""))[:100]
            details.append(f"description: {desc}...")

        return ValidationResult(
            test_name="test_yaml_frontmatter",
            passed=passed,
            score=score,
            details=" | ".join(details)
            if details
            else "Missing name and/or description",
            suggestions=suggestions,
        )

    def test_name_format(self) -> ValidationResult:
        """Test: Skill name is lowercase and max 64 characters."""
        content, frontmatter = self._read_skill_content()

        name = frontmatter.get("name", "") or self._extract_name_from_path()

        is_lowercase = name.islower() or "_" in name  # Allow snake_case
        is_valid_length = len(name) <= self.MAX_NAME_LENGTH

        passed = is_lowercase and is_valid_length

        score = 10.0 if passed else (5.0 if is_valid_length else 0.0)

        details = f"name: '{name}' (length: {len(name)})"
        suggestions = []

        if not is_lowercase:
            suggestions.append(f"Name should be lowercase, got: {name}")
        if not is_valid_length:
            suggestions.append(f"Name exceeds {self.MAX_NAME_LENGTH} characters")

        return ValidationResult(
            test_name="test_name_format",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_description_triggers(self) -> ValidationResult:
        """Test: Description contains trigger conditions for skill usage."""
        content, frontmatter = self._read_skill_content()

        description = frontmatter.get("description", "")
        if isinstance(description, str):
            description_text = description.lower()
        else:
            description_text = str(description).lower()

        # Check for trigger patterns
        found_triggers = []
        for trigger in self.DESCRIPTION_TRIGGERS:
            if re.search(trigger, description_text, re.IGNORECASE):
                found_triggers.append(trigger)

        # Also check full content for trigger words
        content_lower = content.lower()
        content_triggers = []
        for trigger in self.DESCRIPTION_TRIGGERS:
            if re.search(trigger, content_lower, re.IGNORECASE):
                content_triggers.append(trigger)

        has_triggers = len(found_triggers) >= 1 or len(content_triggers) >= 2

        # Bonus for having TRIGGER keyword in uppercase
        has_trigger_keyword = "TRIGGER" in content or "TRIGGERS" in content

        passed = has_triggers or has_trigger_keyword

        score = 15.0 if passed else 0.0

        details = f"found: {len(found_triggers) + len(content_triggers)} triggers"
        suggestions = []

        if not passed:
            suggestions.append(
                "Add trigger conditions like 'Use when...', 'Trigger:...', or 'if...' clauses"
            )

        return ValidationResult(
            test_name="test_description_triggers",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_progressive_disclosure(self) -> ValidationResult:
        """Test: SKILL.md is under 500 lines (progressive disclosure)."""
        content, frontmatter = self._read_skill_content()

        line_count = len(content.split("\n"))

        passed = line_count < self.MAX_SKILL_LINES

        # Calculate score based on how close to limit
        if passed:
            if line_count < 200:
                score = 15.0
            elif line_count < 350:
                score = 12.0
            else:
                score = 10.0
        else:
            score = 0.0

        details = f"lines: {line_count}/{self.MAX_SKILL_LINES}"
        suggestions = []

        if not passed:
            suggestions.append(
                f"SKILL.md has {line_count} lines. Reduce to under {self.MAX_SKILL_LINES} for progressive disclosure"
            )

        return ValidationResult(
            test_name="test_progressive_disclosure",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_gotchas_section(self) -> ValidationResult:
        """Test: At least 3 gotchas/errors documented in SKILL.md."""
        content, frontmatter = self._read_skill_content()

        # Look for gotchas sections (various formats)
        gotcha_patterns = [
            r"##\s*Gotchas",
            r"##\s*GOTCHAS",
            r"##\s*Common Errors",
            r"##\s*Errors & Gotchas",
            r"###\s*Gotchas",
            r"###\s*GOTCHAS",
            r"\*\*Gotchas\*\*",
            r"##\s*Things to Avoid",
            r"##\s*Caveats",
        ]

        gotchas_found = 0
        gotchas_section = ""

        for pattern in gotcha_patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                # Extract section content (until next ## or end)
                start = matches[0].end()
                next_header = re.search(r"\n##\s+", content[start:])
                if next_header:
                    section_content = content[start : start + next_header.start()]
                else:
                    section_content = content[start:]

                gotchas_section = section_content

                # Count individual gotchas (bullet points, numbered lists)
                bullet_gotchas = len(
                    re.findall(r"^\s*[-*]\s+", section_content, re.MULTILINE)
                )
                numbered_gotchas = len(
                    re.findall(r"^\s*\d+\.\s+", section_content, re.MULTILINE)
                )
                gotchas_found = max(gotchas_found, bullet_gotchas + numbered_gotchas)
                break

        passed = gotchas_found >= self.MIN_GOTCHAS_COUNT

        # Scoring: 15 for full pass, partial credit for partial gotchas
        if passed:
            score = 15.0
        elif gotchas_found >= 2:
            score = 10.0
        elif gotchas_found >= 1:
            score = 5.0
        else:
            score = 0.0

        details = f"found: {gotchas_found} gotchas (min: {self.MIN_GOTCHAS_COUNT})"
        suggestions = []

        if not passed:
            suggestions.append(
                f"Add at least {self.MIN_GOTCHAS_COUNT} gotchas/common errors. Found: {gotchas_found}"
            )

        return ValidationResult(
            test_name="test_gotchas_section",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_examples_folder(self) -> ValidationResult:
        """Test: Examples folder exists with at least one example file."""
        examples_exist = self.examples_path.exists()
        is_directory = self.examples_path.is_dir() if examples_exist else False

        example_files = []
        if is_directory:
            # Check both root and subdirectories for .md files
            example_files = list(self.examples_path.glob("**/*.md"))

        has_examples = len(example_files) >= 1

        passed = examples_exist and is_directory and has_examples

        score = 10.0 if passed else (5.0 if examples_exist and is_directory else 0.0)

        details = f"folder: {examples_exist}, files: {len(example_files)}"
        suggestions = []

        if not examples_exist:
            suggestions.append(
                "Create 'examples/' folder with at least one scenario file"
            )
        elif not has_examples:
            suggestions.append("Add at least one .md example file to examples/")

        return ValidationResult(
            test_name="test_examples_folder",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_no_dangerous_commands(self) -> ValidationResult:
        """Test: No dangerous commands in SKILL.md."""
        content, frontmatter = self._read_skill_content()

        dangerous_found = []

        for pattern in self.DANGEROUS_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                dangerous_found.append(pattern)

        passed = len(dangerous_found) == 0

        score = 10.0 if passed else 0.0

        details = f"dangerous commands: {len(dangerous_found)}"
        suggestions = []

        if not passed:
            suggestions.append(f"Remove dangerous patterns: {dangerous_found}")

        return ValidationResult(
            test_name="test_no_dangerous_commands",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def test_absolute_paths(self) -> ValidationResult:
        """Test: No hardcoded absolute paths in SKILL.md."""
        content, frontmatter = self._read_skill_content()

        # Look for absolute paths (Windows and Unix)
        # Exclude common non-problematic patterns
        absolute_path_pattern = r"(?<!\\)(?<!`)([A-Za-z]:\\|/~|/(?:usr|bin|etc|var|home|Users|Program Files))[/\\]"

        # Filter out things that might look like paths but aren't
        potential_paths = re.findall(absolute_path_pattern, content)

        # Additional filtering: exclude URLs, git URLs, etc.
        filtered_paths = []
        for path in potential_paths:
            # Skip if it's part of a URL
            if "http" not in path.lower() and "git@" not in path:
                filtered_paths.append(path)

        # Also check for ~/ references
        tilde_paths = re.findall(r'~/[^\s\)"\']+', content)

        all_absolute = filtered_paths + tilde_paths

        passed = len(all_absolute) == 0

        score = 10.0 if passed else (5.0 if len(all_absolute) <= 2 else 0.0)

        details = f"absolute paths: {len(all_absolute)}"
        suggestions = []

        if not passed:
            suggestions.append(
                "Replace hardcoded paths with relative paths or environment variables"
            )

        return ValidationResult(
            test_name="test_absolute_paths",
            passed=passed,
            score=score,
            details=details,
            suggestions=suggestions,
        )

    def run_all_tests(self) -> ValidationReport:
        """Run all validation tests and return comprehensive report."""
        skill_name = self._extract_name_from_path()

        report = ValidationReport(
            skill_path=str(self.skill_path), skill_name=skill_name
        )

        # Run all tests
        tests = [
            self.test_yaml_frontmatter,
            self.test_name_format,
            self.test_description_triggers,
            self.test_progressive_disclosure,
            self.test_gotchas_section,
            self.test_examples_folder,
            self.test_no_dangerous_commands,
            self.test_absolute_paths,
        ]

        for test in tests:
            try:
                result = test()
                report.tests.append(result)
            except Exception as e:
                # Add failed test with error
                report.tests.append(
                    ValidationResult(
                        test_name=test.__name__,
                        passed=False,
                        score=0.0,
                        details=f"Error: {str(e)}",
                        suggestions=[f"Fix validation error: {str(e)}"],
                    )
                )

        report.calculate_final_score()

        return report


def print_report(report: ValidationReport, verbose: bool = False) -> None:
    """Print validation report in a formatted way."""
    # Set UTF-8 encoding for Windows compatibility
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    print("\n" + "=" * 70)
    print(f"SKILL VALIDATION REPORT: {report.skill_name}")
    print("=" * 70)
    print(f"Path: {report.skill_path}")
    print("-" * 70)

    # Print individual test results
    for test in report.tests:
        status = "[PASS]" if test.passed else "[FAIL]"
        print(f"\n{status} | {test.test_name}")
        print(
            f"       Score: {test.score}/{(test.score if test.passed else 10.0) * (1 if test.passed else 1):.0f}"
        )

        if test.details:
            print(f"       Details: {test.details}")

        if verbose and test.suggestions:
            print("       Suggestions:")
            for suggestion in test.suggestions:
                print(f"         - {suggestion}")

    # Print summary
    print("\n" + "-" * 70)
    print(f"TOTAL SCORE: {report.total_score:.1f}%")
    print(f"Grade: {report.grade}")
    print(f"Tests Passed: {report.passed_tests}/{len(report.tests)}")
    print(f"Tests Failed: {report.failed_tests}/{len(report.tests)}")
    print("=" * 70 + "\n")


def validate_skill(skill_path: str, verbose: bool = False) -> ValidationReport:
    """Validate a single skill and return the report."""
    validator = SkillValidator(skill_path)
    report = validator.run_all_tests()
    print_report(report, verbose)
    return report


def validate_skills_in_directory(
    base_path: str, pattern: str = "*", verbose: bool = False
) -> list[ValidationReport]:
    """Validate all skills in a directory matching the pattern."""
    base = Path(base_path)

    if not base.exists():
        print(f"Error: Base path does not exist: {base_path}")
        return []

    # Find all skill directories
    skill_dirs = []

    # Check if base is a skill directory itself
    if (base / "SKILL.md").exists():
        skill_dirs = [base]
    else:
        # Look for skill directories
        skill_dirs = [
            d for d in base.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
        ]

        # If pattern is provided, filter
        if pattern and pattern != "*":
            skill_dirs = [d for d in skill_dirs if d.match(pattern)]

    reports = []

    print(f"\n{'=' * 70}")
    print(f"VALIDATING {len(skill_dirs)} SKILLS IN: {base_path}")
    print(f"{'=' * 70}\n")

    for skill_dir in sorted(skill_dirs):
        print(f"\n>>> Validating: {skill_dir.name}")
        validator = SkillValidator(skill_dir)
        report = validator.run_all_tests()
        reports.append(report)

        # Print summary line
        grade_marker = (
            "[*]"
            if report.grade == "EXCELLENT"
            else "[~]"
            if report.grade == "GOOD"
            else "[!]"
        )
        print(
            f"    {grade_marker} {report.grade} - {report.total_score:.1f}% ({report.passed_tests}/{len(report.tests)} tests)"
        )

    # Print aggregate summary
    print(f"\n{'=' * 70}")
    print("AGGREGATE SUMMARY")
    print(f"{'=' * 70}")

    excellent = sum(1 for r in reports if r.grade == "EXCELLENT")
    good = sum(1 for r in reports if r.grade == "GOOD")
    fail = sum(1 for r in reports if r.grade == "FAIL")
    avg_score = sum(r.total_score for r in reports) / len(reports) if reports else 0

    print(f"Total Skills: {len(reports)}")
    print(f"Average Score: {avg_score:.1f}%")
    print(f"Excellent (90%+): {excellent}")
    print(f"Good (70-89%): {good}")
    print(f"FAIL (<70%): {fail}")
    print(f"{'=' * 70}\n")

    return reports


def main():
    """Main entry point for the skill validator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate skills against SOTA standards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python skill_validator.py /path/to/skill
  python skill_validator.py /path/to/skills --pattern "sdd-*"
  python skill_validator.py /path/to/skills -v
  
Scoring System:
  90%+ = EXCELLENT
  70-89% = GOOD
  <70% = FAIL
        """,
    )

    parser.add_argument(
        "path", nargs="?", help="Path to skill directory or parent directory of skills"
    )

    parser.add_argument(
        "--pattern",
        "-p",
        default="*",
        help="Glob pattern for skill directories (default: *)",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output with suggestions",
    )

    parser.add_argument(
        "--recursive", "-r", action="store_true", help="Recursively search for skills"
    )

    args = parser.parse_args()

    if not args.path:
        # Try to find skills in current directory or common locations
        search_paths = [
            os.getcwd(),
            os.path.join(os.getcwd(), "skills"),
            os.path.expanduser("~/.config/opencode/skills"),
        ]

        for search_path in search_paths:
            if os.path.exists(search_path):
                args.path = search_path
                break

        if not args.path:
            parser.print_help()
            print("\nError: No path provided and no default found")
            sys.exit(1)

    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path does not exist: {args.path}")
        sys.exit(1)

    if path.is_file():
        # Single file - validate parent as skill
        path = path.parent

    # Check if this is a single skill or directory of skills
    is_single_skill = (path / "SKILL.md").exists()

    if is_single_skill:
        report = validate_skill(str(path), args.verbose)
        sys.exit(0 if report.grade != "FAIL" else 1)
    else:
        # Directory of skills
        reports = validate_skills_in_directory(str(path), args.pattern, args.verbose)

        if not reports:
            print(f"No skills found in: {args.path}")
            sys.exit(1)

        # Exit with error if any failed
        failed = [r for r in reports if r.grade == "FAIL"]
        sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
