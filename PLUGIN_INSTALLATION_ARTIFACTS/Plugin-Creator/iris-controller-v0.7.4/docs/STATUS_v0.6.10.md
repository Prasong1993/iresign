# IRIS v0.6.10 — Host Runtime Restoration

Status: REOPENED FOR REAL HOST VALIDATION

Baseline restored from the v0.6.5 MCP execution contract:
- `.mcp.json` uses `python runtime/mcp_server.py`.
- MCP server exposes 7 tools.
- Five-step gate, evidence, errors, checkpoints, audit and final verification remain the runtime contract.

This release is not declared host-runtime PASS until the actual ChatGPT host invokes the MCP server and returns runtime evidence.

Known package-side issue retained for final reporting: host-side install/binding is dependent on the platform's Plugin Creator runtime path.
