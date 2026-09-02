from pathlib import Path


source = Path("catalog.py").read_text()
for token in ("eval(", "exec(", "shell=True", "pickle.loads"):
    if token in source:
        raise SystemExit(f"security: forbidden construct found: {token}")
print("security: basic source policy passes")

