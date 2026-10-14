# Plugin Installation Artifact Manifest

**Purpose:** traceable source snapshot for review.  
**Archive status:** IN PROGRESS until all destination files are read back and recorded.  
**Install/runtime status:** NOT VERIFIED.  
**Official baseline:** UNKNOWN / NOT SELECTED.

## Package: IRIS v0.6.5

- Source repository: https://github.com/Prasong1993/Prasong
- Source commit reference: `fee44e82a0926ca85833beff8a9462156117a2d9`
- Source directory: `IRIS/iris-controller-v0.6.5/`
- Destination directory: `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/`
- Copy mode: preserve relative paths; text files only.
- Purpose: evidence/reference for inspection, not a release or installability certification.
- Secret review: must be recorded after reviewing contents; do not copy secret values.
- Test execution: NOT RUN by the act of copying.
- Source blob SHA and destination blob SHA: record per file below after write and read-back.

| Source path | Source blob SHA | Destination path | Destination blob SHA | Destination commit SHA | Read-back |
|---|---|---|---|---|---|
| `IRIS/iris-controller-v0.6.5/.codex-plugin/plugin.json` | `b68db556440fd59bc43f14b9ad4818eef49ab501` | `PLUGIN_INSTALLATION_ARTIFACTS/IRIS/iris-controller-v0.6.5/.codex-plugin/plugin.json` | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/.github/workflows/iris-v065-test.yml` | `a20eef08b961c606da87cef85004951ef72f8c75` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/.mcp.json` | `f4292ce99d12a9169c2921bba505123cc024bfa0` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/IRIS_VALIDATION_v0.6.5.md` | `8ab1d9fa2583d20a7dff68878f3f40454a6577e6` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/README.md` | `1aef014fbeda4e1c98241d0c5da4f43d34a6532e` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/docs/IRIS_FIVE_STEP_EXECUTION_CONTRACT.md` | `d5322ead6eecddac1a5ebecc57553195bbced48e` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/docs/IRIS_PLUGIN_STRUCTURE.md` | `ef61207e04049b0c7eaabe950718af5121668dc7` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/plugin.json` | `2f2e854017ab17e0548aa3ac333a84f087dcde6c` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/controller.py` | `194c81e48dadf5f89a6c5e14731b5288b86164f8` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/database.py` | `c3937168f3904b804948c7a090ffd8f7f43cd11c` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/main.py` | `7a883223a0f5dcccf3c9fa45800ae628e6e032dc` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/mcp_server.py` | `e8851bb16101245f05eace2ead1e82868ef0c919` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/model.py` | `92beff61b7f113a6395ae38712c529bad252da13` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/requirements.txt` | `903eaab7371a4bd3719c9cb917f301b879725a9b` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/runtime/verify.py` | `6865448f4091bdeec9f4aab62f3b4ff12f2464c6` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/skills/iris/SKILL.md` | `58828bc0cd8c565a08aa4320534362685f068790` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/tests/test_api.py` | `7d060a16e5cf1f1ce36b0b3b423c49feaf4c2085` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/tests/test_controller.py` | `c7fcbfe2d9267b98d21a684c6e7a894da82e3d4e` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/tests/test_e2e_api.py` | `297c71677f554b59ac86a3a588edac1398e6be27` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/tests/test_mcp.py` | `855a963176e40ff6f4e1845f2bdeed777fecc959` | same relative path under destination root | PENDING | PENDING | PENDING |
| `IRIS/iris-controller-v0.6.5/tests/test_mcp_e2e.py` | `b3bf742a74610b6cc4fdef52862aab52ef3d8122` | same relative path under destination root | PENDING | PENDING | PENDING |

## Known gaps
- No binary installer/zip/tarball has been identified or copied.
- No standalone NEXUS plugin installer has been identified.
- Dropbox archive folders inspected for this task returned no files.
- No install or runtime test has been performed.
