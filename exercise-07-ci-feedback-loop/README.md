# Exercise 7 — GitHub becomes part of the feedback loop

The .NET registration storage formatter passes local checks, while CI enforces a broader normalization contract.

Make this folder a standalone GitHub repository, push the starter state, and create the supplied issue. `make validate` is green; `make ci-validate` is intentionally red. Learners should encounter the additional contract through GitHub Actions.

Launch Codex with `prompts/ci-loop.md`. It may repair and push failed CI at most three times and must stop before merge.
