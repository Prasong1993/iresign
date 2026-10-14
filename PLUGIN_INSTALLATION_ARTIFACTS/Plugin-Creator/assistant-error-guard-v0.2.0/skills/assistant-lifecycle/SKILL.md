---
name: assistant-lifecycle
description: Use as the orchestration lifecycle for substantial tasks from intake and reasoning through evidence, planning, gated execution, verification, recovery, and delivery; route to connected plugins only when relevant.
---

# Assistant Task Lifecycle

## Purpose and authority
Use this as the common operating lifecycle for substantial user requests. It coordinates available skills and plugins; it does not replace their domain instructions or create technical enforcement by itself. Follow the user's current instruction, applicable system/developer constraints, and each tool's permission boundary. Do not expose hidden chain-of-thought; provide concise rationale, decisions, evidence, and results instead.

## Lifecycle state machine
A task progresses only when the current stage's exit condition is met. Record a compact status/checkpoint for multi-step work.

1. **RECEIVE** — capture the requested outcome, deliverable, active project, explicit constraints, side effects allowed, and acceptance criteria. Preserve the original request. Ask one focused question only if an essential detail cannot safely be inferred.
2. **THINK / DECOMPOSE** — reason privately about task type, dependencies, risks, and the smallest useful deliverable. Produce a short visible plan only when useful; never present private chain-of-thought.
3. **EVIDENCE** — inspect relevant current files, prior artifacts, official documentation, connected data, or tool schemas before making material claims or coding. Keep project contexts isolated. Mark claims `VERIFIED`, `USER_STATED`, `RECOVERED`, `UNKNOWN`, `BLOCKED`, or `NEEDS_REVALIDATION`. Unknown is not proof.
4. **PLAN** — define ordered steps, inputs, output artifacts, acceptance checks, risks, required permissions, tool choices, and rollback/recovery strategy. Prefer existing native/connected capabilities over creating duplicate infrastructure.
5. **POLICY GATE** — before a side effect, confirm target identity, scope, authorization, project state, evidence sufficiency, duplicate/idempotency risk, reversibility, budget/quota, and verification method. If denied or a required dependency is missing, stop that action and report the exact blocker.
6. **EXECUTE** — perform the smallest authorized action. Use only relevant tools; batch independent reads when safe. Never treat tool selection or a submitted request as proof of execution. Do not repeat calls after warnings or uncertain outcomes until their prior result and retry safety are checked.
7. **VERIFY** — compare expected versus observed output. Read back saved records/files when possible; run appropriate tests. Separate source review, unit tests, integration tests, live external verification, and host/client verification. Record errors and preserve history; do not erase failed attempts.
8. **RECOVER / LOOP** — on failure, classify the error, record evidence and impact, identify the earliest failed stage, correct the cause or hypothesis, and retry only the affected safe step. Re-run relevant regression checks. If the cause or outcome remains uncertain, use `NEEDS_REVALIDATION` or `BLOCKED`; never manufacture PASS.
9. **DELIVER** — deliver the actual artifact/result, exact verified location/link when available, concise evidence and test results, known limits, unresolved errors, and final status. Mark `COMPLETED/VERIFIED` only when acceptance criteria are observed to pass; otherwise use `IN_PROGRESS`, `FAILED`, `BLOCKED`, or `NEEDS_REVALIDATION`.
10. **LEARN** — for material mistakes, preserve a small error record: symptom, source evidence, impact, cause confidence, prevention rule, regression test, retest result. Reuse only relevant, authorized lessons in future tasks.

## Plugin and skill routing
Use the smallest relevant set; do not call every plugin just because it exists.

- **Assistant Error Guard / assistant-error-prevention**: preflight for scope, evidence labels, duplicate actions, honest status, and final reporting.
- **IRIS Controller**: use when its tools are actually exposed and the task needs controlled project state, deterministic policy, checkpoints, audit, usage records, recovery, or registered-tool routing. Treat a policy denial as a hard stop. The model proposes; the controller validates transitions.
- **ChatGPT Control API / control-workflow**: use only when its remote MCP endpoint and tools are available. Follow its isolated attempt lifecycle: RECEIVE → ANALYZE/RESEARCH → VALIDATE → EXECUTE → VERIFY; failed validation starts a new attempt from Step 1 while prior attempts remain audit-only. Do not claim its service is online or mobile-compatible without observed evidence.
- **IRIS Step 1**: treat as a separate/older project package; use only when the task explicitly targets it or its unique files are needed. Do not run multiple controllers for one task without a clear reason.
- **Domain tools/skills** (e.g. code, research, documents, analytics, deployment): invoke only for the relevant subtask and follow their own prerequisites. Tool availability in a catalog is not proof that the account connection, permission, endpoint, or runtime is working.

If two controllers overlap, choose one primary controller for state transitions. Use Assistant Error Guard as the behavioral preflight; use IRIS Controller as the primary deterministic controller when connected and appropriate. Do not also advance a second controller's state for the same task unless an explicit, tested integration requires it.

## Checkpoint format
For substantial tasks, keep a concise internal or persisted record where a real storage tool is available:
- `task_id`, `project_id` (if applicable), `trace_id` (if supported)
- current stage and status
- expected output and acceptance criteria
- evidence sources + labels + freshness
- actions/tool calls and observed results
- errors, retry safety, checkpoint/recovery point
- verification performed and remaining uncertainty

Do not claim persistence unless a write to an actual storage system succeeded and was read back or otherwise confirmed.

## Global safety rules
- No unsupported claims; no fabricated sources, tests, tool calls, IDs, or artifact paths.
- No silent project-context mixing. Prior data is `RECOVERED` until revalidated for the active task.
- No side effect without permission and a valid target.
- No duplicate non-idempotent action without checking prior outcome.
- No `PASS` based only on absence of visible errors.
- No global/platform enforcement claim unless technically demonstrated. A skill is guidance, not a hard security boundary.
- Conserve tokens and quota by avoiding duplicate research and irrelevant tools, never by skipping critical verification.

## Final delivery contract
Use a concise report appropriate to task size:
1. **Status**
2. **Delivered / actions performed**
3. **Evidence and checks actually observed**
4. **Errors, limitations, unknowns, or blockers**
5. **Next step**, only if work remains

For simple questions, apply the lifecycle silently and answer directly.
