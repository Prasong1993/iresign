---
name: project-workflow-guard
description: Use for recurring project work that requires evidence-first research, a timeline, controlled edits, deterministic checks where possible, iterative validation, and an audit-ready final report.
---

# Project Workflow Guard

## Purpose
Run a repeatable, evidence-first workflow for project tasks. Use this skill when the user asks to analyze, build, repair, review, or complete project work. This skill is an operating procedure, not a technical enforcement boundary: never claim it guarantees correctness or blocks tools unless an actual system enforces that behavior.

## Operating rules
- Use only the current task's relevant project context. Do not silently import old project data as current truth. Treat prior context as background only when relevant and label it accordingly.
- Inspect available capabilities, access, permissions, and constraints before acting. Do not claim a tool was used unless it was actually called.
- Prefer current official documentation and directly inspectable evidence. Cite or record source, version/date when relevant, and the claim it supports.
- Separate facts from assumptions. If evidence is missing, say `ไม่พบข้อมูล` or mark it `UNKNOWN`; never use unknowns as proof.
- Preserve originals. Do not delete, overwrite, publish, or push changes to external systems without authorization appropriate to the action.
- Avoid duplicate tool calls after a warning or failure unless there is a specific new diagnostic reason or changed input.
- Reading/searching may use multiple suitable tools or run in parallel when useful. For writes/edits, work in batches of 2–3 targets, then verify the batch before continuing.
- Do not report progress merely to narrate activity. Deliver the evidence-backed result and unresolved blockers when useful.

## Workflow

### 1. Interpret and scope
- Restate the desired outcome internally and identify acceptance criteria.
- Identify project boundaries, source-of-truth locations, protected originals, and excluded context.
- Inspect available tools/skills/connectors and their access before selecting them.
- If an essential detail is missing and cannot safely be inferred, ask one concise question. Otherwise proceed with clearly labeled assumptions only where harmless.

### 2. Gather evidence
- Research all components required for the task before coding or editing: official APIs/docs, versions, schemas/endpoints, authentication, dependencies, runtime/platform constraints, limits, setup/integration, examples, and credible proof of use where applicable.
- Prefer official sources; use independent corroboration when risk or uncertainty warrants it.
- Maintain a compact evidence ledger with claim, source, observation date/version, and status. Do not dump raw research unless requested.

### 3. Build the master timeline and plan
- Define ordered steps, dependencies, critical path, expected outputs, verification method, and gate criteria.
- For each step, specify what must be true before it starts and what evidence permits it to pass.
- Freeze unsupported architecture/schema/state assumptions as `UNKNOWN` until supported.
- Do not advance past a failed gate just to finish the plan.

### 4. Pre-action validation
Before every material write or external action, check:
- the target and intended change are unambiguous;
- permissions and authorization are sufficient;
- the action respects project scope and protected originals;
- dependencies, schema/API versions, and constraints are consistent;
- the action is not a duplicate of a completed action;
- budget, quota, and tool limits are acceptable where observable;
- rollback/recovery is understood when relevant.
If an important check fails, mark `BLOCKED` and explain why. Do not pretend a checklist itself technically enforces a block.

### 5. Execute in bounded batches
- Make changes only after the required gate passes.
- For writes/edits, limit each batch to 2–3 targets, unless the tool's atomic operation or user instruction requires a different safe unit.
- After each batch, inspect the actual resulting state and compare it with the intended diff/output before starting another batch.
- Keep planned, attempted, executed, and verified states distinct.
- If a change fails, stop the dependent sequence, diagnose using available evidence, update the plan, and retry only when there is a reasoned corrective action.

### 6. Validate iteratively
- Test the actual artifact or behavior using the strongest available relevant checks: schema validation, unit/integration tests, lint/type checks, API calls, runtime checks, or manual inspection.
- Compare outcomes against explicit acceptance criteria and original requirements.
- Resolve contradictions and actionable errors, then rerun affected checks. Do not claim “no errors” based only on a fixed number of retries or on tests that were not run.
- Distinguish tests passed, tests failed, tests not run, and behavior not independently verified.
- If a test cannot be run, mark `NOT RUN` and state the reason.

### 7. Evidence and status vocabulary
Use these labels consistently:
- `VERIFIED`: directly confirmed by an appropriate check or inspectable result.
- `RECOVERED`: restored or reconstructed from identifiable evidence; note provenance.
- `UNKNOWN`: not established by available evidence.
- `BLOCKED`: cannot safely or legitimately proceed due to a named blocker.
- `NOT RUN`: a required check/action was not performed.
- `IN_PROGRESS`: work has begun but acceptance criteria are not yet met.
- `FAILED`: a check or action was performed and failed.
- `PENDING_APPROVAL`: waiting for explicit authorization.
- `COMPLETED`: all required acceptance criteria have passed and the resulting state was verified.

Never label the whole task `COMPLETED` while a required acceptance check is failed, blocked, unknown, or not run. State precisely which parts are complete.

### 8. Final report
Provide a concise report with:
1. Outcome and overall status.
2. Work performed, with affected targets/artifacts.
3. Verification evidence and tests actually run.
4. Evidence sources and important versions/dates.
5. Remaining risks, unknowns, blockers, and `NOT RUN` checks.
6. Next required action, including approval if needed.

## Default checklist
- [ ] Scope and source of truth identified
- [ ] Tools/access/constraints checked
- [ ] Evidence gathered and claims traceable
- [ ] Master timeline and dependencies established
- [ ] Pre-action gates passed
- [ ] Changes executed in bounded batches
- [ ] Actual result inspected after each batch
- [ ] Acceptance checks run and failures addressed
- [ ] Final status matches the evidence
