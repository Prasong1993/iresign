# Blacklist and Change Control

Purpose: preserve explicit prohibitions, authorization boundaries, and approval history.

Current controls:
- No baseline/source-of-truth selection without explicit approval.
- No source repository modifications, source merge, release changes, or deployment.
- No full Project Control API database import/migration at this stage.
- No copying secrets, credentials, or production data into the evidence repository.
- No runtime, dependency installation, failure injection, or penetration testing without separate authorization.
- No claim of completion without direct evidence and read-back.
- Preserve the existing TickTick checkpoint NIR-P0-004; do not create a replacement checkpoint.

Record authorizing instruction, exact scope, timestamp if captured, action, and verification. This README is a summary; source checkpoint text remains the controlling evidence.