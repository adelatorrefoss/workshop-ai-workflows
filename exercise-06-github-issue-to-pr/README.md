# Exercise 6 — From local loop to GitHub

## Learning goal

Treat a GitHub Issue for the .NET registration API as an executable unit of work while moving human oversight from individual edits to pull-request review.

## Setup

Copy this folder so it becomes the root of a new repository; GitHub does not recognize its `.github` configuration while nested in the course repository. Confirm `gh auth status`, then run:

```bash
git init
git add .
git commit -m "chore: add exercise starter"
gh repo create <owner>/<repository> --private --source=. --push
gh issue create --template registration-validation.md
make validate
```

The green starter endpoint saves every payload without validation.

## Run

Launch `codex` and paste `prompts/issue-to-pr.md`, replacing `<issue-number>`. Codex may branch, commit, push, and open a PR, but must stop before merge.

## Success and reflection

The PR should link the issue, cover every criterion, show green validation, and remain unmerged. Which choices still require human review?
