# Architecture

```
                    FORGE CORE
                 (protocol + schema + instructions)
                        |
          +-------------+-------------+
          |             |             |
       Claude         Codex         Cursor   ...   Generic
       Adapter        Adapter        Adapter
          |             |             |
          +-------------+-------------+
                        |
                 Shared Forge State
                 (.forge/state.json)
```

- **Core** is the single source of truth for behavior.
- **Adapters** only supply discovery metadata and install paths for each platform.
- **Universal package** is a self-contained skill for any SKILL.md-compatible host.
- **Shared state** is the durable handoff medium between agents.

Adapters never re-implement protocol logic.
