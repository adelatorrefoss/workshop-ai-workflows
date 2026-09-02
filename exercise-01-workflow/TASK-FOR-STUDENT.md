# Student task — Compare an ad-hoc request with a structured workflow

## Your task

Implement the same health endpoint twice from the same starter state and compare how the working process affects the result.

The endpoint must respond to `GET /api/health` with HTTP 200 and the JSON body `{"status":"ok"}`. Existing registration behavior must continue to work.

## What to do

1. Run `make validate` and confirm that the starter is green.
2. Create two branches from the same starter commit: one for the ad-hoc run and one for the structured run.
3. On the first branch, launch Codex and ask only: `Add a health check endpoint to this application.`
4. Record the files changed, checks added, commands run, and final validation result.
5. On the second branch, launch Codex and paste `prompts/structured.md`.
6. Review the proposed plan when Codex pauses. Approve it only if it is focused and preserves registration behavior.
7. Record the same evidence for this second run and compare both outcomes.

## Constraints

- Do not give the ad-hoc run extra workflow instructions.
- Keep both runs independent and based on the same commit.
- Do not remove or bypass existing behavior or validation.

## Done when

- Both branches provide the required health response.
- `make validate` passes on both branches.
- You can explain which differences came from research, planning, testing, and validation rather than from the feature itself.
