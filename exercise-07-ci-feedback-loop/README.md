# Exercise 7 — GitHub becomes part of the feedback loop

## Learning goal

Make GitHub Actions another feedback channel the agent can inspect and act on within a bounded loop.

## Setup

Copy this folder to the root of a new repository, initialize and push it as in Exercise 6, then create the `normalize-registration.md` issue. Confirm Actions is enabled and `gh auth status` succeeds. The issue requests storage-safety validation, giving the agent a concrete local change to implement.

## Starting state

`make validate` is green for the starter formatter: surrounding whitespace is trimmed and tab-separated storage is preserved. After the issue is implemented locally, CI also enforces an organization-wide canonical-email policy absent from local checks. `make ci-validate` exposes that policy and is intentionally red, but learners should encounter it through the PR check.

## Run

Launch `codex` with `prompts/ci-loop.md`, replacing `<issue-number>`. Let it open the PR, watch checks, inspect the failing log, and repair the cause. Do not relay the error manually.

## Success and reflection

The agent should reach green CI within three runs without weakening a check, then stop before merge. How did remote feedback change the implementation? What should happen if the third run is still red?
