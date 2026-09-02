# Module 7 — Workflows

This repository contains the practical work for **Module 7 — Workflows** from **Codesai Training: Advanced AI-Assisted Development**.

The module explores how to move from an ad-hoc AI coding interaction to a repeatable, bounded autonomous loop. Across seven hands-on Codex exercises, learners progressively combine repository research, explicit planning, implementation rules, executable feedback, local repair loops, GitHub Issues, pull requests, and CI.

All exercises use the same technology and business context as the Codesai `ContextManagement` example: an **ASP.NET Core application targeting .NET 10** where learners submit interest registrations containing a name, email, and course. The API persists registrations to `interests.txt` and is paired with a small HTML/JavaScript form.

The central lesson is that effective autonomy comes from engineering the agent's operating environment: its workflow, constraints, validation mechanisms, and feedback channels.

## How to use this repository

Each exercise is self-contained. Enter its directory, read its `README.md`, start Codex, and paste the prompt shown there.

```bash
cd exercise-01-workflow
codex
```

Exercises 1–5 run locally with the .NET 10 SDK and Make. Exercises 6–7 additionally require Git, GitHub CLI (`gh`), a GitHub account, and a remote repository.

The starting state is intentionally not always green. Some exercises teach the agent to discover and repair a failed test or architecture rule. Each exercise documents its expected initial state.

## Learning path

1. Compare an ad-hoc request with a structured workflow.
2. Encode the workflow in the repository.
3. Add executable architectural feedback.
4. Close the feedback loop with a strict iteration limit.
5. Protect validation from shortcut-driven changes.
6. Turn a GitHub Issue into a pull request.
7. Use CI failures as another feedback channel.

Run the repository-level scaffold check with:

```bash
make check
```

## Safety

The autonomous prompts limit scope and iteration count. They prohibit weakening tests, lint rules, architecture checks, and coverage thresholds. GitHub exercises stop before merging: a human remains the final reviewer.

## Teaching support

- [Instructor guide](docs/INSTRUCTOR_GUIDE.md) explains timing, resets, observations, and debrief questions.
- [Troubleshooting](docs/TROUBLESHOOTING.md) covers local requirements and GitHub exercise setup.
