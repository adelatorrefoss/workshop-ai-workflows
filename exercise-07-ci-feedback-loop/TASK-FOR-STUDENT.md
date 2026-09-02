# Student task — Let CI close the remote feedback loop

## Your task

Use a GitHub Actions failure as feedback that Codex must inspect and repair itself. The feature must reach green CI within three CI runs and the pull request must remain unmerged.

## Prepare the exercise

1. Copy this exercise directory so that it becomes the root of a new repository.
2. Initialize, commit, create, and push a private GitHub repository as described in Exercise 6.
3. Create an issue from `.github/ISSUE_TEMPLATE/normalize-registration.md` and note its number.
4. Confirm that Actions is enabled and `gh auth status` succeeds.
5. Run `make validate` and confirm that local validation is green. Do not run `make ci-validate` before the exercise; the remote policy is meant to arrive through CI feedback.

## What to do

1. Launch Codex and paste `prompts/ci-loop.md`, replacing `<issue-number>` with the real number.
2. Let Codex implement the issue, validate locally, commit, push, and open a pull request.
3. Do not manually relay the CI error. Let Codex watch the checks, inspect the failing Actions log, diagnose the engineering cause, and repair it locally.
4. Observe and record each CI run and corresponding correction.
5. Inspect the final pull request as the human reviewer.

## Constraints

- Use at most three CI runs.
- Do not delete or skip checks, weaken assertions, or alter workflow commands to evade failure.
- Stop before merge even when CI is green.

## Done when

- Local validation and the full GitHub Actions workflow are green within three CI runs, or Codex stops after the third failure and reports the blocker.
- The implementation rejects unsafe stored fields while preserving trimming and tab-separated storage.
- The remote canonical-email policy is satisfied for the engineering reason revealed by CI.
- The pull request links the issue, reports the corrections and exact results, and remains unmerged.
- You can explain what remote feedback added beyond the local checks.
