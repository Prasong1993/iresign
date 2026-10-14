# File Inventory and Architecture

Purpose: account for every in-scope file at an exact source commit, then map entry points, symbols, dependencies, and data flow.

Required inventory columns: source group, repository URL, branch/ref, commit SHA, source path, file type/size where available, role, source blob SHA, destination path/blob SHA, evidence status, limitations, and read-back status.

Do not mark the inventory complete until all in-scope paths are accounted for. Keep generated artifacts, tests, docs, manifests, workflows, and source code distinguishable. No code execution is implied by inventory or source review.