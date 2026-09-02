"""Persistence adapter for user preferences."""

import sqlite3


class PreferencesRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            "CREATE TABLE preferences (user_id TEXT PRIMARY KEY, theme TEXT NOT NULL)"
        )

    def save(self, user_id: str, theme: str) -> None:
        self.connection.execute(
            "INSERT OR REPLACE INTO preferences VALUES (?, ?)", (user_id, theme)
        )
        self.connection.commit()

    def find(self, user_id: str) -> str | None:
        row = self.connection.execute(
            "SELECT theme FROM preferences WHERE user_id = ?", (user_id,)
        ).fetchone()
        return None if row is None else str(row[0])

