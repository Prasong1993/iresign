# Project Control API — Initial Project Data Recovery
**Capture date:** 2026-10-15 (Thailand, UTC+07:00)
**Destination:** `Prasong1993/iresign`, branch `master`
**Record class:** Initial project recovery / provenance-preserving reference
**Execution state:** WRITTEN only after commit response; read-back verification pending at time of creation
**Source-of-truth / baseline:** UNKNOWN / NOT SELECTED

## 1. Purpose and scope
Consolidate the recoverable starting information for the project referred to in prior conversations as “Control API” / “Project Control API” (Thai voice-transcription may render it as “คนโทน API”). This record is a dated evidence package, not a claim that every historical chat, external task, private archive, live database, or deployment record has been recovered.

Do not conflate the three similarly named repositories below. No code migration or baseline selection is authorized by this record.

## 2. Project intent recovered from prior user context
**Status: RECOVERED / USER_STATED; needs source-by-source revalidation.**

The project was intended to provide a control layer that reduces context loss and inconsistent execution across ChatGPT-assisted work. AI proposes; deterministic policy, authorization, evidence, and verification govern execution.

Recovered conceptual components:
- Task Registry
- Message Envelope
- Execution Agent Interface
- Evidence Registry
- Approval Gate
- Audit Trail

Recovered desired workflow:
`CONCEPT → DESIGN → EXECUTE → RESULT → VERIFY`
This earlier five-step description is a historical project requirement, not proof that every candidate implements it.

Recovered quality gates:
- Verify authentication and authorization.
- Verify the task workflow and allowed transitions.
- Require evidence and recorded outcomes.
- Record auditable decisions and execution results.
- Test the actual implementation before deployment.
- Do not treat a successful build, a live endpoint, or a source-code review as proof of live ChatGPT/mobile integration.

## 3. Candidate repositories and identity boundaries

| Candidate | Observed identity/ref | What the available evidence supports | Status / handling |
|---|---|---|---|
| NEXUS workflow/controller | [Prasong1993/Loop-Controller](https://github.com/Prasong1993/Loop-Controller), `main`, inspected tree at `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | Source contains NEXUS deterministic workflow, SQLite persistence, evidence gates, audit/operational records, REST and MCP adapters, and architecture documentation. | VERIFIED for the cited source snapshot; not automatically the original Control API baseline. Keep identity distinct. |
| IRIS / older controller candidate | [Prasong1993/Prasong](https://github.com/Prasong1993/Prasong), `main`, tree snapshot `fee44e82a0926ca85833beff8a9462156117a2d9` | Repository contains IRIS controller artifacts; this is a separate project/codebase. | RECOVERED / separately inventoried; do not merge with NEXUS or Control API by implication. |
| Cloudflare/D1 candidate | [Prasong1993/LoopController](https://github.com/Prasong1993/LoopController), `main`, tree snapshot `7c23df529f4ce2c25386f45f8b91fc90e5cf068d` | Recursive tree query returned only `LICENSE` at this exact ref. | BLOCKED — IDENTITY MISMATCH / insufficient source contents. Do not treat as confirmed source merely because the name resembles the other repository. |
| Central evidence destination | [Prasong1993/iresign](https://github.com/Prasong1993/iresign), `master` | Central registry and audit artifacts are being assembled here. | Destination only; not the application source of truth. |

## 4. Earliest recovered deployment notes — Cloudflare candidate
**Status: RECOVERED from earlier conversation notes; not revalidated against live Cloudflare account or deployment.**

Prior notes recorded:
- Worker name/URL: `project-control-api-cloudflare.prasong5843.workers.dev`
- D1 database name: `project-control-api-db`
- D1 binding: `DB`
- Secret name: `BOOTSTRAP_TOKEN`
- Prior intended branch: `project-control-api-cloudflare` in `Prasong1993/LoopController`
- At the time of the prior check, the endpoint `/_api/health` reportedly returned `Hello World!`, indicating the deployed response did not demonstrate the intended API behavior.
- User instruction recovered from that work: test the implementation successfully before writing/deploying the real API to Cloudflare.

These are historical observations only. Current worker existence, binding, secret configuration, branch content, endpoint behavior, and account access are **UNKNOWN / NEEDS REVALIDATION**. Never copy secret values into this record.

## 5. Current NEXUS candidate: source-backed architecture notes
**Source:** `Prasong1993/Loop-Controller`, `main`, inspected at commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`.

Files directly read for this record:
- `README.md`
- `docs/ARCHITECTURE_MAP.md`
- `docs/IMPLEMENTATION.md`
- `docs/OPERATIONAL_RECORD_SCHEMA.md`
- `docs/CHATGPT_INTEGRATION_CONTRACT.md`
- `nexus/core.py` (blob `bd12f4af3fa59b919ef029a5c9dada047073067b`)
- `nexus/records.py` (blob `2fea2e46cd790c6dc9225a6532c35d48cd586acd`)
- `nexus/api.py` (blob `4e9d632e52f8f5d888e1cbd1d945b7968c09cbba`)

Observed source behavior/design:
- Deterministic workflow states: `INTAKE → RESEARCH → PLAN → POLICY → EXECUTE → VERIFY → AUDIT → COMPLETE`; recovery/block states include `RECOVER` and `BLOCKED`.
- Core policy/state logic is implemented in Python without using an LLM to decide policy transitions.
- SQLite tables include project/task/evidence/audit/checkpoint-related state; the operational record store is append-oriented and searchable.
- REST API and MCP adapter are intended to use the same workflow core.
- Evidence is scoped to the task or explicitly project-wide; source-backed verification is intended to precede planning.
- Execution requires an expected outcome and verification method; completion requires an audit state and recorded result.
- Operational record types include `usage`, `error`, `evidence`, `decision`, `checkpoint`, and `verification`; raw prompts, credentials, and unredacted payloads must not be logged.
- AI planning/code proposals are proposal-only; proposals are not themselves authorization to write or execute code.
- The repository README reports a CI run with 73 tests and OpenAPI checks, but that is repository-reported evidence and does not establish current runtime deployment or live ChatGPT integration.

Important limits explicitly stated in the source:
- Live ChatGPT integration: NOT CONFIGURED / NOT RUN.
- Production identity/OAuth, tenant isolation, secure deployment, rate limiting, secret management, backup/restore, concurrency/idempotency, adversarial network tests, and remote acceptance remain open or require verification.
- Passing CI does not prove a deployed, connected controller or Android/iOS/iPadOS invocation.

## 6. Historical deployment/API requirements vs NEXUS implementation
Keep the following separate rather than silently assuming equivalence:

| Requirement/claim | Evidence class | Current interpretation |
|---|---|---|
| Cloudflare Worker + D1 was the earlier deployment target | RECOVERED | Verify live account and exact source before relying on it. |
| `project-control-api-cloudflare` branch was intended | RECOVERED | Prior branch lookup reportedly did not find it; replacement branch was not approved. |
| Worker health endpoint returned `Hello World!` | RECOVERED | Historical observation; re-test before making a current claim. |
| NEXUS has REST/MCP source, workflow gates and operational records | VERIFIED at pinned source snapshot | Source inspection only; deployment and live integration are not implied. |
| NEXUS is the canonical implementation of the original Control API | UNKNOWN | No explicit baseline decision or verified mapping has been recorded. |
| Full database/history has been imported into this repository | NOT VERIFIED | This document contains selected reference data, not a database dump or complete history export. |

## 7. Evidence inventory and known gaps
Presently captured in this dated record:
- Project intent and recovered conceptual component list.
- Historical Cloudflare/D1 deployment notes with explicit RECOVERED label.
- Distinct repository identities, exact observed refs, and the LoopController tree limitation.
- Selected source-backed NEXUS architecture, workflow, data/record model, and integration limitations.
- Provenance URLs, commit SHAs, and blob SHAs for inspected source files.

Not present / not proven:
- Complete export of all prior conversations, TickTick records, Anchor documents, plugin records, private archives, or external database rows.
- Original Cloudflare project source code at the intended branch.
- Live Cloudflare configuration, secret values, current endpoint behavior, or deployment logs.
- Complete SQLite database contents or production data.
- Explicit approved source-of-truth/baseline selection.
- Runtime/end-to-end tests or live ChatGPT/mobile connector tests executed as part of this capture.

## 8. Safe next work order
1. Read back this file and the central registry from `iresign/master`.
2. Recover original project artifacts from their actual systems of record; preserve source IDs, timestamps, exact refs, and access limitations.
3. Compare requirements and data models across the candidates using a mapping register: `EXACT`, `SEMANTIC CANDIDATE`, `CONFLICT`, `NO EQUIVALENT`, `UNKNOWN`.
4. Keep the baseline `UNKNOWN / NOT SELECTED` until a documented, evidence-backed decision exists.
5. Do not deploy, migrate databases, rotate or reveal secrets, or copy code across repositories as part of evidence collection.

## 9. Capture audit
- Capture date: 2026-10-15 Thailand time.
- Destination branch: `master`.
- Source review: read-only.
- Data classification: a provenance-labelled recovery of available initial project information, not a complete recovery of every external record.
- Runtime tests performed for this capture: NOT RUN.
- Independent reviewer: NOT RECORDED.
