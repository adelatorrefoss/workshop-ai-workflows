.PHONY: test lint mutation-test validate

test:
	python3 -m unittest -v

lint:
	python3 -m py_compile access.py test_access.py mutation_check.py

mutation-test:
	python3 mutation_check.py

validate: test lint mutation-test

