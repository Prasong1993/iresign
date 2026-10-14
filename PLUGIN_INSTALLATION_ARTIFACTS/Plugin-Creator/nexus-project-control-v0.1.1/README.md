# NEXUS Project Control — private skills-only plugin

This plugin packages the reviewed NEXUS workflow as reusable instructions for evidence-gated project work.

## Included
- `plugin.json`: Agent Plugins 1.0 manifest.
- `skills/nexus-controlled-workflow/SKILL.md`: state machine, evidence rules, policy gates, execution boundaries, verification, audit, recovery, and protected NEXUS_IRIS checkpoint handling.

## Important limitation
This release does not connect to the NEXUS REST API/MCP server and does not provide durable database-backed state or deterministic server-side policy enforcement. It is an installable workflow aid, not proof of a deployed controller. A verified, reachable endpoint and a tested authentication/transport configuration are required before adding an MCP connection.

## Evidence basis
The workflow is based on reviewed source/docs for `Prasong1993/Loop-Controller` at commit `de504565a8f942396a6fc704a352baa1b2dece67`, including the state-transition policy, evidence verification, checkpoint/recovery, audit, and operational-record design. The related PR #4 remains Draft/OPEN and known gaps remain; this package does not represent those gaps as solved.
