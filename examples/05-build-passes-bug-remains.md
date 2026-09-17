# Example 5 — Build succeeds but original bug remains

## Scenario

A change is made; the project builds cleanly. The original runtime failure still occurs.

## Expected Forge behavior

1. Do not declare success solely because the build passed.
2. Reproduce the original failure case.
3. Continue debugging with new evidence.
4. Record that build verification passed while runtime verification failed.
5. Keep the bug in `known_issues` or `blocked` until the reproduction is fixed.
