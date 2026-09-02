# Exercise 2 — Crystallize the workflow

The .NET 10 registration application now tells Codex how features should be developed through `AGENTS.md`.

## Learning goal

Move reusable process instructions out of repeated prompts and into the repository's engineering environment.

## Before you start

Run `make validate`, read `AGENTS.md`, and create one clean branch per feature.

## Run

1. Launch `codex` and paste `prompts/feature-a.md`; approve its plan and inspect the result.
2. Return to the starter state on another branch.
3. Launch `codex` and paste `prompts/feature-b.md`; approve its plan and inspect the result.

Feature A adds an operational endpoint. Feature B adds registration validation.

## Success and reflection

Both runs should follow the same phases and finish with validation evidence even though the prompts do not repeat those rules. Which instructions belong to a task, and which belong to the reusable harness?
