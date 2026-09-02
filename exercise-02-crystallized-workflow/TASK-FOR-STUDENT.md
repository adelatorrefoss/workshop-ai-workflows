# Student challenge — Make a workflow reusable

Improve `AGENTS.md` so it defines a reusable feature-development workflow: research, a short plan requiring approval, focused implementation, automated validation, and an evidence-based final report. Keep feature-specific requirements out of this file.

Prove that the harness is reusable by delivering these features independently:

- `GET /api/health` returns HTTP 200 with `{"status":"ok"}`;
- invalid registrations return HTTP 400 and are not persisted, while valid registrations keep working.

Both features must follow the same repository-defined workflow and pass validation. Explain what belongs in `AGENTS.md` and what belongs only in an individual task prompt.
