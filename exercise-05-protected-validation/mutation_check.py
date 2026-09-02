"""Small deterministic mutation check for the policy boundary."""

import access
import test_access
import unittest


def run_with(replacement) -> bool:
    original = access.can_publish
    access.can_publish = replacement
    try:
        suite = unittest.defaultTestLoader.loadTestsFromModule(test_access)
        return unittest.TextTestRunner(stream=open("/dev/null", "w")).run(suite).wasSuccessful()
    finally:
        access.can_publish = original


mutants = {
    "changed >= boundary to >": lambda reputation: reputation > 100,
    "changed threshold 100 to 99": lambda reputation: reputation >= 99,
}
survivors = [name for name, mutant in mutants.items() if run_with(mutant)]
if survivors:
    raise SystemExit(
        "MUTATION FAILURE: tests did not detect: " + ", ".join(survivors) +
        ". Improve tests around the policy boundary."
    )
print("mutation: all policy mutants were detected")

