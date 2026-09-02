import unittest

from pricing import total


class PricingTests(unittest.TestCase):
    def test_regular_customer_pays_full_price(self) -> None:
        self.assertEqual(200, total(100, 2, False))

    def test_premium_customer_gets_ten_percent_discount(self) -> None:
        self.assertEqual(180, total(100, 2, True))

    def test_invalid_quantity_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            total(100, 0, False)


if __name__ == "__main__":
    unittest.main()

