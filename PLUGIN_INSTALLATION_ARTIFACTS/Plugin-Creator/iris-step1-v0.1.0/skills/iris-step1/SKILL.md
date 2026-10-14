---
name: iris-step1
description: Use when operating on the IRIS Step 1 project package, especially when validating projects, creating tasks, checking policy, verifying results, or auditing changes.
---

# IRIS Step 1

Treat this package as a controlled engineering unit. Never claim execution or PASS without inspectable evidence.

## Workflow
1. Perceive the requested work and current source.
2. Plan one coherent work unit.
3. Validate the real source and dependencies.
4. Execute only the allowed change/action.
5. Verify syntax, persistence, policy, and runtime behavior where applicable.
6. Audit evidence, source/version, errors, and remaining uncertainty.
7. Deliver the actual artifact or exact next action.

## Runtime package
- `runtime/main.py` — FastAPI entry point
- `runtime/database.py` — SQLite schema and seed loader
- `runtime/policy.py` — project/budget/phase checks
- `runtime/verify.py` — task verification and verification loop
- `runtime/task_queue.py` — task creation/queue logic
- `runtime/queue.py` — queue compatibility module
- `runtime/requirements.txt` — Python dependencies
- `runtime/seed/` — initial seed data

## Evidence rule
`EXECUTED != OUTPUT_PRESENT != OUTPUT_VALID != MATCHED != VERIFIED != PASSED`.
If runtime execution is unavailable, mark the result UNVERIFIED/BLOCKED rather than PASS.
