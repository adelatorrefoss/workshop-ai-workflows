# Student task — Observe a bounded autonomous repair loop

## Your task

Let Codex diagnose and repair the intentionally failing registration contract without relaying failures or suggesting fixes between attempts.

Complete registrations for both `Introduction` and `Advanced` must be accepted. Blank names, malformed emails, and unknown courses must be rejected.

## What to do

1. Run `make validate` and capture the intentional `VALIDATION FAILURE` for the Advanced-course case.
2. Launch Codex and paste `prompts/autonomous.md`.
3. Do not coach Codex between validation attempts.
4. Observe and record each validation attempt, the feedback it received, and the correction it made.
5. Confirm that it stops after success or after at most three total attempts.

## Constraints

- Do not manually relay the error or propose a code change.
- Do not allow checks to be edited, skipped, weakened, or bypassed.
- Do not allow the `Advanced` course to be removed from the valid contract.

## Done when

- `make validate` passes within three attempts, or Codex stops and clearly reports the unresolved blocker after the third failure.
- If green, all valid and invalid registration cases still behave as specified.
- You can explain how executable feedback drove the correction and what risk the attempt limit controlled.
