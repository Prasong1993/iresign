# NEXUS / IRIS — Project Knowledge Library

**Repository:** `Prasong1993/iresign`  
**Purpose:** Central, evidence-first documentation index for understanding NEXUS and IRIS separately and evaluating possible future integration.  
**Current mode:** READ-ONLY research  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Implementation / Integration:** NOT AUTHORIZED by the current Phase 0 checkpoint

## Document map

| Document | Purpose | Status |
|---|---|---|
| [MASTER_PROJECT_KNOWLEDGE.md](./MASTER_PROJECT_KNOWLEDGE.md) | Project context, principles, scope, reported component map, integration principles and deliverables | Documentation created; claims retain evidence labels |
| [NEXUS_SOURCE_REVIEW_PLAN.md](./NEXUS_SOURCE_REVIEW_PLAN.md) | NEXUS repository identity, reported modules, review questions and read/write paths | Historical source references; live revalidation required |
| [IRIS_SOURCE_REVIEW_PLAN.md](./IRIS_SOURCE_REVIEW_PLAN.md) | IRIS scope, reported modules, database paths and review questions | Historical source references; live revalidation required |
| [INTEGRATION_READINESS.md](./INTEGRATION_READINESS.md) | Ownership, REST/MCP contracts, data/state boundaries and blockers | Proposed evaluation; no integration approved |
| [END_TO_END_WORKFLOW.md](./END_TO_END_WORKFLOW.md) | G0 gates through controlled implementation, verification, release and operations | Phase 0 only is currently in scope |
| [EVIDENCE_AND_VERIFICATION_MODEL.md](./EVIDENCE_AND_VERIFICATION_MODEL.md) | Evidence labels, provenance, test/CI/runtime distinction and closure criteria | Required documentation standard |
| [BLACKLIST_AND_CHANGE_CONTROL.md](./BLACKLIST_AND_CHANGE_CONTROL.md) | Explicit prohibitions, approvals and blocked operations | Checkpoint-derived; standalone TickTick blacklist record not found in attempted searches |

## Current checkpoint

- Checkpoint: `NIR-P0-004 — Provenance Gap Closure & Phase 0 Evidence Consolidation`
- Task ID: `6acfd06b8f0876e81c5f89fd`
- Parent: `NIR-P0-003`
- Phase: 0 — Discovery & Evidence Verification
- Mode: READ-ONLY
- Execution: PENDING
- Baseline / Source of Truth: UNKNOWN / NOT SELECTED
- Next documented gates: G0-07 Mapping Register, then G0-08 Document Consistency
- Runtime/tests/failure injection: NOT RUN
- Phase 1: NOT AUTHORIZED

## Source identity references (historical; revalidate before use)

- NEXUS candidate: [Prasong1993/Loop-Controller](https://github.com/Prasong1993/Loop-Controller), recorded SHA `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`.
- IRIS candidate: [Prasong1993/Prasong](https://github.com/Prasong1993/Prasong), scope `IRIS/iris-controller-v0.6.5/`, recorded SHA `fee44e82a0926ca85833beff8a9462156117a2d9`.
- Cloudflare candidate: [Prasong1993/LoopController](https://github.com/Prasong1993/LoopController), previously marked `BLOCKED — IDENTITY MISMATCH`; do not select as baseline without resolution.

These SHAs and component descriptions are historical handoff data, not live confirmations of current repository heads or runtime behavior.

## Working rules

1. Keep NEXUS and IRIS separate until source identity, ownership, contracts, security and data semantics are verified.
2. Preserve existing evidence and historical observations.
3. Mark statements VERIFIED, REPORTED, INFERRED, UNKNOWN, BLOCKED, NOT RUN or IN PROGRESS as appropriate.
4. Distinguish PLANNED, DISPATCHED, EXECUTED and VERIFIED.
5. Do not claim a folder, document, test, integration or runtime is complete unless directly checked.
6. This library describes the work; it does not authorize source changes, deployments, baseline selection or integration.
