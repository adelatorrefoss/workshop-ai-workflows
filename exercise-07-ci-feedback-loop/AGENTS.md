# GitHub CI feedback loop

Implement the issue and validate locally, then open a PR and watch `gh pr checks --watch`. On failure, inspect Actions logs, repair the engineering cause locally, commit, and push. Use at most three CI runs. Never delete or skip checks, weaken assertions, or alter workflow commands to evade failure. Stop before merge and report every correction and result.
