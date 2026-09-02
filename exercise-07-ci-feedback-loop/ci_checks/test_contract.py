import unittest

from catalog import list_products


class PublicContractTests(unittest.TestCase):
    def test_category_filter_is_case_insensitive(self) -> None:
        self.assertEqual(2, len(list_products("hardware")))

    def test_filter_does_not_leak_internal_container(self) -> None:
        result = list_products("Hardware")
        result.clear()
        self.assertEqual(2, len(list_products("Hardware")))


if __name__ == "__main__":
    unittest.main()

