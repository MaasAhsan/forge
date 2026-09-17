# Forge Design Philosophy

## Primary goal

Write the right code for the actual current environment.

## Ordering of evidence

1. Actual project state (manifests, lockfiles, installed packages, source)
2. Declared and installed versions
3. Official documentation for the exact version in use
4. Official API / reference material, migration guides, changelogs
5. Official source repositories
6. Project-local documentation
7. High-quality secondary sources
8. Model memory (lowest)

## Correctness > confidence

An agent must be willing to say “I don’t know yet; this needs verification” rather than invent an answer.

## Minimal change

The smallest correct change that respects the current environment is usually the best change. Avoid speculative refactors and unrelated cleanup.

## Explicit uncertainty

Every non-trivial claim carries provenance. Verification status is explicit. Assumptions that are disproven are marked INVALIDATED or SUPERSEDED.

## Multi-agent first

Conversation history is ephemeral. Shared state is durable. Different models and vendors must be able to continue the same task from the same files.
