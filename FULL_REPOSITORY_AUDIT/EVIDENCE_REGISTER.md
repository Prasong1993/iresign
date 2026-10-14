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
