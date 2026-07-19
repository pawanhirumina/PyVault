from pathlib import Path
import secrets


CONFIG_DIR = Path.home() / ".config" / "pyvault"

SALT_FILE = CONFIG_DIR / "salt"


def get_salt():

    CONFIG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    if not SALT_FILE.exists():
        SALT_FILE.write_bytes(
            secrets.token_bytes(16)
        )

    return SALT_FILE.read_bytes()