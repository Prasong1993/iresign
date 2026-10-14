# MASTER CHECKLIST — FULL REPOSITORY AUDIT

Legend: `[ ] NOT RUN`, `[~] IN PROGRESS`, `[?] UNKNOWN/BLOCKED`, `[x] VERIFIED`. A checked item requires recorded evidence; none is marked complete at initialization.

## Phase 0 — Repository Identity
- [~] Confirm repository URL, owner, visibility, default branch.
- [ ] Revalidate target branch and HEAD SHA.
- [ ] Enumerate branch refs and relevant commit history.
- [ ] Inspect tags and releases.
- [ ] Inspect submodules, Git LFS, external references, and repository settings where accessible.
- [ ] Record limits on working-tree and permission visibility.
- [ ] Preserve initial observations separately from revalidation.

## Phase 1 — Full File Inventory
- [ ] Enumerate all paths at the selected inspection commit.
- [ ] Classify every file into the required inventory categories.
- [ ] Record purpose, symbols, imports, read/write paths, tests, security relevance, risks, and verification status.
- [ ] Count total files and reviewed files by category.
- [ ] Identify unclassified and inaccessible files.
- [ ] Do not claim inventory completeness while any in-scope path is unreviewed.

## Phase 2 — Source Code and Architecture
- [ ] Identify entry points and module responsibilities.
- [ ] Map dependency direction and shared utilities.
- [ ] Inspect circular dependencies, duplicate logic, and potentially unused code.
- [ ] Review errors, logging, configuration, state transitions, async/background work, external calls, and resource lifecycle.
- [ ] Produce evidence-backed architecture and data-flow map.
- [ ] Keep runtime claims separate from source inspection.

## Phase 3 — API, Integration, and Data Flow
- [ ] Inventory HTTP methods/routes and request/response models.
- [ ] Inspect validation, auth, errors, timeouts, retries, rate limits, and versioning.
- [ ] Inventory OpenAI, MCP, external API, dispatch, registry/allowlist, and evidence integrations.
- [ ] Record inputs/outputs, auth method, data egress, failures, security implications, tests, and unknowns.

## Phase 4 — Database and Read/Write Paths
- [ ] Identify database engine, schemas/models, migrations, constraints, and indexes.
- [ ] Map CRUD, transaction boundaries, validation, concurrency, backup/recovery, audit records, retention, duplicate writes, and failure consistency.
- [ ] Build Read/Write Path Register with evidence and related tests.
- [ ] Do not assert data integrity without suitable evidence.

## Phase 5 — Security
- [ ] Review authentication, authorization, roles, tenant isolation, and secrets handling without exposing secret values.
- [ ] Review input validation, path traversal, SSRF, injection, deserialization, CORS/network exposure, TLS, and MCP trust boundaries.
- [ ] Review tool allowlists, sensitive logging, dependencies, audit integrity, and file/database permissions.
- [ ] Record finding ID, severity, affected path/symbol, evidence, impact, confidence, remediation, and verification required.
- [ ] No live attacks, penetration tests, or failure injection without separate authorization and suitable environment.

## Phase 6 — Tests and CI/CD
- [ ] Identify test frameworks, test discovery, test inventory, fixtures/mocks, skipped/disabled tests, and coverage config.
- [ ] Map tests to source symbols/modules.
- [ ] Inspect lint, formatting, typing, build/package, dependency scanning, and CI triggers.
- [ ] Tie each CI run/job/log to an exact commit SHA.
- [ ] Record failed/skipped jobs and unavailable logs.
- [ ] Do not equate test files with passing tests or old CI with current commit verification.

## Phase 7 — Documentation and Project Control
- [ ] Inspect README, architecture, API contracts, setup, environment, operations/deployment, security, testing, release notes, checkpoints, evidence registers, known issues, migration/rollback.
- [ ] Compare documentation claims against source.
- [ ] Record missing/outdated/conflicting documents, ownership gaps, missing evidence, baseline ambiguity, and open questions.
- [ ] Do not edit original documentation as part of the audit.

## Phase 8 — NEXUS / IRIS Consolidation Readiness
- [ ] Establish evidence that NEXUS and IRIS source and their exact revisions are available.
- [ ] Compare reusable core logic, skill/tool boundaries, API contracts, data ownership, persistence, identity/auth, dependencies, config, and duplicate functionality.
- [ ] Assess migration and regression risks.
- [ ] No source merging or restructuring during audit.

## Phase 9 — Future Website Readiness
- [ ] Assess separation of UI and core/business logic.
- [ ] Assess reusable business logic and API contracts.
- [ ] Assess server-side auth, data-layer boundaries, and shared core usage.
- [ ] Identify platform coupling and refactoring gaps.
- [ ] Report readiness and gaps only; do not design/build the website in this audit.

## Final deliverables
- [ ] REPOSITORY_IDENTITY.md
- [ ] FULL_FILE_INVENTORY.csv or Markdown
- [ ] ARCHITECTURE_AND_DATA_FLOW.md
- [ ] API_AND_INTEGRATION_REGISTER.md
- [ ] READ_WRITE_PATH_REGISTER.md
- [ ] SECURITY_FINDINGS.md
- [ ] TEST_TO_SOURCE_MAPPING.md
- [ ] CI_EVIDENCE_REGISTER.md
- [ ] DOCUMENTATION_GAP_ASSESSMENT.md
- [ ] NEXUS_IRIS_CONSOLIDATION_READINESS.md
- [ ] WEBSITE_UPGRADE_READINESS.md
- [ ] MASTER_CHECKPOINT.md
- [ ] MASTER_CHECKLIST.md
- [ ] EVIDENCE_REGISTER.md

## Change log
- 2026-10-15: Initial checklist created. No audit phase is marked complete by this file.
