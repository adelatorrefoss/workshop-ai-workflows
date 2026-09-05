# Plan: build the autonomous workflow lab

## Objective

Create this repository as a classroom-ready project containing seven progressively autonomous Copilot exercises based on Module 7.

## Design decisions

- Use .NET 10 and avoid third-party packages so setup is immediate and aligned with the course reference application.
- Give every exercise its own application, tests, README, `AGENTS.md`, Makefile, and reusable prompts.
- Keep the domain consistent while snapshotting each autonomy stage into a separate directory.
- Mark deliberate red states clearly; a root-level scaffold check validates teaching materials without solving student tasks.
- Keep GitHub actions safe: prepare issues, workflows, and helper checks, but never merge automatically.

## Implementation steps and commits

1. `docs: define autonomous workflow lab`
   - Add the root README, concise root agent guidance, and this plan.
2. `feat: add workflow foundation exercises`
   - Build Exercises 1 and 2 for ad-hoc versus structured work and crystallized repository guidance.
3. `feat: add executable feedback exercises`
   - Build Exercises 3, 4, and 5 with architecture feedback, a bounded repair loop, and protected validation.
4. `feat: add github autonomy exercises`
   - Build Exercises 6 and 7 with issue templates, PR instructions, local checks, and layered GitHub Actions feedback.
5. `test: add course scaffold verification`
   - Add a root check that verifies required files, commands, guardrails, prompts, and expected exercise states.
6. `docs: finalize instructor and learner guidance`
   - Add an instructor guide, troubleshooting notes, and verify the complete repository.

## Verification

- Run `make check` at the repository root.
- Run green baseline validations where expected.
- Confirm deliberately failing exercises fail for their documented pedagogical reason.
- Inspect Git history for one semantic commit per meaningful step.
