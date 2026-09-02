# Student task — Reuse a repository-defined workflow

## Your task

Run two different feature requests and verify that Codex follows the same development workflow because the reusable instructions live in `AGENTS.md`, not in either prompt.

## What to do

1. Run `make validate` and read `AGENTS.md`.
2. Create two clean branches from the same starter commit.
3. On the first branch, launch Codex and paste `prompts/feature-a.md` to add the health endpoint.
4. Inspect and approve the plan, let Codex implement the feature, and record its validation evidence.
5. Return to the untouched starter state on the second branch.
6. Launch Codex and paste `prompts/feature-b.md` to add registration validation.
7. Inspect and approve the plan, let Codex implement the feature, and record its validation evidence.
8. Compare the phases followed in both runs with the rules in `AGENTS.md`.

## Constraints

- Do not copy the workflow rules into the feature prompts.
- Keep the two implementations on independent branches.
- Do not weaken validation or expand either feature beyond its prompt.

## Done when

- Feature A returns HTTP 200 and `{"status":"ok"}` from `GET /api/health` and has focused automated validation.
- Feature B rejects invalid registrations with HTTP 400, does not persist them, preserves valid registrations, and has focused automated validation.
- `make validate` passes on each branch.
- You can identify which instructions belong to an individual task and which belong to the reusable repository harness.
