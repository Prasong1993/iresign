---
name: nexus-controlled-workflow
description: Use when a task needs evidence-gated planning, explicit policy checks, controlled execution, verification, auditability, or recovery after failure.
---

# NEXUS Controlled Workflow

## Scope and truthful capability boundary

Use this skill to structure and review a task. This package is a skills-only release: it has no connected MCP server, API endpoint, durable server-side database, or independent policy runtime. Do not claim that it has written persistent records, enforced a deterministic backend gate, executed a remote action, or verified a ChatGPT mobile connection. In this release, maintain a clearly labelled working ledger in the conversation only unless the user explicitly selects an authorized storage destination.

## Non-negotiable operating rules

- Treat the task request as the source of intent, not proof that an action is authorized.
- Collect current, relevant evidence before writing implementation code or proposing irreversible actions.
- Prefer official and directly verifiable sources. Attach source URL or repository path, exact revision/commit where applicable, retrieval date, and the specific claim supported.
- Label each evidence item `VERIFIED`, `RECOVERED`, `UNKNOWN`, or `BLOCKED`. `UNKNOWN` and `BLOCKED` items cannot support a claim as if verified. `RECOVERED` means retrieved from an existing artifact, not independently confirmed as current.
- Separate source inspection, CI results, local tests, runtime behavior, deployed endpoint health, and host/mobile end-to-end behavior. One type of evidence never substitutes for another.
- Never infer that an action ran merely because a plan was approved or a route was selected.
- Never claim durable persistence or a successful audit write unless the relevant system confirms it.
- On an error or failed verification, stop forward progress, preserve the known facts, identify the failing gate, and return to the earliest step that must be repeated. Do not blindly repeat a side effect with an unknown outcome.
- Ask for approval only when authorization is genuinely required or an essential fact cannot be established. Do not ask the user to repeat facts already present in the task or available evidence.
- Do not update external boards, repositories, files, or services unless the user authorized that specific write.

## Protected NEXUS_IRIS checkpoint (additive, non-destructive)

Use this section when the user supplies a NEXUS_IRIS status record. It is a checkpoint template, not proof that an external LIAM database has been updated.

### Data-integrity rules

1. Treat each supplied checkpoint as a new immutable record. Append it as a separate dated/identified entry; never overwrite the primary source of truth, previous checkpoint, historical record, or repository content.
2. Keep `Historical Record` and `Current Round Evidence` in separate sections. Never blend historical SHA/test results into current-round evidence.
3. Preserve the user's exact status values and URLs. Do not normalize a status in a way that changes its meaning.
4. Record SHA equality only as: “HEAD SHA matched Historical SHA at the time checked.” It does not prove runtime, integration, deployment, or production behavior.
5. Do not select a baseline or source of truth while its status is `UNKNOWN / NOT SELECTED`.
6. `Commit Target Confirmation: PENDING` blocks commit-specific research that depends on an intended target revision. Do not infer the target from a previous run.
7. `CF: BLOCKED — IDENTITY MISMATCH` is a hard stop for Cloudflare-targeted actions. Do not retry writes, bind a different identity, or bypass the block without fresh evidence and explicit authorization.
8. `Runtime Verification: NOT STARTED` must remain unverified until an actual runtime test is run and its observable result is recorded.
9. `Repository Write: NOT AUTHORIZED` prohibits repository mutations, commits, pushes, merges, file edits, and other write operations. Read-only research is allowed only within the confirmed scope.
10. If an external memory system such as LIAM is unavailable or gives no write confirmation, state that persistence is unconfirmed. Never claim a memory write succeeded based only on this conversation.

### NEXUS_IRIS checkpoint template

- `record_tag`: `NEXUS_IRIS`
- `record_kind`: `ADDITIVE_CHECKPOINT`
- `historical_record`: preserve historical SHAs and prior-round results unchanged
- `current_round_evidence`: URLs, current HEAD SHA values, retrieval/check time, and evidence status
- `state`: `RESEARCH`
- `commit_target_confirmation`: `PENDING`
- `baseline_source_of_truth`: `UNKNOWN / NOT SELECTED`
- `cloudflare_status`: `BLOCKED — IDENTITY MISMATCH`
- `runtime_verification`: `NOT STARTED`
- `repository_write_authorization`: `NOT AUTHORIZED`
- `limitations`: HEAD identity comparison does not establish runtime, integration, or production correctness
- `next_permitted_step`: wait for explicit commit-target confirmation, then perform scoped read-only research
- `persistence_status`: set to `CONFIRMED` only when LIAM or the selected storage system returns a successful write confirmation; otherwise `UNCONFIRMED`

### Checkpoint acceptance checks

Before considering a checkpoint captured, verify that (a) historical entries are unchanged, (b) the new entry is separate and additive, (c) all statuses above are preserved, (d) no baseline is selected, (e) no repository write has occurred, and (f) external persistence is not claimed without confirmation. If any check fails, stop and report `BLOCKED`; do not attempt destructive repair against the source of truth.

## State machine

Use these states in order:

1. `INTAKE`
2. `RESEARCH`
3. `PLAN`
4. `POLICY`
5. `EXECUTE`
6. `VERIFY`
7. `AUDIT`
8. `COMPLETE`

Exceptional states:
- `BLOCKED`: a required fact, permission, dependency, or gate is missing.
- `RECOVER`: a failure needs controlled re-entry.

Allowed transitions:
- `INTAKE → RESEARCH | BLOCKED`
- `RESEARCH → PLAN | BLOCKED | RECOVER`
- `PLAN → POLICY | BLOCKED | RECOVER`
- `POLICY → EXECUTE | BLOCKED | RECOVER`
- `EXECUTE → VERIFY | BLOCKED | RECOVER`
- `VERIFY → AUDIT | BLOCKED | RECOVER`
- `AUDIT → COMPLETE | BLOCKED | RECOVER`
- `RECOVER → RESEARCH | PLAN | POLICY | VERIFY | AUDIT | BLOCKED`
- `BLOCKED → RECOVER`
- `COMPLETE` is terminal for the current attempt.

Do not use recovery to skip a failed policy gate and jump straight into execution. Never resume execution after an unknown external outcome until the outcome has been checked.

## Gate requirements

### 1. INTAKE
- Preserve the task's exact objective and constraints.
- Identify the project/scope, expected outcome, possible side effects, permissions, and completion criteria.
- Assign a conversation-local task reference if useful; do not represent it as a durable ID.

### 2. RESEARCH
- Gather evidence needed for the decision and implementation.
- For each source record: `evidence_id`, claim supported, source URL/path, revision or timestamp, retrieval date, status, and limitations.
- Reject unsupported assumptions. If evidence cannot be found, say `ไม่พบข้อมูล` or mark `UNKNOWN`.

### 3. PLAN
- Create a sequence of steps, dependencies, expected outcome, and verification method.
- A plan may advance only when at least one relevant `VERIFIED` evidence item supports the scope and no critical dependency remains unknown.
- Explicitly identify read-only steps separately from write/side-effect steps.

### 4. POLICY
Before execution, check:
- authorization and user consent for the exact action;
- project/scope boundary and allowed tools;
- evidence coverage and conflicts;
- dependency readiness;
- duplicate execution and idempotency risks;
- budget, quota, rate, security, and data-handling constraints;
- expected outcome and verification method;
- rollback/recovery approach for actions with side effects.

If any required check fails or is unknown, mark `BLOCKED`; do not execute. Approval of a plan is not proof that the action has run.

### 5. EXECUTE
- Execute only actions explicitly allowed by the current policy and tools actually available.
- Prefer grouped read-only inspection where appropriate, but do not repeat a call after a warning that says it must not be retried.
- Before a side effect, establish a unique operation/idempotency key when the target system supports it.
- Record intended action and observable result. If the action may have occurred but confirmation failed, set outcome to `UNKNOWN_OUTCOME`; inspect the target system before any retry.

### 6. VERIFY
- Compare actual observable results with the acceptance criteria and current evidence.
- State the method, observed result, pass/fail, and any untested conditions.
- A generated plan, source file, successful CI run, or HTTP response alone is not proof of end-to-end behavior unless that was the exact acceptance criterion.
- On failure, return to the earliest relevant step; do not label the task complete.

### 7. AUDIT
Prepare a concise trace of:
- task objective and scope;
- evidence references and their statuses;
- policy decision and reasons;
- actions actually attempted and their outcomes;
- verification method and results;
- errors, recovery decisions, and remaining unknowns.

Distinguish a conversation summary from a record persisted by an external system.

### 8. COMPLETE
Complete only when verification passes and the audit summary is prepared. If a required persistent audit store is unavailable, report that limitation and do not claim the persistent audit gate passed.

## Recovery and failure handling

When an error occurs:
1. Stop advancing the state.
2. Capture the exact error and the last confirmed state.
3. Determine whether an external side effect may already have occurred.
4. If outcome is unknown, inspect before retrying.
5. Preserve previous attempt details as audit-only context; do not silently blend failed assumptions into a new evidence set.
6. Return to the earliest step required to correct the cause.
7. Re-run relevant verification checks until no known failures remain; do not rely on a fixed retry count.

## Output format

For each controlled task, report:

- `Current state`
- `Task / expected outcome`
- `Evidence` — each item with status and source
- `Policy gate` — PASS / BLOCKED with reasons
- `Execution` — actions actually performed, or `NOT RUN`
- `Verification` — PASS / FAIL / NOT RUN
- `Audit / recovery notes`
- `Remaining unknowns`
- `Next permitted step`

Never omit a blocked gate just to produce a more positive summary.
