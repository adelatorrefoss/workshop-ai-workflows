.PHONY: test lint architecture-test security-test contract-test validate ci-validate

test:
	python3 -m unittest -v test_catalog.py

lint:
	python3 -m py_compile catalog.py test_catalog.py ci_checks/test_contract.py

architecture-test:
	python3 scripts/check_architecture.py

security-test:
	python3 scripts/security_check.py

contract-test:
	python3 -m unittest -v ci_checks/test_contract.py

validate: test lint architecture-test

ci-validate: validate security-test contract-test
