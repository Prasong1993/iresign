# Central Work Registry — iresign

- **Purpose:** Centralize reusable work context, evidence references, workflow rules, decisions, checkpoints, errors, tool capability notes, and verification status for future work.
- **Target repository:** `Prasong1993/iresign`
- **Target branch:** `master`
- **Record type:** Curated central knowledge registry; this is **not** a SQLite database dump and does not claim to contain every historical chat or every external system record.
- **Registry status:** Initial evidence-backed seed; completeness and runtime integration are not yet verified.
- **Last assembled:** 2026-10-15

## 1. Evidence and status vocabulary

Use these labels consistently:

- `VERIFIED`: directly checked against a current source or test result, with a source reference.
- `USER_STATED`: explicitly stated by the user; not independently verified.
- `RECOVERED`: recovered from prior notes or conversation context; revalidate before treating as current truth.
- `UNKNOWN`: insufficient evidence.
- `BLOCKED`: unable to proceed because a prerequisite, permission, identity, or evidence is missing.
- `NOT RUN`: the check or test has not been performed.
- `NEEDS_REVALIDATION`: evidence exists but may be stale or scope-limited.

Execution lifecycle must be reported separately from evidence status:
`PLANNED` → `DISPATCHED` → `EXECUTED` → `VERIFIED`.
Do not equate a planned or executed action with a verified result.

## 2. Source-of-truth and repository map

| Alias / role | Repository or source | Current evidence status | Notes |
|---|---|---|---|
| NEXUS workflow/controller candidate | [Prasong1993/Loop-Controller](https://github.com/Prasong1993/Loop-Controller) | `VERIFIED` — selected files read at commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | Contains `nexus/core.py`, `nexus/records.py`, API/MCP modules and architecture documentation. Candidate source for reusable workflow and evidence concepts; not automatically the universal baseline. |
| IRIS / legacy controller candidate | [Prasong1993/Prasong](https://github.com/Prasong1993/Prasong) | `RECOVERED` — prior review notes | Prior notes mention IRIS and LF versions. Current contents and commit must be re-read before implementation. Keep IRIS separate from NEXUS unless explicitly approved. |
| Cloudflare Workers/D1 candidate | [Prasong1993/LoopController](https://github.com/Prasong1993/LoopController) | `BLOCKED` — identity mismatch in prior recovery notes | Do not merge or select as baseline without resolving repository identity. This name is distinct from `Loop-Controller`. |
| Target for this registry | [Prasong1993/iresign](https://github.com/Prasong1993/iresign) | `USER_STATED` target; `VERIFIED` branch name `master`; target contents not fully inventoried | A request to place the central work information here was made on 2026-10-15. This file is an initial seed, not proof of complete integration. |

**Baseline rule:** Source of Truth / baseline remains `UNKNOWN / NOT SELECTED` until an explicit, evidence-backed decision is recorded. Do not silently combine the candidate repositories.

## 3. NEXUS data model and workflow — source-backed notes

Source references:
- [nexus/core.py at pinned commit](https://github.com/Prasong1993/Loop-Controller/blob/eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa/nexus/core.py)
- [nexus/records.py at pinned commit](https://github.com/Prasong1993/Loop-Controller/blob/eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa/nexus/records.py)
- [Architecture map](https://github.com/Prasong1993/Loop-Controller/blob/eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa/docs/ARCHITECTURE_MAP.md)
- [Operational record schema](https://github.com/Prasong1993/Loop-Controller/blob/eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa/docs/OPERATIONAL_RECORD_SCHEMA.md)

### 3.1 Workflow states observed in source

`INTAKE` → `RESEARCH` → `PLAN` → `POLICY` → `EXECUTE` → `VERIFY` → `AUDIT` → `COMPLETE`

Recovery/block states also exist: `RECOVER`, `BLOCKED`. Transitions are explicitly constrained in code. The reviewed implementation requires VERIFIED evidence before PLAN, an expected outcome and verification method before EXECUTE, and an AUDIT state plus recorded result before COMPLETE.

### 3.2 Core tables observed in source

- `projects`: project identity/name/creation time.
- `tasks`: task identity, project scope, title, workflow state, expected outcome, verification method, result, error code and timestamps.
- `evidence`: evidence claim/status/source/inspection time/notes, optionally task-scoped.
- `audit_log`: state and evidence events with actor, reason, timestamps and details.
- `checkpoints`: task state snapshot and timestamp.
- `operational_records` in `RecordStore`: structured append-oriented records for usage, error, evidence, decision, checkpoint and verification, including project/task/session/trace/operation identifiers, status, component, severity, summary and a structured payload.

The code defaults to SQLite path `data/nexus.db`; MCP/API can configure `NEXUS_DB` and `NEXUS_RECORDS_DB`. **The actual database file and its contents have not been confirmed available in this target repository.** Do not claim database records were migrated.

### 3.3 Operational record safety observations

The reviewed record writer rejects payload keys associated with credentials and raw content, including prompts, messages, tokens, source bodies, code snippets and patches. The architecture notes warn that separate SQLite files do not provide cross-database atomic transactions and that the append-oriented record store is not itself tamper-proof or cryptographically chained. These are source-code/documentation findings, not production deployment verification.

## 4. Central registries to maintain

These are logical registries. They may begin as Markdown/JSON files and should not be represented as live database tables until implemented and tested.

### 4.1 Project Registry

Required fields: `project_id`, `alias`, `repository_url`, `branch`, `scope`, `source_of_truth_status`, `owner_or_approver`, `last_verified_at`, `evidence_refs`, `notes`.

Rules:
- Keep Project 1/2/3 aliases mapped explicitly to real repository IDs before use.
- Do not infer identity from similar repository names.
- Separate NEXUS and IRIS.
- Baseline selection requires a recorded decision and supporting evidence.

### 4.2 Evidence & Source Registry

Required fields: `evidence_id`, `claim`, `source_url_or_path`, `repository_commit_or_version`, `retrieved_at`, `verification_method`, `status`, `scope`, `supports_or_conflicts_with`, `reviewer`, `notes`.

Rules:
- A URL in a registry does not mean its content was verified.
- Record exact source version/commit and claim supported.
- Keep direct source evidence separate from summaries and recovered memory.
- Mark runtime, mobile, deployed endpoint, integration, and production-database claims `NOT RUN` unless directly tested.

### 4.3 Knowledge & Decision Registry

Required fields: `record_id`, `topic`, `decision_or_finding`, `status`, `evidence_refs`, `alternatives`, `risk`, `approved_by`, `decision_date`, `supersedes`.

Rules:
- Do not turn a suggestion into an approved decision.
- Record conflicts explicitly; do not resolve identity/baseline conflicts by guess.
- Preserve old findings as historical/recovered, not current truth.

### 4.4 Workflow & Phase Registry

Required fields: `workflow_id`, `phase_id`, `objective`, `entry_criteria`, `required_inputs`, `allowed_actions`, `exit_criteria`, `verification_method`, `approval_gate`, `status`, `evidence_refs`.

Default evidence-first lifecycle:
- Phase 0 / G0: intake, source-of-truth mapping, read-only discovery, provenance and identity checks.
- Phase A: feasibility and constraints.
- Phase B: design and mapping.
- Build/execute phases: only after required evidence and approval gates pass.
- Verification and phase exit: independent checks and durable report.
A later phase must consume the approved evidence package from the prior phase; do not restart discovery without a documented reason.

### 4.5 Task & Checkpoint Registry

Required fields: `task_id`, `parent_task_id`, `project_id`, `phase_id`, `mode`, `authorization`, `current_state`, `verified_evidence_refs`, `completed`, `pending`, `blocked`, `not_run`, `risks_conflicts`, `next_action`, `checkpoint_persistence_status`, `updated_at`.

A checkpoint must state current scope, authorization, exact evidence references, completed/pending/blocked/not-run work, risks/conflicts, next safe action and whether the checkpoint was actually persisted.

### 4.6 Error & Recovery Registry

Required fields: `error_id`, `task_id`, `component`, `observed_symptom`, `reproduction_or_evidence`, `root_cause_status`, `mitigation`, `test_case`, `test_result`, `regression_risk`, `status`.

Do not label a root cause confirmed without reproducible evidence. Distinguish recovered workaround from verified permanent fix.

### 4.7 Tool & Integration Registry

Required fields: `tool_id`, `provider`, `capability`, `permission_status`, `cost_or_quota_constraints`, `side_effect_class`, `input_scope`, `output_evidence`, `last_tested_at`, `test_status`, `fallback`.

Before using an integration, inspect its actual available action/schema and authorization. Do not claim a tool was invoked unless it was invoked; do not claim integration works on Android/iOS/web without a real test.

### 4.8 Verification & Audit Registry

Required fields: `verification_id`, `requirement_or_claim`, `test_method`, `expected_result`, `actual_result`, `evidence_ref`, `status`, `reviewer`, `timestamp`.

Use three separate artifacts:
1. **Verification Checklist** — item-by-item criteria, status, evidence and reviewer.
2. **Checkpoint** — current state and handoff.
3. **Phase Exit Report** — phase outcome, criteria met/unmet, exceptions and authorization for next phase.

## 5. Recovered project-control rules

The following are recovered from prior user instructions and must be treated as working rules unless superseded by an explicit later instruction:

1. Start by inspecting existing project state and source evidence; do not rebuild before inventory.
2. Prefer official/current sources and pinned commits. Clearly label recovered historical notes.
3. Read/search work may be parallelized when independent; limit write batches and verify each write with a read-back.
4. AI may propose a plan; execution of material external changes requires the appropriate authorization.
5. Do not claim completion without observable evidence and post-action verification.
6. Keep original sources unchanged unless a specific modification is authorized.
7. Use ChatGPT as the main working surface; do not assume a separate runtime or mobile integration is available.
8. Avoid mixing project contexts or using a tool just because it was used in a previous task.
9. Preserve a restartable checkpoint and a concise phase exit report.
10. Use HTML status/roadmap summaries when a durable visual status report is needed; do not require Mermaid.

## 6. Recovered NEXUS / IRIS checkpoint context

These are historical context items and require revalidation against the latest source before execution.

- NEXUS task `NIR-P0-004`: “Provenance Gap Closure & Phase 0 Evidence Consolidation”; parent `NIR-P0-003`; Phase 0; READ-ONLY; repository/plugin/storage modification not authorized; baseline unknown/not selected; Phase 1 not authorized in the referenced checkpoint.
- Previous task reference supplied in recent conversation: `6acff8878f08565e5fe51399`. Treat as a user-provided task reference, not as a verified current task record until read from its system of record.
- A separate prior user message referenced a TickTick task ID `6acfd06b8f0876e81c5f89fd`; the IDs differ and must not be conflated. Confirm the correct ID in TickTick before updating any task.
- Prior recovery notes say `Prasong1993/LoopController` (no hyphen) has an identity mismatch and is blocked as a baseline candidate.
- Prior notes say an archive handoff was still awaited; no original `.tar.gz` archives were confirmed attached at that time.
- Runtime/integration tests and mobile invocation were not proven by the source review alone.

## 7. Known gaps and current status

| Item | Status | Required next verification |
|---|---|---|
| Seed registry written to target | `PLANNED` before this commit; must be confirmed by commit response and read-back | Read this file from `master` and compare content |
| Full target repository inventory | `NOT RUN` | Enumerate target files/branches and check for existing registry conflicts |
| Actual SQLite database file/data available | `UNKNOWN` | Inspect authorized source artifacts; do not fabricate data |
| Full historical work data imported | `NOT RUN` | Identify accessible authoritative reports, checkpoints and source records; import with provenance |
| Canonical baseline chosen among candidate repos | `UNKNOWN / NOT SELECTED` | Resolve identity and record explicit approval |
| NEXUS/IRIS runtime compatibility | `NOT RUN` | Mapping register and isolated tests |
| TickTick checkpoint created/updated | `NOT VERIFIED` | Read task, apply only authorized update, then read back |
| Android/iOS/iPadOS/web integration | `NOT RUN` unless separately evidenced | Test each supported surface and record result |

## 8. Next safe actions

1. Read back this file from `Prasong1993/iresign` on `master` and verify its commit/content.
2. Inventory the target repository before adding more files; do not overwrite existing project work.
3. Retrieve the latest authoritative reports/checkpoints from connected sources and add evidence references, preserving source IDs, timestamps and statuses.
4. Create a mapping register for NEXUS, IRIS and the target project with `EXACT`, `SEMANTIC CANDIDATE`, `CONFLICT`, `NO EQUIVALENT`, and `UNKNOWN` categories.
5. Keep baseline selection and any runtime or external-system writes pending until their authorization and prerequisites are established.

## 9. Change log

- 2026-10-15: Initial central registry seed assembled from inspected NEXUS source files and recovered project-control context. This entry does not assert full import, runtime integration, or test completion.
