# NEXUS / IRIS — Integration Readiness Review

**Status:** PROPOSED EVALUATION FRAMEWORK; no integration approved  
**Current phase:** Phase 0 — READ-ONLY  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED

## 1. No assumed master/worker relationship

Do not state that NEXUS is the master controller and IRIS is the execution engine unless a decision is explicitly approved and supported by evidence. Similar technology stacks do not establish compatibility.

## 2. Ownership questions

| Domain | Required decision/evidence | Current status |
|---|---|---|
| Workflow state | Identify one authoritative owner and mutation rules | UNKNOWN |
| Work-unit/step state | Identify owner, lifecycle and state mapping | UNKNOWN |
| Operational records | Define schemas, creator, readers/writers and retention | UNKNOWN |
| Evidence | Define retrieval, verification and trust requirements | UNKNOWN |
| OpenAI calls | Identify caller, key ownership, policy and audit path | UNKNOWN |
| Tool authorization | Identify policy-enforcement point for REST and MCP | UNKNOWN |
| Persistence | Identify database ownership, transaction boundaries and migration | UNKNOWN |
| Recovery | Define responsibility after partial cross-system failure | UNKNOWN |

## 3. REST contract requirements

Specify API version, methods/routes, request/response schemas, required/optional fields, authentication, authorization, timeouts, retries, idempotency, error mapping, correlation IDs, audit and compatibility policy.

## 4. MCP contract requirements

Specify client/server roles, transport, discovery, tool names, input/output schemas, authorization, denied/unknown tool behavior, timeout/cancellation, errors, result validation, side effects and audit. Test client connectivity separately from server source presence.

## 5. Data exchange options

Evaluate rather than assume:
- REST contract-based exchange.
- MCP tool-based exchange.
- Independent databases with explicit data exchange.
- Shared persistence only if ownership, schemas, transactions, concurrency, migrations, isolation, retention and recovery are justified.

## 6. Required evidence before a design decision

- Revalidated source identity and full in-scope inventory.
- Source-backed API/MCP contracts.
- Data ownership and state ownership maps.
- Authentication and authorization review.
- Dependency/version compatibility.
- Error, retry and idempotency semantics.
- Read/write paths and transaction analysis.
- Test inventory and relevant CI evidence.
- Failure/recovery requirements and test design.
- Explicit decision record with alternatives and consequences.

## 7. Integration gate

Do not begin integration implementation until required evidence is available, unresolved blockers are documented, target architecture is approved, and separate explicit authorization is recorded. The current checkpoint does not authorize integration or source changes.
