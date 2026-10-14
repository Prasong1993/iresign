# FULL REPOSITORY AUDIT — Audit Scope

- Audit workspace: https://github.com/Prasong1993/iresign
- Owner: Prasong1993
- Default branch observed: `master`
- Repository identity: observed from GitHub metadata; revalidate HEAD when recording new evidence
- Current work: central evidence repository structure, source repository mapping, and provenance-labelled review snapshots
- Phase: Phase 0 — Discovery & Evidence Verification
- Baseline / Source of Truth: UNKNOWN / NOT SELECTED
- Source repositories: READ-ONLY
- Audit-repository documentation/structure and evidence-register writes: authorized by the user's latest instruction, with read-back required
- Application source-code edits, baseline selection, full database migration, integration, deployment, release changes, and runtime/security testing: NOT AUTHORIZED

## Objective

Use this repository as the central review workspace for evidence from the user's separate repositories and six private Plugin Creator plugins. Organize evidence by source/project so each file can be traced to the correct owner, repository, version, path, and exact commit. Keep NEXUS, IRIS, Project Control API, and other candidates separate until evidence establishes their identity and relationships.

The user has clarified the intended sequence:
1. Define and verify the central directory structure first.
2. Register source repositories and their identities.
3. Reconcile the six existing private Plugin Creator source snapshots and provenance.
4. Collect source evidence into the correct per-project group, preserving provenance.
5. Keep central/shared project information separate from a full database migration. The old Project Control API structure is unfinished; its complete database is deliberately deferred.
6. Use the existing checkpoint NIR-P0-004; do not create a replacement checkpoint.

Existing Plugin Creator snapshots are already present in the repository from earlier work. Preserve them while reconciling the structure; do not silently move, rename, overwrite, or delete them.

## Permissions and change control

Authorized in the audit repository:
- Read current repository metadata, files, refs, commits, and accessible CI evidence.
- Create or update audit documentation, structure maps, evidence registers, provenance records, and review snapshots needed for the central evidence workspace.
- Read back each write and record its commit/blob identity.

Not authorized:
- Modifying source code in NEXUS, IRIS, Project Control API, or any other source repository.
- Selecting or declaring an official baseline/source of truth.
- Importing or migrating the complete central database or live/production data.
- Merging source repositories, integrating systems, changing plugin releases, deploying, changing production state, or altering branches in source repositories.
- Installing dependencies, running potentially mutating code, runtime tests, failure injection, penetration testing, or other security attack tests without separate approval.
- Copying secrets, tokens, credentials, or production data into the audit repository.

## Evidence labels

- `VERIFIED`: directly checked against a stated criterion.
- `USER_STATED`: explicitly specified by the user but not independently verified.
- `RECOVERED`: retrieved from previous context or historical records; current truth may require revalidation.
- `PARTIAL`: only part of the criterion is covered.
- `UNKNOWN`: insufficient evidence or unavailable.
- `BLOCKED`: a specific identity, access, or technical barrier prevents verification.
- `NEEDS_REVALIDATION`: historical evidence exists but must be checked against the current ref.
- `NOT RUN`: action/test has not been executed.
- `IN PROGRESS`: work has started but exit criteria are unmet.

Track `PLANNED`, `DISPATCHED`, `EXECUTED`, and `VERIFIED` separately. Source inspection is not test execution. A test definition is not a passing test. Historical CI is not evidence for a different commit. API/MCP reachability is not proof of ChatGPT integration.

## Required workflow

1. Verify the master project structure and read it back.
2. Maintain a source repository register with exact repository, branch/ref, commit, paths, evidence class, and limitations.
3. Inventory each source repository at a specific commit; do not claim completeness until every in-scope path is accounted for.
4. Inspect architecture, APIs, dependencies, persistence paths, security boundaries, tests and CI with path-level evidence.
5. Maintain per-project evidence separately; only then create cross-project mappings.
6. Complete G0-07 Mapping Register and G0-08 Document Consistency under the existing NIR-P0-004 checkpoint.
7. Leave full database migration, source implementation, runtime testing, integration, and baseline selection blocked until separately authorized.

## Historical observations and limitations

Earlier setup records reported that GitHub metadata returned default branch `master`, and an initial root Contents API call returned an empty array. The current tree has since contained audit documentation and plugin artifact folders. Preserve the earlier observation as historical; do not overwrite it or use it as the current tree. Record each new HEAD and inventory as a new observation.

## Change log

- 2026-10-15: Scope clarified to reflect the user's latest authorization for central structure/documentation and provenance-labelled evidence collection in this repository. Source repositories remain read-only; full central database migration remains deferred.
