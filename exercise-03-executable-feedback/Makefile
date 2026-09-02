.PHONY: test lint architecture-test validate

test:
	python3 -m unittest -v

lint:
	python3 -m py_compile controller.py preferences_repository.py test_preferences.py

architecture-test:
	python3 check_architecture.py

validate: test lint architecture-test

