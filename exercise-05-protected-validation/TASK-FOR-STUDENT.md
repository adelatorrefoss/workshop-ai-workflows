# Student task — Strengthen a protected feedback channel

## Your task

Improve the registration test cases so that each business rule is proved independently and every supplied behavioral mutant is detected.

The production validator already contains the intended rules. Your work is to strengthen the focused cases in `Checks/RegistrationCases.cs`, not to change the business behavior or mutation mechanism.

## What to do

1. Run `make test` and confirm that the two broad cases pass.
2. Run `make mutation-test` and capture the intentional `MUTATION FAILURE` showing three surviving mutants.
3. Launch Codex and paste `prompts/strengthen.md`.
4. Let Codex add isolated cases for required name, email syntax, and allowed course behavior.
5. Review why each new case fails for one removed rule while keeping the other input fields valid.
6. Run `make validate`.

## Constraints

- Do not edit `MutationCheck/Program.cs` or the production validator.
- Do not change Make targets, skip checks, lower requirements, or weaken assertions.
- Use at most three repair attempts.

## Done when

- The normal test suite passes.
- The mutation check reports that every supplied mutant is killed.
- `make validate` passes.
- You can name the focused case that independently protects each validation rule.
