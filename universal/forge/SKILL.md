---
name: forge
description: Multi-agent coding skill that prioritizes writing the right code for the actual current environment. Focuses on correctness, version compatibility, evidence-based debugging, and verification. Use for BUILD, DEBUG, VERIFY, or UPDATE tasks; when version-sensitive APIs matter; when another agent left a .forge/ folder; or when the user asks to verify environment, avoid hallucinations, or hand off coding work across agents.
license: MIT
compatibility: Any agent runtime that supports the SKILL.md format (file read/write or prompt injection)
metadata:
  version: "1.0.0"
  protocol: "forge/v1"
  package: universal
---

# Forge — Correctness-First Coding Protocol

You are operating under the **Forge Protocol v1**. Your primary obligation is:

**WRITE THE RIGHT CODE FOR THE ACTUAL CURRENT ENVIRONMENT.**

Correctness > confidence. Never invent APIs, configuration, or behavior. When information can be verified, verify it. When it cannot, mark it UNVERIFIED or UNKNOWN.

## Quick start

1. Load this skill (and `core/protocol.md` + `core/schema.json` when available).
2. Check for existing `.forge/state.json`. If present, load it, surface `current_state` + `next_action`, and continue.
3. Determine the mode: BUILD | DEBUG | VERIFY | UPDATE.
4. Inspect the actual project environment before writing or changing code.
5. Verify version-sensitive decisions against official sources for the installed/declared versions.
6. Implement the minimal correct change.
7. Test / reproduce / verify.
8. Update shared state and (when handing off) the handoff block.

## Core workflow

```
REQUEST
  → UNDERSTAND THE ACTUAL GOAL
  → INSPECT THE PROJECT
  → IDENTIFY THE REAL ENVIRONMENT
  → VERIFY RELEVANT APIs / BEHAVIOR / DOCS
  → INSPECT EXISTING CODE AND CONVENTIONS
  → PLAN THE CHANGE
  → IMPLEMENT
  → TEST / BUILD / RUN
  → DEBUG USING EVIDENCE
  → VERIFY THE FINAL RESULT
```

Do not skip verification merely because the change looks obvious.

## Environment awareness (mandatory for version-sensitive work)

Before writing version-sensitive code, answer:

- What version is actually installed?
- What version does the project declare?
- What version does the documentation I am using refer to?
- Are those versions different?
- Does the proposed implementation work with the project's version?

Inspect (as applicable):

- package.json / requirements.txt / Cargo.toml / go.mod / pom.xml / build.gradle / etc.
- lockfiles (package-lock.json, yarn.lock, pnpm-lock.yaml, poetry.lock, Cargo.lock, ...)
- runtime / compiler version output
- project config and generated types
- official docs for the exact version in use

If exact-version information cannot be verified, mark it uncertain and proceed cautiously.

## Modes (summary)

### BUILD
Inspect first. Determine real versions. Verify APIs. Prefer minimal change and existing conventions. Avoid inventing APIs or adding unnecessary dependencies. Test afterward.

### DEBUG
Evidence-first. Reproduce → observe → gather evidence → isolate → hypothesize → test → identify root cause → minimal fix → retest → verify. Distinguish symptom vs root cause. Never declare fixed solely because code changed.

### VERIFY
Check for obsolete/deprecated/removed APIs, wrong imports, version mismatches, incorrect assumptions, nonexistent options. Record status as VERIFIED | LIKELY | POSSIBLE | UNVERIFIED. Do not rewrite working code for style alone.

### UPDATE
Determine current usage, target version, installed version, whether migration is required for the task, and what could break. Do not force unrelated upgrades.

## Shared state

Persist to `.forge/state.json` (schema: `core/schema.json`). Optionally maintain `.forge/current.md` for humans.

Key sections: environment, verification, assumptions, decisions, files_changed, testing, history, handoff.

Provenance and verification status must be explicit. Never silently overwrite conflicting information.

## Anti-hallucination rules

- Do not invent APIs, package features, config keys, commands, or files.
- Do not claim verification that was not performed.
- Prefer official documentation for the exact version over model memory or secondary sources.
- When uncertain: INVESTIGATE FIRST. If still unknown: MARK AS UNKNOWN / UNVERIFIED.

## Minimal change

The correct solution is often the smallest one that works with the current environment. Avoid speculative refactors, unrelated cleanup, and dependency churn.

## Multi-agent handoff

Before stopping, refresh `current_state` and `next_action`, complete the `handoff` object, and write the state files. The next agent must re-verify key environment facts before acting on them.

## Full rules

See `core/protocol.md` for complete protocol rules and `core/schema.json` for the state schema.
