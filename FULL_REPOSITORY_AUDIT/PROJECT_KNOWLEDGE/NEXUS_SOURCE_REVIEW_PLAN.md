# NEXUS — Source Review Plan

**Repository candidate:** https://github.com/Prasong1993/Loop-Controller  
**Recorded SHA:** `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`  
**Identity status:** REPORTED; revalidate live before relying on it  
**Mode:** READ-ONLY  
**Baseline:** UNKNOWN / NOT SELECTED

## Review contract

For each file, record exact repository/ref/SHA, path, symbols, direct imports/callers/callees, inputs/outputs, validation, permissions, read/write effects, error paths, related tests, CI evidence and unresolved questions. Do not treat this target list as proof the paths exist at the current commit.

## Component targets

| Target from prior handoff | Review focus | Key risk/questions |
|---|---|---|
| `nexus/api.py` | Routes, request/response, validation, controller calls | Which routes mutate state? Auth and error mapping? |
| `nexus/core.py` | State model, transitions, workflow gates | Are transitions guarded and writes atomic? |
| `nexus/capabilities.py` | Capability registry and allowlists | Do all entry points enforce it? |
| `nexus/evidence.py` | Retrieval and quote verification | URL validation, redirects, SSRF, timeout, response limits |
| `nexus/records.py` | Operational record schemas and persistence | Ownership, validation, duplicate writes, integrity |
| `nexus/mcp_server.py` | MCP transport, tools, dispatch, bearer gate | Client integration vs source presence; auth and side effects |
| `nexus/openai_adapter.py` | Client, key configuration, requests, responses | Secrets, retries, timeout, malformed response |
| `nexus/openai_planner.py` | Planning context and output schema | Is output validated before state/operation changes? |
| `nexus/code_proposal.py` | Code proposal construction and records | Is proposal separated from authorized execution? |
| `requirements.txt` | Dependency constraints | Exact versions, Python compatibility, runtime/test split |
| `.github/workflows/ci.yml` | CI matrix and commands | Actual run, job result and exact tested SHA |

## Reported read/write path hypotheses

- RW-NX-01: API → validation → controller → persistence.
- RW-NX-02: evidence URL → fetch → quote verification → record.
- RW-NX-03: OpenAI planner/code proposal → validation → record store.
- RW-NX-04: MCP tool → capability/authorization checks → controller/record store.

These are review targets, not verified exhaustive paths.

## Required output per component

- Identity: repository URL, ref, commit SHA, file path.
- Static findings: symbols, imports, calls, schemas and configuration.
- Data effects: read/write/side effects and transaction boundaries.
- Security: authz, secrets, input validation, network access.
- Tests: related test paths, exact command/result if executed and authorized.
- Evidence status: VERIFIED / REPORTED / PARTIAL / UNKNOWN / BLOCKED / NOT RUN.
- Follow-up: gap, dependency and next approved action.

## Gate

No source edits, dependency installs, runtime execution, deployment, baseline selection, penetration testing or failure injection are authorized by this review plan. Continue with read-only G0 evidence collection.
