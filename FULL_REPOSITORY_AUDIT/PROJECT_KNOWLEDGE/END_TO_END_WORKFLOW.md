# NEXUS / IRIS — End-to-End Workflow Gates

**Current checkpoint:** NIR-P0-004 — Provenance Gap Closure & Phase 0 Evidence Consolidation  
**Task ID:** `6acfd06b8f0876e81c5f89fd`  
**Phase:** 0 — Discovery & Evidence Verification  
**Mode:** READ-ONLY  
**Phase 1:** NOT AUTHORIZED

## Gate sequence

| Gate | Work | Required output | Current state |
|---|---|---|---|
| G0-01 | Repository identity | URL, branch/ref, HEAD SHA, access limits | Historical evidence exists; live revalidation required |
| G0-02 | File inventory | Every in-scope path classified or listed as inaccessible | NOT COMPLETE |
| G0-03 | Architecture/data flow | Entry points, symbols, dependencies, data flow | PARTIAL / INCOMPLETE |
| G0-04 | API and integrations | Routes, schemas, external calls, MCP/API boundaries | INCOMPLETE |
| G0-05 | Read/write paths | Read/write register and side effects | PARTIAL |
| G0-06 | Security and identity | Trust boundaries, auth, secrets, blockers | INCOMPLETE |
| G0-07 | Mapping Register | EXACT / SEMANTIC CANDIDATE / CONFLICT / NO EQUIVALENT / UNKNOWN | NEXT |
| G0-08 | Document consistency | Conflicts/gaps across source and docs | NOT STARTED |
| G0-09 | Tests and CI | Test-to-source map and target-SHA CI evidence | NOT RUN / UNKNOWN |
| G0-10 | Runtime | Authorized runtime evidence | NOT RUN |
| G0-11 | Archive provenance | Inspect two original .tar.gz archives and SHA-256 | WAITING FOR ARCHIVES |
| Phase 1 | Implementation | Approved change set and test evidence | NOT AUTHORIZED |

## End-to-end work sequence

### Stage 1 — Context and source identity
Record repository URL, owner, branch/ref, commit SHA, scope, source files, manifests, workflows, artifacts and permitted actions. Confirm that inspected files belong to the intended source. Keep historical findings separate from new observations.

**Output:** source identity map tied to exact refs and access limitations.

### Stage 2 — Preserve and inventory
Preserve source/history; inventory all paths and classify source, API, controller, adapters, MCP, evidence, records, persistence, configuration, security, tests, CI/CD, deployment, docs, dependencies, generated and legacy files. For each file, record purpose, symbols, imports, read/write paths, tests, security relevance, risks and status.

**Output:** complete inventory or explicit missing/inaccessible/unclassified path list.

### Stage 3 — Architecture and data flow
Trace entry points, symbols, inputs/outputs, validation, permissions, stores, errors and tests for API→controller, controller→state, controller→persistence, evidence→retrieval→quote verification, OpenAI→adapter→response parsing, planner→validation→workflow, proposal→record, MCP→dispatch→controller, operations→records, error→checkpoint/audit, and verification→persistence.

**Output:** architecture map, data-flow map and read/write register.

### Stage 4 — Dependencies and build
Review package constraints, Python requirements, runtime/test/optional dependencies, external services, environment variables, installation/build commands, version conflicts and dependency risks. Do not install or execute dependencies without authorization.

**Output:** dependency map and compatibility risk list.

### Stage 5 — Tests and CI
Inventory tests, map tests to source, inspect fixtures/mocks/assertions, inspect workflows/matrices/jobs, link each run to tested commit, and record failures/skips and coverage limits. A CI run on another commit does not validate the target SHA.

**Output:** test matrix, CI evidence register and gaps.

### Stage 6 — Security and identity
Review authn/authz, roles, secrets, bearer tokens, MCP boundaries, validation, URL/network access and SSRF, tenant isolation if relevant, datastore permissions, redaction, audit integrity and dependency vulnerabilities. Identity mismatch blocks dependent consolidation. Active penetration/failure testing requires separate approval.

**Output:** security findings, trust-boundary map and blockers.

### Stage 7 — Integration contracts
Specify names, schemas, types, required/optional fields, state semantics, errors, timeouts/retries, idempotency, authn/authz, audit, correlation IDs and versioning. Label each behavior existing/verified or proposed.

**Output:** contract package separating implementation from proposal.

### Stage 8 — Component connection planning
Define owner, interface, data flow, permissions, errors, data ownership, state synchronization, recovery, acceptance criteria and tests. Prefer reuse of verified existing capabilities where compatible.

**Output:** component connection map and integration plan. Planning is not permission to change code.

### Stage 9 — Target architecture
Prepare system context, component, API/MCP, data/state ownership, persistence, security, failure/recovery, test, migration and rollback views. Explain each proposal and distinguish existing behavior from new design.

**Output:** target architecture proposal. This does not authorize repository changes.

### Stage 10 — Controlled implementation
Only after separate explicit approval: create task branch, record baseline/history, make small scoped changes, inspect diffs, add/update tests, run authorized checks, inspect regressions, prepare migration/rollback evidence, and obtain approval before merge/deploy.

**Current status:** NOT AUTHORIZED.

### Stage 11 — Integrated verification
After authorized implementation, verify component behavior, contracts, cross-component integration, persistence, security, failure, recovery and end-to-end paths. Record mocks versus real external services.

**Output:** integration results, failure matrix and end-to-end evidence tied to exact revisions.

### Stage 12 — Defect handling and regression
Record symptoms/evidence, map source/component/path, analyze root cause/blast radius, identify contract/data-model impact, define tests, obtain change approval, make only approved changes, run targeted/dependent/regression/integration tests, inspect diff and record actual results. Do not close a defect merely because it did not recur once.

### Stage 13 — Deployment and operations
Evaluate environment config, secrets, network exposure, auth, database paths/permissions, migration, logs/metrics, health checks, timeout/retry, graceful shutdown, backup/recovery, rollback and runbooks. Source review or CI is not production evidence.

### Stage 14 — Release readiness
Require exact release commit, required tests and CI tied to it, security gates, verified contracts, persistence integrity, runtime evidence, failure/recovery tests, resolved critical blockers, migration/rollback plans and release approval. If evidence is insufficient, do not declare readiness.

## Exit criteria

Phase 0 can only be described as complete when required gates have explicit evidence, unresolved paths/blockers are recorded, source identities are unambiguous, mapping/document consistency reviews are complete, and the authorized checkpoint owner accepts the package. Missing archives, inaccessible files or unverified runtime remain explicit gaps.
