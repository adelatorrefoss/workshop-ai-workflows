import unittest

import controller
from preferences_repository import PreferencesRepository


class PreferencesTests(unittest.TestCase):
    def setUp(self) -> None:
        controller.repository = PreferencesRepository()

    def test_saves_and_loads_theme(self) -> None:
        self.assertEqual((204, {}), controller.put_preferences("ada", {"theme": "dark"}))
        self.assertEqual((200, {"theme": "dark"}), controller.get_preferences("ada"))

    def test_rejects_invalid_theme(self) -> None:
        self.assertEqual(400, controller.put_preferences("ada", {"theme": "blue"})[0])


if __name__ == "__main__":
    unittest.main()

