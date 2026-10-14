# MASTER CHECKLIST — PROJECT REBASE: IRESIGN REPOSITORY

**Repository:** https://github.com/Prasong1993/iresign  
**Target branch:** `master`  
**Starting commit:** `8fd0bfae14cb6d0b191d4f718db93f44655e0a6e`  
**Mode:** READ-ONLY AUDIT  
**Overall status:** WAITING FOR REPOSITORY AUDIT

Checklist state reflects this new rebase only. Do not carry completion marks forward from former project reports. Recently added files are unverified until inspected at the current target commit.

Legend: `[ ] NOT RUN`, `[~] IN PROGRESS`, `[?] UNKNOWN/BLOCKED`, `[x] VERIFIED`.

## A. Repository identity and scope

- [x] Confirm repository URL and owner from GitHub metadata.
- [x] Confirm target branch `master` and starting commit SHA.
- [x] Confirm user's decision to use this repository as the new project base.
- [ ] Reconfirm HEAD before recording the final audit snapshot.
- [ ] Establish in-scope and out-of-scope paths for this rebase.
- [ ] Record accessible branch/tag/history/settings evidence and limitations.

## B. Full file and directory inventory

- [ ] Enumerate every path in the selected commit tree.
- [ ] Reconcile file and directory counts with the recursive tree.
- [ ] Classify each file by role, format, ownership, and relevance to the new project.
- [ ] Inspect newly added files from current content; do not inherit old verification status.
- [ ] Identify duplicates, stale project-status files, missing indexes, and unclassified paths.
- [ ] Link inventory rows to exact repository, commit SHA, path, and blob SHA.

## C. Source code and architecture

- [ ] Identify actual source-code files, entry points, modules, and responsibilities.
- [ ] Trace imports, dependency direction, shared components, and initialization paths.
- [ ] Inspect configuration loading, error handling, logging, background work, and external calls.
- [ ] Map architecture and data flow using source-path evidence.
- [ ] Separate source-level observations from runtime claims.

## D. Dependencies and configuration

- [ ] Inventory dependency manifests, lockfiles, version constraints, and package metadata.
- [ ] Identify environment variables and configuration sources without exposing secret values.
- [ ] Inspect build, packaging, installation, and deployment configuration where present.
- [ ] Identify unsupported, missing, duplicated, or conflicting dependencies.
- [ ] Do not install dependencies during this read-only audit.

## E. API, integrations, and data paths

- [ ] Inventory APIs, routes, request/response models, and public interfaces where present.
- [ ] Map external integrations and trust boundaries from source evidence.
- [ ] Identify database engines, schemas, migrations, and persistence code where present.
- [ ] Map read/write paths, transaction boundaries, validation, and failure behavior.
- [ ] Record any API/data-layer capability that is absent or cannot be verified.

## F. Tests and CI

- [ ] Inventory test files, frameworks, fixtures, and test-discovery configuration.
- [ ] Map tests to source modules and requirements.
- [ ] Inventory CI workflows, triggers, jobs, and build/test commands.
- [ ] Tie available CI results to exact commit SHAs and run URLs.
- [ ] Record tests not run and unavailable results explicitly.
- [ ] Do not infer a passing test from the existence of a test file or historical report.

## G. Security review

- [ ] Review authentication, authorization, secrets handling, input validation, and sensitive logging.
- [ ] Review network exposure, external requests, file/database permissions, and dependency risks where applicable.
- [ ] Record each finding with severity, path/symbol, evidence, impact, confidence, and required follow-up.
- [ ] No penetration test, live attack, or failure injection during this read-only audit.

## H. Requirements and gap assessment

- [ ] Map each user requirement to current repository evidence.
- [ ] Mark each requirement EXACT / PARTIAL / CONFLICT / NO EQUIVALENT / UNKNOWN.
- [ ] Identify reusable files and components based on direct inspection.
- [ ] Identify files/modules that need modification, replacement, or creation.
- [ ] Distinguish historical project records from current requirements.
- [ ] Produce a prioritized gap assessment and proposed target structure.

## I. Checkpoint and exit criteria

- [ ] Update this checkpoint only with evidence verified for the new rebase.
- [ ] Ensure Master Checkpoint and Master Checklist identify IRESIGN as the target.
- [ ] Confirm full in-scope inventory and architecture/data-flow assessment.
- [ ] Confirm test/CI evidence assessment and security findings.
- [ ] Confirm requirements gap assessment and source-linked evidence register.
- [ ] Keep overall status open until all required exit criteria have evidence.
- [ ] Obtain separate authorization before source or repository modifications.

## Change log

- 2026-10-15: Replaced the former cross-project checklist with a checklist for PROJECT REBASE — IRESIGN REPOSITORY. All audit items begin unverified except repository identity, branch, starting SHA, and the user's repository selection.
