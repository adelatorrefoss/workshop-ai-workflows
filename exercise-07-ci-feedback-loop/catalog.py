"""Catalog candidate whose local checks do not cover the complete contract."""

PRODUCTS = [
    {"id": 1, "name": "Keyboard", "category": "Hardware"},
    {"id": 2, "name": "Editor", "category": "Software"},
    {"id": 3, "name": "Mouse", "category": "Hardware"},
]


def list_products(category: str | None = None) -> list[dict]:
    if category is None:
        return list(PRODUCTS)
    return [product for product in PRODUCTS if product["category"] == category]

