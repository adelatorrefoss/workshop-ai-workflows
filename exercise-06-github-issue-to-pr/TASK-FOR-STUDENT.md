# Student task — Deliver a GitHub Issue as a pull request

## Your task

Give Codex a GitHub Issue as its unit of work and let it take the registration-validation feature from issue reading through a reviewable pull request. The pull request must remain unmerged.

## Prepare the exercise

1. Copy this exercise directory so that it becomes the root of a new repository.
2. Confirm that `gh auth status` succeeds.
3. Initialize Git, commit the starter, create and push a private GitHub repository, and create an issue from `.github/ISSUE_TEMPLATE/registration-validation.md` using the commands in `README.md`.
4. Run `make validate` and confirm that the starter is green.

## What to do

1. Note the new issue number.
2. Launch Codex and paste `prompts/issue-to-pr.md`, replacing `<issue-number>` with the real number.
3. Review the plan, branch name, implementation, automated checks, and local validation evidence produced by Codex.
4. Let Codex commit, push, and open the pull request.
5. Inspect the resulting pull request as the human reviewer.

## Constraints

- The issue acceptance criteria define the scope.
- Do not expose credentials or rewrite shared history.
- Do not weaken validation.
- Do not merge the pull request.

## Done when

- Invalid registrations return HTTP 400 and are not persisted; valid registrations still return HTTP 201 and are saved.
- Focused automated checks cover the issue criteria and `make validate` passes.
- The branch and commit are focused, and the pull request body contains `Closes #<issue-number>`.
- The pull request is pushed, linked to the issue, ready for human review, and still unmerged.
- You can identify the decisions that still require human review.
