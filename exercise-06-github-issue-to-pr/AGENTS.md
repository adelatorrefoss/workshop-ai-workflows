# Issue-to-PR workflow

1. Use `gh issue view <number>` and treat its acceptance criteria as scope.
2. Inspect repository conventions and write a short plan.
3. Create a feature branch named `exercise/<issue-number>-short-name`.
4. Implement focused code and tests without unrelated changes.
5. Run `make validate`; repair failures without weakening checks.
6. Review the diff, commit semantically, push the branch, and open a PR linked with `Closes #<number>`.
7. Report the PR URL and validation results. Never merge the PR; human review is required.

Do not expose tokens, rewrite shared history, or alter acceptance criteria.

