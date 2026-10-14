# MASTER PROJECT STRUCTURE — NEXUS-Core / iresign

**Repository:** https://github.com/Prasong1993/iresign  
**Branch:** `master`  
**Control checkpoint:** TickTick task `6acfd06b8f0876e81c5f89fd` — `NIR-P0-004 — Checkpoint: Provenance Gap Closure & Phase 0 Evidence Consolidation`  
**Parent checkpoint:** `NIR-P0-003`  
**Current phase:** Phase 0 — Discovery & Evidence Verification  
**Current mode:** READ-ONLY for source repositories; documentation/structure work in this audit repository is authorized by the user's latest instruction.  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Source-code modification, integration, deployment, and database migration:** NOT AUTHORIZED

## 1. Purpose and order of work

This repository is the **central evidence and review workspace**. It gathers traceable reference material from multiple repositories so code, architecture, checkpoints, tests, and project facts can be inspected from one place without mixing their identities.

Required order:
1. Finish and read back this directory and ownership structure.
2. Register every source repository, exact branch/commit, path, and evidence status.
3. Reconcile the six existing private Plugin Creator source snapshots and their provenance.
4. Collect or refresh source evidence into the correct project group, preserving original relative paths and source identity.
5. Build cross-project mapping registers only after the per-project evidence is traceable.
6. Keep the central/shared project information separate from any full database migration. **The old Project Control API / NEXUS-Core structure is unfinished; only its central/reference information belongs here for now. Do not copy its full database or claim it has been migrated.**
7. Verify every write by reading it back. A directory, index, manifest, source snapshot, test file, or CI configuration does not prove tests/runtime passed.

Existing plugin snapshots were placed in this repository before the structure was fully reconciled. Preserve them in place during this structural pass; do not delete, rename, or move them merely to make the tree look tidy. Record their present location and reconcile them after the structure is approved by evidence.

## 2. Governing evidence and change-control rules

- Preserve original evidence. Append or add new records; do not rewrite history to make old observations appear current.
- Track actions separately: `PLANNED`, `DISPATCHED`, `EXECUTED`, `VERIFIED`.
- Evidence labels: `VERIFIED`, `USER_STATED`, `RECOVERED`, `UNKNOWN`, `BLOCKED`, `NEEDS_REVALIDATION`, `PARTIAL`, `NOT RUN`, `IN PROGRESS`.
- Mapping labels: `EXACT`, `SEMANTIC CANDIDATE`, `CONFLICT`, `NO EQUIVALENT`, `UNKNOWN`.
- Each observation must identify its source repository, exact commit/ref, path/symbol or test/run ID, method, timestamp/timezone if captured, result, and limitations.
- Do not select a Source of Truth/Baseline unilaterally.
- Keep NEXUS, IRIS, Control API, and other repositories distinct until identity and ownership mappings are evidence-backed.
- Do not copy secrets, credentials, live database contents, or production data into the audit repository.
- No source-code changes, database migration, plugin-release mutation, deployment, dependency installation, runtime test, failure injection, or security attack testing without separate authorization.
- Do not mark runtime, integration, CI, or test results verified from source inspection alone.
- The repository is a review workspace, not automatically an installable plugin, official baseline, or production database.

## 3. Target directory structure

This is the target organization. The grouping directories and README index files listed below have now been created and read back on GitHub. Other files within those groups remain planned until created and verified. Existing source snapshots remain in their original locations.

```text
iresign/
├── README.md
├── FULL_REPOSITORY_AUDIT/
│   ├── MASTER_PROJECT_STRUCTURE.md             # this structure contract
│   ├── AUDIT_SCOPE.md                          # scope and permissions
│   ├── MASTER_CHECKPOINT.md                    # audit checkpoint history
│   ├── MASTER_CHECKLIST.md                     # phase gates
│   ├── EVIDENCE_REGISTER.md                    # append-only evidence log
│   ├── NEXUS_IRIS_EVIDENCE_REGISTER.md          # existing cross-system register
│   ├── NEXUS_IRIS_MASTER_CHECKPOINT.md          # existing cross-system checkpoint
│   ├── NEXUS_IRIS_PHASE_CHECKLIST.md            # existing phase checklist
│   ├── NEXUS_IRIS_PROJECT_KNOWLEDGE_AND_WORKFLOW.md
│   ├── 00_CONTROL_AND_CHECKPOINTS/              # created: README index verified
│   ├── 01_SOURCE_REPOSITORY_REGISTER/           # created: repository register verified
│   ├── 02_PROJECTS/
│   │   ├── NEXUS/                               # created: inventory and project index
│   │   ├── IRIS/                                # created: inventory and project index
│   │   ├── PROJECT_CONTROL_API/                 # created: candidate inventory and project index
│   │   └── SHARED_CORE/                          # created: reference-only index
│   ├── 03_CROSS_PROJECT_MAPPING/                # created: mapping index
│   ├── 04_FILE_INVENTORY_AND_ARCHITECTURE/       # created: inventory/architecture index
│   ├── 05_API_DATA_AND_READ_WRITE_PATHS/         # created: data/API index
│   ├── 06_SECURITY_IDENTITY_AND_OWNERSHIP/        # created: security/identity index
│   ├── 07_TESTS_CI_AND_RUNTIME_EVIDENCE/          # created: test/CI/runtime index
│   ├── 08_DOCUMENT_CONSISTENCY/                  # created: consistency-review index
│   ├── 09_BLACKLIST_AND_CHANGE_CONTROL/           # created: change-control index
│   ├── 10_WEBSITE_AND_INTEGRATION_READINESS/      # created: readiness index
│   ├── 90_EVIDENCE_HISTORY/                       # created: evidence-history index
│   ├── 98_BLOCKED_AND_MISSING_INPUTS/             # created: blocker index
│   ├── 99_SUPERSEDED_REFERENCE/                   # created: historical-reference index
│   └── PROJECT_KNOWLEDGE/                         # existing: project knowledge documents
└── PLUGIN_INSTALLATION_ARTIFACTS/
    ├── README.md                                 # artifact policy and limitations
    ├── ARTIFACT_MANIFEST.md                       # IRIS snapshot manifest; reconcile separately
    ├── Plugin-Creator/
    │   ├── INDEX.md                               # six private plugin snapshot index
    │   ├── evidence-workflow-guard-v0.1.0/
    │   ├── nexus-project-control-v0.1.1/
    │   ├── assistant-error-guard-v0.2.0/
    │   ├── chatgpt-control-api-v0.2.3/
    │   ├── iris-step1-v0.1.0/
    │   └── iris-controller-v0.7.4/
    └── IRIS/
        └── iris-controller-v0.6.5/                # existing source-repository snapshot
```

## 4. Project separation and source ownership

| Group | Role in this repository | Required separation |
|---|---|---|
| NEXUS | Reference evidence from `Prasong1993/Loop-Controller` | Keep original repository, ref and file paths; no assumption that it is an installable plugin |
| IRIS | Reference evidence from `Prasong1993/Prasong`, especially the recorded `IRIS/iris-controller-v0.6.5/` scope | Keep source version and Plugin Creator snapshot as distinct artifacts |
| Project Control API | Reference evidence from its identified source candidates and existing records | Identity/baseline unresolved until evidence maps the candidates; do not copy the full DB yet |
| SHARED_CORE | Cross-project concepts, common contracts, central data definitions and mapping notes | Reference-only at this stage; no full database import or migration |
| Plugin Creator six | Versioned snapshots of the six private plugins captured from Plugin Creator | Each plugin gets its own folder and provenance; snapshot is not automatically a downloadable installation package |
| Cross-project mapping | Relationships between fields, records, APIs and responsibilities | Must cite both sides and use the five mapping classifications |

Source identities must remain distinct:
- NEXUS candidate: `Prasong1993/Loop-Controller`, current observed `main` SHA `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` — **VERIFIED for branch-head identity and tree inventory (52 entries); not a baseline selection**.
- IRIS candidate: `Prasong1993/Prasong`, current observed `main` SHA `fee44e82a0926ca85833beff8a9462156117a2d9` — **VERIFIED for branch-head identity and tree inventory (107 entries); not a baseline selection**.
- Cloudflare candidate: `Prasong1993/LoopController`, current observed `main` SHA `7c23df529f4ce2c25386f45f8b91fc90e5cf068d`, tree contains only `LICENSE` (1 entry) — remains `BLOCKED — IDENTITY MISMATCH`; do not select as baseline.
- Audit workspace: `Prasong1993/iresign`, default branch observed as `master`; re-read HEAD before relying on any previous commit.

## 5. Six Plugin Creator snapshots — current recorded inventory

The current Plugin Creator inventory was re-read for all six private USER-scope plugins. Current source file lists and contents were compared with GitHub destination files; **72/72 source files matched exactly**. This verifies snapshot content parity with the current Plugin Creator source reader, not official archive parity or runtime/installability.

| Plugin | Version | Recorded source-file count | Snapshot |
|---|---:|---:|---|
| evidence-workflow-guard | 0.1.0 | 3 | `Plugin-Creator/evidence-workflow-guard-v0.1.0/` |
| nexus-project-control | 0.1.1 | 4 | `Plugin-Creator/nexus-project-control-v0.1.1/` |
| assistant-error-guard | 0.2.0 | 5 | `Plugin-Creator/assistant-error-guard-v0.2.0/` |
| chatgpt-control-api | 0.2.3 | 6 | `Plugin-Creator/chatgpt-control-api-v0.2.3/` |
| iris-step1 | 0.1.0 | 16 | `Plugin-Creator/iris-step1-v0.1.0/` |
| iris-controller | 0.7.4 | 38 | `Plugin-Creator/iris-controller-v0.7.4/` |
| **Total** |  | **72** | 6 separate plugin folders |

Verification limits from the existing index:
- Source inventory/read: previously recorded as successful.
- Plugin Creator current source contents compared with GitHub destination: **VERIFIED — 72/72 exact content matches across six plugins**.
- Byte-for-byte parity with official installation archives: **NOT RUN**.
- Installation/runtime tests: **NOT RUN**.
- Do not call these six folders complete install packages unless manifests, required files, archive layout, and install/runtime behavior are separately verified.

## 6. Phase gates and order

| Gate | Work | Exit evidence |
|---|---|---|
| G0-01 | Repository identity and exact refs | Identity records with live branch/HEAD evidence |
| G0-02 | Complete file inventory | Every in-scope path accounted for; counts and exclusions stated |
| G0-03 | Architecture, symbols and dependencies | Evidence-backed maps with source paths |
| G0-04 | API and integration boundaries | Endpoint/contract register tied to exact refs |
| G0-05 | Read/write paths and data ownership | Persistence and mutation map; no runtime claims from code reading |
| G0-06 | Security, identity and ownership | Findings and limitations with evidence |
| G0-07 | Cross-system mapping register | EXACT / SEMANTIC CANDIDATE / CONFLICT / NO EQUIVALENT / UNKNOWN |
| G0-08 | Document consistency | Contradiction and documentation-gap register |
| G0-09 | Test-to-source and CI mapping | Results tied to exact commit SHA and run/test IDs |
| G0-10 | Runtime/integration verification | NOT RUN until separately authorized and actually executed |
| G0-11 | Archive provenance | Original archives, exact paths, TAR listing and SHA-256; comparison only to a trusted reference |
| Phase 1 | Implementation | Requires separate explicit authorization |

Current checkpoint progress: G0-07 Mapping Register is IN PROGRESS; G0-08 Document Consistency has initial findings recorded and remains IN PROGRESS. NEXUS/IRIS path inventories are recorded, but the content-level full audit inventory is incomplete. IRIS v0.6.5 snapshot: 21/21 files exact content match; six Plugin Creator snapshots: 72/72 exact content match. Runtime/tests/failure-injection remain NOT RUN. Baseline remains UNKNOWN / NOT SELECTED.

## 7. Immediate next actions

1. Read back this structure and record the resulting commit/blob identity.
2. Reconcile the actual current tree against Section 3; label existing, planned, duplicate, and misplaced items without deleting or moving them.
3. Revalidate the six Plugin Creator releases and compare their file lists with the existing snapshots; do not overwrite provenance.
4. Create a per-source repository register before collecting additional source files.
5. Gather source evidence into the matching project group only after its exact source ref is recorded.
6. Keep the Control API / shared central database out of full migration; document only the central/reference information until separately authorized.
7. Continue G0-07 Mapping Register and G0-08 Document Consistency using existing checkpoint NIR-P0-004. Do not create a new checkpoint.

## 8. Change log

- 2026-10-15: Reconciled the target organization from the recovered user instruction and existing repository records. This document defines the intended structure; planned folders are not claimed to exist until checked.
- Structure directories and README indexes were created and read back; source-tree inventories were added for NEXUS (52 entries), IRIS (107 entries), and the blocked LoopController candidate (1 entry). Six Plugin Creator source snapshots were compared file-by-file against the current Plugin Creator contents: 72/72 matched. Official archive parity and runtime/installability remain NOT RUN.
- No baseline selected; no source code changed; no full database migrated; no integration or deployment performed.
