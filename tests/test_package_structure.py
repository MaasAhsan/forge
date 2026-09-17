#!/usr/bin/env python3
"""Validate universal package structure and required files."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIVERSAL = ROOT / "universal" / "forge"
REQUIRED = ["SKILL.md", "protocol.md", "schema.json"]

def main() -> int:
    errors = []
    if not UNIVERSAL.is_dir():
        errors.append(f"Missing universal directory: {UNIVERSAL}")
    else:
        for name in REQUIRED:
            p = UNIVERSAL / name
            if not p.exists():
                errors.append(f"Missing required file: {p}")
            elif p.stat().st_size < 50:
                errors.append(f"File too small (suspicious): {p}")

    # SKILL.md frontmatter basics
    skill = UNIVERSAL / "SKILL.md"
    if skill.exists():
        text = skill.read_text()
        if "name: forge" not in text:
            errors.append("SKILL.md missing name: forge")
        if "description:" not in text:
            errors.append("SKILL.md missing description")

    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("OK: universal package structure valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())
