# Exercise 3 — Introduce executable feedback

A candidate .NET registration endpoint builds but violates the required dependency direction.

## Learning goal

Experience an architecture rule as executable, machine-readable feedback rather than prose the agent can overlook.

## Starting state

Run `make build` and see it pass. Then run `make architecture-test` and see the intentional `ARCHITECTURE FAILURE`: the controller directly creates file persistence.

## Run

Launch `copilot` and paste `prompts/implement.md`. Let the failure guide the refactor.

## Success and reflection

`make validate` should pass with the flow `controller → application service → repository interface → file repository`. Registration behavior must remain intact. Was the executable rule clearer than another paragraph of instructions?
