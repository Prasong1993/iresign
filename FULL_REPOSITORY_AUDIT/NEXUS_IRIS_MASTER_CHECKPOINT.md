# NEXUS / IRIS — MASTER CHECKPOINT

**Checkpoint version:** 1.0.0  
**Workspace:** https://github.com/Prasong1993/iresign  
**Mode:** Evidence-first audit; read-only against source repositories  
**Baseline:** UNKNOWN / NOT SELECTED  
**Last update:** 2026-10-15

## Current state

| Workstream | Status | Evidence / constraint |
|---|---|---|
| iresign repository identity | NEEDS REVALIDATION | Re-read live repository metadata and HEAD before next audit decision |
| Initial audit seed docs | VERIFIED | Four documents created and read back in prior step |
| Project knowledge workflow spec | PLANNED | This checkpoint tracks new specification creation; verify file after write |
| NEXUS identity and source | NEEDS REVALIDATION | Historical commit: `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` |
| IRIS identity and source | NEEDS REVALIDATION | Historical commit: `fee44e82a0926ca85833beff8a9462156117a2d9` |
| IRIS v0.6.5 install-shaped source | PARTIAL | Manifest, skill, runtime, tests and docs discovered at historical commit; audit snapshot must be verified file-by-file |
| NEXUS install package | UNKNOWN | No standalone package identified from inspected pinned tree paths |
| Dropbox plugin archive | UNKNOWN / NOT FOUND IN LISTED SUBFOLDERS | Visible archive subfolders returned no files; this is not proof no other storage exists |
| Full file inventory | NOT COMPLETE | Do not claim complete until every in-scope file is inventoried |
| Test execution | NOT RUN | Reading tests is not running tests |
| CI pass for target commits | UNKNOWN | Must map runs to exact target SHA |
| Runtime/integration | NOT RUN | No runtime claim permitted |
| Security audit | NOT COMPLETE | Source review and runtime security evidence remain distinct |
| NEXUS/IRIS integration design approval | NOT AUTHORIZED | Keep systems separate pending evidence and approval |
| Source of Truth/Baseline selection | NOT AUTHORIZED | Do not select unilaterally |

## Actions recorded

- Created and read back the initial four audit seed documents under `FULL_REPOSITORY_AUDIT/`.
- Inspected the IRIS repository tree at the historical commit and found plugin manifests, skill, runtime, tests, and documentation paths.
- Inspected the NEXUS repository tree at the historical commit; a standalone plugin install package was not identified by the paths examined.
- Searched and listed the visible Dropbox `Plugin-Creator-Archive` structure; no package files were returned from its listed subfolders.
- Do not treat these actions as a complete audit or official baseline selection.

## Next controlled steps

1. Finish creating the project knowledge specification and evidence registers.
2. Snapshot the identified IRIS plugin package files into `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/`, preserving relative paths and source provenance.
3. Read back every created file and record audit-side commit/blob identifiers.
4. Re-read the live iresign HEAD and verify all artifact files.
5. Continue Phase 0 identity/history validation; do not advance to implementation.
6. Inventory NEXUS/IRIS sources and plugin package structure using exact commits, keeping historical findings labelled.
7. Ask for separate approval before any source modification, dependency installation, test execution with side effects, deployment, baseline selection, or integration implementation.

## Change control note

Adding project documents and a clearly labelled source snapshot to this audit repository creates commits on the destination branch. It does not alter the original NEXUS/IRIS source repositories and does not select an official source baseline. Each write must be verified by read-back.
