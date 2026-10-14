# Source Repository Register

**Purpose:** identify source repositories and exact refs before collecting or mapping their contents into the central evidence workspace.  
**Audit workspace:** https://github.com/Prasong1993/iresign  
**Status:** live branch/ref identity checked; source content and runtime audit remain partial.  
**Baseline:** UNKNOWN / NOT SELECTED.

## Repository register

| Source group | Repository | Current observed branch/ref | Current observed tree entries | Evidence status | Handling rule |
|---|---|---|---:|---|---|
| NEXUS | https://github.com/Prasong1993/Loop-Controller | `main` → `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | 52 (recursive tree, not truncated) | VERIFIED — branch head matches recorded SHA | Read-only; inventory at [NEXUS/FULL_FILE_INVENTORY.md](../02_PROJECTS/NEXUS/FULL_FILE_INVENTORY.md); keep separate from LoopController |
| IRIS | https://github.com/Prasong1993/Prasong | `main` → `fee44e82a0926ca85833beff8a9462156117a2d9` | 107 (recursive tree, not truncated) | VERIFIED — branch head matches recorded SHA | Read-only; inventory at [IRIS/FULL_FILE_INVENTORY.md](../02_PROJECTS/IRIS/FULL_FILE_INVENTORY.md); distinguish source v0.6.5 from Plugin Creator snapshot v0.7.4 |
| Project Control API / Cloudflare candidate | https://github.com/Prasong1993/LoopController | `main` → `7c23df529f4ce2c25386f45f8b91fc90e5cf068d` | 1 (only `LICENSE` in returned recursive tree) | BLOCKED — IDENTITY MISMATCH; tree listing verified | Candidate inventory at [CANDIDATE_TREE_INVENTORY.md](../02_PROJECTS/PROJECT_CONTROL_API/CANDIDATE_TREE_INVENTORY.md); do not select as baseline |
| Central evidence workspace | https://github.com/Prasong1993/iresign | `master`; current tree enumerated during this work | 181 entries at last tree read | VERIFIED as destination identity; HEAD changes as evidence is added | Audit documentation and provenance-labelled review snapshots; record fresh HEAD after each batch |
| Private Plugin Creator packages | Plugin Creator source inventory (not a source repository) | Six current private USER-scope plugins; versions and release IDs read live | 72 source files | VERIFIED — current Plugin Creator contents compared with destination; 72/72 exact matches | Keep each plugin in its own versioned folder and retain provenance; official archive parity/runtime still NOT RUN |

## Exact source tree evidence

- NEXUS: commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`; recursive tree response was not truncated; 52 entries. Full path/blob/tree SHA list is stored in the NEXUS inventory file.
- IRIS: commit `fee44e82a0926ca85833beff8a9462156117a2d9`; recursive tree response was not truncated; 107 entries. Full path/blob/tree SHA list is stored in the IRIS inventory file.
- LoopController: commit `7c23df529f4ce2c25386f45f8b91fc90e5cf068d`; recursive tree response was not truncated; only the `LICENSE` file was returned. This confirms the observed tree shape but does not resolve project identity or prove that this is the intended Control API source.

## Six Plugin Creator snapshots

Current Plugin Creator metadata/file lists were read for:
- `evidence-workflow-guard` v0.1.0
- `nexus-project-control` v0.1.1
- `assistant-error-guard` v0.2.0
- `chatgpt-control-api` v0.2.3
- `iris-step1` v0.1.0
- `iris-controller` v0.7.4

Every one of the 72 listed source files was read from Plugin Creator and compared against the corresponding GitHub destination file. **72/72 content comparisons matched exactly; no missing or extra source paths were found.** This does not prove byte-for-byte parity with a separately downloaded official installation archive, installability, or runtime correctness.

## Required fields for future observations

- Evidence ID and capture date/time/timezone (do not invent missing timestamps).
- Repository full name and canonical URL.
- Branch/tag/ref and exact commit SHA.
- Source path and blob SHA; for directories, tree SHA and enumerated paths.
- Collection method and destination path.
- Source file count, destination file count, excluded file types.
- Read-back and content-comparison result when performed.
- Limitations, inaccessible data, identity conflicts, and status.
- Whether the record is historical, live-revalidated, or user-stated.

## Remaining gaps

- Content-level audit and full inventory review of the NEXUS and IRIS sources remain incomplete.
- LoopController's identity mismatch remains unresolved even though its current tree was inspected.
- Official installation archive parity and installation/runtime tests for the six Plugin Creator snapshots remain NOT RUN.
- The old Project Control API structure is incomplete; only central/reference information belongs in this workspace for now. Full database import/migration is deferred.
- Runtime, integration, and failure-injection tests remain NOT RUN unless a separate execution record proves otherwise.

## Change log

- 2026-10-15: Revalidated the `main` branch heads for NEXUS, IRIS, and LoopController. NEXUS and IRIS matched the recorded target SHAs; LoopController returned one tree entry and remains identity-blocked.
- 2026-10-15: Re-read current Plugin Creator metadata and file contents for all six plugins; compared 72/72 source files with GitHub snapshots and found exact content matches.
- 2026-10-15: Recorded recursive source-tree inventories and destination paths. No source repository was modified, no baseline selected, and no full database migrated.
