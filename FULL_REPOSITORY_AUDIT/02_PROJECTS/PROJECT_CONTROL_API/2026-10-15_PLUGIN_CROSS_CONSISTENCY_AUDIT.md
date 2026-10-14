# Plugin & Project-Control Cross-Consistency Audit
**Date:** 2026-10-15 (Thailand, UTC+07:00)
**Scope:** All six private plugins returned by Plugin Creator, plus the latest Project Control API recovery package and central registry in `Prasong1993/iresign`.
**Mode:** Read-only inspection of current plugin files/manifests and repository records; this report is a new additive record.
**Runtime status:** NOT RUN in this audit. No plugin was invoked as an application, no tests were executed, and no endpoint/mobile integration was verified.

## 1. Executive result

- **6/6 plugins located and their file inventories inspected.** Selected manifests, workflow instructions, runtime entrypoints, and IRIS validation/structure documents were read.
- The plugins share a consistent *design intent*: evidence before action, explicit policy/approval gates, expected-versus-actual verification, error retention, auditability, and truthful reporting.
- They are **not one integrated system today**. Two are instruction-only workflow packages, two IRIS packages overlap, and two have MCP/runtime configurations but their current host/runtime connectivity is not established by this source inspection.
- **No canonical controller/baseline is selected by this audit.** Do not run two controller state machines for the same task, merge repositories, delete a legacy plugin, or infer live connectivity from a manifest.
- The newest recovery record says the original Control API baseline is `UNKNOWN / NOT SELECTED`; this audit preserves that status.

## 2. Inventory — six current private plugins

| # | Plugin / version | Source-backed role | Connection/runtime evidence | Relationship and status |
|---|---|---|---|---|
| 1 | `assistant-error-guard` v0.2.0 | Behavioral preflight: scope, evidence labels, action-state distinctions, authorization, verification, error prevention. Includes lifecycle routing guidance. | Skills and manifests; no MCP server mapping in the inspected file inventory. | Best candidate for the common *review/preflight layer*, not a deterministic controller. Its own text says it is not a security boundary. |
| 2 | `evidence-workflow-guard` v0.1.0 | Generic evidence-first project lifecycle, bounded writes, read-back, acceptance checks and final report. | Skills-only package in inspected inventory; no runtime/API connection shown. | Strong overlap with Assistant Error Guard and NEXUS instructions. Use as a checklist/reference, not a second independent state machine. |
| 3 | `nexus-project-control` v0.1.1 | NEXUS state machine: INTAKE → RESEARCH → PLAN → POLICY → EXECUTE → VERIFY → AUDIT → COMPLETE; recovery and protected checkpoint rules. | README and skill explicitly state **no connected NEXUS REST/MCP server, durable server DB, or independent policy runtime**. | Instruction-only NEXUS procedure. Cannot be treated as the live NEXUS controller or proof of persistent checkpoint writes. |
| 4 | `chatgpt-control-api` v0.2.3 | Five-step task controller, attempt reset on failure, evidence validation, tool routing, separate usage ledger. | Has `.mcp.json` and `mcp.json` pointing to a remote HTTPS `/mcp` endpoint, plus `server/server.py`. Config presence is verified; endpoint reachability, authentication, durable remote storage and client access are **NOT VERIFIED**. | Candidate remote controller, but cannot yet be declared live/connected. Its five-step attempt policy differs from the NEXUS recovery policy and must be mapped before combining. |
| 5 | `iris-step1` v0.1.0 | Earlier FastAPI + SQLite project/task/phase/budget checks, queue and verification loop. Uses phase labels such as MCR/SRR/PDR/CDR/TRR/ORR. | Contains runtime source, but the inspected manifest has no MCP server mapping; runtime execution was not performed. | Older/separate IRIS package. It overlaps with the newer IRIS controller and has a different schema/runtime surface. Do not operate it alongside the newer controller for the same work. |
| 6 | `iris-controller` v0.7.4 | Unified five-step controller, deterministic project/budget/duplicate-task policy, SQLite evidence/errors/checkpoints/audit, usage ledger, explicit tool registry/routing. | `.mcp.json` maps to `python runtime/launch_merged_mcp.py` and `IRIS_DB_PATH`; source includes tests. Host launch, installed dependencies, current-release tests, database read-back and ChatGPT/mobile calls are **NOT VERIFIED in this audit**. | Most complete *source package* among the six, but not automatically the chosen or live controller. Legacy `iris-step1` must not be removed until parity and runtime are verified. |

## 3. Shared contract — aligned concepts

The following concepts are present across multiple packages and can form one common contract:

1. **Scope and identity first:** name the active project, task, repository/ref, and permitted target before acting.
2. **Evidence ledger:** record claim, source/path/URL, revision/time, evidence class, limitations and reviewer.
3. **Policy gate before side effects:** authorization, target identity, dependencies, duplicate/idempotency risk, reversibility and budget.
4. **Separate lifecycle states:** planned/dispatched/executed/verified; a selected route or successful API response alone does not prove the requested outcome.
5. **Verification:** compare expected with observed results; read back persisted writes; distinguish source review, test results, runtime and host/mobile E2E.
6. **Append-only failure history:** retain errors, attempts, checkpoints and audit trail; retry only after reconciling an uncertain external outcome.
7. **Truthful terminal status:** never report completion while required checks are failed, blocked, unknown or not run.

These are **semantic alignment**, not evidence of shared code, a shared database, common task IDs, automatic plugin-to-plugin invocation, or cross-plugin persistence.

## 4. Conflicts, drift and unresolved mappings

| ID | Finding | Classification | Required resolution |
|---|---|---|---|
| C-01 | NEXUS plugin README cites `Loop-Controller` commit `de504565a8f942396a6fc704a352baa1b2dece67`; the latest recovery record identifies its inspected snapshot as `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`. | **PROVENANCE DRIFT / NEEDS_REVALIDATION** | Re-read the NEXUS files at both exact commits and record which claims belong to which revision. Do not silently replace the plugin's provenance. |
| C-02 | NEXUS plugin explicitly has no connected API/MCP or durable backend, while its name can be mistaken for the NEXUS runtime controller. | **CAPABILITY-CLAIM RISK** | Keep it labelled “instruction-only” until an endpoint and real tool call are verified. |
| C-03 | ChatGPT Control API manifest contains a remote endpoint; local source contains a server, but this does not prove that the configured remote service runs that source or persists data. | **UNKNOWN / NOT RUN** | Verify the actual endpoint, authentication, tool listing, controlled test task, persisted record read-back, and supported ChatGPT client before calling it operational. |
| C-04 | Control API uses five-step isolated attempts and restarts from Step 1 on failure; NEXUS allows controlled recovery to an earlier relevant state. | **SEMANTIC CANDIDATE + POLICY DIFFERENCE** | Define one canonical retry/recovery rule and map both implementations before integration. Preserve previous attempts as audit-only where required. |
| C-05 | `iris-step1` and `iris-controller` overlap on SQLite, policy, task verification and audit, but their schemas, phase models and entrypoints differ. | **DUPLICATE-CONTROLLER RISK** | Keep the older package read-only/reference-only until schema and capability parity plus migration/rollback tests are proven. No uninstall/deletion in this audit. |
| C-06 | IRIS v0.7.4 source declares `APP_VERSION='0.7.4'` and the merged launcher in `.mcp.json`; historical validation document is for v0.6.5 and reports 23/23 tests plus 19/19 stdio E2E. | **HISTORICAL TEST EVIDENCE, NOT CURRENT RELEASE PROOF** | Re-run relevant tests against the exact v0.7.4 package and confirm manifest/launcher/runtime versions and persisted records. Do not reuse v0.6.5 pass counts as v0.7.4 verification. |
| C-07 | Assistant Error Guard and Evidence Workflow Guard both prescribe scope-first, evidence-first, gates, read-back and honest status. | **PROCEDURAL OVERLAP** | Treat Assistant Error Guard as the common behavioral preflight and retain Evidence Workflow Guard as a checklist/reference; avoid duplicating two parallel lifecycle ledgers. |
| C-08 | All six packages have no proof here of automatic discovery/invocation of every ChatGPT tool, and package metadata alone does not prove Android/iOS/iPadOS/web support. | **NOT VERIFIED** | Test each host/client surface separately; document only the exact client and connection actually tested. |
| C-09 | Latest recovery file states baseline `UNKNOWN / NOT SELECTED`, Cloudflare candidate `BLOCKED — IDENTITY MISMATCH`, and runtime/mobile integration `NOT RUN`. | **CONSISTENT — PRESERVE** | Do not promote NEXUS, IRIS, or Control API to the canonical baseline without evidence and explicit approval. |

## 5. Proposed common integration point (logical contract only)

This is a **proposed mapping**, not a claim that the plugins are technically wired together:

- **Behavioral preflight:** Assistant Error Guard — scope, evidence classes, authorization, duplicate-call safety and honest status.
- **Common evidence/acceptance checklist:** Evidence Workflow Guard — source ledger, timeline, batch verification and phase exit criteria.
- **Single primary controller per task:** choose exactly one only after its connection and persistence are verified:
  - IRIS Controller if its configured MCP runtime is actually exposed and its policy/usage tools pass runtime checks;
  - ChatGPT Control API if the remote endpoint and durable records pass equivalent checks;
  - otherwise **no deterministic controller is verified**, and work remains evidence-led/read-only or explicitly marked blocked.
- **NEXUS Project Control:** use as the NEXUS-specific process/checkpoint reference until its server integration is verified.
- **IRIS Step 1:** retain as legacy reference; do not run in parallel with IRIS Controller for the same task.

### Canonical evidence/status fields to align

`project_id`, `task_id`, `parent_task_id`, `source_ref`, `commit_sha`, `evidence_id`, `evidence_status`, `phase`, `authorization`, `attempt_id`, `planned_state`, `execution_state`, `expected_result`, `actual_result`, `verification_status`, `error_id`, `checkpoint_id`, `audit_ref`, `persistence_status`, `next_permitted_action`.

Treat these as a **mapping proposal**, not a confirmed common schema. Each plugin's current field names and semantics must be compared before any adapter or database migration.

## 6. Required next verification sequence

1. Reconcile the two NEXUS commit references by read-only source comparison.
2. Inspect remote Control API health/tool list and confirm the server's actual storage and read-back behavior; no destructive or production test.
3. Run the IRIS v0.7.4 test suite in an authorized executable environment; verify active `.mcp.json` launcher and database read-back.
4. Check whether the target ChatGPT host actually exposes either controller's tools; record Android/iOS/iPadOS/web separately.
5. Build a field-level mapping register with `EXACT`, `SEMANTIC CANDIDATE`, `CONFLICT`, `NO EQUIVALENT`, `UNKNOWN`.
6. Only after these checks, recommend one primary controller and any adapters. Keep baseline `UNKNOWN / NOT SELECTED` until an evidence-backed decision is approved.

## 7. Audit provenance

- Plugin inventories and selected current-release files read through Plugin Creator on 2026-10-15.
- Latest repository records read from `Prasong1993/iresign`, branch `master`:
  - `FULL_REPOSITORY_AUDIT/02_PROJECTS/PROJECT_CONTROL_API/2026-10-15_INITIAL_PROJECT_DATA_RECOVERY.md`, blob `1ebafecfc08aef806c2008d73020345a2338da4e`.
  - `CENTRAL_WORK_REGISTRY.md`, blob `2972a012701de73e0968ab1f8c415bcc90632d76`.
- Scope limits: this is not a complete scan of every source file in every package, does not include full source archives or live service logs, and does not claim tests/runtime integration were run.
