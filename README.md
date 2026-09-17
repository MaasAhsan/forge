# Forge

**WRITE THE RIGHT CODE FOR THE ACTUAL CURRENT ENVIRONMENT.**

Forge is a multi-agent, multi-LLM coding and debugging skill focused on:

- Correctness over confidence
- Current-version compatibility
- Evidence-based debugging
- Explicit verification and assumption tracking
- Portable shared state for agent handoffs

It does not depend on any single proprietary platform.

## Repository layout

```
forge/
├── core/                 # Shared protocol, schema, instructions
│   ├── SKILL.md
│   ├── protocol.md
│   └── schema.json
├── adapters/             # Thin platform-specific discovery / install metadata
│   ├── claude/
│   ├── codex/
│   ├── cursor/
│   ├── devin/
│   ├── gemini/
│   ├── hermes/
│   ├── kimi/
│   ├── opencode/
│   └── generic/
├── universal/            # Platform-independent skill package
│   └── forge/
│       ├── SKILL.md
│       ├── protocol.md
│       └── schema.json
├── docs/                 # Human documentation
├── examples/             # Concrete scenarios
├── tests/                # Validation and protocol tests
├── scripts/              # Helper scripts
└── dist/
    └── forge-skill.zip   # Ready-to-upload universal skill package
```

## Quick start (universal)

1. Obtain `forge-skill.zip`.
2. Import / install according to your chatbot or agent’s skill mechanism (usually extract so that `SKILL.md` is discoverable).
3. Invoke the skill on coding, debugging, or verification tasks.
4. Shared state is written to `.forge/state.json` in the project.

## Design philosophy

See `docs/philosophy.md` and `core/protocol.md`.

Core rule: **CORRECTNESS > CONFIDENCE**.

Prefer actual project state and official docs for the installed version over model memory.

## Modes

- **BUILD** — implement new functionality after inspecting the real environment
- **DEBUG** — evidence-first root-cause isolation and minimal fix
- **VERIFY** — check for obsolete APIs, version mismatches, incorrect assumptions
- **UPDATE** — assess whether migration is necessary and safe

## Multi-agent use

Any compatible agent can read `.forge/state.json` and continue. Use the handoff block when transferring work. The receiving agent should still re-verify environment facts.

## What is intentionally excluded from `forge-skill.zip`

- Platform-specific adapters and plugin manifests
- Full documentation tree
- Test fixtures and examples (kept in the repository for maintainers)

The ZIP contains only the self-contained universal skill.

## License

MIT
