---
name: forge
description: Multi-agent coding skill that prioritizes writing the right code for the actual current environment. Focuses on correctness, version compatibility, evidence-based debugging, and verification. Use for BUILD, DEBUG, VERIFY, or UPDATE tasks; when version-sensitive APIs matter; when another agent left a .forge/ folder; or when the user asks to verify environment, avoid hallucinations, or hand off coding work across agents.
license: MIT
compatibility: Any agent runtime that supports the SKILL.md format (file read/write or prompt injection)
metadata:
  version: "1.0.0"
  protocol: "forge/v1"
  core: "core/"
---

# Forge

**Shared core lives in `core/`.** Read `core/SKILL.md` and `core/protocol.md` for the complete behavior. Platform adapters under `adapters/` only supply discovery metadata and install paths; they do not re-implement logic.

## Quick start

1. Load this skill.
2. Follow the workflow in `core/SKILL.md`.
3. Persist state to `.forge/state.json` (and optionally `.forge/current.md`).
4. On handoff, refresh `current_state` + `next_action` and stop.

## Repository layout

```
forge/
├── SKILL.md                 # This entry (portable)
├── core/
│   ├── SKILL.md             # Full instructions
│   ├── protocol.md          # Protocol rules
│   └── schema.json          # JSON Schema
├── adapters/                # Platform-specific manifests only
├── universal/               # Platform-independent package source
├── docs/
├── examples/
├── tests/
└── dist/
    └── forge-skill.zip      # Ready-to-upload universal skill
```

## What is shared vs platform-specific

| Shared (core) | Platform-specific (adapters) |
|---------------|------------------------------|
| Protocol, schema, operations, conflict rules, handoff format | Plugin manifests, install paths, discovery directories |
| SKILL.md instructions | Wrapper SKILL.md that points at core (if required by the host) |

Do not duplicate core logic inside adapters.

## Universal package

`dist/forge-skill.zip` contains only the platform-independent skill (`forge/SKILL.md`, `protocol.md`, `schema.json`). It is ready for upload/import into any compatible skill system.
