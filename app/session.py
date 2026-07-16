from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from platformdirs import user_config_dir

APP_NAME = "VaultPy"

CONFIG_DIR = Path(user_config_dir(APP_NAME))
SESSION_FILE = CONFIG_DIR / "session.json"


def save_session(session: dict[str, Any]) -> None:
    """Save the current session to disk."""

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with SESSION_FILE.open("w") as file:
        json.dump(session, file, indent=4, default=str)


def load_session() -> dict[str, Any] | None:
    """Load the saved session."""

    if not SESSION_FILE.exists():
        return None

    with SESSION_FILE.open() as file:
        return json.load(file)


def clear_session() -> None:
    """Delete the saved session."""

    if SESSION_FILE.exists():
        SESSION_FILE.unlink()


def has_session() -> bool:
    """Return True if a saved session exists."""

    return SESSION_FILE.exists()