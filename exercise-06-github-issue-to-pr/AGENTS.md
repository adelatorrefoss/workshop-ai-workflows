# Issue-to-PR workflow

1. Read the issue with `gh issue view <number>` and use its acceptance criteria as scope.
2. Inspect the ASP.NET Core registration patterns and write a short plan.
3. Create `exercise/<issue-number>-short-name`.
4. Implement focused code and executable validation.
5. Run `make validate`; never weaken checks.
6. Review the diff, create a semantic commit, push, and open a PR containing `Closes #<number>`.
7. Report the PR URL and exact results. Never merge; human review is required.

Never expose tokens or rewrite shared history.
