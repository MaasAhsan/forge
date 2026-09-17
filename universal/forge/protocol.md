# Forge Protocol v1

Portable rules for correctness-first, environment-aware coding and debugging across any agent or LLM.

## Core principle

**CORRECTNESS > CONFIDENCE**

Never treat model memory, old tutorials, or unverified assumptions as facts. Prefer:

1. Actual project state (manifests, lockfiles, installed packages, source)
2. Installed / declared versions
3. Official documentation for the exact version in use
4. Official API / reference docs, migration guides, changelogs
5. Official source repositories
6. Project-local documentation
7. High-quality secondary sources
8. Model memory (lowest priority)

When information cannot be verified, mark it **UNKNOWN** or **UNVERIFIED**. Never convert an assumption into a verified fact.

## Provenance values

Every non-trivial claim must carry provenance:

- `USER_PROVIDED` — stated by the human
- `VERIFIED` — confirmed against authoritative evidence (lockfile, official docs for the version, runtime check, etc.)
- `INFERRED` — derived from verified facts with clear reasoning
- `ASSUMED` — working hypothesis; must be tested or replaced
- `UNKNOWN` — cannot be established with available evidence

Assumptions that are disproven become `INVALIDATED` or `SUPERSEDED`.

## Verification status

Use exactly these labels:

- `VERIFIED` — confirmed against primary sources for the relevant version
- `LIKELY` — strong evidence but not definitive
- `POSSIBLE` — plausible, insufficient confirmation
- `UNVERIFIED` — not yet checked
- `CONFLICT` — sources disagree; both preserved until resolved

## Modes

Forge operates in one primary mode at a time. Record the mode in shared state.

### BUILD

1. Inspect the project (structure, manifests, config, related code).
2. Identify the real environment (declared vs installed versions).
3. Verify version-sensitive APIs against official docs for those versions.
4. Respect existing conventions; make minimal changes.
5. Implement only what is required.
6. Run the most relevant tests / builds / type checks.
7. Update verification record and shared state.

Do not invent APIs, configuration keys, or package behavior. Prefer zero or minimal new dependencies.

### DEBUG

Evidence-first workflow:

```
BUG → REPRODUCE → OBSERVE → GATHER EVIDENCE → ISOLATE
→ FORM HYPOTHESIS → TEST HYPOTHESIS → IDENTIFY ROOT CAUSE
→ APPLY MINIMAL FIX → RETEST → VERIFY
```

Distinguish:

- Symptom
- Root cause
- Contributing factor
- Unrelated issue

Never declare a bug fixed merely because code changed. Reproduce the original failure after the fix when practical. Do not introduce unrelated changes while debugging.

### VERIFY

Scan for:

- Obsolete / deprecated / removed APIs
- Incorrect imports or package usage
- Wrong framework or lifecycle assumptions
- Version mismatches
- Invalid commands or configuration
- Nonexistent functions or options
- Broken dependency relationships

Do not rewrite working code solely for style. Record verification status for each finding.

### UPDATE

When code may be outdated:

1. What does it currently use?
2. What version does the project target / have installed?
3. Does the usage still work?
4. What has changed in newer versions?
5. Is migration necessary for the current task?
6. What could break?

Do not force unrelated upgrades.

## Shared state location

Default paths (in order):

1. `.forge/state.json` — machine source of truth
2. `.forge/current.md` — optional human-readable summary
3. Path supplied by the user
4. Inline injection only when no filesystem is available

Create `.forge/` on first write if absent.

## Conflict rules

Never silently overwrite.

On conflict:

1. Detect
2. Preserve previous information
3. Record new information
4. Determine authoritative source (prefer verified project state + official docs for the installed version)
5. Mark superseded items
6. Emit history event (`CONFLICT_DETECTED`, `DECISION_CHANGED`, `ASSUMPTION_INVALIDATED`, `STALE_CONTEXT`, etc.)

## Multi-agent handoff

Before stopping:

1. Refresh `current_state` and `next_action`
2. Fill `handoff` with summary, critical context, verified facts, remaining risks, and items not to re-investigate
3. Write state files

The receiving agent must still re-verify environment and key facts before making important changes — the project may have changed since the handoff was written.

## Minimal change principle

Prefer the smallest change that correctly solves the stated problem while remaining compatible with the actual environment. Avoid speculative refactors, unrelated cleanup, and unnecessary dependency changes.

## Testing and verification record

After implementation:

- Run proportional checks (unit tests, typecheck, build, targeted runtime reproduction)
- A green build is not proof of correct runtime behavior
- Record commands, outcomes, and remaining uncertainty in the `testing` and `verification` sections

## Token efficiency

Store compact facts, statuses, references, and verification results. Do not persist full conversation history, repetitive explanations, or stale data with no remaining value.
