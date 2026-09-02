# Protected-feedback workflow

Run `make validate` and fix the engineering weakness it identifies. Validation mechanisms are constraints, not obstacles. Never delete or skip tests, disable checks, edit `mutation_check.py`, lower thresholds, or make commands ignore failures unless the user explicitly requests a policy change. Prefer improving production and test design. Use at most three validation attempts and report each correction.

