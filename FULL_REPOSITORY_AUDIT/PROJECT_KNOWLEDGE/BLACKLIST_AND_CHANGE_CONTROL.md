# NEXUS / IRIS — Blacklist and Change Control

**Source basis:** Current recorded checkpoint NIR-P0-004 and existing audit scope.  
**Status:** Checkpoint-derived prohibitions recorded; a separate standalone TickTick blacklist task was not found in attempted keyword searches. Reconcile if such a record is located.  
**Mode:** READ-ONLY.

## 1. Prohibited until separately authorized

- Do not select or declare an official baseline/source of truth.
- Do not modify application source or plugin release contents.
- Do not move, delete, rename or reorganize existing evidence/source files.
- Do not merge NEXUS and IRIS or consolidate their source code.
- Do not begin Phase 1 implementation.
- Do not deploy or change production state.
- Do not alter production/database data.
- Do not install dependencies or execute potentially mutating code.
- Do not run penetration testing or failure injection.
- Do not claim tests/runtime/CI passed without evidence tied to the exact target revision and environment.
- Do not treat source presence as proof that an API, OpenAI adapter or MCP client integration works.
- Do not treat a Code Proposal as proof that repository files were changed.
- Do not treat a test filename or test definition as proof of coverage or success.
- Do not select `Prasong1993/LoopController` as a baseline while the recorded identity mismatch remains unresolved.
- Do not claim archive identity/parity until original archives are received, identified and inspected.
- Do not overwrite historical observations to make them appear current.
- Do not claim inventory, mapping or audit completeness while in-scope paths remain unreviewed.

## 2. Permitted current work

Subject to tool access and active checkpoint:
- Read repository metadata, branches, commits, source, manifests, tests, CI configuration and documentation.
- Collect read-only evidence.
- Draft/create audit documentation only where authorized.
- Record unknowns, conflicts, limitations and next actions.
- Re-read written documentation to verify the write.

## 3. Approval boundary

Separate authorization is required before source-code changes, repository restructuring, plugin release changes, deployment, production/database modification, dependency installation, runtime execution with possible side effects, penetration testing, failure injection, baseline selection or integration implementation.

A documentation commit does not authorize any of those operations.

## 4. Change-control record

For each future authorized change, record approval source and timestamp; scope/exclusions; repository/ref/baseline; exact paths allowed to change; expected side effects; validation/test plan; rollback plan; actual changed paths and commit SHA; readback/verification result; remaining blockers.

## 5. Current status

- Phase 0: IN PROGRESS
- Mode: READ-ONLY
- Baseline: UNKNOWN / NOT SELECTED
- G0-07 Mapping Register: NEXT
- G0-08 Document Consistency: NOT STARTED
- Runtime/tests/failure injection: NOT RUN
- Phase 1: NOT AUTHORIZED
