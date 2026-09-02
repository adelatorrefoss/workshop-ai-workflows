# Exercise 6 — From local loop to GitHub

Turn a GitHub Issue into a branch, validated implementation, semantic commit, and pull request.

## One-time setup

Make this directory the root of a new GitHub repository (copy it outside this course repository if necessary), push the green starter state, and create an issue using `.github/ISSUE_TEMPLATE/product-filter.md`. Install and authenticate GitHub CLI with `gh auth status`.

## Starting state

`make validate` passes. Category filtering has not been implemented.

## Run

Launch Codex and paste `prompts/issue-to-pr.md`, replacing `<issue-number>`. Codex may create a branch, commit, push, and open a PR, but it must stop before merge for human review.

