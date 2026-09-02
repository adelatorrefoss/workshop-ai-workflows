# Troubleshooting

## Requirements

Local exercises require the .NET 10 SDK and Make. Confirm with:

```bash
dotnet --version
make --version
```

GitHub exercises also require GitHub CLI:

```bash
gh --version
gh auth status
```

Exercise 8 requires Git locally but no GitHub account, remote, or `gh` authentication.

## An exercise starts red

This is expected in Exercises 3, 4, and 5. Exercise 7 passes `make validate` but fails the broader `make ci-validate`. The root `make check` verifies these deliberate .NET failures by their diagnostic messages.

## The wrong .NET SDK is selected

Each project targets `net10.0`. Ensure `dotnet --version` reports a 10.x SDK. If your environment pins another version through `global.json`, run the lab in an environment with .NET 10 installed.

## GitHub does not see the workflow or templates

The exercise directory must be the root of its own GitHub repository. If it remains a subdirectory of this course repository, GitHub will not treat its nested `.github` directory as repository configuration.

## Codex sees instructions from the parent repository

The root `AGENTS.md` provides safety defaults and the exercise-level `AGENTS.md` adds the local workflow. When running an exercise copied into its own repository, only its local instructions apply.

## CI does not start

Check that Actions is enabled, the workflow exists at `.github/workflows/validate.yml` on the pushed branch, and a pull request is open. Use `gh pr checks` to inspect check discovery.

## Authentication or permissions fail

Run `gh auth status`. Ensure the authenticated account can push branches and open pull requests in the repository. Never paste a token into a prompt or commit it to a file.

## Recover a clean exercise

Prefer creating a new branch from the starter commit or making a fresh copy. Avoid weakening validation or modifying the starter branch merely to recover from an experiment.

## The Dark Factory preflight fails

Exercise 8 must be copied into a standalone Git repository. Confirm that its directory is the value of `git rev-parse --show-toplevel`, the current branch is `main`, the working tree is clean, and `dark-factory-start` points to the initial commit. If the factory stopped midway, preserve the run log and feature branch for diagnosis; start from a fresh copy for a new classroom run rather than rewriting the failed evidence.

## The Dark Factory audit reports invalid history

The audit expects only ordered first-parent merge commits after `dark-factory-start`, each with two parents and a subject such as `Merge issue #003: Add course filtering`. A squash, fast-forward, out-of-order issue, direct commit on `main`, nested merge, changed harness file, dirty tree, or missing run-log evidence causes a deliberate failure.
