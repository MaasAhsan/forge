# Example 2 — Symptom vs root cause

## Scenario

A runtime error appears in a UI component. Logs and stack traces point to a data-loading layer instead.

## Expected Forge behavior (DEBUG mode)

1. Reproduce the failure.
2. Gather evidence (logs, stack, network, state).
3. Isolate the actual failing boundary.
4. Form a hypothesis about root cause.
5. Test the hypothesis.
6. Apply a minimal fix at the root cause.
7. Retest the original reproduction.
8. Update verification and testing records.

## Failure mode to avoid

Patching the UI component because that is where the error surface appears, without investigating the data layer.
