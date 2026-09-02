"""Pricing rules with a deliberately incorrect premium discount."""


def total(price: int, quantity: int, premium: bool) -> int:
    if price < 0 or quantity < 1:
        raise ValueError("price must be non-negative and quantity must be positive")
    subtotal = price * quantity
    if premium:
        return subtotal - 5
    return subtotal

