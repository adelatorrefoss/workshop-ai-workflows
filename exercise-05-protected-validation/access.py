"""Access policy whose boundary needs strong tests."""


def can_publish(reputation: int) -> bool:
    """A contributor may publish at a reputation of 100 or higher."""
    return reputation >= 100

