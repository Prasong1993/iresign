# IRIS unified plugin merge notes

This overlay keeps the existing `iris-controller` identity and core runtime, but switches its MCP entrypoint to `runtime/launch_merged_mcp.py`.

Merged capabilities:
- Existing five-step workflow, evidence, checkpoints, errors, verifications, audit, telemetry and explicit tool registry.
- SQLite-backed usage ledger (`record_usage`, `list_usage`, `get_usage`, `update_usage`) with append-only audit events.
- Deterministic project controls for active status, allowed phases, budget limit and duplicate task checks (`create_project`, `check_project_policy`, `create_controlled_task`).

The extension schema is additive. It uses the same `IRIS_DB_PATH` as the existing controller. It does not import or copy data from the two legacy plugin stores. Existing old plugin data must not be assumed migrated.

Verification caveat: source and package tests must pass, then a live MCP call and ChatGPT-host/client verification are still required. Tool routing remains selection-only until a real adapter performs external invocation.
