# Exercise 1 — Turn an ad-hoc request into a workflow

Compare asking only for code with prescribing how the agent should work.

## Starting state

`make validate` passes. The application serves `GET /users`; it does not expose a health endpoint.

## Part A — Ad-hoc

Start from a clean copy or branch, launch Codex, and paste:

```text
Add a health check endpoint to this application.
```

Record files changed, tests added, and validation performed.

## Part B — Structured

Restore the starting state on a new branch, launch Codex, and paste `prompts/structured.md`. Approve the plan when Codex pauses.

Compare consistency, unnecessary changes, coverage, validation, and human intervention. The endpoint should be `GET /health`, return HTTP 200, and produce `{"status": "ok"}`.

