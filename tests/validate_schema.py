#!/usr/bin/env python3
"""Basic schema presence and structure checks for Forge."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "core" / "schema.json"
UNIVERSAL_SCHEMA = ROOT / "universal" / "forge" / "schema.json"

def main() -> int:
    errors = []
    for path in (SCHEMA, UNIVERSAL_SCHEMA):
        if not path.exists():
            errors.append(f"Missing schema: {path}")
            continue
        try:
            data = json.loads(path.read_text())
        except Exception as e:
            errors.append(f"Invalid JSON in {path}: {e}")
            continue
        if data.get("title") != "Forge Shared State":
            errors.append(f"Unexpected title in {path}")
        required = set(data.get("required", []))
        for key in ("schema_version", "task_id", "updated_at", "goal", "mode", "current_state", "provenance"):
            if key not in required:
                errors.append(f"Missing required field {key} in {path}")

    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("OK: schema checks passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
