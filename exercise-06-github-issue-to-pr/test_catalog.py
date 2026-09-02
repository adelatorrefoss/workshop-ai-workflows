import unittest

from catalog import list_products


class CatalogTests(unittest.TestCase):
    def test_lists_all_products(self) -> None:
        self.assertEqual(3, len(list_products()))

    def test_result_cannot_mutate_catalog_container(self) -> None:
        result = list_products()
        result.clear()
        self.assertEqual(3, len(list_products()))


if __name__ == "__main__":
    unittest.main()

