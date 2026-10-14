# Tests, CI, and Runtime Evidence

Purpose: map test files and CI runs to the exact source commit they exercise, and keep test, CI, runtime, integration, and operational evidence separate.

Every test/CI entry must include test or workflow name, run ID/URL, result, branch/ref, exact commit SHA, relevant source paths, timestamp if available, and limitations. A workflow file is not a run. A run on another commit is not evidence for the target commit. Reading tests is not executing them.

Current status: test-to-source mapping incomplete; target-SHA CI status must be freshly retrieved; runtime/integration/failure-injection remain NOT RUN unless directly executed under separate authorization.