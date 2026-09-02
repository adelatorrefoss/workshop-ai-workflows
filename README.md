# Auto Content — From Workflow to Autonomous Loop

Seven hands-on Codex exercises that progressively turn a small coding task into a bounded autonomous workflow with executable feedback and GitHub CI.

## How to use this repository

Each exercise is self-contained. Enter its directory, read its `README.md`, start Codex, and paste the prompt shown there.

```bash
cd exercise-01-workflow
codex
```

Exercises 1–5 run locally with Python 3 and Make. Exercises 6–7 additionally require Git, GitHub CLI (`gh`), a GitHub account, and a remote repository. No Python packages are required.

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

