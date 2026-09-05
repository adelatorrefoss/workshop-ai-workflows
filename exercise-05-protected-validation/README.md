# Exercise 5 — Protect the feedback channel

## Learning goal

See why feedback mechanisms must be protected from shortcuts and why one test case should isolate one business rule.

## Starting state

Run `make test` and see two broad registration cases pass. Run `make mutation-test` and see three surviving behavioral mutants: removal of name, email, or course validation.

## Run

Launch `copilot` and paste `prompts/strengthen.md`. Shared cases live in `Checks/RegistrationCases.cs`; the mutation runner executes altered validator behaviors against the same cases.

## Success and reflection

`make validate` should pass because focused cases kill every mutant—not because the runner or Makefile changed. Which new case proves each validation rule independently?
