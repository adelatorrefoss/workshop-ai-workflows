# Troubleshooting

## Requirements

Local exercises require Python 3.10 or newer and Make. Confirm with:

```bash
python3 --version
make --version
```

GitHub exercises also require GitHub CLI:

```bash
gh --version
gh auth status
```

## An exercise starts red

This is expected in Exercises 3, 4, and 5. Exercise 7 passes `make validate` but fails the broader `make ci-validate`. Read the exercise README before trying to repair anything.

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

