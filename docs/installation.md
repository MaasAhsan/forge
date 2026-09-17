# Installation

## Universal skill (`forge-skill.zip`)

Location: `dist/forge-skill.zip`

This package targets the Agent Skills open standard (SKILL.md + supporting files). It is platform-independent.

### Contents

```
forge/
  SKILL.md
  protocol.md
  schema.json
```

### How to install

- **Claude Code / Claude**: Install as a plugin or place the extracted skill directory where Claude discovers skills (see current Claude Code docs for skills/ and plugins).
- **Cursor**: Place under `.cursor/skills/forge/` or user skills directory.
- **Codex**: Place under the skills discovery path used by Codex (see current Codex skills documentation).
- **Generic / other**: Extract so that a directory containing `SKILL.md` is readable by the agent. Many systems auto-discover folders named after the skill or containing a SKILL.md with matching frontmatter `name`.

Always prefer the current official documentation of the host platform for the exact install path and discovery rules. Do not invent directory names.

## Full repository

Clone or copy the entire repository when you need:

- Platform adapters
- Shared core for multi-agent projects
- Documentation, examples, and tests

Adapters are thin; they do not re-implement core logic.

## Shared state

Once the skill is active, state is written to:

- `.forge/state.json` (authoritative)
- `.forge/current.md` (optional human view)

Create these on first use.
