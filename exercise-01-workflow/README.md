# Exercise 1 — Turn an ad-hoc request into a workflow

This .NET 10 interest-registration application mirrors the Codesai Context Management example. Compare asking only for code with prescribing how Codex should work.

## Starting state

`make validate` passes. `POST /api/register` saves `Name`, `Email`, and `Course` to `interests.txt`. There is no health endpoint.

## Part A — Ad-hoc

On a clean branch, launch Codex and ask: `Add a health check endpoint to this application.` Record the changes and validation.

## Part B — Structured

Return to the starter commit on another branch and paste `prompts/structured.md`. Approve the plan when Codex pauses. Compare scope, ASP.NET consistency, tests, validation, and human intervention.
