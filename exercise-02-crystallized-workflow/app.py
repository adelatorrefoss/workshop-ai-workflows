"""Small application on which the reusable workflow operates."""

import json
from typing import Any


USERS: list[dict[str, Any]] = []


def route(method: str, path: str, body: bytes = b"") -> tuple[int, dict]:
    if method == "GET" and path == "/users":
        return 200, {"users": USERS}
    if method == "POST" and path == "/users":
        payload = json.loads(body or b"{}")
        USERS.append(payload)
        return 201, payload
    return 404, {"error": "not found"}

