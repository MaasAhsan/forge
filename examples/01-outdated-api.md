# Example 1 — Outdated API memory vs current project

## Scenario

The model remembers `React.createClass` or an old Next.js data-fetching API. The project uses a modern React / Next.js version.

## Expected Forge behavior

1. Inspect `package.json` and lockfile → determine actual React / Next.js versions.
2. Consult official docs for those versions.
3. Reject the remembered obsolete API.
4. Implement using the current compatible API.
5. Record environment and verification status in `.forge/state.json`.
6. Run typecheck / tests if available.

## Failure mode to avoid

Writing the old API because “it used to work” without checking the installed version.
