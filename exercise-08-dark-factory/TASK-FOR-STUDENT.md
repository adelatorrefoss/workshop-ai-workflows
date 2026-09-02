# Student task — Run and audit a bounded local Dark Factory

## Your task

Run the supplied autonomous local workflow over the immutable queue of ten issues. Observe whether it isolates work, validates it, obtains an independent review, repairs findings within its limits, and integrates only qualifying changes.

This exercise tests the factory workflow. Do not manually implement the queued product features or coach the factory between issues.

## Prepare the exercise

1. Copy this directory outside the course repository and initialize the copy exactly as shown in `README.md`.
2. Commit the starter on `main`, create the `dark-factory-start` tag, and do not configure a remote.
3. Run `make factory-preflight` and stop if the baseline is not ready.
4. Read `AGENTS.md`, `.dark-factory/config`, the issue queue, and the empty run log before starting.

## What to do

1. Launch Codex from the copied repository and paste `prompts/dark-factory.md`.
2. Do not approve individual issues or coach any role while the factory runs.
3. Observe progress from another terminal with:

   ```bash
   git log --graph --oneline --decorate --all
   sed -n '1,240p' .dark-factory/run-log.md
   ```

4. Let the factory finish when the queue is empty, ten issues have been attempted, or a documented stop condition occurs.
5. After a normal ten-issue completion, run `make factory-audit`. For a stopped run, inspect the retained feature branch and run log instead; a stopped run is not expected to pass the completion audit.

## Constraints

- Work must occur on one `feature/issue-NNN` branch at a time, based on the latest `main`.
- Do not edit the issue files or weaken any validation, review, history, or audit mechanism.
- Each issue may use at most two fix rounds.
- Do not intervene to resolve a meaningful product or architecture decision.
- Do not add a GitHub remote or replace the local workflow with pull requests.

## Done when

For a normal completion:

- `main` is clean and `make validate` passes.
- All ten issues were integrated in order with exactly ten explicit `--no-ff` merge commits and visible feature ancestry.
- Every merge has matching validation, independent-review, rebase, feature-tip, and merge evidence in `.dark-factory/run-log.md`.
- `make factory-audit` passes.

For a bounded stop:

- No failed work was merged and no later issue was attempted.
- The active feature branch and run log retain the failure evidence and stop reason.
- Codex reports the attempted, merged, failed, validation-failure, review-finding, and fix-round counts.

In either case, be ready to explain which executable constraints made the autonomous workflow safe and observable.
