# Example 4 — Conflicting version assumptions

## Scenario

Agent A assumed dependency X is version 2.x. Agent B later finds lockfile evidence of version 3.x.

## Expected Forge behavior

1. Detect the conflict.
2. Preserve both pieces of information in history.
3. Verify against the authoritative source (lockfile + installed package).
4. Mark the incorrect assumption INVALIDATED or SUPERSEDED.
5. Update environment section and continue with the verified version.
6. Emit `CONFLICT_DETECTED` / `ASSUMPTION_INVALIDATED` history events.
