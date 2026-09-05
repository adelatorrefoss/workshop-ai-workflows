# Exercise 4 — Close the loop

## Learning goal

Allow Copilot to consume feedback and correct its work without asking a human to relay each failure, while enforcing a strict stopping boundary.

## Starting state

Run `make validate`. The contract accepts complete registrations for both offered courses and rejects blank names, malformed emails, and unknown courses. Only the Advanced-course case fails intentionally.

## Run

Launch `copilot` and paste `prompts/autonomous.md`. Do not coach it between attempts; record how it interprets feedback and whether it respects the three-attempt limit.

## Success and reflection

The final `make validate` should be green without modified or bypassed checks. Did the agent repair the business rule or optimize only for the visible example? What did the limit protect?
