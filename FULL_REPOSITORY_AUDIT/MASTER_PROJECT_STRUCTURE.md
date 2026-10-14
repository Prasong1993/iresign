# MASTER PROJECT STRUCTURE — NEXUS-Core / iresign

**Repository:** https://github.com/Prasong1993/iresign  
**Branch:** `master`  
**Control checkpoint:** TickTick task `6acfd06b8f0876e81c5f89fd` — `NIR-P0-004 — Checkpoint: Provenance Gap Closure & Phase 0 Evidence Consolidation`  
**Parent checkpoint:** `NIR-P0-003`  
**Phase:** 0 — Discovery & Evidence Verification  
**Mode:** READ-ONLY  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Execution:** PENDING  
**Structure status:** PROPOSED DOCUMENTATION MAP; not a claim that all folders/files exist.

## 1. Governing rules

1. Use the latest available checkpoint as the task handoff; revalidate repository state and target SHAs before relying on historical observations.
2. Preserve original evidence. Add new observations rather than silently rewriting or replacing old evidence.
3. Track `PLANNED`, `DISPATCHED`, `EXECUTED`, and `VERIFIED` separately.
4. Use `VERIFIED`, `PARTIAL`, `UNKNOWN`, `BLOCKED`, `NOT RUN`, and `IN PROGRESS` accurately.
5. Do not claim completeness while any in-scope file or required evidence remains unreviewed.
6. Phase 1 is not authorized. Repository reorganization, plugin/storage modification, baseline selection, deployments, production/database changes, dependency installation, penetration testing, and failure injection are not authorized by the checkpoint.
7. This structure is a documentation proposal. It does not select a source of truth, approve a baseline, or authorize implementation.

## 2. Proposed master directory map

```text
iresign/
├── FULL_REPOSITORY_AUDIT/
│   ├── AUDIT_SCOPE.md                         [existing; verify current content before changes]
│   ├── MASTER_CHECKPOINT.md                   [existing; preserve historical checkpoint]
│   ├── MASTER_CHECKLIST.md                    [existing; phase gate checklist]
│   ├── EVIDENCE_REGISTER.md                   [existing; append-only evidence log]
│   ├── MASTER_PROJECT_STRUCTURE.md            [this document]
│   ├── 00_G0-Intake-and-Identity/
│   │   ├── REPOSITORY_IDENTITY.md             [planned]
│   │   └── ACCESS_AND_LIMITATIONS.md          [planned]
│   ├── 01_G0-07-Mapping-Register/
│   │   ├── MAPPING_REGISTER.md                [next checkpoint action]
│   │   └── FIELD_LEVEL_INVENTORY.md           [planned; partial draft must be reconciled]
│   ├── 02_G0-08-Document-Consistency/
│   │   ├── DOCUMENT_CONSISTENCY_REVIEW.md     [next checkpoint action]
│   │   └── DOCUMENTATION_GAPS.md              [planned]
│   ├── 03_File-Inventory/
│   │   └── FULL_FILE_INVENTORY.md             [planned; not complete]
│   ├── 04_Architecture-and-Dependencies/
│   │   ├── ARCHITECTURE_AND_DATA_FLOW.md      [planned]
│   │   ├── SYMBOL_DEPENDENCY_MAP.md           [planned]
│   │   └── API_AND_INTEGRATION_REGISTER.md    [planned]
│   ├── 05_Read-Write-and-Data/
│   │   └── READ_WRITE_PATH_REGISTER.md        [planned; coverage partial]
│   ├── 06_Security-and-Identity/
│   │   └── SECURITY_FINDINGS.md               [planned; review incomplete]
│   ├── 07_Tests-and-CI/
│   │   ├── TEST_TO_SOURCE_MAPPING.md          [planned; NOT RUN]
│   │   └── CI_EVIDENCE_REGISTER.md            [planned; target-SHA pass unknown]
│   ├── 08_NEXUS-IRIS-Mapping/
│   │   ├── CONSOLIDATION_READINESS.md         [planned; no merge authorized]
│   │   └── OWNERSHIP_AND_IDENTITY_CONFLICTS.md [planned]
│   ├── 09_Website-Readiness/
│   │   └── WEBSITE_READINESS_ASSESSMENT.md    [planned; assessment only]
│   ├── 90_Blacklist-and-Change-Control/
│   │   ├── BLACKLIST_AND_PROHIBITIONS.md      [planned; sourced from checkpoint]
│   │   └── AUTHORIZATION_REGISTER.md          [planned]
│   └── 99_Archive-and-Superseded-Evidence/
│       └── README.md                          [planned; never delete source evidence]
└── PLUGIN_INSTALLATION_ARTIFACTS/
    └── Plugin-Creator/
        ├── INDEX.md                           [existing; six private plugin snapshots]
        ├── evidence-workflow-guard-v0.1.0/     [existing snapshot]
        ├── nexus-project-control-v0.1.1/       [existing snapshot]
        ├── assistant-error-guard-v0.2.0/       [existing snapshot]
        ├── chatgpt-control-api-v0.2.3/         [existing snapshot]
        ├── iris-step1-v0.1.0/                  [existing snapshot]
        └── iris-controller-v0.7.4/             [existing snapshot]
```

**Directory rule:** the tree above is a target information architecture, not a verified listing of current GitHub contents. Create only the next approved documentation deliverable; do not bulk-create empty structure or move existing artifacts as part of Phase 0.

## 3. Checkpoint-driven phase gates

| Gate | Required work | Current status from checkpoint | Exit evidence |
|---|---|---|---|
| G0-01 Repository identity | Revalidate repo, branch, HEAD, refs, tags/releases and limits | Historical observations exist; live revalidation required | Identity record tied to exact ref |
| G0-02 Full inventory | Enumerate and classify every in-scope path | NOT COMPLETE | Complete path inventory and counts |
| G0-03 Architecture | Entry points, symbols, dependencies, data flow | IN PROGRESS / incomplete | Evidence-backed symbol/dependency map |
| G0-04 API and integrations | Routes, external calls, MCP and API boundaries | Incomplete | Integration register with path-level evidence |
| G0-05 Read/write paths | Persistence and all read/write operations | PARTIAL — NOT FULLY VERIFIED | Path register and test links |
| G0-06 Security/identity | Auth, permissions, secrets handling, trust boundaries | NOT COMPLETE | Findings with severity, evidence, limitations |
| G0-07 Mapping Register | Map fields/records across candidate systems | NEXT; READ-ONLY | EXACT / SEMANTIC CANDIDATE / CONFLICT / NO EQUIVALENT / UNKNOWN |
| G0-08 Document Consistency | Compare documents against each other and source | NOT STARTED | Conflict/gap register with evidence |
| G0-09 Tests and CI | Map tests and CI results to exact source SHAs | NOT RUN / UNKNOWN | Test-to-source and CI evidence |
| G0-10 Runtime | Runtime verification | NOT RUN | Reproducible execution evidence; requires separate authorization |
| G0-11 Archive provenance | Receive and inspect two original .tar.gz archives | WAITING FOR ARCHIVES | Exact path/name, TAR listing, SHA-256, trusted-reference comparison if available |
| Phase 1 | Any implementation or modification | NOT AUTHORIZED | Separate explicit approval required |

## 4. Blacklist / prohibited actions

The checkpoint explicitly establishes these prohibitions. They are recorded here as project controls, not as a claim that a separate TickTick task named “Blacklist” was found.

- **Do not select or declare a baseline/source of truth.** Current state: UNKNOWN / NOT SELECTED; not authorized.
- **Do not modify or reorganize repositories, plugin releases, or storage.** Read-only evidence collection only.
- **Do not start Phase 1 or implementation.** Not authorized.
- **Do not merge NEXUS and IRIS or consolidate source code.**
- **Do not deploy or alter production/database state.**
- **Do not install dependencies or run potentially mutating code.**
- **Do not run penetration testing or failure injection.**
- **Do not mark tests/runtime as passed without direct evidence tied to the exact target revision.**
- **Do not treat REST/MCP endpoint availability as proof of ChatGPT integration.**
- **Do not treat source review, a test file, or historical CI as proof that tests passed on the target SHA.**
- **Do not select `Prasong1993/LoopController` as a baseline.** Checkpoint marks this candidate `BLOCKED — IDENTITY MISMATCH`.
- **Do not claim archive identity or parity until the two original archives are received and their paths, contents, and SHA-256 values are verified.**
- **Do not overwrite historical evidence to make it appear current.**
- **Do not claim the full repository inventory or mapping is complete while coverage is partial.**

## 5. Candidate source identity — preserve distinctions

| Candidate | Recorded reference | Checkpoint status | Rule |
|---|---|---|---|
| NEXUS | `Prasong1993/Loop-Controller`, recorded SHA `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | NOT LIVE REVALIDATED | Revalidate read-only; not automatically the baseline |
| IRIS | `Prasong1993/Prasong`, `IRIS/iris-controller-v0.6.5/`, recorded SHA `fee44e82a0926ca85833beff8a9462156117a2d9` | NOT LIVE REVALIDATED | Revalidate read-only; not automatically the baseline |
| Cloudflare candidate | `Prasong1993/LoopController`, recorded SHA `7c23df...c68d` in earlier handoff | BLOCKED — IDENTITY MISMATCH | Do not select as baseline |

## 6. Six private plugin snapshots — evidence boundary

The Plugin Creator archive index records six private USER-scope plugins and 72 source files. Snapshot folder presence, manifest/provenance readbacks, and index readback were previously recorded as verified. This does **not** mean all 72 files have been compared byte-for-byte with Plugin Creator or with official installation archives.

| Verification item | Status |
|---|---|
| Plugin Creator inventory: six private plugins | VERIFIED in prior recorded session; revalidate if used as current release truth |
| Snapshot directories and file counts | VERIFIED in prior recorded session |
| Index and provenance/manifest readbacks | VERIFIED in prior recorded session |
| Full content readback and source-to-snapshot comparison for every file | NOT YET VERIFIED |
| Byte-for-byte parity with official installation archives | NOT RUN |
| Installability/runtime tests | NOT RUN |

## 7. Next action sequence

1. Revalidate repository identity, branch, HEAD, and the relevant source paths without changing them.
2. Complete G0-07 Mapping Register using the five required mapping classifications.
3. Complete G0-08 Document Consistency review.
4. Continue the file inventory and symbol/dependency/read-write mapping; record every unknown or inaccessible path.
5. Await both original archives and record provenance and SHA-256 only after receipt.
6. Keep all prohibited actions blocked until separate explicit authorization.

## 8. Change log

- 2026-10-15: Structure drafted from the retrieved TickTick checkpoint `NIR-P0-004` and existing repository audit documents. No source code was changed, no baseline was selected, and no phase was marked complete by this document.
- Blacklist search limitation: TickTick search returned no matching task for the tested terms `blacklist`, `black list`, `ห้าม`, `NIR-P0-003`, `Project Workflow Guard`, `provenance`, `BLOCKED`, `NEXUS`, or `IRIS`. The prohibition list above is therefore grounded in the checkpoint text retrieved directly by task ID; any additional standalone blacklist record remains UNKNOWN and must be reconciled if located.
