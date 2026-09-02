import unittest

from app import route


class ExistingApplicationTests(unittest.TestCase):
    def test_users_endpoint(self) -> None:
        self.assertEqual((200, {"users": []}), route("GET", "/users"))

    def test_unknown_route(self) -> None:
        self.assertEqual(404, route("GET", "/missing")[0])


if __name__ == "__main__":
    unittest.main()

