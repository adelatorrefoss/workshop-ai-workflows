# Exercise 7 — GitHub becomes part of the feedback loop

Local validation is deliberately narrower than CI. The agent must consume GitHub Actions feedback, repair the implementation, and push again within a bounded loop.

## One-time setup

Make this directory the root of a new GitHub repository, push the starter state, and create an issue from `.github/ISSUE_TEMPLATE/ci-loop.md`. Ensure GitHub Actions is enabled and `gh auth status` succeeds.

## Starting state

`make validate` passes. `make ci-validate` fails one contract test intentionally; students should discover that detail through CI rather than running the CI-only command first.

## Run

Launch Codex and paste `prompts/ci-loop.md`, replacing `<issue-number>`. The agent may fix and push failed CI at most three times. It must never weaken feedback or merge the PR.

