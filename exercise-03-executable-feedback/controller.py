"""HTTP-shaped controller with a deliberate architecture violation."""

from preferences_repository import PreferencesRepository


repository = PreferencesRepository()


def put_preferences(user_id: str, payload: dict) -> tuple[int, dict]:
    theme = payload.get("theme")
    if theme not in {"light", "dark"}:
        return 400, {"error": "theme must be light or dark"}
    repository.save(user_id, theme)
    return 204, {}


def get_preferences(user_id: str) -> tuple[int, dict]:
    theme = repository.find(user_id)
    if theme is None:
        return 404, {"error": "preferences not found"}
    return 200, {"theme": theme}

