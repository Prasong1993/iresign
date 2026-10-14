# NEXUS / IRIS — PHASE CHECKLIST

Status vocabulary: `VERIFIED`, `PARTIAL`, `UNKNOWN`, `BLOCKED`, `NOT RUN`, `IN PROGRESS`, `NEEDS REVALIDATION`.

No item is complete merely because it appears in this checklist. Mark complete only with evidence references.

## Phase 0 — Identity and preservation
- [ ] Re-read iresign repository ID, default branch, visibility, archived status, and live HEAD.
- [ ] Re-read NEXUS repository identity and target commit.
- [ ] Re-read IRIS repository identity and target commit.
- [ ] Compare target SHAs with current branches/tags/history; do not silently substitute HEAD.
- [ ] Record tree and file identities.
- [ ] Inventory prior checkpoints and label them historical.
- [ ] Record source of truth as UNKNOWN until approved.
- [ ] Record all limitations and identity conflicts.

## Phase 1 — Full file inventory
- [ ] Enumerate all files at the exact target commit for each source repository.
- [ ] Record path, type, size, blob SHA, role, and scope classification.
- [ ] Identify manifests, plugin metadata, skill files, runtime files, tests, CI, docs, and generated/legacy artifacts.
- [ ] Map symbols and imports for source files.
- [ ] Map source files to tests.
- [ ] Confirm inventory coverage against the complete tree.

## Phase 2 — Architecture and data flow
- [ ] Map application entry points and lifecycle.
- [ ] Map REST API request/response paths.
- [ ] Map controller/state transitions.
- [ ] Map OpenAI request/response and validation.
- [ ] Map MCP transport, tool discovery, dispatch, auth, and side effects.
- [ ] Map evidence retrieval and quote verification.
- [ ] Map record creation/read/update/search.
- [ ] Map database CRUD, transactions, and failure paths.
- [ ] Map error, checkpoint, audit, and recovery paths.
- [ ] Separate source, test, CI, runtime, and integration claims.

## Phase 3 — Dependency/build review
- [ ] Inspect all manifests and lockfiles.
- [ ] Record exact version constraints and Python versions.
- [ ] Identify environment variables and secret references without copying secret values.
- [ ] Identify build/test commands from authoritative files.
- [ ] Review external services and optional dependencies.
- [ ] Do not install dependencies without separate authorization.

## Phase 4 — Test/CI audit
- [ ] Enumerate tests and test IDs.
- [ ] Review assertions, fixtures, mocks, cleanup, skips, and test discovery.
- [ ] Map tests to source symbols and read/write paths.
- [ ] Inspect CI workflow triggers, matrix, commands, and artifacts.
- [ ] Find CI runs associated with exact target SHA.
- [ ] Record job results/logs and limitations.
- [ ] Do not execute tests until authorized if execution was not included in the current permission.

## Phase 5 — Security/trust boundaries
- [ ] Review authentication and authorization for every entry point.
- [ ] Review bearer-token handling and secret redaction.
- [ ] Review input validation and unknown-operation behavior.
- [ ] Review URL validation, redirects, SSRF, timeouts, and response size.
- [ ] Review DB access, path handling, permissions, and concurrency.
- [ ] Review MCP trust boundaries and tool allowlists.
- [ ] Review audit integrity and sensitive data in logs.
- [ ] Record blockers and unresolved threats.

## Phase 6 — Existing integration contracts
- [ ] Extract REST request/response schemas.
- [ ] Extract MCP tool names and input/output schemas.
- [ ] Record state and error semantics.
- [ ] Record timeout/retry/idempotency behavior.
- [ ] Record auth, permissions, audit and correlation IDs.
- [ ] Label each item existing, proposed, conflicting, or unknown.

## Phase 7 — Component connection map
- [ ] Identify ownership for workflow, work units, evidence, records, verification, and persistence.
- [ ] Identify interfaces and data exchanged.
- [ ] Map permissions and failure/recovery ownership.
- [ ] Define acceptance criteria without changing source.

## Phase 8 — Target architecture proposal
- [ ] Prepare context and component maps.
- [ ] Prepare data/state ownership map.
- [ ] Prepare persistence and security-boundary proposals.
- [ ] Prepare failure/recovery, migration, rollback, and test strategy.
- [ ] Keep existing behavior separate from proposed behavior.
- [ ] Do not treat design as implementation authorization.

## Phase 9 — Controlled implementation
- [ ] NOT AUTHORIZED by this document; require separate explicit approval.
- [ ] If approved, create a dedicated work branch and record baseline.
- [ ] Make small changes, review diffs, add tests, run authorized tests, and verify rollback.
- [ ] Obtain approval before merge/deploy.

## Phase 10 — Integrated verification
- [ ] NOT RUN until implementation is approved and executed.
- [ ] Component, contract, integration, persistence, security, failure, recovery, and E2E verification.
- [ ] Record mocks vs real services, environment, exact commit, commands, logs, and exit statuses.

## Phase 11 — Defect and regression
- [ ] Record symptom, source, evidence, root-cause hypothesis, impact, and affected paths.
- [ ] Obtain authorization before source changes.
- [ ] Verify targeted, connected-component, regression, and integration tests.
- [ ] Close only when evidence supports the exit criterion.

## Phase 12 — Deployment/operations
- [ ] Review environment, secrets, network exposure, database permissions, logging, metrics, health, shutdown, backup, recovery, rollback, and runbook.
- [ ] Do not claim production readiness from source review or CI alone.

## Phase 13 — Release readiness
- [ ] Exact release commit identified.
- [ ] Required tests and CI runs match release SHA.
- [ ] Security, contracts, persistence, runtime, failure and recovery gates verified.
- [ ] Critical blockers resolved or explicitly accepted by authorized owner.
- [ ] Migration/rollback and release approval recorded.

## Plugin artifact snapshot checklist
- [ ] Source repo, commit, path, and source blob SHA recorded.
- [ ] Relative paths preserved.
- [ ] Secret scan/review performed without exposing values.
- [ ] Every copied file read back from destination.
- [ ] Destination blob SHA and commit SHA recorded.
- [ ] Snapshot clearly marked as a review copy, not official baseline.
- [ ] Missing binaries/packages recorded as gaps, not fabricated.
