import unittest

from catalog import list_products


class CatalogTests(unittest.TestCase):
    def test_lists_all_products_without_filter(self) -> None:
        self.assertEqual(3, len(list_products()))

    def test_filters_exact_category(self) -> None:
        self.assertEqual(2, len(list_products("Hardware")))

    def test_unknown_category_is_empty(self) -> None:
        self.assertEqual([], list_products("books"))


if __name__ == "__main__":
    unittest.main()

