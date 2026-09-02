# Instructor guide

## Intended audience

This lab belongs to **Module 7 — Workflows** in **Codesai Training: Advanced AI-Assisted Development**. Learners should already know prompting, context management, evaluation, source control, and the purpose of MCP integrations.

Every exercise deliberately stays in the same context as the earlier Codesai `ContextManagement` example: a .NET 10 ASP.NET Core interest-registration application with `Name`, `Email`, `Course`, file persistence, and a small browser form. The domain remains familiar while the agent harness becomes progressively more autonomous.

## Suggested delivery

Exercises 1–4 form the essential progression and work well in one session. Exercise 5 makes the safety implication explicit. Exercises 6–7 form a GitHub capstone and are best prepared before class. Exercise 8 is a longer local capstone in which Git history and the repository harness replace pull-request oversight.

| Exercise | Focus | Initial validation | Suggested time |
| --- | --- | --- | --- |
| 1 | Ad-hoc versus phased .NET work | Green | 25 min |
| 2 | Repository-encoded workflow | Green | 25 min |
| 3 | Executable architecture feedback | Intentionally red | 25 min |
| 4 | Bounded local repair loop | Intentionally red | 20 min |
| 5 | Protected feedback channels | Intentionally red | 20 min |
| 6 | Issue-to-PR autonomy | Green | 35 min |
| 7 | CI as agent feedback | Local green, CI intentionally red | 40 min |
| 8 | Bounded local Dark Factory | Green | 60 min |

## Reset strategy

Use a fresh Git branch for each run. Exercise 1 needs two branches from the same starter commit so learners can compare ad-hoc and structured outcomes. Exercise 2 likewise needs independent branches for Features A and B. Do not solve exercises on `main`; its deliberate start states are part of the material.

For Exercises 6–7, copy the selected .NET project into its own repository so that its `.github` directory is at the repository root. Create the supplied registration issue only after pushing the starter commit.

For Exercise 8, copy the directory into its own local repository, commit the starter on `main`, add the `dark-factory-start` tag, and run `make factory-preflight`. Do not add a remote. A fresh copy is the simplest reset because the exercise intentionally creates up to ten branches and merge commits.

## What to observe

- Did the agent research conventions before editing?
- Did the plan constrain scope in a useful way?
- Did executable feedback cause a design correction rather than a workaround?
- Did the agent distinguish a product failure from an environment failure?
- Did it respect the three-attempt boundary?
- Did it preserve tests, architecture checks, and CI configuration?
- Did the GitHub agent stop before merge and provide evidence for human review?
- Did the Dark Factory use one current-main feature branch per issue and merge only green, independently reviewed work?
- Does the run log agree with the ordered `--no-ff` history, including bounded fix rounds and any stop condition?

## Debrief

Ask learners to place each instruction in one of three locations: task prompt, repository harness, or executable validation. Then ask which location makes the instruction most reusable and least ambiguous. Compare the human-controlled GitHub merge in Exercises 6–7 with the constrained local merges in Exercise 8. Close by identifying the remaining human responsibility: designing constraints, reviewing risk, and validating outcomes.

## Scaffold verification

Run `make check` from the repository root. A passing scaffold check includes expected failures inside Exercises 3–5 and 7; the script verifies that each failure occurs for its intended teaching reason.
