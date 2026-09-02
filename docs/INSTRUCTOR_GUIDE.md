# Instructor guide

## Intended audience

This lab belongs to **Module 7 — Workflows** in **Codesai Training: Advanced AI-Assisted Development**. Learners should already know prompting, context management, evaluation, source control, and the purpose of MCP integrations.

## Suggested delivery

Exercises 1–4 form the essential progression and work well in one session. Exercise 5 makes the safety implication explicit. Exercises 6–7 are a capstone that require GitHub access and are best prepared before class.

| Exercise | Focus | Initial validation | Suggested time |
| --- | --- | --- | --- |
| 1 | Ad-hoc versus phased work | Green | 25 min |
| 2 | Repository-encoded workflow | Green | 25 min |
| 3 | Executable architecture feedback | Intentionally red | 25 min |
| 4 | Bounded local repair loop | Intentionally red | 20 min |
| 5 | Protected feedback channels | Intentionally red | 20 min |
| 6 | Issue-to-PR autonomy | Green | 35 min |
| 7 | CI as agent feedback | Local green, CI intentionally red | 40 min |

## Reset strategy

Use a fresh Git branch for each run. Exercise 1 needs two branches from the same starter commit so learners can compare ad-hoc and structured outcomes. Exercise 2 likewise needs independent branches for Features A and B. Do not solve exercises on `main`; its deliberate start states are part of the material.

For Exercises 6–7, copy the selected exercise into its own repository so that its `.github` directory is at the repository root. Create the supplied issue only after pushing the starter commit.

## What to observe

- Did the agent research conventions before editing?
- Did the plan constrain scope in a useful way?
- Did executable feedback cause a design correction rather than a workaround?
- Did the agent distinguish a product failure from an environment failure?
- Did it respect the three-attempt boundary?
- Did it preserve tests, architecture checks, and CI configuration?
- Did the GitHub agent stop before merge and provide evidence for human review?

## Debrief

Ask learners to place each instruction in one of three locations: task prompt, repository harness, or executable validation. Then ask which location makes the instruction most reusable and least ambiguous. Close by identifying the remaining human responsibility: designing constraints, reviewing risk, and validating outcomes.

## Scaffold verification

Run `make check` from the repository root. A passing scaffold check includes expected failures inside Exercises 3–5 and 7; the script verifies that each failure occurs for its intended teaching reason.

