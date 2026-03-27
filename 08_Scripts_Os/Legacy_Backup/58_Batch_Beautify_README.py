#!/usr/bin/env python3
"""Batch beautify all README files in project."""

import os
import re
from pathlib import Path


def beautify_table(content):
    """Apply pixel-perfect table formatting."""
    lines = content.split("\n")
    result = []
    in_table = False
    table_lines = []

    for line in lines:
        if line.strip().startswith("|") and "---" not in line:
            if "|" in line and line.strip():
                table_lines.append(line)
                in_table = True
        elif in_table and "---" in line:
            table_lines.append(line)
        elif in_table:
            result.extend(process_table(table_lines))
            table_lines = []
            in_table = False
            result.append(line)
        else:
            if table_lines:
                result.extend(process_table(table_lines))
                table_lines = []
            result.append(line)

    return "\n".join(result)


def process_table(lines):
    """Format a markdown table with consistent widths."""
    if not lines:
        return []

    rows = []
    for line in lines:
        if "|" in line and line.strip():
            cols = [c.strip() for c in line.split("|")[1:-1]]
            rows.append(cols)

    if len(rows) < 2:
        return lines

    widths = []
    for row in rows:
        for i, cell in enumerate(row):
            w = len(strip_markdown(cell))
            if i >= len(widths):
                widths.append(w)
            else:
                widths[i] = max(widths[i], w)

    result = []
    for i, row in enumerate(rows):
        if i == 1:
            sep = "| " + " | ".join("-" * w for w in widths) + " |"
            result.append(sep)
        else:
            cells = []
            for j, cell in enumerate(row):
                w = widths[j] if j < len(widths) else len(cell)
                cells.append(cell.ljust(w))
            result.append("| " + " | ".join(cells) + " |")

    return result


def strip_markdown(text):
    """Remove markdown formatting from text."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def main():
    """Process all README files."""
    root = Path(".")
    excluded = {
        "03_Knowledge/10_Repos_Gentleman",
        "07_Projects/Safe_Backup",
        "06_Archive",
        "node_modules",
        ".git",
    }

    readmes = list(root.rglob("README*.md"))
    processed = 0

    for readme in readmes:
        if any(ex in str(readme) for ex in excluded):
            continue

        content = readme.read_text(encoding="utf-8")
        beautified = beautify_table(content)

        if beautified != content:
            readme.write_text(beautified, encoding="utf-8")
            print(f"Beautified: {readme}")
            processed += 1

    print(f"\nTotal processed: {processed}")


if __name__ == "__main__":
    main()
