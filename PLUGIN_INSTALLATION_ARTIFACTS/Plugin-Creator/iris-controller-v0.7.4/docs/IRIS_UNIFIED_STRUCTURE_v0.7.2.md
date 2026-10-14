# IRIS Unified Plugin Structure — v0.7.2

Status: SOURCE STRUCTURE RECORDED; LIVE MCP AND CHATGPT HOST VERIFICATION NOT YET PROVEN.
Plugin ID: `plugins_6ac62091066c8191beaece899cdc8b8c`
Current release at record time: `pluginrel_6acaf7609b00819194928948beaacf14`

## Path authority rules
1. Treat this document and the current Plugin Creator file listing as the source of truth for paths in this package.
2. Use exact relative paths from the file listing; do not infer a path from an old release, GitHub tree, memory, or a similarly named plugin.
3. Before editing, read the current file and record `current_release_id`. Submit updates with that exact ID as `expected_release_id`.
4. The active MCP entrypoint is defined by `.mcp.json`. Do not assume another server file is active just because it exists.
5. Do not delete files or uninstall legacy plugins until merged capabilities and runtime behavior are verified.
6. Keep source inspection, unit tests, database read-back, live MCP verification, and ChatGPT-host/mobile verification as separate evidence levels.

## Package layout
- `plugin.json` — primary package manifest and plugin version.
- `.codex-plugin/plugin.json` — host interface metadata; version must match `plugin.json`.
- `.mcp.json` — active MCP server mapping; currently launches `runtime/launch_merged_mcp.py`.
- `skills/iris/SKILL.md` — workflow contract and limits for model/tool behavior.
- `runtime/launch_merged_mcp.py` — active merged MCP launcher.
- `runtime/merged_mcp_server.py` — merged MCP tool registration/dispatch; composes the existing controller MCP server with extension tools.
- `runtime/merged_extensions.py` — deterministic project-policy checks and SQLite-backed usage-ledger functions.
- `runtime/mcp_server.py` — existing core MCP server; retained and imported by merged server.
- `runtime/controller.py` — core work state machine and controlled steps.
- `runtime/database.py` — SQLite persistence/schema for core records and merged extension records.
- `runtime/model.py` — workflow/state models and step definitions.
- `runtime/verify.py` — deterministic verification logic.
- `runtime/tool_registry.py` — explicit capability registry/routing; routing selects a registered capability but does not itself invoke an external provider.
- `runtime/main.py` — legacy/separate REST entrypoint from v0.6.19; it is not the active MCP entrypoint configured by `.mcp.json`.
- `tests/` — API, controller, database, MCP, registry, end-to-end, version-alignment and merged-extension test sources.
- `README-MERGE.md` — merge summary and migration/verification caveats.
- `docs/` — prior version notes and structure/contract documents.

## Capability ownership
- Core controller: five-step work flow, evidence, checkpoints, errors, verifications, audit and runtime telemetry.
- Project policy extension: project status, phase, budget and duplicate-task gates; task creation is expected only after a passing policy check.
- Usage ledger extension: `record_usage`, `list_usage`, `get_usage`, `update_usage`; records are persisted in the shared IRIS SQLite database and updates append audit history.
- Tool routing: eligible registered tools only; no claim of automatic discovery of all ChatGPT-native tools or automatic external invocation.

## Database and migration boundary
The merged extension uses the same `IRIS_DB_PATH` as the core controller and extends the package's SQLite schema. This does not mean the separate legacy plugins' private data stores have been migrated. Do not claim old task or usage records were imported unless an explicit migration and read-back evidence exists.

## Current verified facts and open checks
- Package source was read back after the v0.7.2 update and showed the merged launcher in `.mcp.json`, version alignment in both manifests, and `APP_VERSION='0.7.2'` in `runtime/merged_mcp_server.py`.
- Test source files exist, including `tests/test_merged_extensions.py` and `tests/test_version_alignment.py`; their presence is not proof that tests were executed.
- Not yet proven here: execution of the package test suite, live MCP calls against the active runtime, persistence read-back in the deployed runtime, or successful calls from ChatGPT Android.
- Do not uninstall `chatgpt-control-api` or `iris-step1` until the above runtime checks and capability parity are verified.

## Safe change sequence
1. Read current Plugin Creator metadata/file listing.
2. Read exact files that will be edited and confirm active path from `.mcp.json`.
3. Make an additive change unless deletion is required and justified.
4. Update with the exact current release ID.
5. Read back manifests, launcher, changed code and tests.
6. Run tests in an executable environment; record output.
7. Verify live MCP behavior and persisted records.
8. Verify ChatGPT host/mobile access.
9. Only then consider uninstalling duplicate plugins.
