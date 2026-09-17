# Example 3 — Multi-agent handoff

## Scenario

Agent A (any model) starts a feature. Later Agent B (different model/vendor) continues.

## Expected Forge behavior

1. Agent A writes progress to `.forge/state.json`, including environment, verified facts, decisions, files_changed, testing results, current_state, next_action, and a handoff block.
2. Agent B loads `.forge/state.json` (does not require Agent A’s chat history).
3. Agent B re-verifies key environment facts (project may have changed).
4. Agent B continues from `next_action`.

## Failure mode to avoid

Agent B re-discovering everything from scratch or inventing a different plan because conversation history is missing.
