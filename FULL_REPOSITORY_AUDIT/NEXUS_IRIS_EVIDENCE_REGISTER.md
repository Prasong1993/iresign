# NEXUS / IRIS — EVIDENCE REGISTER

This register distinguishes current observations from historical reports. Add one row per verifiable claim. Do not change a status to VERIFIED without a traceable source.

| Evidence ID | Subject | Evidence / locator | Class | Status | Limitation / next check |
|---|---|---|---|---|---|
| AUD-001 | iresign identity | https://github.com/Prasong1993/iresign | Repository metadata | NEEDS REVALIDATION | Re-read live metadata and HEAD before next phase |
| AUD-002 | Initial audit seed docs | `FULL_REPOSITORY_AUDIT/AUDIT_SCOPE.md`, `MASTER_CHECKPOINT.md`, `MASTER_CHECKLIST.md`, `EVIDENCE_REGISTER.md` | Destination file read-back | VERIFIED (prior read-back) | Revalidate after subsequent commits |
| NX-001 | NEXUS target | https://github.com/Prasong1993/Loop-Controller at historical commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | Source tree | NEEDS REVALIDATION | Historical reference; not a live HEAD claim |
| NX-002 | NEXUS standalone plugin package | Pinned tree paths inspected | Source tree | UNKNOWN | No standalone plugin package identified in the paths returned; continue full inventory |
| IR-001 | IRIS target | https://github.com/Prasong1993/Prasong at historical commit `fee44e82a0926ca85833beff8a9462156117a2d9` | Source tree | NEEDS REVALIDATION | Historical reference; not a live HEAD claim |
| IR-002 | IRIS v0.6.5 plugin metadata | `IRIS/iris-controller-v0.6.5/plugin.json`, `.codex-plugin/plugin.json` | Source | VERIFIED (file presence at pinned tree) | Does not prove installability or successful runtime |
| IR-003 | IRIS skill | `IRIS/iris-controller-v0.6.5/skills/iris/SKILL.md` | Source | VERIFIED (file presence at pinned tree) | Skill content alone does not prove tools work |
| IR-004 | IRIS runtime and tests | `runtime/`, `tests/` under v0.6.5 | Source tree | VERIFIED (file presence at pinned tree) | Tests not run by this finding |
| DBX-001 | Plugin-Creator-Archive | Dropbox `/Plugin-Creator-Archive` and visible subfolders | Storage listing | UNKNOWN / NO FILES RETURNED | Listing showed empty visible subfolders; does not establish no other copies exist |
| TEST-001 | Test execution | No test run referenced here | Test | NOT RUN | Require authorization and reproducible run evidence |
| CI-001 | CI for target commit | Not yet mapped to exact run | CI | UNKNOWN | Retrieve runs/checks for exact SHA |
| RUN-001 | Runtime/integration | No runtime evidence in this register | Runtime/Integration | NOT RUN | Must not infer from source |
| BASE-001 | Official baseline | No authorized baseline selection | Governance | UNKNOWN / NOT SELECTED | Approval required |

## Snapshot records

Add one record per copied plugin artifact:
- Destination path
- Source repository and exact commit
- Source path and source blob SHA
- Destination blob SHA and destination commit SHA
- File size
- Read-back result
- Secret review status
- Notes and limitations

A copied file is not an independent validation of its contents; it is a preserved reference snapshot.
