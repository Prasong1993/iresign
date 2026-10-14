# Plugin Installation Artifact Manifest

**Purpose:** traceable source snapshot for review.  
**Archive status:** **VERIFIED — 21/21 source files present and content-matched** against the source package at the pinned commit.  
**Install/runtime status:** NOT VERIFIED.  
**Official baseline:** UNKNOWN / NOT SELECTED.

## Package: IRIS v0.6.5

- Source repository: https://github.com/Prasong1993/Prasong
- Source commit: `fee44e82a0926ca85833beff8a9462156117a2d9`
- Source directory: `IRIS/iris-controller-v0.6.5/`
- Destination directory: `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/`
- Copy mode: preserve relative paths; text files only.
- Purpose: evidence/reference for inspection, not a release or installability certification.
- Content comparison: all 21 listed source files were read from the source repository and compared with their destination files. Destination Git blob SHA equals source blob SHA for each file; exact text comparison passed.
- Destination commit SHA: recorded for 17 files added in this verification pass. The four pre-existing destination files had no per-file creation commit recorded in the earlier manifest; their current content/blob identity was verified and they remain labelled as pre-existing.
- Secret scan: a limited scan for high-confidence API-key/private-key/AWS-key patterns found no matches in the 21 reviewed files. This is not a comprehensive security review and does not prove absence of all secrets.
- Test execution caused by copying: NOT RUN.
- Official installation archive parity: NOT RUN; this is a source-to-destination comparison, not comparison with a separately downloaded ZIP/tarball.

## Per-file provenance and read-back

| Relative path | Source blob SHA | Destination blob SHA | Destination commit SHA | Read-back |
|---|---|---|---|---|
| `.codex-plugin/plugin.json` | `b68db556440fd59bc43f14b9ad4818eef49ab501` | `b68db556440fd59bc43f14b9ad4818eef49ab501` | NOT RECORDED — pre-existing snapshot | MATCH — exact content match |
| `.github/workflows/iris-v065-test.yml` | `a20eef08b961c606da87cef85004951ef72f8c75` | `a20eef08b961c606da87cef85004951ef72f8c75` | NOT RECORDED — pre-existing snapshot | MATCH — exact content match |
| `.mcp.json` | `f4292ce99d12a9169c2921bba505123cc024bfa0` | `f4292ce99d12a9169c2921bba505123cc024bfa0` | NOT RECORDED — pre-existing snapshot | MATCH — exact content match |
| `IRIS_VALIDATION_v0.6.5.md` | `8ab1d9fa2583d20a7dff68878f3f40454a6577e6` | `8ab1d9fa2583d20a7dff68878f3f40454a6577e6` | NOT RECORDED — pre-existing snapshot | MATCH — exact content match |
| `README.md` | `1aef014fbeda4e1c98241d0c5da4f43d34a6532e` | `1aef014fbeda4e1c98241d0c5da4f43d34a6532e` | 563cbef4ef4393816a62482f9277a21b03727028 | MATCH — exact content match |
| `docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md` | `d5322ead6eecddac1a5ebecc57553195bbced48e` | `d5322ead6eecddac1a5ebecc57553195bbced48e` | ec797ba19cdf515bdf3f315b2960f6f9a3405122 | MATCH — exact content match |
| `docs/IRIS_PLUGIN_STRUCTURE.md` | `ef61207e04049b0c7eaabe950718af5121668dc7` | `ef61207e04049b0c7eaabe950718af5121668dc7` | 7500d8ec084088bb42b3f654524c2a1c15d47009 | MATCH — exact content match |
| `plugin.json` | `2f2e854017ab17e0548aa3ac333a84f087dcde6c` | `2f2e854017ab17e0548aa3ac333a84f087dcde6c` | 64044ddc58ab81e1e1def3cdd12450966dd21f7b | MATCH — exact content match |
| `runtime/controller.py` | `194c81e48dadf5f89a6c5e14731b5288b86164f8` | `194c81e48dadf5f89a6c5e14731b5288b86164f8` | b25ee23deb89eafca54f298379758141b249c57a | MATCH — exact content match |
| `runtime/database.py` | `c3937168f3904b804948c7a090ffd8f7f43cd11c` | `c3937168f3904b804948c7a090ffd8f7f43cd11c` | 2ae5018dab6c81616908a3e71e4d79fd9d0fd407 | MATCH — exact content match |
| `runtime/main.py` | `7a883223a0f5dcccf3c9fa45800ae628e6e032dc` | `7a883223a0f5dcccf3c9fa45800ae628e6e032dc` | 72c6e90236290cfc887edcb7a3eab58542f053e0 | MATCH — exact content match |
| `runtime/mcp_server.py` | `e8851bb16101245f05eace2ead1e82868ef0c919` | `e8851bb16101245f05eace2ead1e82868ef0c919` | 18ed71c193cd4da7b4caf636c76b3af84cc17600 | MATCH — exact content match |
| `runtime/model.py` | `92beff61b7f113a6395ae38712c529bad252da13` | `92beff61b7f113a6395ae38712c529bad252da13` | df44b9d28e5dc2d857d2dca3557d469390356b35 | MATCH — exact content match |
| `runtime/requirements.txt` | `903eaab7371a4bd3719c9cb917f301b879725a9b` | `903eaab7371a4bd3719c9cb917f301b879725a9b` | 921fc1aa971a248cc800944808df8a2bec8f9ffb | MATCH — exact content match |
| `runtime/verify.py` | `6865448f4091bdeec9f4aab62f3b4ff12f2464c6` | `6865448f4091bdeec9f4aab62f3b4ff12f2464c6` | b517a1da931bfb50fdda589d3451e34c246a318b | MATCH — exact content match |
| `skills/iris/SKILL.md` | `58828bc0cd8c565a08aa4320534362685f068790` | `58828bc0cd8c565a08aa4320534362685f068790` | 00df44e9b8d8abb1ffdc8fc3793bfdf473a34738 | MATCH — exact content match |
| `tests/test_api.py` | `7d060a16e5cf1f1ce36b0b3b423c49feaf4c2085` | `7d060a16e5cf1f1ce36b0b3b423c49feaf4c2085` | 80ee75720819238b6ea551e29395a6f3e0d755d8 | MATCH — exact content match |
| `tests/test_controller.py` | `c7fcbfe2d9267b98d21a684c6e7a894da82e3d4e` | `c7fcbfe2d9267b98d21a684c6e7a894da82e3d4e` | 06d61777eb8ba913cacaf3f35e2c255bcec435b3 | MATCH — exact content match |
| `tests/test_e2e_api.py` | `297c71677f554b59ac86a3a588edac1398e6be27` | `297c71677f554b59ac86a3a588edac1398e6be27` | 0d951b69be7415568438d41746aa3e26ed87e9c2 | MATCH — exact content match |
| `tests/test_mcp.py` | `855a963176e40ff6f4e1845f2bdeed777fecc959` | `855a963176e40ff6f4e1845f2bdeed777fecc959` | 016410bc93434ad167c41e9c63b54ec1a51254c3 | MATCH — exact content match |
| `tests/test_mcp_e2e.py` | `b3bf742a74610b6cc4fdef52862aab52ef3d8122` | `b3bf742a74610b6cc4fdef52862aab52ef3d8122` | 097cabd4490df4efe4a2353f5e8d69b2bfbe6608 | MATCH — exact content match |

## Known gaps

- No separate binary installer/ZIP/tarball has been identified or copied.
- No standalone NEXUS plugin installer was identified in the inspected source tree.
- Dropbox archive folders inspected for this task returned no files.
- Installation/runtime tests have not been performed.
- The v0.6.5 snapshot is a review copy; Plugin Creator's separate v0.7.4 IRIS snapshot remains a different artifact and must not be conflated with it.

## Change log

- 2026-10-15: Completed the previously partial text snapshot by adding the missing 17 source files after the central structure was established.
- 2026-10-15: Read back all 21 destination files and verified exact content/blob-SHA matches against source commit `fee44e82a0926ca85833beff8a9462156117a2d9`.
- 2026-10-15: Kept source repository unchanged; no dependencies installed, no tests executed, no baseline selected, and no database migrated.
