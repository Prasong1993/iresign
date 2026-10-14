# Plugin Creator Private Plugin Archive Index

Purpose: preserve source snapshots for read-only audit in `Prasong1993/iresign`.

## Scope and limitations
- Captured from Plugin Creator using the owned personal-plugin inventory and source file reader.
- The inventory returned 6 private plugins with `USER` scope at capture time.
- Source files are stored with their original relative paths inside each versioned directory.
- Each snapshot includes `SOURCE_PROVENANCE.md` with plugin ID, version, release ID, scope, and capture limitations.
- These folders are audit/source snapshots, not official installable ZIPs or proof of installation/runtime testing.
- Plugin Creator remains the original source of each plugin.
- No plugin source or release was edited by this capture process.
- Byte-for-byte comparison against official archive packages has not been performed.

## Inventory

| Plugin | Version | Plugin Creator ID | Source files reported | Snapshot folder |
|---|---:|---|---:|---|
| evidence-workflow-guard | 0.1.0 | `plugins_6acc34888abc8191bf1189196d5d3a7a` | 3 | [folder](./evidence-workflow-guard-v0.1.0/) |
| nexus-project-control | 0.1.1 | `plugins_6acc2f56859881919690daf264cceeeb` | 4 | [folder](./nexus-project-control-v0.1.1/) |
| assistant-error-guard | 0.2.0 | `plugins_6acb788220688191ad91bd37d3d511da` | 5 | [folder](./assistant-error-guard-v0.2.0/) |
| chatgpt-control-api | 0.2.3 | `plugins_6ac6cfd6acb08191b21f17302a5b36b6` | 6 | [folder](./chatgpt-control-api-v0.2.3/) |
| iris-step1 | 0.1.0 | `plugins_6ac644a3b194819196e75722dcefc082` | 16 | [folder](./iris-step1-v0.1.0/) |
| iris-controller | 0.7.4 | `plugins_6ac62091066c8191beaece899cdc8b8c` | 38 | [folder](./iris-controller-v0.7.4/) |

**Total reported source files: 72 across 6 plugins.** Provenance documents are additional and are not included in the source-file total.

## Verification state
- Plugin Creator inventory/read: VERIFIED for the listed source paths; no missing paths or size-limited paths were reported in the source reads.
- GitHub destination writes: individual create-file calls returned commit SHAs for the 5 newly added plugin snapshots.
- Destination read-back of every file: NOT YET VERIFIED.
- Byte-for-byte parity with an official install archive: NOT RUN.
- Installation/runtime tests: NOT RUN.
