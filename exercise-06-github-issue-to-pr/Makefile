.PHONY: test lint architecture-test validate

test:
	python3 -m unittest -v

lint:
	python3 -m py_compile catalog.py test_catalog.py

architecture-test:
	python3 scripts/check_architecture.py

validate: test lint architecture-test

