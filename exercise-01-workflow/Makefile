.PHONY: test validate

test:
	python3 -m unittest -v

validate: test
	python3 -m py_compile app.py test_app.py

