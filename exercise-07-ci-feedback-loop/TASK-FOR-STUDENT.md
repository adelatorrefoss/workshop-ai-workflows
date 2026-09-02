# Student challenge — Use CI feedback to complete a feature

Implement the storage-safety GitHub Issue: registration fields containing tabs, carriage returns, or newlines must be rejected, while ordinary values, trimming, and tab-separated storage remain supported. Add focused local checks.

After opening the pull request, let the agent discover the additional canonical-email requirement from the failing CI log. It must repair the engineering cause and add local protection for the newly discovered behavior rather than silencing the remote check.

Reach green local validation and green CI within three CI runs. Record each failure, its cause, and its correction. The issue-linked pull request must remain unmerged for human review.
