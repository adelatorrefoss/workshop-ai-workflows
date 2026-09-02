# Exercise 3 — Introduce executable feedback

A candidate preferences feature works functionally but violates the required dependency direction.

## Starting state

`make test` passes and `make architecture-test` fails intentionally. The controller must depend on an application service, which may depend on the repository.

## Run

Launch Codex and paste `prompts/implement.md`. Let the machine-readable architecture feedback guide the refactor, then inspect the resulting dependency flow.

