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
