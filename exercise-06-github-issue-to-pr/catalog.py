"""Product catalog used by the GitHub workflow exercises."""

PRODUCTS = [
    {"id": 1, "name": "Keyboard", "category": "hardware"},
    {"id": 2, "name": "Editor", "category": "software"},
    {"id": 3, "name": "Mouse", "category": "hardware"},
]


def list_products() -> list[dict]:
    return list(PRODUCTS)

