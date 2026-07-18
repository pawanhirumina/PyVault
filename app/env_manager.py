from __future__ import annotations
from pathlib import Path
from platformdirs import user_config_dir
from dotenv import load_dotenv, set_key, get_key, dotenv_values

class EnvManager:
    def __init__(self, app_name: str = "PyVault", filename: str = "supabase.env"):
        self.config_dir = Path(user_config_dir(app_name))
        self.env_file = self.config_dir / filename

    def ensure(self):
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.env_file.touch(exist_ok=True)
        try:
            self.config_dir.chmod(0o700)
            self.env_file.chmod(0o600)
        except Exception:
            pass

    def save(self, key: str, value: str):
        self.ensure()
        set_key(str(self.env_file), key, value)
        load_dotenv(self.env_file, override=True)

    def get(self, key: str) -> str | None:
        self.ensure()
        return get_key(str(self.env_file), key)

    def load(self):
        self.ensure()
        if self.env_file.exists():
            load_dotenv(self.env_file, override=True)

    def all(self) -> dict:
        self.ensure()
        return dotenv_values(self.env_file)

    def clear(self):
        if self.env_file.exists():
            self.env_file.unlink()

env_manager = EnvManager()