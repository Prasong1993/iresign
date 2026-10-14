# Plugin Installation Artifacts — Review Archive

This directory stores provenance-labelled copies of installation-related source files for audit and inspection. It is not the official source of truth, not a validated release, and not a guarantee that a plugin installs or runs.

## Current discovery
- **IRIS v0.6.5:** plugin-shaped source package discovered in `Prasong1993/Prasong`, target commit `fee44e82a0926ca85833beff8a9462156117a2d9`, path `IRIS/iris-controller-v0.6.5/`. The 21-file text snapshot at `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/` was read back and content-matched against that commit.
- **NEXUS:** a standalone install package was not identified in the inspected tree at historical commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`. Do not invent a package or treat the repository itself as a plugin installer.
- **Dropbox:** the visible `Plugin-Creator-Archive` folders returned no files in the listing performed for this task. No Dropbox package has been copied from that location.

## Contents policy
The IRIS snapshot preserves text files and their relative paths under `IRIS/iris-controller-v0.6.5/`, including plugin metadata, skill, runtime, tests, documentation, requirements, and MCP configuration. The source repository remains unchanged.

## Safe use
- Inspect files; do not execute or install from this archive during read-only audit.
- Never place secrets, API keys, tokens, live database files, or production data here.
- Refer to `ARTIFACT_MANIFEST.md` for source provenance and per-file hashes.
- The destination copy may have different Git blob SHA than the source. Both identities must be recorded separately.
- Missing binary release bundles or archives remain a gap; they must not be fabricated from text files.

## Status
`VERIFIED — IRIS v0.6.5 source snapshot contains 21/21 expected files and all contents match the pinned source commit. Official archive parity and install/runtime remain NOT VERIFIED.`
