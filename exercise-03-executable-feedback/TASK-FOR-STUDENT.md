# Student task — Repair a design using executable architecture feedback

## Your task

Use the failing architecture check to refactor the registration flow without changing its externally visible behavior.

The required dependency direction is:

`controller → application service → repository interface → file repository`

## What to do

1. Run `make build` and confirm that compilation passes.
2. Run `make architecture-test` and capture the intentional `ARCHITECTURE FAILURE` message.
3. Launch Codex and paste `prompts/implement.md`.
4. Let Codex inspect the failure and make the smallest refactor that satisfies the executable rule.
5. Review the resulting dependencies and run `make validate`.

## Constraints

- Preserve `POST /api/register` behavior.
- Do not delete, weaken, bypass, or rewrite the architecture check to make it pass.
- Controllers must not depend directly on concrete file persistence.

## Done when

- `make validate` passes.
- The code follows the required dependency direction.
- Registration behavior remains intact.
- You can explain what the executable failure revealed that a prose-only instruction might not have enforced.
