.PHONY: test lint validate

test:
	python3 -m unittest -v

lint:
	python3 -m py_compile app.py test_app.py

validate: test lint

