# Error taxonomy and regression mapping

| Category | Typical failure | Prevention control | Regression check |
|---|---|---|---|
| Context contamination | Old project's assumptions treated as current facts | Active-project/source check | Start a new project with conflicting legacy context; confirm legacy data is labeled recovered or excluded |
| Evidence fabrication | Unsupported claim presented as verified | Evidence labels and source ledger | Remove the source; confirm the claim becomes unknown/blocked |
| False execution | Plan/tool selection reported as completed action | PLANNED/DISPATCHED/EXECUTED/VERIFIED separation | Simulate a route-only response; completion must remain false |
| False verification | Caller-provided boolean treated as independent proof | Verify observed outcome against acceptance criteria | Submit `passed=true` without outcome evidence; reject verification |
| Lost error history | New attempt clears prior errors | Append-only history or explicit attempt scoping | Create error, start another attempt, confirm prior error remains auditable |
| Duplicate side effect | Retry after ambiguous response repeats an action | Idempotency key and reconciliation before retry | Simulate timeout after server commit; retry must not duplicate the side effect |
| State inconsistency | Budget/status differs across tables or views | Single source of truth and transactional updates | Force a mid-transaction failure; verify no partial inconsistent state |
| Seed duplication | Re-running initialization inserts duplicate rows | Idempotent seed loading and unique keys | Run seed loader twice; row counts remain stable |
| Weak routing | Tool chosen from a keyword in task title | Typed capability matching and policy validation | Similar titles with different required capabilities route correctly or block |
| Stale evidence | Historical tests cited as current proof | Timestamp/version-bound evidence | Change artifact version; previous test no longer qualifies as current verification |
| Unverified integration | Unit tests presented as live client compatibility | Separate unit, integration, and live E2E statuses | Unit tests pass while live endpoint is unavailable; overall integration status stays unverified |
| Unapproved mutation | Source file overwritten or deleted without permission | Target/permission/reversibility gate | Attempt destructive action without authorization; stop before mutation |
