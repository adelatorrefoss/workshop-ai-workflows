# Student challenge — Deliver ten issues through a bounded Dark Factory

Operate the local Dark Factory so that it implements the ten cumulative issues in `.dark-factory/issues/` without per-issue human coaching.

Each issue must be developed on its own current-main feature branch and receive research, planning, implementation, authoritative validation, independent review, bounded repair, rebase validation, and an explicit non-fast-forward merge. Failed work must never be merged, later issues must not continue after a stop condition, and the immutable issue queue and protected harness must not be weakened.

A normal result is a clean, green `main` with ten ordered merge commits, visible feature ancestry, matching evidence in `.dark-factory/run-log.md`, and a passing factory audit. A bounded stop is also valid when it preserves the active branch, evidence, and exact stop reason without merging failed work.

Submit an operator assessment explaining whether the Git graph, run log, validation, independent review, and iteration limits made the autonomous delivery safe and auditable.
