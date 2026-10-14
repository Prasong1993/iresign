# IRIS Control v0.6.18 — Runtime Event Ordering Fix

- Fixes latest-event readback to use SQLite insertion order when multiple events share the same second-resolution timestamp.
- Adds a regression assertion that the latest inserted event is returned.
- Retains v0.6.17 runtime telemetry, additive schema, skill rules, and plugin identity.
- ChatGPT-host MCP handshake remains NOT RUN because the MCP Python dependency is unavailable in this local test environment.
