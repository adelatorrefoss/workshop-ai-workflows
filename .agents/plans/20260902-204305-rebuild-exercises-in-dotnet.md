# Plan: rebuild Module 7 exercises in .NET

## Correction

The first implementation chose Python and a product-catalog domain without confirming the course technology. Rebuild every exercise to match the `development-with-AI/ContextManagement` reference application.

## Reference baseline

- ASP.NET Core Web API targeting `net10.0`.
- Interest-registration domain with `Name`, `Email`, and `Course`.
- `POST /api/register` endpoint.
- File-backed persistence to `interests.txt`.
- Small HTML/JavaScript registration form.
- Docker support where it helps learners run the application.

## Steps and semantic commits

1. `docs: plan dotnet exercise rebuild`
   - Record the correction and align root documentation with the reference application.
2. `refactor: rebuild workflow exercises in dotnet`
   - Replace Exercises 1–2 with .NET interest-registration scenarios for ad-hoc and crystallized workflows.
3. `refactor: rebuild feedback exercises in dotnet`
   - Replace Exercises 3–5 with executable architecture, bounded repair, and protected-test feedback around registration behavior.
4. `refactor: rebuild github exercises in dotnet`
   - Replace Exercises 6–7 with issue-to-PR and CI loops for the registration application.
5. `test: verify dotnet course scaffold`
   - Replace the Python scaffold verifier with .NET build and expected-state checks.
6. `docs: finalize dotnet teaching guidance`
   - Update instructor and troubleshooting guidance, run all verification, and audit the repository.

## Constraints

- Keep each exercise self-contained and launchable from its own directory.
- Avoid third-party test packages so the lab can build from the installed .NET SDK without extra teaching dependencies.
- Preserve intentional red states and identify their expected diagnostic precisely.
- Never weaken validation to simulate success.

