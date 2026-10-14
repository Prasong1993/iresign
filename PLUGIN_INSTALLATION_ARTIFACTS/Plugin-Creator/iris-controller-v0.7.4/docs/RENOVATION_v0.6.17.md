# IRIS Control v0.6.17 — Renovation Notes

- Preserves the existing plugin ID, private personal scope, MCP server name/configuration, and all default prompts.
- Adds persisted MCP call lifecycle records and runtime status readback.
- Adds additive SQLite tables and schema version tracking; existing legacy tables are retained.
- Improves IRIS skill instructions for actual host-tool invocation, safe sequencing, error handling, evidence labels, and truthful delivery.
- `route_tool` remains selection-only. No external provider invocation adapter is included in this package.
- Local persistence test passed before publishing v0.6.16. The final v0.6.17 package requires another source read-back and host-specific test; host behavior is not inferred from source tests.
