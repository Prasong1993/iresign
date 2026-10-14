# NEXUS / IRIS — Evidence and Verification Model

## 1. Evidence classes

| Class | Can support | Does not prove by itself |
|---|---|---|
| Source | Declared logic, schemas, routes, configuration | Runtime behavior or successful external calls |
| Test definition | Intended checks and assertions | That tests were run or passed |
| Test result | Observed result for command/environment/SHA | Uncovered behavior or production behavior |
| CI | Workflow result for a particular run/commit | Other commits or deployment correctness |
| Runtime | Behavior observed in a specified environment | All environments or all input cases |
| Integration | Communication/outcome across identified components | Uncovered paths or long-term reliability |
| Operational | Persistence, failure/recovery, audit behavior in a stated setting | Unobserved incidents or every failure mode |

## 2. Evidence record fields

For each substantive claim, record where applicable: evidence ID; claim/requirement ID; repository URL and owner; branch/ref and commit SHA; file path and symbol/line range; evidence type and collection method; timestamp and environment; test/CI run ID, command and exit status; exact observation; limitations; related checkpoint and next action.

## 3. Status rules

- VERIFIED: evidence directly satisfies the stated acceptance criterion.
- REPORTED: inherited from an earlier report, not freshly checked.
- PARTIAL: some coverage exists but the full criterion is unmet.
- UNKNOWN: evidence insufficient or unavailable.
- BLOCKED: a constraint prevents the next step.
- NOT RUN: execution has not been evidenced.
- IN PROGRESS: started, not closed.

Execution lifecycle is separate: PLANNED, DISPATCHED, EXECUTED, VERIFIED. Never use one label to imply another.

## 4. Verification levels

1. Source presence
2. Static behavior review
3. Unit test
4. Contract test
5. Integration test
6. Runtime test
7. Failure/recovery test
8. Operational observation
9. Release gate

Each level needs its own criteria and evidence. Do not infer a higher level from a lower one.

## 5. Source snapshot rules

A snapshot directory and manifest prove only that an archive record/folder exists to the extent read back. Full parity requires reading every source file and comparing content/hash against the captured source. Installability requires the proper package artifact and installation validation. Runtime requires separate tests. Keep these claims distinct.

## 6. Closure rules

A finding may close only when acceptance criteria are explicit, evidence references the exact target revision/environment, results are reproducible or independently inspectable, limitations are documented, required related tests/CI/recovery checks have evidence, and reviewer decision is recorded.

If evidence is missing, retain PARTIAL/UNKNOWN/BLOCKED/NOT RUN rather than inferring success.
