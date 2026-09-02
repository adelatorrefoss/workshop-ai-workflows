import unittest

from access import can_publish


class AccessTests(unittest.TestCase):
    def test_high_reputation_can_publish(self) -> None:
        self.assertTrue(can_publish(200))

    def test_low_reputation_cannot_publish(self) -> None:
        self.assertFalse(can_publish(10))


if __name__ == "__main__":
    unittest.main()

