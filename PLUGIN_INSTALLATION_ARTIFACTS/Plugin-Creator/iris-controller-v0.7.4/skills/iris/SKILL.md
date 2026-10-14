---
name: iris-controller
description: Use IRIS as the single controlled workflow for evidence, project policy, task execution, usage ledger, verification, audit and recovery.
---

# IRIS Controller — Unified Operating Contract

## Authority boundary
The model analyzes and proposes. Deterministic controller code validates state, policy and required evidence before state-changing actions. Never claim that IRIS intercepts all native ChatGPT activity. It controls only work routed through the exposed IRIS tools and adapters.

## Required workflow
1. **RECEIVE** — preserve the user's task and identify project/work IDs.
2. **ANALYZE + RESEARCH** — gather fresh evidence for this task; prefer official or independently verified sources.
3. **VALIDATE** — check source, freshness, consistency, project status, phase, duplicate work, budget, permissions and required approvals.
4. **EXECUTE** — execute only the validated plan and permitted tool calls.
5. **VERIFY** — compare expected and actual outputs, read back persisted records, retain errors and checkpoints, and run final verification before delivery.

Do not skip steps or turn UNKNOWN into evidence. Label facts VERIFIED, RECOVERED, UNKNOWN or BLOCKED. If a gate fails, preserve the failed attempt and return to the earliest relevant correction step; do not silently erase history.

## Project policy
For controlled project work, call `check_project_policy` before execution. Use `create_controlled_task` only when policy passes. A denied result must be treated as a hard stop. Do not override budget, phase, active-project, or duplicate-task rules based on model judgment alone. Use `allow_rerun` only when a rerun is explicitly justified and authorized.

## Usage ledger
Use `record_usage`, `list_usage`, `get_usage`, and `update_usage` for persisted usage records. Never invent values, units, sources or statuses. Updates require the exact record ID, accept only supported fields, and append audit history. Do not claim deletion support.

## Tool routing
`route_tool` selects from tools explicitly registered with real adapter evidence; selection is not provider invocation. Never claim automatic discovery of all ChatGPT tools or successful external execution without a real call and result. Respect authentication, quotas, paid-call approval and budget constraints.

## Evidence, audit and recovery
Record evidence sources, expected-versus-actual checks, errors, checkpoints, tool-call traces and final verification. Separate static source review, unit tests, database read-back, live runtime verification and ChatGPT-host verification. Report each proof level separately. If the runtime or host is unavailable, mark it UNVERIFIED/BLOCKED.

## Usage on mobile
Use this plugin from a mobile ChatGPT client only when that client/account exposes the plugin connection and tool calls. Package updates alone do not prove mobile runtime availability. Do not require a desktop by default; report the exact client/runtime limitation if a tool is unavailable.
