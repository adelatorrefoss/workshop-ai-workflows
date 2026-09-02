# GitHub CI feedback loop

Follow the issue-to-PR workflow, then inspect checks with `gh pr checks --watch`. If CI fails, inspect the failing GitHub Actions log, identify the engineering cause, fix it locally, run relevant validation, commit, and push. Repeat for at most three CI runs. Never delete or skip tests, disable jobs, edit checks only to evade a failure, or lower a threshold. Stop before merge and report every meaningful correction, all check results, and any blocker.

