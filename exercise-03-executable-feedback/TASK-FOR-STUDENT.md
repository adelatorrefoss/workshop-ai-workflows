# Student challenge — Repair the application architecture

Refactor the registration feature so that it satisfies this dependency direction:

`controller → application service → repository interface → file repository`

The controller must no longer create or depend directly on file persistence. Introduce the required application boundary and dependency-injection wiring while preserving the public behavior of `POST /api/register`.

Do not weaken or bypass the executable architecture rule. The finished application must build, pass the architecture check, and make the responsibility of every layer clear.
