# Exercise 4 — Close the loop

The pricing implementation contains a defect. Codex receives permission to run a bounded implement–validate–repair loop without waiting for a human between attempts.

## Starting state

`make validate` fails one focused test intentionally.

## Run

Launch Codex and paste `prompts/autonomous.md`. Observe whether it finds the underlying business-rule error, respects the three-attempt limit, and reports its corrections.

