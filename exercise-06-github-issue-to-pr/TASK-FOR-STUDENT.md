# Student challenge — Deliver an issue as a pull request

Implement the registration-validation GitHub Issue from acceptance criteria through an unmerged pull request.

The change must reject missing names and courses after trimming, reject emails without exactly one `@` and text on both sides, return HTTP 400 without persistence for invalid input, and preserve HTTP 201 with persistence for valid input. Add focused executable checks for the complete behavior.

Direct the agent through issue analysis, planning, implementation, validation, semantic commit, push, and PR creation. Review the code and tests yourself. The PR must link the issue with `Closes #<issue-number>`, contain evidence of green validation, and remain unmerged for human approval.
