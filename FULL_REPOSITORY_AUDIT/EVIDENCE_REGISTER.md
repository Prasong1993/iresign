# EVIDENCE REGISTER — FULL REPOSITORY AUDIT

This register records initial observations only. It is not an official baseline declaration and does not certify audit completeness.

## Initial evidence

| Evidence ID | Repository / Ref | Observation | Method | Status | Limitations |
|---|---|---|---|---|---|
| EVD-IDENTITY-001 | https://github.com/Prasong1993/iresign | Repository metadata returned name `iresign`, owner `Prasong1993`, public visibility, default branch `master`, and repository ID `1063265974`. | GitHub repository metadata read | OBSERVED | Metadata alone does not describe all historical files or runtime state. |
| EVD-HEAD-001 | `master` | Branch ref points to `b90313cf09ee471d974dee33e87495593e37fcc9`. | GitHub branch/ref read | OBSERVED | This is the initial observed HEAD; revalidate before relying on it later. |
| EVD-TREE-001 | `master` at initial observed HEAD | Commit metadata references tree SHA `4b825dc642cb6eb9a060e54bf8d69288fbee4904`; root Contents API returned `[]`. | Commit metadata and Contents API read | OBSERVED | Does not prove Git history is empty. A recursive tree request by commit SHA returned 404 and did not provide a complete tree listing. |
| EVD-HISTORY-001 | `master` | Latest commit message returned as `Remove temporary placeholder after cleanup`; parent commit SHA `ddb65c5a514ecdf6dadfb53dabe76798f4e4aa21`. | Recent commits API read | OBSERVED | Only the returned history window was inspected. |
| EVD-BRANCH-001 | Repository branches | Branch listing returned one branch, `master`, pointing to the initial observed HEAD. | Branches API read | OBSERVED | Pagination/visibility limits should be rechecked if relevant. |
| EVD-RELEASE-001 | Repository releases | Releases API returned an empty array. | Releases API read | OBSERVED | Tags are separate and have not been verified. |
| EVD-TAGS-001 | Repository tags | The attempted tags endpoint request failed. | GitHub API fetch attempt | UNKNOWN | No conclusion about tag existence can be made from this failed request. |
| EVD-WORKTREE-001 | Local working copy | No local Git working-tree data was available through the inspected GitHub API. | Access-boundary review | UNKNOWN | Do not infer clean/dirty working-tree state. |

## Evidence rules

For every new entry, record:
- Evidence ID
- Repository URL and exact commit/ref
- Source path/symbol/line range when applicable
- CI Run ID/URL or Test ID when applicable
- Observation
- Verification method
- Timestamp and timezone
- Limitations

Use statuses: VERIFIED, PARTIAL, UNKNOWN, BLOCKED, NOT RUN, IN PROGRESS. Distinguish direct observations from reported history and inference. Never record a test as passed without an execution result tied to the relevant source revision.

## Timestamp

Initial inspection date: 2026-10-15. Exact inspection time and timezone were not captured; do not fabricate them.

## Change log

- 2026-10-15: Initial evidence register created from direct GitHub API observations in the current work session. This register must be extended with new evidence rather than silently rewriting historical observations.


## Current evidence observations — 2026-10-15

These records were added after the initial observations above. They do not erase or retroactively replace the initial empty-root observation.

| Evidence ID | Repository / Ref | Observation | Method | Status | Limitations |
|---|---|---|---|---|---|
| EVD-STRUCTURE-002 | `Prasong1993/iresign`, `master`, file `FULL_REPOSITORY_AUDIT/MASTER_PROJECT_STRUCTURE.md` | Central evidence structure contract updated; blob SHA `99886d2456eb2aa050fba512ad8d643af85d92ca`; file read back and key sections confirmed. | GitHub update + read-back | VERIFIED | This verifies the document content and listed directory indexes, not completion of all audit work. |
| EVD-NEXUS-TREE-001 | `Prasong1993/Loop-Controller`, `main`, commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | Recursive tree returned 52 entries and `truncated=false`; full path/type/size/object-SHA inventory stored at `FULL_REPOSITORY_AUDIT/02_PROJECTS/NEXUS/FULL_FILE_INVENTORY.md` (destination blob SHA `1edb8c9ed2ac62200e2b48c27dc54c4563c43cd0`). | GitHub branch read + recursive tree API + destination read-back | VERIFIED for tree listing | Does not verify file contents, tests, CI, or runtime. |
| EVD-IRIS-TREE-001 | `Prasong1993/Prasong`, `main`, commit `fee44e82a0926ca85833beff8a9462156117a2d9` | Recursive tree returned 107 entries and `truncated=false`; full path/type/size/object-SHA inventory stored at `FULL_REPOSITORY_AUDIT/02_PROJECTS/IRIS/FULL_FILE_INVENTORY.md` (destination blob SHA `c70451f33e3446d4bb443e87f9da365bba26d730`). | GitHub branch read + recursive tree API + destination read-back | VERIFIED for tree listing | Does not verify all file contents, tests, CI, or runtime. |
| EVD-CF-CANDIDATE-TREE-001 | `Prasong1993/LoopController`, `main`, commit `7c23df529f4ce2c25386f45f8b91fc90e5cf068d` | Recursive tree returned one entry: `LICENSE`; `truncated=false`. Inventory stored at `FULL_REPOSITORY_AUDIT/02_PROJECTS/PROJECT_CONTROL_API/CANDIDATE_TREE_INVENTORY.md` (destination blob SHA `4d690439d7257dd3176c581c5300c68e180e29f4`). | GitHub branch read + recursive tree API + destination read-back | VERIFIED for returned tree; identity BLOCKED | A one-file tree does not resolve whether this is the intended Control API source. Do not select as baseline. |
| EVD-PLUGIN-SNAPSHOT-001 | Plugin Creator current source file lists for six private USER-scope plugins; destination under `PLUGIN_INSTALLATION_ARTIFACTS/Plugin-Creator/` | Current plugin files were read from Plugin Creator and compared with the matching GitHub destination files. All 72/72 source files matched exact text content; no missing/extra source paths. | Plugin Creator `get_plugin_files` + GitHub `fetch_file` content comparison | VERIFIED for current source-to-snapshot content | Not a byte-for-byte comparison against a separate official install archive; installability/runtime tests NOT RUN. |
| EVD-AUDIT-TREE-002 | `Prasong1993/iresign`, `master`, observed before this evidence-register update | Branch HEAD and recursive tree SHA `dfa5b61291c91e435bd432e8458c6c376f2edb0f`; 181 entries, 122 blobs, `truncated=false`. | GitHub branch and recursive tree API | VERIFIED at observation time | Later documentation commits may advance HEAD; preserve this as a timestamped historical observation. |

## Current limitations

- NEXUS and IRIS path inventories are verified; detailed source review and complete audit conclusions are not complete.
- G0-07 Mapping Register and G0-08 Document Consistency remain pending/in progress under the existing NIR-P0-004 checkpoint.
- CI/test results, runtime, integration, failure injection, and installability remain NOT RUN or UNKNOWN unless separately evidenced.
- Baseline/source of truth remains UNKNOWN / NOT SELECTED. No source repository was modified and the full Project Control API database was not migrated.


## Additional evidence observations — G0-07 / G0-08

| Evidence ID | Repository / Ref | Observation | Method | Status | Limitations |
|---|---|---|---|---|---|
| EVD-NEXUS-CI-001 | [NEXUS Actions run #193](https://github.com/Prasong1993/Loop-Controller/actions/runs/38017042410), head SHA `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | GitHub Actions reports workflow `NEXUS CI`, run 193, completed with conclusion `success`, on the exact target SHA. | GitHub Actions run metadata read | VERIFIED for CI result and SHA association | Does not prove ChatGPT integration, deployment, runtime/mobile acceptance, or security readiness. Exact test count was not asserted in this record. |
| EVD-IRIS-CI-001 | [IRIS Actions run #3](https://github.com/Prasong1993/Prasong/actions/runs/37678194022), head SHA `fee44e82a0926ca85833beff8a9462156117a2d9` | GitHub Actions reports workflow `IRIS v0.6.5 tests`, run 3, completed with conclusion `success`, on the exact target SHA; root workflow runs `python -m pytest -q` in `IRIS/iris-controller-v0.6.5`. | GitHub Actions run metadata and workflow source read | VERIFIED for CI result and SHA association | Does not independently verify the separately reported VM counts 23/23 and 19/19; no host/plugin install or ChatGPT integration claim. |
| EVD-G0-07-001 | `FULL_REPOSITORY_AUDIT/03_CROSS_PROJECT_MAPPING/G0-07_MAPPING_REGISTER.md`, blob SHA `b93d870c42fc0fd4c83e5e9594e8c7e0c4e33a33` | Initial field-level register records 13 mappings/classifications between NEXUS and IRIS source contracts, including scope conflicts, semantic candidates, and a NEXUS design/implementation gap. | Source read + documentation creation + read-back | VERIFIED as a document; mapping remains IN PROGRESS | Not a complete field inventory; several mappings remain candidates and require more source-path review. |
| EVD-G0-08-001 | `FULL_REPOSITORY_AUDIT/08_DOCUMENT_CONSISTENCY/G0-08_DOCUMENT_CONSISTENCY_REVIEW.md`, blob SHA `b8c7ac8ac6471e7a29bc5668b6efe3bb2fa23e80` | Initial review records ten findings, including stale CI references, an IRIS version-heading mismatch, REST/MCP final-verification persistence differences, and a pending IRIS artifact manifest. | Source/document comparison + GitHub Actions metadata + read-back | VERIFIED as an initial review set | G0-08 remains IN PROGRESS; source repositories were not edited and tests were not executed in this review. |
| EVD-IRIS-REST-MCP-001 | IRIS v0.6.5 `runtime/main.py` blob `7a883223a0f5dcccf3c9fa45800ae628e6e032dc`; `runtime/mcp_server.py` blob `e8851bb16101245f05eace2ead1e82868ef0c919` | REST final verification persists the verification row and audit event; on mismatch it returns HTTP 409. The MCP mismatch path additionally records an error and checkpoint. | Direct source inspection at exact target SHA | VERIFIED for source behavior | This is a code-path comparison, not runtime test evidence. README's phrase “parity with REST” is not supported for mismatch error/checkpoint persistence. |

## Current phase status after these observations

- Structure contract and grouping indexes: written and read back.
- NEXUS and IRIS recursive tree inventories: recorded and read back; path inventory only.
- Six Plugin Creator snapshots: 72/72 source files matched the current Plugin Creator file contents at comparison time.
- G0-07 Mapping Register: started, partial.
- G0-08 Document Consistency Review: started, initial findings recorded.
- NEXUS target-SHA CI: success, run #193.
- IRIS target-SHA CI: success, run #3.
- Runtime/integration/failure-injection/installability tests: NOT RUN in this audit.
- Baseline/source of truth: UNKNOWN / NOT SELECTED.
- Full Project Control API database import/migration: deferred and not authorized.


## Additional evidence observations — IRIS source snapshot completion

| Evidence ID | Repository / Ref | Observation | Method | Status | Limitations |
|---|---|---|---|---|---|
| EVD-IRIS-SNAPSHOT-001 | Source: `Prasong1993/Prasong` commit `fee44e82a0926ca85833beff8a9462156117a2d9`; destination: `Prasong1993/iresign` | Completed the previously incomplete `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/` snapshot. All 21 expected files are present. All 21 source blob SHAs equal destination blob SHAs and exact text comparisons passed. Seventeen missing files were added only after the central directory structure was written and read back. | Read source at pinned commit; limited high-confidence secret-pattern scan; create-file writes; destination read-back/content comparison; recursive tree listing | VERIFIED for 21-file source snapshot completeness and content parity | This is not an official archive comparison or installability/runtime test. Four pre-existing files had no per-file destination creation commit recorded before this verification; that history remains explicitly unrecorded. |
| EVD-IRIS-MANIFEST-001 | `PLUGIN_INSTALLATION_ARTIFACTS/ARTIFACT_MANIFEST.md`, destination blob SHA `d3bd8aae67069cf1d8c559630f9f2e6af86026a9` | Manifest now lists 21 source/destination blob SHA matches and read-back status; no PENDING entries remain. Manifest read-back succeeded. | GitHub update + read-back | VERIFIED | The separate binary installer/official archive is still not identified; installation/runtime remain NOT VERIFIED. |

## Updated snapshot status

- IRIS v0.6.5 reference snapshot: 21/21 source files present and exact content-matched.
- Six private Plugin Creator snapshots: 72/72 source files exact content-matched to current Plugin Creator file contents.
- Combined verified source snapshot content comparisons: 93 files across these seven snapshot groups, excluding provenance/index/manifest documents.
- Official installer archive parity and runtime/installability: NOT RUN.
