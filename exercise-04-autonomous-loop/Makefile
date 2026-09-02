.PHONY: test lint validate

test:
	python3 -m unittest -v

lint:
	python3 -m py_compile pricing.py test_pricing.py

validate: test lint

