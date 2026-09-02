"""Tiny HTTP application used by the workflow exercises."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def route(method: str, path: str, body: bytes = b"") -> tuple[int, dict]:
    if method == "GET" and path == "/users":
        return 200, {"users": []}
    return 404, {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def _respond(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        status, payload = route(self.command, self.path, self.rfile.read(length))
        encoded = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    do_GET = _respond
    do_POST = _respond

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()

