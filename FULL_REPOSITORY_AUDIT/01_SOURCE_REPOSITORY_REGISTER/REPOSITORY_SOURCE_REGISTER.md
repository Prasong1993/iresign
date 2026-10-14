# Source Repository Register

**Purpose:** identify every source repository before collecting or mapping its contents into the central evidence workspace.  
**Audit workspace:** https://github.com/Prasong1993/iresign  
**Status:** initial register — partial; repository HEADs and complete inventories require live verification.  
**Baseline:** UNKNOWN / NOT SELECTED.

## Repository register

| Source group | Repository | Recorded scope/ref | Evidence status | Handling rule |
|---|---|---|---|---|
| NEXUS | https://github.com/Prasong1993/Loop-Controller | Historical commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | NEEDS_REVALIDATION | Read-only; keep separate from similarly named LoopController |
| IRIS | https://github.com/Prasong1993/Prasong | Historical commit `fee44e82a0926ca85833beff8a9462156117a2d9`; package scope `IRIS/iris-controller-v0.6.5/` | NEEDS_REVALIDATION | Read-only; distinguish source v0.6.5 from Plugin Creator snapshot v0.7.4 |
| Project Control API / Cloudflare candidate | https://github.com/Prasong1993/LoopController | Historical ref noted as `7c23df...c68d` in prior handoff | BLOCKED — IDENTITY MISMATCH | Do not select as baseline; resolve identity from direct evidence |
| Central evidence workspace | https://github.com/Prasong1993/iresign | Branch `master`; live tree must be re-read for every new inventory | VERIFIED as destination identity; current HEAD recorded separately per evidence batch | Audit docs and provenance-labelled review snapshots only |
| Private Plugin Creator packages | Plugin Creator source inventory (not a source repository) | Six recorded plugins; versions listed in `PLUGIN_INSTALLATION_ARTIFACTS/Plugin-Creator/INDEX.md` | RECOVERED; revalidate current releases and file lists | Keep each plugin in its own versioned folder and retain provenance |

## Required fields for every subsequent source observation

- Evidence ID and capture date/time/timezone (do not invent missing timestamps).
- Repository full name and canonical URL.
- Branch/tag/ref and exact commit SHA.
- Source path and blob SHA; for directories, commit tree SHA and enumerated paths.
- Collection method and destination path.
- Source file count, destination file count, and any excluded file types.
- Read-back result; byte-for-byte comparison result if actually performed.
- Limitations, inaccessible data, identity conflicts, and status.
- Whether the record is historical, live-revalidated, or user-stated.

## Current known gaps

- Live HEADs for the NEXUS and IRIS target refs have not been revalidated in this register.
- The Cloudflare candidate identity mismatch remains unresolved.
- Full file inventories and source-to-destination comparisons are incomplete.
- The six Plugin Creator snapshots are recorded as source snapshots, not confirmed official installable archives.
- The old Project Control API structure is incomplete; central/reference information may be documented, but the full database is intentionally not imported at this stage.
- Runtime, integration, failure-injection, and installability tests remain NOT RUN unless a separate execution record proves otherwise.

## Change log

- 2026-10-15: Initial register created from recovered checkpoint and repository records. It is not a baseline selection and does not certify current source revisions.
