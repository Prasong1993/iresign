# IRIS Control v0.6.19 — Runtime Version Alignment

## Confirmed source defect
The v0.6.18 package manifests declared version 0.6.18 while `runtime/main.py` and `runtime/mcp_server.py` reported `APP_VERSION = "0.6.16"`.

## Changes in this release
- Align REST `APP_VERSION` and FastAPI application version with package version 0.6.19.
- Route MCP startup through `runtime/launch_mcp.py`, which sets the legacy MCP module's version global to 0.6.19 before server startup.
- Preserve the existing MCP server implementation and database path configuration.

## Verification limits
- Static syntax checks can verify Python parsing only.
- MCP handshake and ChatGPT-host execution must be tested in a host with the `mcp` dependency and plugin runtime access; source packaging alone does not prove either.
- External provider invocation remains unimplemented by `route_tool`; routing is not execution.
