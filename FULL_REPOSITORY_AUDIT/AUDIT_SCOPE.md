# AUDIT SCOPE — PROJECT REBASE: IRESIGN REPOSITORY

- **Project:** PROJECT REBASE — IRESIGN REPOSITORY
- **Target repository:** https://github.com/Prasong1993/iresign
- **Owner:** Prasong1993
- **Target branch:** `master`
- **Starting commit:** `8fd0bfae14cb6d0b191d4f718db93f44655e0a6e`
- **Mode:** READ-ONLY AUDIT
- **Overall status:** WAITING FOR REPOSITORY AUDIT
- **Repository/source-code modification:** NOT AUTHORIZED under the current project directive

## Objective

The user has selected `Prasong1993/iresign` as the base for a new project. Treat that choice as settled. The audit's purpose is to inspect the actual repository contents and determine how they map to the user's new project requirements—not to reconsider the repository choice or continue the former project's workflow.

## Handling of former project records

Former NEXUS / IRIS / Project Control API checkpoint statuses and old audit reports are not active status for this rebase. Their old completion marks must not be applied to the new project. Reports may remain in the repository as historical files, but they are not accepted as proof that a currently present or recently added file has been reviewed. Current verification must come from a new check tied to the current target commit, path, and evidence.

This scope reset changes project-control documents only. It does not assert that the repository source code has been audited, tested, or modified.

## In-scope audit work

1. Verify repository identity, target branch, and commit SHA.
2. Enumerate the full tree and classify every in-scope file.
3. Inspect source code, entry points, module responsibilities, dependencies, and configuration.
4. Assess API contracts, integrations, data flow, database usage, and read/write paths.
5. Inspect tests, CI workflows, and commit-bound CI results.
6. Review security and secrets handling from accessible source/configuration evidence.
7. Compare the actual repository with the user's current project requirements.
8. Identify reusable material, gaps, conflicts, and proposed structural changes.
9. Keep a fresh evidence register and update the Master Checkpoint and Master Checklist with read-back verification.

## Evidence requirements

Every finding must include, where applicable:
- Repository URL
- Exact commit SHA or ref
- Source path and symbol/line range
- Blob SHA or test/CI run URL
- Observation and verification method
- Evidence status
- Limitations and follow-up required

Historical observations must be labeled historical/RECOVERED. Do not mark a newly added file VERIFIED solely because an older report lists it or marks a previous state complete.

## Change control

- Read repository metadata, source, configuration, tree, history, and CI evidence.
- Update project-control documents only where specifically directed to replace the former project status.
- Do not modify application source, move/delete project files, commit/push/merge implementation changes, deploy, migrate databases, install dependencies, or run runtime/security tests during this audit.
- A separate explicit authorization is required before implementation or other repository changes.

## Exit criteria

- Full in-scope inventory tied to an exact commit.
- Source/architecture and data-flow assessment.
- Dependency/configuration and API/integration assessment.
- Database/read-write path assessment where relevant.
- Test-to-source and CI evidence assessment.
- Security findings.
- Requirements-to-repository gap assessment.
- New evidence register and verified checkpoint/checklist alignment.

## Change log

- 2026-10-15: Replaced former central-evidence-workspace scope with the user's current IRESIGN repository rebase. Former project status is no longer the active scope; historical reports are not current verification evidence.
