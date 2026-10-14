# NEXUS / IRIS — PROJECT KNOWLEDGE & END-TO-END WORKFLOW

**Document Type:** Project Knowledge & Technical Workflow Specification  
**Version:** 1.0.0  
**Scope:** NEXUS, IRIS, repository audit, plugin installation artifacts, future integration readiness  
**Principle:** Evidence-First · Preserve Before Change · Read-Only Research · Controlled Integration  
**Status:** Reference specification; not a test report, approved baseline, or release certification.

## 1. Purpose and governing rules

This document consolidates the project context and the required end-to-end workflow. It is a guide for investigation, not proof that every listed activity has been completed.

Rules:
- Inspect existing systems before proposing replacements.
- Preserve source identity and historical evidence.
- Keep NEXUS and IRIS separate until repository identity, component ownership, contracts, data ownership, permissions, compatibility, and recovery behavior are established.
- A plan, source file, manifest, test definition, or CI configuration is not proof of runtime success.
- Keep new findings distinct from historical reports.
- Never expose secrets or copy credentials into audit artifacts.
- Do not select an official Source of Truth/Baseline without explicit approval.
- Do not change source code, deploy, install dependencies, modify production data, merge, or release without separate authorization.
- Do not mark work complete without evidence and a verification read-back.

## 2. Evidence and execution vocabulary

### Evidence status
- `VERIFIED`: evidence meets the stated criterion and can be traced to its source.
- `PARTIAL`: only part of the criterion has been verified.
- `UNKNOWN`: evidence is insufficient or unavailable.
- `BLOCKED`: a specific access, identity, or technical barrier prevents verification.
- `NOT RUN`: no evidence that the test/action was executed.
- `IN PROGRESS`: work is underway and exit criteria are not yet met.
- `NEEDS REVALIDATION`: historical evidence exists but must be checked against current source/commit.

### Action lifecycle
Track each action separately as `PLANNED`, `DISPATCHED`, `EXECUTED`, and `VERIFIED`. Do not conflate a tool call or write result with a verified final state.

### Evidence classes
Source, Test, CI, Runtime, Integration, and Operational evidence are separate classes. Do not substitute one class for another.

## 3. Project identity map

### NEXUS — Loop-Controller
- Repository: https://github.com/Prasong1993/Loop-Controller
- Historical target commit from prior project records: `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`
- Historical only until revalidated.
- Reported source areas include `nexus/api.py`, `nexus/core.py`, `nexus/capabilities.py`, `nexus/evidence.py`, `nexus/records.py`, `nexus/mcp_server.py`, `nexus/openai_adapter.py`, `nexus/openai_planner.py`, and `nexus/code_proposal.py`.
- The pinned tree reviewed for artifact discovery did not expose a clearly identified standalone plugin installation bundle. Do not label the repository itself an installable plugin package without inspecting its actual packaging contract.

### IRIS — Prasong repository
- Repository: https://github.com/Prasong1993/Prasong
- Historical target commit: `fee44e82a0926ca85833beff8a9462156117a2d9`
- Scope for the discovered installable plugin package: `IRIS/iris-controller-v0.6.5/`
- Historical only until revalidated.
- A plugin-shaped directory was found at this commit, including `plugin.json`, `.codex-plugin/plugin.json`, `skills/iris/SKILL.md`, `runtime/`, `tests/`, `.mcp.json`, and documentation. These files are copied into the audit repository as a provenance-labelled inspection snapshot, not as an official baseline or release approval.

### Audit workspace — iresign
- Repository: https://github.com/Prasong1993/iresign
- Default branch observed during setup: `master`
- Repository ID observed during setup: `1063265974`
- The four initial audit documents were created and read back successfully.
- Those document commits changed `master` HEAD; this was an authorized documentation change, not baseline selection.
- Current audit HEAD must be re-read before any later conclusion. The original HEAD is historical evidence only.

### Identity conflict guard
A similarly named repository, branch, folder, or plugin must not be assumed to be the same artifact. Keep `Prasong1993/Loop-Controller`, `Prasong1993/LoopController`, `Prasong1993/Prasong`, and `Prasong1993/iresign` as distinct identities unless evidence proves otherwise.

## 4. Repository and plugin artifact preservation

The audit repository contains a separate directory `PLUGIN_INSTALLATION_ARTIFACTS/`. It stores copies of text-based files from the specified IRIS source commit, preserving their relative paths. Each copied file is intended for inspection and must be traceable to its source repository, source path, source commit, and source blob SHA.

Rules for this directory:
- It is a snapshot for review, not the source of truth.
- Do not install or execute from this audit copy as part of the read-only audit.
- Do not add secrets, live tokens, API keys, database contents, or production credentials.
- Keep the original source repository unchanged.
- Record any missing, binary, or unsupported artifacts as gaps; do not silently replace them with reconstructed files.
- The snapshot's Git blob SHA in the audit repository will not necessarily equal the original source blob SHA; the manifest must record both separately.
- Any future refresh must create a new versioned snapshot or explicit approved change, not silently overwrite evidence.

## 5. NEXUS architecture review

Review the following reported areas against the exact target commit:
- API and request/response validation: routes, input models, controller calls, HTTP errors, authentication, authorization, and side effects.
- Core workflow/state: allowed transitions, persistence boundaries, error states, retries, and recovery.
- Capability registry: allowlists, operation checks, and whether every entry point enforces them.
- Evidence retrieval: URL validation, redirects, SSRF, timeout, response size, content parsing, quote matching, provenance, and failure recording.
- Operational records: schemas, creators/readers/mutators, access rules, integrity, and audit semantics.
- MCP: transport, tool discovery/registration, input schemas, dispatch, bearer gate, permissions, unknown-tool behavior, and side effects.
- OpenAI adapter/planner: client configuration, key handling, request/response schema, retries, timeout, error handling, output validation, and separation of planning from authorization/execution.
- Code proposal: proposal generation, provenance, review/approval, records, and whether a separate write/execution path exists.
- Dependencies and CI: manifest contents, Python matrix, commands, assertions, run identity, logs, and exact commit mapping.

These are audit questions, not pre-certified properties.

## 6. IRIS architecture review

Review the following reported areas against the exact target commit:
- `runtime/main.py`: app initialization, routes, configuration, middleware, authentication, network binding, startup/shutdown, and error handling.
- `runtime/controller.py`: work-unit lifecycle, step dispatch, transitions, checkpointing, verification, persistence, retry, and recovery.
- `runtime/database.py`: SQLite path, schema, initialization, connection lifecycle, transactions, CRUD, constraints, concurrency, and integrity.
- `runtime/model.py`: field requirements, enums, serialization, and compatibility across API, MCP, and database.
- `runtime/verify.py`: expected/actual semantics, PASS/FAIL rules, missing/invalid inputs, record creation, and tests.
- `runtime/mcp_server.py`: transport, registration, validation, dispatch, authentication/authorization, error mapping, database side effects, and audit logging.
- `tests/`: actual assertions, fixtures, mocks, cleanup, external dependencies, and what is or is not end-to-end.
- `runtime/requirements.txt` and `.github/workflows/iris-v065-test.yml`: exact requirements and commands, tied to a verified commit/run.

A source-level match between expected and actual values does not by itself prove a real operation executed successfully.

## 7. Cross-system boundaries and integration questions

Do not declare NEXUS the master controller or IRIS the execution engine until approved and evidence-backed. Determine:
1. Workflow state owner.
2. Work-unit and step-state owner.
3. Operational-record owner.
4. Evidence creation and verification owner.
5. OpenAI caller and model-output validator.
6. Tool approval and authorization owner.
7. Data-store write permissions.
8. Correlation identifiers and audit coverage.
9. Retry and idempotency semantics.
10. Failure isolation, compensation, and recovery ownership.

Evaluate REST, MCP, and data-exchange options separately. Shared SQLite is not an assumption. Every proposed contract must label existing behavior separately from proposed behavior.

## 8. Read/write path registers

### NEXUS reported paths — pending full trace
- RW-NX-01: API → validation → controller → persistence.
- RW-NX-02: evidence URL → HTTPS retrieval → quote verification → evidence record.
- RW-NX-03: OpenAI planner/code proposal → validation → record store.
- RW-NX-04: MCP tool call → dispatch/permission checks → controller/record store.

### IRIS reported paths — pending full trace
- RW-IR-01: REST API → controller → SQLite.
- RW-IR-02: MCP dispatch → controller.
- RW-IR-03: step failure → error/checkpoint/audit records.
- RW-IR-04: final verification → verification record → audit.

For each path record entry point, symbol, inputs/outputs, validation, permission checks, store, transaction boundaries, error paths, duplicate/retry behavior, tests, CI, runtime evidence, and limitations.

## 9. End-to-end phases and gates

### Phase 0 — Identity, preservation, and source-of-truth mapping
Record repository URL/ID, branch, HEAD SHA, tree, history, tags, relevant files, existing checkpoints, and permission scope. Preserve historical findings separately. Baseline selection remains pending explicit approval.

**Exit gate:** identity and scope are explicit; evidence gaps are listed; source artifacts are preserved; no unauthorized modifications occurred.

### Phase 1 — Full file inventory
Inventory every file in scope. Classify application source, API, controllers, adapters, MCP, evidence, records, persistence, configuration, security, tests, CI/CD, deployment, docs, dependencies, generated files, legacy/deprecated files, and plugin package files. Map path, blob SHA, size, symbols, dependencies, read/write paths, tests, status, and risks.

### Phase 2 — Architecture and data flow
Trace entry points, API, auth, OpenAI, planner, tool dispatch, MCP, evidence, records, database, errors, checkpoints, audit, and recovery. Separate source-confirmed, test-confirmed, CI-confirmed, runtime-confirmed, inferred, and unknown claims.

### Phase 3 — Dependencies and build requirements
Review manifests, version constraints, runtime/test dependencies, Python versions, environment variables, install/build commands, lockfiles, and supply-chain risk. Do not install dependencies or execute project code without approval.

### Phase 4 — Test and CI audit
Inventory tests; map tests to source; inspect fixtures, mocks, skips, assertions, discovery, CI workflow, matrix, job logs, and commit-to-run identity. A green run on another commit does not verify the target commit.

### Phase 5 — Security and trust boundaries
Review authentication, authorization, role/permission boundaries, secrets, bearer tokens, MCP, input validation, URL/network access, SSRF, data isolation, redaction, audit integrity, database access, and dependency risks. Identity mismatch blocks dependent integration decisions.

### Phase 6 — Existing integration contract extraction
Document current API and MCP contracts, schemas, status semantics, errors, timeouts, retries, idempotency, auth, audit, correlation IDs, and versioning. Mark each item existing, proposed, unknown, or conflicting.

### Phase 7 — Component connection map
Identify owners, interfaces, data flow, permission rules, state ownership, recovery, acceptance criteria, and tests. This is planning only and does not authorize code changes.

### Phase 8 — Target architecture proposal
Create context/component diagrams, data and state ownership maps, security boundaries, persistence strategy, error/recovery flow, test strategy, migration and rollback proposal. Keep NEXUS and IRIS separate unless an approved design says otherwise.

### Phase 9 — Controlled implementation (NOT AUTHORIZED by this document)
Only after separate explicit approval: create a work branch, record baseline, implement small diffs, add tests, inspect changes, run approved tests, check regressions, prepare migration/rollback, and request approval before merge/deploy.

### Phase 10 — Integrated verification (NOT RUN until implementation is authorized)
Verify component behavior, contracts, integration, persistence, security, failures, recovery, and end-to-end behavior. Record mocks vs real services, environment, command, timestamps, exit status, assertions, logs, and limitations.

### Phase 11 — Defect and regression handling
Record observed symptom, evidence, source path/symbol, root-cause hypothesis, impact, affected contracts/data, test plan, authorization, targeted tests, connected-component tests, regression/integration tests, and verified diff. Do not close on a single non-reproduction.

### Phase 12 — Deployment and operational readiness
Review environment configuration, secrets, network exposure, auth, DB paths/permissions, migration, logs/metrics, health checks, shutdown, backup, recovery, rollback, and runbook. Source review/CI is not production readiness.

### Phase 13 — Release readiness
Require exact release commit, required test/CI evidence, security gates, contract and persistence verification, runtime evidence, failure/recovery evidence, blocker disposition, migration/rollback, and release approval.

## 10. Test evidence record

Every test claim should include:
- Test ID and test file.
- Repository, branch, commit SHA, and source blob SHA where relevant.
- Environment and dependency versions.
- Command, start/end time, exit status.
- Assertions and result.
- Logs or run URL/ID.
- Mocks/stubs vs real external services.
- Known limitations and reviewer.

Test definitions alone are not execution evidence.

## 11. Security and preservation controls

- Never copy secrets to the audit repository.
- Treat installation manifests as untrusted configuration until reviewed.
- Do not execute copied plugin code during a read-only audit.
- Do not infer safety from a plugin manifest or README.
- Preserve original source commits and blob hashes.
- Keep evidence snapshots immutable by convention; add versioned snapshots for later captures.
- Record all audit-repository writes and verify each write by reading it back.
- Avoid storing live databases, private user data, credentials, or production data unless separately approved and safely redacted.

## 12. Required deliverables

1. Repository identity map.
2. Complete file inventory.
3. Dependency and package map.
4. Architecture and data-flow maps.
5. Read/write path register.
6. API and MCP contracts.
7. Data/state ownership map.
8. Security boundary map and findings.
9. Test inventory and test-to-source mapping.
10. CI evidence register.
11. Integration test results, when authorized and actually run.
12. Failure/recovery matrix.
13. Plugin installation artifact manifest with provenance.
14. Migration/rollback plan, if implementation is later authorized.
15. Runtime verification report, only when performed.
16. Operational runbook and release readiness assessment, when evidence supports them.
17. Master checkpoint and unresolved-gap list.

## 13. Current initial state

- Audit workspace: `Prasong1993/iresign`.
- Existing audit seed documents: created and read back.
- Initial NEXUS/IRIS historical findings: require revalidation against pinned commits.
- IRIS v0.6.5 plugin-shaped package: found in `Prasong1993/Prasong` at the historical target commit; snapshotting into a clearly labelled audit artifact folder is a copy, not an install/test.
- Dropbox `Plugin-Creator-Archive`: folder tree inspected; no files were returned from its visible subfolders during this check. Do not claim a Dropbox package was recovered.
- NEXUS standalone install package: not yet identified in the inspected pinned tree.
- Official Source of Truth/Baseline: `UNKNOWN / NOT SELECTED`.
- Runtime verification: `NOT RUN`.
- Full repository inventory: `NOT COMPLETE`.
- Source modifications in source repositories: not authorized.
- Tests: do not mark passed unless a specific test run and commit are verified.

## 14. Final principle

**Understand existing systems. Preserve evidence. Trace every data path. Verify every integration. Control every change. Test before claiming success.**

This document is the project knowledge and workflow specification. It is not a checkpoint result, an exhaustive audit, a runtime certification, or an authorization to modify source code.
