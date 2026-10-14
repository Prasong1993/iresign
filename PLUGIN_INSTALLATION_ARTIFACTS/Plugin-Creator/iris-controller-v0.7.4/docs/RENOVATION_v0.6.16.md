# IRIS Control v0.6.16 — Plugin Renovation

- Preserves the existing plugin ID, scope, MCP server name, connection configuration, and default prompts.
- Adds a persisted runtime status query and records MCP tool-call start/result/success/failure events in SQLite.
- Adds additive schema tables for runtime events, tool registry/calls, tasks, policy decisions, recovery points, and verification results.
- Keeps `route_tool` honest: it selects an eligible registry entry but does not invoke external providers.
- Updates the IRIS skill to continue independent work when monitoring is unavailable, call actual host tools directly when available, and distinguish source/test/database/runtime/host proof.
- Verification must be performed after packaging; the source change alone does not establish ChatGPT-host behavior.
