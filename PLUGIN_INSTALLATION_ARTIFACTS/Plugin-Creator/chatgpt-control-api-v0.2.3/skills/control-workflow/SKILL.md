---
name: control-workflow
description: Enforce the ChatGPT Control API five-step task workflow and manage explicit usage records through the remote controller from any supported ChatGPT client, without a PC-only requirement.
---

# Control Workflow

## Client and platform compatibility
- Use the configured remote `control-api` MCP endpoint. Ordinary use must not require a desktop, PC, terminal, local process, or PC-only setup.
- Use the same remote tools from any ChatGPT client that exposes this plugin/MCP connection, including mobile when supported by the installed app, account, and feature availability.
- Do not claim compatibility is verified merely because this package was updated. Verify that the target client exposes the connection and that the remote endpoint responds to tool calls.
- The remote endpoint must be reachable over HTTPS and use durable server-side storage for records that need to persist across restarts/instances. The local `server/server.py` file alone does not make a deployed remote service available.
- Do not promise unlimited usage. Actual availability and limits depend on the ChatGPT plan/client, plugin/MCP access, remote hosting, authentication, and service quotas.
- If a client does not expose the connection or a tool call fails, report `CLIENT_RUNTIME_UNVERIFIED` with the concrete failure; do not tell the user to switch to PC as the default workaround.

## Fixed workflow
Use the `control-api` MCP tools for every controlled task. The AI is a reasoning/proposal layer; the controller is the state and policy authority.
1. RECEIVE: preserve the original task input and create an isolated attempt.
2. ANALYZE + RESEARCH: produce findings only from current-task evidence.
3. VALIDATE: validate format, evidence authenticity/freshness/hash, consistency, and policy.
4. EXECUTE: execute only an approved plan.
5. VERIFY: verify the actual result against the task and current evidence.

PASS at verification completes the task. Any format error, evidence inconsistency, execution failure, or verification failure creates a new attempt starting at Step 1. Previous attempts remain audit-only and must not be used as reasoning input for the new attempt.

## Usage data
When the user asks to update usage data, use the usage ledger tools rather than merely describing changes:
- `record_usage`: create a new usage record with a generated ID and timestamp.
- `list_usage`: retrieve records, optionally filtered by category or status.
- `update_usage`: modify an existing record by exact `usage_id`; preserve its ID and creation timestamp and add an audit event.

Usage records are separate from task workflow state. Only store fields explicitly supplied by the user or supported by current evidence. Never invent usage amounts, units, sources, or statuses. A missing or unknown field stays unknown. Do not delete records unless a dedicated authorized deletion tool exists. Report the record ID and resulting state after a successful write.

## Evidence rules
Allowed source_type values: OFFICIAL, VERIFIED, CROSS_VERIFIED. Findings must not reference unverified evidence.

## Routing rules
The model may propose the next step, but never changes state directly. The controller validates the proposal before transition.
