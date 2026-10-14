# G0-08 — Document Consistency Review

**Checkpoint:** NIR-P0-004 — Provenance Gap Closure & Phase 0 Evidence Consolidation  
**Phase:** 0 — Discovery & Evidence Verification  
**Mode:** READ-ONLY review of source repositories; documentation-only update in the central audit repository  
**Status:** IN PROGRESS — initial findings recorded; not a complete review  
**Baseline / Source of Truth:** UNKNOWN / NOT SELECTED  
**Source repository changes:** NOT AUTHORIZED

## 1. Review method and source revisions

Reviewed documents and source files at the exact refs already recorded in the source register:
- NEXUS: `Prasong1993/Loop-Controller`, `main` / commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`.
- IRIS: `Prasong1993/Prasong`, `main` / commit `fee44e82a0926ca85833beff8a9462156117a2d9`.

Relevant evidence is linked to exact source paths and blob SHAs below. This review reads source and documentation; it does not execute tests or runtime code.

## 2. Findings

| Finding ID | Classification | Source evidence | Observation | Required disposition |
|---|---|---|---|---|
| DOC-001 | **STALE REFERENCE / NEEDS CLARIFICATION** | NEXUS `README.md` blob `71d4c4e5be822a2c3193c969a986baea2c6ddc13`; run [#179](https://github.com/Prasong1993/Loop-Controller/actions/runs/38015769056); target-SHA run [#193](https://github.com/Prasong1993/Loop-Controller/actions/runs/38017042410) | README presents CI run #179 as the final/latest run; that run's head SHA is `83340b5b74fafa54df72554d2b8c3b0b44a0c8dd`, not the currently reviewed target SHA. The API returns run #193 as completed/success for target commit `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa`. | When source docs are next authorized for editing, make CI references commit-specific and distinguish historical test counts from the current target-SHA result. Do not infer the number of tests in run #193 from the README. |
| DOC-002 | **HISTORICAL / NOT CURRENT STATUS** | NEXUS `docs/VERIFICATION_PLAN.md` blob `735fbfbd8fa4e47ba2035eae6c906dde2a664131`; `docs/CHECKPOINT_NEXUS_2026-10-10.md` blob `995a4c84302b6bcca702bb686c28b2dc0742900b` | Verification plan lists a 58-test Python 3.11–3.13 run and references earlier CI #121; the checkpoint records last-confirmed CI #12 at commit `6e89df9bb2f10dd088acecfdc99e46932a60649e`. These are historical snapshots and are not evidence for the later target SHA. | Preserve these as dated history; annotate their scope/ref if reused in a current status report. Current target-SHA CI evidence is run #193. |
| DOC-003 | **IMPLEMENTATION-COVERAGE GAP** | NEXUS `docs/RECORDS_AND_EVIDENCE_SCHEMA.md` blob `35baaa09a55052967ad63bae0059bec88bb6f479`; `nexus/records.py` blob `2fea2e46cd790c6dc9225a6532c35d48cd586acd`; `nexus/core.py` blob `bd12f4af3fa59b919ef029a5c9dada047073067b` | Schema documentation proposes normalized operational tables such as `usage_events`, `error_events`, `evidence_records`, `decisions`, `checkpoints`, and `verification_results`. The inspected RecordStore code defines `operational_records` with a typed envelope and `payload_json`; NEXUS core separately defines project/task/evidence/audit/checkpoint tables. The schema document explicitly says the contract is not proof every producer/query is wired and labels full automatic capture OPEN. | Keep the contract classified as intended design; create an implementation-coverage map per record type and endpoint. Do not describe the full record system as completely implemented without matching source/tests/CI evidence. |
| DOC-004 | **VERSION LABEL MISMATCH** | IRIS `docs/IRIS_PLUGIN_STRUCTURE.md` blob `ef61207e04049b0c7eaabe950718af5121668dc7`; package `IRIS/iris-controller-v0.6.5/` | The document heading says “IRIS Plugin Structure v0.6.3” while it is inside the v0.6.5 package and references its current package structure. | Treat the heading as stale until reviewed. Do not edit the source repository as part of this read-only audit. |
| DOC-005 | **CODE/DOCUMENTATION CONFLICT** | IRIS `README.md` blob `1aef014fbeda4e1c98241d0c5da4f43d34a6532e`; REST `runtime/main.py` blob `7a883223a0f5dcccf3c9fa45800ae628e6e032dc`; MCP `runtime/mcp_server.py` blob `e8851bb16101245f05eace2ead1e82868ef0c919`; `tests/test_mcp.py` blob `855a963176e40ff6f4e1845f2bdeed777fecc959` | README says MCP `final_verify` persists mismatch into verifications/audit/errors/checkpoints “parity with REST.” The inspected MCP path records verification/audit and adds error/checkpoint records on mismatch. The inspected REST `final_verify` path writes verification and audit records, returns 409 on mismatch, and does not add error/checkpoint records in that function. | The “parity with REST” claim is not supported by the inspected source. Clarify whether the intended contract is MCP-only richer persistence or change source later under separate authorization. Record REST/MCP difference in the API contract and tests. |
| DOC-006 | **PARTIAL EVIDENCE / CLAIM NEEDS PROVENANCE** | IRIS `IRIS_VALIDATION_v0.6.5.md` blob `8ab1d9fa2583d20a7dff68878f3f40454a6577e6`; root workflow `.github/workflows/iris-v065-test.yml` blob `443c490f35048e114090d8ddf653bd4cf4d5da56`; run [#3](https://github.com/Prasong1993/Prasong/actions/runs/37678194022) | Validation document reports 23/23 tests and 19/19 MCP stdio E2E executed in a VM on 2026-10-08. GitHub Actions run #3 is confirmed completed/success for the exact target commit and the workflow runs `python -m pytest -q`; the exact 23/23 and 19/19 counts are not established by the run summary fetched in this review. | Keep the historical VM counts labelled as reported until the underlying logs or a run artifact can be tied to those counts. Record the target-SHA CI success separately; do not merge these into one claim. |
| DOC-007 | **STRUCTURE / CI BOUNDARY CLARIFICATION** | IRIS root workflow blob `443c490f35048e114090d8ddf653bd4cf4d5da56`; nested package workflow blob `a20eef08b961c606da87cef85004951ef72f8c75` | The repository has a root GitHub Actions workflow and a similarly named workflow file nested inside the plugin package. The root workflow is the active GitHub Actions path observed in run #3; the nested copy is a packaged file, not independently proven to be an active workflow entrypoint. | Keep their roles distinct in the artifact manifest. Do not count the nested copy as a second CI run. |
| DOC-008 | **EXPLICIT UNPROVEN STATUS — NO CONTRADICTION FOUND** | IRIS `runtime/model.py` blob `92beff61b7f113a6395ae38712c529bad252da13`; `runtime/main.py` blob `7a883223a0f5dcccf3c9fa45800ae628e6e032dc` | The model lists 22 `WORKING_STRUCTURE` section names, while the API reports `canonical_22_source: UNPROVEN`. The source explicitly marks the canonical origin as unproven; the list alone is not proof of canonicality. | Preserve the UNPROVEN label until a trusted original structure artifact and provenance are found. |
| DOC-009 | **DESTINATION MANIFEST INCOMPLETE** | `PLUGIN_INSTALLATION_ARTIFACTS/ARTIFACT_MANIFEST.md` blob `d9c445002ea8997db40f8d2b3383aee7096ced50` | The IRIS v0.6.5 source-to-destination manifest still records destination blob SHA, destination commit SHA, and read-back as PENDING for listed files. The separate six Plugin Creator snapshots have been content-compared 72/72, but that does not close the separate IRIS v0.6.5 manifest. | Continue read-back and per-file provenance for the IRIS v0.6.5 snapshot separately; do not infer it is complete from the six-plugin comparison. |
| DOC-010 | **HISTORICAL OBSERVATION RETAINED** | `FULL_REPOSITORY_AUDIT/EVIDENCE_REGISTER.md` initial entries and current tree evidence | The initial record says the root Contents API returned an empty array; the current repository now contains many audit and artifact files. These observations refer to different points in history and are not a contradiction if the initial observation remains clearly dated. | Keep the initial observation unchanged and add newer dated observations, as already done in the evidence register. |

## 3. Confirmed CI observations (source-bound)

| Repository | Run | Exact head SHA | Result | Boundary |
|---|---|---|---|---|
| NEXUS | [Run #193](https://github.com/Prasong1993/Loop-Controller/actions/runs/38017042410) | `eb5359505bf39e4ca1dcd3512f2b8ea3ac6e8baa` | completed / success | CI result only; no live ChatGPT integration, deployment, production security, or mobile acceptance is implied |
| IRIS v0.6.5 | [Run #3](https://github.com/Prasong1993/Prasong/actions/runs/37678194022) | `fee44e82a0926ca85833beff8a9462156117a2d9` | completed / success | CI result only; host/plugin installation and ChatGPT integration remain unproven |

## 4. Review outcome

- G0-08 has **started**; the findings above are the initial verified review set, not a complete document audit.
- Source-repository edits remain unauthorized. Findings are recorded here so they can be corrected later under the appropriate approval.
- No test was executed during this review. CI results were read from GitHub Actions metadata.
- NEXUS and IRIS remain separate systems. No common schema, baseline, or integration has been approved.
- The central Project Control API database remains deferred; this review uses schema/source descriptions only.

## 5. Next review actions

- [ ] Review all NEXUS project documents against the exact target source and current CI runs.
- [ ] Review all IRIS v0.6.5 package documents/manifests and the v0.7.4 Plugin Creator snapshot for version/ownership conflicts.
- [ ] Reconcile REST versus MCP contracts field-by-field, preserving their current differences.
- [ ] Link every finding to evidence-register IDs and mark resolved only after direct read-back.
- [ ] Continue G0-07 field mapping after additional source-path review; neither G0-07 nor G0-08 is complete.
