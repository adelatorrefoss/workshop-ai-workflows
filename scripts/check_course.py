"""Verify the complete teaching scaffold and its intentional start states."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
EXERCISES = [
    "exercise-01-workflow",
    "exercise-02-crystallized-workflow",
    "exercise-03-executable-feedback",
    "exercise-04-autonomous-loop",
    "exercise-05-protected-validation",
    "exercise-06-github-issue-to-pr",
    "exercise-07-ci-feedback-loop",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"scaffold failure: {message}")


def run(exercise: str, command: tuple[str, ...], expected: int, marker: str = "") -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=ROOT / exercise,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout + result.stderr
    require(result.returncode == expected, f"{exercise}: {' '.join(command)} returned {result.returncode}")
    require(not marker or marker in output, f"{exercise}: expected diagnostic {marker!r}")
    state = "expected red" if expected else "green"
    print(f"{exercise}: {state} ({' '.join(command)})")


for directory in EXERCISES:
    path = ROOT / directory
    require(path.is_dir(), f"missing {directory}")
    for filename in ("README.md", "AGENTS.md", "Makefile", "prompts"):
        require((path / filename).exists(), f"{directory} is missing {filename}")

root_readme = (ROOT / "README.md").read_text()
require("Module 7 — Workflows" in root_readme, "root README lacks module identity")
require("Codesai Training: Advanced AI-Assisted Development" in root_readme, "root README lacks course identity")

guarded = "\n".join((ROOT / name / "AGENTS.md").read_text().lower() for name in EXERCISES[2:])
for phrase in ("never weaken", "at most three", "never merge"):
    require(phrase in guarded, f"agent harness lacks guardrail: {phrase}")

run("exercise-01-workflow", ("make", "validate"), 0)
run("exercise-02-crystallized-workflow", ("make", "validate"), 0)
run("exercise-03-executable-feedback", ("make", "test"), 0)
run("exercise-03-executable-feedback", ("make", "architecture-test"), 2, "ARCHITECTURE FAILURE")
run("exercise-04-autonomous-loop", ("make", "validate"), 2, "FAILED (failures=1)")
run("exercise-05-protected-validation", ("make", "test"), 0)
run("exercise-05-protected-validation", ("make", "mutation-test"), 2, "MUTATION FAILURE")
run("exercise-06-github-issue-to-pr", ("make", "validate"), 0)
run("exercise-07-ci-feedback-loop", ("make", "validate"), 0)
run("exercise-07-ci-feedback-loop", ("make", "ci-validate"), 2, "FAILED (failures=1)")

print("course scaffold: all checks passed")

