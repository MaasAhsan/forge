---
name: forge
description: Multi-agent coding skill that prioritizes writing the right code for the actual current environment. Focuses on correctness, version compatibility, evidence-based debugging, and verification. Use for BUILD, DEBUG, VERIFY, or UPDATE tasks; when version-sensitive APIs matter; when another agent left a .forge/ folder; or when the user asks to verify environment, avoid hallucinations, or hand off coding work across agents.
license: MIT
compatibility: Any agent runtime that supports the SKILL.md format
metadata:
  version: "1.0.0"
  protocol: "forge/v1"
---

# Forge (adapter)

This is a platform adapter. The authoritative instructions live in the shared core.

1. Load the core Forge skill (core/SKILL.md or the universal package).
2. Follow the Forge Protocol v1.
3. Persist state to `.forge/state.json`.
4. Prefer verification over assumption.

See the repository root for the full core, protocol, schema, and documentation.
