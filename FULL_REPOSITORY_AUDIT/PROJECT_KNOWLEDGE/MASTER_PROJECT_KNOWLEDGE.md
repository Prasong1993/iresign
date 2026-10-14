# NEXUS / IRIS — PROJECT KNOWLEDGE & END-TO-END WORKFLOW

## Project context, architecture, evidence requirements and lifecycle

**Document Type:** Project Knowledge & Technical Workflow Specification  
**Project Scope:** NEXUS, IRIS, and preparation for potential controlled integration  
**Execution Principle:** Evidence-First, Read-Only Research, Controlled Integration  
**Current Phase:** Phase 0 — Discovery & Evidence Verification  
**Current Mode:** READ-ONLY  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Purpose:** Provide a stable project reference for understanding systems, preserving evidence, and following a controlled sequence from discovery to release readiness.

> **Evidence boundary:** Component names and behaviors below are based in part on earlier source-review notes. They are not fresh verification of current repository HEADs, complete source trees, successful tests, runtime behavior or production readiness.

---

# PART I — PROJECT OVERVIEW

## 1. Main objective

Understand and organize the control-system landscape around NEXUS and IRIS before deciding whether to reuse, connect, replace or consolidate any component. Avoid rebuilding existing capabilities before their actual implementation, contracts, data ownership and operational behavior are known.

Scope includes:
1. Repositories and source code
2. Application entry points and APIs
3. Workflow controllers and state management
4. OpenAI integration
5. MCP servers and tool dispatch
6. Evidence collection and verification
7. Operational records and audit trails
8. Databases and persistence
9. Authentication and authorization
10. Dependency management
11. Automated tests and CI
12. Data flow and read/write paths
13. Error handling and recovery
14. Integration testing
15. Security verification
16. Deployment readiness and operational reliability

## 2. Governing design principles

### 2.1 Evidence-first

Technical conclusions should link to repository and commit SHA, source path and symbol, configuration, test case/result, CI run/log, API request/response, database observation, runtime observation or error/recovery evidence.

A function name does not prove behavior. A test file does not prove that a test passed. A CI result does not prove deployment correctness. A matching quote does not prove source authority or that the source supports every conclusion.

### 2.2 Preserve before change

Preserve source files, Git history, configuration, dependency manifests, tests, CI workflows and control documents before considering changes. Do not overwrite original evidence or silently transform historical findings into current findings.

### 2.3 Separate before integration

Review NEXUS and IRIS independently. Similar use of Python, FastAPI, SQLite or MCP does not establish compatible schemas, ownership, permission boundaries or failure semantics.

### 2.4 Plan is not execution

Architecture documents, plans, proposed contracts and test matrices describe intended work; they are not evidence that code was written, integration works, tests passed or deployment is ready.

### 2.5 AI proposes; authorization controls execution

Model output is a proposal until validated against deterministic control rules and explicit authorization. A planner or code-proposal module must not be assumed to have permission to execute changes.

## 3. Evidence and status vocabulary

- **VERIFIED** — directly supported by evidence that satisfies stated acceptance criteria.
- **REPORTED** — present in an earlier report/checkpoint but not freshly confirmed.
- **INFERRED** — interpretation, not direct observation.
- **PARTIAL** — some coverage exists but full acceptance criteria are unmet.
- **UNKNOWN** — evidence is insufficient or unavailable.
- **BLOCKED** — an identified constraint prevents the next step.
- **NOT RUN** — no evidence the operation/test was executed.
- **IN PROGRESS** — work started but exit criteria are unmet.

Track lifecycle separately: **PLANNED → DISPATCHED → EXECUTED → VERIFIED**. A successful write/API response is not the same as content readback verification.

---

# PART II — NEXUS

## 4. Repository identity

**System:** NEXUS — Loop-Controller  
**Repository:** https://github.com/Prasong1993/Loop-Controller  
**Recorded reference SHA:** `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`  
**Identity status:** REPORTED; live revalidation required.

This SHA is a historical reference, not a statement of current HEAD. Before treating source conclusions as current, revalidate repository URL, branch/ref, commit SHA, tree and in-scope paths.

## 5. Reported component map and review scope

The component names below are review targets from prior handoffs. Confirm their existence and content at the exact revalidated commit before asserting behavior.

### 5.1 `nexus/api.py` — REST API

Review route inventory, methods, request/response models, input validation, controller calls, HTTP error mapping, authentication dependencies, record retrieval, workflow mutations and side effects. Separate read-only routes from routes that change state or persist data.

### 5.2 `nexus/core.py` — Core logic and workflow

Review state models, allowed transitions, sequencing, execution gates, error/recovery states, persistence calls and links between state changes and operational records. A successful state write does not prove all associated operations completed.

### 5.3 `nexus/capabilities.py` — Capability registry

Review registered capabilities, tool allowlists, operation-name validation, permissions and links to controller/MCP dispatch. Inspect every reachable entry point; a registry does not prove all paths enforce it.

### 5.4 `nexus/evidence.py` — Evidence retrieval and quote verification

Review evidence references, retrieval, HTTP/network errors, quote matching, verification records, URL validation, redirects, SSRF exposure, timeouts, response size and log redaction. Quote matching alone does not establish source authority or conclusion validity.

### 5.5 `nexus/records.py` — Operational records

Review record schemas, creation/update/read/search, validation, persistence, integrity and error handling. For each record type, identify its meaning, creator, read/write permissions and what event it can substantiate.

### 5.6 `nexus/mcp_server.py` — MCP server and tools

Review transport, tool registration, input schemas, dispatch, bearer authentication, authorization, unknown-tool behavior, controller calls and error mapping. Reported existence of a bearer gate requires implementation review. Source presence is not client-connection evidence.

### 5.7 `nexus/openai_adapter.py` — OpenAI adapter

Review client initialization, API-key configuration, request construction, response parsing, timeouts, retries, error handling and secret redaction. Confirm the API surface from code rather than inferring from filenames.

### 5.8 `nexus/openai_planner.py` — Planning

Review input context, instructions, output schema, response validation, model errors and connection to workflow state. Treat model output as a proposal until validated and authorized.

### 5.9 `nexus/code_proposal.py` — Code proposal

Review proposal schema, source context, validation, workflow links, record persistence, proposed change scope and approval requirements. A Code Proposal is not evidence that repository files were changed. Check for a separate execution/write path and its authorization controls.

## 6. NEXUS dependency and CI targets

Prior reports named `requirements.txt` and `.github/workflows/ci.yml`, with FastAPI, Uvicorn, Pydantic, HTTPX, MCP SDK, OpenAI SDK and PyYAML, plus a reported Python 3.11/3.12/3.13 matrix, compile checks, OpenAPI contract checks and unit tests.

**Status: REPORTED, not freshly verified.** Inspect the actual manifest and workflow at the selected SHA, then link CI run/job evidence to that exact commit. Do not claim current CI passes based on this historical description.

## 7. NEXUS reported read/write paths

- **RW-NX-01:** API → validation → controller → persistence. Map endpoint, auth, transaction, state mutation and failure behavior.
- **RW-NX-02:** evidence URL → network retrieval → quote verification → evidence record. Map URL checks, redirects, timeouts, response limits, SSRF and verification semantics.
- **RW-NX-03:** OpenAI planner/code proposal → response validation → record store. Map secret handling, malformed responses, persistence consistency and separation from execution.
- **RW-NX-04:** MCP tool call → dispatch/capability checks → controller/record store. Map allowlists, authorization, unknown tools, error mapping and side effects.

These are review hypotheses from prior reports, not proof that every route or failure path has been inspected.

---

# PART III — IRIS

## 8. Repository identity and scope

**System:** IRIS — `iris-controller-v0.6.5`  
**Repository:** https://github.com/Prasong1993/Prasong  
**Scope:** `IRIS/iris-controller-v0.6.5/`  
**Recorded reference SHA:** `fee44e82a0926ca85833beff8a9462156117a2d9`  
**Identity status:** REPORTED; live revalidation required.

The recorded SHA is a historical reference. Revalidate repository, ref, commit and exact scope before treating prior source review as current.

## 9. Reported component map and review scope

### 9.1 `runtime/main.py` — runtime/API entry point

Review initialization, routes, configuration/environment variables, dependency wiring, startup/shutdown, error handling, middleware, authentication and network binding. Source initialization does not prove runtime starts successfully.

### 9.2 `runtime/controller.py` — controller and step lifecycle

Review work-unit lifecycle, step dispatch, state transitions, error handling, checkpoint creation, verification flow, database interaction, retry and recovery. Inspect partial failure between related record writes.

### 9.3 `runtime/database.py` — SQLite persistence

Prior notes report SQLite and `IRIS_DB_PATH`. Verify initialization, schema/migrations, connection lifecycle, transactions, CRUD, constraints, concurrent access, recovery, database path and integrity. Inspect whether multi-record operations are transactional.

### 9.4 `runtime/model.py` — data models

Review required/optional fields, types, enums/statuses, serialization and compatibility across API, database and MCP. Consistent model declarations do not prove consistent use across all boundaries.

### 9.5 `runtime/verify.py` — verification logic

Prior notes report `verify.matches` comparing expected and actual values. Verify exact semantics, PASS/FAIL rules, missing/invalid values, record creation, errors and tests. Equality/matching alone does not prove execution occurred or evidence is trustworthy.

### 9.6 `runtime/mcp_server.py` — MCP server/dispatch

Review transport, tool registration/name resolution, input validation, controller dispatch, unknown tools, authentication/authorization, error mapping, database side effects and audit logging. Confirm whether REST and MCP share controller and policy enforcement.

### 9.7 `tests/test_mcp_e2e.py` — MCP tests

Review fixtures, mocks, assertions, cleanup, external dependencies and coverage of protocol, dispatch, controller, persistence and failure behavior. The filename `e2e` is not proof of full end-to-end coverage.

## 10. IRIS dependency and CI targets

Prior reports named `runtime/requirements.txt` with FastAPI, Uvicorn, HTTPX, MCP SDK and pytest, plus `.github/workflows/iris-v065-test.yml`, reportedly using Python 3.11 and `pytest -q`.

**Status: REPORTED, not freshly verified.** Confirm actual file content, dependency resolution, workflow run, logs, exit status and commit SHA before claiming a test pass.

## 11. IRIS reported read/write paths

- **RW-IR-01:** REST API → controller → SQLite.
- **RW-IR-02:** MCP dispatch → controller → possible persistence.
- **RW-IR-03:** step failure → error/checkpoint/audit records.
- **RW-IR-04:** final verification → verification record → audit record.

Inspect transaction boundaries, duplicate writes, partial failure, idempotency and consistency between step state, checkpoint, error, verification and audit data. These are targets to verify, not confirmed runtime paths.

---

# PART IV — NEXUS / IRIS RELATIONSHIP

## 12. Similar concepts do not establish compatibility

Reported shared concepts include REST APIs, controllers, MCP, persistence, records, errors and verification. Before integration, inspect component ownership, source of truth for each data category, API contracts, authentication/authorization, MCP contracts, schemas/migrations, error model, idempotency/retry, audit, dependency compatibility, failure isolation and recovery.

Do not declare NEXUS the master controller or IRIS the execution engine without an approved decision supported by evidence.

## 13. Ownership questions

- Which system owns workflow state?
- Which system owns work-unit and step state?
- Which system owns operational records and audit events?
- Which system retrieves and verifies evidence?
- Which system invokes OpenAI?
- Which component authorizes tool use?
- Which system may mutate each datastore?
- Which system is responsible for recovery after cross-system failure?

Duplicated state without explicit ownership creates divergence risk.

## 14. Integration alternatives to evaluate

### REST integration
Specify API version, schemas, auth, permissions, timeouts, retries, idempotency, error mapping, correlation IDs and audit.

### MCP integration
Specify client/server roles, transport, tool discovery/schemas, permissions, timeout/cancellation, error semantics, result validation and denied-tool behavior. Source presence does not prove a client connected.

### Shared database or data exchange
Do not assume both systems should share SQLite. Evaluate schema compatibility, ownership, transactions, concurrent access, migrations, failure isolation, retention, backup and recovery. Independent datastores with explicit contracts remain an option; no design is selected yet.

---

# PART V — END-TO-END PROJECT WORKFLOW

## 15. Stage 1: Context and source identity

Record repository URL, owner, branch/ref, commit SHA, scope, source files, manifests, workflows, relevant artifacts and permitted actions. Confirm inspected files belong to the intended source. Keep historical findings separate from new observations.

**Output:** source identity map tied to exact refs and access limitations.

## 16. Stage 2: Preserve and inventory

Preserve source/history; inventory all paths and classify source, API, controller, adapters, MCP, evidence, records, persistence, configuration, security, tests, CI/CD, deployment, docs, dependencies, generated and legacy files. For each file, record purpose, symbols, imports, read/write paths, tests, security relevance, risks and status.

**Output:** complete inventory or explicit missing/inaccessible/unclassified path list.

## 17. Stage 3: Architecture and data flow

Trace entry points, symbols, inputs/outputs, validation, permissions, stores, errors and tests for:
1. API request → validation → controller
2. Controller → state transition
3. Controller → persistence
4. Evidence reference → retrieval → quote verification
5. OpenAI input → adapter → response parsing
6. Planner output → validation → workflow
7. Code proposal → review/record
8. MCP request → tool dispatch → controller
9. Controller operation → operational record
10. Error → error record/checkpoint/audit
11. Verification input → result → persistence

Separate source inspection, test, CI and runtime evidence.

**Output:** architecture map, data-flow map and read/write register.

## 18. Stage 4: Dependency and build requirements

Review package constraints, Python requirements, runtime/test/optional dependencies, external services, environment variables, installation/build commands, version conflicts and dependency risks. Do not install or execute dependencies without authorization.

**Output:** dependency map and compatibility risk list.

## 19. Stage 5: Tests and CI

Inventory tests, map tests to source, inspect fixtures/mocks/assertions, inspect workflows/matrices/jobs, link each run to tested commit, and record failures/skips and coverage limits. A CI run on another commit does not validate the target SHA.

**Output:** test matrix, CI evidence register and verification gaps.

## 20. Stage 6: Security and identity

Review authn/authz, roles, secrets, bearer tokens, MCP boundaries, validation, URL/network access and SSRF, tenant isolation if relevant, datastore permissions, redaction, audit integrity and dependency vulnerabilities. Identity mismatch blocks dependent consolidation. Active penetration/failure testing requires separate approval.

**Output:** security findings, trust-boundary map and blockers.

## 21. Stage 7: Integration contracts

Specify names, schemas, types, required/optional fields, state semantics, errors, timeouts/retries, idempotency, authn/authz, audit, correlation IDs and versioning. Label each behavior existing/verified or proposed.

**Output:** contract package separating implementation from proposal.

## 22. Stage 8: Component connection planning

Define owner, interface, data flow, permissions, errors, data ownership, state synchronization, recovery, acceptance criteria and tests. Prefer reuse of verified existing capabilities where compatible.

**Output:** component connection map and integration plan. Planning is not permission to change code.

## 23. Stage 9: Target architecture proposal

Prepare system context, component, API/MCP, data/state ownership, persistence, security, failure/recovery, test, migration and rollback views. Explain each proposal and distinguish existing behavior from new design.

**Output:** target architecture proposal. This does not authorize repository changes.

## 24. Stage 10: Controlled implementation

Only after separate explicit approval: create task branch, record baseline/history, make small scoped changes, inspect diffs, add/update tests, run authorized checks, inspect regressions, prepare migration/rollback evidence, and obtain approval before merge/deploy.

**Current status: NOT AUTHORIZED.**

## 25. Stage 11: Integrated verification

After authorized implementation, verify component behavior, contracts, cross-component integration, persistence, security, failure, recovery and end-to-end paths. Record mocks versus real external services.

**Output:** integration results, failure matrix and end-to-end evidence tied to exact revisions.

## 26. Stage 12: Defect handling and regression

Record symptoms/evidence, map source/component/path, analyze root cause/blast radius, identify contract/data-model impact, define tests, obtain change approval, make only approved changes, run targeted/dependent/regression/integration tests, inspect diff and record actual results. Do not close a defect merely because it did not recur once.

## 27. Stage 13: Deployment and operations

Evaluate environment config, secrets, network exposure, auth, database paths/permissions, migration, logs/metrics, health checks, timeout/retry, graceful shutdown, backup/recovery, rollback and runbooks. Source review or CI is not production evidence.

## 28. Stage 14: Release readiness

Require exact release commit, required tests and CI tied to it, security gates, verified contracts, persistence integrity, runtime evidence, failure/recovery tests, resolved critical blockers, migration/rollback plans and release approval. If evidence is insufficient, do not declare readiness.

---

# PART VI — DATA, STATE, ERRORS AND RECOVERY

## 29. Data integrity and idempotency

For every write operation, inspect required fields, schema constraints, transactions, partial failures, duplicate writes, retries, idempotency, concurrency, state consistency and audit consistency. If an error record is written but checkpoint creation fails, determine whether the resulting state is observable and recoverable.

An audit log does not prove all operations are logged or that logs are tamper-resistant; inspect implementation and permissions.

## 30. Error model

Consider invalid input, authentication failure, authorization failure, unknown operation/tool, external API failure, timeout, database error, state conflict, verification failure and internal error. For each, document error code, API/MCP response, retry safety, state mutation, record writes, audit writes, recovery action and test evidence.

Never retry a side-effecting operation until retry safety and idempotency are understood.

## 31. OpenAI integration evidence

Separate client creation, API-key configuration, request, response, response validation, error handling, workflow integration, operational records, tool authorization and real API testing. SDK presence or an adapter file does not prove successful external calls. A model response does not replace business-rule validation.

## 32. MCP integration evidence

Separate these claims, each with its own evidence:
1. MCP server exists in source.
2. Server starts.
3. Client connects.
4. Client discovers tools.
5. Tool call executes.
6. Result is correct.
7. Side effects persist correctly.
8. Integration satisfies security requirements.

---

# PART VII — TEST STRATEGY

## 33. Test categories

- **Unit:** isolated function/module logic.
- **Contract:** API, MCP tool and data-model contracts.
- **Integration:** multiple components, persistence and external interfaces.
- **Security:** authentication, authorization, validation, secrets and trust boundaries.
- **Failure:** timeout, invalid data, unknown tool, database/external service failures.
- **Recovery:** state consistency and restart/recovery after failure.
- **End-to-end:** entry point through expected result and required persistence.
- **Regression:** protection of important existing behavior.

## 34. Test evidence fields

Record test ID, repository, commit SHA, environment, command, start/end time, exit status, assertions, result, logs, dependencies, mocks/stubs and known limitations. A claim that a test passed without reproducible result evidence is insufficient for a release gate.

---

# PART VIII — EVIDENCE AND VERIFICATION

## 35. Evidence types

- **Source evidence:** source, config and manifests.
- **Test evidence:** test behavior and actual result.
- **CI evidence:** workflow behavior in a specific run/commit.
- **Runtime evidence:** observation from a specified running environment.
- **Integration evidence:** communication/outcome between components/systems.
- **Operational evidence:** actual behavior, persistence and recovery in a specified environment.

Do not substitute one evidence type for another without stating limitations.

## 36. Required deliverables at full audit completion

1. Repository identity map
2. Complete file inventory
3. Dependency map
4. Architecture and data-flow maps
5. Read/write path register
6. API contract
7. MCP tool contract
8. Data ownership map
9. Security-boundary map
10. Test inventory
11. CI evidence register
12. Integration test results
13. Failure/recovery matrix
14. Migration and rollback plan
15. Runtime verification report
16. Operational runbook
17. Release-readiness assessment

These are target deliverables, not claims that they already exist or passed review.

---

# PART IX — CURRENT LIMITATIONS AND CHANGE CONTROL

## 37. Do not infer these outcomes

Until supported by current evidence, do not conclude that NEXUS and IRIS are one system, that a source of truth/baseline has been selected, that repositories remain at recorded SHAs, that all tests or CI pass, that runtime works, that OpenAI/MCP integration succeeds, that auth is safe in deployment, that recovery is correct, or that the systems are release/production ready.

## 38. Current control status

- Checkpoint: `NIR-P0-004 — Provenance Gap Closure & Phase 0 Evidence Consolidation`
- Task ID: `6acfd06b8f0876e81c5f89fd`
- Parent: `NIR-P0-003`
- Phase: 0 — Discovery & Evidence Verification
- Mode: READ-ONLY
- Baseline / Source of Truth: UNKNOWN / NOT SELECTED
- G0-07 Mapping Register: next documented action
- G0-08 Document Consistency: not started
- Runtime/tests/failure injection: NOT RUN
- Original archive provenance: waiting for two original `.tar.gz` archives, per prior checkpoint
- Phase 1: NOT AUTHORIZED
- Source changes, deployment, production/database changes, dependency installation, penetration testing, failure injection and baseline selection: NOT AUTHORIZED under current checkpoint

## 39. Future-chat handoff protocol

At the start of a continuation, state current scope, exact repository/commit, permitted actions, files actually inspected, evidence found, unknowns/blockers and next gate. If new information conflicts with this document, preserve the conflict and verify against an authorized source of truth rather than silently overwriting historical evidence.

## 40. Final principle

**Understand the existing systems. Preserve the evidence. Trace every data path. Verify every integration. Control every change. Test before claiming success.**

This specification is a knowledge and workflow reference, not a current checkpoint, fresh source audit, integration approval or certification of operational readiness.
