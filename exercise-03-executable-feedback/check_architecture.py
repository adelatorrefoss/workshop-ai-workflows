"""Executable fitness function for controller dependency boundaries."""

import ast
from pathlib import Path


tree = ast.parse(Path("controller.py").read_text())
for node in ast.walk(tree):
    if isinstance(node, ast.ImportFrom) and node.module == "preferences_repository":
        raise SystemExit(
            "ARCHITECTURE FAILURE: controller.py imports the persistence adapter. "
            "Required flow: controller -> application service -> repository."
        )
print("architecture: controller boundary is valid")

