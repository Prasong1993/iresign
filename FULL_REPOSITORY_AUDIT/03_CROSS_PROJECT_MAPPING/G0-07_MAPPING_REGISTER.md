# G0-07 — Cross-Project Mapping Register

**Checkpoint:** NIR-P0-004 — Provenance Gap Closure & Phase 0 Evidence Consolidation  
**Phase:** 0 — Discovery & Evidence Verification  
**Mode:** READ-ONLY source review; documentation-only update in the central audit repository  
**Status:** IN PROGRESS — initial field-level mapping recorded; not a complete mapping  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Implementation / database migration:** NOT AUTHORIZED

## 1. Source identities used for this mapping

| Side | Repository and exact ref | Relevant source evidence |
|---|---|---|
| NEXUS operational record model | [Prasong1993/Loop-Controller](https://github.com/Prasong1993/Loop-Controller), `main` at `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | `docs/RECORDS_AND_EVIDENCE_SCHEMA.md` blob `35baaa09a55052967ad63bae0059bec88bb6f479`; `docs/OPERATIONAL_RECORD_SCHEMA.md` blob `e4ea653cc626627626d39c699205e7dd68d50dcd`; `nexus/records.py` blob `2fea2e46cd790c6dc9225a6532c35d48cd586acd`; `nexus/core.py` blob `bd12f4af3fa59b919ef029a5c9dada047073067b` |
| IRIS v0.6.5 model | [Prasong1993/Prasong](https://github.com/Prasong1993/Prasong), `main` at `fee44e82a0926ca85833beff8a9462156117a2d9` | `IRIS/iris-controller-v0.6.5/runtime/database.py` blob `c3937168f3904b804948c7a090ffd8f7f43cd11c`; `runtime/model.py` blob `92beff61b7f113a6395ae38712c529bad252da13`; `runtime/controller.py` blob `194c81e48dadf5f89a6c5e14731b5288b86164f8`; `runtime/main.py` blob `7a883223a0f5dcccf3c9fa45800ae628e6e032dc`; `tests/test_api.py` blob `7d060a16e5cf1f1ce36b0b3b423c49feaf4c2085` |

The recorded `main` branch heads matched the historical target SHAs during live revalidation. This register maps source contracts and schema declarations; it does not select either system as a baseline.

## 2. Field and record mapping

| Mapping ID | NEXUS field/record | IRIS field/record | Classification | Evidence-based finding | Gap / follow-up |
|---|---|---|---|---|---|
| MAP-001 | `project_id` in NEXUS project/task/evidence and operational-record scope | IRIS `work_units.id` / `work_id` used by step runs, errors, checkpoints, verifications and audit rows | **CONFLICT** | NEXUS distinguishes a project from a task; IRIS v0.6.5 schema uses a work-unit identifier as the common workflow scope and has no `project_id` column in the listed tables. | Do not map these IDs 1:1. Need an explicit project-to-work-unit relationship if future integration is approved. |
| MAP-002 | NEXUS `task_id`, optional on operational record envelope; core task has `task_id`, `project_id`, state and expected outcome | IRIS `work_units.id`, `title`, `status`, `current_step` | **SEMANTIC CANDIDATE** | Both can identify a unit of work, but their lifecycle scope differs: NEXUS task belongs to a project and uses a broader state machine; IRIS work unit tracks the five-step workflow. | Need state/lifecycle mapping and explicit ownership; do not merge identifiers. |
| MAP-003 | NEXUS `evidence` table/core evidence flow and evidence-record payload (`claim`, `source_url`, quote/provenance/verification metadata) | IRIS `evidence(id,status,topic,fact,source,verification_state,created_at)` | **SEMANTIC CANDIDATE** | Both store claims/facts with source and verification state. NEXUS's contract carries richer provenance fields such as publisher, page title, retrieved time, source revision, quote hash, method, limitations, reviewer, requirement/test links; IRIS table does not expose those columns. | Record each field-level correspondence; missing fields remain UNKNOWN/NO EQUIVALENT rather than being silently dropped. Review NEXUS core evidence table and operational evidence envelope separately. |
| MAP-004 | NEXUS checkpoint: checkpoint ID, task ID, state/snapshot metadata; schema contract includes snapshot hash, restore count/status | IRIS `checkpoints(id,work_id,step,state,snapshot,created_at)` | **SEMANTIC CANDIDATE** | Both persist resumable workflow state. IRIS snapshot is stored as serialized JSON text; the table has no explicit snapshot hash, restore count, or restore status fields. | Need restore semantics, integrity checks, stale-state handling, and external side-effect behavior reviewed before any mapping can be accepted. |
| MAP-005 | NEXUS verification contract: target record, method, expected/observed, result, verifier version, checked time, test URL | IRIS `verifications(id,work_id,expected,actual,status,note,created_at)` | **SEMANTIC CANDIDATE** | Both store expected-versus-observed outcomes, but IRIS v0.6.5 table lacks target record ID, method, verifier version and test-run URL fields. | Preserve distinctions between static review, unit, integration, runtime and host acceptance. Do not equate `status=VERIFIED` with evidence of external runtime verification without a linked test record. |
| MAP-006 | NEXUS error payload: error code/category/severity, redacted message, component/operation, retryability, occurrence history, resolution and related record IDs | IRIS `errors(id,work_id,step,attempt,error_type,message,expected,actual,root_cause,impact,correction,verification,prevention_rule,created_at)` | **SEMANTIC CANDIDATE** | Both preserve diagnostic records and corrective/verification context, but their fields and granularity differ. NEXUS explicitly defines redaction controls; IRIS schema stores a `message` field and requires a separate privacy/security review. | Map error taxonomy and retry/resolution semantics. Review whether message content is redacted before any future export; do not copy raw error content into the central evidence repository. |
| MAP-007 | NEXUS `audit_log`: event ID, project/task IDs, event type, state transition, actor, reason, time, details | IRIS `audit_log(id,work_id,action,details,created_at)` | **SEMANTIC CANDIDATE** | Both record workflow events, but NEXUS schema has explicit project/task scope, actor, reason and transition fields; IRIS stores a smaller work-scoped action/details record. | Need actor attribution, event ordering, state-transition semantics, and retention guarantees compared. |
| MAP-008 | NEXUS `operational_records` in `nexus/records.py`, with common envelope and JSON payload | IRIS split tables: `evidence`, `work_units`, `step_runs`, `errors`, `checkpoints`, `verifications`, `audit_log` | **SEMANTIC CANDIDATE** | Both persist operational evidence, but the storage grain differs: one NEXUS record envelope with `record_type` and `payload_json` versus IRIS typed relational tables. NEXUS core also has its own normalized project/task/evidence/audit/checkpoint tables. | Do not prescribe a unified schema yet. Distinguish NEXUS core workflow state from NEXUS operational record store before designing any central data model. |
| MAP-009 | NEXUS schema documentation proposes normalized append-only tables for usage, errors, evidence, decisions, checkpoints and verification results | Current NEXUS `RecordStore` implementation defines `operational_records`; NEXUS core separately defines project/task/evidence/audit/checkpoint tables | **CONFLICT** | The design contract describes a broader normalized storage layout than the observed `RecordStore` table implementation. The operational-record store and core database are separate code paths; they are not one already-consolidated database. | Carry into G0-08 Document Consistency and implementation-coverage review. Do not call the contract fully implemented. |
| MAP-010 | NEXUS operational record envelope uses `occurred_at` as UTC RFC3339/ISO timestamp and links by trace/operation IDs | IRIS tables mostly use SQLite `CURRENT_TIMESTAMP`; step runs and records are linked by `work_id`, step and attempt | **SEMANTIC CANDIDATE** | Both timestamp records, but NEXUS includes cross-component trace and operation correlation fields; IRIS uses work/step/attempt correlation and timestamp defaults without an explicit timezone in the schema text. | Define time normalization and correlation strategy only after data-owner approval; no timezone conversion assumed. |
| MAP-011 | NEXUS task transition, checkpoint restore, evidence gating and audit history | IRIS `run_step` requires previous step to PASS, records CHECKING/WORKING/VERIFYING/PASSED/FAILED, and saves checkpoints/errors | **SEMANTIC CANDIDATE** | Both implement evidence-gated workflow progression and failure retention, but their gates and state models are not identical. IRIS defines five steps; its `WORKING_STRUCTURE` contains 22 section labels while the API labels the canonical 22 source as UNPROVEN. | Compare complete state enums, transitions, recovery semantics and final verification behavior; 22 labels are not proof of a canonical structure. |
| MAP-012 | NEXUS `project_id`, `task_id`, `trace_id`, `operation_id` correlation and search | IRIS `work_id`, `step`, `attempt`, row IDs | **NO EQUIVALENT** for full trace/operation correlation | No corresponding IRIS `trace_id` / `operation_id` fields were found in the inspected v0.6.5 schema. | Confirm against all in-scope IRIS files before closing; do not synthesize IDs and imply they were original data. |
| MAP-013 | NEXUS default operational record database `data/nexus.db`; NEXUS core has its own database boundary | IRIS DB path defaults to `runtime/data/iris.db` and can be overridden by `IRIS_DB_PATH` | **CONFLICT** as a migration assumption | The source code exposes separate database paths and schemas. There is no evidence that these databases are already one central DB or share IDs. | Full central DB migration is deferred. Preserve separate ownership and do not copy database contents at this phase. |

## 3. Cross-cutting findings

1. **Two distinct NEXUS persistence paths exist in the inspected source:** the deterministic core database (`projects`, `tasks`, `evidence`, `audit_log`, `checkpoints`) and `RecordStore` (`operational_records`). Do not collapse them into one schema in documentation.
2. **IRIS v0.6.5 is a five-step controller with typed SQLite tables.** Its source declares 22 `WORKING_STRUCTURE` section labels, while the API reports `canonical_22_source: UNPROVEN`; this is not evidence that the canonical structure is verified.
3. **Similar purpose does not mean exact field equivalence.** All semantic candidates need field-by-field evidence and explicit missing-field treatment.
4. **The six private Plugin Creator snapshots are separate plugin artifacts.** Their current 72 source files match the current Plugin Creator file contents in GitHub; this does not resolve NEXUS/IRIS system integration or prove runtime behavior.
5. **The Cloudflare `LoopController` candidate remains identity-blocked.** Its current inspected tree contained only `LICENSE`; do not use it as the Control API baseline.

## 4. Open items for G0-07

- [ ] Inspect all relevant NEXUS core task/evidence/checkpoint fields and the full state enum at the pinned SHA.
- [ ] Inspect the full IRIS final-verification and MCP code paths, including REST/MCP persistence differences.
- [ ] Inspect the current Project Control API source identity and central DB schema without importing database contents.
- [ ] Map exact field names, data types, nullability, lifecycle semantics, and ownership per table.
- [ ] Add evidence IDs for every field-level finding and preserve unknowns/conflicts.
- [ ] Review all project documentation for contradictions in G0-08.

## 5. Safety and execution status

- Source repositories: READ-ONLY.
- Audit-repository documentation: written and must be read back.
- Database migration/import: NOT RUN and not authorized.
- Runtime/tests/failure injection: NOT RUN.
- Baseline/source of truth: UNKNOWN / NOT SELECTED.
- Mapping register: IN PROGRESS, not complete.
