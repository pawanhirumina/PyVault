from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from platformdirs import user_config_dir


class SessionManager:
    def __init__(self, app_name: str = "pyvault") -> None:
        self.config_dir = Path.home() / ".config" / app_name
        self.session_file = self.config_dir / "session.json"

    def save(self, session: dict[str, Any]) -> None:
        """Save the current session to disk."""

        self.config_dir.mkdir(parents=True, exist_ok=True)

        with self.session_file.open("w") as file:
            json.dump(session, file, indent=4)

    def load(self) -> dict[str, Any] | None:
        """Load the saved session."""

        if not self.session_file.exists():
            return None

        with self.session_file.open() as file:
            return json.load(file)

    def clear(self) -> None:
        """Delete the saved session."""

        if self.session_file.exists():
            self.session_file.unlink()

    def exists(self) -> bool:
        """Return True if a session exists."""

        return self.session_file.exists()


session_manager = SessionManager()