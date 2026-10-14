# IRIS — Source Review Plan

**Repository candidate:** https://github.com/Prasong1993/Prasong  
**Scope candidate:** `IRIS/iris-controller-v0.6.5/`  
**Recorded SHA:** `fee44e82a0926ca85833beff8a9462156117a2d9`  
**Identity status:** REPORTED; revalidate live before relying on it  
**Mode:** READ-ONLY  
**Baseline:** UNKNOWN / NOT SELECTED

## Review contract

Record exact repository/ref/SHA, path, symbols, data schemas, callers/callees, validation, permissions, read/write effects, transactions, error paths, tests, CI evidence and limitations. The file list below is historical and must be confirmed at the revalidated commit.

## Component targets

| Target from prior handoff | Review focus | Key risk/questions |
|---|---|---|
| `runtime/main.py` | App initialization, routes, config, middleware | Startup vs runtime proof; auth and network binding |
| `runtime/controller.py` | Work units, steps, state transitions, recovery | Partial failures, retry safety, checkpoint consistency |
| `runtime/database.py` | SQLite schema, connections, transactions, CRUD | `IRIS_DB_PATH`, concurrent access, migrations |
| `runtime/model.py` | Models, enums, serialization | API/database/MCP schema parity |
| `runtime/verify.py` | Expected/actual matching and result semantics | Does PASS mean only equality or verified execution? |
| `runtime/mcp_server.py` | Transport, registration, dispatch, auth | Same policy as REST? Side effects and audit? |
| `tests/test_mcp_e2e.py` | Fixtures, mocks, assertions, cleanup | Actual coverage vs filename implication |
| `runtime/requirements.txt` | Dependency versions/constraints | Compatibility and install reproducibility |
| `.github/workflows/iris-v065-test.yml` | Python setup and pytest command | Run result and exact commit mapping |

## Reported read/write path hypotheses

- RW-IR-01: REST API → controller → SQLite.
- RW-IR-02: MCP dispatch → controller → persistence.
- RW-IR-03: step failure → error/checkpoint/audit.
- RW-IR-04: final verification → verification record → audit.

These are review targets, not verified exhaustive runtime paths.

## Required output per component

- Exact identity and source provenance.
- Static behavior and data model.
- Read/write operations and transaction boundaries.
- Authentication/authorization and sensitive data handling.
- Error and recovery semantics.
- Tests/CI linked to exact SHA.
- Evidence classification and known limitations.

## Gate

This plan does not authorize source edits, dependency installation, runtime execution, production/database changes, deployment, baseline selection, penetration testing or failure injection. Keep work read-only until a separate approval changes the scope.
