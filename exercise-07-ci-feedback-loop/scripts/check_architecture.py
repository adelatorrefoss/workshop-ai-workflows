from pathlib import Path


source = Path("catalog.py").read_text()
for forbidden in ("requests", "sqlite3", "subprocess"):
    if f"import {forbidden}" in source:
        raise SystemExit(f"architecture: catalog domain must not import {forbidden}")
print("architecture: catalog dependencies are valid")

