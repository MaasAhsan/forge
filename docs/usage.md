# Usage

## Invoking Forge

Trigger phrases / situations:

- “Use Forge”
- “Build this the correct way for the current versions”
- “Debug this with evidence”
- “Verify these APIs against the installed packages”
- Presence of a `.forge/` directory
- Multi-agent handoff of coding work

## Typical BUILD session

1. Load skill → inspect project structure and manifests.
2. Record environment (declared + installed) with VERIFIED provenance where possible.
3. Verify any version-sensitive APIs against official docs for those versions.
4. Plan minimal change.
5. Implement.
6. Run proportional tests.
7. Update `.forge/state.json`.

## Typical DEBUG session

Follow the evidence pipeline in `core/protocol.md`. Keep symptom, root cause, and fix clearly separated in the state file.

## Reading existing state

```bash
cat .forge/state.json
# or
cat .forge/current.md   # if generated
```

## Handoff

When stopping:

- Refresh `current_state` and `next_action`
- Complete the `handoff` object
- Write the state file

The next agent should re-verify environment before acting on critical assumptions.
