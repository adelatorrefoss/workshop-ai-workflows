import json
import unittest

from app import USERS, route


class ApplicationTests(unittest.TestCase):
    def setUp(self) -> None:
        USERS.clear()

    def test_lists_users(self) -> None:
        self.assertEqual((200, {"users": []}), route("GET", "/users"))

    def test_creates_user(self) -> None:
        body = json.dumps({"name": "Ada"}).encode()
        self.assertEqual((201, {"name": "Ada"}), route("POST", "/users", body))


if __name__ == "__main__":
    unittest.main()

