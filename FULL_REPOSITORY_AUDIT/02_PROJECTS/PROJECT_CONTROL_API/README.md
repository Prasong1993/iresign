# Project Control API Evidence

Purpose: consolidate reference evidence for the older Project Control API / NEXUS-Core project while keeping its source identity unresolved where the evidence conflicts.

Known candidate repositories:
- `Prasong1993/Prasong` — FastAPI/SQLite candidate recorded in earlier recovery context; do not assume it is the selected baseline.
- `Prasong1993/LoopController` — Cloudflare Workers/D1 candidate previously marked `BLOCKED — IDENTITY MISMATCH`.
- `Prasong1993/Loop-Controller` — NEXUS workflow/audit candidate; distinct repository and identity.

Status: PARTIAL / NEEDS_REVALIDATION. Record direct source evidence and identity conflicts here. Do not declare a source of truth or move code across candidates.

**Central database rule:** capture only central/reference information, schema descriptions, and mappings needed for inspection at this stage. Do not import the complete database, live records, secrets, or production data. Full database migration is deferred and not authorized.